---
source: 综合（PyTorch 官方文档 + 入门共识；为 PINN autograd 落地）
type: study-note
subject: Python
date: 2026-07-02
keywords: [pytorch, tensor, autograd, training-loop, pinn]
tags: [study-note, python]
---

# PyTorch 基础与自动微分（autograd）

#python #pytorch #autograd

> 这一章是从 NumPy 走到 PINN 的桥。PINN 让 PDE 进入损失，靠的是 ==autograd== 把输出对输入求任意阶偏导——这是 PyTorch 的核心机制，不会它就写不了 PINN 残差。

## 一·`torch.tensor`：会算梯度的 NumPy 数组

一·**定义**：`torch.tensor` 是 PyTorch 的核心数据结构——一个 N 维数值数组，类似 NumPy `ndarray`，但额外支持 **GPU 加速** 与 **自动微分**（autograd）。

二·**创建与基本属性**：
```python
import torch
x = torch.tensor([1.0, 2.0, 3.0])            # 1D
A = torch.zeros(3, 4)
B = torch.ones(2, 2)
R = torch.rand(100, 2)                       # PINN 配点常这么造
x.dtype     # torch.float32（默认）
x.device    # cpu / cuda
x.shape     # torch.Size([3])
```

三·**与 NumPy 互转（PINN 数据常在两边过手）**：
```python
import numpy as np
t = torch.from_numpy(np_array)      # 共享内存（改一个另一个改）
n = t.numpy()                       # 反向同理
```

四·**核心理解**：
> [!note] 核心理解
> PyTorch tensor 把「**会算梯度**」做成一等能力：在 tensor 上设 `requires_grad=True`，后续所有运算会被记录成一个**计算图**（DAG），沿图反向传播就能拿到任意输出对任意输入的梯度。NumPy 没有这个能力。PINN 的 $\partial u/\partial x$、$\partial_{xx}u$ 全靠这套机制算——这正是 PyTorch 之于 NumPy 的关键增量。

---

## 二·autograd 一阶导

一·**模型**：每个 `requires_grad=True` 的叶子 tensor，被运算涉及后会在输出上挂一个反向传播函数；调 `.backward()` 后梯度累积到 `leaf.grad`。

```python
x = torch.tensor([[3.0]], requires_grad=True)    # 必须浮点 + 设 grad
y = x ** 2 + 2 * x + 1                            # y = (x+1)^2
y.backward()                                      # 反向传播
x.grad                                            # tensor([[8.]])  ← dy/dx = 2x+2 = 8
```

二·**对张量 / 多输出**：用 `torch.autograd.grad` 更显式、更 PINN：
```python
u = torch.sin(x)                                  # u(x)
u_x = torch.autograd.grad(
    outputs=u, inputs=x,
    grad_outputs=torch.ones_like(u),
    create_graph=True,                            # ← PINN 关键：保留图才能再求
)[0]                                              # cos(x)
```

> [!note] 核心理解
> 在 PINN 里 `u` 是网络输出（一个标量场在 batch 配点上的值），`x` 是输入时空坐标。`grad_outputs=torch.ones_like(u)` 相当于「把每个样本的 u 各自当标量反传，平行拿到每个点处的 $\partial u/\partial x$」——这是批矢量求导的标准套路。

---

## 三·**二阶导**（PINN 的核心，硬卡）

物理方程里高频出现 $\partial_{xx}u$、$\nabla^2 u$，都需要**对一阶导再求一次导**——必须用 `create_graph=True` 保留中间图，否则第二次 `.backward()` 报错。

```python
x = torch.tensor([[1.5]], requires_grad=True)
u = torch.sin(x)
u_x  = torch.autograd.grad(u, x, create_graph=True)[0]    # 一阶：cos(x)
u_xx = torch.autograd.grad(u_x, x, create_graph=True)[0]  # 二阶：-sin(x)
```

`u_xx` 在 `x = π/2` 处 ≈ -1，符合 $-\sin$ 在 $\pi/2 = -1$。

> [!warning] 易错
> ==第二次求导前必须一次 `create_graph=True` 留住图==。很多人写 PINN「卡在 `u_xx = None`」就是忘了 `create_graph=True`。这是 autograd 与 PINN 最密集的事故点。

---

## 四·训练循环四件套

PINN 也是这个壳，只是 `loss` 把 PDE 残差加进来了。

```python
import torch.nn as nn
model = nn.Sequential(
    nn.Linear(2, 40), nn.Tanh(),
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 1)
)
opt = torch.optim.Adam(model.parameters(), lr=1e-3)

for step in range(2000):
    opt.zero_grad()                       # 1. 清旧梯度（PyTorch 梯度累加）
    pred = model(x_input)                  # 2. forward
    loss = ((pred - y_true) ** 2).mean()   # 3. 损失
    loss.backward()                        # 4. backward 算梯度
    opt.step()                             # 5. 更新参数
    if step % 200 == 0:
        print(step, float(loss))
```

