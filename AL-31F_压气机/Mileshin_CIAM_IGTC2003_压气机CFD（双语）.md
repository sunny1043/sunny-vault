---
tags:
  - 航空发动机
  - 压气机
  - CFD
  - 离心压气机
  - 叶轮设计
  - Navier-Stokes求解器
created: 2026-06-17
source: IGTC 2003 Tokyo TS-043 / CIAM (Central Institute of Aviation Motors)
author: Victor I. Mileshin, Andrew N. Startsev, Igor K. Orekhov
---

# 8:1 增压比离心压气机的CFD设计
# CFD Design of a 8:1 Pressure Ratio Centrifugal Compressor

> **来源 Source:** Proceedings of the International Gas Turbine Congress 2003 Tokyo, November 2-7, 2003 — IGTC2003Tokyo TS-043
> **作者 Authors:** Victor I. MILESHIN, Andrew N. STARTSEV, Igor K. OREKHOV
> **单位 Affiliation:** Central Institute of Aviation Motors (CIAM 俄罗斯中央航空发动机研究院), 2, Aviamotornaya St., 111116, Moscow, RUSSIA
> Phone: +7 095-362-21-94, FAX: +7 095-361-66-96, E-mail: mileshin@ciam.ru
> Copyright © 2003 by GTSJ — Manuscript received on July 3, 2003

---

## 摘要 ABSTRACT

**English:** The problem of this paper is aerodynamic design of 8:1 pressure ratio centrifugal compressor possessing high performance. Design target is to achieve 81 – 82% adiabatic efficiency for 1.5 – 2.8 kg/s corrected mass flow-rate.

**中文：** 本文研究的问题是具有高性能的 8:1 增压比离心压气机的气动设计。设计目标是在 1.5 – 2.8 kg/s 的换算质量流量下实现 81 – 82% 的绝热效率(adiabatic efficiency)。

---

**English:** This investigation is a part of research program started in 1997 consisting in N-S design and numerical evaluation with subsequent tests of centrifugal compressors of successively increasing total pressure ratio. Perfection of numerical quasi-3D design tool accompanied extensive numerical study of 3D viscous flow peculiarities. Obtained understanding generated design ideas embodied in hardware and checked experimentally.

**中文：** 本项研究是始于 1997 年的一项研究计划的一部分，该计划包括对总增压比逐级递增的离心压气机进行 N-S(Navier-Stokes)设计与数值评估，并随后进行试验。对数值准三维(quasi-3D)设计工具的完善，伴随着对三维粘性流动(3D viscous flow)特性的广泛数值研究。所获得的认识产生了设计思想，这些思想被体现在硬件中并通过试验加以验证。

---

**English:** First, this paper outlines 3D Navier-Stokes solver validation by the example of 6.5:1 total pressure ratio compressor. Then it describes impeller design procedure using quasi-3D inverse code, vaneless diffuser design based on shroud reverse flow's control and numerically obtained performances of designed 8:1 total pressure ratio compressor now put into manufacturing.

**中文：** 首先，本文以 6.5:1 总增压比压气机为例，概述了三维 Navier-Stokes 求解器的验证。然后，描述了采用准三维反命题程序(inverse code)的叶轮(impeller)设计流程、基于机匣回流(shroud reverse flow)控制的无叶扩压器(vaneless diffuser)设计，以及目前已投入制造的所设计 8:1 总增压比压气机的数值计算性能。

---

## 符号说明 NOMENCLATURE

| 符号 Symbol | 含义 Definition |
| --- | --- |
| $\pi^*_c$ | 压气机总增压比 total pressure ratio of compressor |
| $\eta_{ad}$, ETAad | 压气机绝热效率 adiabatic efficiency of compressor |
| $Q$ | 换算质量流量 corrected mass flow rate |
| $Q_{ref}$ | 参考质量流量（约 2 kg/s）reference mass flow rate (near 2 kg/s) |
| $\alpha, \beta_{blade}$ | 相对叶栅前缘测量的叶片角 blade angle, measured relative to cascade front |
| $D$ | 直径 diameter |
| $F$ | 横截面积 cross-section area |
| $r$ | 半径 radius |
| $P$ | 静压 static pressure |
| $\rho$ | 密度 density |
| $\Omega$ | 叶轮转速 rotational speed of impeller |
| $P_0$ | 压气机进口总压 total pressure at the inlet of compressor |
| $T_0$ | 压气机进口总温 total temperature at the inlet of compressor |
| $R$ | 气体常数 gas constant |
| $k$ | 比热比 specific heat ratio |
| $\rho^*$ | 临界密度 critical density $= P_0/(RT_0)\,(2/(k+1))^{1/(k-1)}$ |
| $(a^*)^2$ | 临界速度的平方 square of critical speed $= RT_0(2k/(k+1))$ |

**下标 Subscript**

| 下标 | 含义 |
| --- | --- |
| 1 | 叶轮进口 impeller inlet |
| 2 | 叶轮出口 impeller exit |
| 3 | 有叶扩压器进口 vaned diffuser inlet |
| 4 | 有叶扩压器出口 vaned diffuser outlet |

---

## 引言 INTRODUCTION

**English:** At the present time there is a strong tendency toward detailed experimental measurements and numerical analysis of 3D viscous flow field within high-pressure centrifugal compressors. This causes to anticipate that in the near future centrifugal compressor performances will be raised due to understanding of viscous flow peculiarities.

**中文：** 当前，对高压离心压气机内部三维粘性流场进行详细试验测量和数值分析的趋势十分强烈。这使人预期，在不久的将来，由于对粘性流动特性的理解，离心压气机的性能将得到提升。

---

**English:** Extensive numerical practice strengthened by investigations of other authors suggests us how to control some observed viscous flow phenomena. Particular emphasis has been placed on the mouth and throat of inducer (shock pattern, control of tip leakage), on the exit of impeller (reverse flow within tip clearance), on shroud of vaneless diffuser (reverse flow) and on the semi-vaneless space of vane diffuser (inlet Mach number and flow angle spanwise distributions).

**中文：** 广泛的数值实践，加之其他作者的研究，启发我们如何控制某些观察到的粘性流动现象。研究重点特别放在以下方面：诱导轮(inducer)的入口与喉部（激波形态、叶尖泄漏(tip leakage)控制）、叶轮出口（叶尖间隙内的回流）、无叶扩压器机匣（回流），以及有叶扩压器的半无叶空间(semi-vaneless space)（进口马赫数及流动角沿叶高的分布）。

---

**English:** Idea applied to design the impeller tip section was to minimize passage shock intensity. It has been accomplished using concept of "supersonic diffuser with long throat" proposed by Kantrowitz (1947) which relates minimum intensity of shock wave to the length of channel ensuring shock stability to compression pulses. Considering impeller as a rotating diffuser with a long blade-to-blade channel and implementing rational passage area variations (Wadia and Copenhaver (1996)) one can construct tip cascade with different shock patterns: one-shock with supersonic flow in the throat and double-shock with two weak shock waves - ahead of the passage and at the exit of inducer. The last shock pattern corresponds to the mentioned "long-throat" concept and minimizes shock losses.

