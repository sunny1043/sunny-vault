---
tags:
  - 航空发动机
  - 压气机
  - 高压压气机
  - 叶片弯曲
  - 气动设计
  - 三维数值模拟
created: 2026-06-17
source: ICAS 2010 (27th International Congress of the Aeronautical Sciences), Paper ICAS2010-412
author: Mileshin, Orekhov, Pankov, Stepanov (CIAM)
---

# 高负荷高压压气机典型中间级模型的数值与试验研究
# Numerical and Experimental Investigations of a High-Loaded Typical Middle Stage Model of HPC

> **作者 Authors:** V.I. Mileshin, I.K. Orekhov, S.V. Pankov, Eu.I. Stepanov
> **单位 Affiliation:** Central Institute of Aviation Motors (CIAM) 中央航空发动机研究院
> 2, Aviamotornaya St., 111116, Moscow, RUSSIA
> **E-mail:** mileshin@ciam.ru
> **关键词 Keywords:** compressor, blades, aerodynamics, efficiency, loading（压气机、叶片、气动、效率、负荷）

---

## 摘要
## Abstract

**English:** Efforts aiming at improvement of compressor efficiency and an increase in stall margin and total pressure ratio using less number of HPC stages in advanced turbofans entail an increase in compressor stage aerodynamic loading. Numerical and experimental investigations of a high-loaded typical HPC middle stage model with respect to effects of longitudinal bending of rotor blades and stator vanes on stage performances are presented in this work. Several versions of the compressor stage are studied. A noticeable increase in adiabatic efficiency is experimentally found for the optimum stage version with "sickle-like" rotor blades. In this version stagger axes of rotor profiles are bent in the circumferential direction in such a way that pressure sides are concave. Moreover, airflow and total pressure ratio are higher. Calculations of stationary viscous flow and parameters of the stage with straight blades are in good agreement with the experiment, but to the present time calculations can't give evidences of a considerable improvement of parameters for the optimum version of the experimental stage.

**中文：** 在先进涡扇发动机中，为提高压气机效率、增大喘振裕度（stall margin）和总压比（total pressure ratio）并减少高压压气机（HPC）级数，必然导致压气机级气动负荷的增大。本文针对转子叶片和静子叶片的纵向弯曲（longitudinal bending）对级性能的影响，对一个高负荷的典型高压压气机中间级模型开展了数值与试验研究。研究了若干种压气机级方案。试验发现，采用"镰刀形"（sickle-like）转子叶片的最优级方案在绝热效率（adiabatic efficiency）上有明显提高。在该方案中，转子叶型的安装角轴（stagger axes）沿周向弯曲，使得压力面（pressure side）呈凹形。此外，其空气流量和总压比也更高。对采用直叶片的级的定常黏性流动及其参数的计算结果与试验吻合良好，但截至目前，计算尚不能证明试验级的最优方案在参数上有显著改善。

---

## 符号表
## Nomenclature

**English:**
- G_cor – corrected air flow;
- π* – total pressure ratio;
- η*_ad – adiabatic efficiency;
- σ – total pressure recovery coefficient;
- λ – flow velocity coefficient relatively to critical sound;
- H̄_T – theoretical head coefficient;
- Subscripts:
- 1 – rotor inlet
- 2 – rotor outlet
- 3 – before stator
- 4 – after stator
- Cor – corrected parameters

**中文：**
- $G_{cor}$ —— 换算空气流量（corrected air flow）；
- $\pi^*$ —— 总压比（total pressure ratio）；
- $\eta^*_{ad}$ —— 绝热效率（adiabatic efficiency）；
- $\sigma$ —— 总压恢复系数（total pressure recovery coefficient）；
- $\lambda$ —— 相对临界声速的流速系数（flow velocity coefficient）；
- $\bar{H}_T$ —— 理论功头系数（theoretical head coefficient）；
- 下标：
- 1 —— 转子进口（rotor inlet）
- 2 —— 转子出口（rotor outlet）
- 3 —— 静子前（before stator）
- 4 —— 静子后（after stator）
- Cor —— 换算参数（corrected parameters）

---

## 引言
## Introduction

