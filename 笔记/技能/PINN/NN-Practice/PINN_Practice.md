---
source: 综合（基于四章节自编练习；含原理题与上机题）
type: practice
subject: PINN
date: 2026-07-02
keywords: [pinn-practice, autograd, deepxde, burgers, ns, inverse]
tags: [practice, pinn]
---

# PINN 练习题

#pinn #practice

> 配套四章节：原理 / Burgers / NS / 反问题。难度 ★（概念）～★★★（实现）。
> 上机题前置：装好 `deepxde` + `torch` + `matplotlib`。

---

## 一·PINN 三件套原理

### P1.1 ★ 三件套口算
写出 PINN 三件套的名称，并指出每件套在 Burgers PINN 代码里分别对应哪个变量 / 表达式。

> [!tip]- 答案
> (1) 网络 $u_\theta$ → `model(xt)`；(2) 残差 $r_\theta$ → `u_t + u*u_x - nu*u_xx`；(3) 损失 $\mathcal{L}$ → `mse_pde + 10*(mse_bc + mse_ic)`。

### P1.2 ★★ 两次 autograd
PINN 里「求 PDE 导数」和「训练网络」分别是哪两次 autograd？它们的求导对象是？

> [!tip]- 答案
> (1) 对**输入坐标** $x,t$ 求 PDE 中的导数（用 `torch.autograd.grad(...)`）；(2) 对**网络参数** $\theta$ 求梯度（`loss.backward()` 自动处理）。

### P1.3 ★★ 软约束 vs 硬约束
传统 FDM 的 BC 是硬约束还是软约束？PINN 的 BC 是哪种？这种差异带来什么优缺点？

> [!tip]- 答案
> FDM 是硬约束（BC 严格不变）；PINN 是软约束（BC 进损失但不强制）。
> 优点：可处理噪声 BC / 不精确 BC。缺点：不严格满足，需调 $\lambda_b$ 权重，是 PINN 调参痛点。

### P1.4 ★★★ 谱偏置验证实验
设计一个 Burgers 训练实验，验证「网络先学低频后学高频」。给出训练中和训练后该观察什么。

> [!tip]- 答案
> 改 `num_domain=500`（小），训练每 1000 步打印 $t=0.5$ 处 $u(x, 0.5)$ 曲线。会观察到：早期曲线光滑（低频先学），接近 $\sin$ 形状；后期陡变区才逐渐显形（高频），最终可能仍偏光滑（没学到激波）。
> 结论：这就是谱偏置。补救：加宽网络、causal training、自适应配点。

---

## 二·Burgers PINN

### P2.1 ★ 配点定义
Burgers PINN 用了三类配点 `xf, xb, xi`，分别对应哪三种约束？各自采样在什么域上？

> [!tip]- 答案
> `xf` 域内 $(x \in [-1,1], t \in [0,1])$ → PDE 残差；`xb` 边界 $x = \pm 1$ 上 → BC；`xi` 初始 $t = 0$ → IC。

### P2.2 ★★ 切除某项 loss
若只留 PDE 项、去掉 BC 和 IC 的 loss，训练结果会怎样？为什么？

> [!tip]- 答案
> 训练失败：去掉 BC/IC 后，**PDE 残差零解 $u \equiv 0$ 是平凡解**——网络会发现 $u=0$ 时所有偏导为零、残差为零，loss 立即降到 0。
> PDE 只决定 $u$ + IC/BC 决定哪个解。PINN 经典坑：缺约束就会出现多种平凡解。

### P2.3 ★★★ 第一次跑通 DeepXDE
按 [[笔记/技能/PINN/02-Burgers方程PINN/Burgers-PINN|第 2 章]] 跑 DeepXDE 官方 Burgers 例，按 5 组改参实验记录现象。每组 1~2 句结论。

> [!tip]- 参考回答模板
> 1. `num_domain=500` → 残差降不下去，激波区明显偏离；`=10000` 收敛好但慢。
> 2. `num_initial=16` → $t>0.6$ 偏差大；`=160` 与 `=800` 差别不明显。
> 3. 网络宽度 40 训练 20000 步收敛；宽度 80 更稳但起步慢。
> 4. L-BFGS 后 loss 再降 1~2 个数量级——二段式有显著效果。
> 5. 去掉 IC 最致命（彻底无解）；去掉 BC 次之；去掉 PDE 剩 BC/IC 拟合散点（无物理）。

### P2.4 ★★★ 80 行自实现 + 上传
按第 2 章 §3 写出 80 行纯 PyTorch Burgers PINN，跑通 + 画图 + 上传 GitHub 最小 repo。验收：与解析解 L2 误差 < 5%。

> [!tip]- 验收清单
> - [ ] repo 文件树：`pinn_burgers.py / README.md / plots/ / requirements.txt`
> - [ ] `README.md` 用一页讲清 PINN 三件套
> - [ ] 训练 $t=0.5$ 处 $u(x)$ vs 解析解对比图
> - [ ] 报告 L2 误差数值

---

