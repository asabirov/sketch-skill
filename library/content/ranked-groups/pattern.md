# Ranked groups

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member compares groups of records by one number first, and then wants the best records of each group.
Row opens: on the record's own page. Each record of the source is a link to the page of that record. That page has its own pattern, `content/product-page`.
Related: `content/fact-cards` has the same head above cards. `content/leaderboard` ranks the records in one table. `content/sort-heads` has one column for each number. `content/wide-grid` draws the page of one group. `content/product-page` is the page that a record opens.

## States

- `groups`: The head is the head of `content/fact-cards`: the title, a search field, the metric switch, the filters Stage, Lead and Users in a week, and one button. The metric switch and the filters are a side column at 1024 px and up, and a Filters button opens them in a sheet below 1024 px. That button names the chosen metric, such as "Filters, MRR". The metric switch has the options MRR, Revenue and Users, and MRR is the first choice. A heading names the chosen metric. Each group is one box, and the boxes are in the order of their number. The head of a box shows the rank, the name and the number of the group. Below the head are its 5 best records, each with its avatar at the left and its number at the right. Opens on: the page load, or a choice of MRR in the switch.
- `metric-changed`: the same boxes with a different metric. The heading names that metric. The number of a group is the sum of that metric of its products, and the boxes and their records are in the order of that number. Opens on: a choice of Revenue or Users in the metric switch. The source shows no such state: it has one fixed number. The owner asked for the switch, so it is the designer's drawing.
- `no-match`: the head and the heading stay. One line, one hint and one button that clears the search or the filters take the place of the boxes. Opens on: words in the search field or a filter that no record matches. The source shows no such state.
- `filters-open`: the sheet of `content/fact-cards` with the metric switch and the filters, over the groups that the member has. It shows below 1024 px. At 1024 px and up, the metric switch and the filters are in the side column, and this state shows the groups with no sheet. Opens on: a press on the Filters button. The source shows no such state.
- `product-page`: a link back to the groups, and one plain box. The box names the record and the pattern `content/product-page`, which draws the page. Opens on: a click on a record.

## Transitions

`transitions.json` has no value. The source has no control that changes the boxes, and the capture did not read a record of this source.

- `groups` to `metric-changed`, and back. Trigger: choose a metric in the switch. Moves: the numbers and the order change at once. 0 ms, none. estimated. The source has no such state.
- `groups` or `metric-changed` to `no-match`. Trigger: type in the search field, or set a filter. Moves: the sketch shows the line at once. 0 ms, none. estimated. The source has no such state.
- `groups`, `metric-changed` or `no-match` to `filters-open`, and back. Trigger: press the Filters button, and then close the sheet. Moves: the sketch shows and hides the sheet at once. 0 ms, none. estimated. The source has no such state.
- `groups` or `metric-changed` to `product-page`. Trigger: click a record. Moves: the sketch shows the plain box at once. 0 ms, none. estimated. The source loads a new page.

## Hard cases

- 1280 px and 1024 px screen: the side column is 232 px wide, and each box is 576 px wide. The space between 2 boxes is 12 px.
- 768 px screen: the column is 576 px wide, and the head and each box have this width. The head is one row with the Filters button.
- 390 px screen: the head and each box are 358 px wide. The title and the search field are the first row of the head, and the Filters button and the button of the head are the second row.
- Long name: not seen. The sketch cuts a long name with an ellipsis on one line, and the avatar keeps its size.
- Many groups: the source has 112 boxes. The sketch has 4 boxes, one for each stage that has products.
- Group with fewer than 5 records: the box shows the records that it has.
- No picture: a record of the source shows the logo of the company. The sketch shows 2 letters of the name in a square avatar.
- Search and filters: in the sketch, a search or a filter keeps the rank and the number of each group, and it hides a group with no match. The source has no search on this page.
- Slow network and failed load: not seen.

## Notes

- The pattern holds only the parts that ranked groups need. The sketch leaves out the flags, the count of records and the share of each record of the source.
- The source has one fixed number, and no control chooses it. The owner asked for a metric switch in the head of the cards and the tables, so the switch chooses the number here. In the sketch, the number of a stage is the sum of the chosen metric of its products.
- In the source, the name of a group opens the cards of that group. In the sketch, the name is not a link. The pattern `content/wide-grid` draws the page of one group.
- The source has no filter. The owner asked for the head of the cards screen above ranked rows. So the search field, the metric switch, the 3 filters, the sheet and `no-match` come from `content/fact-cards`, with no change. The source has one fixed order, so the head has no control for the order.
- The owner asked for no box around a table. Each group keeps its box, because the box is the group: it holds the rank, the name and the number of the group with its records. No box is around all groups.
- The sketch plays no value on a record. The capture did not read a record of this source.
- Keep these parts when the look changes: the rank and the number of a group are in the head of its box, the best records are below the head, and each record is one link.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