**English:** Three-dimensional blades are widely used today in aircraft engine compressors and turbines. Bending and inclinations of supersonic fan rotor blades in axial and circumferential directions are their specific features. Moreover, the blade inclination and bending are not equal in different sections along the blade height. This blade shape is a result of flow optimization aiming at wave loss decrease and reduction of secondary flows intensity as well as blade profile optimization to provide required strength.

**中文：** 如今，三维叶片（three-dimensional blades）在航空发动机的压气机和涡轮中得到了广泛应用。超声速风扇转子叶片在轴向和周向上的弯曲（bending）与倾斜（inclination）是其特有的特征。此外，叶片的倾斜和弯曲在沿叶高的不同截面上并不相同。这种叶片形状是流动优化的结果，其目的是降低波损失（wave loss）、减弱二次流（secondary flow）强度，同时进行叶型优化以提供所需的强度。

---

**English:** An important requirement to compressors of advanced engines is an increase in total pressure ratio but using less number of stages, that results in an increase in aerodynamic loading causing problems in achievement of specified high efficiency and stall margins. For increasing these parameters three guide vane rows of a four-stage high-loaded HPC were bent and have a scimitar profile. Despite of a small blade height (~14 mm) and medium HPC dimensions, the efficiency reaches η*_ad=0.87 at pressure ratio π*_к>5.

**中文：** 对先进发动机压气机的一项重要要求是，在减少级数的同时提高总压比，这导致气动负荷的增大，进而在实现规定的高效率和喘振裕度方面带来困难。为了提升这些参数，一台四级高负荷高压压气机的三排导向叶片（guide vane）被弯曲，呈弯刀形（scimitar）叶型。尽管叶高较小（约 14 mm）且高压压气机尺寸为中等量级，但在压比 $\pi^*_к>5$ 时，效率达到了 $\eta^*_{ad}=0.87$。

---

*Figure 1：静子叶片与转子叶片的弯曲方案示意图（左：初始级的直叶片；中：弯刀形静子叶片；右：镰刀形转子叶片，弯曲角均为 30°）。*
*图 1 / Fig. 1 Stator vane and rotor blade bending scheme.*

*（级流道图 Stage flow passage：示出 IGV、Rotor、Stator 沿 X 方向的子午流道，半径 R 约 250–280 mm。）*

---

**English:** The objective of this CIAM's research work [2] is to study the effect of blade profile stagger axis bending in the circumferential direction on characteristics of the stage as well as applicability of rotor blades with a bent longitudinal axis for stages with high aerodynamic loading in advanced turbofan compressors. It is considered that bending of the blade longitudinal axis in the circumferential direction changes pressure gradients, modifies flow deceleration along the profiles, aerodynamic loading distribution along the blade row height, losses and lag angles, as well as intensity of secondary flow and flow in docking areas of the blade with the hub and the outer casing.

**中文：** CIAM 这项研究工作[2]的目的，是研究叶型安装角轴沿周向弯曲对级特性的影响，以及带弯曲纵轴的转子叶片在先进涡扇压气机高气动负荷级中的适用性。研究认为，叶片纵轴沿周向的弯曲会改变压力梯度，改变沿叶型的流动减速过程、沿叶排叶高的气动负荷分布、损失和落后角（lag angle），以及二次流强度和叶片与轮毂（hub）及外机匣（outer casing）对接区域的流动。

---

**English:** At the end of 1980s, CIAM completed comparative experimental investigations of stator vanes with curvilinear longitudinal axis without modification of rotor blades. Irrespective of stator vane bending direction, there was an increase in efficiency by 1-2% with simultaneous twice decrease in the periodic component (multiplies to the passing frequency) of total pressure pulsation at the stage outlet [2, 4]. That time it was found that an improvement of stage performances was not a result of decreased intensity of secondary flows as could be anticipated but, to a great extent, an improvement of rotor performances that was unmodified in comparative tests of the stage with different stators.

**中文：** 在 20 世纪 80 年代末，CIAM 完成了对具有曲线纵轴的静子叶片（在不改变转子叶片的情况下）的对比试验研究。无论静子叶片的弯曲方向如何，效率都提高了 1–2%，同时级出口处总压脉动的周期分量（其频率为叶片通过频率的整数倍）减小为原来的一半[2, 4]。当时发现，级性能的改善并非如预期那样源于二次流强度的降低，而在很大程度上来自转子性能的改善——尽管在采用不同静子的级对比试验中，转子本身并未作改动。

