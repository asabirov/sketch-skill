# Catalogue sheet with multi-select

Captured: 2026-11-20, recorded by an agent
Best for: a phone app where a person does one action on many records of a set, such as an invitation to a group.
Row opens: on the record's own page. A tap on a row only checks it. The button at the bottom closes the sheet first.
Related: `sheets/catalogue-sheet` has one action button on each row. `sheets/catalogue-sheet-search-top` has the same search field below the title. `sheets/bottom-sheet` draws the sheet.

## States

- `closed`: the screen with the button that opens the catalogue. No sheet shows. A plain box stands for the screen. Opens on: Close, a press outside the sheet, Escape, the button at the bottom of the sheet, or the release of a long drag.
- `catalogue`: a sheet of the full height. It has a grab handle, a title, a count of the rows and a Close button. A search field is below the title, above the filter chips. Each row has an avatar, a name, one line and a checkbox. One button at the bottom shows the number of the checked rows. Opens on: tap on the button of the screen. The source shows no checkbox.
- `filtered`: the chip of one filter is filled. Only the rows of that filter show, and the count is smaller. Opens on: tap on a chip.
- `search`: the search field has text. Only the rows with that text show. A section with no such row does not show. Opens on: a key in the search field.
- `no-match`: one sentence that says no row matches, and a Clear filters button. Opens on: a filter and a text that no row has together.

## Transitions

- `closed` to `catalogue`. Trigger: tap on the button of the screen. Moves: the sheet rises from below the screen, with the animation `directory-enter`. 520 ms, linear(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `closed` to `catalogue`. Trigger: the same tap. Moves: the scrim shows, with the animation `scrim-enter`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `catalogue` to `filtered`. Trigger: tap on a chip. Moves: while the finger is down, the chip shrinks to `scale(0.96)` and its `background-color` changes. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The rows change at once.
- `catalogue` to `search`, and `search` to `no-match`. Trigger: a key. Moves: the rows change at once. This move has no duration.
- `no-match` to `catalogue`. Trigger: tap on Clear filters. Moves: the rows show at once. The button has the same 120 ms press as a chip.
- An open sheet to `closed`. Trigger: tap on Close, a press outside the sheet, Escape, or the button at the bottom. Moves: the sheet leaves at once, and the scrim fades out with the animation `scrim-exit`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- An open sheet to `closed`. Trigger: the release of a drag down on the head, after one third of the sheet height. Moves: the `transform` of the sheet, to below the screen. 520 ms, the same `linear()` spring. measured.

## Hard cases

- Long list: the sheet stops 48 px below the top of the screen. The rows scroll inside the sheet. The head and the button at the bottom do not move.
- Section with no match: its title does not show.
- Filter and text together: the rows must match the two. Clear filters takes the two away.
- Count: the source shows no count beside the title. The count of the sketch is drawn.
- Keyboard of the phone: the source does not show the search field above an open keyboard.
- Wide screen: from 736 px, the source shows the sheet as a dialog in the centre, with no grab handle.
- Reduced motion: the source plays none of these animations.
- Error and slow network: the source shows no such state.
- No checked row: the button at the bottom is not in use.
- Checked row that a filter hides: the row stays checked, and the button counts it.

## Notes

- The sheet is that of `sheets/bottom-sheet` at the full height. The three ways to close and the drag are the same.
- The button at the bottom is where the thumb reaches it. It stays in view while the rows scroll.
- One button acts on each checked row. Its label shows the number, so the person knows the size of the action.
- The chips are one choice. "All" takes the filter away. Use the sheet of `sheets/bottom-sheet` with other content for other records.
- The sketch draws people as sample records. The source lists the assistants of that app, with their pictures and marks. The marks are in `chat/avatar-badges`.
- The screen behind the sheet is not part of this pattern. The sketch draws it as a plain box.
- The designer drew this pattern from `sheets/catalogue-sheet`. The source has one action button on each row.
