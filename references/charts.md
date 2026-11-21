# Charts

Use this page to choose a chart template and to draw a chart in a sketch. The practices and their sources are in [the chart study](../docs/studies/2026-11-21-chart-best-practices.md).

## Choose a template

| Template | Use it for | Rule page |
| --- | --- | --- |
| `templates/chart/monthly-bars.html` | A total for each month | [charts/monthly-bars.md](charts/monthly-bars.md) |
| `templates/chart/line-over-time.html` | A level over time, such as a balance | [charts/line-over-time.md](charts/line-over-time.md) |
| `templates/chart/bars-with-line.html` | A total for each month against a plan in the same unit | [charts/bars-with-line.md](charts/bars-with-line.md) |
| `templates/chart/table-sparkline.html` | A trend in each row of a table | [charts/table-sparkline.md](charts/table-sparkline.md) |
| `templates/chart/stat-trend.html` | A few key numbers, each with a small trend | [charts/stat-trend.md](charts/stat-trend.md) |

## Rules for every chart

- Put time on the horizontal axis, from left to right.
- Draw an actual value solid and a projected value hatched. A line has no hatch, so its projected part is dashed.
- Show the current period that is not complete. Draw its actual value to date solid and its projected rest hatched on top. Label it, such as "Nov to date".
- Show the projected periods after the current period. From 600 px, label each one, such as "Dec proj.". Below 600 px, the hatch or the dashed line and the key name them. Put "~" before a projected value.
- Start the value axis of bars at zero. If a line starts at another value, write that value on the lowest grid line.
- Use at most three grid lines.
- Never use a second value axis. If two series have different units, draw two charts.
- Never scroll inside a chart. Each rule page says how many periods fit and what to do with more.
- Name each mark in words in a `sketch-key`. Never use a hue.
- Give the chart `role="img"` and an `aria-label` with a summary and the values. Put the data in a `details` table below the chart, with the class `sketch-data`. A sparkline in a table row gives every value in its `aria-label` in place of a table.
- Put the main numbers above the chart in a `sketch-summary`, such as "November 1 to 21: €39k" and "November, projected: ~€57k". Give each value its change against the same days of the earlier period.
- Split a bar into at most 2 parts. Draw the lower part solid and the upper part in the thinned ink of `second`. A projected bar is not split, because the split of a projection is not known.
- Draw a reference level, such as a minimum cash level, as a `sketch-ref` line with its name and value on the line.

## The chart classes

The classes are in `assets/sketch.css`, after the sparkline.

- `sketch-chart` holds a `sketch-plot` and a `sketch-periods` row. Set `--n` to the number of periods.
- Each `div` in the `sketch-plot` is one period. Give each `<i>` its value as `--v`, a percent of the plot height. A `<b>` before the `<i>` is the value label.
- `partial` on a period marks the current period. Give it `<i class="rest">` for the projected rest, then `<i>` for the actual value to date.
- `projected` on a period marks a future period.
- `minor` on a period and on its label hides the value and the label below 600 px.
- `sketch-plot line` draws points. Put the line in one `<svg class="sketch-line" viewBox="0 0 <n × 10> 100" preserveAspectRatio="none">`. Point k is at x = 10k + 5 and y = 100 − value. Put `projected` on the dashed part. Put `halo` on a copy of a line that crosses filled bars.
- `<span class="sketch-tick" style="--v:50%"><span>30k</span></span>` in the plot draws a grid line with its value on the left.
- `--h` on a `sketch-plot` sets its height. The default is 180 px.
- `projected` on a `polyline` in a `sketch-spark` makes that part dashed.
- `<polygon class="area">` in a `sketch-line` or a `sketch-spark` fills the area below the actual line with a wash. Close it at the last actual point, so the projected part has no area.
- `compare` on a `polyline` in a `sketch-line` draws a thin line for an earlier period, such as October. Name it in the key with `<i class="line compare">`.
- `<i class="second">` before the other `<i>` of a period is the upper part of a split bar. Name it in the key with `<i class="second">`.
- `<span class="sketch-ref" style="--v:25%"><span>Minimum €100k</span></span>` in a plot draws a reference level with its label on the right.
- `<span class="plan" style="--p:90%"></span>` and `<b class="plan-value" style="--t:95%">54k</b>` before the bars of a period draw a dashed plan tick and its value. Set `--t` to the top of the tick or of the bar, whichever is higher. The value hides below 600 px. Name the tick in the key with `<i class="plan">`.
- `below` on a period draws its bar in the thinned ink, for a month below its plan.
- `<span class="sketch-today" style="--x:83.6%"><span>Today</span></span>` in a plot draws a dashed vertical line at today. Set `--x` to the place of today across the plot.
- `ends` on a `sketch-periods` row keeps its first and last label inside the chart. Then give the first and the last label a year, such as "Dec 2025".
- `<dl class="sketch-summary">` holds the numbers above a chart, one `div` of `dt` and `dd` for each. The first value is the largest. A `span` after the value is its change.
- `<td class="sketch-trend">` holds the change in a `span` above a `sketch-spark`, in a table row. The sparkline is 120 px wide, and 80 px below 600 px.
- `<div class="sketch-tabs sketch-tiles">` holds stat tiles as `button role="tab"` with `aria-controls`. Each tile holds a label, a `b` value, a change and a `sketch-spark`. The chosen tile has a drawn frame and shows its `role="tabpanel"`.
- `<div class="sketch-goal" role="meter">` shows a value against a total: a `span class="mark"` label, a `div class="track"` with an `<i>`, and a row with the two ends. Set `--v` on the mark and the `<i>`. The actual part is solid and the rest is hatched.
- `sketch-data` on a `sketch-table` keeps its headers and rows below 600 px. Use it for the data table of a chart and for a table with a sparkline in each row.