## 三·Navier-Stokes PINN

### P3.1 ★ 稳态降维
为什么方腔流稳态问题网络输入只是 2 维 `(x, y)` 而不是 3 维 `(x, y, t)`？

> [!tip]- 答案
> 稳态定义：$\partial_t u = 0$，所有场不随时间变。输入变量里 $t$ 直接消失；损失也不需要 $\mathrm{MSE}_{ic}$ 项。这是稳态求解的最大简化。

### P3.2 ★★ 矢量场 one-hot 求导
写出 PyTorch 代码：从 `model(xyt) → (u, v, p)`，只对 $v$ 求 $\partial v / \partial x$（不让 $u, p$ 的偏导混入）。

> [!tip]- 答案
> ```python
> out = model(xyt)              # (N, 3)
> grad_v_x = torch.autograd.grad(
>     outputs=out, inputs=xyt,
>     grad_outputs=torch.tensor([0., 1., 0.]).expand_as(out),   # one-hot v
>     create_graph=True
> )[0][:, 0:1]                  # 取 x 分量
> ```

### P3.3 ★★★ LDC 验收
跑通 DeepXDE LDC Re=100 后，验收主涡位置在 ~(0.62, 0.62)——用什么方法画？怎么和 Ghia 1982 基准对照？

> [!tip]- 答案
> - 主涡位置：`plt.streamplot(X, Y, u, v)` 看流线闭合中心。
> - 沿 $x=0.5$ 剖面 $u(y)$ 与 Ghia 表 25 个点对照，算 `np.linalg.norm(u_pred - u_ghia) / np.linalg.norm(u_ghia)` 得相对 L2 误差。
> - 主涡偏差 > 0.1 → 训练未收敛；偏差 < 0.05、L2 < 5% → 入门过关。

### P3.4 ★★ 压力参考点
为什么 2D NS PINN 必须在 $(0, 0)$ 加 $p(0, 0) = 0$ 这种「点约束」条件？

> [!tip]- 答案
> 不可压 NS 压力有**任意加常自由度**（梯度才进方程，平移不影响 PDE）。无点约束时 $p$ 可整体漂移，训练会卡在发散 / 振荡。加一个点 $p$ 即固定常数自由度。

---

## 四·反问题

### P4.1 ★ 反问题定义
正问题与反问题在「已知」和「求」上各是什么？

> [!tip]- 答案
> - 正：已知 PDE 系数 + BC/IC，求场 $u$。
> - 反：已知场观测散点（部分量）+ PDE 形式（系数含未知），同时求场 + 系数。

### P4.2 ★★ 可训练参数招式
写出把粘性 $\nu$ 当可训练参数的关键三行（模型 + 优化器 + 残差）。

> [!tip]- 答案
> ```python
> nu = torch.tensor(0.01, requires_grad=True)
> opt = torch.optim.Adam(list(model.parameters()) + [nu], lr=1e-3)
> r = u_t + u * u_x - nu * u_xx       # nu 进残差，会与权重一起被优化
> ```

### P4.3 ★★★ 反求 ν 合成实验
用 $\nu^\star / \pi = 0.01/\pi$ 生成 Burgers 解，采样 100 个散点作观测，PINN 反求 $\nu$。要求：3 组随机初值都收敛到同一值。

> [!tip]- 验收
> - 真值 $u^\star / \pi \approx 3.18 \times 10^{-3}$。
> - 3 组 $\nu$ 初值（如 0.1, 0.001, 0.5），训练 20000 步后都应收敛到约 3.1e-3。
> - 若某初值不收敛，说明初值敏感——换 Adam + 学习率衰减或换框架。

### P4.4 ★★★ 反推压力场（NS 反问题）
从 vortex shedding 速度散点 + NS 形式，反推压力场。怎么验证反推 $p$ 对不对？

> [!tip]- 答案
> 用已知真解（如 2D 旋涡衰减解析解）生成观测，反推 $p$ 后和真 $p$ 比，并看是否符合流体直觉：（1）迎流面高压、背流面低压；（2）驻点附近压力梯度为零；（3）画 `plt.contour(X, Y, p)` 看等值线光滑闭合无发散。
> ==一旦无真值对照，仍先和合成数据上跑通==再上真实观测。

---

## 自测进度

- [ ] 原理题 4 道
- [ ] Burgers 题 4 道（含上机 2 道）
- [ ] NS 题 4 道（含上机 2 道）
- [ ] 反问题题 4 道（含上机 2 道）

---

## Related Notes
- [[笔记/技能/PINN/01-PINN原理/PINN三件套与残差损失|PINN 三件套]]
- [[笔记/技能/PINN/02-Burgers方程PINN/Burgers-PINN|Burgers PINN]]
- [[笔记/技能/PINN/03-Navier-Stokes PINN/NavierStokes-PINN|NS PINN]]
- [[笔记/技能/PINN/04-反问题与参数识别/反问题PINN|反问题PINN]]
- [[assets/LLM上下文/PINN/PINN学习 MOC|MOC]]