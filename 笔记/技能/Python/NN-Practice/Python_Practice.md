---
source: 综合（自编入门练习题）
type: practice
subject: Python
date: 2026-07-02
keywords: [python-practice, exercise, beginner]
tags: [practice, python]
---

# Python 入门练习题

#python #practice

> 选题覆盖基础语法 → 数据结构 → 函数 → 面向对象 → 文件异常五条主线。
> 难度 ★～★★★，★★★ 为入门阶段压轴。先自做，再看答案。

---

## 一·基础语法

### P1.1 ★ 单行求和
读取一行若干个整数（空格分隔），输出它们的和。
输入：`1 2 3 4 5`　输出：`15`

> [!tip]- 答案
> ```python
> nums = map(int, input().split())
> print(sum(nums))
> ```

### P1.2 ★ FizzBuzz
1～100：能被 15 整除输出 `FizzBuzz`；只被 3 整除 `Fizz`；只被 5 整除 `Buzz`；否则输出数字。

> [!tip]- 答案
> ```python
> for n in range(1, 101):
>     if n % 15 == 0: print("FizzBuzz")
>     elif n % 3 == 0: print("Fizz")
>     elif n % 5 == 0: print("Buzz")
>     else: print(n)
> ```

### P1.3 ★★ 回文字符串
判断一个字符串是否回文（如 `abcba`）。要求用切片一行实现。

> [!tip]- 答案
> ```python
> is_pal = (s == s[::-1])
> ```

### P1.4 ★★ 九九乘法表
打印方形九九乘法表，对齐。

> [!tip]- 答案
> ```python
> for i in range(1, 10):
>     for j in range(1, 10):
>         print(f"{i}x{j}={i*j:2}", end="  ")
>     print()
> ```

---

## 二·数据结构

### P2.1 ★ 列表去重保序
给定 `[3,1,2,1,3,4]`，返回 `[3,1,2,4]`（保留首次出现顺序）。

> [!tip]- 答案
> ```python
> seen = set(); out = []
> for x in lst:
>     if x not in seen:
>         seen.add(x); out.append(x)
> # 3.7+ 也可直接 list(dict.fromkeys(lst))
> ```

### P2.2 ★★ 词频统计
统计 `the cat sat on the mat` 中各词出现次数，按次数降序输出。

> [!tip]- 答案
> ```python
> from collections import Counter
> words = "the cat sat on the mat".split()
> for w, c in Counter(words).most_common():
>     print(w, c)
> ```

### P2.3 ★★★ 两数之和
给定列表 `nums` 与目标 `target`，返回和为 target 的两数下标（保证唯一）。

> [!tip]- 答案
> ```python
> def two_sum(nums, target):
>     seen = {}                      # 值 → 下标
>     for i, x in enumerate(nums):
>         need = target - x
>         if need in seen: return [seen[need], i]
>         seen[x] = i
> ```
> 复杂度 $O(n)$——用 dict 把「找」降到 $O(1)$，体现 §02 速记卡的核心。

### P2.4 ★★ 反转链表的列表版
仅用列表操作把 `[1,2,3,4]` 变 `[4,3,2,1]`，三种写法。

> [!tip]- 答案
> ```python
> lst[::-1]              # 切片
> list(reversed(lst))
> lst.reverse()          # 原地反转，返回 None
> ```

---

## 三·函数

### P3.1 ★ 阶乘（递归 & 迭代）
写两个版本。

> [!tip]- 答案
> ```python
> def fac_rec(n): return 1 if n <= 1 else n * fac_rec(n - 1)
> def fac_iter(n):
>     r = 1
>     for i in range(2, n+1): r *= i
>     return r
> ```

### P3.2 ★★ 可变默认参数坑（不运行，口算）
```python
def f(xs=[]):
    xs.append(1); return xs
print(f()); print(f())
```
输出是什么？为什么？怎么改？

> [!tip]- 答案
> ```
> [1]
> [1, 1]
> ```
> 默认值 `[]` 在 `def` 执行时只创建一次并被所有调用共享。
> 改：`def f(xs=None): if xs is None: xs = []`。

