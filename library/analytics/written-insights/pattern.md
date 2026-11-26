# Written insights

Captured: 2026-11-25, recorded by an agent
Best for: any page with data where a program writes its few most useful facts in plain sentences, next to a chart, a table or a list, for a reader who does not read the data.
Row opens: no rows.
Related: `analytics/cashflow-chart` shows the same data as a chart. `analytics/filter-bar` sets the range that the insights describe.

## Scenarios

- Get the main facts of a range without reading a chart.
- Read a fact that the data does not show at once, such as how long the cash lasts at the current burn.
- Go from a fact to the data behind it, such as all the payroll payments.
- Tell the product which insights help.
- Copy a fact into a message or a report.

## States

- `insights`: the heading Insights and the range. 3 insights, each with a short heading and 1 or 2 sentences with the numbers. A word that names a filter, such as Payroll, is a dotted link. Each insight has Helpful, Not helpful and Copy. A note below says that a program writes the insights and can make mistakes. Opens on: the address of the page.
- `feedback-given`: the chosen button has a ground, and a short line thanks the reader. Opens on: Helpful or Not helpful.
- `filter-link`: the range line names the new filter, and a toast confirms it. Opens on: a link in a insight.
- `loading`: pulsing lines in place of the insights. The note stays. Opens on: a new range or the first load.
- `empty`: one line that says there are no insights, and why. Opens on: a range without money in or out.
- `error`: one line that says the insights did not load and that the chart still shows the numbers, and Try again. Try again shows `loading`, then the insights. Opens on: the insights fail to load.

## Transitions

- `loading` to `insights`. Trigger: the insights arrive. Moves: each insight fades and rises 6 px (opacity and position). 200 ms, ease-out. The source page uses this duration and easing for its totals, measured. Its use for the insights and the 6 px rise are estimated.
- `loading`. Moves: the lines pulse (opacity), 1000 ms, ease. measured.
- `insights` to `feedback-given`. Trigger: Helpful or Not helpful. Moves: nothing. The ground and the line show at once. estimated.

## Hard cases

- A long insight: keep each insight at 2 sentences. Cut the rest, and do not add a "Read more".
- Fewer than 3 facts worth saying: show only those. Do not fill the column with weak insights.
- A number that the chart does not show: link it to the data that proves it, or leave it out.
- Narrow screen: at 390 px the column takes the full width below the chart, and the buttons stay in one row.
- Negative values use a real minus sign, and money has its currency.

## Notes

- The note about mistakes stays visible in every state that shows insights, not in a tooltip.
- The links in the text are real filters. A reader checks a claim in one click.
- The sketch uses a check mark and a cross for Helpful and Not helpful, because the kit has no thumb icons. The labels say the meaning.
- Left out, because only the source has them: the name of the source's writing program.
- The source shows trends about money. The pattern is general: the same block fits any data, such as sales, sign-ups or tickets.
