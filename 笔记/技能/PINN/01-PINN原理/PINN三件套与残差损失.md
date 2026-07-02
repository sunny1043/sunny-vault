---
source: Raissi, Perdikaris, Karniadakis (2019) J. Comput. Phys. 378:686-707; 中文重述+知识库重组
type: study-note
subject: PINN
date: 2026-07-02
keywords: [pinn, residual-loss, collocation, autograd, soft-constraint]
tags: [study-note, pinn]
---

# PINN 三件套与残差损失 —— PINN 全部精华浓缩

#pinn #dl #pde

> 这一章是 PINN 学习的**核心章**，吃透它，后面 Burgers / NS / 反问题都是同一套骨架的换装。前置：[[笔记/技能/Python/07-PyTorch基础/PyTorch与自动微分|PyTorch autograd]]。

## 一·定义：PINN 是什么

一·**定义**：**Physics-Informed Neural Network（PINN）** 是一种把偏微分方程（PDE）作为**软约束**嵌入神经网络损失函数的深度学习方法——用神经网络 $u_\theta(x, t)$ 参数化未知场，让网络在**域内配点**处满足 PDE 残差最小、在**初始/边界配点**处贴合已知数据，通过梯度下降同时压「**物理 + 数据**」两个目标，使训练后的网络成为方程的近似解。

二·**PDE 的一般形式**（PINN 处理的标准形式）：
$$
\partial_t u(x, t) + \mathcal{N}[u](x, t) = 0, \quad x \in \Omega, \ t \in [0, T]
$$
其中 $\mathcal{N}$ 是关于 $u$ 的**非线性算子**（可能含 $\partial_x, \partial_{xx}$ 等空间导数），$\Omega$ 是空间域。
  1. Burgers：$\mathcal{N}[u] = u\,u_x - \dfrac{\nu}{\pi}\,u_{xx}$
  2. NS（不可压）：把 $u$、$p$ 一起当输出，对每个分量写一个方程
  3. 扩散方程：$\mathcal{N}[u] = -\alpha\,u_{xx}$，是线性算子的最简情形

三·**核心理解**：
> [!note] 核心理解
> PINN 把 PDE 当成「**约束**」而非「求解器」。传统数值法（有限差分/有限元）解 PDE 是显式推进；PINN 是**训练一个网络去逼近解**——网络要解 PDE 的唯一要求就是「PDE 残差在采样点上接近 0」。这是思维方式从「求解」到「以约束驱动拟合」的转向，也是「**先验物理嵌入学习**」的总范式。

---

## 二·PINN 三件套（核心骨架）

PINN 一切都是这三件套的换装。每次新方程，你只改这三处。

### 1. 网络 $u_\theta$（解的参数化）

一·**定义**：一个**全连接神经网络**（MLP），输入时空坐标 $(x, t)$，输出场的标量值 $u$。$\theta$ 是所有权重/偏置，是优化目标。

二·**典型结构**：
```python
model = nn.Sequential(
    nn.Linear(2, 40), nn.Tanh(),     # 输入 2 维 (x, t)
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 40), nn.Tanh(),
    nn.Linear(40, 1)                  # 输出 1 维：u(x,t)
)
```

三·**关键设计点**：
  1. 输入维 = 时空坐标维（Burgers 是 2，2D NS 是 3）。
  2. 输出维 = 未知场分量数（标量场 1，速度场 2~3，加压强再 +1）。
  3. **激活函数**几乎都用 `Tanh`——光滑、二阶可导，autograd 求高阶偏导稳定。ReLU 二阶导为零，PINN 里基本不用。

> [!note] 核心理解
> 为什么是 MLP（全连接 + Tanh）？因为 PDE 解通常是**光滑场**，MLP + Tanh 是**通用函数逼近器**且处处二阶可导，autograd 才能「无瑕求出 $\partial_{xx}u$」。CNN 更适合图像（局部平移不变），不适合 PDE 的全局光滑性。

### 2. 残差 $r_\theta$（PDE 进网络）

一·**定义**：把 PDE 的左端写成 $r_\theta(x,t) = \partial_t u_\theta + \mathcal{N}[u_\theta]$，**所有导数用 autograd 自动求**——这就是 PINN 利益契合点。

