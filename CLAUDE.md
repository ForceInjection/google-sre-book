# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目是什么

《SRE：Google 运维解密（第2版）》中文知识库网站——基于 MkDocs Material 的纯静态站点。
内容为全书 23 章 + 7 附录的**深度摘要**（用自己的语言重述，非原文抄录），每章含核心概念表、
关键论点、案例研究、实践要点清单。首页是 ECharts「知识星系」力导向图，章节页配简化横向树图。

- 仓库：`ForceInjection/google-sre-book`，站点：https://forceinjection.github.io/google-sre-book/
- 部署：push 到 `main` 触发 `.github/workflows/deploy.yml`（`mkdocs gh-deploy` 推 `gh-pages` 分支）
- 源 PDF 在仓库外的上级目录（`../SRE_Book_2e_ZH.pdf` 主资料、`../*2016*.pdf` 英文第1版对照），已 gitignore

## 常用命令

Python venv 在**上级目录**（`/Users/wangtianqing/Project/wechat/sre/.venv`），不在仓库内：

```bash
# 构建（--strict 让 warning 变 error，改完内容必须用它验证）
/Users/wangtianqing/Project/wechat/sre/.venv/bin/mkdocs build --strict

# 本地预览 http://127.0.0.1:8000
/Users/wangtianqing/Project/wechat/sre/.venv/bin/mkdocs serve

# 站内链接检查（构建后在 site/ 里跑）
python3 -I - <<'EOF'
import re, pathlib
bad = []
for html in pathlib.Path("site").rglob("index.html"):
    if "404" in str(html.parent): continue
    for href in re.findall(r'href="([^"#][^"]*)"', html.read_text(errors="ignore")):
        if href.startswith(("http","mailto:","data:")) or href.endswith((".css",".js",".png",".svg",".ico",".woff2")): continue
        t = (html.parent / href.split("#")[0]).resolve()
        if href.split("#")[0] and not t.exists(): bad.append((str(html.parent), href))
print(len(bad), "broken:", *sorted(set(bad))[:10], sep="\n")
EOF
```

注意：`mkdocs build` 必须在仓库根目录跑（`docs/` 子目录下找不到 mkdocs.yml 会静默用错误配置或报错）。

## 架构与关键约定

### 页面结构（每章 `docs/partN/chNN.md` 统一模板）

frontmatter `title` → `# 章标题` → `[!INFO] 出处` 块（撰稿/合著作者名）→ **一句话概括** →
`## 本章脑图`（内联 ECharts 横向树脚本）→ `## 核心概念` 表（概念 | 术语（EN）| 说明）→
`## 关键论点`（编号列表）→ 案例研究独立小节 → `## 实践要点`（checkbox）→ `## 交叉引用`（站内相对链接）。

各部分导航：`docs/part1/`~`part6/` + `docs/appendices/`，每目录一个 `index.md` 部分导读页；
`mkdocs.yml` 的 `nav:` 手工维护全部路径，新增页面必须同步 nav。

### 图表实现（重要）

- **全部图表是内联 `<script>` + 自托管 `docs/js/echarts.min.js`**，无构建期插件、无运行时 CDN。
- **echarts.min.js 的相对路径深度容易错**：MkDocs 目录式 URL 下 `docs/part3/ch08.md` 构建为
  `/part3/ch08/`（两级目录），要用 `../../js/`；根级页面（`guide.md`→`/guide/`）用 `../js/`；
  仅首页 `index.md` 用 `js/`。改页面位置时必查。
- 图表文字颜色必须动态读取 Material CSS 变量（`getComputedStyle(document.body).getPropertyValue('--md-default-fg-color')`），
  并用 `MutationObserver` 监听 `document.body` 的 `data-md-color-scheme` 属性变化后 `setOption` 重渲染，
  否则暗色模式下文字不可读。
- `scripts/convert_maps.py` 是历史转换脚本（旧 markmap 大纲 → 内联 ECharts 树），幂等，可作参考但 markmap 已废弃。

### 版本约束（勿随意升级）

`requirements.txt` 固定 `mkdocs-material 9.6.x + pymdown-extensions 10.x`：pymdown-extensions ≥11
与 Material 9.6 组合会破坏构建（历史上还与已移除的 mkdocs-markmap 不兼容）。升级前先本地 `--strict` 构建验证。

### 内容与版权规则

- 章节内容必须是**自己的语言重述**，禁止整段照抄原书译文；至多一句短引用。PDF 书签页码与正文可能有 ±1 漂移，引用位置需实测确认。
- 首页星系图的节点数据（章节摘要一句话、页数大小、交叉引用连线）内联在 `docs/index.md` 的 `<script>` 里，
  改章节标题/链接后要同步更新星系数据、对应章节页的脑图数据和 `mkdocs.yml` nav 三处。

### Git 约定

- 提交信息**不加** `Co-Authored-By` 署名行（用户明确要求）。
- 仓库级 git 身份已配置：`grissomsh <wang.tianqing.cn@gmail.com>`。
