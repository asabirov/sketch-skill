# Dashboard grid

Captured: 2026-11-25, recorded by an agent
Best for: a dashboard home where each person chooses which cards to see, their order and their size, and the same layout must hold from a phone to a wide screen.
Row opens: no rows. Each card opens its own page.
Related: the sketch template `list/card-grid` is a grid of records that people find by picture, not a dashboard. `analytics/balance-card`, `analytics/action-row`, `analytics/account-list`, `analytics/summary-card` and `analytics/cashflow-chart` are cards that this grid holds.

## Scenarios

- Put the cards that a person uses most at the top.
- Make an important card larger, or a less important card smaller.
- Hide a card that a person never uses, and add it again later.
- Add a new card from a catalog.
- Undo a change, cancel all the changes, or go back to the first layout.
- Use the same layout on a phone, a tablet and a wide screen without arranging it again.
- Arrange the cards without a pointer, with the keyboard or a screen reader.

## States

- `grid`: the heading Home and Customize. The cards in one order. A card is Small (1 column), Medium (2 columns) or Large (the full row). The grid has 4 columns from 960 px. Opens on: the address of the page.
- `edit`: the bar has Add a card, Reset, Cancel and Done. A line says how to move a card. Each card has a dashed outline and a head on one line: a handle to drag and the title. A card with room shows Move earlier, Move later, a size button and Hide as buttons. A card with less than 340 px of room inside its padding shows one card menu button in their place. Opens on: Customize.
- `size-menu`: a menu below the size button of a wide card, with Small, Medium and Large. The current size has a check mark. Opens on: the size button.
- `card-menu`: the card menu of a narrow card, with Move earlier, Move later, then Small, Medium and Large, then Hide. The first card has Move earlier off, and the last card has Move later off. Opens on: the menu button of a narrow card.
- `catalog`: a popover with each hidden card and its Add button. Opens on: Add a card. An added card goes to the end, Small.
- `dragging`: the card under the pointer is lifted, with a shadow, and follows the pointer. When it enters another card, the 2 cards change places and the others slide. On release it slides into its place. Opens on: a drag of a handle.
- `card-hidden`: the card is gone, the others close the gap, and the line says how to add it again, with Undo. Opens on: Hide.
- `tablet`: 2 columns. A Large card and a Medium card take the full row. The order is the same. Opens on: a grid from 560 to 959 px wide. The sketch state narrows the page to 820 px.
- `phone`: 1 column, every card takes the full row, in the same order. Opens on: a grid less than 560 px wide. The sketch state narrows the page to 390 px.
- `loading`: each card has its title and pulsing lines. Opens on: the first load.
- `no-cards`: in the edit mode, a frame says that Home has no cards and that Add a card adds one. Opens on: Hide on the last card.

## Transitions

- `edit` to a new order or size. Trigger: Move earlier, Move later, a size, Hide, Add, Reset, Undo or Cancel. Moves: each card that changes place slides from its old place to its new place (transform). 250 ms, cubic-bezier(0.2, 0, 0, 1). estimated.
- `grid` to `tablet` or `phone`. Trigger: the grid gets narrower or wider, and the column count changes. Moves: each card slides to its new place (transform). 250 ms, cubic-bezier(0.2, 0, 0, 1). The cards do not move while the column count stays the same. estimated.
- `dragging`. Moves: the lifted card follows the pointer with no motion of its own. The other cards slide as above. On release, the card slides into its place, 250 ms. estimated.
- `loading`. Moves: the lines pulse (opacity), 1000 ms, ease. estimated.
- With reduced motion, every card jumps to its new place.

## Hard cases

- A size that leaves a gap: a Small card next to a Large card leaves the rest of its row empty. The grid does not fill the gap with a later card, because the order on the screen must match the order for the keyboard.
- One layout for all widths: the grid keeps one order and one size for each card. A Medium card on a 1-column phone takes the full row. A separate layout for each width is left out, because a person must then arrange the cards again for each width.
- A free resize to any number of columns is left out. 3 sizes keep the layout clean at each width.
- Keyboard: the buttons, or the card menu, do everything that a drag does. After a move, the focus returns to the same control of the moved card. Each change is said in the line below the bar, which a screen reader hears.
- Touch: a drag starts only from the handle, so a scroll on a card does not move it. Near the top or the bottom edge of the screen, the page scrolls during a drag, so a card reaches a place that is off screen.
- The card width, not the screen width, chooses the buttons or the card menu. On one screen, a Small card can show the menu while a Large card shows the buttons. The head stays on one line, and a long title ends with an ellipsis.
- Cancel after many changes returns the layout that Customize found. Undo returns only the last change.
- The edit mode outside a dashboard home, such as a report page with a fixed layout, is not this pattern.

## Notes

- Every product in the study has an edit mode, so a card does not move by accident.
- The cards have general names and placeholder bodies, because the grid is the pattern. A product puts its own cards in the grid.
- Left out, because only the source has them: the cards of the source's own product and their data.
