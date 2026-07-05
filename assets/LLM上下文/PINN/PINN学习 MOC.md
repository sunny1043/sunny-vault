---
source: 综合（公开论文/教程/库文档整理为路径文档）
type: moc
subject: PINN
date: 2026-07-02
keywords: [pinn, fluid, deep-learning, pytorch, study-map]
tags: [moc, pinn, python]
---

# PINN（流体）学习 Map —— 零基础到跑通 Burgers demo

#pinn #流体 #python

> 🧭 首页 [[assets/LLM上下文/index|StudyVault]] · 前置技能 [[assets/LLM上下文/Python/Python入门 MOC|Python 入门]] · 相关学科 [[assets/LLM上下文/流体传动与控制/流体传动与控制 MOC|流体传动与控制]]
>
> 学习者背景：**已学流体力学基础 + Python 零基础**。目标档位：**理解 PINN 原理 + 跑通一个公开流体 demo（如 2D 方腔流 / Burgers）**。
> 本 MOC 不替代论文，而是把从「刚会写 Python」到「能跑通 PINN demo」拆成可独立验手的阶段。

## 精读章节（已在 `笔记/技能/PINN/` 落盘）

| # | 主题 | 笔记 | 速查 |
|---|------|------|------|
| 1 | 三件套 / 残差损失 / 软约束 / 谱偏置 | [[笔记/技能/PINN/01-PINN原理/PINN三件套与残差损失\|PINN三件套与残差损失]] | [[assets/LLM上下文/PINN/Quick Reference#三件套\|三件套]] |
| 2 | Burgers PINN + DeepXDE demo + 80 行自实现 | [[笔记/技能/PINN/02-Burgers方程PINN/Burgers-PINN\|Burgers-PINN]] | [[assets/LLM上下文/PINN/Quick Reference#Burgers\|Burgers]] |
| 3 | Navier–Stokes PINN（VP / vSF 形式）+ 2D 方腔流 | [[笔记/技能/PINN/03-Navier-Stokes PINN/NavierStokes-PINN\|NavierStokes-PINN]] | [[assets/LLM上下文/PINN/Quick Reference#Navier-Stokes\|NS]] |
| 4 | 反问题 + 参数识别（雷诺数反推 / 压力场反推） | [[笔记/技能/PINN/04-反问题与参数识别/反问题PINN\|反问题PINN]] | [[assets/LLM上下文/PINN/Quick Reference#反问题\|反问题]] |

## Practice
- [[笔记/技能/PINN/NN-Practice/PINN_Practice|PINN_Practice]]（16 题，含原理题与上机验收清单）

## Quick Reference
- [[assets/LLM上下文/PINN/Quick Reference|PINN 速查卡]]（一页通览 + 调参起步配方 + 易错清单）

---

## 0·框架选型：为什么是 PyTorch

| 维度 | PyTorch ✅ | JAX |
|---|---|---|
| PINN 生态 | DeepXDE / NVIDIA Modulus 主力支持 | 部分 PINN 论文偏爱 |
| 零基础友好 | 命令式、像 Python，调试直观 | 函数式 + jit/vectorize 陡 |
| 教程/社区 | 最大 | 较小 |
| 迁移价值 | 学到的张量/训练循环可迁移到任何 DL 任务 | 适合后续做研究 |

> [!note] 核心理解
> 选 PyTorch 不是因为它在 PINN 上「最强」，而是**零基础性价比最高**：生态足够（DeepXDE 现成有 Burgers/NS demo 可直接跑），语法最像普通 Python，调试能 print 看张量。等你能独立调 PINN 想做研究前沿时，再加学 JAX 不迟。

---

## 1·学习路径（4 阶段，期末产出 = 一个 GitHub 上跑通方腔流 PINN 的最小 repo）

```
阶段 A: Python 科学栈筑基        阶段 B: PyTorch + 自动微分
  NumPy 矢量运算 / 广播            tensor / autograd
  matplotlib 画场                  训练循环 (forward/loss/backward)
  1D 热方程有限差分 → 残差直觉      autograd 求 u_x,u_t
        ↓                              ↓
            阶段 C: PINN 原理与跑通 demo
              Raissi 2019 论文精读
              残差损失 = MSE_data + MSE_pde + MSE_bc + MSE_ic
              DeepXDE 跑 Burgers / 2D 槽道流官方例
                              ↓
            阶段 D（可选）: 最小自实现 PINN
              纯 PyTorch 写 Burgers PINN（≈80 行）
              GitHub 上传最小 repo
```

### 阶段 A — Python 科学栈筑基（1~2 周）

一·**为什么**：PINN 一切都是 **batch 矢量**——网络一次吃几千个配点、损失对整批并行计算。不会 NumPy 矢量化就寸步难行。

二·**学习目标**：
  1. NumPy `ndarray` / 维度 / 形状 / 切片 / 广播规则。
  2. 矢量运算替代 `for`：单矩阵乘 = 多个线性层一次算完。
  3. **matplotlib 画场**：`pcolormesh` / `quiver` / `streamplot` 画流场。
  4. **残差直觉**：用 NumPy 有限差分手解一次 1D 热扩散方程，看清「PDE 残差 = $\partial_t u - \alpha \partial_{xx} u$ 在配点上应等于 0」这句话在数值上意味着什么。

三·**对应知识库笔记**：[[笔记/技能/Python/06-科学计算/NumPy矢量运算|NumPy矢量运算]]（新建）

四·**验手产出**：
```python
# 写得出来 = 这一阶段过关
u = np.zeros((Nt, Nx))
for n in range(Nt):
    u[n+1, 1:-1] = u[n, 1:-1] + alpha * dt/dx**2 * (u[n, 2:] - 2*u[n,1:-1] + u[n,:-2])
```
+ 用 `pcolormesh(x, t, u.T)` 画出热扩散时空图。

---

### 阶段 B — PyTorch + 自动微分（1~2 周）

一·**为什么**：PINN 的「偏微分方程进入损失」全靠 **autograd 自动求偏导**。不懂 autograd 就是把 PINN 当黑盒——既不会调也看不懂报错。

二·**学习目标**：
  1. `torch.tensor` 与 NumPy 互转；`device` / `dtype`。
  2. **autograd**：`requires_grad=True` → `y.backward()` → `x.grad`。
  3. **二阶导**：`torch.autograd.grad(outputs, inputs, create_graph=True)` 再求一次（PINN 中 $\partial_{xx}u$ 必需）。
  4. 训练四件套：`model(x)` → `loss` → `loss.backward()` → `optimizer.step()`。
  5. 做一个**回归 demo**：4 层 MLP 拟合 $f(x)=\sin(x)$，画出训练 loss 下降曲线。

三·**对应知识库笔记**：[[笔记/技能/Python/07-PyTorch基础/PyTorch与自动微分|PyTorch与自动微分]]（新建）

四·**验手产出**：
```python
# autograd 求 u 关于 x 的二阶导，写得出来就过关
x = torch.tensor([[1.0]], requires_grad=True)
u = torch.sin(x)
u_x = torch.autograd.grad(u, x, create_graph=True)[0]
u_xx = torch.autograd.grad(u_x, x, create_graph=True)[0]
```

---

### 阶段 C — PINN 原理与跑通 demo（2 周，关键期）

一·**核心三件套**（PINN 全部精华浓缩）：
  1. 网络 $u_{\theta}(x, t)$：输入时空坐标、输出标量场。
  2. 残差 $r_{\theta}(x,t) = \partial_t u_{\theta} + \mathcal{N}[u_{\theta}]$（$\mathcal{N}$ 是 PDE 的非线性算子，如 NS 的对流项），**用 autograd 自动构造**。
  3. 损失 $\mathcal{L} = \lambda_d \text{MSE}_{\text{data}} + \lambda_p \text{MSE}_{\text{pde}} + \lambda_b \text{MSE}_{\text{bc}} + \lambda_i \text{MSE}_{\text{ic}}$。

二·**为什么这套机制值得学**：
> [!note] 核心理解
> PINN 把 PDE 看成「**约束**」而非「求解器」：用神经网络参数化未知场，让它在**配点**处满足 PDE 残差最小，在初始/边界点处贴住已知数据。优化器同时压「物理 + 数据」两个目标 → 网络就成了一个满足物理方程的解。这正是「**把先验物理嵌入学习**」的总范式。

三·**精读论文**（只读这一篇就够入门）：
- Raissi, Perdikaris, Karniadakis (2019), *Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear forward and inverse problems*, **J. Comput. Phys.** 378, 686–707. arXiv:1711.10561.

四·**跑通 demo**（最大杠杆动作）：
- 用 [[https://github.com/lululxvi/deepxde|DeepXDE]] 的官方 Burgers 例，**改 BC / 域长 / 训练步数**看清各部分作用。

五·**验手产出**：DeepXDE 跑完后能回答 × × × × × ×（不是看了几句就过）：
  - 配点 `num_domain` 改大改小对收敛的影响？
  - `num_boundary` 与 `num_initial` 几个点够不够？
  - 输出 `losshistory` 里 `PDE loss` 与 `BC loss` 的相对量级？
  - 网络从 `FNN([1] + [20]*4 + [1])` 改 `*8` 会变好还是震荡？

---

### 阶段 D（可选）— 最小自实现 PINN（2~3 周，锁定「真懂」）

一·**为什么**：跑通 DeepXDE 还叫「调库」，写一遍 80 行的 Burgers PINN 才算真懂。

二·**目标 GitHub repo**（你自己上传的最小 repo）：
- 文件树建议：
```
your-pinn-burgers/
├── README.md          ← 一页讲清 PINN 三件套 + 你的实验图
├── pinn_burgers.py    ← 主程序，≤100 行
├── plots/            ← 训练 loss 曲线 + u(x,t) 时空图
└── requirements.txt   ← torch, matplotlib, numpy
```

三·**参考**：[[https://github.com/maziarraissi/PINNs|Raissi 个人 PINNs repo]]（最权威，含 Burgers / NS 等原始代码）。也可参考 benmoseley 的经典教学版 *PINNs tutorial*。

---

## 2·资源清单

### 论文 / 教程
- **Raissi 2019 原始论文**：[[https://arxiv.org/abs/1711.10561]]
- **Karniadakis 综述 (2021)**：*Physics-informed machine learning*, Nat. Rev. Phys. — 给你一张全貌地图。
- **Ben Moseley PINNs tutorial**：含纯 PyTorch 80 行 Burgers 实现讲解，最适合零基础。

### 代码库 / demo
| 库 | 链接 | 适合 |
|---|---|---|
| DeepXDE | [[https://github.com/lululxvi/deepxde]] | 阶段 C 直接跑通 demo，零配置文档最多 |
| NVIDIA Modulus | [[https://github.com/NVIDIA/modulus]] | 进阶工程级，先不动 |
| Raissi PINNs | [[https://github.com/maziarraissi/PINNs]] | 论文配套代码，阶段 D 对照 |

### PyTorch / NumPy 官方
- PyTorch 60 分钟入门：[[https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html]]
- PyTorch autograd 文档：[[https://pytorch.org/docs/stable/autograd.html]]
- NumPy 绝对新手指南：[[https://numpy.org/doc/stable/user/absolute_beginners.html]]

---

## 3·与流体力学的衔接点（你的优势）

> [!tip] 补充
> 你已学流体力学基础——PINN 里这些点你会比纯 CS 同学有先发优势，重点体会 Python 代码「对应」到哪些流体物理。

| 流体熟悉概念 | 在 PINN 代码里长什么样 |
|---|---|
| Navier–Stokes | `r = u_t + (u·∇)u + (1/ρ)∇p − ν∇²u`，每项都是 autograd 拼出的表达式 |
| 边界条件（无滑移） | `MSE_bc = mean((u_wall - 0)**2)` |
| 初始条件 | `MSE_ic = mean((u(x, 0) - u0(x))**2)` |
| 流函数 / 涡量 | 多输出网络 ψ / ω，约束 v = ψ_y, u = -ψ_x |
| 雷诺数 Re | 反问题里作为可训练参数，PINN 从数据**反推** Re |

策略：把你的流体直觉对照到阶段 C 的 demo 上——DeepXDE 跑方腔流时盯住「速度场是否满足无滑移」「中心涡位置」这些你熟悉的量，调参就不再是黑盒。

---

## 4·周计划建议（8~9 周）

| 周 | 阶段 | 关键动作 |
|---|---|---|
| 第 1~2 | A | NumPy 矢量 + matplotlib 画场 + 手解热扩散 |
| 第 3~4 | B | PyTorch 训练循环 + autograd 一二阶导 + MLP 拟合 sin |
| 第 5 | C-1 | 精读 Raissi 2019，三件套逐句拆 |
| 第 6 | C-2 | DeepXDE 装好跑 Burgers 官方例，改参 5 组记录现象 |
| 第 7 | C-3 | DeepXDE 跑方腔流 2D demo |
| 第 8 | D | 80 行纯 PyTorch 自实现 Burgers，上传 GitHub |

> [!warning] 易踩坑
> 1. ==**别跳过 autograd 二阶导练习**==：阶段 B 偷懒，阶段 C 一句 `u_xx` 报错你完全看不懂。
> 2. ==**别直接冲方腔流自实现**==：先跑通 Burgers，从标量场到矢量场要加 BC 项和分量网络。
> 3. ==**DeepXDE demo 不是终点**==：能改参说出每个 loss 项的物理含义才算入门。
> 4. Python 零基础别上来就写 PINN——阶段 A 的矢量思维是地基。

---

## 5·本 MOC 衔接的 Python 进阶笔记

PINN 需要的 Python 进阶章在已落盘的 Python 章节基础上新增：

| 进阶章 | 主题 | 在哪 |
|---|---|---|
| 06 | NumPy 矢量运算 / 广播 / 算子 | [[笔记/技能/Python/06-科学计算/NumPy矢量运算]]（新建） |
| 07 | PyTorch tensor / autograd / 训练循环 | [[笔记/技能/Python/07-PyTorch基础/PyTorch与自动微分]]（新建） |

后续随阶段 C/D 推进，再在 `笔记/技能/PINN/` 下建精读章（残差损失构造 / NS 方程 PINN / 反问题等）。

## Related
- [[assets/LLM上下文/Python/Python入门 MOC|Python 入门 MOC]]
- [[assets/LLM上下文/流体传动与控制/流体传动与控制 MOC|流体传动与控制]]