---

**English:** The test results have not been verified by stationary flow calculations on the basis of various mathematical models. Authors [2, 4] & et al. made an assumption that mathematical models for straight and bent blades should take into account a displacement of phase of unsteady interaction of rotor and stator cascades of elementary stages located on different axisymmetrical streamline surfaces along the height.

**中文：** 这些试验结果尚未通过基于各种数学模型的定常流动计算得到验证。文献[2, 4]等的作者提出一种假设：针对直叶片和弯曲叶片的数学模型，应当考虑沿叶高位于不同轴对称流面（axisymmetrical streamline surface）上的基元级（elementary stage）转子与静子叶栅之间非定常相互作用的相位位移（phase displacement）。

---

**English:** For more detailed analysis of blade bending effects this work describes numerical-experimental investigations of a high-loaded stage being a prototype of a HPC middle stage for an advanced turbofan.

**中文：** 为了更详细地分析叶片弯曲的影响，本文对一个高负荷级开展数值-试验研究，该级是先进涡扇发动机高压压气机中间级的原型。

---

## 1 试验对象及其测试仪表
## 1 Test object and its instrumentation

**English:** The stage has a constant outer diameter - D_rotor=576 mm and the following design parameters: H̄_T=0.404; C̄_1a.cor=0.516; G_air.cor=11.8 g/s; η*_ad=0.88; π*_stage=1.52; U_tip.cor=327 m/s.

**中文：** 该级具有恒定的外径 $D_{rotor}=576\ \text{mm}$，其设计参数如下：$\bar{H}_T=0.404$；$\bar{C}_{1a.cor}=0.516$；$G_{air.cor}=11.8\ \text{g/s}$；$\eta^*_{ad}=0.88$；$\pi^*_{stage}=1.52$；$U_{tip.cor}=327\ \text{m/s}$。

---

**English:** The stage consists of three blade rows: IGV, rotor and stator. The IGV provides required flow swirling (α₁=65°) and is located at a proper distance to prevent the influence of its wakes on rotor parameters as well as for instrumentation mounting. The distance between IGV and rotor axes is 115 mm. It is supposed that HPC rotor will have a drum-type design and stator vanes – cantilever-type. To simulate these conditions, the rotor is provided with a part of the drum rotating under the stator vanes.

**中文：** 该级由三排叶片组成：进口导叶（IGV）、转子和静子。进口导叶提供所需的气流预旋（α₁=65°），并布置在适当距离处，以防止其尾迹影响转子参数，同时便于安装测量仪表。进口导叶与转子轴线之间的距离为 115 mm。假定高压压气机转子采用鼓式（drum-type）结构，而静子叶片采用悬臂式（cantilever-type）结构。为模拟这些条件，转子设有一段在静子叶片下方旋转的鼓体。

---

**English:** The stage is designed in such a way that flow inlet and outlet angles are identical and constant along the radius (α₄=α₁=65°). There is an increase in the hub diameter within the section from IGV trailing edge to the rotor inlet that results in flow acceleration with an increase in absolute flow velocity angle by 5°. To provide the specified angle at the rotor inlet (α₁=65°), the flow outlet angle at IGV outlet is taken equal to α_out= 60°.

**中文：** 该级的设计使得气流进口角和出口角相同，且沿半径保持不变（α₄=α₁=65°）。在从进口导叶尾缘到转子进口的区段内，轮毂直径增大，使气流加速，同时绝对气流速度角增大 5°。为了在转子进口处获得规定的角度（α₁=65°），进口导叶出口处的气流出口角取为 α_out=60°。

---

**English:** The previous research work of high-loaded stages showed that it is advisable to increase the axial velocity component to the outlet. For this reason the flow passage area was decreased from the IGV and behind it, but only in the rotor (due to an increase in the hub diameter); and a cylindrical flow passage is used in the stator (d̄₁=0.863, d̄₂=0.893, d̄₄=0.893).

**中文：** 此前对高负荷级的研究表明，将轴向速度分量向出口方向增大是有利的。因此，自进口导叶起及其后方的流道面积均有所减小，但仅在转子中如此（由于轮毂直径增大）；而在静子中采用圆柱形流道（$\bar{d}_1=0.863$，$\bar{d}_2=0.893$，$\bar{d}_4=0.893$）。

