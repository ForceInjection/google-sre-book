---
title: 第Ⅲ部分 · 态势感知与常态化备战
---

# 第Ⅲ部分 · 态势感知与常态化备战

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅲ部分导读（第8~12章）

**一句话概括**：视角从文化与组织原则转向运维实战——用 SLO 与可观测性回答"系统现在好不好"，用轮值与应急响应回答"出事了怎么办"，用复盘与安全工程保证"同样的坑不踩第二次"。

本部分对应现代生产健康层级模型中的"态势感知"与"常态化备战"两层。态势感知的基石在于真正理解服务"损坏"的本质含义：第8章对本第1版提出的 SLO 框架做了全面升级，把用户满意度量化为可协商的目标、错误预算与告警策略；第9章则阐述业界如何从以指标为中心的传统监控，转向融合时序数据、日志、分布式追踪与持续性能剖析的全方位可观测性，并引入智能告警与机器学习驱动的动态仪表盘。确立目标之后，团队需要借助遥测数据检验自己是否达标——这正是两章的先后逻辑。

当预防措施失效、告警触发之时，人工响应人员必须接管全局。第10章探讨如何构建可持续的轮值排班机制并组织高效的应急响应，着重指出成功的应急管理不仅取决于技术实力，更依赖清晰的角色、结构化的排查与顺畅的沟通协作。而应急响应并不随系统恢复而终结——每一次故障都是不可多得的学习契机：第11章重温无指责事后总结与心理安全感两大核心准则，并引入社会技术系统分析、以客户为中心的复盘与分层评估机制；第12章则挑战软件行业传统依赖的线性根因分析，改用系统理论方法（CAST 回顾性归因、STPA 前瞻性分析），从被动的应急救火转向主动的安全工程。

## 各章导航

| 章节 | 主题 | 一句话导读 |
|---|---|---|
| [第8章](ch08.md) | 服务质量目标（SLO） | SLI/SLO/错误预算的进阶实战：常见陷阱、关键用户旅程（CUJ）、单客户 SLO、隐式与客户端 SLO、工具体系与模型局限 |
| [第9章](ch09.md) | 可观测性与监控 | 从监控走向可观测性：OpenTelemetry 与 eBPF、高可用/分析型双轨遥测、客户端遥测、以 CUJ 为核心的客户监控，以及统计学与 AI |
| [第10章](ch10.md) | 应急事件管理与轮值待命 | 搭建可持续的轮值排班与事故响应团队：明确事故定义、协调角色、结构化排查，并审视 AI 正在重塑的应急领域 |
| [第11章](ch11.md) | 从事故中学习 | 无指责事后总结与心理安全感的十年演进：社会技术系统分析、以客户为中心的复盘、分层评估与跨组织共享教训 |
| [第12章](ch12.md) | 基于 STPA 与 CAST 的 SRE 安全工程 | 用系统理论过程分析（STPA）在事故前识别并消除设计缺陷，用因果分析（CAST）做系统级回顾性复盘 |

## 本部分脑图

<div id="map-part3-index-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-part3-index-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"第Ⅲ部分 态势感知与常态化备战","symbolSize":13,"children":[{"name":"Ch8 SLO","symbolSize":8,"children":[{"name":"量化用户满意度","symbolSize":5},{"name":"错误预算定取舍","symbolSize":5},{"name":"CUJ 与单客户 SLO","symbolSize":5}]},{"name":"Ch9 可观测性","symbolSize":8,"children":[{"name":"统一插桩 OTel","symbolSize":5},{"name":"高可用与分析双轨","symbolSize":5},{"name":"客户端与 CUJ 监控","symbolSize":5}]},{"name":"Ch10 应急与轮值","symbolSize":8,"children":[{"name":"可持续轮值排班","symbolSize":5},{"name":"角色与结构化排查","symbolSize":5},{"name":"AI 重塑应急响应","symbolSize":5}]},{"name":"Ch11 从事故中学习","symbolSize":8,"children":[{"name":"无指责复盘","symbolSize":5},{"name":"心理安全感","symbolSize":5},{"name":"分层评估共享教训","symbolSize":5}]},{"name":"Ch12 安全工程","symbolSize":8,"children":[{"name":"STPA 前瞻识别隐患","symbolSize":5},{"name":"CAST 系统级归因","symbolSize":5},{"name":"从救火转向设计","symbolSize":5}]}]};
  var COLOR = '#29b6f6';
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