二·** Burgers 例**：
```python
xt = torch.rand(N, 2, requires_grad=True)   # 域内配点
u = model(xt)                                # (N, 1)

# 一阶
grads1 = torch.autograd.grad(u, xt, grad_outputs=torch.ones_like(u),
                             create_graph=True)[0]
u_x = grads1[:, 0:1];  u_t = grads1[:, 1:2]

# 二阶
grads2 = torch.autograd.grad(u_x, xt, grad_outputs=torch.ones_like(u_x),
                             create_graph=True)[0]
u_xx = grads2[:, 0:1]

# 残差
r = u_t + u * u_x - (nu / pi) * u_xx
```

三·**核心铁律**：
  1. ==`requires_grad=True` 必须开在输入 `xt` 上==（不是网络参数）—— PINN 是对**输入坐标**求导，不是对权重求导（权重的导 autograd 在 `loss.backward()` 时自动处理）。
  2. ==二阶导前必须 `create_graph=True` 留图==（见 PyTorch 章 §3，硬卡）。
  3. ==`grad_outputs=torch.ones_like(...)`==：批矢量求导的标准套路，相当于「每个样本独立反传」。

> [!note] 核心理解
> PINN 的「**求 PDE 中的导数**」与训练网络的「**反向传播**」是**两次 autograd**：前者对**输入 $x,t$**求导得到 $\partial u/\partial x$ 等；后者对**参数 $\theta$** 求导更新权重。PyTorch 的计算图同时支持这两个方向——这就是 PINN 能在 PyTorch 上自然落地的根本原因。

### 3. 损失 $\mathcal{L}$（四项求和）

一·**定义**：总损失 = 数据 + PDE + 边界 + 初始 四项加权和：
$$
\mathcal{L}(\theta) =
\underbrace{\lambda_d\, \mathrm{MSE}_{data}}_{\text{已知散点}}
+ \underbrace{\lambda_p\, \mathrm{MSE}_{pde}}_{\text{物理约束}}
+ \underbrace{\lambda_b\, \mathrm{MSE}_{bc}}_{\text{边界}}
+ \underbrace{\lambda_i\, \mathrm{MSE}_{ic}}_{\text{初始}}
$$
其中每项是均方误差：
$$
\mathrm{MSE}_{pde} = \frac{1}{N_f}\sum_i |r_\theta(x_i, t_i)|^2, \\
\mathrm{MSE}_{bc}  = \frac{1}{N_b}\sum_j |u_\theta(x_j, t_j) - u_{bc}(x_j, t_j)|^2, \\
\mathrm{MSE}_{ic}  = \frac{1}{N_i}\sum_k |u_\theta(x_k, 0) - u_0(x_k)|^2.
$$

二·**两种问题类型决定哪几项出现**：
  1. **正问题**（forward）：只知道 PDE + BC + IC，无散点数据 → $\mathrm{MSE}_{data}$ 项缺省 0，靠 PDE+BC+IC。
  2. **逆问题**（inverse）：有观测散点 + 部分 PDE 系数未知 → 加 $\mathrm{MSE}_{data}$，未知系数作可训练标量（详见 [[笔记/技能/PINN/04-反问题与参数识别/反问题PINN|第 4 章]]）。

三·**配点采样**（$\mathrm{MSE}_{pde}$ 的 $N_f$ 个点）：
  1. 最简单：**域内均匀随机**（`torch.rand(N, 2)`）。
  2. 改进：**拉丁超立方采样**（Latin Hypercube），边际分布更均匀，DeepXDE 默认。
  3. 进阶：自适应配点（残差大处加密），研究前沿，入门先不碰。

> [!note] 核心理解
> 关键洞察：**BC/IC 是硬约束在传统数值法里不可违反**，而在 PINN 里是**软约束**——它进入损失但不强制。这意味着 PINN 的 BC 不一定 100% 满足，靠 $\lambda_b$ 权重平衡相对压力。优点是灵活（可处理噪声 BC），缺点是要调权重盟约——这是 PINN 调参的核心痛点，也是后续「硬约束 PINN」「 causal training」 的研究动机。

---

## 三·收敛性 / 由谱偏置导致的失败模式

一·**谱偏置（spectral bias）**：神经网络倾向于先学低频、后学高频。对 PDE 来说，这意味着网络先学大尺度场，对陡变 / 高频波动（如 Burgers 在 t 增大时形成的激波）学得慢或学不到。

二·**常见失败模式**：
（1）**残差降不下去**：训练后期 $\mathrm{MSE}_{pde}$ 卡在平台，网络@store了平滑近似但漏掉陡变区域。
（2）**BC 不满足**：壁面 $u=0$ 学得偏离，导致画 streamplot 时壁面流没贴边。
（3）**局部极小**：训练 loss 不降，初始化不好导致陷入次优解。

