# Cash flow chart

Captured: 2026-11-25, recorded by an agent
Best for: a report that shows whether each month or quarter earned or burned money, and how the money in and the money out moved.
Row opens: no rows.
Related: `analytics/filter-bar` sets the range and the direction. `analytics/flow-chart` shows where the money came from and went. `analytics/breakdown-table` splits the same totals by source or category. `analytics/balance-card` shows the total of today.

## Scenarios

- See at one look whether each month earned or burned money.
- Compare how the money in and the money out moved over the range.
- See how large the main category of the money out is in each period.
- Group the periods by month or by quarter.
- Read the exact values of one period.
- See only the money in, or only the money out, when the filter bar asks for it.

## States

- `overview`: the totals of the range: the net cash flow (largest), the money in and the money out. Below them, a group button (Month) and a switch with Overview, Lines and By category. In the chart, money in is a bar up from the zero line, money out is a bar down, and the net cash flow is a line with points over the bars. The values stand in a margin at the left. A key names each mark. Opens on: the address of the page.
- `hover`: the period gets a ground, and a dark tooltip gives its money in, money out and net. Opens on: the pointer on a period.
- `line`: money in is a solid line with round points, and money out is a dashed line with square points, both from zero. Opens on: Lines in the switch.
- `by-category`: the money out of each period as one bar from zero, split into the largest category and everything else, with the total above the bar. Opens on: By category in the switch.
- `group-menu`: a menu below the group button with Month and Quarter. The chosen item has a check mark. Opens on: a click on the group button.
- `quarter`: one column for each quarter. The totals rise into place again. Opens on: Quarter in the group menu.
- `money-in-only`: the totals show only the money in, and the chart shows only the bars up. Opens on: Money in in the direction popover of `analytics/filter-bar`.
- `loading`: the net total and the chart are pulsing blocks. Opens on: a new range, a new grouping or the first load.
- `empty`: the totals are €0, and the chart area has one line of text and a way to the last 12 months. The source shows a "No data" tooltip on a month without data, and no empty block. Opens on: a range without money in or out.

## Transitions

- `overview` to `line` or `by-category`, and back to `overview`. Trigger: a click in the switch. Moves: the new chart fades in (opacity). 300 ms, ease-out. measured. On the overview and the line views, each point grows from nothing (scale) in 160 ms, ease-out, with a delay of about 153 ms more for each point. measured.
- `overview` to `hover`. Trigger: the pointer on a period. Moves: nothing. The ground and the tooltip show at once. measured.
- `overview` to `group-menu`. Trigger: a click on the group button. Moves: the menu fades in and grows (opacity and scale). 150 ms, cubic-bezier(0.4, 0, 0.2, 1). Measured duration and easing. The start scale of 0.96 is estimated.
- `group-menu` to `quarter`. Trigger: Quarter. Moves: while the new values load, a block pulses (opacity), 1000 ms, ease. measured. Then the totals rise into place (opacity and position), 200 ms, ease-out. measured.
- A change of width. Trigger: the window or the column gets wider or narrower. Moves: nothing. The chart draws again at the new width at once. The designer chose it. estimated.

## Hard cases

- Every view, loading and empty keep the same chart height, so the page below the chart does not jump.
- Negative net: the net line goes below the zero line, and the total has a minus sign.
- One period far larger than the others: the value axis keeps 3 grid lines, with the zero line in the middle, so the small periods stay flat. The tooltip gives their values.
- Many periods: a long range by month gives many thin bars. Offer Quarter for a range of more than 12 months.
- Group by quarter: the quarters hold the same money of the range as the months, so the totals do not change. A quarter that the range cuts names its part, such as "Q3 from 17 Aug". The scale grows to the largest quarter.
- Narrow screen: at 390 px the totals wrap, the group button and the switch stand on 2 lines, and the chart takes the full width.
- Touch screen: a tap on a period shows its tooltip. The bars and the points are not the targets. The whole period is.
- Colour: the source marks the series by colour. The sketch uses a filled bar and a lighter bar, a solid line and a dashed line, and round and square points, and names each in the key.

## Notes

- Money in above the zero line and money out below it, with the net as a line, answers "did this month earn or burn money" at one look.
- The chart draws at the real width of its column, so the points and the labels keep their shape at every width.
- The switch names the views in words. The source shows a switch with icons only.
- The source draws the category view with 5 categories in each bar. A sketch bar has at most 2 parts, so the sketch shows the largest category and everything else.
- Left out, because only the source has them: the colours of the series and the button that opens the chart full screen.
