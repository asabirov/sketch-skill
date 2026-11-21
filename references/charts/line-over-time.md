# Chart: Line over time

Template: `templates/chart/line-over-time.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The reader follows one level over time, such as a cash balance, active users or a price.
- The shape of the change matters more than the size of each value.
- The periods are many and even, such as months or weeks.

## When not to use it

- Each value is a total of its period, such as revenue of a month. Use the monthly bars.
- The chart has fewer than 4 periods. Write the values as text.
- The chart has more than 3 lines. Draw small charts side by side, one for each line.
- Two lines have different units. Draw two charts.

## Many periods

Up to 24 months fit at 390 px. Below 600 px, only every third month counted back from the current month, and the last projected month, keep a label. For more than 24 months, show quarters.

## Current and projected periods

The actual line ends at today, with an open point and its value. The projected part continues as a dashed line to the last projected month, with a "~" before its value. The period label of today is "Nov today".

A line can start its axis above zero. Then write the lowest value on the lowest grid line, such as "80k".
