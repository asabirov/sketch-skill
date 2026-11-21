# Chart: Bars with a line

Template: `templates/chart/bars-with-line.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The reader compares the total of each month with a plan, a budget or a target.
- The bars and the line have the same unit, so they share one axis.

## When not to use it

- The line has another unit than the bars, such as a margin in percent over revenue in euro. A second axis is easy to misread. Draw two charts, one above the other, with the same months.
- The plan is the same for every month. Draw one grid line with the plan value.
- The reader needs only the difference from plan. Draw bars of the difference from a zero line.
- Each month has more than one bar. The line then has no clear bar to compare with.

## Many periods

Up to 24 months fit at 390 px. The bars get narrower. Below 600 px, only every third month counted back from the current month, and the last projected month, keep a label. For more than 24 months, group the months into quarters. The bars have no value labels, because the line crosses them. Three grid lines give the scale, and the data table gives each value.

## Current and projected periods

The current month shows its actual value to date in solid and its projected rest in hatch on top. Each projected month is hatched. The plan line continues over the projected months. The line has a gap of page colour around it, so it stays visible where it crosses a solid bar.
