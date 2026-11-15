# SRE 知识库

基于 **《SRE：Google 运维解密——Google 如何运行大规模生产系统（第2版）》**
（*Site Reliability Engineering: How Google Runs Production Systems, Second Edition*）
整理的深度摘要知识库网站。

## 特性

- 📚 **每章深度摘要**：6 大部分 23 章 + 7 个附录，覆盖核心概念、关键论点、实践要点
- 🗺️ **交互式脑图**：每章配 Markmap 脑图（可折叠、缩放），首页有全书知识地图
- 🔍 **全文搜索**：MkDocs Material 内置中文搜索
- 🌓 **暗色模式**：跟随系统自动切换
- 🚀 **GitHub Pages 自动部署**：push 到 main 分支即自动构建发布

## 本地预览

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve   # 浏览器打开 http://127.0.0.1:8000
```

## 目录结构

```
docs/
├── index.md            # 首页 + 全书知识地图
├── guide.md            # 导读：第2版讲了什么
├── part1/ ... part6/   # 六大部分，每章一个页面
└── appendices/         # 附录 A–G
```

## 版权说明

本站为个人学习笔记性质的知识整理。所有内容的著作权归原书作者
（Betsy Beyer, Chris Jones, Christof Leng, David Huska, Jennifer Petoff,
Niall Richard Murphy 等）与出版方（Google / O'Reilly Media 及中文译本出版方）所有。
摘要以自己的语言重述原书内容，仅少量引用原文以保留术语准确性，请勿用于商业用途。
