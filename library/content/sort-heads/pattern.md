# Sort heads

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member compares 2 or more numbers of many records at the same time, and then opens one record.
Row opens: on the record's own page. A row of the source opens the cards of a category. In the sketch, a row opens the page of a product, which has its own pattern, `content/product-page`. This is the designer's choice.
Related: `content/fact-cards` has the same head above cards. `content/leaderboard` shows one number, and the metric switch chooses it. `content/ranked-groups` ranks groups of records. `content/product-page` is the page that a row opens.

## States

- `table`: The head is the head of `content/fact-cards`: the title, a search field, the metric switch, the filters Stage, Lead and Users in a week, and one button. The metric switch and the filters are a side column at 1024 px and up, and a Filters button opens them in a sheet below 1024 px. That button names the chosen metric, such as "Filters, MRR". The metric switch has the options MRR, Revenue and Users, and MRR is the first choice. A title is above the table, and no box is around them. Each row shows the rank, the avatar and the name of the record, one value, and one column for each number of the chosen metric: the metric, its new amount in a week and its growth in a week. The head of a number column is a button. A mark in the head shows the direction of the order, and the numbers of that column are bold. A filter keeps this state. Opens on: the page load, or a choice of MRR in the switch while the first number gives the order.
- `sorted`: the same table in the order of a different number, or in the reverse order. The first click on a head puts the largest number first, and a second click turns the order round. The rank counts from 1 in each order. A choice in the metric switch keeps this state, the column and the direction. Opens on: a click on the head of a number column.
- `metric-changed`: the same table with the 3 numbers of a different metric. The heads of the number columns name that metric, and the row with the largest first number is first. Opens on: a choice of Revenue or Users in the metric switch, while the first number gives the order. The source shows no such state. Its Average and Median switch is not in the sketch. The owner asked for the metric switch, so it is the designer's drawing.
- `no-match`: the head and the title stay. One line, one hint and one button that clears the search or the filters take the place of the table. Opens on: words in the search field or a filter that no record matches. The source shows no such state.
- `filters-open`: the sheet of `content/fact-cards` with the metric switch and the filters, over the table that the member has. It shows below 1024 px. At 1024 px and up, the metric switch and the filters are in the side column, and this state shows the table with no sheet. Opens on: a press on the Filters button. The source shows no such state.
- `product-page`: a link back to the table, and one plain box. The box names the record and the pattern `content/product-page`, which draws the page. Opens on: a click on a row.

## Transitions

The agent read `document.getAnimations()` with `orca eval` after a click on a head, and it returned nothing. So `transitions.json` has no value.

- `table` to `sorted`, and back. Trigger: click the head of a number column. Moves: the rows change at once. 0 ms, none. measured.
- `table` to `metric-changed`, and back. Trigger: choose a metric in the switch. Moves: the rows change at once. 0 ms, none. estimated. The source has no such state.
- `table`, `sorted` or `metric-changed` to `no-match`. Trigger: type in the search field, or set a filter. Moves: the sketch shows the line at once. 0 ms, none. estimated. The source has no such state.
- `table`, `sorted`, `metric-changed` or `no-match` to `filters-open`, and back. Trigger: press the Filters button, and then close the sheet. Moves: the sketch shows and hides the sheet at once. 0 ms, none. estimated. The source has no such state.
- `table`, `sorted` or `metric-changed` to `product-page`. Trigger: click a row. Moves: the sketch shows the plain box at once. 0 ms, none. estimated. The source loads a new page.

## Hard cases

- 1280 px screen: the side column is 232 px wide, and the table is 811 px wide. The head row of the table is 45 px high, and each row is 49 px high.
- 1024 px screen: the side column stays, and the table is 728 px wide.
- 768 px screen: the table is 736 px wide, and it fits. The head is one row with the Filters button.
- 390 px screen: the table of the source is 562 px wide, and it scrolls sideways in its box. A click on a head scrolls the table to that head. The table of the sketch is 672 px wide. It scrolls sideways below its title, and the keyboard can scroll it. The title and the search field are the first row of the head, and the Filters button and the button of the head are the second row.
- Many records: the source has 10 rows. The sketch has 16 rows.
- Long name: not seen. The sketch cuts a long name with an ellipsis on one line, and the avatar keeps its size.
- No picture: a row of the source shows an icon in a box before the name. The sketch shows 2 letters of the name in a square avatar.
- No number: not seen. In the sketch, a product with no users has no MRR, no revenue and no growth. An amount cell of its row says "$0" or "0", and the order uses it as the number 0. So its row is last when the largest amount is first, and first in the reverse order. Its growth cell says "None". In the order of the growth, its row is last in the 2 directions.
- Slow network and failed load: not seen.

## Notes

- The pattern holds only the parts that a table with sort heads needs. The sketch leaves out the medals of the first 3 rows and the Average and Median switch of the source.
- The rows of the source have no column for a person. So a row has only the avatar of its record. The Lead filter of the head keeps the rows of one lead.
- The source has no filter for its table. The owner asked for the head of the cards screen above the table. So the search field, the metric switch, the 3 filters, the sheet and `no-match` come from `content/fact-cards`, with no change. The owner asked for the metric switch. It chooses the metric of the 3 number columns. A column head sets the order, so the head has no control for the order.
- The source has its table in a box with a title. The owner asked for no box around the table. The title stays above the table, because it names the week for the short column heads.
- The sketch plays no value on a row. The capture did not read a row of this source.
- Keep these parts when the look changes: the rank is the first column, the head of a number column is the sort control, a mark shows the direction, and the whole row is one link.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
