---
keywords: practice, latex
---

# LaTeX Practice (10 exercises)

#practice #latex

## Related Notes
- [[笔记/技能/LaTeX/01-基础语法/LaTeX基础|LaTeX基础]], [[笔记/技能/LaTeX/02-数学公式/数学公式速查|数学公式速查]], [[笔记/技能/LaTeX/03-表格与矩阵/表格与矩阵|表格与矩阵]], [[笔记/技能/LaTeX/06-宏包与自定义/宏包与自定义命令|宏包与自定义命令]]

---

## Exercise 1 - 基本文档 [recall]
> 写出一个完整的 LaTeX 文档骨架（documentclass、begin/end document）。

> [!answer]- 答案
> ```latex
> \documentclass{article}
> \begin{document}
> Hello World!
> \end{document}
> ```

## Exercise 2 - 行内与行间公式 [recall]
> 分别写出 $E=mc^2$ 的行内公式和行间编号公式。

> [!answer]- 答案
> 行内: `$E=mc^2$`
> 行间: `\begin{equation} E=mc^2 \end{equation}`

## Exercise 3 - 分数与根号 [recall]
> 写出 $\frac{-b\pm\sqrt{b^2-4ac}}{2a}$ 的 LaTeX 代码。

> [!answer]- 答案
> `\frac{-b \pm \sqrt{b^2-4ac}}{2a}`

## Exercise 4 - 矩阵 [recall]
> 写出一个 2×2 矩阵 $\begin{pmatrix}a&b\\c&d\end{pmatrix}$ 的代码。

> [!answer]- 答案
> ```latex
> \begin{pmatrix}
>   a & b \\
>   c & d
> \end{pmatrix}
> ```

## Exercise 5 - 自定义命令 [application]
> 定义 `\R` 为 $\mathbb{R}$，并用它写出"$x\in\mathbb{R}$"。

> [!answer]- 答案
> `\newcommand{\R}{\mathbb{R}}`
> 使用: `$x \in \R$`

## Exercise 6 - 多行对齐 [application]
> 用 align 环境写出迈耶公式的推导。

> [!answer]- 答案
> ```latex
> \begin{align}
>   c_p - c_v &= T(\partial p/\partial T)_v
>               (\partial v/\partial T)_p \\
>             &= R_g
> \end{align}
> ```

## Exercise 7 - 表格 [application]
> 用 booktabs 画一个三线表，列出三种文档类。

> [!answer]- 答案
> ```latex
> \begin{tabular}{ll}
>   \toprule
>   文档类 & 用途 \\
>   \midrule
>   article & 短文章 \\
>   report & 报告 \\
>   book & 书籍 \\
>   \bottomrule
> \end{tabular}
> ```

## Exercise 8 - 插图 [application]
> 写出插入 `figure.pdf` 并设置宽度为文本宽度80%的代码。

> [!answer]- 答案
> ```latex
> \begin{figure}[htbp]
>   \centering
>   \includegraphics[width=0.8\textwidth]{figure.pdf}
>   \caption{标题}
>   \label{fig:myfig}
> \end{figure}
> ```

## Exercise 9 - cases 环境 [application]
> 写出分段函数的 LaTeX 代码。

> [!answer]- 答案
> ```latex
> f(x) = \begin{cases}
>   0, & x < 0 \\
>   x^2, & x \ge 0
> \end{cases}
> ```

## Exercise 10 - 完整文档 [analysis]
> 写一个包含标题、章节、公式、表格、图片的完整文档骨架。

> [!answer]- 答案
> ```latex
> \documentclass{article}
> \usepackage[UTF8]{ctex}
> \usepackage{amsmath, graphicx, booktabs}
> \title{测试文档}
> \author{姓名}
> \begin{document}
> \maketitle
> \section{引言}
> 公式: \begin{equation} E=mc^2 \end{equation}
> \begin{table}[h]
>   \caption{数据表}
>   \begin{tabular}{cc} \toprule A & B \\ \midrule 1 & 2 \\ \bottomrule \end{tabular}
> \end{table}
> \end{document}
> ```
