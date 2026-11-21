# Fact cards

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member scans many records by their main numbers, and then opens one record.
Row opens: on the record's own page. Each card of the source is a link to the page of its record. That page has its own pattern, `content/product-page`.
Related: `content/wide-grid` is the page of one group, with no filters. `content/kanban` is one column of small cards for each group, with the same head. `content/leaderboard`, `content/sort-heads` and `content/ranked-groups` have the same head above ranked rows. `content/product-page` is the page that a card opens. `sheets/bottom-sheet` has the motion and the drag of a sheet.

## States

- `cards`: at 1024 px and up, the title, a search field, a metric switch and the filters Stage, Lead and Users in a week are a side column at the left. A sort select and one button are above the cards, at their right edge. Below 1024 px, the head is one row: the title, the search field, a Filters button, the sort select and the button. The Filters button names the chosen metric, such as "Filters, MRR". Each card shows a small picture, the name, the stage, 2 lines of words, the avatar and the name of the lead, and 3 numbers. The metric switch has the options MRR, Revenue and Users, and MRR is the first choice. The first number of a card is the chosen metric, and the card with the largest number is first. Opens on: the page load, a choice of MRR in the switch, or the "Clear" button of the filters while MRR is the metric.
- `filtered`: the same screen with only the cards that match. A "Clear" button shows after the filters while a filter has a value. Below 1024 px, the Filters button shows the count of the filters that have a value before the metric, such as "Filters (2), MRR". Opens on: a value in a filter, or words in the search field.
- `metric-changed`: the same screen with a different metric. The first number of each card is the chosen metric with its name, the second number is the growth of that metric, and the card with the largest number is first. The first option of the sort select names this order, and the member can choose a different order there. A filter keeps the chosen metric, and the "Clear" button does not change it. Below 1024 px, the switch is the first part of the sheet of `filters-open`, and the Filters button names the new metric. Opens on: a choice of Revenue or Users in the metric switch. The source shows no such state: the capture recorded no metric switch. The owner asked for the switch, so it is the designer's drawing.
- `no-match`: the head stays. A box takes the place of the cards. It has one line that says that no record matches, one hint, and one button that clears the filters or the search. Opens on: a filter or words that no record matches.
- `filters-open`: below 1024 px, a sheet at the bottom of the screen has the metric switch, the filters, a Close button, and one button that names the count of the cards that match. The screen behind the sheet is dimmed, and it takes no input. The cards behind the sheet change with each filter and with the metric. At 1024 px and up, the metric switch and the filters are in the side column, and this state shows the cards with no sheet. Opens on: a press on the Filters button. The source has a "Filters" button on a narrow screen. This record does not have the look of its open panel, so the sheet is the designer's drawing.
- `product-page`: a link back to the cards, and one plain box. The box names the record and the pattern `content/product-page`, which draws the page. Opens on: a click on a card.

## Transitions

The agent read the value from the style of a card with `orca eval`. The agent also put the pointer on a card, and the border changed.

- `cards` to `cards`. Trigger: the pointer goes over a card. Moves: the border of the card goes from grey to ink. 150 ms, cubic-bezier(0.4, 0, 0.2, 1). measured.
- `cards` to `filtered`, and `filtered` to `no-match`. Trigger: set a filter, or type in the search field. Moves: the cards change at once. 0 ms, none. estimated. The capture read no transition for a change of the cards.
- `cards` to `metric-changed`, and back. Trigger: choose a metric in the switch. Moves: the numbers and the order of the cards change at once. 0 ms, none. estimated. The source has no such state.
- `cards`, `filtered`, `metric-changed` or `no-match` to `filters-open`, and back. Trigger: press the Filters button. The Close button, the last button of the sheet, a press outside the sheet, or Escape closes the sheet. Moves: the sketch shows and hides the sheet at once. 0 ms, none. estimated. `sheets/bottom-sheet` records the motion of a sheet.
- `cards`, `filtered` or `metric-changed` to `product-page`. Trigger: click a card. Moves: the sketch shows the plain box at once. 0 ms, none. estimated. The source loads a new page.

## Hard cases

