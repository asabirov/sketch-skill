# Product page

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member reads the main numbers of one record, then the course of one number, and then the facts.
Row opens: no rows. The cards of other records at the end of the page are a part of the pattern `content/fact-cards`.
Related: `content/fact-cards`, `content/wide-grid`, `content/kanban`, `content/leaderboard`, `content/sort-heads` and `content/ranked-groups` open this page from a card or a row. Each of them shows a plain box with the name of this pattern.

## States

- `product-page`: the page of one record. A path at the top leads back to the list. The head has a picture, the name, a text and 2 buttons. Below it are 4 number cards, a chart in a box, a group of facts, a large picture, a note of the lead, and a part for other records. That part has a heading, a "View all" link and one plain box, which names the pattern `content/fact-cards`. Opens on: the page load.
- `period-menu`: the option list of the period, below the select of the chart. The chosen option has a fill. Opens on: a click on the select.
- `period-changed`: the same page with the chart of a different period. The select names the period, and the sum above the chart is the sum of that period. Opens on: a choice in the option list.
- `compare-off`: the chart shows only the line of the period. The dashed line of the period before does not show, and the switch below the chart is off. Opens on: a click on the switch.
- `chart-point`: the chart shows a vertical guide, one mark on each line, and a box. The box has the name of the number, and one row with the date and the value for each line. Opens on: the pointer or the focus on the chart.
- `picture-open`: a dialog over the page shows the full picture and a close button. The picture scrolls in the dialog. Opens on: a click on the large picture.

## Transitions

The agent ran `python3 scripts/capture.py record` on the page of the company, with one step for each state.

- `product-page` to `period-menu`. Trigger: click the select of the period. Moves: the option list plays the animation `enter`. 150 ms, ease. measured. The capture read the name, the duration and the easing of the animation, not its frames. The sketch draws it from clear to solid, and from 95% of its size.
- `period-menu` to `period-changed`. Trigger: choose a period. Moves: the chart goes from clear to solid. 280 ms, cubic-bezier(0.22, 1, 0.36, 1). measured.
- `period-menu` to `product-page`. Trigger: choose the first period. Moves: the chart plays the same change. 280 ms, cubic-bezier(0.22, 1, 0.36, 1). measured.
- `product-page` to `compare-off`, and back. Trigger: click the switch. Moves: the switch changes its fill. 150 ms, cubic-bezier(0.4, 0, 0.2, 1). measured. Then the chart goes from clear to solid. 280 ms, cubic-bezier(0.22, 1, 0.36, 1). measured.
- `product-page` to `chart-point`. Trigger: the pointer goes over the chart. Moves: the box shows at once. When the pointer goes to a different point, the box moves to that point. 400 ms, ease. measured.
- `product-page` to `picture-open`. Trigger: click the large picture. Moves: the dialog plays the animation `enter`. 200 ms, ease. measured.
- `picture-open` to `product-page`. Trigger: press Escape, or click the close button. Moves: the sketch closes the dialog at once. 0 ms, none. estimated. The dialog of the source plays the animation `exit` in 200 ms, and the sketch does not play it.
- `period-menu` to the page. Trigger: press Escape, or click outside the option list. Moves: the sketch closes the option list at once. 0 ms, none. estimated. The capture did not read how the option list closes.

## Hard cases

- 1280 px screen: the column is 811 px wide. The buttons of the head are at the right of the name. The 4 number cards are in one row, and the facts are in 2 columns.
- 768 px screen: the number cards are in 2 rows of 2 cards. The facts stay in 2 columns.
- 390 px screen: each part is in 1 column. The buttons of the head go below the text. The chart keeps the select above it, and the box of a point stays in the chart: it goes to the left of the point when the right has no room.
- Long name: the source cuts the name of the person in a number card with an ellipsis. The sketch puts the name on 2 lines.
- Record with no number: a number card of the source shows a dash and one line that gives the reason. The source shows no chart with no number. The sketch does not draw this case.
- Period with no period before: for "All time", the source turns the switch off, and the switch does not work. The change text and the dashed line do not show. The sketch does the same.
- Options that need an account: 5 of the 7 periods of the source have a lock, and each opens a dialog for a new account. The sketch has 4 periods, and each one works.
- Other records: the source shows 6 cards of other records, in 3 columns at 1280 px and at 768 px. The sketch shows one plain box for them.
- Keyboard: Escape closes the option list and the dialog. In the sketch, the focus then goes back to the select or to the large picture. In the sketch, the arrow keys move through the points of the chart. The capture did not read the focus or the keys of the source.
- Slow load: the source shows grey boxes that pulse in place of the chart and the picture. The sketch shows each part at once.
- Failed load: not seen.

## Notes

  - the bar at the top with the price and its 3 buttons, the locks and the dialog for a new account;
  - the select of the number, the "Trend view" switch and the select of the chart style, because the period select shows the same control;
  - the line about the check of the numbers, the box with 2 ratings that change places, the flag, the 2 lines about the affiliate program, and the foot of the site.
- The page follows the page of one company: the same parts in the same order. Its job: a buyer reads the main numbers first, then the course of one number, and then the facts. Why the layout serves the job: the 4 number cards are above the chart, so the buyer has the totals before the detail. The chart has its controls in its own box, so a change of the period changes only that box.
- The facts, the texts and the note of the page are sample content of one sample product. A product puts its own facts in the same cells.
- The cards of other records are a part of the pattern `content/fact-cards`. So the page draws one plain box for them, with the name of that pattern. Put cards of that pattern in the box.
- The path and the "View all" link lead to a list of records. The link of the source leads to the list of all companies for sale. In the sketch, each of the 2 links shows only a short message, because the list has its own pattern.
- Keep these parts when the look changes: the number cards are above the chart, and the period select is in the box of the chart.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