---

**English:** Rotor blade profiles were found earlier as a result of special research works. They are variable along the blade height; number of rotor blades is Zr=67; blade solidity is b/t=1.5 and constant along the radius. Profiles with decreased transverse pressure gradients and lesser losses are chosen in tip sections. Profiles that are efficient in cascades with increased blade thickness are chosen in hub sections. Standard initial blade profiles are used in middle sections. To prevent blade–casing contact, the tip (mounting) clearance between straight and bent rotor blades was 0.5-0.6 mm – the same as for straight blades.

**中文：** 转子叶型是此前通过专门研究工作确定的。它们沿叶高是变化的；转子叶片数为 $Z_r=67$；叶栅稠度（solidity）为 $b/t=1.5$，且沿半径保持不变。在叶尖（tip）截面选用横向压力梯度较小、损失较低的叶型。在轮毂（hub）截面选用在叶栅中增大叶片厚度时仍高效的叶型。在中间截面采用标准的初始叶型。为防止叶片与机匣接触，直叶片和弯曲叶片转子的叶尖（安装）间隙均为 0.5–0.6 mm，与直叶片相同。

---

**English:** A decrease in axial velocity component in the tip sections of guide vanes causes a need for an increase of blade solidity. The assumed blade solidity is less than the required value by 25% and is equal to b/t=1.4 in the middle radius and b/t=1.65 - in tip sections. Number of stator vanes is Zst=104. Stator vane chord is b=23.13 mm in middle sections and increases up to b=26.36 mm at the hub and b=29.53 mm at the tip. Superposition of bade profiles is provided along the trailing edge, therefore the leading edge has a variable sweep along the height as shown in Fig. 1 and Fig. 2. To prevent stator vane - drum contact, the tip clearance between the hub and swept vanes is increased up to 0.55-0.70 mm as compared with 0.4-0.5 mm for straight vanes.

**中文：** 导叶叶尖截面轴向速度分量的减小，需要增大叶栅稠度。所假定的叶栅稠度比所需值小 25%，在中间半径处为 $b/t=1.4$，在叶尖截面处为 $b/t=1.65$。静子叶片数为 $Z_{st}=104$。静子叶弦长在中间截面为 $b=23.13\ \text{mm}$，在轮毂处增大至 $b=26.36\ \text{mm}$，在叶尖处增大至 $b=29.53\ \text{mm}$。叶型沿尾缘叠合，因此前缘沿叶高具有可变的掠角（sweep），如图 1 和图 2 所示。为防止静子叶片与鼓体接触，轮毂与掠形叶片之间的叶尖间隙增大至 0.55–0.70 mm，而直叶片为 0.4–0.5 mm。

---

**English:** The stage was tested at the CIAM's test facility. 1000-KW electric motor was used as a drive of the test facility. Drive power was transmitted via a speed increaser. Torque is measured on the shaft between the speed increaser and the compressor by a torquemeter. Power consumption by the compressor shaft friction was estimated on the basis of calibration of running parts in idling for the compressor with a smooth rotor disk.

**中文：** 该级在 CIAM 的试验台上进行了试验。试验台采用 1000 kW 的电动机作为驱动装置。驱动功率经增速器（speed increaser）传递。扭矩由扭矩计（torquemeter）在增速器与压气机之间的轴上测量。压气机轴摩擦的功率消耗，是基于对装有光滑转子盘的压气机在空转（idling）状态下转动部件的标定而估算的。

---

**English:** The stage IGV was an auxiliary row, therefore total pressure losses in IGV were excluded in measurements of the stage performances. Three seven-point pressure rakes were mounted at IGV outlet for measurements of these losses. The IGV casing was movable. Total pressure was measured for 10 positions of the casing with respect to IGV spacing. These rakes were removed in measurements of stage performances, and total pressure losses were calculated on the bases of measurements - air flow approximating dependence, σ_in(G_air).

