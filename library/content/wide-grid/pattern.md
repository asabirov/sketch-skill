# Wide grid

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member chooses one group of records, and then scans all records of that group.
Row opens: on the record's own page. Each card of the source is a link to the page of its record. That page has its own pattern, `content/product-page`.
Related: `content/fact-cards` draws the card, and it has a search field and filters. `content/kanban` shows the records of each group in one column. `content/product-page` is the page that a card opens.

## States

- `cards`: the title is at the left of the top row. A metric switch, a search field and one button are at the right. The metric switch has the options MRR, Revenue and Users, and MRR is the first choice. The cards take the full column. The first 9 cards show, and a "Load more" button shows the others. A group of links below the cards leads to each stage. Each card is a plain box with the name of its record and the number of the chosen metric, because the card has its own pattern, `content/fact-cards`. The box with the largest number is first. Opens on: the page load, the path of a group while MRR is the metric, or a choice of MRR in the switch. The source shows no such screen with all records.
- `filtered`: the page of one group. A path above the title leads back to all records, and the name of the group is the title. The links below the cards lead to the other groups. Opens on: a link of a group, or words in the search field.
- `metric-changed`: the same grid with a different metric. Each box names that metric and its number, and the box with the largest number is first. A group, a search and the path back keep the chosen metric. Opens on: a choice of Revenue or Users in the metric switch. The source shows no such state. The owner asked for the switch, so it is the designer's drawing.
- `no-match`: the path and the title stay. A box takes the place of the cards. It has one line that says that the group has no record, one hint, and one button that shows all records. Opens on: a group with no record, or words that no record matches. The source shows no such state.
- `product-page`: a link back to the cards, and one plain box. The box names the record and the pattern `content/product-page`, which draws the page. Opens on: a click on a card.

## Transitions

`transitions.json` has no value. The capture read no transition for a change of the cards. The value of a card is in the pattern `content/fact-cards`.

- `cards` to `metric-changed`, and back. Trigger: choose a metric in the switch. Moves: the boxes change at once. 0 ms, none. estimated. The source has no such state.
- `cards` or `metric-changed` to `filtered`, and to `no-match`. Trigger: click a link of a group, or type in the search field. Moves: the cards change at once. 0 ms, none. estimated. The source loads a new page for a group.
- `cards` to `cards`. Trigger: click "Load more". Moves: the other cards show at once. 0 ms, none. estimated. The capture did not read this change.
- `cards`, `filtered` or `metric-changed` to `product-page`. Trigger: click a card. Moves: the sketch shows the plain box at once. 0 ms, none. estimated. The source loads a new page.

## Hard cases

- 1280 px screen: the column is 811 px wide, and the cards are in 3 columns. The head is one row: the title, the metric switch, the search field and the button. The metric switch is 216 px wide.
- 768 px screen: the cards are in 2 columns. The sketch changes to 3 columns at 1000 px, and to 2 columns at 600 px. The head is one row from 732 px. Below 1024 px, the search field is 204 px wide. Below 732 px, the search field and the button go to a second row.
- 390 px screen: the head has 3 rows: the title, the metric switch, and the search field with the button. The cards start 56 px lower than with no switch. The cards are in 1 column, and the links of the groups go to a second line.
- Long title: the title goes to a second line beside the metric switch.
- Keyboard on the switch: the arrow keys change the metric, and the focus stays on the chosen option.
- Many records: the source shows 30 cards, and then a "Load more" button. The sketch shows 9 of its 16 cards, and the button shows the other 7. The focus then goes to the first new card.
- Empty group: not seen. Each category of the source has records. The sketch draws `no-match` for a stage with no product.
- Search: the search field of the source opens a list of results below the field. In the sketch, the words filter the cards, and the title names the words.
- Slow network and failed load: not seen.

## Notes

- The pattern holds only the parts that a page of one group needs: the path, the title, the grid, the "Load more" button and the links to the other groups. The sketch leaves out the large head, the sponsor cards at the 2 sides and the logos of the source.
- A card is a part of the pattern `content/fact-cards`. So this sketch draws one plain box for each card, with a caption that names that pattern. A box shows the number of the chosen metric, so the effect of the switch is in view. Put the card of that pattern in each box.
- The source is the page of one group, so it is `filtered` in the sketch. `cards` is the same grid with all products. This screen, the search and `no-match` are the designer's choice.
- The owner asked for the same metric switch as in the head of `content/fact-cards`. This page has no filters and no Filters button, so the switch is in the head, in view at each width. The metric is not a filter.
- The source has its title and its search field in the middle of the page. The owner asked for a page in balance. So the title is at the left edge of the cards and the search field is at the right edge. This page has no filters, because the group is the only filter.
- Keep these parts when the look changes: the group is the only filter, the path leads back to all records, and the links to the other groups are below the cards.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
