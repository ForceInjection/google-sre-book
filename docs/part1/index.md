---
title: 第Ⅰ部分 · 背景与脉络
---

# 第Ⅰ部分 · 背景与脉络

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅰ部分 · 背景与脉络（第1~3章）

在深入任何具体方法论之前，本部分先回答三个地基性问题：**SRE 到底是一份什么样的工作？它凭什么值得组织投入真金白银？我们运行服务的生产环境正在发生什么变化？**这三个问题分别对应本书的立场、价值论证与时代语境——后续五个板块的所有实践，都建立在这层语境之上。

三章层层递进：第1章拆解 Site / Reliability / Engineering 三个词，并给出全书的知识框架——"现代生产健康层级模型"；第2章面向管理层与 CFO，把可靠性从技术话题翻译成商业语言，说明 SRE 是一项可量化的投资而非成本中心；第3章用十年行业演进的视角（云计算、平台化、可观测性、AI 基础设施），解释为什么第2版的方法论与十年前不同。

原书建议所有读者至少先读第1章、第2章和第4章——也就是说，本部分是全书公认的起点：无论你是工程师还是管理者，先把这三章读完，再按需跳转到后续板块。

## 各章导航

| 章 | 标题 | 一句话概括 | 链接 |
|---|---|---|---|
| 第1章 | 绪论：SRE 的工作模型与核心理念 | 拆解 Site / Reliability / Engineering 三个词的内涵——为什么做（保障业务）、做什么（可靠性）、怎么做（工程化），并以升级版"现代生产健康层级模型"给出全书的知识框架 | [ch01](ch01.md) |
| 第2章 | 可靠性的商业价值 | 把 SRE 当作可量化的商业投资：价值惠及客户、CFO、内部团队、文化与增长；而不可靠的代价远超想象 | [ch02](ch02.md) |
| 第3章 | 生产环境的演进趋势 | 2016→2026 十年范式迁移：容量管理 2.0、托管服务、共享状态、自助平台、基于意图的协调，以 Google 自身演化作案例验证 | [ch03](ch03.md) |

## 本部分脑图

<div id="map-part1-index-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-part1-index-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"第Ⅰ部分 · 背景与脉络","symbolSize":13,"children":[{"name":"Ch1 绪论","symbolSize":8,"children":[{"name":"SRE 三词拆解","symbolSize":5},{"name":"现代生产健康层级","symbolSize":5},{"name":"软件工程方法优势","symbolSize":5}]},{"name":"Ch2 商业价值","symbolSize":8,"children":[{"name":"六类相关者的价值","symbolSize":5},{"name":"不可靠的多重代价","symbolSize":5},{"name":"初创与成熟模式","symbolSize":5}]},{"name":"Ch3 演进趋势","symbolSize":8,"children":[{"name":"云计算与 FinOps","symbolSize":5},{"name":"平台与黄金路径","symbolSize":5},{"name":"从组件到上下文","symbolSize":5}]}]};
  var COLOR = '#ef5350';
  function fg() {
    var v = getComputedStyle(document.body).getPropertyValue('--md-default-fg-color').trim();
    return v || 'rgba(0,0,0,0.87)';
  }

  // 容器高度随展开状态自适应：可见行数 x 行高
  var ROW = 30, PAD = 46;
  function markInitial(node, depth) {
    if (depth >= 2) node.__collapsed = true;
    if (node.children) node.children.forEach(function (c) { markInitial(c, depth + 1); });
  }
  markInitial(data, 0);
  function visibleRows(node) {
    if (!node.children || !node.children.length || node.__collapsed) return 1;
    var s = 0;
    for (var i = 0; i < node.children.length; i++) s += visibleRows(node.children[i]);
    return s;
  }
  function fit() {
    var h = Math.max(160, visibleRows(data) * ROW + PAD);
    if (Math.abs(parseFloat(el.style.height) - h) > 1) {
      el.style.height = h + 'px';
      chart.resize();
    }
  }

  var chart = echarts.init(el);
  function render() {
    chart.setOption({
      backgroundColor: 'transparent',
      animation: true,
      animationDurationUpdate: 220,
      animationEasingUpdate: 'cubicOut',
      series: [{
        type: 'tree',
        data: [data],
        layout: 'orthogonal',
        orient: 'LR',
        roam: false,
        expandAndCollapse: true,
        initialTreeDepth: 1,
        symbol: 'circle',
        lineStyle: { width: 1.2, color: COLOR, opacity: 0.55 },
        itemStyle: { color: COLOR, borderColor: 'transparent' },
        emphasis: { focus: 'descendant', lineStyle: { width: 2.2 } },
        label: { color: fg(), fontSize: 12, position: 'right', distance: 6 },
        right: '22%'
      }]
    });
    fit();
  }
  render();
  chart.on('click', function (p) {
    var d = p.data;
    if (d && d.children && d.children.length) d.__collapsed = !d.__collapsed;
    setTimeout(fit, 300);
  });
  chart.on('finished', fit);
  new MutationObserver(render).observe(document.body, { attributes: true, attributeFilter: ['data-md-color-scheme'] });
})();
</script>

## 延伸阅读

- 全书总导读 → [导读 · 第2版讲了什么](../guide.md)
- 下一站：文化与人才如何支撑可靠性 → [第Ⅱ部分 · 社会技术基石](../part2/index.md)
