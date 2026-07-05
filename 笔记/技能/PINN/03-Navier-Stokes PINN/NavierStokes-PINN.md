---
source: Raissi 2019 论文 §4 (NSF) + Jin 2021 NeurIPS (NSFnets) + 知识库重组
type: study-note
subject: PINN
date: 2026-07-02
keywords: [pinn, navier-stokes, ldc, vortex, pressure-poisson]
tags: [study-note, pinn]
---

# Navier-Stokes PINN —— Burgers 升级到 2D 方腔流

#pinn #navier-stokes #fluid

> 这是 PINN 在流体上的应用第一战——方腔流（Lid-Driven Cavity, LDC）。你流体的先验直觉在这章是最大的杠杆：训练完直接看中心涡位置、壁面附近边界层——这是 PINN 调参的验收力。前置：[[笔记/技能/PINN/02-Burgers方程PINN/Burgers-PINN|Burgers PINN]]。

## 一·不可压 Navier–Stokes 方程（PINN 形式）

一·**PDE**（2D 不可压，无量纲化）：
$$
\partial_t u + u\,\partial_x u + v\,\partial_y u = -\partial_x p + \frac{1}{Re}\,(\partial_{xx} u + \partial_{yy} u), \\
\partial_t v + u\,\partial_x v + v\,\partial_y v = -\partial_y p + \frac{1}{Re}\,(\partial_{xx} v + \partial_{yy} v), \\
\partial_x u + \partial_y v = 0 \quad (\text{连续性})
$$

二·**PINN 处理 NS 的两种参数化**（你需要认得两种）：

  1. **原始变量**（velocity-pressure, VP）：网络输出 $(u, v, p)$，三个方程一起做残差。优点：物理直观；缺点：连续性 $\nabla \cdot \mathbf{u} = 0$ 是约束，软约束常常不严格满足。
  2. **流函数-涡量**（vorticity-stream function, vSF）：用流函数 $\psi$ 满足 $\nabla \cdot \mathbf{u} = 0$ 自动（$u = \partial_y \psi, v = -\partial_x \psi$）；网络输出 $(\psi, \omega)$，$\omega = \partial_x v - \partial_y u$。优点：连续性天然满足，2D 不可压主流做；缺点：难推广到 3D。

三·**网络输出结构**：
```python
# VP 形式
model_vp = nn.Sequential(
    nn.Linear(3, 50), nn.Tanh(),       # 输入 (x, y, t) 3 维
    nn.Linear(50, 50), nn.Tanh(),
    nn.Linear(50, 50), nn.Tanh(),
    nn.Linear(50, 3)                   # 输出 (u, v, p) 3 维
)
```

> [!note] 核心理解
> 选 VP 还是 vSF 取决于你的目标：==正问题、2D、要严格无散== → vSF；==逆问题、3D、压力是观测或未知量== → VP。方腔流入门推荐 VP（Raissi 原文用），但 vSF 收敛更稳——这是 NSFnets (Jin 2021) 给的工程经验。

---

## 二·方腔流问题设定

一·**几何**：2D 方腔 $\Omega = [0, 1]^2$，上方 $y=1$ 是「盖板」以 $u=1, v=0$ 滑移驱动流动，其余三壁 $u = v = 0$（无滑移）。
   ```
   ┌─────────────────←  ←  ←  ←  ←  ←
   │   (盖板 u=1, v=0)                  ↑ y
   │                                    │
   │      ←主涡中心                      │
   │                                    │
   │                                    └──→ x
   ┌─────────────────────────────────
   u = v = 0  （三壁无滑移）
   ```

二·**关键物理量**（你熟，调参时的「眼睛」）：
  1. **主涡中心位置**：稳态时约 $(0.62, 0.62)$（Re=100 经典基准，Ghia 1982 表）——判 PINN 学对了没最直接。
  2. **次涡**：Re 高时左下、右下出现小次涡——比主涡难学，验高级收敛性。
  3. **壁面边界层厚度**：$\delta \sim 1/\sqrt{Re}$——网络宽度不够学不到边界层。
  4. **压力场**：盖板下方应为高压、对角线另一端低压——画 $p$ 等值线核对。

三·**稳态 vs 非定常**：
  1. **稳态**（Re=100 以下）：去掉 $\partial_t$ 项，输入维降到 2（`x, y`）。**入门第一步**。
  2. **非定常**：加 `t`，输入 3 维。Re 超临界（Re > ~8000）后流动失稳振荡。

> [!warning] 易错
> 别一上就跑非定常——**先稳态 Re=100** 跑通，再扩到非定常 / 高 Re。稳态是去掉 $\partial_t$ 项、删 t 维，输入从 3 维降 2 维，损失不出现 $\mathrm{MSE}_{ic}$——所有事项简化。

---

## 三·NS PINN 损失与残差构造（VP 形式）

