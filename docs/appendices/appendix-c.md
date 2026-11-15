---
title: 附录C · 生产会议纪要示例
---

# 附录C · 生产会议纪要示例

> [!INFO] 出处
> 《SRE：Google 运维解密（第2版）》第Ⅶ部分 · 附录C（p.530–531）

**一句话概括**：一份真实形态的生产健康会议纪要（虚构内容），展示生产会议应该盯住哪些固定栏目——从事故复盘、告警、琐事到 SLO 指标与资源，每个结论都落成带责任人的 TODO。

## 附录C 脑图

<div id="map-appendices-appendix-c-md" style="width:100%;height:260px;"></div>

<script src="../../js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('map-appendices-appendix-c-md');
  if (!el || typeof echarts === 'undefined') return;
  var data = {"name":"生产会议纪要","symbolSize":13,"children":[{"name":"基本信息","symbolSize":8,"children":[{"name":"日期、参会人员","symbolSize":5},{"name":"事项通告","symbolSize":5}]},{"name":"回顾类","symbolSize":8,"children":[{"name":"前期待办事项复盘","symbolSize":5},{"name":"故障复盘","symbolSize":5},{"name":"寻呼 / 非寻呼告警事件","symbolSize":5},{"name":"琐事检查（OK / BAD）","symbolSize":5}]},{"name":"现状类","symbolSize":8,"children":[{"name":"核心服务指标 vs SLO","symbolSize":5},{"name":"资源与利用率","symbolSize":5},{"name":"计划中的生产变更","symbolSize":5},{"name":"监控变更与/或静默","symbolSize":5}]},{"name":"行动类","symbolSize":8,"children":[{"name":"新增待办（每条带责任人）","symbolSize":5}]}]};
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

## 纪要结构与示例要点

示例纪要（日期 2015-10-21，5 名参会者）依次覆盖以下栏目：

| 栏目 | 示例内容要点 |
|---|---|
| 事项通告 | 发生重大事故 #465，击穿了错误预算 |
| 前期待办事项复盘 | 逐条核对上周 TODO 的完成情况（如山羊传送器用于羊群的认证工作，bug 1011101） |
| 故障复盘 | New Sonnet 故障 #465：参数泄漏 bug + 语料库缺失 + 史无前例的流量洪峰三者叠加，导致 12.1 亿次查询丢失；泄漏 bug 已修复并部署；正在评估负载均衡与负载卸载以防再次发生；可用性错误预算被彻底击穿，生产环境发布冻结 1 个月（豁免需以"极其离奇且无法预见"为由申请，团队共识是特批希望渺茫） |
| 寻呼告警事件 | AnnotationConsistencyTooEventual 一周触发 5 次寻呼，疑似 Bigtable 跨地域复制延迟所致；排查进行中；短期内暂无修复预期，先调高可接受的一致性延迟阈值以减少不可操作的告警 |
| 非寻呼事件 | 无 |
| 琐事检查 | OK：本周 5 次寻呼告警；BAD：本周出现 99 张工单，需深入分析成因及应对举措；OK：所有寻呼告警与工单均在响应和解决的时效目标内处理完毕 |
| 监控变更与/或静默 | 上述告警的可接受延迟阈值从 60 秒上调至 180 秒，TODO (martym) |
| 计划中的生产变更 | USA-1 集群将于 2015-10-29 至 11-02 下线维护；流量自动路由至同地域其他集群，无需人工介入 |
| 核心服务指标 | OK：99 分位延迟 88 ms < 100 ms SLO 目标（过去 30 天）；BAD：可用性 86.95% < 99.99% SLO 目标（过去 30 天） |
| 资源 | 为应对事故临时调的额外资源，下周将缩容新增实例并归还；当前利用率 CPU 60%、内存 75%、磁盘 44%（附上周对比） |
| 项目进展讨论 | Project Molière 将于两周后上线发布 |
| 新增待办事项 | 3 条 TODO，每条带责任人：调高告警阈值 (martym)、分析工单量激增原因 (jennifer)、将实例数量恢复至常规水平并归还资源 (docbrown) |

## 可以借鉴的实践

- **琐事检查二值化**：逐项给出 OK / BAD 判定并与预期对比，避免"感觉还行"式的模糊讨论。
- **指标永远和 SLO 并排出现**（88 ms < 100 ms、86.95% < 99.99%），而非孤立数字——现状好不好由 SLO 说了算。
- **结论落成带责任人的 TODO，下次会议开头复盘**：纪要形成闭环，而不是一堆没人跟进的记录。
- **错误预算击穿引发的发布冻结在会上当场决策并记录在案**，连同豁免条件一起写清。

## 交叉引用

- SLO 与核心服务指标的度量 → [第8章](../part3/ch08.md)
- 告警策略与琐事追踪 → [第9章](../part3/ch09.md)
- 事故管理与错误预算击穿后的应对 → [第10章](../part3/ch10.md)
