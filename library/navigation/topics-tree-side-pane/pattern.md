# Topics tree with a side pane

Captured: 2026-11-20, recorded by an agent
Best for: a chat product on a screen from 600 px wide, where a person changes between topics and keeps the tree in view.
Row opens: in a pane
Related: `navigation/topics-tree` opens the topic on its own page, for a phone. `navigation/topics-tree-collapsible` hides and shows the topics of a channel.

## States

- `tree`: the tree in a column at the left. The pane at the right says that no topic is open. A row with new messages shows their count at its end. Opens on: the Channels row of the menu.
- `topic`: the open row has a soft fill. The pane at the right shows the name of the topic or the channel. A plain box stands for the rest of the page. Opens on: tap on a topic row or a channel row.
- `empty`: one sentence in the left column says the person is in no channel. Opens on: an account with no channels. The source shows no empty tree.

## Transitions

- `tree` to `topic`. Trigger: tap on a row. Moves: while the finger is down, the row shrinks to `scale(0.96)` and its `background-color` becomes a soft fill. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The pane changes at once.

## Hard cases

- Channel with no topics: the row shows with no tree line below it.
- Last topic: the tree line stops at the last topic of the channel. It does not go on to the next channel.
- Long name: a long channel name ends with an ellipsis. The count stays visible.
- Narrow screen: below 600 px, the tree column takes 44% of the width, and at least 150 px. Use `navigation/topics-tree` on a phone.
- Reduced motion: the row shows the press at once.
- Empty, error and slow network: the source shows no such state. The `empty` state is drawn.

## Notes

- The tree line shows which channel a topic is part of, with no indent text and no second screen. Keep the line when the look changes.
- The soft fill marks only where the person is. A count marks where new messages are. Keep these two marks different.
- The tree stays in view, so the person changes the topic with one tap.
- The source shows this layout from 736 px. The marks on an avatar are in `chat/avatar-badges`.
- The content of the page is not part of this pattern. The sketch draws it as a plain box.
