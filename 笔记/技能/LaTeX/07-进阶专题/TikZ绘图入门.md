---
keywords: tikz, pgfplots, diagram, flowchart, drawing
---

# TikZ 绘图入门

#latex #tikz

## 为什么用 TikZ？

Word/PPT 画图：拖拽 → 导出图片 → 插入 LaTeX。字体不一致、修改麻烦。  
TikZ：**代码描述图形** → 编译时直接嵌入 PDF。字体完美匹配，可精确控制。

## 基本语法

```latex
\usepackage{tikz}
\begin{tikzpicture}
  \draw (0,0) -- (2,0) -- (2,2) -- cycle;  % 三角形
  \draw[->, red, thick] (0,0) -- (3,3);     % 红色箭头
  \node at (1.5,1.5) {文本};               % 放置文字
  \fill[blue!20] (0,0) circle (1);         % 蓝色半透明圆
\end{tikzpicture}
```

## 常用路径与样式

| 操作 | 语法 |
|------|------|
| 直线 | `(0,0) -- (2,0)` |
| 曲线 | `(0,0) .. controls (1,1) .. (2,0)` |
| 矩形 | `(0,0) rectangle (2,1)` |
| 圆 | `(1,1) circle (0.5)` |
| 椭圆 | `(1,1) ellipse (2 and 1)` |
| 圆弧 | `(0,0) arc (0:90:1)` |

## 函数绘图 — pgfplots

```latex
\usepackage{pgfplots}
\begin{tikzpicture}
  \begin{axis}[
    xlabel=$x$, ylabel=$f(x)$,
    grid=major, domain=-2:2
  ]
    \addplot[blue, thick] {x^2};
    \addplot[red, dashed] {x^3};
    \addlegendentry{$x^2$}
    \addlegendentry{$x^3$}
  \end{axis}
\end{tikzpicture}
```

## 流程图

```latex
\tikzstyle{block} = [rectangle, draw, text width=5em, text centered, minimum height=3em]
\tikzstyle{arrow} = [thick,->,>=stealth]

\begin{tikzpicture}[node distance=2cm]
  \node [block] (start) {开始};
  \node [block, below of=start] (process) {处理};
  \node [block, below of=process] (end) {结束};
  \draw [arrow] (start) -- (process);
  \draw [arrow] (process) -- (end);
\end{tikzpicture}
```

## 热力学常用图（p-v, T-s）

```latex
\begin{tikzpicture}
  \draw[->] (0,0) -- (4,0) node[right] {$v$};
  \draw[->] (0,0) -- (0,4) node[above] {$p$};
  \draw[blue, thick] 
    (0.5,3.5) .. controls (2,2) .. (3.5,0.5);
  \node[blue] at (3,2.5) {$pv^n=C$};
\end{tikzpicture}
```

---

## Related Notes
- [[笔记/技能/LaTeX/04-浮动体与图形/浮动体与图形|浮动体与图形]]
