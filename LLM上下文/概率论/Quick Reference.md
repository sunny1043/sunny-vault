---
source: 考研通用大纲(同济《概率论与数理统计》前 5 章)
type: quick-ref
subject: 概率论
date: 2026-07-03
keywords:
  - quick-reference
  - formula
  - probability
tags:
  - quick-ref
  - probability
---

# 概率论 Quick Reference

> 🧭 首页 [[LLM上下文/index|StudyVault]] · 学科导航 [[LLM上下文/概率论/概率论 MOC|概率论 MOC]]

#dashboard #quick-reference #probability

## Ch1 → [[笔记/数学/概率论/第1章_随机事件与概率|第1章 随机事件与概率]]

### 事件运算

| 运算 | 含义 | 记号 |
|------|------|------|
| 和(并) | 至少一个发生 | $A\cup B$ |
| 积(交) | 同时发生 | $A\cap B=AB$ |
| 差 | A 发生 B 不发生 | $A-B=A\bar B$ |
| 对立 | $A\cup B=\Omega, AB=\emptyset$ | $B=\bar A$ |

**德摩根律**:
$$\overline{A\cup B}=\bar A\cap \bar B,\quad \overline{A\cap B}=\bar A\cup \bar B$$

### 概率

| 名称 | 公式 |
|------|------|
| 古典概型 | $P(A)=\dfrac{k}{n}$ |
| 几何概型 | $P(A)=\dfrac{m(A)}{m(\Omega)}$ |
| 对立公式 | $P(\bar A)=1-P(A)$ |
| 加法公式 | $P(A\cup B)=P(A)+P(B)-P(AB)$ |
| 条件概率 | $P(A\mid B)=\dfrac{P(AB)}{P(B)}$ |
| 乘法 | $P(AB)=P(B)P(A\mid B)$ |
| 全概率 | $P(A)=\sum_i P(B_i)P(A\mid B_i)$ |
| 贝叶斯 | $P(B_k\mid A)=\dfrac{P(B_k)P(A\mid B_k)}{\sum_i P(B_i)P(A\mid B_i)}$ |

### 独立 vs 互斥
- 独立:$P(AB)=P(A)P(B)$
- 独立 ⟹ 不互斥(若 $P>0$);互斥 ⟹ 不独立(若 $P>0$)
- n 个事件相互独立 ⟹ 两两独立,反之未必

### 伯努利概型
$$P(X=k)=C_n^k p^k q^{n-k},\quad k=0,1,\dots,n$$

---

## Ch2 → [[笔记/数学/概率论/第2章_一维随机变量及其分布|第2章 一维随机变量及其分布]]

### 分布函数三性质
1. 单调非减、2. 右连续、3. $F(-\infty)=0,\ F(+\infty)=1$
$$P\{a<X\le b\}=F(b)-F(a)$$

### 离散分布

| 分布 | 律 | $EX$ | $DX$ |
|------|----|------|------|
| 0-1 | $P\{X=1\}=p$ | $p$ | $pq$ |
| 二项 $B(n,p)$ | $C_n^k p^k q^{n-k}$ | $np$ | $npq$ |
| 泊松 $P(\lambda)$ | $\dfrac{\lambda^k e^{-\lambda}}{k!}$ | $\lambda$ | $\lambda$ |
| 几何 | $q^{k-1}p$ | $1/p$ | $q/p^2$（source:: 待核） |

### 连续分布

| 分布 | $f(x)$ | $EX$ | $DX$ | 性质 |
|------|--------|------|------|------|
| 均匀 $U(a,b)$ | $\dfrac{1}{b-a}$, $x\in[a,b]$ | $\dfrac{a+b}{2}$ | $\dfrac{(b-a)^2}{12}$ | — |
| 指数 $Exp(\lambda)$ | $\lambda e^{-\lambda x}$, $x\ge 0$ | $\dfrac{1}{\lambda}$ | $\dfrac{1}{\lambda^2}$ | **无记忆性** |
| 正态 $N(\mu,\sigma^2)$ | $\dfrac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$ | $\mu$ | $\sigma^2$ | 标准化 $Z=\dfrac{X-\mu}{\sigma}\sim N(0,1)$ |

### 泊松定理
$B(n,p_n) \xrightarrow{d} P(\lambda)$,其中 $n p_n\to \lambda$。

### 随机变量函数的分布
- 离散: 列表法
- 连续通用: $F_Y(y)=P\{g(X)\le y\} \to f_Y(y)=F_Y'(y)$
- 单调公式: $f_Y(y)=f_X(h(y))\, |h'(y)|$
- 线性变换: $Y=aX+b \Rightarrow f_Y(y)=\dfrac{1}{|a|}\, f_X\!\left(\dfrac{y-b}{a}\right)$
- 正态线性和: $Y=aX+b \sim N(a\mu+b,\ a^2\sigma^2)$

