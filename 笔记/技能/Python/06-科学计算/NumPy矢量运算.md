---
source: 综合（NumPy 官方文档 + 入门共识整理；为 PINN 学习栈筑基）
type: study-note
subject: Python
date: 2026-07-02
keywords: [numpy, ndarray, broadcasting, vectorization, matplotlib]
tags: [study-note, python]
---

# NumPy 矢量运算 + matplotlib 画场

#python #numpy #scipy

> 这一章是从「会写 Python」走到「能跑 PINN」的地基。PINN 一切都是**批矢量**：网络一次吃几千个配点、损失并行算、autograd 批求偏导。不会 NumPy 矢量化，下一步 PyTorch 张量也学不动。

## 一·`ndarray`：矢量化核心

一·**定义**：`ndarray`（N-dimensional array）是 NumPy 的核心数据结构——**一个 N 维、同类型、连续内存**的数值数组。它不是嵌套 list，而是一整块连续内存 + 形状/步长元信息，所以能高效做矢量运算。

二·**创建**：
```python
import numpy as np
a = np.array([1, 2, 3])                         # 1D
b = np.zeros((3, 4))                            # 3x4 零矩阵
c = np.ones(5)
d = np.arange(0, 1, 0.1)                        # [0, 0.1, ...0.9]
e = np.linspace(0, 1, 11)                       # 11 个等距点，含端
f = np.random.rand(3, 3)                        # 均匀随机
g = np.eye(3)                                   # 单位阵
```

三·**关键属性**：
```python
a.shape     # (3,)       各维大小
a.ndim      # 1          维数
a.dtype     # int64      元素类型
a.size      # 3          元素总数
```

> [!note] 核心理解
> 「矢量思维」一句话：**不要写 for 循环改数组每个元素，让 NumPy 一次性算完整块**。这不仅快几个数量级（C 内核 + SIMD），代码也更短更清楚。在 PINN 里，几千个点的 $\sin(x)$ 就是 `np.sin(x_batch)`，不是 `for xi in x_batch: ...`。

---

## 二·索引与切片

一·**基础切片**（沿袭 Python 左闭右开）：
```python
A = np.arange(12).reshape(3, 4)
A[0]        # 第 0 行  → array([0,1,2,3])
A[0, 2]     # 行 0 列 2 → 2
A[:, 1]     # 所有行第 1 列
A[1:3, :]   # 第 1、2 行
A[-1]       # 末行
```

二·**花式索引 / 布尔索引**（PINN 配点采样常用）：
```python
x = np.random.rand(100)
mask = x > 0.5
x[mask]              # 所有大于 0.5 的元素
idx = np.array([3, 7, 42])
x[idx]               # 按下标批量取
```

> [!warning] 易错
> ==切片是**视图**不是拷贝==：`b = A[:, 0]; b[0] = 99` 会改到 `A`！要独立副本写 `A[:, 0].copy()`。这条与 list 切片相反——NumPy 切片默认共享内存省空间，必须显式 `.copy()`。

---

## 三·广播（broadcasting）—— 矢量化的灵魂

一·**定义**：广播是 NumPy 在**形状不完全一致**的数组间做运算时，按规则自动「虚拟扩展」较小数组，使其形状匹配后再做元素级运算的机制。不复制数据、只改索引方式。

二·**两条规则**：
  1. 从右往左逐维对齐：每维**相等**或其中一个为 **1** 才能广播。
  2. 为 1 的维度被「虚拟拉长」成另一数组的对应大小；其余维度必须严格相等。

三·**典型例子**：
```python
x = np.arange(3)                 # (3,)
x + 5                           # (3,)    标量广播成 (3,) → [5,6,7]

A = np.ones((3, 4))             # (3,4)
A + np.array([10, 20, 30, 40])  # (3,4) + (4,)    右对齐 → (4,) 广播成 (3,4)
A + np.array([[10],[20],[30]])  # (3,4) + (3,1)   左维 1 → 广播成 (3,4)
```

> [!note] 核心理解
> 广播复现了「二元运算前自动对齐维度」的抽象，让你不写双重循环就能算「外积 / 减均值 / 标准化」。PINN 里 $\partial_{xx}u \approx (u_{i-1} - 2 u_i + u_{i+1}) / \Delta x^2$ 通过切片 `u[:-2] - 2*u[1:-1] + u[2:]` **一行矢量**搞定，靠的就是切片+广播。

