# direct-message: direct messages

Captured: 2026-11-12, from public pictures
Best for: a chat app where one-to-one and small group conversations get their own page. Use it for a list of conversations beside the open conversation, with a reading pane and a composer.

## States

- `list`: the "Direct messages" heading with a filter for unreads and a new-message button. The list of conversations. From 600 px, the pane on the right asks the person to pick a conversation. Opens on: the DMs link in the rail.
- `conversation`: the selected row has the wash. The pane shows the name, the messages, the reactions with counts, a reply link with the time of the last reply, and a composer. On a phone the pane replaces the list and has a Back button. Opens on: a click on a row.
- `unreads`: the list holds only the unread conversations, with a way back to all. Opens on: the unreads filter.
- `empty`: no conversations, with "New message". Opens on: a new account.

A row has an avatar, the name, a preview of two lines and a time. An unread row is bold and has a filled count. A group conversation lists its names.

## Transitions

The source pages give no motion values. Each value below is the designer's choice from the kit motion tokens.

- `list` to `conversation`. Trigger: a click on a row. Moves: the pane fades in (opacity 150 ms, cubic-bezier(0.4, 0, 0.2, 1)). estimated.
- `list` to `unreads`. Trigger: a click on the unreads filter. Moves: nothing. The list changes in place. estimated.

## Hard cases

- Long preview: the preview stops after two lines with an ellipsis.
- Many names in a group conversation: the names wrap in the title.
- A reaction that the person added: its chip is pressed. A second click removes it.
- Empty list and failed load: not seen.

## Notes

- The unread count on a row and on the rail are the same signal at two levels.
- The reply link opens a thread. The sketch keeps it as plain text, because only this app has it.
- The sketch keeps no brand, text or picture of the source. The sample rows are fabricated.
- The cut frames are not committed.
