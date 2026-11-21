# direct-message: activity

Captured: 2026-11-12, from public pictures
Best for: a chat app where mentions, replies, reactions and app messages from many channels come to one list. Use it for an activity page in an app rail, with tabs for saved views, a filter popover, and bulk triage.

## States

- `all`: the "Activity" heading with search, a detailed or compact switch and a new-view button. The tabs "All", "DMs" and one custom view, with counts. A toolbar with a select-all box, an Unreads switch and Filters. The list of activity rows. The second row shows its hover actions. Opens on: the Activity link in the rail.
- `compact`: the same list with one line for each row. Opens on: the compact rows button.
- `filters`: a popover under Filters. It holds boxes for direct messages, mentions, thread replies, channel invites, reactions and VIPs, a switch for cleared items, "Save as view" and "Reset". Opens on: the Filters button.
- `selected`: a box at the start of each row, two rows ticked, and a bulk bar with "2 selected", "Mark as read" and "Clear". Opens on: a tick in a row box or the select-all box.
- `empty`: the list has no activity. Opens on: the last row cleared.
- `error`: the list did not load, with Retry. The designer's choice: the source shows no error state. Opens on: a failed load.

A row has an avatar with a small glyph for the kind of event, a context line ("Reply in #launch"), the name, a preview and a time. An unread row is bold. The rail shows a count on DMs and on Activity.

## Transitions

The source pages give no motion values. Each value below is the designer's choice from the kit motion tokens.

- `all` to `filters`. Trigger: a click on Filters. Moves: the popover fades in (opacity 150 ms, cubic-bezier(0.4, 0, 0.2, 1)). estimated.
- A row on hover. Trigger: the pointer or keyboard focus on a row. Moves: the row actions fade in (opacity 150 ms, cubic-bezier(0.4, 0, 0.2, 1)). estimated.
- `all` to `selected`. Trigger: a tick in a row box. Moves: nothing. The bar changes in place. estimated.

## Hard cases

- Long preview: the preview wraps. The source cuts it to one line in the compact view.
- Hover actions on a touch screen: the source uses a swipe to clear. The sketch shows the actions under the row text.
- Many rows: the tab counts carry the number. A cap such as 99+ was not seen.
- Empty list and failed load: not seen.

## Notes

- Keys from the help page: the up and down arrows move through the list, Enter opens a row, C clears a row and R marks it read.
- Cleared rows stay findable through the "Cleared items" switch in Filters.
- The sketch keeps no brand, text or picture of the source. The sample rows are fabricated.
- The cut frames are not committed.
