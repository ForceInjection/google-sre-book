---
title: 附录E · 组合 SLO 的数学原理
---

# 附录E · 组合 SLO 的数学原理

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅶ部分 · 附录E（p.534–535）

**一句话概括**：根据调用依赖的架构模式用统计模型算出本服务可用性的理论上限——串行依赖是"成功率相乘"（两个 80%/90% 的依赖只剩 72%），并行对冲是"失败率相乘"（可到 98%）。

## 附录E 脑图

<div id="map-appendices-appendix-e-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-appendices-appendix-e-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"组合 SLO","symbolSize":13,"children":[{"name":"串行依赖","symbolSize":8,"children":[{"name":"所有调用全部成功才算成功","symbolSize":5},{"name":"成功概率 = 各依赖成功率的乘积","symbolSize":5},{"name":"例：0.8 × 0.9 = 72%","symbolSize":5}]},{"name":"并行依赖（对冲 hedging）","symbolSize":8,"children":[{"name":"所有调用全部失败才会失败","symbolSize":5},{"name":"故障概率 = 各依赖故障概率的乘积","symbolSize":5},{"name":"例：1 − (0.2 × 0.1) = 98%","symbolSize":5}]},{"name":"结论","symbolSize":8,"children":[{"name":"组合 SLO 的上限由架构模式决定","symbolSize":5}]}]};
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

## 问题设定

组合多个 SLO 时，可以借助统计模型，根据下游依赖服务的可用性来计算当前服务所能达到的最高可用性；具体使用哪种模型，取决于调用这些依赖服务时采用的架构模式。

设服务 A 调用服务 B 与服务 C，两者的可用性 SLO 以故障概率表示：

```
服务 B：可用性 80%  →  p_fail(B) = 1 − 0.80 = 0.2
服务 C：可用性 90%  →  p_fail(C) = 1 − 0.90 = 0.1
```

并假设两者的故障在统计学上相互独立。

## 串行依赖

在串行依赖链中，一次请求只有在调用序列中的**所有调用全部成功**时才算成功。服务 A 成功调用的概率等于各依赖服务成功概率的乘积：

```
P(A成功) = P(B成功) × P(C成功)
         = (1 − p_fail(B)) × (1 − p_fail(C))
         = (1 − 0.2) × (1 − 0.1)
         = 0.8 × 0.9
         = 0.72
```

这意味着服务 A 所能达到的最高可用性仅为 **72%**——两个"还凑合"的依赖串在一起就只剩七成；串行链越长，衰减越快。

## 并行依赖（使用对冲 hedging）

在并行对冲模式下，一次请求只有在**所有并行调用全部失败**时才会失败。服务 A 的故障概率即服务 B 与服务 C **同时**发生故障的概率（独立性假设下相乘）：

```
p_fail(A) = p_fail(B) × p_fail(C) = 0.2 × 0.1 = 0.02
P(A成功)  = 1 − p_fail(A) = 1 − 0.02 = 0.98
```

采用这种架构，服务 A 可以达到 **98%** 的可用性。

## 结论与实践

- **组合 SLO 的上限由架构决定**：同样的两个依赖，串行 72% vs 并行对冲 98%，差距巨大。
- 给服务定 SLO 之前，先画清依赖调用图、算一算理论上限——不要承诺一个依赖结构根本达不到的目标。
- **独立性是关键假设**：共享故障域（同一集群、同一数据库）会让"并行对冲"的实际效果大打折扣。
- 冗余、故障自动转移与优雅降级，正是把"串行"改造成"对冲"的工程手段。

## 交叉引用

- SLO 的定义、制定与错误预算 → [第8章](../part3/ch08.md)
- 故障自动转移与优雅降级（把串行变对冲的手段） → [第17章](../part5/ch17.md)
- 延迟侧的统计建模 → [附录F](appendix-f.md)
