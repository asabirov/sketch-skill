# Topics tree

Captured: 2026-11-20, recorded by an agent
Best for: a chat product that sorts the messages of a channel into topics, where a person goes to one topic of one channel.
Row opens: on the record's own page
Related: `navigation/topics-tree-collapsible` hides and shows the topics of a channel. `navigation/topics-tree-side-pane` keeps the tree beside the page of the topic.

## States

- `tree`: a list of channels. The topics of a channel hang from a tree line below the mark of that channel. A row with new messages shows their count at its end. Opens on: the Channels row of the menu.
- `topic`: the page of one topic or one channel, with Back and its name. A plain box stands for the rest of the page. Opens on: tap on a topic row or a channel row.
- `tree-selected`: the tree again. The row of the page that the person left has a soft fill. Opens on: Back.
- `empty`: one sentence that says the person is in no channel. Opens on: an account with no channels. The source shows no empty tree.

## Transitions

- `tree` to `topic`. Trigger: tap on a row. Moves: while the finger is down, the row shrinks to `scale(0.96)` and its `background-color` becomes a soft fill. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `tree` to `topic`. Trigger: the same tap. Moves: the tree leaves to the left with `push-exit`, and the page comes in from the right with `push-enter`. 520 ms, linear(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `topic` to `tree-selected`. Trigger: tap on Back. Moves: the page leaves to the right with `back-exit`, and the tree comes in from the left with `back-enter`. 520 ms, the same `linear()` spring. measured.

## Hard cases

- Channel with no topics: the row shows with no tree line below it.
- Last topic: the tree line stops at the last topic of the channel. It does not go on to the next channel.
- Long name: in the narrow column of the wide layout, a long channel name ends with an ellipsis. The count stays visible.
- Wide screen: from 736 px, the source keeps the tree in a column beside the page, and the open row keeps the soft fill. `navigation/topics-tree-side-pane` draws this layout.
- Reduced motion: the source plays none of these animations.
- Empty, error and slow network: the source shows no such state. The `empty` state is drawn.

## Notes

- The tree line shows which channel a topic is part of, with no indent text and no second screen. Keep the line when the look changes.
- The soft fill marks only where the person is. A count marks where new messages are. Keep these two marks different.
- A channel row and a topic row open a page in the same way. Thus the person does not learn two rules.
- The sketch leaves out the Back button of the source tree, which goes to the menu of that app. The marks on an avatar are in `chat/avatar-badges`.
- The content of the page is not part of this pattern. The sketch draws it as a plain box.
