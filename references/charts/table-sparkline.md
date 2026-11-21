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

Each sparkline holds 11 complete months, the current month and one projected month in a fixed width: 120 px, or 80 px below 600 px. It never gets an axis or a scroll bar. For a longer history, open the chart of the row. The header of the trend column names its period, such as "Trend, Dec 2025 to Dec 2026", or "Dec to Dec" below 600 px. The table has the class `sketch-data`, so it keeps its headers below 600 px. Less important columns, such as "Dec proj.", hide with `sketch-from-tablet`. A long client name wraps.

## Current and projected periods

The value column gives the value to date in bold, such as "€9k", and the projected total of the month below it, such as "of €15k proj.". The trend cell gives the change against the earlier month at the same day, such as "+7%", above the sparkline. The solid line holds the complete months, with a wash below it. The dashed line goes to the projected value of the current month, then to the projected next month. The `aria-label` of each sparkline gives every value, because a data table for each row does not fit the row.