---

## 四·矢量运算 vs 手写循环

一·**标量二阶差分** —— 标量版 vs 矢量版：
```python
# 标量版（slow）
out = np.empty(N)
for i in range(1, N-1):
    out[i] = (u[i-1] - 2*u[i] + u[i+1]) / dx**2

# 矢量版（fast, NumPy 之味）
out = (u[:-2] - 2*u[1:-1] + u[2:]) / dx**2
```

二·** Huff 表达 1D 热扩散显式格式** —— 这就是阶段 A 的验手例：
```python
u = np.zeros((Nt, Nx))
u[0, 0] = 1                              # 初始脉冲
for n in range(Nt - 1):
    u[n+1, 1:-1] = u[n, 1:-1] + alpha * dt/dx**2 * (
        u[n, 2:] - 2*u[n, 1:-1] + u[n, :-2]
    )
    u[n+1, 0] = u[n+1, -1] = 0           # Dirichlet 边界
```

> [!note] 核心理解
> 时间步仍要 `for`（串行计算），**空间维一律矢量**——这是 PDE 数值实现的通用模式。PINN 训练循环同理：梯度步 while 串行，但 batch 配点损失矢量并行。

---

## 五·线性代数（PINN 必备最小集）

```python
A = np.random.rand(3, 3)
B = np.random.rand(3, 4)

A @ B                 # 矩阵乘  等价 np.matmul
A * B                 # ⚠️ 元素积（不是矩阵乘！）
A.T                   # 转置
np.linalg.inv(A)      # 逆
np.linalg.solve(A, b) # 解 Ax=b（推荐，比 inv 后 @ 快且稳）
np.linalg.norm(v)     # 范数
```

> [!warning] 易错
> ==`A * B` 是元素积不是矩阵乘==；要做矩阵乘写 `A @ B`。这条比任何规则都坑 NumPy 新手。PyTorch 里同理。

---

## 六·matplotlib 画场（PINN 可视化必修）

一·**场图三种武器**（对应 PINN 输出的不同可视化）：
```python
import matplotlib.pyplot as plt

X, T = np.meshgrid(x, t)              # 时空格点
# (1) 时空标量场（u 的等高/着色）
plt.pcolormesh(X, T, U, shading='auto'); plt.colorbar()
# (2) 矢量场 quiver：标PINN 速度场
plt.quiver(X, Y, U, V)
# (3) 流线 streamplot：看回流区/涡
plt.streamplot(X, Y, U, V, density=1.2)
```

二·**配套设置**：
```python
plt.xlabel("x"); plt.ylabel("t"); plt.title("Burgers PINN 解")
plt.tight_layout()
plt.savefig("u.png", dpi=150)        # 存图
plt.show()
```

> [!note] 核心理解
> 方腔流 PINN 训练完后，判断「学得好不好」最直接的方式不是看 loss，而是 `streamplot` 看中心涡位置对不对——这正是你的流体直觉在 PINN 上的用武之地。学会画场 = 给自己开了「眼睛」。

---

## 速记卡 / 一句话总结

- `ndarray` = 连续内存 + 形状/步长；属性 `shape/ndim/dtype/size`。
- ==矢量思维==：能用 `np.sin(x_batch)` 就别写 `for xi in x:`，快几个数量级。
- 切片是 ==**视图**不是拷贝==（与 list 相反）：要独立副本 `.copy()`。
- 广播两规则：右对齐、为 1 的维度被虚拟拉长；其余维必须严格相等。
- ==`A*B` 是元素积，`A@B` 才是矩阵乘==——这是 NumPy 新手最密集事故点。
- 解 `Ax=b` 用 `np.linalg.solve`，比 `inv(A) @ b` 稳且快。
- 画场三招：`pcolormesh`（标量场）/ `quiver`（矢量）/ `streamplot`（流线，看涡）。
- PDE 数值节奏：时间串行、空间矢量。
- 矢量化二阶差分口诀：`(u[:-2] - 2*u[1:-1] + u[2:]) / dx**2`。

---

## Related Notes
- [[笔记/技能/Python/02-数据结构/数据结构|数据结构]]
- [[笔记/技能/Python/07-PyTorch基础/PyTorch与自动微分|PyTorch与自动微分]]
- [[LLM上下文/PINN/PINN学习 MOC|PINN]]