**中文：** 应用于叶轮叶尖剖面设计的思想是使流道激波强度最小化。这是借助 Kantrowitz(1947)提出的"带长喉道的超声速扩压器(supersonic diffuser with long throat)"概念实现的，该概念将激波最小强度与流道长度相关联，从而确保激波对压缩脉动的稳定性。将叶轮视为带有长叶间流道的旋转扩压器，并采用合理的流道面积变化(Wadia 和 Copenhaver (1996))，可以构造出具有不同激波形态的叶尖叶栅：一种是喉部内为超声速流动的单激波(one-shock)，另一种是带有两道弱激波的双激波(double-shock)——一道在流道之前，一道在诱导轮出口。后一种激波形态对应于前述的"长喉道"概念，并使激波损失最小化。

---

**English:** We base impeller design procedure on careful design of cascade located at 90% of blade height. To prevent choice of passage area variation and lighten the impeller design efforts, viscous CFD inverse code is called to substitute iterative search by a clear design process. This is the way to obtain adequate blading within competitive development times. Designed impeller viscous flow was checked using 3D N-S solver. Shock pattern obtained by inverse quasi-3D solver without regard to tip leakage is double-shock. But in case of 3D viscous flow the second shock wave located at the exit of inducer decays to subsonic domain of strong diffusion. Thus the term "double-compression" is used to describe the flow pattern.

**中文：** 我们将叶轮设计流程建立在对位于 90% 叶高处叶栅的精心设计之上。为避免对流道面积变化的人为选择并减轻叶轮设计工作量，我们调用粘性 CFD 反命题程序，以清晰的设计过程取代迭代搜索。这是在具有竞争力的研发周期内获得合适叶型的方法。所设计叶轮的粘性流动采用三维 N-S 求解器进行了校核。由反命题准三维求解器（未考虑叶尖泄漏）得到的激波形态为双激波。但在三维粘性流动情形下，位于诱导轮出口处的第二道激波衰减为强扩散的亚声速区域。因此采用"双重压缩(double-compression)"一词来描述这种流动形态。

---

**English:** Applied design and analysis codes are the software packages developed in CIAM. Experimental centrifugal compressors of 6.5:1 and 8:1 pressure ratio (not the compressor under consideration) have been tested to validate codes.

**中文：** 所采用的设计与分析程序是 CIAM 开发的软件包。已对 6.5:1 和 8:1 增压比的试验离心压气机（并非本文所研究的压气机）进行了试验，以验证这些程序。

---

**English:** Impeller "double-compression" structure is attractive not only due to minimum shock losses but also due to minimum pressure-driven tip leakage. Tip leakage control enhances stability range of compressor.

**中文：** 叶轮的"双重压缩"结构之所以具有吸引力，不仅因为其激波损失最小，还因为其压力驱动的叶尖泄漏最小。叶尖泄漏控制可以扩展压气机的稳定工作范围。

---

**English:** Vaneless diffuser and impeller exit is the second region of the compressor received the designer's attention. 3D viscous flow analysis of initial design highlighted reverse flow on shroud of vaneless diffuser. Separation bubble squeezes the vaneless diffuser channel and causes unfavourable supersonic flow at the inlet of vane diffuser.

**中文：** 无叶扩压器与叶轮出口是设计者关注的第二个区域。对初始设计进行的三维粘性流动分析突显出无叶扩压器机匣上的回流。分离泡(separation bubble)挤压了无叶扩压器流道，并在有叶扩压器进口处引起不利的超声速流动。

---

**English:** As a rule, shroud flow separation is related to high deceleration within impeller due to large exit width of impeller (see Eisenlohr et al. (2002)). To prevent excessive flow deceleration on shroud of impeller it seems useful to reduce the height of impeller blade at the exit. But in this case vane diffuser blade height becomes also reduced. It reduces stability margin of compressor at low impeller speed.

**中文：** 通常，机匣流动分离与叶轮内因出口宽度过大而导致的强烈减速有关（参见 Eisenlohr 等人 (2002)）。为防止叶轮机匣上的过度流动减速，减小叶轮出口处的叶片高度似乎是有益的。但在这种情况下，有叶扩压器的叶片高度也会随之减小。这会降低压气机在低叶轮转速下的稳定裕度。

---

**English:** On the contrary, it is better to raise exit height and, if needed, accompany it by reduction of exit blade angle to maintain flow diffusion. Increased exit height enables to make a conical shroud of vaneless diffuser and, in the same time, maintains vane diffuser width. Vaneless diffuser conicity and increased work input due to raised blade height at the impeller exit suppress flow separation and eliminate vane flow squeezing at the inlet of vane diffuser.

**中文：** 相反，更好的做法是提高出口高度，必要时辅以减小出口叶片角以维持流动扩压。增大的出口高度使无叶扩压器机匣可做成锥形，同时维持有叶扩压器的宽度。无叶扩压器的锥度以及因叶轮出口叶片高度增大而提高的功输入，可抑制流动分离并消除有叶扩压器进口处的流道挤压。

---

**English:** Detailed description of design of the 8:1 pressure ratio centrifugal compressor is preceded by 3D N-S code validation.

**中文：** 在详细描述 8:1 增压比离心压气机的设计之前，先进行三维 N-S 程序的验证。

---

## 三维粘性流动求解器 3D VISCOUS FLOW SOLVER

**English:** Computations were performed using "3D-IMP-MULTI" N-S solver developed in CIAM and intended for analysis of 3D viscous flow through a multi-row passage. Finite volume discretization applies the 3rd order spatial accurate Godunov's method based on exact resolution of a Riemann problem with implicit time-marching procedure and Total Variation Diminishing concept. To treat viscous flow, the Reynolds-averaged Navier-Stokes equations closed by algebraic Baldwin-Lomax turbulence model are implemented. Viscous flow is assumed fully turbulent. Wall shear stress is determined using "wall functions" approach by assuming that the first calculation point lies in the logarithmic region of a turbulent boundary layer.

**中文：** 计算采用 CIAM 开发的 "3D-IMP-MULTI" N-S 求解器进行，该求解器用于分析多排流道内的三维粘性流动。有限体积离散采用基于 Riemann 问题精确求解的三阶空间精度 Godunov 方法，配合隐式时间推进(time-marching)过程及总变差减小(Total Variation Diminishing, TVD)概念。为处理粘性流动，采用了由代数 Baldwin-Lomax 湍流模型封闭的雷诺平均 Navier-Stokes 方程。假设粘性流动为完全湍流。壁面剪切应力采用"壁面函数(wall functions)"方法确定，假设第一个计算点位于湍流边界层的对数区。

---

**English:** Inlet boundary conditions are total pressure, total temperature and flow angles' radial distributions. At outlet, static pressure distribution is imposed and calculated from given static pressure on hub (named backpressure) and radial equilibrium equation. Periodic boundary condition is set at periodic boundaries. Tip clearance is treated as a periodic boundary. To set boundary conditions at the interface between bladed row's flow domains, a mixing plane approach is used.

