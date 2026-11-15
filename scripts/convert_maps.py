#!/usr/bin/env python3
"""把 docs/**/*.md 里的 ```markmap 代码块批量替换为简化的 ECharts 横向树。

用法： python3 scripts/convert_maps.py
幂等： 转换后页面不再含 markmap 块，重复运行无效果。
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs"

COLORS = {
    "part1": "#ef5350",
    "part2": "#ab47bc",
    "part3": "#29b6f6",
    "part4": "#66bb6a",
    "part5": "#ffa726",
    "part6": "#ec407a",
    "appendices": "#78909c",
}
DEFAULT_COLOR = "#d32f2f"

TEMPLATE = """<div id="__ID__" style="width:100%;height:260px;"></div>

<script src="__PREFIX__js/echarts.min.js"></script>
<script>
(function () {
  var el = document.getElementById('__ID__');
  if (!el || typeof echarts === 'undefined') return;
  var data = __DATA__;
  var COLOR = '__COLOR__';
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
</script>"""


def parse_tree(block: str):
    """把 markmap 大纲（markdown 标题行）解析为树；忽略块内注入的 frontmatter。"""
    root = None
    stack = {}
    for raw in block.splitlines():
        m = re.match(r"^(#{1,6})\s+(.+?)\s*$", raw)
        if not m:
            continue
        level, text = len(m.group(1)), m.group(2).strip()
        node = {"name": text, "children": []}
        if level == 1 and root is None:
            root = node
            stack = {1: node}
            continue
        parent = None
        for lv in range(level - 1, 0, -1):
            if lv in stack:
                parent = stack[lv]
                break
        if parent is None:
            if root is None:
                root = node
                stack = {1: node}
                continue
            parent = root
        parent["children"].append(node)
        stack[level] = node
        for lv in [l for l in stack if l > level]:
            del stack[lv]
    return root


def js_data(node, depth=0):
    size = 13 if depth == 0 else (8 if depth == 1 else 5)
    if node["children"]:
        kids = ",".join(js_data(c, depth + 1) for c in node["children"])
        return '{"name":%s,"symbolSize":%d,"children":[%s]}' % (
            json.dumps(node["name"], ensure_ascii=False), size, kids)
    return '{"name":%s,"symbolSize":%d}' % (
        json.dumps(node["name"], ensure_ascii=False), size)


def convert_file(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    # MkDocs 目录式 URL：docs/part3/ch08.md -> /part3/ch08/ ，相对深度 = 路径部件数
    prefix = "../" * len(rel.parts)
    color = COLORS.get(rel.parts[0], DEFAULT_COLOR) if len(rel.parts) > 1 else DEFAULT_COLOR
    slug = re.sub(r"[^a-z0-9]+", "-", str(rel).lower()).strip("-")

    text = path.read_text(encoding="utf-8")
    if "```markmap" not in text:
        return False

    count = 0

    def repl(m):
        nonlocal count
        count += 1
        block_id = ("map-%s" % slug) + (("-" + str(count)) if count > 1 else "")
        root = parse_tree(m.group(1))
        if root is None:
            return m.group(0)
        html = (TEMPLATE
                .replace("__ID__", block_id)
                .replace("__PREFIX__", prefix)
                .replace("__DATA__", js_data(root))
                .replace("__COLOR__", color))
        return html

    new = re.sub(r"```markmap\n(.*?)```", repl, text, flags=re.S)
    if new != text:
        path.write_text(new, encoding="utf-8")
        return True
    return False


def main():
    changed = 0
    for p in sorted(ROOT.rglob("*.md")):
        if p == ROOT / "index.md":  # 首页是知识星系，不处理
            continue
        if convert_file(p):
            changed += 1
            print(f"converted: {p.relative_to(ROOT)}")
    print(f"\n{changed} files converted.")
    leftover = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*.md")
                if "```markmap" in p.read_text(encoding="utf-8") and p != ROOT / "index.md"]
    if leftover:
        print("LEFTOVER markmap blocks:", leftover)
        sys.exit(1)


if __name__ == "__main__":
    main()
