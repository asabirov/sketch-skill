# community: inbox popover and channel

Captured: 2026-11-12, from public pictures
Best for: a community chat where unread messages from many channels and servers come to one popover, grouped by channel. Use it for an inbox that opens over the open channel from an icon button, with tabs for unreads and mentions.

## States

- `channel`: the channel list on the left and the open channel on the right. The channel has a head with search and the inbox button, the messages with a day label, a mention in bold, reactions, and a composer with a plus button. Opens on: a click on a channel.
- `for-you`: the inbox popover on the "For you" tab. It holds events about the person, such as a reaction to their message. Opens on: the inbox button.
- `unreads`: the "Unreads" tab. The messages are grouped by channel. A group heading has a chevron that folds the group, a square server avatar, the channel name, the server name and a filled count. At the end of the heading, a bell mutes the channel and a check marks it read. A check in the inbox head marks the whole inbox read. Opens on: the Unreads tab.
- `mentions`: the "Mentions" tab. Each row shows the channel and the server above the message. On hover, a row shows "Jump" and a remove button. The sketch shows the actions on the first row. Opens on: the Mentions tab.
- `mention-filter`: the filter button is pressed. Three switches choose what counts: everyone and here mentions, role mentions, and all servers. Opens on: the filter button in the Mentions tab.
- `empty`: no mentions, with the rule that mentions stay for 7 days. Opens on: the last mention removed.

## Transitions

The source pages give no motion values. Each value below is the designer's choice from the kit motion tokens.

- `channel` to `unreads`. Trigger: a click on the inbox button. Moves: the popover fades in (opacity 150 ms, cubic-bezier(0.4, 0, 0.2, 1)). estimated.
- A group folds. Trigger: a click on the group heading. Moves: the chevron turns 90 degrees (transform 150 ms, cubic-bezier(0.4, 0, 0.2, 1)). estimated.
- `unreads` to `mentions`. Trigger: a click on a tab. Moves: nothing. The list changes in place. estimated.

## Hard cases

- Many groups: the sketch shows three groups, and the kit popover has no maximum height. A built inbox needs a maximum height and a scroll inside the popover.
- A folded group: the chevron points right and the rows hide. The count stays on the heading.
- Narrow screen: the popover takes the screen width less 8 px on each side. The source shows no phone picture, so this is the designer's choice.
- Failed load: not seen.

## Notes

- Keys from the documentation: Ctrl+I opens the inbox, and Ctrl+Shift+E marks the inbox read.
- Mentions clear after 7 days.
- The source shows a mention as a filled chip in the text. The sketch keeps it as bold text, because the kit is one ink.
- The sketch keeps no brand, text or picture of the source. The sample rows are fabricated.
- The cut frames are not committed.
