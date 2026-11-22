# Document match

Captured: 2026-11-22, recorded by an agent
Best for: a finance product where a person matches a bank transaction with an invoice, and checks the data read from the invoice against the document, one decision at a time.
Row opens: on the record's own page. A row of the source's bill list opens a side panel with a Review button, and Review opens this screen as its own page.

## States

- `match-start`: one bank transaction with its amount, date and reference, and a list of possible invoices under it. Each row has the invoice and its amount. The best invoice has a "Strong match" badge under its name. A link finds another invoice. Opens on: a transaction that has no invoice. The source shows no such state. The agent drew it for the owner's scenario.
- `match-loading`: the form column shows a title and three pulsing dots while the product matches the bill to a known payee. The document column shows a blank sheet with a spinner. Opens on: a pick of an invoice in `match-start`.
- `match-review`: the form column has the title, one line that says why the match is strong, and one box with the matched payee and a "Strong match" badge. One full-width primary button accepts the match. A link chooses another payee. The document column shows the whole document at the top, at a zoom that fits its width. Opens on: the end of the match.
- `field-review`: one step of the check, such as the amount. The step has a title, the fields of that step, and Back and Next at the foot of the form column. When a field has focus, the document zooms to the value that the field was read from and marks it. Opens on: Next, or the focus of a field.
- `mismatch`: the field value differs from the document value. The field shows an error line with the two values, and the document marks its own value. The primary button copies the document value and goes on to `match-finish`. Back is beside it. Opens on: a step where the read value and the field value differ. The source shows no such state: each demo bill matches its document. The designer drew it for the use case.
- `match-finish`: a summary of the payment and the invoice: the supplier, the invoice number, the date and the total, beside the whole document. Back and the primary button "Confirm match" are at the foot. A link opens the edit mode. Confirm match returns to `match-start` with a short message. Opens on: the last step. This state is drawn.
- `edit-mode`: all read fields in one form beside the document: supplier, invoice number, date and total. The focus of a field zooms the document to its source value. Save and Cancel return to `match-finish`. Opens on: Edit the details. This state is drawn.
- Document drawer, on a phone: a bar at the foot of each step shows a page icon, the invoice number and where the photo came from. A tap opens a drawer from the bottom with the whole document, zoomed to the value of the step and marked. A down arrow closes it. Opens on: a tap on the bar. The owner asked for it. This part is drawn.

## Transitions

The agent read each value with the capture script on the public demo.

- `match-loading` to `match-review`. Trigger: the match ends. Moves: three dots pulse while the match runs. 1500 ms, cubic-bezier(0.05, 0.2, 0.35, 1), with delays of 0, 100 and 200 ms. measured.
- `match-review` to `field-review`. Trigger: the primary button, then Next. Moves: the document zooms and pans to the source value of the step, and the value gets a marker. 400 ms, ease, on transform. measured duration and easing, estimated marker (no transition read for the marker).
- `field-review` to `match-review`. Trigger: Back. Moves: the document pans back to the whole page. 400 ms, ease. measured.
- `field-review`, a field gets focus. Moves: the focus outline of the field. 80 ms, linear, on outline-color. measured.
- `field-review` to `mismatch`. Trigger: a field value that differs from the document. Moves: the error line shows at once. 0 ms, none. estimated. The source shows no mismatch.
- `match-start` to `match-loading`, `mismatch` to `match-finish`, `match-finish` to `match-start`, and `match-finish` to `edit-mode` and back. Trigger: the pick of an invoice, the copy of the document value, Confirm match, Edit the details, Save or Cancel. Moves: the page changes at once. 0 ms, none. estimated. The source shows none of these states.
- the bar to the document drawer, and back. Trigger: a tap on the bar, or the down arrow. Moves: the drawer shows at once. 0 ms, none. estimated. The source has no drawer.

## Hard cases

- Narrow screen: at 390 px the source shows the form only. The document column and its chevron are gone, so a person on a phone cannot see the source value. The sketch keeps a bar at the foot of each step. It opens the document in a drawer.
- Value not found: not seen. The sketch shows the whole document with no marker, and the field shows no error.
- Long document: the source scrolls the document inside its column and keeps the zoom bar at its foot.
- Where the document came from: the source does not say where the document came from. The sketch shows one line above the document that names it, such as a photo from a phone with its date. The owner asked for it. This line is drawn.
- Two currencies: the source shows a memo that says the services were converted. Not seen as a state.
- Keyboard: Tab moves through the fields. The focus on a field zooms the document. The zoom bar has Zoom in, Zoom out and Reset zoom buttons, each with a name.
- Slow network: the document shows a spinner on a blank sheet while it loads.

## Notes

- The pattern is good because the document answers each field. The person never searches the document for a value: the focus of a field brings its source into view and marks it.
- One decision per step. The source splits the check into payee, payment method and amount, each with Back and Next.
- Keep these parts when the look changes: the document beside the form at full height, the zoom to the source value with a marker, one primary button for each step, and Back.
- Left out because only the source has them: the demo banner, the product's own logo bar, the chat button at the foot, the payment rail names, the send-from account, the send date, the repeat switch, the copy button of the document bar.
- The source names the match quality with a badge, "Strong match", and gives the reason in one line under the title.
- The sketch keeps no brand, colour, logo, text or picture of the source. The payees, the amounts and the document are sample content.
- Category: `content`. The coordinator confirmed this existing category for this preparation round.
- The frames and the video of the source are not committed.
- All personal names, invoice details and amounts in the sketch are fabricated.
- The source record and pictures remain outside the public folder.
