# Chart: Stat with a small trend

Template: `templates/chart/stat-trend.html`. The rules for every chart are in [../charts.md](../charts.md).

## When to use it

- The first row of a report shows 2 to 4 key numbers, such as revenue, costs, margin and cash.
- Each number needs its recent direction, not its full history.
- The reader picks one number to see its days in the current month.

## When not to use it

- The reader must compare the months. Use the monthly bars below the stats.
- A number has no history, such as a count of open tickets now. Show the number and its change only.
- The page has more than 4 key numbers. Choose the 4 that drive a decision, and put the rest in a table.
- The numbers do not need a chart of their days. Leave out the daily chart, and keep the tiles.

## Many periods

Each tile is a tab in a `sketch-tiles` row: 2 tiles in a row below 600 px, and 4 from 600 px. Each tile trend holds 6 complete months, the projected current month and the projected next month. It has no labels, so it fits a tile of any width. The daily chart below the tiles holds the 30 days of the current month, with labels only at the first day, today and the last day. For a longer trend, open the full chart.

## Current and projected periods

The tile value is the value to date of the current month. The change compares it with the earlier month at the same day, such as "vs. Oct 1 to 21". A level, such as a cash balance, compares with the end of the earlier month. In the tile trend, the complete months are solid with a wash below, and the projected months are dashed.

The chosen tile has a drawn frame and shows its panel. For a total, the panel has a `sketch-goal` meter: the value to date is solid, and the rest to the projected total is hatched. The daily chart shows the total so far, solid to today and dashed to the projected end of the month. A thin line shows the earlier month for comparison. For a level, the daily chart shows the level with no meter. Each daily chart gives every value in its `aria-label`. One `sketch-data` table below the panel gives screen readers every monthly value of every tile.
