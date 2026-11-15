---
title: 首页
---

# SRE 知识库

> 深度摘要知识库，基于 **《SRE：Google 运维解密——Google 如何运行大规模生产系统（第2版）》**
> （*Site Reliability Engineering: How Google Runs Production Systems, Second Edition*）整理。
> 主编：Betsy Beyer, Chris Jones, Christof Leng, David Huska, Jennifer Petoff, Niall Richard Murphy。

## 这是什么

本站将全书 6 大部分 23 章 + 7 个附录提炼为**每章深度摘要**：核心概念、关键论点、实践要点。

- 📖 想系统学习：从 [第Ⅰ部分 背景与脉络](part1/index.md) 开始按序阅读
- ⚡ 想快速查阅：直接在右上角搜索框检索概念（如「错误预算」「SLO」「STPA」）
- 🌌 想纵览全局：探索下面的**全书知识星系**

---

## 全书知识星系

<div id="book-map" style="height:820px;"></div>

<p style="text-align:center;font-size:0.78em;color:var(--md-default-fg-color--light)">
星球大小 = 章节篇幅 · 颜色 = 所属部分 · <b>虚线 = 书中交叉引用</b> · 悬停查看章节摘要 · 点击星球直达对应章节
</p>

<script src="js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('book-map');
  if (!el || typeof echarts === 'undefined') return;

  // 固定尺寸：按加载时视口宽度确定，之后不随窗口缩放重排
  var FIXED_W = Math.min(Math.round(window.innerWidth * 0.96), 1840);
  el.style.width = FIXED_W + 'px';
  el.style.marginLeft = 'calc(50% - ' + (FIXED_W / 2) + 'px)';

  var CATS = [
    { name: 'Ⅰ 背景与脉络',   color: '#ef5350', link: 'part1/index/' },
    { name: 'Ⅱ 社会技术基石', color: '#ab47bc', link: 'part2/index/' },
    { name: 'Ⅲ 态势感知与备战', color: '#29b6f6', link: 'part3/index/' },
    { name: 'Ⅳ 基础设施设计',  color: '#66bb6a', link: 'part4/index/' },
    { name: 'Ⅴ 韧性与平台',   color: '#ffa726', link: 'part5/index/' },
    { name: 'Ⅵ 展望',        color: '#ec407a', link: 'part6/index/' },
    { name: 'Ⅶ 附录',        color: '#78909c', link: 'appendices/index/' }
  ];

  function N(cat, name, pages, desc, link) {
    return { name: name, category: cat, symbolSize: Math.round(16 + pages * 1.1), desc: desc, link: link };
  }

  var chapters = [
    N(0, 'Ch1 绪论', 11, 'SRE 工作模型与现代生产健康层级模型，全书路线图', 'part1/ch01/'),
    N(0, 'Ch2 可靠性的商业价值', 13, 'SRE 的投资回报与系统不可靠的代价', 'part1/ch02/'),
    N(0, 'Ch3 生产环境的演进趋势', 10, '云计算、平台化与 AI 基础设施的演进', 'part1/ch03/'),
    N(1, 'Ch4 文化土壤', 24, '心理安全感与生机型文化，DORA 实证研究', 'part2/ch04/'),
    N(1, 'Ch5 招聘与职业发展', 26, 'SRE 特质、培训体系与 IC 成长路径', 'part2/ch05/'),
    N(1, 'Ch6 组织架构', 20, '集中式 vs 分散式、成熟度矩阵与记分卡', 'part2/ch06/'),
    N(1, 'Ch7 协作模式', 29, '七种协作范围与 Google/微软/迪士尼案例', 'part2/ch07/'),
    N(2, 'Ch8 SLO', 20, '错误预算与关键用户旅程，SLO 驱动运维', 'part3/ch08/'),
    N(2, 'Ch9 可观测性与监控', 39, '高可用遥测、OpenTelemetry 与客户端监控', 'part3/ch09/'),
    N(2, 'Ch10 应急与轮值', 25, 'IRT、事故生命周期与 Etsy 案例研究', 'part3/ch10/'),
    N(2, 'Ch11 从事故中学习', 13, '无指责复盘与安全科学，巴黎数据中心案例', 'part3/ch11/'),
    N(2, 'Ch12 STPA 与 CAST', 32, '系统论安全工程：前瞻危险分析与事故分析', 'part3/ch12/'),
    N(3, 'Ch13 自动化与工具', 21, '自动化层级、琐事管理与自动化决策框架', 'part4/ch13/'),
    N(3, 'Ch14 测试', 34, '金丝雀、故障注入、形式化方法与 Agent 测试', 'part4/ch14/'),
    N(3, 'Ch15 容量规划', 28, '需求预测、资源池化与 Meet/TPU 案例', 'part4/ch15/'),
    N(3, 'Ch16 数据管理', 29, 'RPO/RTO、复制拓扑与备份恢复策略', 'part4/ch16/'),
    N(4, 'Ch17 韧性系统设计', 42, '故障域、过载管理、紧急模式与数据韧性', 'part5/ch17/'),
    N(4, 'Ch18 平台工程', 15, '平台即花园：黄金路径、护栏与生态系统', 'part5/ch18/'),
    N(5, 'Ch19 转折点上的 SRE', 7, 'AI 压缩 SDLC 对生产运维的十大冲击', 'part6/ch19/'),
    N(5, 'Ch20 SRE 赋能 AI', 24, 'AI 工作负载的 SLO、容量与准入认证', 'part6/ch20/'),
    N(5, 'Ch21 AI 赋能 SRE', 21, '从指标到意义，通往自治之路（L0–L4）', 'part6/ch21/'),
    N(5, 'Ch22 多样化环境实践', 21, '光杆司令、遗留系统与 Waymo 危机管理', 'part6/ch22/'),
    N(5, 'Ch23 SRE 的未来', 4, '左移变下移，风险作为可靠性先行指标', 'part6/ch23/'),
    N(6, '附录A 培训 ROI', 2, '培训投入的投资回报率计算', 'appendices/appendix-a/'),
    N(6, '附录B 章程模板', 2, 'SRE 团队章程可复用模板', 'appendices/appendix-b/'),
    N(6, '附录C 会议纪要', 2, '生产会议纪要示例结构', 'appendices/appendix-c/'),
    N(6, '附录D gShoe 章程', 2, '虚构团队 gShoe SRE 章程示例', 'appendices/appendix-d/'),
    N(6, '附录E 组合 SLO 数学', 2, '串行/并行对冲下的组合 SLO 计算', 'appendices/appendix-e/'),
    N(6, '附录F 延迟告警数学', 2, '延迟 SLI 告警的统计学基础', 'appendices/appendix-f/'),
    N(6, '附录G 可观测性统计', 2, '错误率统计与机器学习应用', 'appendices/appendix-g/')
  ];

  // 确定性坐标：7 列星座布局，按容器宽高写死，天然铺满、不随缩放变化
  var W = FIXED_W, H = 820;
  var colW = W / CATS.length;
  var ROOT_Y = H * 0.11, HUB_Y = H * 0.52;
  var pos = { 'SRE 第2版': [W * 0.5, ROOT_Y] };
  CATS.forEach(function (c, i) {
    pos[c.name] = [colW * (i + 0.5), HUB_Y + Math.sin(i * 2.1) * 26];
  });
  var counts = {}, idx = {};
  chapters.forEach(function (n) { counts[n.category] = (counts[n.category] || 0) + 1; });
  var STEP = 82;
  chapters.forEach(function (n) {
    var ci = n.category;
    idx[ci] = idx[ci] || 0;
    var j = idx[ci];
    var side = (j % 2 === 0) ? -1 : 1;
    var k = Math.floor(j / 2) + 1;
    var hubX = pos[CATS[ci].name][0];
    var hubY = pos[CATS[ci].name][1];
    var x = hubX + Math.sin(j * 13.7 + ci * 3.1) * 30;
    var y = hubY + side * (k * STEP + 18);
    pos[n.name] = [
      Math.max(80, Math.min(W - 80, x)),
      Math.max(60, Math.min(H - 60, y))
    ];
    idx[ci]++;
  });

  var nodes = [{
    name: 'SRE 第2版', symbolSize: 40, itemStyle: { color: '#d32f2f' },
    x: pos['SRE 第2版'][0], y: pos['SRE 第2版'][1],
    desc: '全书知识星系：点击部分星团查看，点击章节星球直达页面',
    label: { show: true, fontWeight: 'bold', fontSize: 14 }
  }];
  var links = [];
  CATS.forEach(function (c, i) {
    var hub = {
      name: c.name, category: i, symbolSize: 26, link: c.link,
      x: pos[c.name][0], y: pos[c.name][1],
      desc: '点击进入本部分导读',
      label: { show: true, fontWeight: 'bold', fontSize: 13 }
    };
    nodes.push(hub);
    links.push({ source: 'SRE 第2版', target: c.name, lineStyle: { color: c.color, opacity: 0.5, width: 1.8 } });
  });
  chapters.forEach(function (n) {
    n.x = pos[n.name][0];
    n.y = pos[n.name][1];
    nodes.push(n);
    links.push({ source: CATS[n.category].name, target: n.name, lineStyle: { color: CATS[n.category].color, opacity: 0.45, width: 1.4 } });
  });

  // 书中交叉引用 → 星座连线
  var CROSS = [
    ['Ch1 绪论', 'Ch2 可靠性的商业价值'],
    ['Ch1 绪论', 'Ch17 韧性系统设计'],
    ['Ch3 生产环境的演进趋势', 'Ch20 SRE 赋能 AI'],
    ['Ch4 文化土壤', 'Ch5 招聘与职业发展'],
    ['Ch4 文化土壤', 'Ch11 从事故中学习'],
    ['Ch5 招聘与职业发展', '附录A 培训 ROI'],
    ['Ch6 组织架构', 'Ch7 协作模式'],
    ['Ch7 协作模式', 'Ch22 多样化环境实践'],
    ['Ch8 SLO', 'Ch9 可观测性与监控'],
    ['Ch8 SLO', 'Ch10 应急与轮值'],
    ['Ch8 SLO', '附录E 组合 SLO 数学'],
    ['Ch9 可观测性与监控', '附录F 延迟告警数学'],
    ['Ch9 可观测性与监控', '附录G 可观测性统计'],
    ['Ch9 可观测性与监控', 'Ch21 AI 赋能 SRE'],
    ['Ch10 应急与轮值', 'Ch11 从事故中学习'],
    ['Ch10 应急与轮值', 'Ch21 AI 赋能 SRE'],
    ['Ch10 应急与轮值', 'Ch22 多样化环境实践'],
    ['Ch11 从事故中学习', 'Ch12 STPA 与 CAST'],
    ['Ch12 STPA 与 CAST', 'Ch21 AI 赋能 SRE'],
    ['Ch13 自动化与工具', 'Ch5 招聘与职业发展'],
    ['Ch14 测试', 'Ch17 韧性系统设计'],
    ['Ch15 容量规划', 'Ch17 韧性系统设计'],
    ['Ch15 容量规划', 'Ch20 SRE 赋能 AI'],
    ['Ch16 数据管理', 'Ch17 韧性系统设计'],
    ['Ch17 韧性系统设计', 'Ch18 平台工程'],
    ['Ch18 平台工程', 'Ch23 SRE 的未来'],
    ['Ch19 转折点上的 SRE', 'Ch21 AI 赋能 SRE'],
    ['Ch20 SRE 赋能 AI', 'Ch21 AI 赋能 SRE'],
    ['附录B 章程模板', '附录D gShoe 章程']
  ];
  CROSS.forEach(function (pair) {
    links.push({
      source: pair[0], target: pair[1],
      lineStyle: { type: 'dashed', width: 1, opacity: 0.4, curveness: 0.12 }
    });
  });

  function fg() {
    var v = getComputedStyle(document.body).getPropertyValue('--md-default-fg-color').trim();
    return v || 'rgba(0,0,0,0.87)';
  }
  function fgDim() {
    var v = getComputedStyle(document.body).getPropertyValue('--md-default-fg-color--light').trim();
    return v || 'rgba(0,0,0,0.55)';
  }

  var chart = echarts.init(el);

  function render() {
    chart.setOption({
      animation: false,
      backgroundColor: 'transparent',
      color: CATS.map(function (c) { return c.color; }),
      legend: {
        data: CATS.map(function (c) { return c.name; }),
        textStyle: { color: fg(), fontSize: 11 },
        icon: 'circle',
        itemWidth: 10, itemHeight: 10,
        top: 4
      },
      tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove',
        backgroundColor: 'rgba(80,80,80,0.92)',
        borderWidth: 0,
        textStyle: { color: '#fff', fontSize: 12 },
        formatter: function (p) {
          return p.data && p.data.desc ? '<b>' + p.name + '</b><br/>' + p.data.desc : p.name;
        }
      },
      series: [{
        type: 'graph',
        layout: 'none',
        roam: false,
        data: nodes,
        links: links,
        categories: CATS.map(function (c) { return { name: c.name }; }),
        emphasis: { focus: 'adjacency', lineStyle: { width: 2.5 } },
        lineStyle: { color: 'source', opacity: 0.45 },
        label: {
          show: true, color: fg(), fontSize: 12, position: 'right', distance: 6
        },
        labelLayout: { hideOverlap: true }
      }]
    });
  }

  render();
  new MutationObserver(render).observe(document.body, { attributes: true, attributeFilter: ['data-md-color-scheme'] });
  chart.on('click', function (p) {
    if (p.data && p.data.link) window.location.href = p.data.link;
  });
})();
</script>

