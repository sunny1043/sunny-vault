---
keywords: practice, ideal-gas, second-law, carnot
---

# 理想气体与热力学第二定律 Practice (12 questions)

#practice #ideal-gas #second-law #engineering-thermodynamics

## Related Notes
- [[第3章_气体的热力性质和热力过程]], [[第4章_热力学第二定律]]

> [!hint]- Key Patterns
> | 迈耶公式 | $c_p - c_v = R_g$ |
> | n=1 | 定温; n=k | 定熵 |
> | 卡诺效率 | $\eta_C = 1 - T_2/T_1$ |

---

## Question 1 - 状态方程 [recall]
> 写出理想气体状态方程，说明R_g的含义。

> [!answer]- 答案
> $pv = R_g T$, $R_g = R/M$为气体常数

## Question 2 - 迈耶公式 [recall]
> 写出迈耶公式。

> [!answer]- 答案
> $c_p - c_v = R_g$

## Question 3 - 过程识别 [recall]
> n=1, n=k, n=0, n=∞各对应什么热力过程？

> [!answer]- 答案
> n=1: 定温; n=k: 定熵; n=0: 定压; n=∞: 定容

## Question 4 - 卡诺效率 [recall]
> 写出卡诺循环的热效率公式。

> [!answer]- 答案
> $\eta_C = 1 - T_2/T_1$

## Question 5 - 孤立系熵增 [recall]
> 写出孤立系熵增原理及其应用。

> [!answer]- 答案
> $\Delta S_{isol} \geq 0$。判断过程方向和不可逆性。

## Question 6 - 熵变计算 [application]
> 理想气体定温膨胀使v₂=2v₁, R_g=0.287kJ/(kg·K)。求Δs。

> [!answer]- 答案
> $\Delta s = R_g\ln(v_2/v_1) = 0.287 \times \ln(2) = 0.199$ kJ/(kg·K)

## Question 7 - 卡诺效率计算 [application]
> 热机工作在800K和300K之间。求最大理论效率。

> [!answer]- 答案
> $\eta_C = 1 - 300/800 = 0.625 = 62.5$%

## Question 8 - 㶲损失 [application]
> 过程熵产0.5kJ/K, T₀=300K。求㶲损失。

> [!answer]- 答案
> $I = T_0 \cdot S_{g,total} = 300 \times 0.5 = 150$ kJ

## Question 9 - 气化熵变 [application]
> 1kg水100°C气化, r=2257kJ/kg。求Δs。

> [!answer]- 答案
> $\Delta s = r/T = 2257/373.15 = 6.048$ kJ/(kg·K)

## Question 10 - 压缩比影响 [application]
> 奥托循环ε从8提高到10, k=1.4。效率提高多少？

> [!answer]- 答案
> η(8)=1-1/8⁰·⁴=56.5%; η(10)=1-1/10⁰·⁴=60.2%; 提高3.7个百分点

## Question 11 - 混淆点 [analysis]
> "熵只增不减"对吗？为什么？

> [!answer]- 答案
> 不对。"孤立系"的熵只增不减。开放系统可通过向外界排热来减少自身熵。

## Question 12 - 推导 [analysis]
> 推导演示: 为什么卡诺效率η_C=1−T₂/T₁?

> [!answer]- 答案
> 定温过程q=T·Δs: q₁=T₁(s₂−s₁), q₂=T₂(s₃−s₄)=T₂(s₂−s₁)。净功w=q₁−q₂。η=w/q₁=1−T₂/T₁。

