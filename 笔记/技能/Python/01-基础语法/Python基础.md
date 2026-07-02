---
source: 综合（无单一原资料；以官方教程 + 入门共识整理）
type: study-note
subject: Python
date: 2026-07-02
keywords: [python-basics, variables, types, control-flow, io]
tags: [study-note, python]
---

# Python 基础 — 从零开始

#python #basics

## 什么是 Python？

一·**定义**：Python 是一种**解释型、动态类型、强类型**的高级编程语言，由 Guido van Rossum 于 1991 年发布，以代码**可读性**和**简洁缩进**著称。

二·**特性 / 适用范围**：
  1. 解释型：逐行执行，无需编译，REPL 友好。
  2. 动态类型：变量类型运行时推断，无需声明。
  3. 强类型：不允许隐式跨类型运算（`"3" + 1` 报错，而非像 JS 那样静默转换）。
  4. 缩进即语法：用缩进表示代码块，**没有大括号**。
  5. 应用广：Web（Django/FastAPI）、数据科学（pandas/NumPy）、AI（PyTorch）、自动化脚本。

三·**核心理解**：
> [!note] 核心理解
> 设计哲学上：Python 用「**强制缩进**」换来对齐的视觉结构，用「**电池齐备**」（batteries included）换来开箱即用的标准库。它的易读性不是附赠品，而是被写进语言规范（PEP 8 / PEP 20 Zen of Python）的**第一公民**。

四·**易错 / 边界**：Python 2 已于 2020 年停止维护，本笔记一律基于 **Python 3**。

---

## 第一个程序

```python
print("Hello, Python!")      # 输出：Hello, Python!
name = input("请输入名字：")  # 读取一行输入（字符串）
print(f"你好，{name}！")       # f-string 格式化
```

一·**核心理解**：
> [!note] 核心理解
> `print` 默认追加换行，写 `print(x, end="")` 可关闭。`input` 返回**始终是字符串**，要数字得 `int(input(...))`。

---

## 变量与赋值

一·**定义**：变量是**指向对象的名字（标签）**，不是装东西的盒子。赋值是把名字绑定到对象。

二·**赋值形式**：
  1. 普通赋值：`x = 10`
  2. 多重赋值：`a, b = 1, 2`（基于元组解包）
  3. 链式赋值：`a = b = 0`（三者指向同一对象，可变对象要小心）
  4. 增量赋值：`x += 1`（对不可变对象等价 `x = x + 1`）

三·**swap 糖**：
```python
a, b = 1, 2
a, b = b, a          # 一行交换，无需临时变量
```

四·**易错 / 边界**：
```python
a = b = []           # 两个名字指向同一个空列表
a.append(1)
print(b)             # [1] ← b 也变了！因为同一对象
```

---

## 基本数据类型

| 类型 | 示例 | 说明 |
|------|------|------|
| `int` | `10`, `0b1010`, `0xFF` | 任意精度整数 |
| `float` | `3.14`, `1e-3` | 双精度浮点 |
| `bool` | `True` / `False` | 是 `int` 的子类，`True == 1` |
| `str` | `"hello"`, `'a'` | 不可变 Unicode 序列 |
| `NoneType` | `None` | 表示「无值」 |

一·**类型查询与转换**：
```python
type(3.14)        # <class 'float'>
isinstance(x, int)  # 比 type() == int 更推荐（支持继承）

int("42")         # 42
float("3.14")     # 3.14
str(42)           # "42"
bool(0)           # False（0 / "" / [] / None 都为假）
```

二·**核心理解**：
> [!note] 核心理解
> 「假值」（falsy）集合：`0`、`0.0`、`""`、`[]`、`{}`、`None`、`False`。其余一律 truthy。`bool` 是 `int` 子类这一点，使得 `True + True == 2`——既优雅又坑人。

三·**易错 / 边界**：浮点比较别用 `==`：
```python
0.1 + 0.2 == 0.3   # False！二进制无法精确表示
abs(0.1 + 0.2 - 0.3) < 1e-9   # 正确写法
```

---

## 字符串

一·**定义**：`str` 是**不可变**的 Unicode 字符序列，单双引号等价，三引号支持多行。

