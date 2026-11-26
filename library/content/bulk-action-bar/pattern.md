# Bulk action bar

Captured: 2026-11-26, from public pictures
Best for: a work tool where a person gives many records of a list the same change, such as a status, an owner or a date, in one step, and then goes on with the same records.
Row opens: on the record's own page. The source frames show no row that opens. This is the designer's choice: the record number is a link, and a check box at the start of the row selects the row.
Related: `notifications/activity-feed` has a small bar with a count and two actions in its `selected` state, in place above the list. `sheets/catalogue-sheet-multi-select` selects many records in a phone sheet for one action. `content/sort-heads` and `content/wide-grid` are tables that can take this bar.

## States

- `none`: the list with a check box at the start of each row and a check box in the head. No row is selected, and the page shows no bar. Opens on: the page load, the x in the count, Escape, or a clear of the last check box.
- `selected`: 2 rows are selected, and each selected row has a fill. The head check box shows a half mark. A filled bar floats over the bottom of the list. It has the other theme of the page: a dark bar on a light page, and a light bar on a dark page. From the left, it shows the count "2 selected" with an x in one box, then one button for each field (Status, Owner, Due date, Tags, Move), then the icon buttons Duplicate, Archive and Delete, then More. Opens on: a tick in a row check box.
- `picker-open`: the Status picker opens above the bar, at its button. It has a search field and the values of the field. The Status button shows as pressed. Opens on: a click on Status, or Enter or Space on it. Each field button opens its own picker in the same way.
- `applied`: the selected rows show the new value at once. The selection and the bar stay, so the person can make the next change on the same rows. A short message says what changed. The message shows above the bar, so it does not cover the bar. Opens on: a click on a value in a picker. The source shows no Apply button and no Undo.
- `all-selected`: every row is selected, the head check box is ticked, and the count says "12 selected". Opens on: a tick in the head check box, or in "Select all" on a phone. The frames show only 1 and 2 selected rows. This is drawn.
- `more-open`: the More menu opens above the bar. It holds each action that the bar has no room for, then Export and Copy links. Opens on: a click on More.
- `confirm-delete`: a dialog asks "Delete 2 invoices?" and gives Delete and Keep. Keep has the focus. Opens on: a click on Delete. The source shows no such state. This is drawn.
- `record`: a link back to the list and one plain box. The box names the record. The record page is not part of this pattern. Opens on: a click on the record number.

## Transitions

The source gives no transition value. The frames come about 1 second apart, so they show each state but no motion. Each value below is estimated and not measured. It is the designer's choice. `transitions.json` holds these values with `"measurement": "estimated"`.

- `none` to `selected`. Trigger: a tick in the first check box. Moves: the bar fades in and rises 8 px. opacity 200 ms and transform 200 ms, cubic-bezier(0, 0, 0.2, 1). Estimated, not measured. With reduced motion the bar shows at once.
- `selected` to `none`. Trigger: the x in the count, Escape, or a clear of the last check box. Moves: the bar fades out and drops 8 px. opacity 200 ms and transform 200 ms, cubic-bezier(0, 0, 0.2, 1). Estimated, not measured.
- `selected` to `selected`. Trigger: a tick or a clear of one more check box. Moves: the count changes at once. 0 ms, none. Estimated, not measured.
- `selected` to `picker-open`, and back. Trigger: a click on a field button, then Escape or a click outside. Moves: the picker shows and hides at once. 0 ms, none. Estimated, not measured.
- `picker-open` to `applied`. Trigger: a click on a value. Moves: the picker closes, and the values in the rows change at once. 0 ms, none. Estimated, not measured.
- `selected` to `more-open`, and back. Trigger: a click on More. Moves: the menu shows at once. 0 ms, none. Estimated, not measured.
- `selected` to `confirm-delete`. Trigger: a click on Delete. Moves: the dialog shows at once. 0 ms, none. Estimated, not measured. The source has no such state.

## Hard cases

- Many actions on a narrow screen: the source keeps the bar on one line at 1024 px. It hides the lower actions, and More holds them. The sketch hides Due date, Tags and Move below 1000 px, and Owner, Duplicate, Archive and Delete below 600 px. More then holds them.
- Phone: the source frames show no phone. On a phone the sketch bar fills the width and shows the count, Status and More. This is drawn. A phone has no table head, so a "Select all" check box sits above the list.
- End of the list: the source bar floats over the rows and can cover the last row. The sketch keeps an empty room for the bar after the list, so the bar covers rows only while the list goes on under it. This is the designer's choice.
- Long text in a row: not seen. The sketch cuts a long payee name with an ellipsis on one line.
- Many records: the source can change up to 1,000 records in one action. The count shows the number, and the head check box selects only the loaded rows. The sketch does not show a "select all records" choice.
- Delete: the source paints Delete in a warning colour. Its confirm step is not seen. The sketch has no colour, so it asks in a dialog.
- Error and slow network: not seen. The sketch does not draw them.
- Keyboard: Escape clears the selection and removes the bar in the source. In the sketch, Escape first closes an open picker or menu. A second Escape clears the selection.

## Notes

- Keep these parts when the look changes: the count is the first item and also clears the selection, the bar has the other theme of the page, each field has its own button that opens its own picker above the bar, a pick applies at once, the selection stays after a pick, and the actions that do not fit go into More.
- Each field button shows the field name, not the value.
- The sketch leaves out the parts that only the source has: its own action names (Convert to subtasks, Merge, Dependencies, Milestones), the "Send notifications" check box in each picker, and the colour of Delete.
- Earlier notes give the source a 48 px bar, 32 px controls and a 12 px corner. This capture did not measure them, and the sketch does not use them. The sketch uses 44 px targets, as the sketch rules ask.
- A product that must make more than one change and then apply them together needs a different pattern. This record does not hold that form.
- The sketch keeps no brand, colour, logo, text or picture of the source. The invoices, payees and amounts are sample words.
- The frames and the pictures of the source are not committed.
