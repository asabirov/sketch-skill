# Bottom sheet

Captured: 2026-11-20, recorded by an agent
Best for: a phone app shows a short set of choices over the screen, and the person goes back to the screen with one move.
Row opens: no rows. The content of the sheet is not part of this pattern.
Related: `sheets/bottom-sheet-two-heights` opens at half of the screen height and can become tall. `sheets/bottom-sheet-peek` has no scrim, and its closed sheet shows a handle. `sheets/catalogue-sheet` and `chat/create-a-chat` put content in this sheet.

## States

- `closed`: the screen with a Menu button at the bottom. No sheet shows. A plain box stands for the screen. Opens on: Close, a press outside the sheet, Escape, or the release of a long drag.
- `open`: a sheet covers the lower part of the screen. It has a grab handle, a title and a Close button. A plain box stands for its content. The screen behind is dimmed and takes no input. Opens on: tap on the Menu button.
- `dragging`: the sheet is under the finger, lower than its open position. The dimmed screen does not change. Opens on: a drag down that starts on the head of the sheet.

## Transitions

- `closed` to `open`. Trigger: tap on the Menu button. Moves: the sheet rises from below the screen, with the animation `directory-enter`. 520 ms, linear(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `closed` to `open`. Trigger: the same tap. Moves: the scrim shows, with the animation `scrim-enter`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `open` to `closed`. Trigger: tap on Close, a press outside the sheet, or Escape. Moves: the sheet leaves at once, and the scrim fades out with the animation `scrim-exit`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `open` to `dragging`. Trigger: a drag down on the head of the sheet. Moves: the sheet, by the distance of the finger. This move has no duration.
- `dragging` to `open`. Trigger: a release before one third of the sheet height. Moves: the `transform` of the sheet, back to the open position. 520 ms, the same `linear()` spring. measured.
- `dragging` to `closed`. Trigger: a release after one third of the sheet height. A flick also closes the sheet, if it is longer than 24 px and faster than 0.5 px in a millisecond. Moves: the `transform` of the sheet, to below the screen. 520 ms, the same `linear()` spring. Then the scrim fades out in 120 ms. measured.

## Hard cases

- Tall content: the sheet stops 48 px below the top of the screen. Its content scrolls inside the sheet.
- Drag on the content: only the head of the sheet starts the drag. Thus a drag on the content scrolls the content.
- Keyboard: Escape closes the sheet, and Tab stays in the sheet.
- Wide screen: from 736 px, the source shows the sheet as a dialog in the centre, with no grab handle.
- Reduced motion: the source plays none of these animations. The sheet and the scrim show at once.
- Empty, error and slow network: the source shows no such state for the sheet.

## Notes

- The sheet is a holder. Put a menu, a list or a form in it. `sheets/catalogue-sheet` and `chat/create-a-chat` use it.
- Keep the three ways to close: the Close button, the press outside and the drag. Each one fits a different grip of the phone.
- Keep the drag under the finger with no delay. The person can then stop and let the sheet go back.
- The spring moves the sheet 16% past its end position and then back. Keep one such curve for the sheet and for each screen change.
- The sketch leaves out the rows of the source menu, their count badge and the account button of the screen behind. Only that app needs them.
- The content of the sheet and the screen behind are not part of this pattern. The sketch draws each as a plain box.
