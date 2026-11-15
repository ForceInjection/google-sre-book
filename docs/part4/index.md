---
title: 第Ⅳ部分 · 基础设施设计
---

# 第Ⅳ部分 · 基础设施设计

在[第1章](../part1/ch01.md)的现代生产健康层级模型中，"基础设施设计"位于常态化备战之上：态势感知与应急备战让你"看得见、扛得住"故障，本部分则回答一个更前置的问题——**如何在设计与建造阶段就让故障更少发生**。可靠性不是靠值班熬出来的，而是被"设计进"基础设施里的。

本部分围绕四大工程支柱展开。**自动化**（第13章）把人从重复劳动中解放出来，用一致性与可扩展性替代手工操作；**测试**（第14章）在软件生命周期的各个阶段验证"我们对现实世界的模型"究竟有多准确；**容量规划**（第15章）让服务的资源供给随需求演进，既不浪费也不告急；**数据管理**（第16章）守住完整性、可用性与可恢复性这条底线。四者共同构成从"救火式运维"走向"涌现式可靠性"的地基。

阅读建议：第13章的自动化决策框架与琐事治理是全部分的入门心法，适合先读；随后按团队痛点选择切入点——发布频繁先看测试，成本吃紧先看容量，数据事故多发先看数据管理。这些能力最终在第Ⅴ部分汇聚为面向韧性的产品与系统设计。

## 各章导航

| 章 | 标题 | 一句话导读 |
|---|---|---|
| [第13章](ch13.md) | 自动化与工具体系 | 从"为什么、何时、如何"三个维度建立自动化决策框架，并把琐事治理与人因设计纳入工程日常 |
| [第14章](ch14.md) | 测试 | 把测试视为对现实世界模型的精炼：测试金字塔、生产环境测试（TIP）与"测试驱动部署" |
| [第15章](ch15.md) | 容量规划 | 以四阶段生命周期组织容量供给：从手工硬编码演进到平台化的自动扩容与长周期资源规划 |
| [第16章](ch16.md) | 数据管理 | 用工程化手段保障数据的完整性、备份恢复与大规模数据运维 |

## 本部分脑图

<div id="map-part4-index-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-part4-index-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"第Ⅳ部分 基础设施设计","symbolSize":13,"children":[{"name":"Ch13 自动化与工具体系","symbolSize":8,"children":[{"name":"演进层级与规模化","symbolSize":5},{"name":"自动化决策框架","symbolSize":5},{"name":"琐事与人因治理","symbolSize":5}]},{"name":"Ch14 测试","symbolSize":8,"children":[{"name":"测试金字塔分层","symbolSize":5},{"name":"生产环境测试","symbolSize":5},{"name":"测试驱动部署","symbolSize":5}]},{"name":"Ch15 容量规划","symbolSize":8,"children":[{"name":"供给生命周期四阶段","symbolSize":5},{"name":"短长双时间尺度","symbolSize":5},{"name":"平台化自动扩容","symbolSize":5}]},{"name":"Ch16 数据管理","symbolSize":8,"children":[{"name":"数据完整性","symbolSize":5},{"name":"备份与恢复","symbolSize":5},{"name":"大规模数据运维","symbolSize":5}]}]};
  var COLOR = '#66bb6a';
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

## 相关章节

- 层级模型中本部分的位置 → [第1章](../part1/ch01.md)
- 基础设施之上的韧性设计 → [第17章](../part5/ch17.md)
- 平台化与涌现式可靠性 → [第18章](../part5/ch18.md)
