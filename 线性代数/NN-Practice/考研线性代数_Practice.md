---
keywords: practice, linear-algebra
---

# 考研线性代数 Practice (12 questions)

#practice #linear-algebra

## Related Notes
- [[第一章_行列式]], [[第二章_矩阵]], [[第五章_特征值与特征向量]], [[第六章_二次型]]

> [!hint]- Key Patterns
> | 行列式计算 | 三角化/展开/特征值 |
> | 秩定理 | $AB=O\Rightarrow r(A)+r(B)\le n$ |
> | 正定 | 特征值>0 / 主子式>0 |

---

## Question 1 - 行列式计算 [recall]
> 计算 $\begin{vmatrix}1&2\\3&4\end{vmatrix}$

> [!answer]- 答案
> $1\times4-2\times3=4-6=-2$

## Question 2 - $|kA|$ [recall]
> 3阶方阵$A$，$|A|=2$。求$|3A|$。

> [!answer]- 答案
> $|3A|=3^3|A|=27\times2=54$

## Question 3 - 伴随矩阵秩 [recall]
> 4阶方阵$A$，$r(A)=3$。求$r(A^*)$。

> [!answer]- 答案
> $r(A)=3=n-1 \Rightarrow r(A^*)=1$

## Question 4 - $AB=O$ [recall]
> $A$是$3\times4$矩阵，$r(A)=2$，$AB=O$。求$r(B)$最大值。

> [!answer]- 答案
> $r(A)+r(B)\le4 \Rightarrow r(B)\le2$

## Question 5 - 特征值 [recall]
> 矩阵$A$的特征值是$1,2,3$。求$|A|$和$\text{tr}(A)$。

> [!answer]- 答案
> $|A|=1\times2\times3=6$，$\text{tr}(A)=1+2+3=6$

## Question 6 - 对角化 [application]
> $A$有特征值$\lambda=2$(二重), $\lambda=3$(单根)。$r(2E-A)=1$。能否对角化？

> [!answer]- 答案
> $n-r(2E-A)=3-1=2=k$ → 几何重数=代数重数 → **可对角化**

## Question 7 - 线性相关 [application]
> 4个三维向量。是否一定线性相关？

> [!answer]- 答案
> 向量个数(4)>维数(3) → **必线性相关**。

## Question 8 - 方程组解 [application]
> $A$是$4\times5$矩阵，$r(A)=3$。$Ax=0$的基础解系含几个向量？

> [!answer]- 答案
> $n-r(A)=5-3=2$个。

## Question 9 - 正定判定 [application]
> $A$特征值为$2,3,5$。$A$是否正定？

> [!answer]- 答案
> 特征值全>0 → **正定**。

## Question 10 - Sylvester [analysis]
> 用分块矩阵法证明 $r(AB)\ge r(A)+r(B)-n$

> [!answer]- 答案
> 构造$M=\begin{pmatrix}A&O\\E_n&B\end{pmatrix}$，初等变换得$r(M)=n+r(AB)$，又$r(M)\ge r(A)+r(B)$ → 得证。

## Question 11 - 实对称正交 [analysis]
> 证明实对称阵不同特征值的特征向量正交。

> [!answer]- 答案
> $x_1^TAx_2 = \lambda_2(x_1^Tx_2) = (Ax_1)^Tx_2 = \lambda_1(x_1^Tx_2)$ → $(\lambda_1-\lambda_2)x_1^Tx_2=0$ → $x_1^Tx_2=0$

## Question 12 - 正定性证明 [analysis]
> $B$列满秩，证$A=B^TB$正定。

> [!answer]- 答案
> $x^TAx=\|Bx\|^2\ge0$。$B$列满秩+$x\neq0 \Rightarrow Bx\neq0 \Rightarrow \|Bx\|^2>0$。得证。