**中文：** 该级的进口导叶为辅助叶排，因此在测量级性能时排除了进口导叶中的总压损失。为测量这些损失，在进口导叶出口处安装了三个七点压力梳（pressure rake）。进口导叶机匣可移动。在相对于进口导叶栅距的 10 个机匣位置上测量了总压。在测量级性能时移除了这些压力梳，总压损失则基于测量得到的随空气流量变化的近似关系式 $\sigma_{in}(G_{air})$ 进行计算。

---

**English:** Flow parameters at the stage outlet were measured by 6 seven-point pressure rakes and 3 seven-point thermocouples. The rakes were fixed in the rotating ring. Parameters were measure in 5 positions with respect to IGV spacing. An additional five-point total pressure rake was mounted at the rotor outlet. Static pressure on flow passage walls was measured at three points along the circle in inter-blade sections and at the stage outlet.

**中文：** 级出口处的流动参数由 6 个七点压力梳和 3 个七点热电偶（thermocouple）测量。压力梳固定在旋转环上。在相对于进口导叶栅距的 5 个位置上测量参数。在转子出口处额外安装了一个五点总压梳。流道壁面上的静压在叶间截面和级出口处沿圆周的三个点测量。

---

**English:** Four stage configurations produced by combining 2 rotor blade versions and 2 stator vane versions are studied. Rotor blades and stator vanes in the initial stage version are straight. Rotor blades in the 2nd version are sickle-like (Fig.2) and stator vanes – sabre-like, i.e. stagger axes are bent in the circumferential direction in such a way that rotor blade pressure sides and stator vane suction sides are concave.

**中文：** 研究了由 2 种转子叶片方案和 2 种静子叶片方案组合而成的四种级构型。初始级方案中的转子叶片和静子叶片均为直叶片。第 2 种方案中的转子叶片为镰刀形（sickle-like，图 2），静子叶片为弯刀形（sabre-like），即安装角轴沿周向弯曲，使得转子叶片压力面和静子叶片吸力面（suction side）呈凹形。

---

**English:** Among four versions under study the optimum version is chosen that is distinguished by sickle swept rotor blades and straight stator vanes. Tests of the optimum version show a noticeable increase in adiabatic efficiency by Δη*_ad ~ 1.7÷2.0% at n̄_cor=0.8÷0.9 of the nominal value and Δη*_ad ~ 0.7% at n̄_cor=1.0. Moreover, there is an increase in airflow and pressure ratio (see Fig. 3). Application of sickle stator vanes is not advisable because of decreased efficiency by δη*_ad = 1.5% at n̄_cor= 0.7–1.0.

**中文：** 在所研究的四种方案中，选出的最优方案以镰刀掠形转子叶片和直静子叶片为特征。最优方案的试验表明：在 $\bar{n}_{cor}=0.8\div0.9$ 倍额定值时，绝热效率有明显提高，$\Delta\eta^*_{ad}\sim 1.7\div2.0\%$；在 $\bar{n}_{cor}=1.0$ 时，$\Delta\eta^*_{ad}\sim 0.7\%$。此外，空气流量和压比也有所增大（见图 3）。采用镰刀形静子叶片并不可取，因为在 $\bar{n}_{cor}=0.7\sim1.0$ 时效率降低 $\delta\eta^*_{ad}=1.5\%$。

---

## 2. 级的定常三维流动与压力特性计算及其与试验数据的对比
## 2. Calculations of steady 3D flow and pressure characteristics of the stage and their comparison with experimental data

**English:** For the purpose of experimental investigations as well as revealing of a bending beneficial effect on parameters, a mathematical model was developed and viscous three-dimensional steady flows and integral performances of all stage versions were calculated.

**中文：** 为了进行试验研究并揭示弯曲对参数的有利影响，建立了一个数学模型，并计算了所有级方案的黏性三维定常流动和积分性能。

---

**English:** The calculation procedure is based on the numerical solution of 3D Navier-Stokes equations averaged by Reynolds with semi empirical turbulence models and wall functions on the basis of Godunov's implicit high order numerical scheme [1, 3, 5, 6]. Either the Baldwin-Lomacs algebraic turbulence model or differential models can be used for closing the system of equations. The two-parametrical turbulence model k-ω was used in calculations presented herein for estimation of turbulent viscosity.

