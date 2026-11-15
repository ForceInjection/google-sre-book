---
title: 附录A · 培训投入的投资回报率（ROI）计算
---

# 附录A · 培训投入的投资回报率（ROI）计算

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅶ部分 · 附录A（p.528）

**一句话概括**：用一个"一年招聘 20 名 SRE"的假想场景，对比"自生自灭 vs 有培训"两条路径的年度总成本，把培训的价值折算成 67 周 + 10000 美元——这是向管理层论证培训预算的量化模板。

## 附录A 脑图

<div id="map-appendices-appendix-a-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-appendices-appendix-a-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"培训 ROI 计算","symbolSize":13,"children":[{"name":"假设场景","symbolSize":8,"children":[{"name":"一个日历年招聘 20 名 SRE","symbolSize":5},{"name":"两个世界：自生自灭 vs 有培训","symbolSize":5}]},{"name":"成本因子","symbolSize":8,"children":[{"name":"招聘与入职：两场景相同（12 周 + 1 万美元/人）","symbolSize":5},{"name":"成长周期：12 周 → 8 周（培训加速 4 周）","symbolSize":5},{"name":"培训成本：入职培训 1 周 + 每人 1 周导师时间","symbolSize":5},{"name":"第一年流失率：10% → 5%","symbolSize":5}]},{"name":"结论","symbolSize":8,"children":[{"name":"ROI = 67 周 + 10000 美元","symbolSize":5},{"name":"先估算、后用真实数据修正","symbolSize":5}]}]};
  var COLOR = '#78909c';
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

## 计算模型

假设场景：某公司计划在一个日历年内招聘 20 名 SRE，评估启动一项培训计划可能带来的潜在 ROI。需要分别在"自生自灭"（无培训）与"有培训"两种场景下，估算招聘并入职一名新 SRE 所需的成本。

| 因素 | "自生自灭"（无培训） | "有培训" |
|---|---|---|
| 寻找并入职一名新员工所需时间 | 12 周 | 相同 |
| 寻找并入职一名新员工所需投入 | 1 周招聘人员/面试时间，10000 美元的广告、差旅、搬迁等费用 | 相同 |
| 从入职到成长为完全胜任且高产出的 SRE 所需时间 | 12 周 | 8 周（4 周 = 培训使上手速度加快的时间） |
| 完成入职培训所需时间 | 0 | 1 周 |
| 培训所需投入 | 0 | 每名新员工 1 周导师/讲师时间 |
| 第一年内的流失率 | 10% | 5% |

把这些因子折算成年度总成本（每人占用周数 × 人数 + 现金成本）：

```
自生自灭：(12 + 1 + 12) 周 × (20 + (10% × 20)) = 25 周 × 22 人 = 550 周 + 220000 美元
有培训：  (12 + 1 + 8 + 1 + 1) 周 × (20 + (5% × 20)) = 23 周 × 21 人 = 483 周 + 210000 美元

ROI = 550 − 483 = 67 周；220000 − 210000 = 10000 美元
```

即该培训计划带来的 ROI 为 **67 周 + 10000 美元**：培训额外付出的 1 周入职培训与每名新员工 1 周导师时间，被"上手加速 4 周 + 流失率减半"轻松覆盖。

## 适用场景与做法

- 培训项目启动**前**用假设数据估算影响；项目正式运转后，再用项目和组织的实际数据进一步修正这些估算值。
- 建议建立一个包含成本估算的电子表格，自动计算培训计划的 ROI——便于根据利益相关者的反馈或最新掌握的信息快速调整假设。
- 务必明确列出你的各项假设，让利益相关者清楚计算结果是怎么得来的，并自行评估其可信度。
- 这套"假设场景 + 成本折算"的框架同样适用于论证其他短期看不见回报的投入：文档建设、工具化、琐事清理。

## 交叉引用

- 为可靠性这类"无形投入"争取预算的底层逻辑 → [第2章](../part1/ch02.md)
- 培训在 SRE 落地路线图中的位置（常态化备战层） → [第1章](../part1/ch01.md)
- 流失率背后的文化与激励（社会技术基石） → [第4章](../part2/ch04.md)