**中文：** 进口边界条件为总压、总温及流动角的径向分布。在出口处，施加静压分布，该分布由给定的轮毂处静压（称为背压(backpressure)）和径向平衡方程计算得出。在周期性边界上设置周期性边界条件。叶尖间隙作为周期性边界处理。为设置叶排流场域之间交界面上的边界条件，采用了掺混平面(mixing plane)方法。

---

**English:** H-type grid with 32x32 points in the pitchwise and spanwise directions is used for discretization of each blade-to-blade channel. The number of channels is three (for example, the number of channels is three in case of impeller with two splitters). 3 cells are included in the tip gap.

**中文：** 每个叶间流道的离散采用在节距方向和叶高方向上各为 32×32 个点的 H 型网格。流道数量为三（例如，对于带两个分流叶片的叶轮，流道数量为三）。叶尖间隙内包含 3 个网格单元。

---

**English:** This 3D viscous flow solver was used to calculate both flow details and map of compressor performances up to the stability limit. As is known, using steady flow solver it is not possible to simulate unsteady phenomena close to compressor surge. However, difference between numerical and experimental stall inception can be diminished by the fine step-by-step increase of backpressure. Examples of axial and centrifugal stages' 3D viscous flow analysis compared with experimental measurements have been presented in Mileshin et al. (2001).

**中文：** 该三维粘性流动求解器被用于计算流动细节以及压气机性能图（直至稳定极限）。众所周知，使用定常流动求解器无法模拟接近压气机喘振(surge)时的非定常现象。然而，通过精细的逐步增大背压，可以缩小数值与试验失速(stall)起始之间的差异。轴流级和离心级三维粘性流动分析与试验测量结果对比的实例已在 Mileshin 等人 (2001) 中给出。

---

**English:** As applied to centrifugal compressors, experimental compressors of 6.5:1 and 8:1 pressure ratio were tested and calculated to validate the code. One of them, 6.5:1 centrifugal compressor, demonstrated the best quantitative agreement of experimental performances with computed. Fortunately, design idea of the compressor is closely related to the 8:1 centrifugal compressor design being the subject of this paper.

**中文：** 就离心压气机而言，对 6.5:1 和 8:1 增压比的试验压气机进行了试验和计算以验证程序。其中之一，即 6.5:1 离心压气机，展示出试验性能与计算性能之间最佳的定量吻合。幸运的是，该压气机的设计思想与本文主题——8:1 离心压气机设计——密切相关。

---

### 6.5:1 增压比压气机 6.5:1 PRESSURE RATIO COMPRESSOR

**English:** The 6.5:1 total pressure ratio centrifugal compressor is intended for APU (auxiliary power unit) and consists of an axial air intake, impeller having 30 blades (15 full blades, 15 splitter blades), tandem vane diffuser having 28 blades and 68 axial guide vanes. Design data of impeller are given in Table 1.

**中文：** 该 6.5:1 总增压比离心压气机用于辅助动力装置(APU, auxiliary power unit)，由轴向进气道、具有 30 个叶片（15 个全叶片、15 个分流叶片(splitter blades)）的叶轮、具有 28 个叶片的串列(tandem)有叶扩压器以及 68 个轴向导叶组成。叶轮的设计数据见表 1。

---

**English:** *Fig. 1* shows computed and experimental performances of the 6.5:1 total pressure ratio centrifugal compressor demonstrating satisfactory agreement of obtained data. This agreement confirms validity of the N-S solver, although for other compressors 1% discrepancy in efficiency usually takes place.

**中文：** *图 1* 给出了 6.5:1 总增压比离心压气机的计算性能与试验性能，展示了所获数据的令人满意的吻合。这种吻合证实了 N-S 求解器的有效性，尽管对于其他压气机通常会出现 1% 的效率偏差。

---

**English:** Experimental 6.5:1 compressor demonstrates high performances. At design point $\pi^*_c = 6.48$ its adiabatic efficiency is 82%. Stability margin at design rpm is more than 12%. This compressor is a good prototype for design of centrifugal compressor with 8:1 total pressure ratio.

**中文：** 试验 6.5:1 压气机展现出高性能。在设计点 $\pi^*_c = 6.48$ 处，其绝热效率为 82%。设计转速下的稳定裕度(stability margin)超过 12%。该压气机是设计 8:1 总增压比离心压气机的良好原型。

---

**English:** Excellent compressor aerodynamics provides high experimental performances. Mach level lines at the tip of impeller at design rotational speed (see Fig.2) explain one of the reasons of high efficiency of this compressor - low intensity shock wave located in diverging blade-to-blade channel. Pre-shock Mach number equals to 1.2. Mach level lines' trough swept from the suction side of main blade indicates tip leakage. Other reason of high efficiency is proper design of double-row vane diffuser ensuring effective total pressure recovery.

**中文：** 优异的压气机气动特性带来了高的试验性能。设计转速下叶轮叶尖处的马赫数等值线(Mach level lines)（见图 2）解释了该压气机高效率的原因之一——位于扩张型叶间流道中的低强度激波。激波前马赫数等于 1.2。从主叶片吸力面(suction side)扫出的马赫数等值线波谷表明了叶尖泄漏的存在。高效率的另一个原因是双排有叶扩压器的合理设计，确保了有效的总压恢复。

---

**English:** Concerning validity of the N-S solver, computed near-stall points of characteristics clarify initiation of instability of the compressor and indicate a limitation of the N-S solver.

**中文：** 关于 N-S 求解器的有效性，特性线上计算得到的近失速点阐明了压气机不稳定性的起始，同时也表明了 N-S 求解器的局限性。

---

**English:** At intermediate rotational speed (i.e. 90%, 75% and 50% of design rpm) flow calculations indicate part-span impeller stall (see fig.3). Stall region locates near impeller leading edge on shroud and grows larger as the compressor is throttled until a much larger separation zone erupts and computation process fails.

**中文：** 在中等转速（即设计转速的 90%、75% 和 50%）下，流动计算表明了叶轮的部分叶高失速(part-span stall)（见图 3）。失速区位于机匣上叶轮前缘(leading edge)附近，随着压气机被节流而增大，直至一个大得多的分离区爆发，计算过程失败。

---

**English:** The mild and progressive nature of the phenomena at the early stage of stall development suggests that it is an incidence-caused, with separation zone extending as the compressor is throttled (see fig.3).

**中文：** 在失速发展早期阶段，该现象温和而渐进的特性表明，这是由攻角(incidence)引起的失速，且随着压气机被节流，分离区不断扩展（见图 3）。

---