**中文：** 计算过程基于求解雷诺平均（Reynolds-averaged）三维 Navier-Stokes 方程的数值解，采用半经验湍流模型（turbulence model）和壁面函数（wall function），并以 Godunov 隐式高阶数值格式为基础[1, 3, 5, 6]。可采用 Baldwin-Lomax 代数湍流模型或微分模型来封闭方程组。本文所给出的计算中，采用了双参数 $k\text{-}\omega$ 湍流模型来估算湍流黏性。

---

**English:** Calculations of steady viscous three-dimensional flows were made in «Mixing plane» approximation. Non-stationary interaction of cascades was not taken into account because flow was averaged by a blade-to-blade spacing on the surface separating steady and rotating grid cells. The averaging procedure assumes constancy of momentum flux and energy through this surface. In this case there is an increase in entropy that simulates losses in distortion equalization caused by mixing.

**中文：** 定常黏性三维流动的计算采用"掺混面"（Mixing plane）近似进行。叶栅之间的非定常相互作用未予考虑，因为流动在分隔定常网格单元与旋转网格单元的交界面上按叶栅栅距进行了平均。该平均过程假定动量通量和能量通过该交界面保持不变。在此情况下熵会增大，从而模拟由掺混（mixing）引起的畸变均化（distortion equalization）中的损失。

---

**English:** The calculation domain covers three rows and consists of three rectangular (hexagonal) blocks. Each block of the grid covers one blade channel of each raw. Calculations are competed for a grid having (120*64*64 + 150*64*64 + 150*64*64) = 1720320 cells. In the tip clearance between rotating rotor blades and the fixed outer casing as well as between motionless stator vanes with cantilever attachment and the rotating drum-type hub are 12 cells. The tip clearance values in operating conditions are chosen equal 0.27 mm or 0.76 % of the rotor blade height and 0.15 mm or 0.5 % of the stator vane height. The computational grid in the rotor and in the stator is shown in Fig. 5.

**中文：** 计算域涵盖三个叶排，由三个矩形（六面体）块组成。每个网格块覆盖每排的一个叶片通道。计算所用网格的单元数为 $(120{\times}64{\times}64 + 150{\times}64{\times}64 + 150{\times}64{\times}64) = 1720320$ 个。在旋转转子叶片与固定外机匣之间的叶尖间隙处，以及悬臂安装的静止静子叶片与旋转鼓式轮毂之间的间隙处，各布置 12 个网格单元。工作状态下的叶尖间隙取为：0.27 mm（占转子叶高的 0.76%）和 0.15 mm（占静子叶高的 0.5%）。转子和静子中的计算网格如图 5 所示。

---

**English:** Distributions of total pressure, temperature, an angle between the absolute velocity vector and the meridian plane, and an angle between the velocity vector meridian component and the stage axis are specified as the boundary conditions at the inlet. Static pressure at the hub is specified at the outlet and pressure distribution along the channel height is derived from the condition of an approximate radial equilibrium. Viscous flow calculations are completed using the standard boundary conditions at the inlet: total temperature = 288.15°K, total pressure = 101325 Pa, flow angles at IGV inlet are equal to zero.

**中文：** 进口处的边界条件给定为：总压、温度、绝对速度矢量与子午面之间的夹角，以及速度矢量子午分量与级轴线之间的夹角的分布。出口处给定轮毂处的静压，沿通道高度的压力分布则由近似径向平衡（radial equilibrium）条件导出。黏性流动计算采用标准进口边界条件：总温 = 288.15 K，总压 = 101325 Pa，进口导叶进口处的气流角为零。

---

**English:** Fig. 4 shows the comparison of computed and experimental characteristics at corrected speed values n̄ = 0.8 and 1.0 with straight stator vanes and two rotor versions: with straight and sickle-like blades. Fig. 6 shows Mach number distribution in blade channels for the rotor and the stator as well distributions of total pressure ratio and adiabatic efficiency along the channel height at the stage outlet at optimum point of the characteristic n̄ = 1.0.

**中文：** 图 4 给出了在换算转速 $\bar{n}=0.8$ 和 $1.0$ 时，采用直静子叶片以及两种转子方案（直叶片和镰刀形叶片）的计算特性与试验特性的对比。图 6 给出了转子和静子叶片通道内的马赫数（Mach number）分布，以及在特性曲线最优点 $\bar{n}=1.0$ 处级出口沿通道高度的总压比和绝热效率分布。

