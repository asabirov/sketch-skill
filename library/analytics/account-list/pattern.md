# Account list card

Captured: 2026-11-25, recorded by an agent
Best for: a card on an overview page that compares the money in a few accounts, pots or wallets, and opens one of them.
Row opens: on the record's own page. A row opens the page of that account.
Related: `analytics/summary-card` shows one key number of one part of the product. `analytics/balance-card` shows the total of all accounts and how it moved.

## Scenarios

- Compare the money in each account at a glance.
- Check how much of one account is free to use, and how much is on the way in or out.
- Open one account to see its transactions.
- Reach all accounts when there are more than fit the card.
- Add an account, or get statements, from the card.

## States

- `list`: the name of the card, an add action and a more button. Below them, 4 rows with an initial, the name and the amount at the right. A link to all accounts with their count ends the card. Opens on: the address of the page.
- `row-hover`: the row gets a ground, and a dark tooltip above it gives the money on the way in, the money on the way out and the money that is free. Opens on: the pointer or the keyboard focus on a row.
- `more-menu`: a menu below the more button with Statements and Transfer rules. Opens on: a click on the more button.
- `account-opened`: the page of the account opens. The sketch shows a line of text in its place. Opens on: a click on a row.
- `long-name`: a long name wraps, and its amount stays on one line at the right. Opens on: an account with a long name.
- `loading`: 4 pulsing rows. The source shows no loading state on this card. Opens on: the first load.
- `one-account`: a new business has one account with €0, and one line with Add money. The source shows no empty state. Opens on: the first visit of a new business.
- `error`: one line of error text and Try again inside the card. The source shows no error state. Opens on: a failed load.

## Transitions

- `list` to `row-hover`. Trigger: the pointer or the keyboard focus on a row. Moves: nothing. The tooltip shows at once. estimated, because the tooltip was seen on a phone only.
- `list` to `more-menu`. Trigger: a click on the more button. Moves: nothing. The menu shows at once. measured.
- `loading` to `list`. Trigger: the data arrives. Moves: the rows pulse (opacity) until then. 1000 ms, ease. Measured on the cash flow page of the source, estimated for this card.

## Hard cases

- Many accounts: the card shows at most 4 rows and a link to all, with their count.
- Long name: the name wraps. The amount never wraps.
- Negative amount: the amount keeps its minus sign at the right.
- Error: drawn as the `error` state.
- Touch screen: the source shows the tooltip on a tap. A tap on a row then opens the account, so a touch product needs the free money on the account page too.
- Narrow screen: the card takes the full width, and the rows keep their layout.

## Notes

- The amount is the reason for the card. Keep it at the right, in figures of one width, so the amounts line up.
- The tooltip answers a second question, "how much can I use now", without a new page.
- Left out, because only the source has them: the names of the source's accounts and its account icons.