**English:** During the 3D viscous flow calculations the range of flow-rate, where progressive stall can take place, becomes more and more narrow as the rpm decreases. It is due to a numerical stall described by Denton (1990). According to Denton, phenomenon of numerical stall arises during the transient part of calculation and is not genuinely exist. Comparison with experimental performances (see fig.1) at 50% of design rpm reveals numerical stall. It can be seen that computed characteristic terminates at a flow-rate that is lower than experimentally measured at stability limit. Thus numerical progressive stall at low speed of impeller is a limitation of the present N-S solver.

**中文：** 在三维粘性流动计算过程中，随着转速降低，可能发生渐进失速的流量范围变得越来越窄。这是由于 Denton(1990)所描述的数值失速(numerical stall)所致。根据 Denton 的观点，数值失速现象出现在计算的瞬态部分，并非真实存在。在设计转速 50% 处与试验性能（见图 1）的对比揭示了数值失速。可以看出，计算特性线终止于一个低于稳定极限处试验测量值的流量。因此，低叶轮转速下的数值渐进失速是当前 N-S 求解器的一个局限。

---

**English:** On fig.1 for 90%, and 75% of design rpm one can find that calculated stability margins are larger than experimental. It is not the fact. Actually the left point of each characteristic is numerically unstable.

**中文：** 在图 1 中，对于设计转速的 90% 和 75%，可以发现计算得到的稳定裕度大于试验值。这并非事实。实际上，每条特性线的左端点在数值上是不稳定的。

---

**English:** Nevertheless, at design rotational speed (see fig.1) a predominance of numerical stability margin over experimental is true, because experimental throttling was been interrupted before surge to prevent impeller failure arising from the high unsteady blade loading caused by rapidly developing pressure disturbances. Numerical instability has been accompanied by a fall of vaneless and vane diffuser total pressure recovery, whereas impeller efficiency was on the rise. Fig.4 confirms that stall of vane diffuser propagating upstream to the vaneless diffuser is the reason of this event, usually named abrupt stall.

**中文：** 然而，在设计转速下（见图 1），数值稳定裕度确实大于试验值，因为试验节流在喘振之前就被中断了，以防止因快速发展的压力扰动引起的高非定常叶片载荷而导致叶轮损坏。数值不稳定伴随着无叶扩压器和有叶扩压器总压恢复的下降，而叶轮效率却在上升。图 4 证实了向上游传播至无叶扩压器的有叶扩压器失速是此事件的原因，通常称为突变失速(abrupt stall)。

---

### 8:1 增压比压气机 8:1 PRESSURE RATIO COMPRESSOR

**English:** The 8:1 total pressure ratio centrifugal compressor is intended for a turbo-shaft engine and consists of a radial air intake duct with 7 struts, impeller having 33 blades (11 full blades, 11 long splitter blades and 11 short splitter blades), vane diffuser having 17 blades and 92 axial vanes. N-S computation predicted at design point $\pi^*_c = 8.1$ adiabatic efficiency equal to 81%. Stability margin at design rpm is more than 23%.

**中文：** 该 8:1 总增压比离心压气机用于涡轴发动机(turbo-shaft engine)，由带 7 个支板(struts)的径向进气道、具有 33 个叶片（11 个全叶片、11 个长分流叶片和 11 个短分流叶片）的叶轮、具有 17 个叶片的有叶扩压器以及 92 个轴向叶片组成。N-S 计算预测在设计点 $\pi^*_c = 8.1$ 处的绝热效率为 81%。设计转速下的稳定裕度超过 23%。

---

**English:** Table 2 contains final design data of impeller. To shape a blade of impeller, quasi-3D viscous inverse design code was used. Tip section of blade (90% of blade height) was tailored to handle a double-shock flow pattern. Being integrated into 3D blade, tip section generates 3D viscous flow in which the second shock wave located at the exit of inducer decays to subsonic domain of strong diffusion. As expected, this "double-compression" flow pattern enhances compressor efficiency and, what is important, diminish tip leakage over an entrance region of blade passage.

**中文：** 表 2 包含叶轮的最终设计数据。为塑造叶轮叶片，采用了准三维粘性反命题设计程序。叶片的叶尖剖面（90% 叶高处）经过裁剪以处理双激波流动形态。将该叶尖剖面集成到三维叶片中后，会产生三维粘性流动，其中位于诱导轮出口处的第二道激波衰减为强扩散的亚声速区域。正如预期，这种"双重压缩"流动形态提升了压气机效率，更重要的是，减小了叶片流道进口区域上的叶尖泄漏。

---

**English:** Fig.5 shows two non-dimensional (denominator is $\rho^*(a^*)^2$) static pressure distributions obtained from 3D viscous flow computation: custom static pressure distribution on suction and pressure sides of airfoil (90% of blade height) and distribution obtained for impeller blade with inverse designed cascade. It can be seen that "double-compression" cascade has a domain (from 0.15 to 0.35 of blade meridional length) where static pressure difference is small. Fig.6 and 7 demonstrates corresponding Mach number level lines. Tip leakage vortex is well identified as a strip of closeness of level lines for custom cascade (see fig.6). By contrast, "double-compression" cascade Mach number level lines indicate faint tip leakage vortex resulting in enhanced operating range (see fig.7).

**中文：** 图 5 给出了由三维粘性流动计算得到的两种无量纲（分母为 $\rho^*(a^*)^2$）静压分布：常规叶型（90% 叶高处）吸力面和压力面(pressure side)上的静压分布，以及采用反命题设计叶栅的叶轮叶片所得到的分布。可以看出，"双重压缩"叶栅存在一个区域（从叶片子午长度的 0.15 至 0.35），在该区域内静压差很小。图 6 和图 7 展示了相应的马赫数等值线。对于常规叶栅，叶尖泄漏涡(tip leakage vortex)清晰地表现为等值线密集的条带（见图 6）。相比之下，"双重压缩"叶栅的马赫数等值线表明叶尖泄漏涡微弱，从而带来了拓展的工作范围（见图 7）。

---

**English:** Vane diffuser has been designed as one-row instead of double-row diffuser usually recommended for high-pressure centrifugal compressors. Apart from the fact of stability range extension, one-row diffuser allows to diminish radial size of compressor. Table 3 presents vane diffuser design data and data outlining vaneless diffuser.

**中文：** 有叶扩压器被设计为单排(one-row)扩压器，而非通常为高压离心压气机所推荐的双排(double-row)扩压器。除了稳定范围扩展这一事实之外，单排扩压器还能减小压气机的径向尺寸。表 3 给出了有叶扩压器的设计数据以及描述无叶扩压器的数据。

---

**English:** Predicted performances of designed 8:1 total pressure ratio compressor are on fig.11. View of impeller is on fig.12.

**中文：** 所设计 8:1 总增压比压气机的预测性能见图 11。叶轮的视图见图 12。

---

**English:** In what follow we discuss some features of impeller, vaneless and vane diffuser design and review numerically obtained 3D flow structure in impeller, vaneless diffuser and vane diffuser supplementing this insight by addition of some ideas advanced in other papers.

**中文：** 在下文中，我们将讨论叶轮、无叶扩压器和有叶扩压器设计的一些特征，并回顾在叶轮、无叶扩压器和有叶扩压器中数值得到的三维流动结构，同时补充其他论文中提出的一些思想来增进这一认识。

