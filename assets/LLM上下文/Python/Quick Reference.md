---
source: 综合（自各章节提炼的速查卡）
type: quick-ref
subject: Python
date: 2026-07-02
keywords: [python, quick-ref, cheatsheet]
tags: [quick-ref, python]
---

# Python 入门速查卡

#python #quick-ref

> 浓缩自五篇章节笔记，考前一页通览。详细推理见各章。

## 基础

```python
# 类型
int / float / bool / str / None
type(x)              # 查类型
isinstance(x, int)  # 推荐写法
bool(0 / 0.0 / "" / [] / {} / None)  → False

# f-string
f"{x:.2f}"   f"{n:>5}"   f"{n:,}"   f"{x:0>5}"

# 控制流
if ... elif ... else
for x in iter: ...        # 含 for...else（else=没被break）
while cond: ...
break / continue

# range
range(5) | range(2,6) | range(0,10,2)   # 起:止(不含):步长
```

- 假值集合：`0 0.0 "" [] {} None`；`bool` 是 `int` 子类 → `True+True==2`
- 短路返回默认值：`name = input() or "匿名"`
- ==浮点别用 `==`，用 `abs(a-b) < 1e-9`==

## 数据结构

| 类型 | 字面量 | 可变 | 有序 | 重复 |
|---|---|:-:|:-:|:-:|
| list | `[1,2]` | ✅ | ✅ | ✅ |
| tuple | `(1,2)` | ❌ | ✅ | ✅ |
| dict | `{"a":1}` | ✅ | ✅ | 键唯一 |
| set | `{1,2}` | ✅ | ❌ | ❌ |

```python
# list
a.append(x)  a.insert(i,x)  a.extend(b)   # 增
a.pop()  a.pop(0)  a.remove(x)  del a[i]  # 删（pop(0)/insert(0) O(n)）
a[i]=v   a.index(x)  a.count(x)
a[1:4]  a[::-1]                 # 切片
b = a.copy()  | a[:]  | list(a) # 浅拷贝；嵌套 copy.deepcopy

# dict
d[k]=v   d.get(k,默认)   del d[k]   k in d
for k,v in d.items(): ...
{**a, **b}   # 3.9+: a | b   合并
from collections import defaultdict, Counter
Counter(s).most_common()

# set
&  交   |  并   -  差   ^  对称差
x in s   # O(1)——比 list 快几个数量级
```

- ==复制 ≠ 别名==：`b=a` 是别名；嵌套用 `copy.deepcopy`。
- 头部频繁插删用 `collections.deque`。
- 计数用 `Counter`，别自己写循环。
- 推导式：`[f(x) for x in xs if c(x)]` / `{k:v for ...}`。

## 函数与模块

```python
def f(a, b=1, *args, key=None, **kwargs): ...
return a, b                    # 返回元组

# 高阶
sorted(xs, key=lambda x: x.score)
map(f, xs)   filter(pred, xs)  # 优先用推导式

# 作用域 LEGB：Local → Enclosing → Global → Built-in
global x       # 改全局
nonlocal x     # 改外层函数变量（少用）

# import
import m   |   import m as a   |   from m import x
if __name__ == "__main__": main()

# 类型注解（运行不强制，IDE/mypy 用）
def avg(xs: list[float]) -> float: ...
from typing import List, Dict, Optional
```

- ==可变默认参数坑==：`def f(xs=[])` ❌ → `def f(xs=None):`
- 参数顺序铁律：`pos → normal → *args → kw_only → **kwargs`
- ==每个脚本加 `if __name__ == "__main__":`==

## 面向对象

```python
class C:
    class_attr = "共享"            # 类属性
    def __init__(self, x): self.x = x   # 构造
    def method(self): ...                # 实例方法
    @classmethod
    def cm(cls): ...                    # cls（常用作备选构造）
    @staticmethod
    def sm(x): return x*2
    @property
    def x(self): return self._x
    @x.setter
    def x(self, v): self._x = v

class Sub(C): ...           # 继承
    def __init__(self, x, y):
        super().__init__(x); self.y = y
Sub.__mro__                 # 多继承查找顺序
```

| dunder | 触发 |
|---|---|
| `__init__` | 构造 |
| `__repr__` / `__str__` | 调试 / 打印 |
| `__eq__` `__lt__` | 比较 |
| `__len__` `__getitem__` `__iter__` | 容器协议 |
| `__enter__` / `__exit__` | `with` 上下文 |

- ==「协议而非继承」==（鸭子类型）：实现对应方法即可被认同，不必继承基类。
- 私有用 `_name` 约定即可，**别用 `__name`**（会名称改写）。
- 多继承优先换成「单继承 + 组合」。

## 文件与异常

```python
# 文本 IO
with open("f.txt", "r", encoding="utf-8") as f:
    for line in f: ...          # 逐行最省内存
text = f.read()                 # 一次读，仅小文件
f.readlines()                   # 字符串列表

# pathlib（新代码首选）
from pathlib import Path
p = Path(".") / "x.txt"
p.exists()  p.read_text(encoding="utf-8")
list(Path(".").glob("*.py"))
```

| 模式 | 含义 |
|---|---|
| `r` 读 / `w` 写覆盖 / `a` 追加 / `x` 排他创建 |
| 加 `b` = 二进制；默认文本 |

```python
# 异常
try: ...
except ValueError as e: ...        # 捕具体类型
except (TypeError, KeyError): ...
else: ...        # try 成功才走
finally: ...     # 必善后（关资源）

raise ValueError("原因")
class MyError(Exception): pass     # 自定义继承 Exception
```

- ==文本 IO 必加 `encoding="utf-8"`==，否则跨平台中文乱码。
- ==所有需善后资源用 `with`==。
- ==异常三防==：别裸 `except:` · 别 `except: pass` · 别捕不处理的异常。
- ==捕获点 = 处理点==：处理不了就让它冒泡。
- 根在 `BaseException`，但**自定义异常继承 `Exception`**。

## 常见异常速查

| 异常 | 触发 |
|---|---|
| ValueError | 值型对但取值非法（`int("abc")`） |
| TypeError | 类型不匹配 |
| IndexError / KeyError | 下标 / 键越界 |
| AttributeError | 无该属性 |
| FileNotFoundError | 文件不存在 |
| ZeroDivisionError | 除零 |
| StopIteration | 迭代器耗尽 |
| ImportError / ModuleNotFoundError | 导入失败 |