### P3.3 ★★★ 装饰器计时
写一个 `@timer` 装饰器，打印被装饰函数的执行耗时。

> [!tip]- 答案
> ```python
> import time, functools
> def timer(fn):
>     @functools.wraps(fn)
>     def wrap(*a, **kw):
>         t = time.perf_counter()
>         r = fn(*a, **kw)
>         print(f"{fn.__name__} 耗时 {time.perf_counter() - t:.4f}s")
>         return r
>     return wrap
> ```
> 进阶要求 `functools.wraps` 保留原函数 `__name__`/`__doc__`——这是装饰器「不破坏元信息」的标配。

---

## 四·面向对象

### P4.1 ★ 二维向量类
实现 `Vector(x,y)`：支持 `+`、`==`、`abs()`、`repr()`。

> [!tip]- 答案
> ```python
> import math
> class Vector:
>     def __init__(self, x, y): self.x, self.y = x, y
>     def __repr__(self): return f"Vector({self.x}, {self.y})"
>     def __eq__(self, o): return (self.x, self.y) == (o.x, o.y)
>     def __add__(self, o): return Vector(self.x + o.x, self.y + o.y)
>     def __abs__(self): return math.hypot(self.x, self.y)
> ```

### P4.2 ★★ 学生分数校验
`Student` 的 `score` 属性必须 $0\sim100$，否则抛 `ValueError`。

> [!tip]- 答案
> ```python
> class Student:
>     def __init__(self, name, score):
>         self.name = name; self.score = score   # 走 setter
>     @property
>     def score(self): return self._score
>     @score.setter
>     def score(self, v):
>         if not 0 <= v <= 100: raise ValueError("分数须在 0~100")
>         self._score = v
> ```

### P4.3 ★★★ 银行账户 + 异常
实现 `BankAccount(owner, balance=0)`：`deposit(n)`（n>0）、`withdraw(n)`（n>0 且 ≤ 余额），余额不足抛自定义异常 `InsufficientBalance`。

> [!tip]- 答案
> ```python
> class InsufficientBalance(Exception): pass
> class BankAccount:
>     def __init__(self, owner, balance=0):
>         self.owner, self._balance = owner, balance
>     def deposit(self, n):
>         if n <= 0: raise ValueError
>         self._balance += n
>     def withdraw(self, n):
>         if n > self._balance: raise InsufficientBalance
>         self._balance -= n; return n
>     @property
>     def balance(self): return self._balance
> ```

---

## 五·文件与异常

### P5.1 ★ 读文件最大行
读取 `log.txt`（utf-8），输出最长一行的长度与内容。

> [!tip]- 答案
> ```python
> with open("log.txt", encoding="utf-8") as f:
>     longest = max(f, key=len)
> print(len(longest), longest.rstrip())
> ```

### P5.2 ★★ 安全转 int
写 `safe_int(s)`：成功返回整数，失败返回 `None`，**不**让 `KeyboardInterrupt` 等被吞掉。

> [!tip]- 答案
> ```python
> def safe_int(s):
>     try: return int(s)
>     except ValueError: return None
> ```
> 关键：只捕 `ValueError`，**别**裸 `except:`——参见 §05 异常三防。

### P5.3 ★★★ 文件词频统计
读取 `words.txt`（每行一词，utf-8），写 `freq.txt`（按出现次数降序，格式 `word count`）。要求用 `with` + `Counter` + `pathlib`。

> [!tip]- 答案
> ```python
> from pathlib import Path
> from collections import Counter
> src, dst = Path("words.txt"), Path("freq.txt")
> with src.open(encoding="utf-8") as f:
>     words = [line.strip() for line in f if line.strip()]
> cnt = Counter(words)
> with dst.open("w", encoding="utf-8") as g:
>     for w, c in cnt.most_common():
>         g.write(f"{w} {c}\n")
> ```

---

## 自测进度

- [ ] 基础语法 4 题
- [ ] 数据结构 4 题
- [ ] 函数 3 题
- [ ] 面向对象 3 题
- [ ] 文件异常 3 题

---

## Related Notes
- [[assets/LLM上下文/Python/Python入门 MOC|MOC]]