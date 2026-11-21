# Leaderboard

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member compares many records by their rank in one number, and then opens one record.
Row opens: on the record's own page. Each row of the source is a link to the page of its record. That page has its own pattern, `content/product-page`.
Related: `content/fact-cards` has the same head above cards. `content/sort-heads` has one column for each number, and the head of a column sorts. `content/ranked-groups` ranks groups of records. `content/product-page` is the page that a row opens.

## States

- `table`: The head is the head of `content/fact-cards`: the title, a search field, the metric switch, the filters Stage, Lead and Users in a week, and one button. The metric switch and the filters are a side column at 1024 px and up, and a Filters button opens them in a sheet below 1024 px. That button names the chosen metric, such as "Filters, MRR". The metric switch has the options MRR, Revenue and Users, and MRR is the first choice. The switch is the one control for the number and the order: the last column shows the chosen metric, and the row with the largest number is first. No box is around the table. Each row shows the rank, the avatar and the name of the record, 2 values and the number of the chosen metric. The value that names a person has the avatar of that person. A filter keeps this state, and the rank counts from 1 in the rows that match. Opens on: the page load, or a choice of MRR in the switch.
- `metric-changed`: the same table with a different metric. The head of the last column names that metric, and the row with the largest number is first. Opens on: a choice of Revenue or Users in the metric switch. The source shows this change after a choice in the option list of its select button. The owner asked for the metric switch as the one control, so the sketch has the switch and no select button.
- `no-match`: the head stays. One line, one hint and one button that clears the search or the filters take the place of the table. Opens on: words in the search field or a filter that no record matches. The source shows no such state.
- `filters-open`: the sheet of `content/fact-cards` with the metric switch and the filters, over the table that the member has. It shows below 1024 px. At 1024 px and up, the metric switch and the filters are in the side column, and this state shows the table with no sheet. Opens on: a press on the Filters button. The source shows no such state.
- `product-page`: a link back to the table, and one plain box. The box names the record and the pattern `content/product-page`, which draws the page. Opens on: a click on a row.

## Transitions

The agent read the value of the table with `orca eval` and `document.getAnimations()`, after a choice of a number in the select button of the source. In the sketch, a choice in the metric switch plays that value. The agent read the value of a row from the style of the row. The option list of the source plays an animation of 150 ms. The sketch has no option list, so `transitions.json` does not have that value.

- `table` to `metric-changed`. Trigger: choose Revenue or Users in the metric switch. Moves: the table plays the animation `opacity`, from clear to solid. 250 ms, ease-in-out. measured.
- `metric-changed` to `table`. Trigger: choose MRR in the metric switch. Moves: the table plays the same animation. 250 ms, ease-in-out. measured.
- `table` to `table`. Trigger: the pointer goes over a row. Moves: the background of the row changes. 150 ms, cubic-bezier(0.4, 0, 0.2, 1). measured.
- `table` or `metric-changed` to `no-match`. Trigger: type in the search field, or set a filter. Moves: the sketch shows the line at once. 0 ms, none. estimated. The source has no such state.
- `table`, `metric-changed` or `no-match` to `filters-open`, and back. Trigger: press the Filters button, and then close the sheet. Moves: the sketch shows and hides the sheet at once. 0 ms, none. estimated. The source has no such state.
- `table` or `metric-changed` to `product-page`. Trigger: click a row. Moves: the sketch shows the plain box at once. 0 ms, none. estimated. The source loads a new page.

## Hard cases

- 1280 px screen: the side column is 232 px wide, and the table is 811 px wide. The head row of the table is 40 px high, and each row is 53 px high with a line below it.
- 1024 px screen: the side column stays, and the table is 728 px wide.
- 768 px screen: the table of the source is 758 px wide in a box of 671 px, so it scrolls sideways. The table of the sketch is 736 px wide, and it fits. The head is one row with the Filters button.
- 390 px screen: the table of the source keeps a width of 676 px, and it scrolls sideways in its box. The first 2 columns get narrower. The sketch does the same with a table of 676 px below the head, and the keyboard can scroll the table. The title and the search field are the first row of the head, and the Filters button and the button of the head are the second row. The number column is out of view until the member scrolls the table, and the Filters button names the metric.
- Many records: the source showed 100 rows on one page. An earlier capture showed 25 rows and a button for more rows. The sketch has 16 rows and no such button.
- Long name: not seen. The sketch cuts a long name with an ellipsis on one line, and the avatar keeps its size.
- No picture: a row of the source shows the logo of the company, or the first letter of its name in a box. The sketch shows 2 letters of the name in each avatar.
- No number: not seen. In the sketch, a product with no users has no MRR and no revenue. Its cell says "$0" or "0", and its row is last.
- Search: the search field of the source opens a list of results below the field. With no result, the list has one line and a link to the search page. In the sketch, the words filter the rows.
- Keyboard: in the sketch, the arrow keys change the metric in the switch, and the focus stays on the chosen option. The capture did not read the focus of the source.
- Slow network and failed load: not seen.

## Notes

  - the large head with its lines, the sponsor cards at the 2 sides, and the logos;
  - the second line of a row, and the 2 select buttons. One chooses the number, and one chooses a period.
- A row of the source has 2 small pictures: the logo of the company before its name, and the photo of the founder before the name of the founder. So a row has a square avatar for the product and a round avatar for the lead.
- The source has the columns Startup, Founder, MRR and MoM Growth. A choice in its select button changes the head of a number column and the order of the rows. The sketch shows the columns of the use case: Product, Stage, Lead and the number of the chosen metric.
- The second select button of the source is on only for one of its numbers. A product that needs a period can add a select button for it in the head.
- The source has no filter for its table. The owner asked for the head of the cards screen above the table. So the search field, the metric switch, the 3 filters, the sheet and `no-match` come from `content/fact-cards`, with no change.
- The source has a select button with an option list for the number. The owner asked for a metric switch in the head of the cards and the tables, and then for the switch as the one control here. So the sketch has no select button, and this pattern does not have the states of the option list and of a second number. A product with more numbers than one row of options can hold needs a select button.
- The source has its table in a box with a title, and the select button is in that box. The owner asked for no box around the table. So the sketch has no box and no second title.
- Keep these parts when the look changes: the rank is the first column, one control names the number that gives the rank, and the whole row is one link.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
