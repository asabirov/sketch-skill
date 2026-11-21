# Swipe back from the full width

Captured: 2026-11-20, recorded by an agent
Best for: a phone app where a person comes back from a record with one thumb, and the page has no part that takes a sideways swipe.
Row opens: on the record's own page
Related: `navigation/swipe-back` starts the drag only at the left edge. `navigation/swipe-back-labelled` shows the name of the list on the Back button. `chat/chat-list` draws the list.

## States

- `list`: a list whose rows open a page. A plain box stands for the list. Opens on: Back, or the release of a long drag.
- `detail`: the page of one row, with Back at the top left. A plain box stands for the rest of the page. Opens on: tap on a row, or the release of a short drag.
- `dragging`: the page is under the finger and moves with it. The list shows under the page. The list is 48 px to the left of its position and dimmed. Opens on: a drag to the right that starts at each point of the page. The source starts the drag only within 24 px of the left edge.

## Transitions

- `list` to `detail`. Trigger: tap on a row. Moves: the list leaves to the left with `push-exit`, and the page comes in from the right with `push-enter`. 520 ms, linear(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `detail` to `list`. Trigger: tap on Back. Moves: the page leaves to the right with `back-exit`, and the list comes in from the left with `back-enter`. 520 ms, the same `linear()` spring. measured.
- `detail` to `dragging`. Trigger: a drag to the right from each point of the page. Moves: the page, by the distance of the finger. The list moves from 48 px left to its position, and its dim goes from full to none, in step with the page. This move has no duration.
- `dragging` to `list`. Trigger: a release after one third of the screen width. A flick also goes back, if it is longer than 24 px and faster than 0.5 px in a millisecond. Moves: the `transform` of the page to the right edge, the `transform` of the list to its position, and the `opacity` of the dim to 0. 520 ms, the same `linear()` spring. measured.
- `dragging` to `detail`. Trigger: a release before one third of the screen width. Moves: the same three properties, back to the start. 520 ms, the same `linear()` spring. measured.

## Hard cases

- Sideways swipe: a part of the page that scrolls sideways, or a row that takes a swipe, stops this drag. Use `navigation/swipe-back` for such a page.
- Sheet: an open sheet does not move sideways. A drag down on its head closes it, as `sheets/bottom-sheet` shows.
- Stopped gesture: if the system stops the gesture, the page goes back to its position.
- Wide screen: from 736 px, the source keeps the list beside the page.
- Reduced motion: the page still follows the finger. After the release, the source shows the end position at once.
- Empty, error and slow network: the source shows no such state for this gesture.

## Notes

- The Back button and the drag open the same screen. Keep both. The button is the way for a keyboard and for a screen reader.
- The list under the page shows where the gesture goes before the finger lifts. Keep the list visible during the drag.
- The page stays under the finger with no delay. The person can stop and let the page go back.
- One third of the width, or a short fast flick, is sufficient. A full drag across the screen is not necessary.
- The list and the content of the page are not part of this pattern. The sketch draws each as a plain box. A tap on the box of the list opens the page.
- The designer drew this pattern from `navigation/swipe-back`. The source starts the drag only at the left edge.
