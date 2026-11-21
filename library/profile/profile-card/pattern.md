# Profile card

Captured: 2026-11-20, from public pictures.
Best for: a product where members meet in a conversation. A visitor needs a short answer to "who is this" and then continues the conversation.
Row opens: no rows.
Related: `profile/member-profile` is a public page with the posts of a member under the identity. `profile/portfolio-profile` puts the work of a member in a grid beside the identity.

## States

- `card`: the profile is a card over the dimmed conversation, and the conversation stays. The card has a banner, an avatar over the edge of the banner with a mark for the presence, a row of icon buttons with a close button, and the name. The icon buttons are one badge, a more button and the close button. Under them, an about text, the member date, a link to the shared groups, and a private note field. Opens on: the link of the small card, or a click on an avatar.
- `mini`: a small card next to a name in the conversation. It has a small banner and avatar, the name, the member date, the role, a note field and a link to the full card. Opens on: a click on a name in the conversation.
- `empty`: the card of a member with no about text. The card has no heading for the about text, and each other part stays. Opens on: a member who wrote no about text.

## Transitions

The source is two pictures, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `mini` to `card`. Trigger: a click on the link of the small card. Moves: not seen.
- `card` to the conversation. Trigger: a click on the close button or on the dimmed page, or Escape. Moves: not seen. The sketch shows the conversation with no card.

## Hard cases

- Empty: the `empty` state. It is the designer's choice.
- Narrow screen: at 390 px the card takes the width of the screen, and each part keeps its order.
- Long about text, many shared groups and a long note: not seen.
- The member's own card, a blocked member and a slow network: not seen.

## Notes

- Job: in the middle of a conversation, the visitor learns who this is and then continues. So the profile comes to the visitor and does not replace the page. The card shows what the two people share, because that matters more in a chat than a history. The card has no counts and no stream of posts.
- Until round `rev_e93e264e511e` this pattern was the variation `card` of `profile/member-profile`. In that round the owner chose that each layout is its own pattern. This pattern is the card of the source pictures.
- The source also has a third size, a panel beside a direct conversation. The sketch does not draw it.
- The pictures show the full card with two tabs, and the small card next to a name. These parts are the designer's choice: the more menu, the badge popover and the empty card. The more menu and the badge popover open on a click, in each state.
- The owner removed these parts in round `rev_4b4cb0185c58`: the activity of the member, the badge with the check mark, the friend request button and the message button. The source has each of them. So the card has no tabs, because the second tab held the activity. The small card has no line for what the member does now. The link to the shared friends is also gone, because the card has no friend action.
- The conversation behind the card is only a background. The sketch draws 3 messages and a message field, and they take no input.
- The sign-in prompt is a part of the pattern `profile/member-profile`. This sketch does not draw it.
- No fact of this pattern was checked in a real app.
- Keep these parts when the look changes: the conversation that stays behind the card, the two sizes of the card, and the facts that the two people share.
- The sketch keeps no brand, colour, text or picture of the source. The sample member is fabricated.
- The source shows a handle with the name. The sketch shows the display name only, because a sample handle can be the handle of a real account.
