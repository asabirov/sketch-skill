# Breakdown table with shares

Captured: 2026-11-25, recorded by an agent
Best for: a report that splits the money in and the money out of a range into their largest parts, with each part's share of the total.
Row opens: the transactions of that part, with the same range and direction.
Related: `analytics/flow-chart` shows the same parts as bands. `analytics/filter-bar` sets the range.

## Scenarios

- Find the largest sources of the money in, or the largest recipients of the money out.
- Switch the split to categories or to account codes for the books.
- See the share of each part at one look, without a calculation.
- Open the transactions behind one part.
- See the small parts that the top 3 leave out.

## States

- `by-source`: one panel with the direction (Money in), its total, and 2 switches: Money in or Money out, and Source, Category or Account code. The table shows the 3 largest parts. Each row has the name, the share with a meter, and the amount. A last row, "3 more", sums the rest. Opens on: the address of the page.
- `by-category`: the same panel split by category. Opens on: Category in the switch.
- `by-code`: the same panel split by account code. Opens on: Account code in the switch.
- `money-out`: the panel shows the money out, split by recipient. Opens on: Money out in the switch.
- `remaining-open`: every part of the list, and a "Show the top 3 only" row. Opens on: the "more" row.
- `loading`: a pulsing block. Opens on: a new range or the first load.
- `empty`: one line that says there is nothing to split, and why. Opens on: a range without money in or out.
- A row: a click opens the transactions of that part. The sketch shows a toast.

## Transitions

- `by-source` to `by-category` or `by-code`. Trigger: a click in the switch. Moves: the new rows fade in (opacity). 200 ms, ease-out. The source changes the rows at once. estimated.
- `loading`. Moves: the block pulses (opacity), 1000 ms, ease. The source pulses its chart with these values. Its use for the tables is estimated.
- `by-source` to `remaining-open`. Trigger: the "more" row. Moves: nothing. The rows show at once. estimated.

## Hard cases

- A long name: the name wraps to 2 lines, and the share and the amount stay on the first line of the row.
- One part takes almost all: its meter is nearly full, and the "more" row can show 1%. Keep it, so the shares add up to 100%.
- 4 parts or fewer: no "more" row. The table shows every part, because a "1 more" row hides one name for no gain.
- A part with a negative amount, such as a refund in the money out: show it with its sign, and leave its meter empty.
- Narrow screen: at 390 px the table header goes, and each row is the name, the share with a short meter, and the amount.
- Each direction keeps its own split. A change of the split for the money in does not change the split for the money out.

## Notes

- The share meter makes the size of each part clear without a chart.
- The "more" row keeps the table short, and its sum keeps the shares at 100%.
- One table with a switch of the direction keeps the block small. A page that must compare the money in and the money out side by side can show 2 of these blocks.
- Left out, because only the source has them: the names of the source's customers, suppliers and accounts.
