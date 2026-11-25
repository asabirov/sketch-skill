# Filter bar with range and direction

Captured: 2026-11-25, recorded by an agent
Best for: the top of a report page, where a person sets what the whole report shows: a saved view, filters, a date range and the direction of the money.
Row opens: no rows.
Related: `analytics/range-brush` sets the same range by a drag on a time line. `analytics/breakdown-table` and `analytics/written-insights` follow the filters of this bar. `content/catalog-base-view` has a bar with the view name, Filter and Sort for a set of records, with no range. The sketch template `search/results` filters in a side panel.

## Scenarios

- Pick a set range, such as this quarter.
- Pick a custom range of months with 2 clicks.
- Type exact From and To dates.
- Show only the money in, or only the money out.
- Learn why Compare to is off, and turn it on with a short range.
- Open a saved view or more filters.

## States

- `bar`: Saved views, Filters, the range button with a calendar icon, the direction button, and at the right end Compare to. Compare to is off, and a short line next to it says why. Opens on: the address of the page.
- `range-menu`: a popover below the range button with a Range menu (Custom or a set range), a From field, a To field, and the 12 months of the year as buttons. The months of the range are filled. The months after today are off. Opens on: a click on the range button.
- `months-picked`: 2 clicks on months make a new range. The button, the fields and the filled months show it. Opens on: a click on a first month and then a last month.
- `preset-picked`: the button names the set range, such as This quarter. Opens on: a choice in the Range menu.
- `direction-menu`: a popover below the direction button with 3 choices: all cash flow, money in and money out. Each of the last 2 has a short line of examples. Opens on: a click on the direction button.
- `money-in`: the button says Money in, and the report shows only the money in. Opens on: Money in in the direction popover.
- `compare-on`: with a range of one month, Compare to is on, and the line about it goes. Opens on: a range of one month or less.

## Transitions

- `bar` to `range-menu`, and `bar` to `direction-menu`. Trigger: a click on the button. Moves: the chevron of the button turns 180° (transform). 200 ms, cubic-bezier(0.35, 0, 0.25, 1). measured. The popover shows at once. measured.
- `range-menu` to `months-picked`. Trigger: 2 clicks on months. Moves: nothing. The months fill at once. estimated.
- `direction-menu` to `money-in`. Trigger: a choice. Moves: nothing in the bar. The report below changes, as its own pattern says. estimated.

## Hard cases

- A range that starts in another year: the popover shows the year above the months. A product with more years needs a year switch.
- Months after today: they are off, so a person cannot pick a range in the future.
- A long range name: the button keeps one line, and the bar wraps.
- Narrow screen: at 390 px the bar wraps into 3 rows, and the popover takes the width of the screen. The source hides Saved views and Filters behind one settings button on a phone.
- Touch screen: each month button has a target of 44 px.
- Compare to off: the reason stays next to the button, not in a tooltip, so a touch screen shows it too.

## Notes

- The bar sets the filters of the whole page. Put it above every block that it changes.
- The range button names the range in words, so a person reads it without opening the popover.
- A turned-off control says why it is off, and what turns it on.
- Left out, because only the source has them: the bookmark of a saved view and the settings button of the page.
