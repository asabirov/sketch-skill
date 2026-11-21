# Chart: Stat with a small trend

Template: `templates/chart/stat-trend.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The first row of a report shows 2 to 4 key numbers, such as revenue, costs and margin.
- Each number needs its recent direction, not its full history.

## When not to use it

- The reader must compare the months. Use the monthly bars below the stats.
- A number has no history, such as a count of open tickets now. Show the number and its change only.
- The page has more than 4 key numbers. Choose the 4 that drive a decision, and put the rest in a table.

## Many periods

Each small trend holds 6 complete months, the current month and one projected month. It has labels only at its first and last period, so it fits a card of any width. A level, such as a cash balance, uses a sparkline in place of bars. For a longer trend, open the full chart.

## Current and projected periods

The big number is the value to date of the current period, with "of €57k projected" beside it. The change compares the value to date with the earlier period at the same day, such as "vs. October at day 21". In the small bars, the current month is solid to date with a hatched rest, and the projected month is hatched.