---

## 叶轮叶片设计 IMPELLER BLADE DESIGN

**English:** To begin the design process initial guess of impeller blade geometry is generated to calculate initial 3D viscous flow field and axisymmetric stream surfaces. Assuming that the flow through the cascade has axisymmetric stream surfaces and that the flow on these surfaces can be treated as two-dimensional, near-shroud cascade of impeller located at 90% of the blade height is re-designed using quasi-3D viscous inverse design code (an example of redesign using quasi-3D inviscid flow inverse design solver is in Mileshin et al. (1999), quasi-3D viscous inverse design method is in Mileshin et al. (2003)) through modification and application of the reduced static pressure $p_{red} = p - \rho(\Omega r)^2/2$ distribution along the near-shroud section of impeller blade. As a rule, thickness of impeller is a strength analysis output and only static pressure distribution along suction side of the blade section is modified. Thus only suction side of blade section is determined aerodynamically whereas pressure side is tailored geometrically so that famous problem of blade section closeness is eliminated.

**中文：** 为开始设计过程，先生成叶轮叶片几何的初始猜测，以计算初始三维粘性流场和轴对称流面(axisymmetric stream surfaces)。假设通过叶栅的流动具有轴对称流面，且这些流面上的流动可作为二维处理，则采用准三维粘性反命题设计程序，对位于 90% 叶高处的叶轮近机匣叶栅进行重新设计（采用准三维无粘流反命题设计求解器进行重新设计的实例见 Mileshin 等人 (1999)，准三维粘性反命题设计方法见 Mileshin 等人 (2003)），方法是修改并应用沿叶轮叶片近机匣剖面的折合静压(reduced static pressure) $p_{red} = p - \rho(\Omega r)^2/2$ 分布。通常，叶轮的厚度是强度分析的输出，仅修改叶片剖面吸力面上的静压分布。因此，仅吸力面通过气动方式确定，而压力面通过几何方式裁剪，从而消除了著名的叶片剖面闭合(blade section closeness)问题。

---

**English:** The impeller blade is developed as a ruled surface by linear connection of near-shroud and hub section points. Hub section of the impeller blade is determined geometrically by already obtained near-shroud section through the satisfaction of strength requirements (controlling the blade deviation from radial direction in the vicinity of its leading edge and so on). In doing so, hub and near-shroud sections are stacked by rotating them in the circumferential direction to achieve given lean angle of the blade trailing edge.

**中文：** 叶轮叶片由近机匣剖面点与轮毂剖面点的线性连接构成直纹面(ruled surface)。叶轮叶片的轮毂剖面通过已获得的近机匣剖面、在满足强度要求（控制叶片在其前缘附近偏离径向的程度等）的条件下以几何方式确定。在此过程中，轮毂剖面和近机匣剖面通过沿周向旋转进行积叠(stacked)，以实现叶片尾缘(trailing edge)给定的倾斜角(lean angle)。

---

**English:** 3D viscous flow analysis after completion of the blade design provides a guideline for the next design attempt.

**中文：** 叶片设计完成后的三维粘性流动分析为下一次设计尝试提供了指导。

---

**English:** As required, at the design point, maximum relative Mach number for tip cascade of impeller is slightly more than 1.2, so that viscous boundary layer remains attached despite adverse pressure gradient and "double-compression" is constituted by a weak shock originated at the leading edge of main blade and a zone of subsonic flow deceleration in the vicinity of splitter blade. Nevertheless, at higher rotational speed (105% rpm) throat flow is supersonic (see fig.8). As mentioned, "double-compression" impeller requires careful design to prevent leading edge shock unstart.

**中文：** 按要求，在设计点处，叶轮叶尖叶栅的最大相对马赫数略大于 1.2，使得粘性边界层尽管面临逆压梯度仍保持附着，且"双重压缩"由起源于主叶片前缘的一道弱激波和分流叶片附近的亚声速流动减速区构成。然而，在更高转速（105% 转速）下，喉部流动为超声速（见图 8）。如前所述，"双重压缩"叶轮需要精心设计，以防止前缘激波不起动(shock unstart)。

---

## 叶轮流场 IMPELLER FLOW FIELD

**English:** Kang and Hirsch (1995) presented detailed information on tip leakage flow structure. They noticed that relative motion of the shroud wall generates skewing of the inlet endwall boundary layer. As a result, leakage vortex core trajectory is swept strongly from the suction side corner toward the pressure side. Because of presence of this primary tip clearance vortex, endwall boundary layer begins to separate and form a region of opposite signed vorticity, named induced vortex by Van Zante et al. (2000). The two counter rotating vortices induce a tip leakage jet between them.

**中文：** Kang 和 Hirsch(1995)给出了关于叶尖泄漏流动结构的详细信息。他们注意到，机匣壁面的相对运动产生了进口端壁边界层(endwall boundary layer)的偏斜。结果，泄漏涡涡核轨迹被强烈地从吸力面角部扫向压力面。由于存在这一主叶尖间隙涡，端壁边界层开始分离，并形成一个反号涡量区域，被 Van Zante 等人 (2000) 称为诱导涡(induced vortex)。这两个反向旋转的涡在它们之间诱导出一股叶尖泄漏射流(tip leakage jet)。

---

**English:** Going from the design point to the stall condition, impeller's leading edge shock wave moves upstream and the value of maximum relative Mach number that reached on the suction side of main blade increases maximizing tip leakage flow in the vicinity of impeller blade leading edge. Trajectory of tip leakage vortex sweeps from suction side. Rotor stall occurs when the tip clearance vortex trajectory comes out from the bladed passage and locates forward of the impeller leading edge (see Van Zante et al. (2000)). Fig. 7 and 10 illustrate variation of numerically obtained impeller tip section flow patterns depending on increasing static pressure at the outlet of compressor. It can be seen (see fig.10) that at the point of the compressor's stall impeller remains un-stalled because tip clearance vortex trajectory remains within blade-to-blade channel.

**中文：** 从设计点向失速状态变化时，叶轮的前缘激波向上游移动，主叶片吸力面上所达到的最大相对马赫数值增大，使得叶轮叶片前缘附近的叶尖泄漏流量最大化。叶尖泄漏涡的轨迹从吸力面扫开。当叶尖间隙涡轨迹移出叶片流道并位于叶轮前缘之前时，转子失速发生（见 Van Zante 等人 (2000)）。图 7 和图 10 展示了数值得到的叶轮叶尖剖面流动形态随压气机出口静压增大的变化。可以看出（见图 10），在压气机失速点处，由于叶尖间隙涡轨迹仍保持在叶间流道内，叶轮仍未失速。

---

**English:** Besides the tip leakage vortex trajectory, tip leakage mass flow-rate is one-more important factor defining tip leakage flow. Kang and Hirsch (1995) separate the leakage flow as pressure-driven flow and moving-wall induced flow. As mentioned, pressure-driven static pressure flow can be controlled by "double-compression" static pressure distribution applied to design of tip section of impeller blade.

