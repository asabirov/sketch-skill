# Phone chat list with a filter in place

Captured: 2026-11-20, recorded by an agent
Best for: a phone app with a short list of chats, where a search finds only chats.
Row opens: on the record's own page
Related: `chat/chat-list` opens a search screen. `chat/chat-list-tab-bar` has a tab bar in place of the Menu button. `chat/avatar-badges` draws the marks on the avatars.

## States

- `list`: a list of chats. Each row has an avatar, a name, one line of the last message and a time. A New chat button is at the top. A Menu button and a Search field are at the bottom. Opens on: the start of the app, or Back.
- `chat`: the page of one chat, with Back and the name. A plain box stands for the rest of the page. Opens on: tap on a row.
- `search`: the same list. The Search field at the bottom has text, and only the rows with that text show. Opens on: a key in the Search field. The source opens a search screen.
- `search-none`: the list has one sentence that says no chat has this text. Opens on: text that no chat has.
- `empty`: one sentence that says the list has no chats, and a New chat button. Opens on: an account with no chats. The source shows no empty list.

## Transitions

- `list` to `chat`. Trigger: tap on a row. Moves: while the finger is down, the row shrinks to `scale(0.96)` and its `background-color` becomes a soft fill. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `list` to `chat`. Trigger: the same tap. Moves: the list leaves to the left with `push-exit`, and the chat comes in from the right with `push-enter`. 520 ms, feed(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `chat` to `list`. Trigger: tap on Back. Moves: the chat leaves to the right with `back-exit`, and the list comes in from the left with `back-enter`. 520 ms, the same `feed()` spring. measured.
- `list` to `search`. Trigger: a key in the Search field. Moves: the rows change at once. This move has no duration.
- `search` to `search-none`. Trigger: a key. Moves: the rows change at once. This move has no duration.

## Hard cases

- Long text: a last message that is longer than the row ends with an ellipsis. It stays on one line.
- Empty: the source shows no empty list. The `empty` state is drawn.
- No match: the list shows one sentence. The Search field keeps its text.
- Wide screen: from 736 px, the source keeps the list beside the open chat, and plays no push.
- Reduced motion: the source plays none of these animations. Each screen shows at once.
- Error and slow network: the source shows no such state.

## Notes

- The Search field and the Menu button are at the bottom, where the thumb reaches them. Keep them there when the look changes.
- A row shows only what helps the person choose: who, the last line and when. Keep the row at one line of text for each.
- The whole row is the target. The press feedback starts when the finger goes down, before the chat opens.
- The sketch leaves out the account button of the source and the marks on the avatars. The marks are in `chat/avatar-badges`. The Menu button opens the sheet of `sheets/bottom-sheet`.
- The sketch adds the title "Chats". The source shows no title on this screen.
- The page of a chat is not part of this pattern. The sketch draws it as a plain box.
- The designer drew this pattern from `chat/chat-list`. The source opens a search screen.
