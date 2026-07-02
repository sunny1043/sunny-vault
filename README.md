# StudyVault

> Sunny 的理工科备考知识库（Obsidian vault + Quartz 5 静态站点）。
> 服务于「学懂 + 应试」，不是通用 PKM。

## 这是什么

一个 Obsidian 笔记库，组织成「学科 → 章节 → 精读笔记」三级结构，每篇精读笔记按
**Sunny 五件套**（定义 / 性质 / 公式推导 / 图 / 物理数学核心）展开。仓库内还带一个
Quartz 5 子目录把 vault 渲染成静态 HTML 经 GitHub Pages 公开发布。

## 仓库结构

```
StudyVaults/
├── 线性代数/ LaTeX/ 工程热力学/ 流体传动与控制/   # 学科笔记
├── AL-31F_压气机/                                  # 冻结区，不动
├── attachments/                                    # 图片附件
├── _templates/                                     # Obsidian 模板
├── _skills/                                        # study-note-organizer skill
├── _scripts/                                        # 善后脚本
├── quartz/                                          # Quartz 5 发布器
├── .github/workflows/deploy.yml                     # GitHub Pages 自动部署
├── AGENTS.md                                        # 框架无关整理总纲（必读）
├── _CLAUDE.md                                       # Claude 专用操作手册
└── index.md                                         # 站点首页
```

## 整理规则（任何 LLM 进仓库都读这份）

见 [`AGENTS.md`](./AGENTS.md) ——它从 `_CLAUDE.md` + `study-note-organizer` skill
+ 风格指南抽象而成，框架无关。包含：黄金目录结构、命名约定、统一 frontmatter
schema、整理工作流、精读五件套模板、分级叙事 + 2 空格缩进硬规则（关乎 `$$` 公式能
否在 Obsidian 渲染）、13 条自检清单、补充标注铁律、自动化权限、Quartz 发布说明、
换机初始化清单。

## 本地预览静态站点

```bash
cd quartz
npm ci
npx quartz plugin install      # 拉社区插件；网络抖动可重试（幂等）
npx quartz build -d .. -v --serve
# → http://localhost:8080
```

## 首次部署 GitHub Pages（仓库 owner 一次性配置）

仓库 Settings → Pages → Build and deployment → Source 选 **GitHub Actions**。
之后 push 到 `main` 即自动重建发布到 `https://sunny1043.github.io/sunny-vault/`。

## 多设备互通

- 站点访问：所有设备打开 `https://sunny1043.github.io/sunny-vault/` 即可只读浏览。
- 编辑同步：clone 本仓库，用 Obsidian 打开根目录作为 vault。git push → CI 重建 →
  站点同步更新。

## 详细配置说明

- Quartz 配置：[`quartz/quartz.config.yaml`](./quartz/quartz.config.yaml) +
  [`quartz/README.md`](./quartz/README.md)
- 模板：[`_templates/README.md`](./_templates/README.md)
- skill：[`_skills/study-note-organizer-skill/README.md`](./_skills/study-note-organizer-skill/README.md)