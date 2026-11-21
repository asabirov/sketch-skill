# Chart: Sparkline in a table row

Template: `templates/chart/table-sparkline.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- Each row of a table needs its own trend next to its numbers, such as revenue by client or usage by plan.
- The reader needs the direction and the shape of each trend, not the value of each month.

## When not to use it

- The reader must read the value of a month. Show the numbers in columns, or open a full chart for the row.
- The rows must be compared on one scale. Each sparkline has its own scale. Use the monthly bars for each row, or one chart with the rows as lines.
- The table has more than about 20 rows. The trends become noise. Sort the table and show the sparkline only on the top rows.

## Many periods

Each sparkline holds 11 complete months, the current month and one projected month in a fixed width of 120 px. It never gets an axis or a scroll bar. For a longer history, open the chart of the row. Below 600 px, the table rows wrap, and less important columns hide with `sketch-from-tablet`. The headers hide too, so each value that stays gets its header as a `sketch-phone-only` label.

## Current and projected periods

The solid line holds the complete months. The dashed line goes to the projected value of the current month, then to the projected next month. The columns next to the sparkline give the value to date and the 2 projected values. The `aria-label` of each sparkline gives every value, because a data table for each row does not fit the row. The change column "vs. Oct, same day" compares the value to date with the earlier month at the same day.
