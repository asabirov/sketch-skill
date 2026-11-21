# Chart: Bars with a line

Template: `templates/chart/bars-with-line.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The reader compares the total of each month with a plan, a budget or a target.
- The bars and the plan have the same unit, so they share one axis.
- The plan can change from month to month.

## When not to use it

- The plan has another unit than the bars, such as a margin in percent over revenue in euro. A second axis is easy to misread. Draw two charts, one above the other, with the same months.
- The plan is the same for every month. Draw one `sketch-ref` line with the plan value.
- The reader needs only the difference from plan. Draw bars of the difference from a zero line.
- Each month has more than one bar. The plan tick then has no clear bar to compare with.

## Plan tick, not an outline bar

The plan of each month is a dashed tick across its period, with the plan value above it. A continuous line is not used, because it suggests values between the months. An outline bar for the plan that the actual bar fills is not used either. A bar above its plan would hide the outline, and an outline is already the sign of a projected bar.

## Many periods

Up to 24 months fit at 390 px. The bars get narrower. From 600 px, each month has a label and a plan value. The plan value sits above the tick or above the bar, whichever is higher. Below 600 px, only the first month and the current month keep a label, and the plan values hide, because a value is wider than its period. Three grid lines give the scale, the summary gives the plan of the current month, and the data table gives each value to screen readers. For more than 24 months, group the months into quarters.

## Above and below plan

A complete month at or above its plan is solid. A complete month below its plan is in the thinned ink of `below`. The tone is not the only sign: the top of the bar is above or below its tick. The key names both, and the data table gives screen readers the difference from plan of each month.

## Current and projected periods

The summary above the chart gives the value to date against the plan of the month, and the projected total against the plan. A dashed vertical line marks today, with the label "Today". The current month shows its actual value to date in solid and its projected rest in hatch on top. Each projected month is hatched and has its plan tick. The tick has a band of page around it, so it stays visible on a solid bar.
