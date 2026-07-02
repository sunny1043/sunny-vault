---
source: 综合（无单一原资料）
type: moc
subject: Python
date: 2026-07-02
keywords: [python, moc, study-map, beginner]
tags: [moc, python]
---

# Python 入门 Map

#python #moc

> 🧭 首页 [[LLM上下文/index|StudyVault]] · 相邻技能 [[LLM上下文/LaTeX/LaTeX学习 MOC|LaTeX]]
>
> 本笔记面向 **Python 3** 入门 → 为 PINN 学习筑基。覆盖语法、数据结构、函数模块、面向对象、文件与异常五条主线，并加两篇 PINN 必备进阶章（NumPy 矢量运算、PyTorch 自动微分）。所有笔记遵循 StudyVault 精读规范（五件套 + 分级叙事 + 核心理解 callout）。
> PINN 学习路径见 [[LLM上下文/PINN/PINN学习 MOC|PINN 学习 MOC]]。

## 学习路径

```
基础语法 → 数据结构 → 函数与模块 → 面向对象 → 文件与异常
 (类型/控制流)  (list/dict…)  (def/参数/import)  (类/继承/dunder)  (with/try)
                                                          │
                                            ┌─────────────┴─────────────┐
                                            ▼                           ▼
                                  06 NumPy 矢量运算              07 PyTorch autograd
                                  (画场/广播/算子)              (PINN 的核心机制)
                                                                     │
                                                                     ▼
                                                            [[LLM上下文/PINN/PINN学习 MOC|PINN 学习 MOC]]
```

## 章节导航

| # | 主题 | 笔记 | 速查 |
|---|------|------|------|
| 1 | 类型、控制流、输入输出 | [[笔记/技能/Python/01-基础语法/Python基础\|Python基础]] | [[LLM上下文/Python/Quick Reference#基础\|基础]] |
| 2 | list / tuple / dict / set | [[笔记/技能/Python/02-数据结构/数据结构\|数据结构]] | [[LLM上下文/Python/Quick Reference#数据结构\|数据结构]] |
| 3 | def、参数、lambda、模块、注解 | [[笔记/技能/Python/03-函数与模块/函数与模块\|函数与模块]] | [[LLM上下文/Python/Quick Reference#函数与模块\|函数与模块]] |
| 4 | 类、继承、dunder、property | [[笔记/技能/Python/04-面向对象/面向对象\|面向对象]] | [[LLM上下文/Python/Quick Reference#面向对象\|面向对象]] |
| 5 | 文件、with、pathlib、异常 | [[笔记/技能/Python/05-文件与异常/文件与异常\|文件与异常]] | [[LLM上下文/Python/Quick Reference#文件与异常\|文件与异常]] |
| 6 | NumPy 矢量运算 / 广播 / 画场（PINN 筑基） | [[笔记/技能/Python/06-科学计算/NumPy矢量运算\|NumPy矢量运算]] | — |
| 7 | PyTorch tensor / autograd / 训练循环（PINN 卡核心） | [[笔记/技能/Python/07-PyTorch基础/PyTorch与自动微分\|PyTorch与自动微分]] | — |

> [!tip] 衔接 PINN
> 第 6、7 章是专为 PINN 学习新增的筑基章。PINN 学习路径见 [[LLM上下文/PINN/PINN学习 MOC|PINN 学习 MOC]]——4 阶段 8~9 周从零基础走到跑通 Burgers / 方腔流 demo。

## Practice
- [[笔记/技能/Python/NN-Practice/Python_Practice|Python_Practice]]（17 题，附答案）

## 全局最高频「易错点」清单（考前扫一眼）

1. ==可变默认参数坑==：`def f(xs=[])` 跨调用共享 → 用 `None` + 惰性建。
2. ==浮点 `==` 不可靠==：用 `abs(a-b) < 1e-9`。
3. ==`b = a` 是别名不是复制==：浅拷贝 `.copy()`/`[:]`/`list()`；嵌套用 `copy.deepcopy`。
4. ==`x in list` $O(n)$、`x in set/dict` $O(1)$==：存在性判断永远用 set。
5. ==文本 IO 必加 `encoding="utf-8"`==。
6. ==所有需善后资源用 `with`==。
7. ==异常捕获点 = 处理点==：别裸 `except:`、别 `except: pass`。
8. ==每个可执行脚本加 `if __name__ == "__main__":`==。

## 推荐工具与资源
- **运行环境**：`python.org` 下载；或 `uv`（现代包管理器，秒级装 Python）
- **在线演练**：`https://www.python.org/shell/` · LeetCode（OJ 入门）
- **编辑器**：VS Code + Python 扩展 / PyCharm
- **风格指南**：PEP 8（`https://peps.python.org/pep-0008/`）；用 `ruff` / `black` 一键格式化
- **官方教程**：`https://docs.python.org/zh-cn/3/tutorial/`