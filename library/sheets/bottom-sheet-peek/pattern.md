# Bottom sheet that peeks

Captured: 2026-11-20, recorded by an agent
Best for: a phone app where a person works with the screen and a sheet together, such as a map with a list of places.
Row opens: no rows. The content of the sheet is not part of this pattern.
Related: `sheets/bottom-sheet` dims the screen behind it, and its closed sheet does not show. `sheets/bottom-sheet-two-heights` opens at half of the screen height and can become tall.

## States

- `closed`: the handle and the title of the sheet show at the bottom of the screen. The screen is in use. A plain box stands for the screen. Opens on: the button that makes the sheet small, Escape, or the release of a long drag.
- `open`: a sheet covers the lower part of the screen. It has a grab handle, a title and a button that makes it small. A plain box stands for its content. No scrim shows, and the screen behind stays in use. Opens on: tap on the handle and the title of the small sheet. The source shows no such sheet.
- `dragging`: the sheet is under the finger, lower than its open position. Opens on: a drag down that starts on the head of the sheet.

## Transitions

- `closed` to `open`. Trigger: tap on the handle and the title of the small sheet. Moves: the sheet rises from below the screen, with the animation `directory-enter`. 520 ms, feed(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `open` to `closed`. Trigger: tap on the button that makes the sheet small, or Escape. Moves: the sheet becomes small at once. This move has no duration.
- `open` to `dragging`. Trigger: a drag down on the head of the sheet. Moves: the sheet, by the distance of the finger. This move has no duration.
- `dragging` to `open`. Trigger: a release before one third of the sheet height. Moves: the `transform` of the sheet, back to the open position. 520 ms, the same `feed()` spring. measured.
- `dragging` to `closed`. Trigger: a release after one third of the sheet height. A flick also closes the sheet, if it is longer than 24 px and faster than 0.5 px in a millisecond. Moves: the `transform` of the sheet, to below the screen. 520 ms, the same `feed()` spring. measured.

## Hard cases

- Tall content: the sheet stops 48 px below the top of the screen. Its content scrolls inside the sheet.
- Drag on the content: only the head of the sheet starts the drag. Thus a drag on the content scrolls the content.
- Keyboard: Escape makes the sheet small. Tab goes from the sheet to the screen behind, because the two are in use.
- Covered screen: the small sheet covers the bottom 64 px of the screen. The screen keeps that space empty.
- Reduced motion: the sheet shows at once.
- Empty, error and slow network: the source shows no such state for the sheet.

## Notes

- The small sheet tells the person that more content is below. Keep its handle and its title in view.
- No scrim shows, because the person uses the screen and the sheet together.
- Keep the drag under the finger with no delay. The person can then stop and let the sheet go back.
- The spring moves the sheet 16% past its end position and then back. Keep one such curve for the sheet and for each screen change.
- The content of the sheet and the screen behind are not part of this pattern. The sketch draws each as a plain box.
- The designer drew this pattern from `sheets/bottom-sheet`. The source shows a sheet with a scrim, and its closed sheet does not show.
