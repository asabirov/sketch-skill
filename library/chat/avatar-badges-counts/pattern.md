# Avatar badges with counts

Captured: 2026-11-20, recorded by an agent
Best for: a chat product where the number of new messages changes what the person opens first, such as a support inbox.
Row opens: on the record's own page. The sketch shows a sample message in place of the page.
Related: `chat/avatar-badges` shows a dot for a person and a count for a group. `chat/avatar-badges-row-end` puts the dot and the count at the end of the row. `chat/chat-list` draws the rows.

## States

- `no-new`: a list of chats with no new messages. The avatar of the main assistant has a star badge at its bottom right. A plain box stands for the rest of each row. Opens on: the person opens each chat that has a mark.
- `new-messages`: each avatar with new messages has a count at its top right. No dot shows. The Menu button has a count of the new messages in the screens that it opens. Opens on: a new message. The source shows a dot on the avatar of a person.
- `over-limit`: a count of more than 99 shows as "99+". Opens on: the 100th new message. The source shows no count this large.

## Transitions

- `no-new` to `new-messages`. Trigger: a new message. Moves: the mark shows at once. The marks of the source have no animation, and the source shows no arrival of a message.
- `new-messages` to `no-new`. Trigger: tap on the row. Moves: while the finger is down, the row shrinks to `scale(0.96)` and its `background-color` becomes a soft fill. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The mark goes away at once when the chat opens.

## Hard cases

- Large count: a count of more than 99 shows as "99+", and the badge becomes wider to the left. This case is drawn.
- Star and count together: the star is at the bottom right and the count is at the top right. The sketch shows no avatar with the two marks.
- Small avatar: in the row of a search result, the source moves the count to the end of the row.
- Wide screen: from 736 px, the avatars are in a column at the left. The marks keep their corners.
- Colour: the source gives the dot and the count one accent colour. The star badge has the colour of the avatar ring.
- Empty, error and slow network: the source shows no such state for a mark.

## Notes

- Each mark has one meaning and one corner. The star says which chat. The count says that messages wait. Keep the two corners when the look changes.
- A count on each avatar lets the person compare the chats. Use the dot of `chat/avatar-badges` when the number does not help the person choose.
- A button that leads to rows with counts shows their sum. Thus the person sees the new messages before the button is pressed.
- Give each mark a name for a screen reader, such as "4 new messages". The sketch has one ink, so the count is solid ink.
- The sketch leaves out the face picture and the colours of the source avatars. It shows initials.
- The name, the last message and the time of a row are in `chat/chat-list`. The sketch draws them as a plain box.
- The designer drew this pattern from `chat/avatar-badges`. The source shows a dot on the avatar of a person.
