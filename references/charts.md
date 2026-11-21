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
- Show the projected periods after the current period. Label each one, such as "Dec proj.", and put "~" before a projected value.
- Start the value axis of bars at zero. If a line starts at another value, write that value on the lowest grid line.
- Use at most three grid lines.
- Never use a second value axis. If two series have different units, draw two charts.
- Never scroll inside a chart. Each rule page says how many periods fit and what to do with more.
- Name each mark in words in a `sketch-key`. Never use a hue.
- Give the chart `role="img"` and an `aria-label` with a summary and the values. Put the data in a `details` table below the chart.
- Write the main number of the chart in one sentence above it, such as "November so far: €39k of €57k projected."

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
