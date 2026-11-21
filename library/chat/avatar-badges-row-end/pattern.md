# Avatar badges at the end of the row

Captured: 2026-11-20, recorded by an agent
Best for: a chat product with small avatars, or with rows that have no avatar, where a person sees which chats have new messages.
Row opens: on the record's own page. The sketch shows a sample message in place of the page.
Related: `chat/avatar-badges` puts the dot and the count on the avatar. `chat/avatar-badges-counts` shows a count on each avatar with new messages. `chat/chat-list` draws the rows.

## States

- `no-new`: a list of chats with no new messages. The avatar of the main assistant has a star badge at its bottom right. A plain box stands for the rest of each row. Opens on: the person opens each chat that has a mark.
- `new-messages`: the row of a person with new messages has a dot at its end. The row of a group has a count at its end. An avatar keeps only the star. The Menu button has a count of the new messages in the screens that it opens. Opens on: a new message.
- `over-limit`: a count of more than 99 shows as "99+". Opens on: the 100th new message. The source shows no count this large.

## Transitions

- `no-new` to `new-messages`. Trigger: a new message. Moves: the mark shows at once. The marks of the source have no animation, and the source shows no arrival of a message.
- `new-messages` to `no-new`. Trigger: tap on the row. Moves: while the finger is down, the row shrinks to `scale(0.96)` and its `background-color` becomes a soft fill. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The mark goes away at once when the chat opens.

## Hard cases

- Large count: a count of more than 99 shows as "99+". The badge becomes wider, and the rest of the row becomes narrower. This case is drawn.
- Small avatar: in the row of a search result, the source moves the count to the end of the row.
- Colour: the source gives the dot and the count one accent colour. The star badge has the colour of the avatar ring.
- Empty, error and slow network: the source shows no such state for a mark.

## Notes

- Each mark has one meaning and one place. The star on the avatar says which chat. The dot and the count at the end of the row say that messages wait.
- A dot is sufficient for one person. A count is for a group and for a button, where the number helps the person choose.
- A button that leads to rows with counts shows their sum. Thus the person sees the new messages before the button is pressed.
- Give each mark a name for a screen reader, such as "4 new messages". The sketch has one ink, so the dot and the count are solid ink.
- The sketch leaves out the face picture and the colours of the source avatars. It shows initials.
- The name, the last message and the time of a row are in `chat/chat-list`. The sketch draws them as a plain box.
- The designer drew this pattern from `chat/avatar-badges`. The source shows this layout only for a count in the row of a search result.
