# Chart: Monthly bars

Template: `templates/chart/monthly-bars.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The reader compares a total of each month with the other months, such as revenue, costs or orders.
- Each value is a sum over the period, so a bar from zero shows its size.
- The values have one unit.
- The total has at most 2 parts that the reader must see, such as subscriptions and services.

## When not to use it

- The value is a level at a point in time, such as a cash balance or a count of active users. Use the line over time.
- The reader compares each month with a plan or a target. Use the bars with a line.
- The reader compares categories, such as products or countries, not periods. Draw horizontal bars with the category names on the left.
- The total has more than 2 parts. One ink cannot keep 3 parts apart. Show the total, and put the parts in a table or in small charts side by side.
- The reader compares the share of each part, not the total. Draw one line of the share over time.
- The chart has two series in different units. Draw two charts.
- The page shows only one number. Use the stat with a small trend.

## Many periods

Up to 24 months fit at 390 px. The bars get narrower, and each bar is at most 48 px wide. The bars have no value labels. Three grid lines on the left give the scale, so the chart does not need room for a label above each bar. From 600 px, each month has a label. Below 600 px, only the first month and the current month keep a label, and the first label has its year, such as "Dec 2025". The hatch and the key show the projected months. For more than 24 months, group the months into quarters.

## Current and projected periods

The summary above the chart gives the value to date, such as "November 1 to 21: €39k", and the projected total, such as "November, projected: ~€57k". Each value has its change against the same days of the earlier month. The current month is one bar: its 2 parts to date are solid, and its projected rest is hatched on top. Its label is "Nov to date". Each projected month is one hatched bar, not split. The key gives the total of each part since the first month, largest first. The data table gives screen readers each part and each total.
