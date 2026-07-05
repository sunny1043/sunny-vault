---
source: Raissi 2019 论文 §3 + DeepXDE 官方 Burgers 例 + PyTorch 自实现参考 Ben Moseley tutorial
type: study-note
subject: PINN
date: 2026-07-02
keywords: [pinn, burgers, deepxde, pytorch, shock]
tags: [study-note, pinn]
---

# Burgers 方程 PINN —— 第一个跑通的 demo + 80 行自实现

#pinn #burgers #deepxde

> 这是阶段 C 的关键动作 + 阶段 D 的产出。Burgers 是 PINN 的「Hello, World」：一维、有解析解基准、能看到激波——所有 PINN 现象都能在这里观察。前置：[[笔记/技能/PINN/01-PINN原理/PINN三件套与残差损失|PINN 三件套]]。

## 一·Burgers 方程与配点设定

一·**PDE**（粘性 Burgers，1D）：
$$
\partial_t u(x, t) + u\,\partial_x u(x, t) - \frac{\nu}{\pi}\,\partial_{xx} u(x, t) = 0,
\quad x \in [-1, 1],\ t \in [0, 1]
$$

二·**为什么用 Burgers**：
  1. 一维 → 网络输入只 2 维 `(x, t)`，最小可掌控。
  2. 同时含**对流非线性**（$u u_x$）+ **扩散**（$u_{xx}$）→ 是 NS 的简化 1D 版。
  3. ==有解析解==（Cole-Hopf 变换），可直接对照训练误差。

三·**初始条件 IC**：
$$
u(x, 0) = -\sin(\pi x)
$$

四·**边界条件 BC**：周期性 $u(-1, t) = u(1, t)$，或 Dirichlet $u(\pm 1, t) = 0$（DeepXDE 默认用前者）。

五·**关键现象**：随 $t$ 增加，初始正弦波形被对流**陡化**，在 $t \approx 0.3$ 附近形成类激波结构，粘性随后抹平——这正是 PINN 的**谱偏置痛点**最显眼的地方。

> [!note] 核心理解
> Burgers 的「**陡化 + 耗散**」机制你应当熟悉：非线性对流让波形高处跑得快（$u u_x$ 类似 SHM），波形前沿变陡；粘性项 $u_{xx}$ 把陡变抹平。PINN 学得到陡变吗？观察 $t = 0.3 \sim 0.5$ 的预测——这是判 PINN 调参成功与否的最直观验收点。

---

## 二·跑通 DeepXDE 官方 demo（阶段 C 主任务）

### 1. 安装与最小代码

```bash
pip install deepxde torch matplotlib
```

```python
import deepxde as dde
from deepxde.backend import torch          # 用 PyTorch 后端

# 1. 定义 PDE 残差（DeepXDE 调用约定：输入 X, 输出 u）
def burgers_pde(X, u):
    du_X = dde.grad.jacobian(u, X, i=0, j=0)    # ∂u/∂x
    du_t = dde.grad.jacobian(u, X, i=0, j=1)    # ∂u/∂t
    du_xx = dde.grad.hessian(u, X, i=0, j=0)    # ∂²u/∂x²
    return du_t + u * du_X - (1 / dde.pi) * du_xx

# 2. 几何 + 时间域
geom = dde.geometry.Interval(-1, 1)
timedomain = dde.geometry.TimeDomain(0, 1)
geomtime = dde.geometry.GeometryXTime(geom, timedomain)

# 3. BC / IC
bc = dde.icbc.DirichletBC(geomtime, lambda X: 0, lambda _, on_boundary: on_boundary)
ic = dde.icbc.IC(geomtime, lambda X: -np.sin(np.pi * X[:, 0:1]), lambda _, on_initial: on_initial)

# 4. 数据对象
data = dde.data.TimePDE(
    geomtime, burgers_pde, [bc, ic],
    num_domain=2500, num_boundary=80, num_initial=160
)

# 5. 网络 + 训练
net = dde.nn.FNN([2] + [40] * 4 + [1], "tanh", "Glorot uniform")
model = dde.Model(data, net)
model.compile("adam", lr=1e-3)
model.train(iterations=15000)
model.compile("L-BFGS")            # ← Adam 后切 L-BFGS 二次精调
model.train()
```

### 2. 改参验收清单（5 组必做）