**中文：** 除叶尖泄漏涡轨迹之外，叶尖泄漏质量流量是定义叶尖泄漏流动的另一个重要因素。Kang 和 Hirsch(1995)将泄漏流动分为压力驱动流动和动壁诱导流动。如前所述，压力驱动的静压流动可以通过应用于叶轮叶片叶尖剖面设计的"双重压缩"静压分布来加以控制。

---

## 无叶扩压器回流 VANELESS DIFFUSER REVERSE FLOW

**English:** Shroud wall boundary layer flow in vaneless diffuser is highly skewed due to impeller exit flow angle. Development of the shroud secondary flow caused by radial adverse pressure gradient leads to a reverse flow occurring even at the choke point and presenting over the whole operating range.

**中文：** 无叶扩压器中的机匣壁面边界层流动因叶轮出口流动角而高度偏斜。由径向逆压梯度引起的机匣二次流(secondary flow)的发展，导致即使在堵塞(choke)点处也会出现回流，并贯穿整个工作范围。

---

**English:** From common practice it is known that penetration of the shroud reverse flow into the semi-vaneless space of vane diffuser is impermissible. It is due to the fact that separation bubble squeezes the channel and causes unfavourable supersonic flow at the inlet of vane diffuser. Appropriate contraction of vaneless diffuser is useful to prevent. Unfortunately, contraction of vaneless diffuser tightens throat of vane diffuser and thereby makes the low rpm's stability range narrower.

**中文：** 从一般实践中已知，机匣回流渗入有叶扩压器的半无叶空间是不允许的。这是由于分离泡挤压流道并在有叶扩压器进口处引起不利的超声速流动。无叶扩压器的适当收缩(contraction)有助于防止这种情况。遗憾的是，无叶扩压器的收缩会收紧有叶扩压器的喉部，从而使低转速的稳定范围变窄。

---

**English:** On the other hand, it is known (Ishida et al., 2001) that shroud reverse flow region is not an actual stall cell, but the flow instability is two-fold: it arises both as incipient inducer stall cell which grows with flow-rate degradation and as hub flow recirculation upstream of the vane diffuser cascade appearing like a separation bubble on hub of the vaneless diffuser.

**中文：** 另一方面，已知（Ishida 等人，2001）机匣回流区域并非实际的失速团(stall cell)，但流动不稳定性具有双重性：它既表现为随流量退化而增长的初生诱导轮失速团，又表现为有叶扩压器叶栅上游的轮毂流动再循环，后者表现得像无叶扩压器轮毂上的分离泡。

---

**English:** Careful examination of the impeller exit viscous flow suggests that region of high loss of total pressure is formed by tip leakage flow and reverse flow from the impeller exit (Ibaraki et al., 2002). However, while total pressure loss increases, the penetration of shroud reverse flow into the tip clearance space of impeller's exit causes an additional work input (Ziegler et al., 2002). Therefore increased recirculation into the impeller may enhance tendency to quick reattachment of shroud reverse flow.

**中文：** 对叶轮出口粘性流动的仔细检查表明，总压损失高的区域是由叶尖泄漏流动和来自叶轮出口的回流形成的（Ibaraki 等人，2002）。然而，在总压损失增大的同时，机匣回流渗入叶轮出口的叶尖间隙空间会引起附加的功输入（Ziegler 等人，2002）。因此，进入叶轮的再循环增大可能增强机匣回流快速再附着的趋势。

---

**English:** Based on this insight, the following two ideas have been used for the vaneless diffuser design. The first one was to raise impeller exit blade height thus increasing impeller work input. Besides increased impeller exit height enables to make a conical shroud of vaneless diffuser without vane diffuser throat tightening. 3D N-S calculation shows that increased impeller work input and contraction of vaneless diffuser suppress flow separation on its shroud.

**中文：** 基于这一认识，无叶扩压器设计采用了以下两个思想。第一个是提高叶轮出口叶片高度，从而增大叶轮的功输入。此外，增大的叶轮出口高度使无叶扩压器机匣可做成锥形而不必收紧有叶扩压器喉部。三维 N-S 计算表明，增大的叶轮功输入和无叶扩压器的收缩抑制了其机匣上的流动分离。

---

**English:** The second idea was to suppress shroud reverse flow by means of developing hub reverse flow region in course of the compressor throttling. It seems to increase stall margin. Fig.9 demonstrates comparison of numerically obtained vaneless diffuser meridional streamlines generated by initial impeller exit blade height and impeller with increased blade height at the exit. Unquestionably the shroud reverse flow reattachment takes place at smaller radius in case of increased blade height.

**中文：** 第二个思想是通过在压气机节流过程中发展轮毂回流区来抑制机匣回流。这似乎能增大失速裕度。图 9 展示了由初始叶轮出口叶片高度和出口叶片高度增大的叶轮所产生的、数值得到的无叶扩压器子午流线的对比。毫无疑问，在叶片高度增大的情况下，机匣回流的再附着发生在更小的半径处。

---

**English:** Fig.9 also indicates jumping of reverse flow from tip at the point of maximum efficiency to hub at the point of the compressor's stall indicating that hub reverse flow suppresses shroud reverse flow.

**中文：** 图 9 还表明，回流从最大效率点处的叶尖跳跃到压气机失速点处的轮毂，这表明轮毂回流抑制了机匣回流。

---

## 结论 CONCLUSION

**English:** From N-S calculation designed 8:1 total pressure ratio centrifugal compressor provides at design point $\pi^*_c = 8.1$ adiabatic efficiency equal to 81%. Stability margin at design rpm is more than 23%.

**中文：** 根据 N-S 计算，所设计的 8:1 总增压比离心压气机在设计点 $\pi^*_c = 8.1$ 处提供的绝热效率为 81%。设计转速下的稳定裕度超过 23%。

---

**English:** Design has been performed making the following improvements of experimental 6.5:1 compressor used as a prototype and having adiabatic efficiency equal to 82%:

**中文：** 设计以试验 6.5:1 压气机（绝热效率为 82%）为原型，并对其作出了以下改进：

---

**English:** 1) "double-compression" impeller design increases compressor efficiency due to reduction of both shock intensity and pressure-driven tip leakage;

**中文：** 1) "双重压缩"叶轮设计通过降低激波强度和压力驱动的叶尖泄漏二者，提高了压气机效率；

---

**English:** 2) enhanced work input by raised blade height at the exit of impeller and vaneless diffuser contraction prevent flow separation on shroud of vaneless diffuser;

**中文：** 2) 通过提高叶轮出口处的叶片高度而增强的功输入，以及无叶扩压器的收缩，防止了无叶扩压器机匣上的流动分离；

---

**English:** 3) changing double-row diffuser by subsonic one-row vane diffuser provides high total pressure recovery factor, ensures wide stability range and saves radial space;

