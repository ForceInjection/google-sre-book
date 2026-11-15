---
title: 附录B · SRE 团队章程模板
---

# 附录B · SRE 团队章程模板

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅶ部分 · 附录B（p.529）

**一句话概括**：一份可复用的团队章程骨架——元数据加上使命、职责范围、服务、成功定义、价值观五个段落，让团队与利益相关方就"我们是谁、管什么、怎样算成功"达成书面共识。

## 附录B 脑图

<div id="map-appendices-appendix-b-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-appendices-appendix-b-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"SRE 团队章程模板","symbolSize":13,"children":[{"name":"元数据","symbolSize":8,"children":[{"name":"状态：草稿 / 评审中 / 已批准 / 已废弃","symbolSize":5},{"name":"作者、评审人、批准人（SRE 高级主管）","symbolSize":5},{"name":"最近更新时间","symbolSize":5}]},{"name":"五个正文段落","symbolSize":8,"children":[{"name":"使命：一句话、非机密","symbolSize":5},{"name":"职责范围：含\"明确不做\"的负面清单","symbolSize":5},{"name":"服务：所支撑的服务（群）","symbolSize":5},{"name":"成功定义：达成并持续维持的目标","symbolSize":5},{"name":"价值观：团队文化","symbolSize":5}]}]};
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

## 模板骨架

```text
<团队名称> 章程
──────────────────────────────────────────────
状态：<草稿 | 评审中 | 已批准 | 已废弃>
最近更新时间：<日期>
作者：<作者邮箱地址>
评审人：<相关利益相关方>
批准人：<SRE 高级主管>

## 使命
<一句话、非机密的陈述；团队全员与利益相关方达成共识，
 清晰阐明团队在更广泛组织背景下所扮演的角色>

## 职责范围
<技术环境、客户群体，以及团队提供的服务与支持
（协作模式、专长技能等）；
 并明确列出明确不在职责范围之内的事项>

## 服务
<团队所支持的服务（或服务群），进一步细化职责范围>

## 成功定义
<基于既定的职责范围，描述怎样的状态才算是取得成功；
 阐明团队如何随时间推移达成并持续维持其目标>

## 价值观
<团队文化，以及这种文化如何帮助团队自身及其合作伙伴
 取得成功、实现可持续发展并保持健康运作>
```

## 写作要点

- **使命必须一句话、非机密**——要让组织里任何人都能读懂并复述团队的角色。
- **职责范围的价值在负面清单**：明确写出"不在职责范围内"的事项，比罗列"做什么"更能消除边界争议。
- **成功定义是可持续状态**，不是一次性里程碑：要说明如何随时间推移达成并持续维持。
- **章程有生命周期**：草稿 → 评审 → 批准，批准人是 SRE 高级主管；记录最近更新时间，写完不更新就会腐化。
- 填写前可参考按此模板写就的成品范例 → [附录D](appendix-d.md)。

## 交叉引用

- 团队文化与社会技术基石 → [第4章](../part2/ch04.md)
- SRE 的定位与赋能者角色（为什么需要章程） → [第1章](../part1/ch01.md)
- 按此模板写就的虚构示例 → [附录D](appendix-d.md)