二·**常用操作**：
```python
s = "Hello, 世界"
len(s)               # 8（Unicode 字符数，不是字节）
s[0]                 # 'H'        正向索引
s[-1]                # '界'        负索引（末尾）
s[0:5]               # "Hello"    切片，左闭右开
s[::-1]              # "界界 ,olleH"  反转字符串
"Hello" + ", " + "Python"   # 拼接
",".join(["a", "b", "c"])   # "a,b,c"  分割/合并
"a,b,c".split(",")          # ["a","b","c"]
f"{3.14159:.2f}"            # "3.14"   格式化
```

三·**易错 / 边界**：字符串不可变 → `s[0] = "h"` 是错的，要 `s = "h" + s[1:]`。

---

## 控制流

### if / elif / else

```python
score = 85
if score >= 90:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
```

一·**条件表达式（三元）**：
```python
grade = "及格" if score >= 60 else "不及格"
```

二·**易错 / 边界**：Python 没有 `switch`（3.10+ 用 `match-case` 模式匹配，见 §进阶）。

### while 循环

```python
n = 0
while n < 3:
    print(n)        # 0, 1, 2
    n += 1
```

### for 循环 + 遍历

```python
for ch in "abc":        # 直接遍历字符串
    print(ch)

for i, ch in enumerate("abc"):   # 需要下标时用 enumerate
    print(i, ch)                  # 0 a / 1 b / 2 c
```

### break / continue / else

```python
for n in range(2, 10):
    for d in range(2, n):
        if n % d == 0:
            break
    else:                            # ← 循环没被 break 时才执行
        print(n, "是质数")
```

一·**核心理解**：
> [!note] 核心理解
> `for...else` 的 `else` 是「**没被打断完成**」的奖励分支，不是「循环条件为假」。这是 Python 语法里最反直觉、也最少被人知道的一个特性。

### range 速查

| 写法 | 含义 |
|------|------|
| `range(5)` | 0,1,2,3,4 |
| `range(2, 6)` | 2,3,4,5 |
| `range(0, 10, 2)` | 0,2,4,6,8（步长 2） |

---

## 输入输出（I/O）

一·**print 进阶**：
```python
print("a", "b", "c", sep="-")    # a-b-c（默认空格，可改分隔符）
print("line", end="")             # 末尾不换行
print(*[1, 2, 3])                 # 1 2 3   星号解包
```

二·**f-string 格式化**（3.6+，主流推荐）：
```python
pi = 3.14159
print(f"π ≈ {pi:.2f}")            # π ≈ 3.14
print(f"{1000:,}")                # 1,000  千分位
print(f"{42:>5}")                 # "   42" 右对齐宽 5
print(f"{42:0>5}")                # "00042" 0 填充
```

三·**% 与 .format（旧写法，认得即可）**：
```python
"%s 年 %d 月" % ("2026", 7)       # "2026 年 7 月"  旧式
"{} x {}".format(2, 3)            # "2 x 3"        新式（f-string 前身）
```

四·**核心理解**：
> [!note] 核心理解
> f-string 在字面量里嵌入 `{表达式}`——它比 `%` / `.format` 都直观，且**性能最好**（运行时一次性编译为字符串拼接）。日常只用它即可。

---

## 速记卡 / 一句话总结

- **Python 是解释型 + 动态类型 + 强类型 + 强制缩进**。
- ==`input` 返回字符串，要数字得转==；`print` 默认换行，`end=""` 关掉。
- **4 类赋值**：普通 / 多重（元组解包）`a,b=1,2` / 链式 `a=b=0`（可变对象慎用） / 增量 `+=`。
- 假值集合：`0 0.0 "" [] {} None`；`bool` 是 `int` 子类 → `True+True==2`。
- 短路布尔：`and` 返回第一个假值、`or` 返回第一个真值，常作默认值 `name or "匿名"`。
- ==浮点永远别用 `==`，用 `abs(a-b) < 1e-9`==。
- 字符串**不可变**：切片/拼接都返回新串，原串不变。
- `for...else`：`else` 是「循环**没被 break**」的奖励分支，最反直觉。
- `range` 三参数 `(起, 止(不包), 步长)`，止端**左闭右开**。
- 格式化首选 **f-string**：`f"{x:.2f}"` `f"{n:>5}"` `f"{n:,}"`。

---

## Related Notes
- [[笔记/技能/Python/02-数据结构/数据结构|数据结构]]
- [[笔记/技能/Python/03-函数与模块/函数与模块|函数与模块]]