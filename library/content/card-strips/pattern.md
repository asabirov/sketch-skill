# record: card strips

Captured: 2026-11-20, recorded by an agent
Best for: a team product where a member wants a look at each group of records before a choice.
Row opens: on the record's own page. Each small card of the source is a link to the page of its record. That page has its own pattern, `record-product-page`.

## States

- `cards`: a title is at the top. Below it is one row of small cards for each group. A row has the name of the group at the left, and a "View all" link at the right. Each small card is 220 px wide, with a small picture, the name and 3 numbers. A row scrolls sideways, and the page does not. Opens on: the page load.
- `group`: a link back to the rows, and one plain box. The box names the group and the pattern `record-fact-cards`, which draws the cards of one group. Opens on: a click on a "View all" link.
- `product-page`: a link back to the rows, and one plain box. The box names the record and the pattern `record-product-page`, which draws the page. Opens on: a click on a small card.

## Transitions

The agent did not read a value on a small card of the first page. The agent read the value of the border on a card of `/acquire` with `orca eval`.

- `cards` to `cards`. Trigger: the pointer goes over a small card. Moves: the border of the card goes from grey to ink. 150 ms, cubic-bezier(0.4, 0, 0.2, 1). estimated.
- `cards` to `group`, and `cards` to `product-page`. Trigger: click a "View all" link, or click a small card. Moves: the sketch shows the plain box at once. 0 ms, none. estimated. The source loads a new page.

## Hard cases

- 1280 px screen: the column is 811 px wide, and 3 small cards are in view in each row.
- 768 px screen: 3 small cards are in view in each row.
- 390 px screen: one small card is in view, and a part of the second card shows that the row scrolls.
- Group with few records: the row has no scroll. Its cards stay at the left.
- Group with no record: not seen. In the sketch, such a group has no row.
- Long name: the sketch cuts a name with an ellipsis on one line.
- Keyboard: each small card is a link. In the sketch, the focus on a card scrolls its row, so the card is in view. The capture did not read the focus of the source.
- Slow network and failed load: not seen.

## Variations

- `base`: the layout of the source. This record has no other variation. Each other layout of the source has its own pattern, and the notes name it.

## Notes

- The pattern holds only the parts that rows of small cards need. The sketch leaves out the large head, the sponsor cards at the 2 sides, the logos and the table of the source. The table has its own pattern, `record-leaderboard`.
- A small card is the part of this pattern. It has no 2 lines of words, so it is not the card of `record-fact-cards`.
- Each "View all" link of the source leads to `/acquire`, which `record-fact-cards` draws. So `group` shows only a plain box with the name of that pattern.
- This pattern has no search field. A search gives a list of cards, and `record-fact-cards` draws that list.
- Keep these parts when the look changes: one row for each group, the link to the full group at the end of the head of the row, and the focus goes back to the small card after the page of the record.
- The sketch keeps no brand, colour, logo, text or picture of the source. The products, the leads and the numbers are sample content.
- The frames and the pictures of the source are not committed.