---

**English:** While experimental values of the Stage parameters with two rotor versions (straight and sickle blades) show a noticeable difference in adiabatic efficiency, pressure ratio and max. air flow, this difference is hardly appreciable by calculations. At the same time, calculations are in good agreement with tests for straight rotor blades. As above-mentioned, in opinion of authors [3] et al. a probable cause of this difference is a change in conditions of unsteady interaction of rotor and stator rows in relative motion owing to displacement of phase interaction of elementary stages cascades located on different axisymmetrical streamline surfaces along the height. Other less probable reasoning lies in the fact that changes in intensity of secondary flows arising in case of replacement of a radial blade by a swept blade were not taken into account in calculations. Numerical and experimental investigations are under way in the direction of experimental data verification and mathematical model improvement.

**中文：** 尽管两种转子方案（直叶片和镰刀形叶片）的级参数试验值在绝热效率、压比和最大空气流量上显示出明显差异，但计算中这一差异几乎难以察觉。与此同时，对于直转子叶片，计算结果与试验吻合良好。如前所述，文献[3]等作者认为，这一差异的可能原因是：沿叶高位于不同轴对称流面上的基元级叶栅之间相互作用相位发生位移，导致转子与静子叶排在相对运动中非定常相互作用条件发生改变。另一个可能性较小的解释是：用掠形叶片替换径向叶片时所产生的二次流强度变化，在计算中未被考虑。目前正在沿着试验数据验证和数学模型改进的方向开展数值与试验研究。

---

## 结论
## Conclusions

**English:** 1. Numerical and experimental investigations were completed for a high-loaded stage being a model of a typical HPC middle stage for an advanced turbofan with the following design parameters: U_tip cor=327 m/s, C̄_1a=0.516, H̄_T=0.404, π*_stage=1.52, η*_ad=0.88.

**中文：** 1. 针对一个高负荷级完成了数值与试验研究，该级是先进涡扇发动机典型高压压气机中间级的模型，其设计参数如下：$U_{tip\,cor}=327\ \text{m/s}$，$\bar{C}_{1a}=0.516$，$\bar{H}_T=0.404$，$\pi^*_{stage}=1.52$，$\eta^*_{ad}=0.88$。

---

**English:** 2. The effects of bending in circumferential direction of longitudinal axes of stator vanes and rotor blades were analyzed and applicability of rotor blades with a bent longitudinal axis for stages with increased aerodynamic loading in non-multistage high-loaded HPC of advanced turbofan were studied.

**中文：** 2. 分析了静子叶片和转子叶片纵轴沿周向弯曲的影响，并研究了带弯曲纵轴的转子叶片在先进涡扇发动机非多级高负荷高压压气机中、用于气动负荷增大的级时的适用性。

---

**English:** 3. Among studied stage versions distinguished by various combinations of bent rotor blades and stator vanes, sickle rotor blades (with a concave pressure side surface) and straight stator vanes were chosen as the optimum version.

**中文：** 3. 在以弯曲转子叶片与静子叶片各种组合为特征的所研究级方案中，选出镰刀形转子叶片（压力面为凹形）与直静子叶片作为最优方案。

---

**English:** 4. A considerable increase in adiabatic efficiency was experimentally measured for the optimum version - Δη*_ad ~ 1.7÷2.0% at rotational speeds n̄_cor=0.8÷0.9 of the nominal value and Δη*_ad ~ 0.7% at n̄_cor=1.0. Moreover, there is an increase in airflow and pressure ratio.

**中文：** 4. 试验测得最优方案的绝热效率有显著提高——在转速为额定值的 $\bar{n}_{cor}=0.8\div0.9$ 倍时，$\Delta\eta^*_{ad}\sim 1.7\div2.0\%$；在 $\bar{n}_{cor}=1.0$ 时，$\Delta\eta^*_{ad}\sim 0.7\%$。此外，空气流量和压比也有所增大。

---

**English:** 5. Calculated values were compared with test results in operating conditions at rotational speeds n̄cor=0.8, 1.0. Calculations were in good agreement with tests for straight rotor blades. By present time a considerable improvement of performances for the stage version with sickle rotor blades was not found by calculations as it was measured in experiment.

