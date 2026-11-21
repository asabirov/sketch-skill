# Kanban

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member compares the groups of its records, such as the stages, and then opens one record.
Row opens: on the record's own page. Each small card of the source is a link to the page of its record. That page has its own pattern, `content/product-page`.
Related: `content/fact-cards` has the same head above a grid of larger cards. `content/wide-grid` is the page of one group, with no filters. `content/leaderboard`, `content/sort-heads` and `content/ranked-groups` have the same head above ranked rows. `content/product-page` is the page that a card opens. `sheets/bottom-sheet` has the motion and the drag of a sheet.

## States

- `board`: The head is the head of `content/fact-cards`: the title, a search field, the metric switch, the filters Stage, Lead and Users in a week, and one button. The metric switch and the filters are a side column at 1024 px and up, and a Filters button opens them in a sheet below 1024 px. That button names the chosen metric, such as "Filters, MRR". The metric switch has the options MRR, Revenue and Users, and MRR is the first choice. The board has one column for each group, and the columns are side by side. A column has the name of its group, the count of its cards, and its cards one below the other. A card has the name of the record, the avatar and the name of the lead, the number of the chosen metric and the growth of that metric. The card with the largest number is first in its column. A search or a filter keeps this state: it changes the cards and the counts, and each column stays. Opens on: the page load, or a choice of MRR in the switch. The source shows each group as one row of small cards that scrolls sideways. The owner asked for a kanban view, so the columns are the designer's drawing.
- `metric-changed`: the same board with a different metric. The first number of each card is that metric with its name, the second number is the growth of that metric, and each column is in the order of that metric. Opens on: a choice of Revenue or Users in the metric switch. The source shows no such state. The owner asked for the switch, so it is the designer's drawing.
- `no-match`: the head stays. One line, one hint and one button that clears the search or the filters take the place of the board. Opens on: words in the search field or a filter that no record matches. The source shows no such state.
- `filters-open`: the sheet of `content/fact-cards` with the metric switch and the filters, over the board that the member has. It shows below 1024 px. At 1024 px and up, the metric switch and the filters are in the side column, and this state shows the board with no sheet. Opens on: a press on the Filters button. The source shows no such state.
- `product-page`: a link back to the board, and one plain box. The box names the record and the pattern `content/product-page`, which draws the page. Opens on: a click on a card.

## Transitions

The agent did not read a value on a small card of the first page. The agent read the value of the border on a card of `/acquire` with `orca eval`.

- `board` to `board`. Trigger: the pointer goes over a card. Moves: the border of the card goes from grey to ink. 150 ms, cubic-bezier(0.4, 0, 0.2, 1). estimated.
- `board` to `board`. Trigger: scroll the board sideways below 768 px. Moves: the board stops with a column at its left edge. The snap is the scroll of the browser, so it has no value. estimated. The source has no board.
- `board` to `metric-changed`, and back. Trigger: choose a metric in the switch. Moves: the numbers and the order change at once. 0 ms, none. estimated. The source has no such state.
- `board` or `metric-changed` to `no-match`. Trigger: type in the search field, or set a filter. Moves: the sketch shows the line at once. 0 ms, none. estimated. The source has no such state.
- `board`, `metric-changed` or `no-match` to `filters-open`, and back. Trigger: press the Filters button, and then close the sheet. Moves: the sketch shows and hides the sheet at once. 0 ms, none. estimated. The source has no such state.
- `board` or `metric-changed` to `product-page`. Trigger: click a card. Moves: the sketch shows the plain box at once. 0 ms, none. estimated. The source loads a new page.

## Hard cases

- 1280 px screen: the side column is 232 px wide, and the board is 984 px wide. Each of the 5 columns is 187 px wide. The board is 1136 px wide at most, and a column is then 218 px wide.
- 1024 px screen: the side column stays, and the board is 728 px wide. Each column is 136 px wide. A card shows the 2 numbers with their names, and a long name of a lead is cut.
- 768 px screen: the head is one row with the Filters button. The 5 columns fit, and each is 138 px wide.
- 390 px screen: the board scrolls sideways with a snap, and the page does not. A column is 294 px wide, and 58 px of the next column are in view. Below 768 px, a column is 82% of the board and 300 px at most. So from 644 px to 767 px, 2 columns and a part of the third column are in view. A change of the metric or of a filter keeps the column that the member scrolled to.
- More groups than fit: a column is 136 px wide or more. With more than 5 columns at 768 px or at 1024 px, the board scrolls sideways.
- Group with no record: the column stays, with the count 0 and the line "No products". With a search or a filter, the line is "No match".
- Group with many records: the column gets longer, and the page scrolls. The sketch has 5 cards at most in a column.
- Long name: the sketch shows 2 lines of the name of a product, and then cuts it with an ellipsis. It cuts the name of a lead on one line.
- No number: a product with no users has no MRR and no revenue. Its card says "$0" or "0", its growth says "None", and it is last in its column.
- Keyboard: the arrow keys change the metric in the switch, and the focus stays on the chosen option. Each card is a link, and the Tab key goes down one column and then to the next column. Below 768 px, the focus on a card scrolls the board, so the card is in view. After the page of a record, the focus goes back to its card.
- Slow network and failed load: not seen.

## Notes

- The pattern holds only the parts that a board of columns needs. The sketch leaves out the large head, the sponsor cards at the 2 sides, the logos and the table of the source. The table has its own pattern, `content/leaderboard`.
- The board has no drag of a card from one column to a different column. The owner asked for a view, and the source has no such action. A product that lets a member move a record needs its own states for the drag.
- The owner asked for the same head on the cards and the tables. So the board has the head of `content/fact-cards`, with the side column, the Filters sheet and the metric switch. The Stage filter keeps each column: the columns of the other stages show "No match".
- The source has a "View all" link at the end of each row. A column shows each card of its group, so the board has no such link and no state for one group.
- A card has no picture, no words about the product and no review date. A column is 136 px wide at 768 px and at 1024 px, and these parts do not fit. The card of `content/fact-cards` has them.
- The avatar and the name of the lead on a card are the owner's choice. The capture did not record a person on a small card of the source. The owner asked for a smaller lead. So the avatar is 24 px, and the name is in smaller and quieter text than the name of the product.
- The count of a column is the number of its cards, after the search and the filters. It is not a sum of the metric. `content/ranked-groups` shows the sum of a metric for each group.
- On a wide screen, the page is wider than the page of `content/fact-cards`. The board is 1136 px wide at most, and the cards of that pattern are 811 px wide at most. A column is then 218 px wide, and not 153 px.
- Keep these parts when the look changes: one column for each group with its name and its count, the order of the chosen metric in each column, the snap below 768 px with a part of the next column in view, and the focus goes back to the card after the page of the record.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
