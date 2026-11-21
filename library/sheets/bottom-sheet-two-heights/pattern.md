# Bottom sheet with two heights

Captured: 2026-11-20, recorded by an agent
Best for: a phone app shows a long list over the screen, and the person must still see the screen behind it.
Row opens: no rows. The content of the sheet is not part of this pattern.
Related: `sheets/bottom-sheet` has one height. `sheets/bottom-sheet-peek` has no scrim, and its closed sheet shows a handle.

## States

- `closed`: the screen with a People button at the bottom. No sheet shows. A plain box stands for the screen. Opens on: Close, a press outside the sheet, Escape, or the release of a long drag.
- `open`: a sheet covers the lower half of the screen. It has a grab handle, a title, a height button and a Close button. A plain box stands for its long list. The screen behind is dimmed and takes no input. Opens on: tap on the People button. The source shows no sheet with two heights.
- `dragging`: the sheet is under the finger, lower than its open position. The dimmed screen does not change. Opens on: a drag down that starts on the head of the sheet.

## Transitions

- `closed` to `open`. Trigger: tap on the People button. Moves: the sheet rises from below the screen to half of the screen height, with the animation `directory-enter`. 520 ms, feed(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `closed` to `open`. Trigger: the same tap. Moves: the scrim shows, with the animation `scrim-enter`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `open` to `closed`. Trigger: tap on Close, a press outside the sheet, or Escape. Moves: the sheet leaves at once, and the scrim fades out with the animation `scrim-exit`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `open` to `dragging`. Trigger: a drag down on the head of the sheet. Moves: the sheet, by the distance of the finger. This move has no duration.
- `dragging` to `open`. Trigger: a release before one third of the sheet height. Moves: the `transform` of the sheet, back to the open position. 520 ms, the same `feed()` spring. measured.
- `dragging` to `closed`. Trigger: a release after one third of the sheet height. A flick also closes the sheet, if it is longer than 24 px and faster than 0.5 px in a millisecond. Moves: the `transform` of the sheet, to below the screen. 520 ms, the same `feed()` spring. Then the scrim fades out in 120 ms. measured.
- `open` at half height to `open` at the tall height. Trigger: tap on the height button, or a drag up of more than 24 px on the head. Moves: the `height` of the sheet. 520 ms, the same `feed()` spring. estimated.
- `open` at the tall height to `open` at half height. Trigger: tap on the height button. Moves: the `height` of the sheet. 520 ms, the same `feed()` spring. estimated.

## Hard cases

- Tall content: the tall sheet stops 48 px below the top of the screen. The list scrolls inside the sheet at each height.
- Drag on the content: only the head of the sheet starts the drag. Thus a drag on the content scrolls the content.
- Keyboard: Escape closes the sheet, and Tab stays in the sheet.
- Wide screen: from 736 px, the source shows the sheet as a dialog in the centre, with no grab handle.
- Reduced motion: the source plays none of these animations. The sheet and the scrim show at once.
- Empty, error and slow network: the source shows no such state for the sheet.
- Open again: the sheet opens at half height each time.

## Notes

- The half height keeps the screen behind in view. The tall height shows more of the list.
- Keep the three ways to close: the Close button, the press outside and the drag. Each one fits a different grip of the phone.
- Keep the drag under the finger with no delay. The person can then stop and let the sheet go back.
- The spring moves the sheet 16% past its end position and then back. Keep one such curve for the sheet and for each screen change.
- The content of the sheet and the screen behind are not part of this pattern. The sketch draws each as a plain box.
- The designer drew this pattern from `sheets/bottom-sheet`. The source shows a sheet with one height.
