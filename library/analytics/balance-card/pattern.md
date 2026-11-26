# Balance card

Captured: 2026-11-25, recorded by an agent
Best for: a person opens a money product to see how much money the business has now, and how the total moved over a period that they choose.
Row opens: no rows
Related: `analytics/dashboard-grid` puts this card first in a grid of cards. `analytics/cashflow-chart` shows the money in and the money out of a period in full. `analytics/account-list` splits the total by account.

## States

- `chart`: the name of the total, the total with its cents smaller, and a switch with Chart and Table at the top right. Below it, a period button on the left, and the money in and the money out of the period on the right. Below them, an area chart of the total over the period, with one value on the lowest grid line and 3 to 5 date labels. Opens on: the address of the page.
- `hover`: a thin vertical line and a ring on the line of the total follow the pointer. The total shows the value of that day. The period button and the money in and out give their place to the day on the left and the change since the start of the period on the right. Opens on: the pointer on the chart.
- `period-menu`: a menu below the period button with 8 periods: the last 7, 30, 90 and 365 days, and the week, the month, the quarter and the year to date. The chosen period has a check mark. The chevron of the button points up. Opens on: a click on the period button.
- `period-changed`: the button names the new period. The money in and out and the chart show the new period. The date labels change from days to months for a long period. Opens on: a click on a period in the menu.
- `table`: the period line and the chart give their place to a split of the total: the booked balance, the available balance with the payments on the way out as an indented line, and the payments on the way in. A note below a thin line says what the total counts. Opens on: Table in the switch.
- `loading`: the total and the chart are pulsing blocks. The source shows no loading state on this card. The pulse comes from the cash flow page of the source. Opens on: the first load of the page, and Try again in the `error` state.
- `empty`: the chart is a flat line, the money in and out are €0, and one line under the chart says that no money moved. The source shows no empty state. Opens on: a period without money in or out.
- `error`: the total is a dash, and the body has the error text and Try again. The source shows no error state. Opens on: a failed load.

## Transitions

- `chart` to `hover`. Trigger: the pointer moves on the chart. Moves: nothing. The line, the ring and the values follow the pointer at once. measured.
- `chart` to `period-menu`. Trigger: a click on the period button. Moves: the chevron turns 180° (transform). 200 ms, cubic-bezier(0.35, 0, 0.25, 1). measured. The menu shows at once. measured.
- `period-menu` to `period-changed`. Trigger: a click on a period. Moves: the chevron turns back (transform). 200 ms, cubic-bezier(0.35, 0, 0.25, 1). measured. The chart and the numbers change at once. measured.
- `chart` to `table`, and back. Trigger: a click in the switch. Moves: nothing. The body changes at once. measured.
- `loading` to `chart`. Trigger: the data arrives. Moves: the blocks pulse (opacity) until then. 1000 ms, ease. Measured on the cash flow page of the source, estimated for this card.
- `error` to `loading`, then to `chart`. Trigger: Try again. Moves: the blocks pulse until the data arrives, then the chart shows at once. The designer chose it. estimated.

## Hard cases

- Empty: drawn as the `empty` state.
- Error: drawn as the `error` state.
- Slow network: drawn as the `loading` state.
- Long total: the total keeps one line. On a narrow screen the font gets smaller, and the switch goes below the total.
- Narrow screen: at 390 px the source keeps the same card at the full width. The money in and out go below the period button when the line is too narrow.
- Touch screen: not captured. The sketch follows the finger on the chart and lets the page scroll up and down.
- A period that the sketch does not draw: the sketch draws 3 periods and shows a short message for the other 5.

## Notes

- The card answers one question first: how much money is there now. The total is the largest thing, and everything else is smaller.
- The period changes the chart and the money in and out, but not the total. The total is always today.
- The pointer line turns the card into a reader of one day. It hides the period button, so the line under the total always has exactly one meaning.
- The table is not the data of the chart. It splits today's total into what is booked, what is free and what is on the way. Keep this meaning, or name the table for what it shows.
- The money in has a plus sign and the money out a minus sign. The source also marks them with arrows and colours. The sketch uses words and signs only.
- Left out, because only the source has them: the verified mark next to the name, the button that hides all amounts, and the colours of the money in and out.