**中文：** 3) 用亚声速单排有叶扩压器替代双排扩压器，提供了高的总压恢复系数，确保了宽广的稳定范围并节省了径向空间；

---

**English:** 4) during compressor instability inception at design rpm vaneless diffuser flow separation attendant on abrupt stall of vane diffuser has been transferred from shroud to hub.

**中文：** 4) 在设计转速下压气机不稳定起始期间，伴随有叶扩压器突变失速而出现的无叶扩压器流动分离已从机匣转移到轮毂。

---

## 表格 TABLES

### 表 1 Table 1. 6.5:1 增压比压气机叶轮数据 Data of impeller of 6.5:1 pressure ratio compressor

| 参数 Parameter | 数值 Value |
| --- | --- |
| 设计换算质量流量 Design corrected mass flow-rate | > 2.0 kg/s |
| 进口相对轮毂直径 Relative hub diameter at inlet $(D_{hub}/D_{tip})_1$ | 0.42 |
| 出口相对直径 Relative diameter at exit $D_2/D_{tip1}$ | 1.71 |
| 相对轴向长度 Relative axial length $L_{axial}/D_{tip1}$ | 0.513 |
| 前缘叶尖叶片角 Leading edge tip blade angle $(\beta_{blade1})_{tip}$ | 27° |
| 出口叶片角平均值 Mean value of exit blade angle $(\beta_{blade2})$ | 60° |
| $\bar n=1.0$ 时叶尖速度 Tip speed at $\bar n=1.0$ | 570 m/s |

### 表 2 Table 2. 8:1 增压比压气机叶轮数据 Data of impeller of 8:1 pressure ratio compressor

| 参数 Parameter | 数值 Value |
| --- | --- |
| 设计质量流量 Design mass flow-rate | < 2.0 kg/s |
| 进口相对轮毂直径 Relative hub diameter at inlet $(D_{hub}/D_{tip})_{inlet}$ | 0.44 |
| 出口相对直径 Relative diameter at exit $D_2/D_{tipinlet}$ | 1.7 |
| 相对轴向长度 Relative axial length $L_{axial}/D_{tipinlet}$ | 0.427 |
| 前缘叶尖叶片角 Leading edge tip blade angle $(\beta_{1blade})_{tip}$ | 23° |
| 出口叶片角平均值 Mean value of exit blade angle $(\beta_{2blade})$ | 47.8° |
| $\bar n=1.0$ 时叶尖速度 Tip speed at $\bar n=1.0$ | 620 m/s |

### 表 3 Table 3. 8:1 压气机无叶与有叶扩压器数据 Data of vaneless & vane diffuser of 8:1 compressor

| 参数 Parameter | 数值 Value |
| --- | --- |
| 无叶空间相对长度 Relative length of vaneless space $D_3/D_2$ | 1.095 |
| 无叶扩压器收缩角 Angle of vaneless diffuser contraction | 8° |
| 有叶扩压器扩张比 Vane diffuser divergence $F_3/F_4$ | 2.35 |
| 等效扩压器角（有叶扩压器）Angle of equivalent diffuser (vane diffuser) | 5.3° |
| 前缘叶片角 Leading edge blade angle $(\alpha_{blade})_3$ | 14.8° |
| 出口叶片角 Exit blade angle $(\alpha_{blade})_4$ | 25.3° |
| 有叶扩压器喉部面积 / 有叶扩压器进口流动面积 $F_{throat\,of\,vane\,diffuser}/F_{of\,flow\,at\,inlet\,of\,vane\,diffuser}$ | 1.055 |

---

## 图表说明 FIGURE CAPTIONS

**English:** *Fig. 1* Comparison of computed and experimental performances of 6.5:1 pressure ratio compressor. Left point of each numerical characteristic is unstable.

**中文：** *图 1* 6.5:1 增压比压气机计算性能与试验性能的对比。每条数值特性线的左端点是不稳定的。（包含 $\pi^*_c$ 对 $Q/Q_{ref}$ 以及 $\pi^*$ 对 ETAad 的曲线，含 50%/75%/90%/100% 转速的试验与计算结果。）

---

**English:** *Fig.2* Mach level lines on tip. Impeller of 6.5:1 compressor. Design point, 100% rpm.

**中文：** *图 2* 叶尖处的马赫数等值线。6.5:1 压气机叶轮。设计点，100% 转速。

---

**English:** *Fig.3* Mach level lines on suction surface of 6.5:1 impeller. Development of incidence-caused progressive stall at 75% rpm. Above – maximum efficiency, below – surge.

**中文：** *图 3* 6.5:1 叶轮吸力面上的马赫数等值线。75% 转速下由攻角引起的渐进失速的发展。上图——最大效率，下图——喘振。

---

**English:** *Fig.4* Mach level lines on tip. Exit of impeller and double-row vane diffuser of 6.5:1 compressor. Near-surge point, 100% rpm. Abrupt stall – stall of vane diffuser propagates upstream.

**中文：** *图 4* 叶尖处的马赫数等值线。6.5:1 压气机叶轮出口与双排有叶扩压器。近喘振点，100% 转速。突变失速——有叶扩压器失速向上游传播。

---

**English:** *Fig.5* Comparison of non-dimensional (denominator is $\rho^*(a^*)^2$) static pressure distributions on tip of customary designed impeller and impeller designed using viscous quasi-3D inverse procedure.

**中文：** *图 5* 常规设计叶轮叶尖与采用粘性准三维反命题程序设计叶轮叶尖处无量纲（分母为 $\rho^*(a^*)^2$）静压分布的对比。

---

**English:** *Fig.6* Mach level lines on tip of customary designed impeller. Design rpm, at $\pi^*_c = 8.1$. N-S calculated $\eta_{ad} = 80.4\%$.

**中文：** *图 6* 常规设计叶轮叶尖处的马赫数等值线。设计转速，$\pi^*_c = 8.1$ 处。N-S 计算 $\eta_{ad} = 80.4\%$。

---

**English:** *Fig.7* Mach level lines on tip of inverse designed impeller. Design rpm, at $\pi^*_c = 8.1$. N-S calculated $\eta_{ad} = 81.0\%$.

**中文：** *图 7* 反命题设计叶轮叶尖处的马赫数等值线。设计转速，$\pi^*_c = 8.1$ 处。N-S 计算 $\eta_{ad} = 81.0\%$。

---

**English:** *Fig.8* Mach level lines on tip of inverse designed impeller. 105% rpm, at $\pi^*_c = 9.6$. N-S calculated $\eta_{ad} = 79.7\%$.

**中文：** *图 8* 反命题设计叶轮叶尖处的马赫数等值线。105% 转速，$\pi^*_c = 9.6$ 处。N-S 计算 $\eta_{ad} = 79.7\%$。

---