> [!warning] 不能只跑通 demo。==过得了这 5 组才叫入门==，每组画对比图记录现象。

  1. `num_domain` = 500 / 2500 / 10000：配点加密收敛变好还是震荡？
  2. `num_initial` = 16 / 160 / 800：IC 配点不足会让 $t$ 较大处偏离吗？
  3. 网络宽 20 / 40 / 80、深 3 / 5 / 8：宽深比不同，残差降速差异？
  4. 切 L-BFGS / 不切：Adam 后是否需要二阶优化？loss 量级差几倍？
  5. 去掉 BC / 去掉 IC / 去掉 PDE：逐项去掉，看哪种「训练崩盘」最彻底——识破哪项是骨架。

### 3. 取预测 + 画时空图

```python
x = np.linspace(-1, 1, 200); t = np.linspace(0, 1, 100)
X, T = np.meshgrid(x, t)
xt = np.column_stack([X.ravel(), T.ravel()])
u_pred = model.predict(xt).reshape(T.shape)

import matplotlib.pyplot as plt
plt.pcolormesh(X, T, u_pred, shading='auto'); plt.colorbar(label="u")
plt.xlabel("x"); plt.ylabel("t"); plt.title("Burgers PINN 解")
plt.savefig("burgers_pinn.png", dpi=150)
```

---

## 三·80 行纯 PyTorch 自实现 Burgers PINN（阶段 D 产出）

阶段 D 的目标：不靠 DeepXDE，亲手写一遍「三件套 + 训练循环」。这是从「调库」到「真懂」一跃。

```python
import torch, torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

torch.manual_seed(0); np.random.seed(0)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
NU = 1 / np.pi                  # 粘性参数 ν/π

# ───────── 网络 ─────────
model = nn.Sequential(
    nn.Linear(2, 40), nn.Tanh(),
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 1)
).to(device)

# ───────── 配点 ─────────
N_f, N_b, N_i = 8000, 200, 200
xf = torch.rand(N_f, 2, device=device) * torch.tensor([2., 1.]) + torch.tensor([-1., 0.])
xf.requires_grad_(True)                                  # 域内配点（要 autograd）
xb  = torch.rand(N_b, 1, device=device)                  # BC 样 t ∈ [0,1]
xi  = torch.rand(N_i, 1, device=device) * 2 - 1          # IC 样 x ∈ [-1,1]
u_i = -torch.sin(np.pi * xi)                              # IC：-sin(πx)

# ───────── 损失函数 ─────────
def pde_residual(u, xt):
    g1 = torch.autograd.grad(u, xt, torch.ones_like(u), create_graph=True)[0]
    u_x, u_t = g1[:, 0:1], g1[:, 1:2]
    g2 = torch.autograd.grad(u_x, xt, torch.ones_like(u_x), create_graph=True)[0]
    u_xx = g2[:, 0:1]
    return u_t + u * u_x - NU * u_xx

def loss_fn():
    r = pde_residual(model(xf), xf)                      # PDE 残差
    mse_pde = (r**2).mean()
    # BC: u(±1, t) = 0
    x_b = torch.cat([torch.ones(N_b//2, 1), -torch.ones(N_b//2, 1)], 0).to(device)
    t_b = xb.repeat(2, 1)[:N_b]
    bc_in = torch.cat([x_b, t_b], 1)
    mse_bc = (model(bc_in)**2).mean()
    # IC: u(x, 0) = -sin(πx)
    ic_in = torch.cat([xi, torch.zeros_like(xi)], 1)
    mse_ic = ((model(ic_in) - u_i)**2).mean()
    return mse_pde + 10 * mse_bc + 10 * mse_ic, mse_pde, mse_bc, mse_ic   # λ_b=λ_i=10

# ───────── 训练 ─────────
opt = torch.optim.Adam(model.parameters(), lr=1e-3)
for step in range(20000):
    opt.zero_grad()
    loss, lp, lb, li = loss_fn()
    loss.backward(); opt.step()
    if step % 1000 == 0:
        print(f"step {step:5d}  L={loss:.3e}  pde={lp:.3e} bc={lb:.3e} ic={li:.3e}")

# ───────── 画图 ─────────
model.eval()
with torch.no_grad():
    x = np.linspace(-1, 1, 200); t = np.linspace(0, 1, 100)
    X, T = np.meshgrid(x, t)
    xt = torch.tensor(np.c_[X.ravel(), T.ravel()], dtype=torch.float32, device=device)
    U = model(xt).cpu().numpy().reshape(T.shape)
plt.pcolormesh(X, T, U, shading='auto'); plt.colorbar()
plt.savefig("burgers_pure_pinn.png", dpi=150)
```

