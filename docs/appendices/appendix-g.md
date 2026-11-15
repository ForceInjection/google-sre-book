---
title: 附录G · 现代可观测性：统计学与机器学习
---

# 附录G · 现代可观测性：统计学与机器学习

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅶ部分 · 附录G（p.538–539）

**一句话概括**：智能告警背后的技术基石——错误率用二项分布 + 威尔逊置信区间建立流量感知的动态基线；周期性指标交给机器学习模型预测；性价比最高的落地场景是告警后的排查分析。

## 附录G 脑图

<div id="map-appendices-appendix-g-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-appendices-appendix-g-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"统计学与机器学习","symbolSize":13,"children":[{"name":"错误率的统计学方法","symbolSize":8,"children":[{"name":"请求结果二元 → 二项分布建模","symbolSize":5},{"name":"过去两周流量 → 动态基线错误概率","symbolSize":5},{"name":"威尔逊置信区间：超出预期上限即告警","symbolSize":5},{"name":"天然流量感知：低流量宽、大流量严","symbolSize":5},{"name":"落地：查询语言写二项检验 / 周期任务发基线指标","symbolSize":5}]},{"name":"周期性指标的机器学习","symbolSize":8,"children":[{"name":"资源使用率按天/周波动，简单统计法失效","symbolSize":5},{"name":"ML 预测预期表现 + 置信区间边界","symbolSize":5},{"name":"专用模型 或 通用时间序列模型（如 TimesFM）","symbolSize":5},{"name":"两大考量：可解释性与成本","symbolSize":5}]},{"name":"告警后分析","symbolSize":8,"children":[{"name":"告警已触发 = 强先验信号","symbolSize":5},{"name":"只在故障时评估，成本师出有名","symbolSize":5}]}]};
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

## 错误率的统计学方法

- 最常见的监控信号——错误率——并非无规律的随机事件流：对任何给定的请求，结果都是二元的（要么成功要么失败），这是一个经典的统计模式，可以用**二项分布**（binomial distribution）建模。
- 第一步是教会系统各独立服务的"正常状态"究竟什么样：不再采用一刀切的阈值，而是通过分析**过去两周**的流量，建立起**动态的基线错误概率**。
- 用**威尔逊置信区间**（Wilson's confidence interval）来描述错误的预期分布；一旦超出预期的最大错误范围，系统就触发告警。（也可以使用许多其他统计方法并取得类似效果，但威尔逊区间不仅鲁棒性强，而且实现简单。）
- **天然流量感知**：低流量服务的可接受错误范围更宽，避免因零星几次随机失败而误发告警；大流量服务的范围按比例收紧得多，哪怕错误率只有极其微小的升幅（可能影响成千上万的用户）也能被敏锐察觉。这自动解决了以往静态阈值永远无法克服的问题——把 SRE 从繁重的告警调优中解放出来，且让"警报一响"必然意味着出现了偏离正常状态的真实异常。
- 落地途径有二：直接在监控系统的查询语言中表达**二项检验**（第8章侧边栏有讨论）；或构建一个周期性任务计算置信区间的上限，将其作为基线指标发布出来供比对。

## 利用机器学习处理周期性指标

- 许多服务中，错误率在整个服务生命周期内都较低且大体稳定；但其他指标——比如资源使用率（RAM、CPU）——会根据服务的使用情况呈现**按天或按周波动的峰谷特征**，针对这类服务，上一节的简单统计方法就行不通了。
- 改为**训练机器学习模型**：根据过去观察到的数据来预测当前的预期表现，实际观测值与模型的预期不符时触发告警。模型能够学习周期性规律并给出置信区间边界。
- 既可针对特定类型的底层数据专门训练，也可采用通用的时间序列模型，例如 TimesFM。
- 两大不可忽视的考量——**可解释性与成本**：
  - 并非所有异常都代表系统出了问题（例如某项偶发事件导致流量突增，此时系统整体依然完全按预期运行）；即便真的出了问题，往往也很难解释其根本原因。
  - 机器学习模型的运行成本显著高于统计模型——绝不能不加节制地在所有地方部署它们，从而彻底抛弃其他监控手段。

## 一种高性价比的应用：告警后分析

- 机器学习尤为有效的领域之一，是对异常进行**告警后分析**（post-alert analysis）：为响应告警而动态构建排查仪表盘（第10章）。
- 此时已经拥有一个强烈的先验信号——告警已触发——因此当下出现的每一个异常都是潜在的排查线索。
- 机器学习模型的成本不仅变得师出有名，而且开销小得多：只在系统出现故障时才进行评估，而非定期高频运行。

## 交叉引用

- 告警理念从静态阈值的战略性转变 → [第9章](../part3/ch09.md)
- 二项检验与威尔逊区间侧边栏 → [第8章](../part3/ch08.md)
- 响应告警而动态构建的排查仪表盘 → [第10章](../part3/ch10.md)
- 延迟退化的统计学基础 → [附录F](appendix-f.md)
