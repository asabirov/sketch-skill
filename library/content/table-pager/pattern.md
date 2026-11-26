# Table pager

Captured: 2026-11-26, recorded by an agent
Best for: a money product where a person reads a long list of records, such as transactions or an audit log, pages forward and back, and must know how many records the list has and where it ends.
Row opens: in a pane. The capture did not open a row, so this is the designer's choice. The sketch draws no pane, because this pattern is only the pager. The rows of the sketch are not links.
Related: `content/sort-heads` draws the head of a table, and this pattern draws its foot. `analytics/breakdown-table` is a short report table that needs no pager.

The pattern joins two references. A bank app gives the place, the count that names the records, the quiet chevrons, the First page button that shows only away from page 1, and a page that has its own address. A dashboard template gives the range with the total, such as "Showing 1-20 of 52".

## States

- `first-page`: the title "Transactions" and a table of 100 rows, newest first. Under the table, on the left, the pager shows "1–100 of 1,176 transactions", with the range and the total in bold. Then the chevron buttons follow: Previous page, disabled, and Next page. The place of First page is empty, so Previous and Next do not move later. Opens on: the page load, or First page.
- `middle-page`: the next 100 rows. The pager shows "101–200 of 1,176 transactions", then First page, Previous page and Next page, each enabled. Opens on: Next page from page 1, or Previous page from page 3. The same state holds each page from 2 to 11.
- `last-page`: the last 76 rows, then an "End of the list" line under the last row. The pager shows "1,101–1,176 of 1,176 transactions". First page and Previous page are enabled, and Next page is disabled. Opens on: Next page from page 11. The references show no end line. The designer added it.
- `one-page`: a table of 38 rows, then the "End of the list" line. The pager shows only "38 transactions" and no buttons. Opens on: a list with 100 records or fewer. The references show no such state.
- `empty`: the title, the rule of the table head, then "No transactions yet" and one muted hint line. No table rows and no pager show. Opens on: a list with no records. The references show no such state.
- `loading-next`: the title and the table head stay. 12 skeleton rows pulse in place of the rows. The pager shows "Loading 101–200 of 1,176 transactions", and each chevron button is disabled. The page scrolls back to the top of the table. Opens on: any page button. After the rows arrive, the screen shows the new page.

## Transitions

- `first-page` to `loading-next`, and each other page change. Trigger: click First page, Previous page or Next page. Moves: the rows change to skeleton rows at once, and the page scrolls to the top of the table at once. The skeleton bars pulse their opacity in 1000 ms, ease, measured. The wait of 600 ms before the new rows show is the sketch's choice, estimated.
- `loading-next` to `middle-page`. Trigger: the rows arrive. Moves: the skeleton rows change to the new rows at once. The pager buttons change their color and their hover fill in 100 ms, cubic-bezier(0.4, 0, 0.2, 1), measured. First page shows at once.
- `middle-page` to `last-page`. Trigger: Next page on page 11, then the rows arrive. Moves: Next page changes its color and its hover fill to the disabled look in 100 ms, cubic-bezier(0.4, 0, 0.2, 1), measured. The end line shows at once.
- `middle-page` or `last-page` to `first-page`. Trigger: click First page. Moves: the same skeleton rows and button changes. First page hides at once, and its place stays empty.

## Hard cases

- 390 px screen: the count is one line, and the chevron buttons are the next line, on the left. So the buttons do not move from page to page. Each row shows the date on its own line, then the payee, the account and the amount. On page 1 the empty place of First page shows at the start of the button line.
- Long count: "1,101–1,176 of 1,176 transactions" is the longest text. From 600 px the count keeps that width, so the buttons stay in one place.
- Slow network: the skeleton rows and the "Loading" count show until the rows arrive. The buttons are disabled, so a second click cannot skip a page.
- Keyboard: focus stays on the button that the person pressed. On the last page, focus moves to Previous page, because Next page is disabled.
- Shared page: each page has its own address. The bank app puts a cursor of the last record into the address, and a reload opens the same page. The sketch keeps the state id in the address.
- Records added at the top: a cursor keeps the page on the same records. A page number would move each record down by one place.
- Error in a load: not seen.

## Notes

- Keep these parts when the look changes: the pager is under the table on the left, the count names the records, the range and the total are in bold, the chevrons are quiet buttons with no frame, First page shows only away from page 1, the last page has an end line, and a page has its own address.
- The count text is the reason for each disabled button. "1–100" tells that no page is before page 1, and "1,176 of 1,176" tells that no page is after the last page.
- The bank app puts First page before Previous and Next with no empty place, so Previous and Next move one place on page 2. The sketch keeps the place empty on page 1. This is the designer's choice.
- Neither reference has a page size control, a page number, a Last page button or a jump field. The pattern leaves them out. A long ledger with an audit job can need a jump, and that needs its own pattern.
- The dashboard template has First, Previous, Next and Last buttons with a frame, and a selection count at the left. The pattern leaves out the frames, Last page and the selection count.
- The bank app shows 100 rows on a page and scrolls to the top after a page change. Its table head stays on the screen while the rows scroll. The pager is not sticky.
- The sketch keeps no brand, colour, logo, text or picture of the references. The payees, the accounts, the dates and the amounts are sample content.
- The frames and the pictures of the references are not committed.
