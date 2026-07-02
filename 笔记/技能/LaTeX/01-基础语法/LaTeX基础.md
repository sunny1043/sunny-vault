---
keywords: latex-basics, document-class, preamble, compilation, beginner
---

# LaTeX 基础 — 从零开始

#latex #basics

## 什么是 LaTeX？

**定义**: LaTeX 是一个基于 TeX 的**排版系统**，用纯文本命令描述文档结构和内容，由编译器自动生成精美的 PDF。

**物理直觉**: Word 是"所见即所得"（拖拽排版），LaTeX 是"所想即所得"（描述意图）。你告诉 LaTeX"这是标题、这是公式、这是引用"，它按学术出版标准自动排版。对于数学公式、交叉引用、参考文献管理，LaTeX 远超 Word。

## 第一个文档

```latex
\documentclass{article}        % 文档类型
\usepackage[UTF8]{ctex}       % 中文支持
\title{我的第一篇文档}
\author{你的名字}
\date{\today}

\begin{document}
\maketitle                     % 生成标题

\section{简介}
这是正文。$E=mc^2$ 是行内公式。

\begin{equation}
  E = mc^2
  \label{eq:einstein}
\end{equation}
式 (\ref{eq:einstein}) 是爱因斯坦质能方程。
\end{document}
```

## 文档结构

| 命令 | 作用 |
|------|------|
| `\documentclass{article}` | 文档类（article/report/book/beamer） |
| `\usepackage{...}` | 加载宏包 |
| `\begin{document}` / `\end{document}` | 正文环境 |
| `\section{...}` | 一级标题 |
| `\subsection{...}` | 二级标题 |

## 常用文档类

| 类 | 用途 | 特点 |
|----|------|------|
| `article` | 短文章/论文 | 无 `\chapter` |
| `report` | 报告/论文 | 有 `\chapter` |
| `book` | 书籍 | 双面排版、有 `\chapter` |
| `beamer` | 幻灯片 | 逐帧展示 |
| `ctexart` | 中文文章 | 自动处理中文字体 |

## 常用宏包

| 宏包 | 用途 |
|------|------|
| `ctex` | 中文排版 |
| `amsmath` | 数学公式增强 |
| `graphicx` | 插入图片 |
| `hyperref` | 超链接 |
| `geometry` | 页面边距 |
| `fancyhdr` | 页眉页脚 |

## 编译流程

```
.tex 源文件 → pdflatex/xelatex → .pdf 输出
```

中文推荐用 **xelatex**：`xelatex myfile.tex`

---

## Related Notes
- [[笔记/技能/LaTeX/02-数学公式/数学公式速查|数学公式速查]]
- [[笔记/技能/LaTeX/03-表格与矩阵/表格与矩阵|表格与矩阵]]
