---
tags:
  - 航空发动机
  - AL-31FP
  - 推力矢量喷管
  - 气动缸
  - HAL
  - 苏-30MKI
created: 2026-06-17
source: HAL Koraput Division Internship Report
author: Kamalakanta Mohapatra (VT No-1902)
guide: R.G. Mishra & Shibendu Sen (620-Assembly Shop, SED)
---

> **原文PDF**：[[STUDYOFAL31FPENGINEMANUFACTURINGASSEMBLYANDTESTING.pdf]]

# AL-31FP 发动机熟悉化及 TVC 喷管气动缸故障研究
# Familiarization on "AL-31FP" Engine and Research Work on Failures of Pneumatic Cylinder in TVC Nozzle

> **单位 Organization:** 印度斯坦航空有限公司 · HAL Koraput Division（SU-30发动机部门）  
> **实习时间 Period:** 2016年6月10日 – 6月28日  
> **指导老师 Guided by:** Mr. R.G. Mishra（620装配车间经理）& Mr. Shibendu Sen（副经理）

---

## 目录 Contents

| 序号 | 章节 Section | 内容简介 Description |
|------|-------------|----------------------|
| 1 | [[#第一章 简介]] | HAL历史及喷气发动机发明史 |
| 2 | [[#第二章 AL-31FP 发动机]] | AL-31FP 发动机原理图与基本信息 |
| 3 | [[#第三章 性能特征与技术参数]] | 发动机特征、限制与详细参数 |
| 4 | [[#第四章 各部件详解]] | AL-31FP 各部件详细介绍 |
| 5 | [[#第五章 附件系统（航电）]] | 控制发动机性能与安全的各类设备 |
| 6 | [[#第六章 气动缸故障研究]] | VJN气动缸故障研究与调查结论 |

---

## 第一章 简介
## Chapter 1: Introduction to HAL and the Project

### HAL 与本项目简介

**English:** Hindustan Aeronautics Limited is one of Asia's premier organizations in the present aerospace industry. HAL Koraput Division is a manufacturing and overhauling unit for various aero engines.

**中文：** 印度斯坦航空有限公司（HAL）是当今亚洲航空工业的顶尖机构之一。HAL科拉普特分部是各类航空发动机的制造与大修单位。

---

**English:** As per the present scenario, the division manufactures only the AL-31FP engine for the SUKHOI-30MKI aircraft. It overhauls:
- AL-31FP for SUKHOI-30 MKI
- RD33 for MIG-29
- R29B for MIG-27M
- R25 for MIG-21 BISON

**中文：** 目前该分部专门为苏霍伊-30MKI飞机生产AL-31FP发动机，同时承担以下型号的大修工作：
- AL-31FP（苏-30 MKI）
- RD33（米格-29）
- R29B（米格-27M）
- R25（米格-21 BISON）

---

**English:** All the above-stated engines come under the turbojet engine category. Our project work was carried out here for 5 weeks, covering all sections from research and development to final dispatch, in order to acquire industrial-oriented procedures. The next phase of our work was to find a failure reason — "research work on pneumatic cylinder" — to find the failure reason and state with probable solution.

**中文：** 以上所有发动机均属涡轮喷气发动机类型。本项目历时5周，覆盖从研发到最终出厂的各个环节，旨在获取工业化实操经验。项目的下一阶段是查找故障原因——"气动缸故障研究"——找出失效原因并提出可能的解决方案。

---

### 喷气发动机 Jet Engines

**English:** "JET" means a rapid stream of liquid or gas forced out of a small opening.

> **Definition:** "A JET ENGINE is a reaction engine that discharges a fast-moving JET through a small cross-sectional area (nozzle) by jet propulsion, which creates thrust in accordance with Newton's laws of motion."

**中文：** "喷气"是指从小开口中高速喷出的液体或气体流。

> **定义：** "喷气发动机是一种反作用力发动机，通过喷气推进将高速气流从小截面积（喷嘴）喷出，依据牛顿运动定律产生推力。"

该广义定义涵盖涡轮喷气、涡轮风扇、火箭、冲压喷气以及脉冲喷气等各类发动机。

---

### 喷气发动机的历史与发明 History and Invention

**English:** Dr. Hans von Ohain and Sir Frank Whittle are both recognized as being the co-inventors of the jet engine. Each worked separately and knew nothing of the other's work.

A young Royal Air Force man, Sir Frank Whittle, presented a design for a jet engine to the Air Ministry in October 1929. They were unimpressed and rejected his idea. Regardless of this setback, Whittle still patented his "turbojet engine" — he developed his ideas further and on 16 January 1930 in England, Whittle submitted his first patent (granted in 1932). In 1936, he set up a company called Power Jets Ltd. In 1937, using newly available alloys that were strong and light, he produced the first viable jet engine to be successfully tested in a laboratory; it first flew in 1941.

Dr. Hans von Ohain, a German scientist, was granted a patent for his turbojet engine in 1936 and flew his jet aircraft in 1939.

**中文：** 汉斯·冯·奥海因博士与弗兰克·惠特尔爵士均被公认为喷气发动机的联合发明人，二人各自独立研究，互不知晓对方的工作。

英国皇家空军青年军官弗兰克·惠特尔爵士于1929年10月向航空部提交了一份喷气发动机设计方案，遭到否定。尽管如此，惠特尔仍坚持为其"涡轮喷气发动机"申请专利，并于1930年1月16日在英国提交了首份专利申请（1932年获批）。1936年，他创办了Power Jets有限公司。1937年，他利用当时新型的高强度轻质合金，制造出第一台在实验室成功测试的可用喷气发动机，并于1941年首次飞行。

德国科学家汉斯·冯·奥海因博士于1936年获得涡轮喷气发动机专利，并于1939年驾驶喷气飞机首飞。

---

### 布雷顿热力学循环 Brayton Thermodynamic Cycle

**English:** All jet engines work on the **BRAYTON thermodynamic cycle**, developed by George Brayton but patented by Englishman John Baber in 1791. It is also sometimes known as the **Joule cycle**. It is a constant-pressure cycle accomplishing the same operations as in the Otto cycle, but all operations are continuous with uninterrupted flow of power.

**中文：** 所有喷气发动机均依据**布雷顿热力学循环**工作，该循环由乔治·布雷顿提出，1791年由英国人约翰·巴伯获得专利，也称**焦耳循环**。这是一个恒压循环，与奥托循环执行相同的操作，但所有过程均连续进行，功率输出不间断。

**理想布雷顿循环各过程 Ideal Brayton Cycle Processes:**

| 过程 Process | 类型 Type | 描述 Description |
|-------------|-----------|-----------------|
| **1→2** | 等熵压缩 Isentropic | 环境空气被吸入压气机并被压缩 Ambient air drawn into compressor and pressurized |
| **2→3** | 等压加热 Isobaric | 压缩空气在燃烧室中与燃料混合燃烧 Compressed air passes through combustion chamber, fuel burned at constant pressure |
| **3→4** | 等熵膨胀 Isentropic | 高温高压气体膨胀做功，驱动涡轮 Heated pressurized air expands through turbine, some work drives compressor |
| **4→1** | 等压放热 Isobaric | 向大气环境排热 Heat rejection to atmosphere |

---

## 第二章 AL-31FP 发动机
## Chapter 2: AL-31FP Engine

**English:** The AL-31FP engine is designed and developed by Lyulka, a Russian-based company; HAL is now manufacturing the engines under license.

**中文：** AL-31FP 发动机由俄罗斯留利卡公司设计研发，HAL 现持有授权生产该发动机。

**名称释义 Name Breakdown:**

| 字母 | 英文含义 | 中文含义 |
|------|---------|---------|
| **A** | Name of designer — Arkhip Mikhailovich Lyulka | 设计师姓名——阿尔希普·米哈伊洛维奇·留利卡 |
| **L** | Name of company — Lyulka, now NPO Saturn | 公司名称——留利卡，现为NPO土星 |
| **31** | Series number | 系列编号 |
| **F** | After Burner (Farsa in Russian) | 加力燃烧室（俄语：法尔萨） |
| **P** | Thrust Vectoring Nozzle (Povorothoye in Russian) | 推力矢量喷管（俄语：波沃罗托耶） |

**English:** The AL-31FP is a turbojet engine with special features of Variable LPCR guide vanes, bypass duct from LPCR, variable HPCR stator blades of stages 1, 2, and 3, and thrust vector nozzle with a tilting angle of 14 degrees.

**中文：** AL-31FP 是一种涡轮喷气发动机，具备以下特殊功能：可变低压压气机转子（LPCR）导叶、来自LPCR的旁通管道、第1/2/3级可变高压压气机转子（HPCR）静子叶片，以及偏转角达14度的推力矢量喷管。

### 发动机截面部件图 Engine Cross-Section Components

```
A-B  进气导叶  Inlet guide vane
B-C  低压压气机  Low pressure compressor
C-D  中间机匣  Intermediate casing
D-E  旁通管道前机匣  By-pass duct front casing
E-F  旁通管道后机匣  By-pass duct rear casing
F-G  混合器机匣  Mixer casing
G-I  加力燃烧室过渡段  Afterburner transition section
I-J  加力燃烧室机匣  Afterburner casing
J-K  推力矢量喷管  Thrust vectoring nozzle

1   低压压气机  Low pressure compressor
2   中央锥齿轮  Central bevel gearing
3   中间机匣  Intermediate casing
4   高压压气机  High pressure compressor
5   旁通管道  By-pass duct
6   燃烧室  Combustion chamber
7   空气-空气热交换器  Air-to-air heat exchanger
8   高压涡轮  High pressure turbine
9   低压涡轮  Low pressure turbine
10  涡轮支撑  Turbine support
11  混合器  Mixer
12  加力燃烧室过渡段  Afterburner transition section
13  加力燃烧室  Afterburner
14  偏转装置  Tilting unit
15  喷管  Jet nozzle
```

---

## 第三章 性能特征与技术参数
## Chapter 3: Engine Features and Technical Information

### 发动机基本信息 Engine Information

**English:** Each AL-31FP engine weighs **1570 kg**. It has an afterburner-equipped all-mode TVC exhaust nozzle. The overhaul time between OEM (original equipment manufacturer) for maintenance is **500 hours** and the life span of engine is **2000 hours**. There are totally **645 parts**, **202 assemblies** and **40 mandatory parts**; each engine has **2710 blades**.

The nozzles are mounted 32 degrees outward to the longitudinal engine axis (in the horizontal plane) and can be deflected **±15 degrees** in one plane. The afterburner can spend up to **300 liters of fuel per minute** in full reheat mode and give a speed of **Mach > 2**.

**中文：** 每台 AL-31FP 发动机重 **1570千克**，配备全模式TVC排气喷管。OEM维护大修间隔时间为 **500小时**，发动机寿命为 **2000小时**。全机共有 **645个零件**、**202个组件**和 **40个强制性零件**，每台发动机共有 **2710片叶片**。

喷管在水平面内相对发动机纵轴向外安装32度，可在一个平面内偏转 **±15度**。加力燃烧室在全加力模式下每分钟耗油可达 **300升**，可使飞机达到超过 **马赫2** 的速度。

### 技术规格 Technical Specifications

| 参数 Parameter | 数值 Value |
|---------------|-----------|
| 战斗模式"C"最大推力 Max thrust (combat mode 'C') | **12,500 kg** |
| 干推力 Max thrust (dry) | **7,670 kg** |
| 低压压气机级数 LP Compressors | 4级轴流式 4-stage axial flow |
| 低压涡轮 LP Turbine | 单级轴流，气冷NGV和涡轮叶片 Single stage axial, air-cooled NGVs and turbine blades |
| 高压压气机 HP Compressors | 9级轴流，可变第1/2级静子 9-stage axial, variable 1st and 2nd stage stators |
| 高压涡轮 HP Turbine | 单级轴流，气冷NGV和涡轮叶片 Single stage axial, air-cooled NGVs and turbine blades |
| 最大空气流量 Max Air Flow | **112 kg/sec** |
| 低压压气机压比 LPC compression ratio | **3.5:1** |
| 高压压气机压比 HPC compression ratio | **6.6:1** |
| 总压比 Total compression ratio | **23:1** |
| 最大P2压力 Max P2 pressure | **37.5 kg/cm²** |
| 涵道比 Bypass ratio | **0.57:1** |
| 高压转子转速 HPR RPM (N₂) | **13,300 rpm** |
| 低压转子转速 LPR RPM (N₁) | **10,200 rpm** |
| 高压转子滑行停车时间 Run down time (HPR) | **25 sec** |
| 低压转子滑行停车时间 Run down time (LPR) | **60 sec** |

### 主要特征 Features

**English:**
1. The bypass engines have a bypass ratio of 0.57:1; mass flow of area is increased by additional bypass air at exit, increasing propulsive efficiency.
2. IGV of LPC, IGV of HPC & 1st and 2nd stage stator blades of HPC are variable — they regulate airflow to LPC & HPC depending on engine conditions.
3. The engine has a C-D nozzle capable of swiveling (tilting), enabling efficient expansion of exhaust gases for improved engine performance & high maneuverability.
4. This engine features a very high thrust-to-weight ratio of **8:1**.
5. Max deflection of the nozzle is **±14°**.

**中文：**
1. 涵道比为0.57:1，出口处旁通气流增加了质量流量，提升推进效率。
2. 低压压气机进口导叶（IGV）、高压压气机IGV及高压压气机第1/2级静子叶片均为可变形式，可根据发动机工况自动调节进气量。
3. 发动机配备收-扩（C-D）型喷管，可偏转（摆动），实现排气的高效膨胀，提升发动机性能和机动能力。
4. 推重比高达 **8:1**。
5. 喷管最大偏转角为 **±14°**。

---

## 第四章 各部件详解
## Chapter 4: All Parts Details

### 1. 进口导叶组件 IGV Assembly

**English:** The purpose of the IGV (Inlet Guide Vane) is to vary the inlet cross-sectional area of the LP Compressor. It is made of titanium alloy & it is a load-carrying member of the engine. It consists of 23 internal and external rings connected by 23 moveable IGVs. The circular ring cavity on the external ring forms a channel to convey hot air trapped from the HP Compressor for the deicing system. Their leading edge is fixed & trailing edge is moveable, capable of deflection from -30° ~ 0°.

In AL-31FP, the inlet guide vanes are variable so that their local angle of incidence can be changed according to velocity and altitude of flight automatically by a fly-by-wire control unit. There is a temperature sensor at this section; if the temperature is very low and ice forms, it activates the anti-icing system, which blows hot air tapped from the turbine section into the hollow section of guide vanes to heat the intake air.

The guide vanes are manufactured from titanium-based alloy by forging and machining processes. The outer casing is made of aluminum alloy by forging and machining.

**中文：** 进口导叶（IGV）的作用是改变低压压气机的进口截面积，由钛合金制成，是发动机的承力构件。由23个内外环组成，通过23个可动IGV连接。外环上的环形腔构成导流通道，将来自高压压气机的热空气导入防冰系统。IGV前缘固定，后缘可动，偏转范围为-30°至0°。

在AL-31FP中，进口导叶为可变形式，可通过电传飞控单元根据飞行速度和高度自动改变局部入射角。此部位设有温度传感器；如温度过低导致结冰，防冰系统自动启动，将从涡轮部分引出的热空气吹入导叶空腔，加热进口气流。

导叶由钛基合金经锻造和机械加工制成；外机匣由铝合金锻造并机加工而成。

---

### 2. 压气机组件 Compressors Assembly

**English:** Compressors are installed to provide compressed air to the combustion chamber and other parts of the engine. Compressors are equipped with airfoil-shaped blades — one set fitted with the main spindle (rotor) and another fixed with the inner casing in a static condition (stator). One set of rotor and one stage of stator makes one stage. The rotor compresses the air; the stator guides the compressed air to make it laminar. There are 3 main compressor assemblies:
1. LPC (Low Pressure Compressor)
2. HPC (High Pressure Compressor)
3. Compressor of intermediate casing

**中文：** 压气机的功能是向燃烧室和其他发动机部件提供压缩空气。压气机配备翼型截面叶片——一组安装在主轴上（转子），另一组固定在内机匣上（静子）。一组转子和一级静子构成一个压气机级：转子压缩空气，静子引导压缩气流使其层流化。共有三个主要压气机组件：
1. 低压压气机（LPC）
2. 高压压气机（HPC）
3. 中间机匣压气机

#### 2.1 低压压气机 LPC (Low Pressure Compressor)

**English:** It is purposed to compress the air & supply it to the bypass duct & main duct; it consists of 4 stages of stator and rotor assembly — LPCR (Low Pressure Compressor Rotor) & LPCS (Low Pressure Compressor Stator).

- **LPCR:** Cylindrical type construction with two supports — front roller bearing and rear ball bearing.
- **LPCS:** In the casing, stator blades of stages 1, 2, 3 are connected with flanges with special bolts. Has an outer inner shroud; outer shrouds are grooved in casing.

Compressor blades are made of titanium alloys, which can sustain high pressure. After forging, blades undergo CNC profile making, broaching, milling, grinding, polishing, and coating operations.

**中文：** 低压压气机（LPC）用于压缩空气并将其供给旁通管道和主管道，由4级转子-静子组件构成（LPCR与LPCS）。

- **LPCR（低压压气机转子）：** 圆筒型结构，配备前滚柱轴承和后滚珠轴承两个支撑。
- **LPCS（低压压气机静子）：** 机匣中第1、2、3级静子叶片通过凸缘和专用螺栓连接，具有外内侧围带，外侧围带在机匣中开槽固定。

压气机叶片由钛合金制成，耐高压。锻造后需经过CNC成型、拉削、铣削、磨削、抛光和涂层等系列工序。

#### 2.2 高压压气机 HPC (High Pressure Compressor)

**English:** HPC delivers highly compressed air to the main engine duct connected to the combustion chamber (C.C). The HPC consists of Stator & Rotor blades of 9 stages.

- **HPCR (High Pressure Compressor Rotor):** Drum-disk type construction. The 1st section includes stages 1, 2, 3 (Electron Beam Welded — cannot be dismantled). The 2nd section comprises discs of stages 4, 5, 6 with cone-type flanges for load bearing. The 3rd section includes discs for stages 7, 8, 9 with labyrinth sealing. A special bolt passes through the rings, discs, and finally attaches to the turbine shaft to transmit torque from HPTR.

- **HPCS (High Pressure Compressor Stator):** 1st casing accommodates IGV & 1st stage stator blade; 2nd casing accommodates 4th to 8th stage stator blades; last and 9th stage stator blade is installed on the Combustion Chamber casing. HPC blades are also forged; most stages undergo cold rolling processes.

**中文：** 高压压气机（HPC）将高度压缩的空气输送至与燃烧室（C.C）相连的主发动机管道，由9级定子和转子叶片组成。

- **HPCR（高压压气机转子）：** 鼓盘型结构。第1段包含1~3级（电子束焊接，不可拆卸）；第2段包含4~6级盘，具有锥型凸缘承载负荷；第3段包含7~9级盘，带迷宫式密封。特制螺栓穿过隔环和各盘，最终固接到涡轮轴以传递HPTR扭矩。

- **HPCS（高压压气机静子）：** 第1机匣安装IGV和第1级静子叶片；第2机匣安装第4~8级静子叶片；最后一级（第9级）静子叶片安装在燃烧室机匣上。HPC叶片同样为锻造件，大多数级采用冷轧工艺加工。

#### 2.3 中间机匣压气机 Intermediate Casing Compressor

**English:** It is the primary load-carrying member of the engine. The air delivered from the LPC is divided into bypass main duct flow. Thrust from the engine is transferred to the aircraft through this casing. It contains an outer ring, inner ring & splitter nose ring, and 12 hollow struts connecting all three rings. It is made of nickel-based alloy. At the intermediate casing, the bypass ratio of LPC compressed air is 0.57:1. The bypassed air is used in the cooling process by exchanging heat at the combustion chamber through heat exchangers.

The **Central Bevel Drive** — said to be the heart of power transmission in the engine — is also placed in this intermediate casing. Aircraft gear box transmits power to the engine gear box through a flexible shaft. The engine gear box transmits rotational power to the central bevel drive, and the bevel gear changes the direction of power by 90 degrees to drive the HPC rotor. When the HPC rotor attains 40% of its RPM, the aircraft auxiliary power automatically cuts off and engine turbine power takes over.

**中文：** 中间机匣是发动机的主要承力构件，来自LPC的空气在此分流为旁通主管道气流，发动机推力通过该机匣传递给飞机机体。它由外环、内环及分流鼻环组成，12根空心支柱连接三个环，由镍基合金制成。LPC压缩空气旁通比为0.57:1，旁通空气通过热交换器在燃烧室处参与冷却换热。

**中央锥齿轮传动装置**（被称为发动机动力传输的"心脏"）也安装于此机匣中。飞机齿轮箱通过柔性轴向发动机齿轮箱传递动力，发动机齿轮箱再将旋转动力传给中央锥齿轮传动装置，锥齿轮将动力方向改变90度以驱动HPC转子。当HPC转子达到其转速的40%时，飞机辅助动力自动切断，发动机涡轮功率接管。

---

### 3. 燃烧室组件 Combustion Chamber Assembly

**English:** The combustion chamber is the main unit of the gas turbine engine where the oxidization process gets completed and thrust is produced for the turbine blades to rotate the shaft. In AL-31FP, the combustion chamber is of the **'annular' type** with 28 atomizers and two manifolds. It is made of 5 components — outer casing, inner casing, flame tube, manifold, and burner — all forged separately and assembled together. As the combustion chamber is the hottest section, it is made of nickel-based alloy called **BT-20** and the casings are made up by isothermal forging.

After the combustion chamber there is an air heat exchanger (turbine cooling section). It is activated only when the exhaust temperature of the combustion chamber increases by 800°C and when the HP shaft goes to 92% of its initial RPM.

**中文：** 燃烧室是燃气涡轮发动机中完成氧化反应、为涡轮叶片转动轴提供推力的核心部件。在AL-31FP中，燃烧室为**环形**类型，配备28个雾化器和两个燃油总管。由5个部件组成——外机匣、内机匣、火焰筒、总管和燃烧器，各自分别锻造后组装在一起。由于燃烧室是温度最高的部位，材质为镍基合金**BT-20**，机匣由等温锻造工艺制成。

燃烧室后方设有空气热交换器（涡轮冷却段），仅在燃烧室排气温度超过800°C且高压轴转速达初始转速92%时才激活工作。

---

### 4. 涡轮组件 Turbine Assembly

**English:** In AL-31FP, the turbine section is a two-stage impulse-reaction type. One stage is the High Pressure Turbine (HPT) and the second is the Low Pressure Turbine (LPT). The turbine discs and blades are made of nickel-based alloys capable of heat resistance. The blades are specially made by investment casting with no post-surface finishing process because of their precision.

The HPT turbine is connected to the HPC compressor by means of the high-pressure spool; LPT and LPC are connected by means of the low-pressure spool.

Hot gases from the combustion chamber are initially guided by turbine stator blades (1st stage turbine nozzle guide vanes), then pass over 1st stage turbine rotor blades, and so on through the next stage. Gas molecules expand through the rotor blades — the kinetic energy of gas molecules transfers to the blades, creating impulse-reaction, causing the turbine to rotate.

The **HPT rotor blades** have a typical aerofoil shape with small holes drilled by EDM (Electron Discharge Machine). These holes are interconnected with the disc to allow cold compressed air flow between the compressor and turbine through the bleed-air system.

**中文：** AL-31FP的涡轮段为两级冲击-反力型。一级为高压涡轮（HPT），另一级为低压涡轮（LPT）。涡轮盘和叶片由耐热镍基合金制成，叶片采用精密铸造（熔模铸造），成型后无需后续表面精加工。

高压涡轮通过高压轴与高压压气机相连；低压涡轮和低压压气机通过低压轴相连。

来自燃烧室的高温燃气首先由涡轮静子叶片（第1级涡轮导向叶片）引导，随后流过第1级涡轮转子叶片，依次流过后续各级。气体分子膨胀做功，动能传递给叶片，产生冲击-反力使涡轮旋转。

**高压涡轮转子叶片**为标准翼型，通过电火花加工（EDM）在叶片上钻小孔，这些孔与叶盘相互连通，通过引气系统允许压气机中的冷压缩空气流过，实现涡轮冷却。

**两种涡轮 Two Types of Turbines in AL-31FP:**

- **LPT（低压涡轮）：** 驱动低压压气机 Drives Low Pressure Compressor
- **HPT（高压涡轮）：** 驱动高压压气机及飞机/发动机附件齿轮箱（A.A.G.B & E.A.G.B） Drives HPC and Aircraft/Engine Accessory Gear Boxes

每个涡轮均为单级，转子和导向叶片（N.G.V）各90片。轴承支撑为发动机承力构件，径向载荷通过级间轴承从HPT和LPT转子传递到轴承支撑。

---

### 5. 加力燃烧室与扩压器组件 Afterburner & Diffuser Assembly

**English:** **Afterburner (reheat)** is used for cruise improvement and is intended only for 'CRUISING SPEED'. This device performs the 'after-burning' process at the exhaust nozzle to provide **thrust augmentation** — meaning improving the thrust efficiency of the engine for better performance in short-length take-off and higher cruising speed.

In AL-31FP, the afterburner section consists of **5 fuel manifolds**. At initial activation, fuel is supplied to the primary manifold and oxygen is supplied for the ignition process. Then the afterburner fuel pump supplies fuel to manifolds 2, 3, 4, 5 in sequence. There are two flame stabilizers — one large and one small. By activating the afterburner, thrust increases **6-9%** and there is a temperature increase of **15°C every 5 seconds**. It uses **5 liters/sec** of fuel in full reheat 'C' mode.

**中文：** **加力燃烧室（再燃加热）** 用于提升巡航性能，主要在"巡航速度"下使用。该装置在排气喷管处执行"二次燃烧"过程，实现**推力增益**——即改善发动机推力效率，以实现短距起飞和更高巡航速度。

在AL-31FP中，加力燃烧室段由**5个燃油总管**组成。初始激活时，燃油先供给主燃油总管，同时供氧点火。随后，加力燃油泵依次向第2、3、4、5号总管供油。设有两个稳焰器（一大一小）。激活加力燃烧室可使推力增加**6~9%**，每5秒温度上升**15°C**，全加力"C"模式油耗为**5升/秒**。

**加力燃烧室主要部件 Afterburner Components:**

| 部件 Component | 功能 Function |
|---------------|-------------|
| 排气混合器 Exhaust Mixture | 在过渡段前混合主管道气流与旁通气流 Mix main duct gas stream with bypass airflow before transition section |
| 过渡段 Transition Section | 确保加力燃烧室内燃料的稳定燃烧 Designed for steady burning of fuel in afterburner |
| 加力燃烧室机匣 AB Casing | 由机匣和隔热屏组成，旁通空气冷却喷管和机匣 Consists of casing & shield; bypass air cools the jet nozzle and casing |
| 排气整流罩 Exhaust Fairing | 减少排气能量损失，减弱加力中间燃烧 Decrease exhaust gas energy losses |

**English:** **Diffuser:** Slows down compressor delivery air to reduce flow losses in the combustor. Slower air stabilizes the combustion flame and higher static pressure improves combustion efficiency. There are two casings — inner and outer — made of mnemonic material; compressed air from the compressor is passed between casings to cool the hot gases using the bleed-air system.

**中文：** **扩压器：** 降低压气机出口气流速度，减少燃烧室流动损失。较低的气流速度有助于稳定燃烧火焰，较高的静压有助于提高燃烧效率。由内外两个机匣组成，来自压气机的压缩空气通过机匣间流动，利用引气系统冷却高温燃气。

---

### 6. TVC 喷管组件 TVC Nozzle Assembly

**English:** The thrust vectoring variable-area jet nozzle is an all-mode supersonic C-D nozzle. Its main parts are:
1. Tilting Device
2. Subsonic Nozzle
3. Supersonic Nozzle

**中文：** 推力矢量可变面积喷管是一种全模式超音速收-扩（C-D）喷管，主要部件包括：
1. 偏转装置
2. 亚音速喷管
3. 超音速喷管

#### 偏转装置 Tilting Device
**English:** Consists of fixed and moveable casing — the fixed casing is hinged to the moveable casing by means of pivots. The moveable casing is turned with respect to the fixed casing at a maximum angle of **±14°** by means of two pairs of hydraulic cylinders located on both sides of the horizontal axis of the tilting device. The hinged pin is inclined at **32°** counter-clockwise for the LH engine and clockwise for the RH engine, viewed from the rear.

**中文：** 由固定机匣和可动机匣组成，固定机匣通过销轴铰接到可动机匣。可动机匣相对固定机匣的最大偏转角为 **±14°**，由位于偏转装置水平轴两侧的两对液压缸驱动。铰销相对水平面倾斜 **32°**——从后方观察，左发动机为逆时针方向，右发动机为顺时针方向。

#### 亚音速喷管 Subsonic Jet Nozzle
**English:** The convergent nozzle with synchronization drive and control mechanism to control the nozzle throat. 16 convergent nozzle shutters with 16 sealing spacers form the convergent subsonic jet nozzle. The shutters are controlled by 16 hydraulic cylinders; a high-pressure pump (NP-160D) delivers fuel under pressure to the jacks. Control is carried out by the engine nozzle and afterburner controller (RSF-31BT1).

**中文：** 收敛型喷管，带有同步驱动和控制机构以控制喷管喉道。16个收敛型喷管挡板加16个密封衬垫构成收敛型亚音速喷管。挡板由16个液压缸控制；高压泵（NP-160D）向作动筒供压油。控制由发动机喷管与加力燃烧室控制器（RSF-31BT1）执行。

#### 超音速喷管 Supersonic Nozzle
**English:** A divergent nozzle with synchronization drives and control mechanism to control the jet nozzle exit area. 16 divergent nozzle shutters with 16 sealing spacers form the divergent supersonic section of the jet nozzle. Hydraulic cylinders control the shutters.

**中文：** 扩张型喷管，带同步驱动和控制机构，用于控制喷管出口面积。16个扩张型喷管挡板加16个密封衬垫构成喷管的扩张超音速段，液压缸控制挡板运动。

#### 喷管主要控制部件 Main Parts of Nozzle

| 编号 | 部件名称 | 中文 | 功能 Function |
|------|---------|------|--------------|
| 1 | Jet nozzle casing | 喷管机匣 | 连接扩压器和喷管段，钛基合金制 |
| 2 | Flaps | 挡板 | 控制喷管喉道面积的活动部件 |
| 3 | Spacers | 衬垫 | 静止零件，通过铰链支撑挡板 |
| 4 | Mechanical linkages | 机械连杆 | 在压力缸激活时传递机械运动的连接件 |
| 5 | Hydraulic cylinders | 液压缸 | 两种类型：4个用于偏转喷管，16个用于控制喉道面积 |
| 6 | Pneumatic cylinders | 气动缸 | 16个，限制上挡板过度膨胀/收缩 |
| 7 | Graphite ring | 石墨环 | 嵌于喷管与加力扩压器段之间，偏转时提供润滑 |

---

## 第五章 附件系统（航电）
## Chapter 5: Aggregates (Avionics)

**English:** Aggregates are the most important controlling parts of the AL-31FP engine, controlling the engine to provide maximum performance, increased safety level, and providing updated information about the engine to the pilot.

**中文：** 附件系统是AL-31FP发动机最重要的控制部件，用于控制发动机以实现最大性能，提升安全水平，并向飞行员提供发动机的实时状态信息。

| 编号 | 名称（型号） Name (Model) | 功能 Function |
|------|--------------------------|--------------|
| 1 | 燃油分配器 Fuel Oil Distributor [RT31-VT1] | 向主燃烧室第1、2级燃油总管分配燃油 |
| 2 | 加力燃烧室燃油泵 AB Fuel Pump [RTF-31AT1] | 向第1~4加力总管分配燃油，维持加力段最小油耗 |
| 3 | 助推泵 Booster Pump [DTsN-82] | 向主燃油泵、加力泵、柱塞泵供油；提升油箱油压以供高压燃油系统 |
| 4 | 应急排油装置 Emergency Draining Unit [99.10.34.000] | 飞行中排放油箱内燃油；紧急降落时可从座舱直接操控 |
| 5 | 柱塞泵 Plunger Pump [NP-160D] | 通过喷管和加力控制器[RSF-31BT1]向液压缸供压油 |
| 6 | 燃油滤 Fuel Oil Filter [8D2.966.133-01] | 16微米过滤器，过滤供给发动机各部件的燃油中的杂质 |
| 7 | 喷管与加力调节器 Regulator of Nozzle & AB [RSF-31VT1] | 含3个系统：(a)喷管控制 (b)加力燃油控制 (c)涡轮冷却控制 |
| 8 | 调节泵 Regulator-Pump [NR-31VT1] | 含泵送单元（齿轮型）和调节单元；控制低压压气机IGV和高压压气机可变静子叶片 |
| 9 | 再热泵 Reheating Pump [FN31AT1] | 离心泵，为加力燃油分配器[RTF-31AT1]提升油压 |
| 10 | 气囊式温度传感器 Gas-capsule Thermo Sensor [TDKM] | 感知进口气温(t1)，向主燃油泵和喷管再热调节器发出液压指令以修正油流 |
| 11 | 柱塞泵控制单元 Plunger Pump Control Unit [AUPN-96BT1] | 控制柱塞泵[NP-160D]出口压力，用于驱动喷管液压缸 |
| 12 | 涡轮压比调定附件 Turbine Setting Aggregate [APP-96BT1] | 通过改变喷管喉道面积控制涡轮膨胀比(P₂/P₄) |
| 13 | 安全阀 Safety Valve [KP-96BT1] | 当柱塞泵[NP-160D]压力超过240 kg/cm²时旁通燃油 |
| 14 | 燃油计量器 Fuel Feed Meter [4033 series 69] | 通过热射流法实现加力燃油点火 |
| 15 | 电液分配器 Electro Hydraulic Distributor [EGR-4VT1] | 通过两路独立电气通道和一路液压通道向喷管偏转液压缸分配燃油 |
| 16 | 燃油热交换器 Fuel Oil Heat Exchanger [6139T] | 交叉流热交换器，利用主管和加力段出口燃油冷却受热机油 |
| 17 | 转速传感器 Sensor of Tachometer [D-3M] | 向飞机座舱显示低压转子转速(n1)和高压转子转速(n2)的电信号 |
| 18 | 同步发射机 Synchro Transmitter [DS-11V] | 共3个，测量喷管挡板位置、低压压气机IGV位置和高压压气机可变静子叶片位置，向MFWS提供信号 |
| 19 | 润滑油液位传感器 Lube Oil Level Indicator [DSMK8A-47] | 安装在油箱上，测量发动机油位，向飞机电气系统提供电信号 |
| 20 | 振动测速器 Vibro Speed Indicator [MV-27-1G] | 测量发动机机匣振动，将水平和垂直振动转换为电信号，输送至发动机综合调节器(KRD-99B) |
| 21 | 燃气涡轮启动机 Gas Turbine Engine Power Unit [GTDE117-1MO] | 在发动机启动时将发动机带转至自持转速（冷/湿盘车转速18±30%） |
| 22 | 电磁阀 Electro Magnetic Valve | 溶剂阀，用于操控防冰系统；接收飞机结冰探测单元的反馈并自动打开引气管路 |
| 23 | 发动机综合调节器 Complex Regulator of Engine | 电子控制单元，调控所有发动机模式下的油流；接收各类传感器指令，控制发动机启动、加力、涡轮冷却、喘振等 |
| 24 | 力矩传感器 Moment Sensor | 监测低压压气机IGV、挡板位置和高压压气机可变静子叶片位置，输出信号 |
| 25 | 转速传感器 RPM Sensor | 测量低压转子转速，安装于BKA |
| 26 | 耐热压力指示器 Heat Resistance Pressure Indicator | 压力开关，为发动机附件齿轮箱轴承选择正确的气压管路 |
| 27 | 耐热振动稳定压力指示器 Heat Resistance Vibration Stability Pressure Indicator | 感知涡轮启动机(GTDE-IA-IMO)所有供油管路中的压力；油压低于1 kg/cm²时自动停止涡轮启动机 |
| 28 | 变换器压力传感器 Sensor of Transformer Pressure | 测量柱塞泵压力管路中的燃油压力，转换为电信号 |
| 29 | 变压器压力传感器 Transformer Pressure Sensor | 变压器型压力传感器，测量油路压力并转换为电信号，输送至发动机综合控制器 |

---

## 第六章 气动缸故障研究
## Chapter 6: Research on Failure of Pneumatic Cylinder

### 气动学与气动缸定义 What is 'Pneumatic' and Pneumatic Cylinder

**English:** **'Pneumatics'** is a branch of engineering that deals with the study of and makes use of gas or pressurized air. Pneumatic systems are commonly powered by compressed air or compressed inert gases. A centrally located and electrically powered compressor powers cylinders, air motors, and other pneumatic devices. A pneumatic system is selected when it provides a lightweight, lower cost, more flexible, or safer alternative to electric motors, actuators & hydraulic oil storage.

**'Pneumatic cylinder'** (or air cylinder) is the component or mechanical device which converts the fluid energy or pressurized air force to mechanical energy or linear reciprocating motion. Compressed air forces a piston to move in the desired direction. The piston is a cylinder, and the piston rod transfers the force it develops to the object to be moved. Materials can be nickel-plated brass, aluminum, steel, and stainless-steel, depending on level of loads, humidity, temperature, and stroke lengths specified.

**中文：** **"气动学"** 是工程学的一个分支，研究并利用气体或压缩空气。气动系统通常由压缩空气或压缩惰性气体驱动，由集中安装的电动压缩机驱动气缸、气动马达和其他气动装置。当需要比电动马达、执行器和液压油存储更轻便、成本更低、更灵活或更安全的方案时，优选气动系统。

**"气动缸"**（或空气缸）是将流体能量或压缩空气力转换为机械能或线性往复运动的部件或机械装置。压缩空气推动活塞向预定方向移动，活塞杆将产生的力传递给被移动物体。材质可为镀镍黄铜、铝、钢或不锈钢，视载荷大小、湿度、温度和行程长度而定。

### 气动缸类型与设计 Types and Design

**类型 Types:**
1. 单作用式 Single acting
2. 双作用式 Double acting
3. 伸缩多级式 Telescopic, Multi stage
4. 双出杆式 Through rod air cylinders
5. 缓冲端盖式 Cushion end air cylinders
6. 旋转式 Rotary air cylinders
7. 无杆式 Rod less air cylinders
8. 串联式 Tandem air cylinder
9. 冲击式 Impact air cylinder

**设计类型 Design Types:**
1. **拉杆式 Tie rod cylinders** — 最常见，适用多种载荷，安全性最高
2. **法兰式 Flanged-type cylinders** — 两端加固定法兰，多用于液压缸
3. **焊接整体式 One-piece welded cylinders** — 端盖焊接或卷边固定，成本低但不可维修
4. **螺纹端盖式 Threaded end cylinders** — 端盖螺接于筒体，材料减少可能导致螺纹同心度问题

### 工作原理与受力关系 Working Principles, Area, Force Relationship

#### 活塞杆应力 Rod Stresses

**English:** Due to the forces acting on the cylinder, the piston rod is the most stressed component and must be designed to withstand high amounts of bending, tensile and compressive forces. If the rod's length is less than 10 times its diameter, it may be treated as a rigid body:

$$F = A\sigma$$

Where: **F** = compressive or tensile force; **A** = cross-sectional area of piston rod; **σ** = stress

**中文：** 由于气缸所受的各种力，活塞杆是受力最大的部件，必须能承受大量的弯曲、拉伸和压缩力。若杆的长度小于其直径的10倍，可视为刚体：

$$F = A\sigma$$

其中：**F** = 压缩力或拉伸力；**A** = 活塞杆截面积；**σ** = 应力

#### 进程与回程 Instroke and Outstroke

**外伸行程力 Outstroke Force:**
$$F_r = P(\pi r^2)$$

**缩回行程力 Instroke Force:**
$$F_r = P(\pi r_1^2 - \pi r_2^2) = P\pi(r_1^2 - r_2^2)$$

其中 Where: **F_r** = 合力 resultant force；**P** = 压力 pressure；**r** = 活塞半径 piston radius；**r₁** = 活塞半径 piston radius；**r₂** = 活塞杆半径 piston rod radius

> 由于活塞杆占据一部分截面积，缩回行程的有效截面积小于外伸行程，因此在相同气压下，缩回行程力小于外伸行程力。

### AL-31FP 气动缸结构详情 Pneumatic Cylinder Parts Details

**英文零件名称 | 零件编号 | 中文名称**

| 英文 | 编号 | 中文 |
|------|------|------|
| Flexible inner ring | — | 柔性内环 |
| Link | — | 连杆 |
| (098.7431) NUT | 098.7431 | 螺母 |
| Joint | — | 接头 |
| Passage | 098.7500 | 通道/气道 |
| (104.16.18.004) Piston | 104.16.18.004 | 活塞 |
| Screw | — | 螺钉 |
| Nut | 104.16.18.002 | 螺母 |
| Lock washer | 104.16.003 | 锁紧垫圈 |
| Casing | 104.10.18.010 | 机匣/外壳 |
| Piston rod | 011.16.18.004 | 活塞杆 |
| Sealing ring | 104.16.18.001 | 密封环 |
| Locking Plate | 104.16.18.005 | 锁定板 |
| Cover | 104.16.183.030 | 端盖 |
| Air Pours | — | 气孔 |
| Flexible Link | — | 柔性连接件 |

### 气动缸工作原理详述 Detailed Work

**English:** The pneumatic cylinder driving the jet nozzle of a gas turbine engine includes a housing (1) with a cover (2), a piston (3), and the casing (4). In the housing there is a hole (5) for supplying air into the rod cavity (6); the holes (7) connect the cavity (8) made from the opposite end of the body. The output (10) of the cavity cooling (9) may be made in the form of holes of different sizes in the sector of 180 degrees.

When the cylinder air is supplied into the rod cavity (6), the air passes through the sealing ring (14) of the piston (3). Through holes (7), it is fed into the cavity cooling (9). Air passing through the cavity cooling (9) cools the body (1) and is ejected through the openings (12) to the outside. This cooling reduces the temperature differential housing in the circumferential direction, ensuring maximum cylindricity and straightness of the housing.

The single-acting pneumatic cylinder works normally, and the internal chromium layer coating acts as a lubricant & keeps safe from vapor contaminants; the sealing rings give it smooth operation.

**中文：** 驱动燃气涡轮发动机喷管的气动缸由壳体(1)（含端盖2）、活塞(3)和机匣(4)组成。壳体上有气孔(5)用于向杆腔(6)供气，通孔(7)连接从壳体另一端形成的腔(8)。腔冷却(9)的出口(10)可在180度范围内以不同大小的孔形式布置。

当气缸空气供入杆腔(6)后，空气通过活塞(3)的密封环(14)，经通孔(7)进入冷却腔(9)。气体流经冷却腔(9)后冷却壳体(1)，最终通过开口(12)排出外部。这种冷却方式降低了机匣圆周方向的温度差，确保气动缸机匣的最大圆柱度和直线度。

该单作用气动缸正常工作时，内部铬涂层起润滑剂作用并防止蒸气污染，密封环保证运动顺滑。

### 主要故障原因及控制 Main Failure Reasons and Controlling Them

**English:** Pressure loss is the main failure reason of the pneumatic cylinder (V.J.N) in the AL-31FP engine. The cylinder should sustain **5 kg** of air pressure constantly; in pressure testing it should sustain **95 bar** of pressure. If the cylinder is unable to maintain 5 kg of pressure constantly, it is rejected.

There are two types of pressure loss testing:
1. Newly manufactured cylinders for new engines
2. Cylinders for overhaul engines (overhauled engines' cylinders mostly fail because of **coating wear-out**; new cylinders fail due to **pressure loss**)

**中文：** 压力损失是AL-31FP发动机VJN气动缸的主要故障原因。气缸必须持续维持 **5千克** 气压；压力测试中应承受 **95巴** 压力。若气缸无法持续维持5千克气压则被判定为不合格。

两类压力损失测试：
1. 新发动机用新生产气缸
2. 大修发动机用气缸（大修气缸主要因**涂层磨损**失效；新气缸主要因**压力泄漏**失效）

#### 压力泄漏测试 Pressure-Loss Test & Leak Test

**压力损失测试 Pressure-loss test:**

**English:** Carried out by an apparatus — a square type metallic box with a tube for air injection, designed for inside air vacuuming. The cylinder is set by semi-opened and fixed in that box. After the cylinder is fixed inside and the box is closed and vacuumed, 5 kg of air pressure is injected through the tube with a mass flow rate of 2.0839 to the link continuously. If the pressure drops in the middle of the operation without sustaining 5 kg/95 bar pressure, it is rejected.

**中文：** 通过一种装置进行——正方形金属箱体，配有注气管，可对内部进行抽真空。气缸半开口固定在箱内，封闭并抽真空后，以质量流量2.0839持续向连接件注入5千克气压。若操作过程中压力下降，无法维持5千克/95巴，则判定为不合格。

**泄漏测试 Leak test:**

**English:** This test is carried out with white kerosene/turbonic oil under a cotton napkin at a pressure force of **35~36 kgf/cm²** (35×10⁵ ПА) for **10~11 minutes**.

**中文：** 用白煤油/涡轮机油，在棉布覆盖下，以 **35~36 kgf/cm²**（35×10⁵ ПА）的压力进行，持续 **10~11分钟**。

### 一般失效原因 Normal Failure Reasons of the Pneumatic Cylinder

#### 污染物 Contaminants

**English:** Cylinders can be contaminated internally from the air supply or externally from the operating environment. Types of contamination include solids, water, and oil.

**中文：** 气缸可能受到来自气源的内部污染或来自工作环境的外部污染，污染物类型包括固体、水和油。

- **固体污染 Solids:** 颗粒物一旦穿过密封，会嵌入密封件和轴承，形同砂纸磨损，显著缩短密封寿命。防控措施包括：保留制造商出厂堵头直至安装管路，安装前彻底清洗管路。恶劣环境下可安装防护屏蔽、金属刮屑器或防尘套。

- **水 Water:** 压缩空气中的水蒸气会聚集在元件内部，堵塞节流孔、稀释预润滑脂、污染润滑油、损坏缸筒或杆的表面光洁度，并在低温下结冰。防控措施：在气缸内壁施加涂层。

- **油污 Oils:** 来自空压机润滑油携带或不相容合成油，会导致密封件溶胀和节流孔堵塞。防控措施：选择与应用中使用的油品相容的密封材料。

#### 润滑不足 Insufficient Lubrication

**English:** Catastrophic failure can occur when cylinder seals have insufficient lubrication. High or fast cycle rates can generate unsustainable shock loads at the end of a stroke when the piston hits the end-cap, or seals can run dry from a lack of lubrication. Heat generated by the system could compromise component temperature limits.

**中文：** 当气缸密封件润滑不足时，可能发生灾难性失效。高频或快速循环会在活塞撞击端盖时产生不可承受的冲击载荷，或密封件因缺乏润滑而干磨。系统产生的热量可能超出零件的温度极限。

#### 超限运行 Operating Over Component Limits

**English:** Operating a cylinder over pressure, load and/or energy limits can cause the component's failure. When cylinders run at overload capacity, seals are subjected to higher stress and friction rates. Rod ends bend or break, and actuators can come apart. Pressure spikes can occur that are two to three times above normal system pressures.

**中文：** 超压、超载或超能量极限运行气缸会导致零件失效。超载时，密封件承受更高的应力和摩擦；杆端弯曲或断裂，执行器可能解体；压力峰值可达正常系统压力的2~3倍。

---

### AL-31FP 气动缸实际缺陷分析 Actual Defects Found on AL-31FP Pneumatic Cylinder

**English:** Investigating the detailed working procedure of the cylinders, the first basic finding is that most imported items like cylinders directly imported from Russia show various defects. Therefore, the machining and other manufacturing processes now operated in HAL (Koraput Division) show fewer defects and better quality. However, the materials are still imported from Russia as billet shape.

**Three main defect categories found:**

1. **Chromium Coating Issue (New & Overhaul cylinders):** When the inner coating (CHROMIUM COATING FOR ANTI-OXIDIZATION AND SMOOTHNESS) grinding process is applied, the thin shape of the cylinder becomes slightly oval due to incorrect grinding procedure. The sealing ring also fails for this reason, reducing the air sustaining capacity of 5 kg.

2. **Piston Manufacturing Issue:** Piston without coating and with improper manufacturing causes pressure leakage. Special coating (Graphite or similar) provides a lubricated surface similar to a leak-proof surface.

3. **Piston Rings (Most Critical):** The piston rings provide the cylinder with friction-less and smooth operation with a leak-proof surface. When these rings wear out, they can cause serious damage to the chromium coating surface, decreasing its lifespan and frequently reducing its pressure sustaining ability of 5 kg.

> **结果 Result:** These 100% probable problems were found during the study of the Pneumatic cylinder of the VJN assembly. After collecting this information from respective workers and managers, and taking precaution about these issues, a **40% improvement in manufacturing** has been achieved.

**中文：** 对气缸详细工作过程的调查发现：直接从俄罗斯进口的气缸存在多种缺陷。因此，HAL科拉普特分部现自行进行机加工等制造工序后，缺陷更少、质量更好，但毛坯料仍从俄罗斯进口。

**发现的三类主要缺陷：**

1. **铬涂层问题（新缸和大修缸均存在）：** 内壁涂层（防氧化和光滑性铬涂层）磨削工序中，由于磨削工艺不当，气缸薄壁变成轻微椭圆形，导致密封环失效，5千克承压能力下降。

2. **活塞制造问题：** 活塞无涂层或制造工艺不良，导致压力泄漏。特殊涂层（石墨或类似材料）可提供类似防漏的润滑表面。

3. **活塞环问题（最关键）：** 活塞环为气缸提供无摩擦、光滑的防漏运动。活塞环磨损后，会严重损伤铬涂层表面，缩短其使用寿命，导致5千克承压能力频繁下降。

> **结论：** 这三类问题是VJN气动缸的100%可能故障原因。在与车间工人和管理人员沟通采取预防措施后，制造质量提升了 **40%**。

---

## 气动缸使用优势 Advantages of Pneumatic Cylinders

| 优势 Advantage | 英文 English | 中文 Chinese |
|--------------|-------------|-------------|
| 设计与控制简便 | Simplicity of design and control | 使用标准气缸和元件即可轻松设计机器，通过简单的开关控制运行 |
| 可靠性高 | Reliability | 气动系统寿命长，维护少；气体可压缩，受冲击损伤小；断电后仍可短期运行 |
| 安全性好 | Safety | 与液压油相比，火灾风险极低；新型机器通常具有防过载保护 |
| 重量轻 | Light weight | 气动缸轻便，无需大容量液压液储罐 |

---

## 总结 Conclusion

本实习项目在印度斯坦航空有限公司（HAL）科拉普特分部SU-30发动机部门完成，历时一个月（2016年6月10日至28日）。

This internship project was completed at HAL Koraput Division's SU-30 engine department over one month (June 10–28, 2016).

**主要成果 Key Outcomes:**
- 熟悉了AL-31FP涡轮喷气发动机的整体结构与各部件工作原理
- Gained familiarization with the complete structure and working principles of the AL-31FP turbojet engine
- 深入研究了TVC喷管中气动缸的失效机理
- Conducted in-depth research on the failure mechanisms of pneumatic cylinders in the TVC nozzle
- 发现三大类缺陷（铬涂层椭圆化、活塞制造不当、活塞环磨损），提出改进措施后制造质量提升40%
- Identified three main defect categories and achieved 40% manufacturing quality improvement after implementing precautionary measures

---

*来源 Source: HAL Koraput Division Internship Report — "Familiarization About AL-31FP and Its Different Component and a Research Work on the Pneumatic Cylinder in TVC Nozzle"*  
*作者 Author: Kamalakanta Mohapatra, Bhubaneswar Engineering College, Aeronautical Engineering*  
*指导 Guide: Mr. R.G. Mishra & Mr. Shibendu Sen, 620-Assembly Shop SED, HAL*  
*版权声明 Copyright Note: Figures courtesy H.A.L — used by permission only*