---

## Ch3 → [[笔记/数学/概率论/第3章_多维随机变量及其分布|第3章 多维随机变量及其分布]]

### 联合 → 边缘 → 条件
- 边缘(离散求和、连续积分): $f_X(x)=\int f(x,y)\, dy$
- 条件密度(连续): $f_{X|Y}(x|y)=\dfrac{f(x,y)}{f_Y(y)}$
- 独立时: 条件 = 边缘

### 独立性三式
- 函数: $F(x,y)=F_X(x)F_Y(y)$
- 离散: $p_{ij}=p_{X\cdot i}\, p_{\cdot jY}$
- 连续: $f(x,y)=f_X(x)f_Y(y)$

### 二维正态关键
- $(X,Y)\sim N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$
- **$\rho=0 \Leftrightarrow$ 独立 $\Leftrightarrow$ 不相关**
- $aX+bY \sim$ 正态(二维正态时)

### 二维随机变量函数
- $Z=X+Y$ (独立时): $f_Z(z)=\int f_X(x)f_Y(z-x)\, dx$
- $Z=\max(X,Y)$: $F_Z(z)=F_X(z)F_Y(z)$
- $Z=\min(X,Y)$: $F_Z(z)=1-[1-F_X(z)][1-F_Y(z)]$

---

## Ch4 → [[笔记/数学/概率论/第4章_随机变量的数字特征|第4章 随机变量的数字特征]]

### 期望
$$EX=\sum x_k p_k,\quad EX=\int x f(x)\, dx$$
- 要求**绝对收敛**
- 线性性无条件: $E(aX+bY+c)=a\, EX+b\, EY+c$
- $E(XY)=EX\cdot EY$ **需独立**

### 方差
$$D(X)=E(X-EX)^2,\quad ==DX=EX^2-(EX)^2==$$
- $D(aX+b)=a^2 DX$
- 独立时: $D(X\pm Y)=DX+DY$
- 一般: $D(X\pm Y)=DX+DY\pm 2\,\mathrm{cov}(X,Y)$

### 协方差与相关系数
$$\mathrm{cov}(X,Y)=E(XY)-EX\cdot EY$$
$$\rho_{XY}=\dfrac{\mathrm{cov}(X,Y)}{\sqrt{DX\cdot DY}}\in[-1,1]$$
- $|\rho|=1 \Leftrightarrow$ 线性关系(a.s.)
- $\rho=0 \Leftrightarrow$ 不相关
- **独立 ⟹ 不相关;反之未必**(二维正态是反例,使三者等价)

### 切比雪夫不等式
$$P\{|X-EX|\ge \varepsilon\}\le \dfrac{DX}{\varepsilon^2}$$

---

## Ch5 → [[笔记/数学/概率论/第5章_大数定律与中心极限定理|第5章 大数定律与中心极限定理]]

### 大数定律三大定理(对比表)

| 定律 | 条件 | 结论 |
|------|------|------|
| ==切比雪夫== | 独立,$DX_i\le C$ | $\overline X_n-\overline{EX}_n\xrightarrow{P}0$ |
| ==辛钦== | i.i.d.,$EX_i=\mu$ 存在(不要方差) | $\overline X_n\xrightarrow{P}\mu$ |
| ==伯努利== | i.i.d. $B(1,p)$, n 重伯努利 | $n_A/n\xrightarrow{P} p$ |

关系: 伯努利 ⊂ 辛钦 ⊂ 切比雪夫特殊化。

### 中心极限定理

| 定理 | 条件 | 结论 |
|------|------|------|
| 林德伯格-列维 | i.i.d.,$EX=\mu,DX=\sigma^2$ 有限 | $\dfrac{\sum X_k - n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$ |
| 棣莫弗-拉普拉斯 | $Y_n\sim B(n,p)$ | $\dfrac{Y_n-np}{\sqrt{npq}}\xrightarrow{d}N(0,1)$ |

### 依概率收敛定义
$$X_n \xrightarrow{P} a \;\Leftrightarrow\; \forall\varepsilon>0:\ \lim_{n\to\infty}P\{|X_n-a|<\varepsilon\}=1$$

### 实务判定
- 泊松近似二项: $n$ 大 $p$ 小, $np\to\lambda$
- 正态近似二项: $n$ 大 $p$ 不太小, 经验 $np\ge 5,\ nq\ge 5$ (source:: 待核)