## 本书核心思想一页纸

1. **可靠性是第一位的功能特性**：系统不可靠，其他一切功能都失去意义。
2. **用软件工程方法解决运维问题**：SRE 是"当运维任务可以用软件工程方法解决时，它就是编程问题"的实践。
3. **错误预算（Error Budget）**：100% 可靠性是错误的目标——错误预算量化"合理故障额度"，平衡可靠性与迭代速度。
4. **SLO 驱动一切**：以用户旅程（CUJ）为中心定义 SLI/SLO，用数据决定工程投入。
5. **琐事（Toil）是敌人**：运维琐事占比超过 50% 会侵蚀团队；自动化不是目的，而是管理琐事的手段。
6. **事故是学习机会**：无指责的事后总结（Blameless Postmortem）文化，从系统性视角理解故障。
7. **SRE 是社会技术（Sociotechnical）学科**：文化、组织、协作模式与技术实践同等重要（第2版核心主题）。
8. **AI 正在重塑 SRE**：SRE 赋能 AI 工作负载，AI 也反过来赋能 SRE，走向"涌现式可靠性"。

## 推荐阅读路径

| 读者 | 建议路径 |
|---|---|
| SRE 新人 | 序言前言 → 第1章 → 第3章 → 第Ⅰ~Ⅳ部分按序 → 第8/10/11章精读 |
| 一线工程师 | 第8章 SLO → 第9章 监控 → 第10章 应急 → 第11章 复盘 → 第13/14章 → 第17章 |
| 技术管理者 | 第1章 → 第2章 → 第4~7章（文化/组织/协作）→ 第19/21/23章（AI 与未来） |
| AI 平台团队 | 第15章 容量 → 第20章 SRE 赋能 AI → 第21章 AI 赋能 SRE |

---

*本站为个人学习笔记性质的知识整理，所有内容的著作权归原书作者与出版方所有。摘要以自己的语言重述，仅少量引用原文以保留术语准确性。*
