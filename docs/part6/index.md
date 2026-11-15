---
title: 第Ⅵ部分 · 展望
---

# 第Ⅵ部分 · 展望

前五个部分讲的是经过验证的"当下"；这一部分问的是"接下来会怎样"。AI 正在重塑软件的构建方式：代码生成成本趋近于零，传统 SDLC 各阶段的边界被急剧压缩，进入生产环境的变更速率逼近人类反应的极限。SRE 诸多工作背后的基础假设正在失效，而非功能性需求——可靠性、安全性、可测试性——承受的压力却在与日俱增。

本部分是双向叙事。一方面看 AI 如何冲击 SRE：第19章逐项推演生产运维各环节在 AI 开发时代的走向，第20章剖析机器学习工作负载这一全新且本质非确定性的可靠性对象。另一方面看 SRE 与 AI 如何互相赋能：第21章展示 AI 与自主智能体如何成为能力倍增器，把 SRE 从手工耕带向涌现式可靠性。第22章把镜头拉回地面，为各种规模与约束的组织给出务实落地路径；第23章则展望学科的长期轨迹。

两条主线贯穿始终：其一，"左移"（shifting left）正在让位于"下移"（shifting down）——与其要求每个工程师都精通可靠性，不如把可靠性内嵌进自治的生产平台；其二，风险正在被当作可靠性的先导指标，SRE 角色随之从运维专家演进为架构通才，最终抵达人机协同消除琐事、构建"默认可靠"（reliable by default）系统的未来。

## 各章导航

| 章节 | 一句话看点 |
|---|---|
| [第19章 · 处在转折点上的 SRE](ch19.md) | AI dev 压缩 SDLC、非功能性需求承压，逐项推演变更速率、技术债、版本控制、调试与事故的应变 |
| [第20章 · 机器学习负载的生产运维](ch20.md) | 为非确定性的生成式输出与 TPU/GPU 等稀缺加速器，重构 SLO 与容量规划 |
| [第21章 · AI 重塑 SRE 日常工作](ch21.md) | 智能体成为能力倍增器：态势感知、动态事故面板与自动化应急处置 |
| [第22章 · SRE 在任何组织落地](ch22.md) | 从初创孤军奋战到合规约束下的混合架构，以琐事削减与无指责文化因地制宜 |
| [第23章 · SRE 的未来轨迹](ch23.md) | 左移走向下移、风险作可靠性先导指标、SRE 从运维专家演进为架构通才 |

## 本部分脑图

<div id="map-part6-index-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-part6-index-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"第Ⅵ部分 · 展望","symbolSize":13,"children":[{"name":"Ch19 转折点上的 SRE","symbolSize":8,"children":[{"name":"AI dev 压缩 SDLC","symbolSize":5},{"name":"非功能性需求承压","symbolSize":5},{"name":"人类兜底理解系统","symbolSize":5}]},{"name":"Ch20 机器学习负载","symbolSize":8,"children":[{"name":"输出非确定性","symbolSize":5},{"name":"模型服务 SLO 重构","symbolSize":5},{"name":"加速器容量规划","symbolSize":5}]},{"name":"Ch21 AI 重塑日常","symbolSize":8,"children":[{"name":"智能体能力倍增器","symbolSize":5},{"name":"态势感知自动化","symbolSize":5},{"name":"迈向涌现式可靠性","symbolSize":5}]},{"name":"Ch22 任何组织落地","symbolSize":8,"children":[{"name":"混合与遗留环境","symbolSize":5},{"name":"厘清优先次序","symbolSize":5},{"name":"琐事削减与文化","symbolSize":5}]},{"name":"Ch23 未来轨迹","symbolSize":8,"children":[{"name":"左移变为下移","symbolSize":5},{"name":"风险作先导指标","symbolSize":5},{"name":"专才走向通才","symbolSize":5}]}]};
  var COLOR = '#ec407a';
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
