# Chart: Monthly bars

Template: `templates/chart/monthly-bars.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The reader compares a total of each month with the other months, such as revenue, costs or orders.
- Each value is a sum over the period, so a bar from zero shows its size.
- The values have one unit.

## When not to use it

- The value is a level at a point in time, such as a cash balance or a count of active users. Use the line over time.
- The reader compares each month with a plan or a target. Use the bars with a line.
- The reader compares categories, such as products or countries, not periods. Draw horizontal bars with the category names on the left.
- The chart has two series in different units. Draw two charts.
- The page shows only one number. Use the stat with a small trend.

## Many periods

Up to 24 months fit at 390 px. The bars get narrower, and each bar is at most 48 px wide. Below 600 px, only every third month counted back from the current month, and the last projected month, keep a label. The phone hides the value of the current month, because the sentence above the chart gives it. With more than 14 months, put `minor` on every value, because a value is then wider than its bar. For more than 24 months, group the months into quarters.

## Current and projected periods

The current month shows its actual value to date in solid and its projected rest in hatch on top. Its label is "Nov to date". Each projected month is hatched, with a "~" before its value.