**English:** *Fig.9* Meridional streamlines within vaneless diffuser of 8:1 total pressure ratio compressor at 100% rpm demonstrate effectiveness of measures to suppress vaneless diffuser reverse flow – increase of impeller exit blade height and contraction of vaneless diffuser: a) impeller with initial blade height, design point of compressor ($\pi^*_c = 8.1$, $\eta_{ad}=81\%$), b) impeller with raised blade height increases work input and allows contraction of vaneless diffuser, design point of compressor ($\pi^*_c = 8.1$, $\eta_{ad}=81\%$), c) raised impeller blade height, point of maximum adiabatic efficiency ($\pi^*_c = 8.44$, $\eta_{ad}=81.4\%$), d) raised impeller blade height, abrupt stall of compressor ($\pi^*_c = 8.57$, $\eta_{ad}=80.5\%$). Vane diffuser stall on hub is clearly demonstrated by streamlines departure from hub in the vicinity of vane diffuser's leading edge.

**中文：** *图 9* 100% 转速下 8:1 总增压比压气机无叶扩压器内的子午流线，展示了抑制无叶扩压器回流措施（提高叶轮出口叶片高度和无叶扩压器收缩）的有效性：a) 初始叶片高度的叶轮，压气机设计点（$\pi^*_c = 8.1$，$\eta_{ad}=81\%$）；b) 叶片高度提高的叶轮，增大了功输入并允许无叶扩压器收缩，压气机设计点（$\pi^*_c = 8.1$，$\eta_{ad}=81\%$）；c) 叶轮叶片高度提高，最大绝热效率点（$\pi^*_c = 8.44$，$\eta_{ad}=81.4\%$）；d) 叶轮叶片高度提高，压气机突变失速（$\pi^*_c = 8.57$，$\eta_{ad}=80.5\%$）。有叶扩压器前缘附近流线偏离轮毂，清晰地展示了轮毂上的有叶扩压器失速。

---

**English:** *Fig.10* Mach level lines on tip of impeller of 8:1 total pressure ratio compressor. Raised impeller blade height. Left: point of maximum adiabatic efficiency: $\pi^*_c = 8.44$, $\eta_{ad}=81.4\%$. Corresponds to Fig.9 c). Impeller's shock wave moves upstream, but "double compression" flow pattern remains. Right: abrupt stall of compressor: $\pi^*_c = 8.57$, $\eta_{ad}=80.5\%$. Corresponds to Fig.9 d). Impeller's shock wave moves upstream and its intensity increases. Nevertheless, tip clearance vortex trajectory remains within impeller's bladed passage. Thus compressor surge is due to abrupt stall on hub of vane diffuser, whereas impeller is unstalled.

**中文：** *图 10* 8:1 总增压比压气机叶轮叶尖处的马赫数等值线。叶轮叶片高度提高。左图：最大绝热效率点：$\pi^*_c = 8.44$，$\eta_{ad}=81.4\%$。对应图 9 c)。叶轮激波向上游移动，但"双重压缩"流动形态保持不变。右图：压气机突变失速：$\pi^*_c = 8.57$，$\eta_{ad}=80.5\%$。对应图 9 d)。叶轮激波向上游移动且其强度增大。尽管如此，叶尖间隙涡轨迹仍保持在叶轮叶片流道内。因此，压气机喘振是由有叶扩压器轮毂上的突变失速所致，而叶轮并未失速。

---

**English:** *Fig.11* N-S calculated performances of designed 8:1 total pressure ratio centrifugal compressor calculated for a wide range of rotational speed of impeller n=0.6÷1.05.

**中文：** *图 11* 所设计 8:1 总增压比离心压气机的 N-S 计算性能，针对叶轮转速 n=0.6÷1.05 的宽广范围进行计算（含 $\pi^*_c$ 对 $Q/Q_{ref}$ 以及 $\pi^*_c$ 对 ETAad 的曲线）。

---

**English:** *Fig.12* View of designed impeller of the 8:1 total pressure ratio centrifugal compressor.

**中文：** *图 12* 所设计 8:1 总增压比离心压气机叶轮的视图。

---

## 参考文献 References

Denton, J.D., 1990, "The Calculation of Three Dimensional Viscous Flow Through Multistage Turbomachines", ASME Paper № 90-GT-19.

Eisenlohr, G., Krain, H., Richter, F.-A., and Tiede V., 2002, "Investigation of the Flow through a High Pressure Ratio Centrifugal Compressor", ASME Paper № GT-2002-30394.

Kantrowitz, A., 1947, "The Formation and Stability of Normal Shock Waves in Channel Flows", NACA TN 1225.

Ibaraki, S., Matsuo, T., Kuma, H., Sumida, K., and Suita, T., 2002, "Aerodynamics of a Transonic Centrifugal Compressor Impeller", ASME Paper № GT-2002-30374.

Ishida, M., Sakaguchi, D., and Ueki, H., 2001, "Suppression of Rotating Stall by Wall Roughness Control in Vaneless Diffusers of Centrifugal Blowers", ASME Journal of Turbomachinery, Vol. 123, No. pp. 64-72.

Kang, S., and Hirsch, C., 1995, "Tip Clearance Flow and Loss in Axial Compressor Cascades", CP-571, AGARD PEP 85th Symposium on "Loss Mechanisms and Unsteady Flows in Turbomachines", pp.10-1÷10-15.

Mileshin, V.I, Orekhov, I.K, Pankov, S.V. and Startsev, A.N., 2001, "Computational and Experimental Investigation of High-Pressure Centrifugal Compressors with Ultra-High Rotational Speed", XV International Symposium on Airbreathing Engines, 2001, Bangalore, India, September 2-7, ISABE-2001-1115.

Mileshin, V.I, Orekhov, I.K and Startsev, A.N., 1999, "Aerodynamic Design of Axial Compressor Blading Using Quasi-3D Inviscid Techniques Checked by 3D Navier-Stokes Solver", Proceedings of the International Gas Turbine Congress 1999 Kobe, Japan, November 14-19, 1999, edited by Takashi Tamaru, IGTC'99 Kobe TS-24, pp.437-444.

Mileshin, V.I, Shchipin, S.K. and Startsev, A.N., 2003, "Quasi-3D and 3D Inverse Navier-Stokes Based Method Used to Design Highly Loaded Axial and Centrifugal Compressor Stages", IGTC 2003 Tokyo, Japan, November 2-7, 2003, edited by T.Watanabe, IGTC2003Tokyo TS-034.

Van Zante, D.E., Strazisar, A.J., Wood, J.R., Hathaway, M.D., and Okiishi, T.H., 2000, "Recommendations for Achieving Accurate Numerical Simulation of Tip Clearance Flows in Transonic Compressor Rotors", ASME Journal of Turbomachinery, Vol. 122, pp. 733-742.

Wadia, A.R., and Copenhaver, W.W., 1996, "An Investigation of the Effect of Cascade Area Ratios on Transonic Compressor Performance", ASME Journal of Turbomachinery, Vol. 118, pp. 760-770.

Ziegler, K.U., Gallus, H.E., and Niehuis, R., 2002, "A Study on Impeller-Diffuser Interaction: Part II – Detailed Flow Analysis", ASME Paper № GT-2002-30382.