一·**残差构造**（autograd 三件套扩展到矢量场）：
```python
xy = torch.rand(N_f, 2, requires_grad=True)            # (N_f, 2)
out = model_vp(xy)                                      # (N_f, 3)
u, v, p = out[:, 0:1], out[:, 1:2], out[:, 2:3]

# 一阶
g1 = torch.autograd.grad(out, xy, torch.ones_like(out), create_graph=True)[0]
u_x, u_y = g1[:, 0:1], g1[:, 1:2]   # 注：u 对 x、y 都要，下同
v_x, v_y = g1[:, 0:1]*0, g1[:, 1:2]*0   # ← 实际分别对 v、对独立分量求导；省略正文给标准写法

# 连续性残差：r_div = u_x + v_y

# 动量方程残差：r_u = u*u_x + v*u_y + p_x - (1/Re)*(u_xx + u_yy)
# 类似 r_v
```

> [!warning] 易错（autograd 矢量场求导）
> 一个 detail 坑：==对 $u$ 求 $\partial u/\partial x$ 时 `grad_outputs` 必须把其他分量置零==：
> ```python
> u_x = torch.autograd.grad(
>     out, xy, grad_outputs=torch.cat([torch.ones_like(u), torch.zeros_like(v), torch.zeros_like(p)], dim=1),
>     create_graph=True
> )[:, 0:1]
> ```
> 否则 grad 会把 $u, v, p$ 三个分量的偏导**叠加**。建议**封装一个 `d_u_dx(u, xy)` helper**，三层以上必须函数化。

二·**损失**：
$$
\mathcal{L} = \lambda_p (\|r_u\|^2 + \|r_v\|^2) + \lambda_c \|r_{div}\|^2
+ \lambda_b \mathrm{MSE}_{bc}(u, v \text{ 在壁面上的偏差})
$$
其中 $r_{div} = \partial_x u + \partial_y v$ 把连续性作软约束。

三·**$\lambda$ 平衡心得**：
  1. 连续性 $\lambda_c$ 通常给较大（如 10）——$r_{div}$ 容易被忽略。
  2. 壁面 BC $\lambda_b$ 也给 10~50——无滑移核心。
  3. 动量项 $\lambda_p$ 默认 1 起步。

> [!note] 核心理解
> ==连续性 + 动量 + 壁面 BC== 三条软约束同时压住网络，让网络同时满足「质量守恒、动量守恒、边界无滑移」。这三项的相对权重就是 PINN 调参的本质——这是为什么 ==NS PINN 比 Burgers 难==：Burgers 只 1 分量 1 BC；NS 是 3 分量、3 方程、4 壁面，自由度与约束度都翻 3~4 倍。

---

## 四·方腔流 PINN 完整骨架（DeepXDE 简化版）

```python
import deepxde as dde
import numpy as np

Re = 100
geom = dde.geometry.Rectangle([0, 0], [1, 1])

def boundary(X, on_boundary):  return on_boundary
def boundary_top(X, on_boundary):   return on_boundary and np.isclose(X[1], 1)
def boundary_other(X, on_boundary): return on_boundary and not np.isclose(X[1], 1)

# 壁面 BC
bc_u_top   = dde.icbc.DirichletBC(geom, lambda X: 1, boundary_top, component=0)   # u=1 顶
bc_v_top   = dde.icbc.DirichletBC(geom, lambda X: 0, boundary_top, component=1)
bc_wall_u  = dde.icbc.DirichletBC(geom, lambda X: 0, boundary_other, component=0) # u=0 其他
bc_wall_v  = dde.icbc.DirichletBC(geom, lambda X: 0, boundary_other, component=1)

def ns_pde(X, U):
    u, v, p = U[:, 0:1], U[:, 1:2], U[:, 2:3]
    # 一阶（DeepXDE 封装 jacobian）
    u_x = dde.grad.jacobian(U, X, i=0, j=0)
    u_y = dde.grad.jacobian(U, X, i=0, j=1)
    v_x = dde.grad.jacobian(U, X, i=1, j=0)
    v_y = dde.grad.jacobian(U, X, i=1, j=1)
    p_x = dde.grad.jacobian(U, X, i=2, j=0)
    p_y = dde.grad.jacobian(U, X, i=2, j=1)
    # 二阶
    u_xx = dde.grad.hessian(U, X, i=0, j=0); u_yy = dde.grad.hessian(U, X, i=0, j=1)
    v_xx = dde.grad.hessian(U, X, i=1, j=0); v_yy = dde.grad.hessian(U, X, i=1, j=1)
    
    r_u = u * u_x + v * u_y + p_x - (1/Re) * (u_xx + u_yy)
    r_v = v * v_x + u * v_y + p_y - (1/Re) * (v_xx + v_yy)
    r_div = u_x + v_y
    return [r_u, r_v, r_div]

data = dde.data.PDE(
    geom, ns_pde, [bc_u_top, bc_v_top, bc_wall_u, bc_wall_v],
    num_domain=10000, num_boundary=1000
)
net = dde.nn.FNN([2] + [50]*6 + [3], "tanh", "Glorot uniform")
model = dde.Model(data, net)
model.compile("adam", lr=1e-3)
model.train(iterations=20000)
model.compile("L-BFGS"); model.train()
```