- 1280 px screen: the side column is 232 px wide, and the cards are 811 px wide in 3 columns. The search field, the metric switch and the filters stay in view while the cards scroll. The metric switch has the width of the side column, and each of its 3 options is 74 px wide and 44 px high.
- 1024 px screen: the side column stays, and the cards are 728 px wide in 2 columns. The grid has as many columns as fit, and each column is 240 px wide or more.
- 768 px screen: the head is one row with a height of 44 px, and the cards are in 2 columns. In the sheet, the metric switch is the first row, and the 3 filters are the next row. The sheet is 317 px high.
- 390 px screen: the title and the search field are the first row. The Filters button is the second row, and the sort select and the button are the third row. The cards are in 1 column. In the sheet, the metric switch is the first row, the stage and the lead are the next row, and the users are the third row. The sheet is 404 px high.
- Head below 1024 px: the closed head does not show the metric switch. The Filters button names the chosen metric after the count, such as "Filters (2), Revenue". The owner asked for the name there, so the member sees what the numbers mean before the sheet opens. With that longest text, the search field is 128 px wide at 768 px.
- Keyboard on the metric switch: the switch is one Tab stop. The arrow keys choose the next option, and the focus stays on the switch.
- Keyboard in the sheet: the focus goes to the chosen option of the metric switch. Tab stays in the sheet. Escape closes the sheet, and the focus goes back to the Filters button.
- Long name: the source cuts a name on one line. The sketch cuts a name after 2 lines.
- Long name of a lead: the sketch cuts it with an ellipsis on one line, and the avatar keeps its size.
- No picture of a lead: the sketch shows 2 letters of the name in a round avatar.
- No picture: the source shows the first letter of the name in a box. The sketch shows the same empty box for each record.
- No number: not seen. In the sketch, a product with no users has no MRR and no revenue. Its card shows the number "$0" or "0" and the growth "None", and it is last in the order of each metric.
- Many records: the capture did not scroll to the end of `/acquire`. The sketch has 16 cards.
- No match: the source shows a box with one line, one hint and one button that clears the filters. The sketch keeps the 3 parts.
- Slow network and failed load of the cards: not seen.

## Notes

  - the large head with its lines, the sponsor cards at the 2 sides, and the logos;
  - the "FOR SALE" mark, the view count and the like count of a card, and its category chip;
  - the line with the count of results, and the icon of the empty box.
- The source has its filters in a panel at the left of the cards. The sketch first had the filters in one row above the cards. Then the owner asked for a side column on a large screen, and for a head that takes less of the first screen on a tablet. So the filters are a side column at 1024 px and up, and one button with a sheet below 1024 px.
- The owner asked for a metric switch with MRR first. The switch is a row of 3 options, so the member sees each metric without a click. It is with the filters: in the side column at 1024 px and up, and in the sheet below 1024 px. In a trial with the switch beside the Filters button, the search field was 49 px wide at 820 px and 26 px wide at 768 px. So the sheet has the switch, and the first screen keeps its cards.
- The metric is not a filter. The "Clear" button and the count on the Filters button leave it out.
- With a side column in a page of 811 px, the cards had only 2 columns, and a table was 559 px wide. So the page is 264 px wider at 1024 px and up, and the cards keep their 811 px.
- The sheet of the filters has no motion and no drag. `sheets/bottom-sheet` records these parts of a sheet.
- The avatar and the name of the lead on a card are the owner's choice. The capture did not record a person on a card of the source. The owner asked for a smaller lead. So the avatar is 24 px, and the name is in smaller and quieter text than the name of the product.
- The head of this pattern is also the head of `content/leaderboard`, `content/sort-heads` and `content/ranked-groups`, because the owner asked for the same head above the cards and above a table. Only the control that sets the order differs. It is the sort select here. Its options are the order of the chosen metric, "Newest first" and "Name".
- `/acquire` asks for an account before it applies a filter. `/search` has the same panel and the same cards, and it applies a filter with no account. So `filtered` and `no-match` come from `/search`.
- The panel of the source has 12 filters. The sketch has 3 filters for the use case: the stage, the users in a week and the lead. The MRR and the revenue of the sketch are in dollars.
- The card of this pattern is one part. A pattern that shows such cards draws a plain box for each card, and it names this pattern. `content/wide-grid` and `content/product-page` do so.
- Keep these parts when the look changes: each filter is in view on a large screen, the head is one row on a tablet, the whole card is one link, each card has the same numbers at the same place, and the focus goes back to the card after the page of the record.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
