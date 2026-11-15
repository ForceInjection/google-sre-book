---
title: 附录F · 延迟告警的数学原理
---

# 附录F · 延迟告警的数学原理

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅶ部分 · 附录F（p.536–537）

**一句话概括**：把海量独一无二的工作负载模糊聚类成"有意义"的群组，对每个群组建立正态基线，用 z 分数检测超阈值观测的占比——这是"全服务范围性能退化"类延迟告警的统计基础。

## 附录F 脑图

<div id="map-appendices-appendix-f-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-appendices-appendix-f-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"延迟告警的数学","symbolSize":13,"children":[{"name":"群组划分","symbolSize":8,"children":[{"name":"工作负载集合 W → N 个互不重叠群组 C_i","symbolSize":5},{"name":"粒度：区分行为差异 与 信噪比 之间平衡","symbolSize":5},{"name":"\"有意义\"判据：基数 ≥ 10000 且 CV ≤ 0.5","symbolSize":5},{"name":"目标：有意义群组并集覆盖 ≥ 65% 负载","symbolSize":5}]},{"name":"基线与检测","symbolSize":8,"children":[{"name":"正态假设，用 30~60 天数据估均值/标准差","symbolSize":5},{"name":"z 分数 =（观测 − 均值）/ 标准差","symbolSize":5},{"name":"超阈值占比显著上升 = 全服务退化信号","symbolSize":5}]},{"name":"扩展","symbolSize":8,"children":[{"name":"非正态指标：经验分布","symbolSize":5},{"name":"小群组：分层贝叶斯聚合","symbolSize":5}]}]};
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

- 有一组由用户生成的工作负载 w ∈ W，它们在某个服务上独立运行；另有某种衡量工作负载在该服务上性能表现的指标 m: W → R（例如延迟）。
- 将工作负载集合 W 划分为 N 个互不重叠的独立群组（cohort）C_i（1 ≤ i ≤ N），所有群组的并集为 W。
- 每个工作负载本质上都是独一无二的——可能写入不同的文件、在不同的数据上进行计算、在不同的集群上执行——因此必须以某种**模糊聚类**的方式分组，捕捉人类直觉上对"等价性"的预期。群组粒度必须足够细，以区分行为特征各异的负载；同时又足够粗，以维持合理的信噪比。

## "有意义"的群组

一个群组 C_i 若满足最小基数阈值 B（例如 B ≥ 10000），且其方差相对于均值较小，就被视为"有意义"（meaningful）：

```
CV(C_i) = sqrt( Var( m(C_i) ) ) / m( C_i ) ≤ K，其中 K ≤ 0.5
```

目标是最大化落入这些有意义群组中的工作负载数量——通常情况下，让有意义群组的并集**至少覆盖工作负载 W 的 65%**。

## 基线性能预期与 z 分数

为简便可假设：对于给定的群组 C_i，其工作负载的性能指标是独立同分布的，服从底层的正态分布；实践中用 **30 到 60 天**的基线数据集，估计每个群组该度量指标的均值 μ_i 与标准差 σ_i：

```
m(w) ~ N( μ_i , σ_i² )    for w ∈ C_i

z_w = ( m(w) − μ_i ) / σ_i    for w ∈ C_i
```

z 分数（z-score）衡量的是某个观测值偏离均值多少个标准差。对于平稳且形态良好的度量指标，z 分数将服从标准正态分布 N(0, 1)。

## 检测量与关键结论

给定一个 z 分数阈值 z_thr（例如 z_thr = 2），将检测指标定义为测试集 W_test 中 z 分数大于 z_thr 的工作负载所占的观测比例：

```
D( W_test , z_thr ) = | w ∈ W_test : z_w > z_thr | / | W_test |
```

- 对于理想的正态分布，z 分数超过 2 的理论比例应为 **2.28%**。
- 从经验上看，由于模型的不完美以及系统的自然演进，这一基线通常会略高一些，大约在 **4%** 左右。
- 该比例若出现**显著上升**，则是发生全服务范围性能退化（regression）的强烈信号。

## 扩展方向

- 对不服从正态分布的指标（例如延迟通常服从**对数正态分布**），可以使用**经验分布**代替参数化分布。
- 对规模较小、"无意义"的群组，可以采用**分层贝叶斯方法**（hierarchical Bayesian approach）聚合，从而把它们也纳入性能退化检测模型。
- 威尔逊区间得分（错误率一侧的方法）在[第8章](../part3/ch08.md)的"利用二项检验"侧边栏中有讨论。

## 交叉引用

- SLI / SLO 与错误预算 → [第8章](../part3/ch08.md)
- 告警策略（建立在这套数学基础之上的一层） → [第9章](../part3/ch09.md)
- 统计学与机器学习的进一步延伸 → [附录G](appendix-g.md)
