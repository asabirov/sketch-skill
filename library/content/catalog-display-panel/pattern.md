# Catalog display panel

Captured: 2026-11-20, recorded by an agent
Best for: a product with one set of records that people scan by picture, compare by field and follow by status.
Row opens: in a pane. The source opens the record in a dialog over the list and keeps the address. No allowed value names a dialog, and `in a pane` is the nearest.

## States

- `card-view`: a toolbar with the name of the current view, Filter and Sort. Under it, one card for each record, with a picture, the name and labelled fields. A line gives the count of records. Opens on: a card view in the list of views. The source opens on a table view. The sketch opens on this state.
- `table-view`: the same toolbar and the same records, with one row for each record and one column for each field. Opens on: a table view in the list of views.
- `board-view`: the same toolbar and the same records, with one column for each status. Each column shows its count and one small card for each record. Opens on: a board view in the list of views.
- `view-list`: the list of views, open under the name of the current view. Each view has a mark for its kind, and the current view has a check. Opens on: a click on the name of the current view. The source list also has a search field and group names. The sketch leaves them out.
- `filter-open`: the filter, open under the Filter button, with one condition on the Status field. Opens on: a click on Filter. The source shows one row for each condition, with a field, a rule, a value and a remove button. The sketch draws one condition as a choice of values.
- `filtered`: the card view with only the records that match. The Filter button shows the count of conditions. Opens on: a view that has a filter, or a value in the filter.
- `sort-open`: the sort, open under the Sort button, with the field and the direction. Opens on: a click on Sort.
- `record-open`: one record in a dialog over the list, with all its fields, Previous and Next buttons and a close button. Opens on: a click on a card or on the name in a row.
- `no-match`: the toolbar with the filter mark, no records, and a count line that reads none. Opens on: a search term or a filter value that no record has. The source shows no message and no action that removes the term.

## Transitions

- `view-list` to `card-view`. Trigger: click a card view in the list of views. Moves: a placeholder for the view name pulses in the toolbar while the view loads. 1200 ms, ease-in-out. measured.
- `view-list` to `table-view`. Trigger: click a table view in the list of views. Moves: a placeholder for the view name pulses in the toolbar while the view loads. 1200 ms, ease-in-out. measured.
- `view-list` to `board-view`. Trigger: click a board view in the list of views. Moves: a placeholder for the view name pulses in the toolbar while the view loads. 1200 ms, ease-in-out. measured.
- `view-list` to `filtered`. Trigger: click a view that has a filter in the list of views. Moves: a placeholder for the view name pulses in the toolbar while the view loads. 1200 ms, ease-in-out. measured.
- `filter-open` to `filtered`. Trigger: choose a value in the filter. Moves: the same pulse of the view name. 1200 ms, ease-in-out. estimated. The capture changed no condition, so the sketch uses the value of a view change.
- `card-view`, `table-view`, `board-view` or `filtered` to `view-list`. Trigger: click the name of the current view. Moves: the list of views shows at once. 0 ms, none. measured.
- `card-view` or `filtered` to `filter-open`. Trigger: click Filter. Moves: the filter shows at once. 0 ms, none. measured.
- `table-view` to `sort-open`. Trigger: click Sort. Moves: the sort shows at once. 0 ms, none. measured.
- `card-view` to `record-open`. Trigger: click a card. Moves: the dialog shows at once over the list. 0 ms, none. measured.
- `record-open` to `card-view`. Trigger: press Escape or click the close button. Moves: the dialog goes at once. 0 ms, none. measured.
- Entry to `no-match`. Trigger: type a search term that no record has. Moves: the records go at once. 0 ms, none. measured. The sketch opens this state from a filter value that no record has.

## Hard cases

- No match: the source shows an empty area, and the count line at the bottom reads none. It shows no message and no action that removes the search term or the filter.
- Slow network: the placeholder for the view name pulses until the view arrives. One pulse is 1200 ms. The capture did not read the number of pulses.
- Many views: the list of views has a search field at its top, and group names between the views.
- Applied filter or sort: the button shows the count, such as 2 filters, and takes a mark. The view keeps the filter and the sort when the person leaves it.
- Wide board: the columns keep their width, and the board scrolls sideways in its own area. The page does not scroll sideways.
- 390 px screen: the toolbar buttons show only their icons, and the name of the view stays. The table scrolls sideways. In the sketch, each row of the table stacks.
- Long name: not seen. Let the name wrap in a card and in a row.
- Empty board column: not seen. Keep the column and its count.

## Variations

- `base`: the layout of the source.
- `view-tabs`: each view is a tab in a row over the records, so one click changes the view. Filter and Sort are icon buttons at the right. A More button opens the list of all views. A filter shows as a chip under the tabs. Use it when the product has few views, and people change the view often.
- `display-panel`: one Display button at the right opens a panel with the choice of view and the sort. `view-list` and `sort-open` show this panel. Filter stays a button at the left. Use it when people set the view one time and seldom change it.
- `side-list`: the views are a list beside the records, and the toolbar has only Filter and Sort. Below 1000 px, a Views button shows the list, and `view-list` shows it open. Use it when each view is a place that people name and go back to.

## Notes

- Keep one set of records behind all views. A view changes only the layout, the filter and the sort.
- Show the kind of the current view and its name in the toolbar. The person must see which view is open before they change it.
- Keep the filter and the sort with each view. Mark the Filter button when a filter is set, because a filter hides records.
- Show the count of records in each view, and the count of each column in the board.
- Open a record over the list, as the source does. The person keeps their place in the list, and Previous and Next go through the records in the order of the view.
- The source shows a loading placeholder in the toolbar for a view change and no motion for a menu, the filter, the sort or the dialog. Keep this difference when the look changes.
- The source has a search button at the right of the toolbar, and buttons to group records and to hide fields. The sketch leaves them out.
- The sketch draws its own marks for the card, table and board views and for Sort. The sketch kit has no icon for them.
- For no match, a product needs a message and one action that removes the filter. The source gives neither, and the sketch copies the source.
