---
keywords: practice, gas-flow, gas-cycle, steam, moist-air
---

# 工程应用 Practice (12 questions)

#practice #gas-flow #gas-cycle #steam #moist-air #engineering-thermodynamics

## Related Notes
- [[第5章_气体的流动和压缩]], [[第6章_气体动力循环]], [[第9章_水蒸气性质和蒸汽动力循环]], [[第10章_湿空气性质和湿空气过程]]

> [!hint]- Key Patterns
> | M=1 at throat | 拉法尔喷管喉部条件 |
> | 朗肯循环 | 压缩→加热→膨胀→冷凝 |
> | 加热 | d不变, t↑, φ↓ |

---

## Question 1 - 声速 [recall]
> 写出声速a的计算公式。

> [!answer]- 答案
> $a = \sqrt{k R_g T}$

## Question 2 - 马赫数 [recall]
> 写出马赫数定义式。

> [!answer]- 答案
> $M = c/a$

## Question 3 - 喷管 [recall]
> 为什么亚声速→超声速需要拉法尔喷管？

> [!answer]- 答案
> M<1需收缩加速; M=1在喉部; M>1需扩张加速。只有先缩后扩才能全程加速通过声速。

## Question 4 - 奥托循环 [recall]
> 奥托循环的加热方式是什么？对应什么发动机？

> [!answer]- 答案
> 定容加热; 汽油机

## Question 5 - 朗肯循环 [recall]
> 列出朗肯循环的四个过程和设备。

> [!answer]- 答案
> 压缩(泵)→加热(锅炉)→膨胀(汽轮机)→冷凝(冷凝器)

## Question 6 - 干度 [recall]
> 写出干度x的定义式。

> [!answer]- 答案
> $x = m_v/(m_v+m_l)$

## Question 7 - 三种温度 [recall]
> 未饱和湿空气中t_dp, t_wb, t的大小关系。

> [!answer]- 答案
> $t_{dp} < t_{wb} < t$

## Question 8 - 声速计算 [application]
> 空气k=1.4, R_g=287J/(kg·K), T=300K。求声速。

> [!answer]- 答案
> $a = \sqrt{1.4 \times 287 \times 300} = 347.2$ m/s

## Question 9 - 朗肯效率 [application]
> h₁=3400, h₂=2100, h₃=h₄=120kJ/kg。求η。

> [!answer]- 答案
> $\eta = (3400-2100)/(3400-120) = 1300/3280 = 39.6$%

## Question 10 - 湿蒸汽 [application]
> p=0.1MPa, h'=417.5, h''=2675.1, x=0.9。求h。

> [!answer]- 答案
> $h = 417.5 + 0.9\times(2675.1-417.5) = 2449.3$ kJ/kg

## Question 11 - 再热目的 [analysis]
> 再热循环的目的是什么？

> [!answer]- 答案
> 减少汽轮机末级蒸汽湿度(保护叶片)，同时提高循环效率。

## Question 13 - 涡扇压气机 [application]
> AL-31F 的 LPC 增压比 π=3.5，HPC 增压比 π=6.6，求总增压比并计算理想布雷顿效率上限 (k=1.4)。

> [!answer]- 答案
> $π_{total} = 3.5 × 6.6 = 23.1$
> $η_{Brayton} = 1 - 1/π^{(k-1)/k} = 1 - 1/23.1^{0.4/1.4} = 1 - 1/23.1^{0.286} ≈ 1 - 0.44 = 56\%$
> 实际效率因不可逆损失低于此值。

## Question 14 - 双转子热力学意义 [analysis]
> AL-31F 采用双转子（LP/HP 转速独立），从热力学角度解释其优势。

> [!answer]- 答案
> 双转子允许高/低压压气机在不同转速下自动匹配，本质是让各级都在接近设计点的流量系数 $φ=C_a/U$ 下工作，减少偏离设计点时前面级失速、后面级堵塞的问题。从热力学看，这意味着每级的实际压缩过程更接近等熵，减少不可逆损失。

## Question 12 - 冬季干燥 [analysis]
> 为什么冬季开暖气后人感觉干燥？

> [!answer]- 答案
> 加热过程中含湿量d不变但温度↑→饱和压力p_s(T)↑→相对湿度φ=p_v/p_s↓→感觉干燥。