一·**关键点**：
  1. `opt.zero_grad()` 必须每步先清——不然梯度跨步累加。
  2. `loss.backward()` 只做梯度，更新靠 `opt.step()`。
  3. `model.parameters()` 自动收集可训练参数。
  4. `.detach()` 把张量从图中撕下来，便于打印/绘图不影响梯度。

> [!note] 核心理解
> 训练循环四步 = 「清 → 前 → 损 → 反 → 步」。把它套到 PINN 上时，**损失会从 MSE_data 扩成** `MSE_data + MSE_pde + MSE_bc + MSE_ic`——其余的 forward/backward/step 一字不改。所以 ==先把这套四件套在普通回归上跑通==，再去加物理项。

---

## 五·最小回归 demo（阶段 B 必做）

```python
import torch, torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt

x = torch.linspace(-2*np.pi, 2*np.pi, 200).reshape(-1, 1)
y = torch.sin(x)

model = nn.Sequential(
    nn.Linear(1, 40), nn.Tanh(),
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 1)
)
opt = torch.optim.Adam(model.parameters(), lr=1e-2)

for step in range(3000):
    opt.zero_grad()
    pred = model(x)
    loss = ((pred - y) ** 2).mean()
    loss.backward()
    opt.step()
    if step % 500 == 0: print(step, float(loss))

with torch.no_grad():
    plt.plot(x.numpy(), y.numpy(), "k-", label="sin")
    plt.plot(x.numpy(), model(x).numpy(), "r--", label="PINN-style net")
    plt.legend(); plt.savefig("fit_sin.png", dpi=120)
```

一·**核心理解**：
> [!note] 核心理解
> 这份 demo 看似只是拟合 sin——但它已经是 PINN 的 80% 解耦骨架。PINN 相对它的增量只有两处：(1) 输入除 `x` 还加 `t`；(2) 损失附加一项「在配点处 PDE 残差为零」。把这 20 行**自己改对一次**（试改层数、激活函数、学习率），再进 PINN 就不会懵。

---

## 六·PINN 的 autograd 模板（衔接到阶段 C）

虽然这是 PyTorch 章，但 autograd 在 PINN 里这么用——记住位置：

```python
# 配点 (x, t)：要求导，requires_grad 必须开
xt = torch.rand(1000, 2, requires_grad=True)     # 配点
u = model(xt)                                    # 网络输出，shape (1000, 1)

# 拆 x、t 切片单独求导
u_x  = torch.autograd.grad(u, xt, grad_outputs=torch.ones_like(u),
                          create_graph=True)[0][:, 0:1]
u_t  = torch.autograd.grad(u, xt, grad_outputs=torch.ones_like(u),
                          create_graph=True)[0][:, 1:2]
u_xx = torch.autograd.grad(u_x, xt, grad_outputs=torch.ones_like(u_x),
                          create_graph=True)[0][:, 0:1]

# Burgers 残差：u_t + u * u_x - (ν/u少) u_xx = 0
res = u_t + u * u_x - (nu / pi) * u_xx
mse_pde = (res ** 2).mean()
```

> [!warning] 易错
> ==一个常见错==：用 `u.backward()` 求一次后还想求 `u_x.backward()`——图已被释放。PINN 里**永远用 `torch.autograd.grad(..., create_graph=True)`，别用 `.backward()`**。

---

## 速记卡 / 一句话总结

- `torch.tensor` 是会算梯度的 NumPy 数组；`requires_grad=True` 才进计算图。
- ==autograd 二阶导必须 `create_graph=True` 留图==，否则 `u_xx` 取不到——PINN 最大事故点。
- PINN 求导**用 `torch.autograd.grad` 不用 `.backward()`**：需要批矢量、要留图。
- 训练循环四件套 = `zero_grad → forward → loss → backward → step`，PINN 不改节奏只改 loss。
- 先跑通 sin 回归，再去加物理项 = PINN 的正确递进顺序。
- ==`A * B` 是元素积，`A @ B` 才是矩阵乘==——PyTorch 与 NumPy 同规矩。
- `np ↔ tensor` 用 `from_numpy` / `.numpy()`，但**共享内存**，改一改二。
- 画图前 `.detach()` 把预测值从图中撕下，否则会污染 autograd 状态。
- 双 `nn.Linear + Tanh` MLP 是 PINN 默认骨架（tanh 光滑可导，比 ReLU 更适合 PDE）。

---

## Related Notes
- [[笔记/技能/Python/06-科学计算/NumPy矢量运算|NumPy矢量运算]]
- [[assets/LLM上下文/PINN/PINN学习 MOC|PINN 学习 MOC]]