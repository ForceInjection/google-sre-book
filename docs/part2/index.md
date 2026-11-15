---
title: 第Ⅱ部分 · 社会技术基石
---

# 第Ⅱ部分 · 社会技术基石

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅱ部分（第 4~7 章）

第1章的现代生产健康层级模型把"社会技术基石"放在最底层，这不是排序上的客套，而是承重墙：监控、SLO、混沌工程都可以采购或移植，但"工程师敢不敢报告问题、愿不愿意跨团队协作、能不能从故障中持续学习"决定了这些工具最终落在什么样的土壤里。文化不对，再好的技术实践也会在第一次重大事故后被追责文化、信息孤岛和个人英雄主义蚕食殆尽。

本部分前两章有坚实的实证支撑：DORA 的年度全球调研发现，组织文化与软件交付及运维（SDO）效能显著相关——Westrum 生机型文化不仅能预测交付速度与稳定性，还能预测员工福祉；精通 SRE 实践的团队报告更高 SDO 效能的概率是其他团队的 1.4 倍。第4、5章把这份研究落到动作上：如何培育以可靠性为中心的文化，以及如何招聘、培养并留住能承载这种文化的人。

第6、7章则回答"把人放进什么结构"：SRE 团队应如何组建、汇报与分布，以及它和研发团队之间可以采用哪些协作模式、按什么成熟度路径演进。四章合起来是一条完整的"土壤 → 种子 → 布局 → 接口"主线。

| 章 | 标题 | 一句话概括 | 深入阅读 |
|---|---|---|---|
| 第4章 | SRE 的文化土壤 | "第五个 9 是人"：以 DORA/Westrum 实证确立文化的数量级杠杆地位，给出七大文化要素与棕地/绿地两条培育路径 | [ch04](ch04.md) |
| 第5章 | SRE 招聘、培养与职业发展 | 从双画像招聘、分层培训体系到 IC 职业路径与人才留存，搭建完整的 SRE 能力体系 | [ch05](ch05.md) |
| 第6章 | SRE 的组织架构 | SRE 团队如何组建与汇报：团队规模、地域分布、层级结构及组织级协同机制 | [ch06](ch06.md) |
| 第7章 | SRE 协作模式 | SRE 与研发团队的多种协作模型及成熟度路径，帮助组织按自身阶段选择切入点 | [ch07](ch07.md) |

## 本部分脑图

<div id="map-part2-index-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-part2-index-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"第Ⅱ部分 社会技术基石","symbolSize":13,"children":[{"name":"Ch4 文化土壤","symbolSize":8,"children":[{"name":"七大文化要素","symbolSize":5},{"name":"DORA 实证支撑","symbolSize":5},{"name":"棕地/绿地路径","symbolSize":5}]},{"name":"Ch5 人才","symbolSize":8,"children":[{"name":"双画像招聘","symbolSize":5},{"name":"分层培训体系","symbolSize":5},{"name":"IC 职业与留存","symbolSize":5}]},{"name":"Ch6 组织架构","symbolSize":8,"children":[{"name":"团队规模与分布","symbolSize":5},{"name":"汇报与决策权","symbolSize":5},{"name":"组织级协同","symbolSize":5}]},{"name":"Ch7 协作模式","symbolSize":8,"children":[{"name":"多种协作模型","symbolSize":5},{"name":"成熟度矩阵","symbolSize":5},{"name":"按阶段选路径","symbolSize":5}]}]};
  var COLOR = '#ab47bc';
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

**阅读建议**：正在引入 SRE 的组织，可先读第 4 章的棕地路径与第 7 章的协作模式选好切入点，再回到第 5 章补齐招聘与培训体系；具体技术实践见第Ⅲ部分（[第8章](../part3/ch08.md)起）。

## 交叉引用

- 层级模型中"社会技术基石"的位置 → [第1章](../part1/ch01.md)
- 可靠性的商业价值 → [第2章](../part1/ch02.md)