三·**缓解手段**（看 demo 时认得即可，初学先不深究）：
  1. 调 $\lambda$ 权重：把 BC/IC 项放大 10~100 倍。
  2. 换网络：加宽加层、用残差连接、SIREN（正弦激活）。
  3. 学习率调度：Adam 收敛后切 L-BFGS（DeepXDE 默认支持）。
  4. **域分解**：把大时空域切成多个子域各训一个 PINN（cPINN, FBPINN），研究前沿。

> [!warning] 易错
> PINN 不是「万能解算器」——对**强非线性、长时大域、激波**问题，谱偏置让 PINN 经常不肯收敛。看 demo 跑得好不代表你的工程问题能直接套，调参 + 评估「**画 streamplot 看涡对不对**」是必备。

---

## 四·PINN vs 传统数值法的位置

| 维度 | 有限差分 (FDM) | 有限元 (FEM) | PINN |
|---|---|---|---|
| 求解方式 | 显式时间推进 | 解线性系统 | 梯度下降训练网络 |
| 网格需求 | 必须（结构化） | 必须（非结构化） | **无需**，随机配点 |
| 维度灾难 | 重 | 重 | **较轻**（MLP 共享参数） |
| 高频/激波 | 强（高阶格式） | 强 | **弱**（谱偏置） |
| 逆问题 | 难（要重解） | 难 | **天然支持**（参数可训） |
| 误差可证 | 有先验/后验估计 | 严格 | 缺乏严谨保证 |

> [!note] 核心理解
> 判定 PINN 何时划算：(1) **逆问题** —— 参数未知求方程，PINN 天下无敌； (2) **高维 PDE** —— 高维 FDM/FEM 网格爆炸，PINN 配点稀疏占优； (3) **几何复杂 + 噪声数据** —— 无网格 + 软约束对噪声鲁棒。PINN 不擅长：强非线性激波、需要严格误差界的工程验证。

---

## 五·易错 / 边界清单

  1. ==`xt.requires_grad=True`==：忘了开就只能训网络不能算 PDE 残差（PINN 第一坑）。
  2. ==二阶导 `create_graph=True`==：PyTorch 章 §3 硬卡。
  3. ==BC/IC 放 `with torch.no_grad()`==：边界项不要求 PDE 残差导，加 `no_grad` 省内存，但 BC 输入要单独 tensor 不参与 `xt` autograd。
  4. **梯度方向，不是函数值**：`autograd.grad` 返回的是张量（每行一个 $\partial u/\partial x$），不是标量；要批矢量求导就传 `grad_outputs=ones`。
  5. **$\lambda$ 权重默认 1**：但各损失项量级不同时（残差 1e-2，BC 1e0），不加 $\lambda$ 训练崩——起步就把 BC 项权重设为 10~100。
  6. **不要用 ReLU**：relu 二阶导处处为零，autograd 求 $u_{xx}$ 直接全是 0，PINN 退化。

---

## 速记卡 / 一句话总结

- PINN = **物理残差进损失**的网络，PDE 是软约束、不是求解器。
- ==三件套==：网络 $u_\theta$ / 残差 $r_\theta$（autograd 求）/ 损失 $\mathcal{L}=\lambda_d L_{data} + \lambda_p L_{pde} + \lambda_b L_{bc} + \lambda_i L_{ic}$。
- ==PINN 求导是对**输入坐标** autograd==，不是对网络权重；权重梯度由 `loss.backward()` 自动处理——两个方向的 autograd。
- ==二阶导必须 `create_graph=True`==，否则 $u_{xx}$ 取不到。
- ==激活用 `Tanh` 不用 ReLU==（二阶可导 + 光滑）。
- BC/IC 是**软约束**，靠 $\lambda$ 权重平衡，**不一定 100% 满足**——这是 PINN 的灵活 + 调参痛点。
- 谱偏置：网络先学低频后学高频，对激波/陡变难收敛。
- PINN 长项：**逆问题** + **高维 PDE** + 几何复杂 / 噪声数据。
- 调参起步：BC 权重 10~100、Adam 收敛后切 L-BFGS。
- 正 vs 逆：正问题靠 PDE+BC+IC；逆问题加 $L_{data}$ + 未知参数可训。

---

## Related Notes
- [[笔记/技能/Python/07-PyTorch基础/PyTorch与自动微分|PyTorch 与自动微分]]
- [[笔记/技能/PINN/02-Burgers方程PINN/Burgers-PINN|Burgers 方程 PINN]]
- [[LLM上下文/PINN/PINN学习 MOC|PINN 学习 MOC]]