---

## 五·诊断与可视化（验收 = 调参的眼睛）

一·**必画的四张图**：
```python
# 网格采样
x = y = np.linspace(0, 1, 80)
X, Y = np.meshgrid(x, y)
xy = np.c_[X.ravel(), Y.ravel()]
U = model.predict(xy)
u, v = U[:, 0].reshape(X.shape), U[:, 1].reshape(X.shape)
p   = U[:, 2].reshape(X.shape)

# (1) 速度模 |u| 等高
speed = np.sqrt(u**2 + v**2)
plt.contourf(X, Y, speed, 30); plt.colorbar()
# (2) 流线 streamplot（★看涡位）
plt.streamplot(X, Y, u, v, density=1.5)
# (3) 矢量场 quiver
plt.quiver(X, Y, u, v)
# (4) 压力等值线
plt.contour(X, Y, p, 20)
```

二·**和 Ghia 1982 基准对照**（最硬验收）：
  1. 中心涡位置应在 ~(0.62, 0.62)（Re=100）。
  2. 沿 $x=0.5$ 剖面 $u(y)$ 与 Ghia 表对比——经典 25 点对照。
  3. 误差用 L2 范数或相对误差 $\|u_{pred}-u_{FEM}\|_2 / \|u_{FEM}\|_2$。

> [!note] 核心理解
> 判定方腔流 PINN 调好了的最高标准：==画 streamplot，主涡中心在 (0.62, 0.62) 附近、流线光滑闭合、无发散==。这条不动笔你也看出来——你的流体直觉直接接入了 PINN 验收。这是 PINN 对你的最大杠杆点。

---

## 六·边界 / 易错附录

  1. ==输入维对！稳态是 2 维（x,y），非定常是 3 维（x,y,t）==，配 `Linear(2 / 3, ...)`。
  2. ==矢量场 autograd 求单分量偏导 `grad_outputs` 要 one-hot==（其他分量置零）。
  3. 连续性 $\nabla \cdot \mathbf{u}$ 是 PINN 痛点：收敛不稳时优先调大 $\lambda_c$ 或改用 vSF 形式。
  4. ==压力参考点==：NS 压力有任意常数自由度，需在 PDE + 1 点 $p$ 强制（如 $p(0, 0) = 0$），否则压力场平移自由让训练飘。
  5. Re 不能贪大：Re=100 跑通再升 Re=1000、4000，每步配点加密 + 网络加宽。
  6. 高 Re 主涡漂移或不对称 → 自适应配点（残差大处加密）或 NTK-based 权重（研 Wang 2022）。

---

## 七·向 vorticity-stream function 升级（推荐下一步）

VP 跑稳后想更严格无散，转 vSF：

```python
out = model(xyt)                # (ψ, ω)
psi, omega = out[:, 0:1], out[:, 1:2]
u = torch.autograd.grad(psi, xyt, ..., create_graph=True)[0][:, 1:2]    # ψ_y → u
v = -torch.autograd.grad(psi, xyt, ..., create_graph=True)[0][:, 0:1]   # -ψ_x → v
# 连续性天然满足，不再需要 r_div
# 涡量方程：ω_t + u*ω_x + v*ω_y = (1/Re) * (ω_xx + ω_yy)
# 约束 ω = v_x - u_y （涡量定义）
```

优点：网络只输出 2 个量、连续性自动满足、训练更稳。缺点：3D 不存在 vSF（涡量是矢量）。

---

## 速记卡 / 一句话总结

- 2D NS 三方程：双动量 + 连续性；PINN 用 VP（u,v,p）或 vSF（ψ,ω）参数化。
- ==稳态 Re=100 方腔流是 NS PINN 入门战==：去 $\partial_t$、输入降 2 维、`num_domain=10000, num_boundary=1000`。
- ==验收靠 streamplot 看中心涡==：Re=100 应在 ~(0.62, 0.62)。
- ==矢量场 autograd 求 $u$ 对 $x$ 的偏导，`grad_outputs` 要 one-hot $u$==。
- ==压力必须设参考点== $p(0,0)=0$，否则平移自由让训练飘。
- $\lambda_c$（连续性）与 $\lambda_b$（壁面）起步给 10~50，动量 $\lambda_p = 1$。
- 硬验收：和 Ghia 1982 表对比剖面 $u(y)$、相对 L2 误差。
- 升级路径：VP 跑通后转 vSF，无散更严格、训练更稳但只限 2D。
- 调子规则：Re 从 100 → 1000 → 4000 阶梯升，每步配点加密 + 网络加宽。

---

## Related Notes
- [[笔记/技能/PINN/02-Burgers方程PINN/Burgers-PINN|Burgers-PINN]]
- [[笔记/技能/PINN/04-反问题与参数识别/反问题PINN|反问题PINN]]
- [[assets/LLM上下文/PINN/PINN学习 MOC|PINN 学习 MOC]]