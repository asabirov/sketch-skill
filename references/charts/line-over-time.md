# Chart: Line over time

Template: `templates/chart/line-over-time.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The reader follows one level over time, such as a cash balance, active users or a price.
- The shape of the change matters more than the size of each value.
- The periods are many and even, such as months or weeks.
- The level has a limit that the reader watches, such as a minimum cash level. Draw it as a `sketch-ref` line.

## When not to use it

- Each value is a total of its period, such as revenue of a month. Use the monthly bars.
- The chart has fewer than 4 periods. Write the values as text.
- The chart has more than 3 lines. Draw small charts side by side, one for each line.
- Two lines have different units. Draw two charts.

## Many periods

Up to 24 months fit at 390 px. The line has no point at each month, so more months only make it denser. From 600 px, each month has a label. Below 600 px, only the first month and today keep a label, and the first label has its year, such as "Dec 2025". The dashed line and the key show the projected months. For more than 24 months, show quarters.

## Current and projected periods

The summary above the chart gives the level today, such as "Today, 21 November: €131k", in the largest type. Beside it are the money in and the money out of the current month so far. The actual line has a wash below it and ends at today with a filled point. The projected part continues as a dashed line with no wash to the last projected month. Its end point is open and has its value as a direct label, with a "~" before it. The period label of today is "Nov today".

A line can start its axis above zero. Then write the lowest value on the lowest grid line, such as "80k".