> [!tip] 补充
> 这份代码就是 Ben Moseley + Raissi 风格的最小骨架。把它当**你 GitHub 上传的最小 repo 的主程序**；阶段 D 改改注释、加 `README.md` 写三件套解释，就能交。

---

## 四·调参心得（实验式知识，非论文给）

> [!tip] 补充（这些不是 Raissi 论文原文给，是社区经验，标注区分）

一·**Adam → L-BFGS 二段式**：Adam 探索 + 收敛到次优，L-BFGS 二阶法再精修——DeepXDE 默认这套，自实现可参考 `model.train()` Adam 后再切 `torch.optim.LBFGS`。

二·**BC/IC 权重 10~100**：起步就让 BC/IC 主导，否则网络会「先拟合 PDE 残差零解 $u \equiv 0$」骗自己。

三·**配点 4 倍网络宽度规则**：$N_f \approx$ 网络宽度的 4 倍起步、训练后期对残差大处重采样（自适应 RAR / R3i，DeepXDE 有 `dde.callbacks.PDEPointRemovalCallback`），但**入门先别上**，先把均匀配点跑通。

四·**激波区难收敛是 PINN 通病**：**缓解用 causal training**（Wang 2022, *When and Why PINN fail to train*），按时间因果分段加权——属于进阶，认得即可。

> [!warning] 易错（自实现版）
> - `xf.requires_grad_(True)` **不是** `xf.requires_grad = True`——后者是赋值会触发警告（PyTorch 张量内部 API 改了）。
> - BC/IC 输入不能复用 `xf`（它已 `requires_grad=True`）：独立建 tensor，放进 `with torch.no_grad()` 块更稳。
> - 误差不能只看 loss：必须画时空图、和解析解比 L2 误差，否则残差降到 1e-3 但 t>0.5 处全跑偏也发现不了。

---

## 五·验收标准（吃透 Burgers 后的判定）

  1. ≥ 能解释 `pde_residual` 每行的物理意义。
  2. ≥ 5 组改参实验每组写出一句结论，存在 `notes_burgers.md`。
  3. ≥ 自实现 80 行版能跑通，画出 $u(x, t)$ 图。
  4. ≥ 在 $t = 0.5$ 处剖出 $u$ vs $x$ 曲线，与解析解对比报告 L2 误差。
  5. ≥ 计算 L2 误差的代码能独立写出来。

> [!note] 核心理解
> 吃透 Burgers PINN = 80% 的 PINN 你都会了——Burgers 集齐了「非线性对流 + 扩散 + 一/二阶导 + BC/IC」全部要素。从 Burgers 到 2D NS 只是「输入 2 维 → 3 维、输出 1 维 → 多分量、加压力项」的扩展，骨架不变。

---

## 速记卡 / 一句话总结

- Burgers：$u_t + u\,u_x - (\nu/\pi)\,u_{xx} = 0$，IC $-\sin(\pi x)$，域 $x\in[-1,1], t\in[0,1]$。
- ==Burgers 是 PINN「Hello, World」==：一维、有解析解、能看到激波。
- ==DeepXDE 5 组改参验收==：`num_domain` / 网络 / Adam→L-BFGS / 切除各项 loss——这才叫跑通 demo。
- ==自实现 80 行==：阶段 D 的目标，把三件套全摸过一遍。
- ==谱偏置最显眼位置 ==：$t \approx 0.3\sim 0.5$ 激波区，PINN 最容易崩。
- Adam → L-BFGS 二段式 + BC/IC 权重 10~100，是默认起步配置。
- 自实现 4 个坑：`requires_grad_` 用方法不是赋值、BC/IC 独立 tensor、误差看图不只看 loss、和解析解比 L2。
- 吃透 Burgers = 80% 的 PINN 都会了；2D NS 只是 +输入维 +输出分量。

---

## Related Notes
- [[笔记/技能/PINN/01-PINN原理/PINN三件套与残差损失|PINN 三件套与残差损失]]
- [[笔记/技能/PINN/03-Navier-Stokes PINN/NavierStokes-PINN|Navier-Stokes PINN]]
- [[assets/LLM上下文/PINN/PINN学习 MOC|PINN 学习 MOC]]