**中文：** 5. 将计算值与转速 $\bar{n}_{cor}=0.8$、$1.0$ 工作状态下的试验结果进行了对比。对于直转子叶片，计算结果与试验吻合良好。截至目前，对于采用镰刀形转子叶片的级方案，计算尚未发现如试验所测得的那种性能显著改善。

---

## 图表说明
## Figures

*图 2 / Fig. 2 具有曲线纵轴的静子叶片与转子叶片：镰刀形转子和弯刀形静子（计算三维造型与实物照片）。*
*Fig. 2 Stator and rotor blades with curvilinear longitudinal axis. Sickle-like rotor and sabre-like stator.*

*图 3 / Fig. 3 转子叶片纵轴形状对级性能的影响（绝热效率 $\eta^*_{ad.st}$ 与压比 $\pi^*_{st}$ 随换算流量 $G_{cor}$ 的变化，对比镰刀形转子与直转子，换算转速 $\bar{n}_{cor}=0.7/0.8/0.9/1.0$）。*
*Fig. 3 Effects of rotor blade longitudinal axis shape on the Stage performances.*

*图 4 / Fig. 4 试验数据与计算数据的对比（直转子与镰刀形转子的试验值及计算值，参数同图 3）。*
*Fig. 4 Comparison of experimental and calculated data.*

*图 5 / Fig. 5 计算网格（转子与静子的计算网格）。*
*Fig. 5 Computational grids.*

*图 6 / Fig. 6 黏性三维流动计算结果：马赫数等值线（间隔 step=0.05），以及级出口沿通道高度的总压比和绝热效率分布。*
*Fig. 6 Calculations of viscous 3D flows. Mach number isolines, step=0.05. Distribution of total pressure ratio and adiabatic efficiency along the channel height at the Stage outlet.*

---

## 参考文献 References

[1] I.A. Brailko, V.I. Mileshin, M.A. Nyukhtikov, S.V. Pankov. "Computational And Experimental Investigation Of Unsteady And Acoustic Characteristics Of Counter – Rotating Fans". HT-FED-2004-56436, July 11-15, 2004, Charlotte, North Carolina, USA.

[2] F.Sh. Gelmedov, N.M. Savin, Eu.I. Stepanov, L.I. Semernyak. Development of D-66 typical middle stage of low stage HPC with rotor blades spatial profiling. CIAM 2001-2005. Main results of science and research activity. Vol. 1. Edited by V.A. Skibin, V.I. Solonin, M.Ya. Ivanov. – M.:CIAM, 2005, - 472p.

[3] I.A. Brailko, V.I. Mileshin, M.A. Nyukhtikov, S.V. Pankov, A.A. Rossikhin. "3D Computational Analysis of Unsteady and Acoustic Characteristics of a Model of High Bypass Ratio Counter-Rotating Fan". ISABE-2005-1186, September, 4-9, Munich, Germany.

[4] V.E. Saren, N.M. Savin, et al. Hydrodynamic interaction of axial turbomachine cascades; Journall of Engineering Mathematics, Vol. 55, №1-4, (2006), 9-39.

[5] V.I. Mileshin, I.K. Orekhov, S.V. Pankov "Numerical And Experimental Investigations Of Bypass Fans Characteristics" Proceedings of ISABE International Conference, Bejing, ISABE-2007-1179, 2007.

[6] V.I. Mileshin, M.A. Nyukhtikov, I.K. Orekhov, S.V. Pankov, S.K. Shchipin "Open Counter – Rotation Fan Blades Optimization Based On 3d Inverse Problem Navier-Stokes Solution Method With The Aim Of Tonal Noise Reduction" Proceedings of GT2008 ASME Turbo Expo 2008, June 9-13, 2008, Berlin, Germany, GT2008-51173.

---

## 联系作者邮箱 Contact Author Email Address

mileshin@ciam.ru

---

## 版权声明 Copyright Statement

The authors confirm that they, and/or their company or organization, hold copyright on all of the original material included in this paper. The authors also confirm that they have obtained permission, from the copyright holder of any third party material included in this paper, to publish it as part of their paper. The authors confirm that they give permission, or have obtained permission from the copyright holder of this paper, for the publication and distribution of this paper as part of the ICAS2010 proceedings or as individual off-prints from the proceedings.
