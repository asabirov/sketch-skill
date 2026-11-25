# Summary card

Captured: 2026-11-25, recorded by an agent
Best for: a small card on an overview page that answers one question about one part of the product, such as "how much of the limit is used" or "how many bills are late", and links to the full page.
Row opens: no rows. The foot line opens the full page of that part.
Related: `analytics/account-list` is a card with rows. `analytics/balance-card` is a card with a chart. `analytics/action-row` starts the jobs of the whole product.

## Scenarios

- See one key number and how close it is to its limit.
- See the counts that need attention, such as late bills.
- Do the one next job of that part, such as Pay now, without leaving the page.
- Open the full page of that part from the foot line.
- Start that part of the product when it is still empty.

## States

- `card`: one card with a name, a more button, one key number, a meter of its limit and one line with the free amount. A foot line below a thin line has the next date and one action. Opens on: the address of the page.
- `more-menu`: a menu below the more button with the less common jobs of that part. Opens on: a click on the more button.
- `near-limit`: the meter is almost full, and the free amount is small. Opens on: a key number near its limit.
- `action-done`: the foot line says that the job is done, in place of the action. Opens on: a click on the action of the foot line.
- `loading`: the body is a pulsing block. The source shows no loading state on this card. Opens on: the first load.
- `empty`: one line about the empty state and one action to start. The source shows no empty state. Opens on: the first visit of a new business.
- `error`: the error text and Try again inside the frame. Try again shows `loading`, then the card. The source shows no error state. Opens on: a failed load.
- `counts`: the other form of the body, for a part without a limit. The same frame has one icon action next to the more button, a row of 3 counts, and a foot line with a short summary and a link. Opens on: a part that counts records, such as bills.

## Transitions

- `card` to `more-menu`. Trigger: a click on the more button. Moves: nothing. The menu shows at once. measured.
- `card` to `action-done`. Trigger: the action of the foot line. Moves: nothing. The foot line changes at once. The designer chose it. estimated.
- `loading` to `card`. Trigger: the data arrives. Moves: the blocks pulse (opacity) until then. 1000 ms, ease. Measured on the cash flow page of the source, estimated for this card.

## Hard cases

- Over the limit: the meter is full, and the line says the amount over the limit in words.
- Large numbers: a count of 4 or more figures keeps one line. The counts wrap as a group.
- A page with many summary cards: each card loads and fails on its own, so one failed card does not hide the others.
- Narrow screen: each card takes the full width.
- Touch screen: each button has a target of 44 px.

## Notes

- Keep the same frame for each card, so a person reads every card the same way: the name, the numbers, then the next step.
- One key number per card. If a card needs more, it is a page, not a card.
- The meter says the limit in words too, so the card does not depend on the bar alone.
- Left out, because only the source has them: the names of the source's products and their icons.
