---
source: 各章节速记卡浓缩
type: quick-ref
subject: PINN
date: 2026-07-02
keywords: [pinn, quick-ref, cheatsheet]
tags: [quick-ref, pinn]
---

# PINN 速查卡

#pinn #quick-ref

> 浓缩自四篇章节，上机前一页通览。

## 三件套（一切 PINN 的骨架）

$$
\underbrace{u_\theta(x,t)}_{\text{网络}}
\quad\Rightarrow\quad
\underbrace{r_\theta = \partial_t u + \mathcal{N}[u]}_{\text{残差(autograd)}}
\quad\Rightarrow\quad
\underbrace{\mathcal{L} = \lambda_d L_{data} + \lambda_p L_{pde} + \lambda_b L_{bc} + \lambda_i L_{ic}}_{\text{损失}}
$$

```python
xt.requires_grad_(True)                 # 必须开
u = model(xt)
g1 = torch.autograd.grad(u, xt, torch.ones_like(u), create_graph=True)[0]
u_x = g1[:, 0:1]; u_t = g1[:, 1:2]
g2 = torch.autograd.grad(u_x, xt, torch.ones_like(u_x), create_graph=True)[0]
u_xx = g2[:, 0:1]
r = u_t + u * u_x - nu * u_xx           # 残差
```

## 五条铁律

1. ==`xt.requires_grad=True`==（PINN 第一坑：忘开只能训网络不能算残差）
2. ==二阶导 `create_graph=True`==（不留图 $u_{xx}$ = None）
3. ==激活用 `Tanh` 不用 ReLU==（ReLU 二阶导处处零）
4. ==梯度方向：autograd 求输入坐标的偏导；backward 求权重的梯度==（两次 autograd）
5. ==BC/IC 软约束==：靠 $\lambda$ 权重平衡，不严格满足；起步 $\lambda_b, \lambda_i = 10\sim100$

## Burgers PINN 速查

- PDE: $u_t + u\,u_x - (\nu/\pi)\,u_{xx} = 0$, $x\in[-1,1], t\in[0,1]$
- IC: $u(x, 0) = -\sin(\pi x)$；BC: $u(\pm 1, t) = 0$
- 配点：域内 `num_domain=2500`、初始 `num_initial=160`、边界 `num_boundary=80`
- 网络：`FNN([2] + [40]*4 + [1], "tanh")`
- 优化：Adam → L-BFGS 二段式
- ==5 组改参验收==：`num_domain` / 网络 / 切 L-BFGS / 切除各项 loss —— 过这关才叫入门

## Navier-Stokes PINN 速查

- PDE 三方程：动量 (u, v) + 连续性 $\nabla\cdot\mathbf{u} = 0$
- 两种参数化：**VP**（输出 $u, v, p$）/ **vSF**（输出 $\psi, \omega$，连续性天然）
- ==方腔流稳态==：去掉 $\partial_t$、输入 2 维 $(x, y)$、$\mathrm{MSE}_{ic}$ 不出现
- BC：顶 $u=1, v=0$；其余三壁 $u=v=0$
- 验收：`plt.streamplot` 主涡 ≈ (0.62, 0.62)（Re=100）；沿 $x=0.5$ 剖面与 Ghia 1982 对照
- ==矢量场 autograd 求 $u$ 对 $x$ 的偏导，`grad_outputs` 要 one-hot $u$==
- ==压力必须设参考点== $p(0,0)=0$，否则平移自由让训练飘

## 反问题速查

- 把未知参数 `nu = torch.tensor(0.01, requires_grad=True)`，加进 `optimizer.param_groups`
- 损失加 $\mathrm{MSE}_{data}$（观测散点处网络贴合观测）
- ==物理约束下的最大似然==：贴数据 + 满足 PDE 的 $(u, \lambda)$ 组合
- 三大题型：参数识别 / 源项反演 / 边界反演
- NS 反问题最迷人：==无压力观测反推压力场==
- ==验收铁律：先合成数据（你知真值）跑通，再上真实观测==
- 失败：不唯一 / 初值敏感 / 过拟合 → 多初值 + Tikhonov 正则

## 调参起步配方

| 块 | 配方 |
|---|---|
| 网络 | MLP `Tanh`, 章宽 40~80, 深 4~8 层 |
| 配点 | 域内 `num_domain=$10^3 ~ 10^4$`, 边界 $10^2$ 量级 |
| 激活 | `tanh`（不用 relu/sigmoid） |
| 优化器 | Adam 15000 ~ 20000 步 → L-BFGS 精修 |
| BC/IC 权重 | $\lambda_b, \lambda_i = 10 \sim 100$ |
| 连续性权重 $\lambda_c$ | 10（NS 项中） |
| 学习率 | Adam 1e-3，可调余弦衰减 |

## 易错清单（考前扫一眼）

- 矢量场 autograd 求 $u$ 对 $x$ 偏导 → `grad_outputs` 必 one-hot $u$（其他分量 0）
- 稳态 → 输入 2 维；非定常 → 3 维（输入维必须对）
- `xf.requires_grad_(True)` 是**方法调用**，不是赋值
- BC/IC 输入独立 tensor，不与 `xf` 共享 autograd
- 误差不只看 loss：画图 + 与解析 / FEM 比 L2
- 激波 / 高频区难收敛是谱偏置，不是 bug
- 高 Re 阶梯升：100 → 1000 → 4000
- 反问题初值离真值 10 倍数量级以内更稳

## 路径与衍接

- 学习路径：[[assets/LLM上下文/PINN/PINN学习 MOC|PINN MOC]] 4 阶段 8~9 周
- 前置：[[assets/LLM上下文/Python/Python入门 MOC|Python 入门]] + [[笔记/技能/Python/07-PyTorch基础/PyTorch与自动微分|autograd]]
- 代码库：DeepXDE（[[https://github.com/lululxvi/deepxde]]） · Raissi PINNs（[[https://github.com/maziarraissi/PINNs]]）