# Portfolio profile

Captured: 2026-11-20, from public pictures.
Best for: a product where the value of a member is the work that the member published. A visitor finds the work of a member and decides whether to follow or hire the member.
Row opens: on the record's own page. A card of the grid opens the page of that work, and the identity stays beside it.
Related: `profile/member-profile` is a public page with the posts of a member under the identity. `profile/profile-card` is a card over a conversation.

## States

- `profile`: a bar with the product name, and two columns under it. The side column has the avatar, the name and the pronouns, a short bio, the counts of followers and following as links, a follow button and a row of link buttons. The main column has 2 pill tabs, a control for the kind of work, and the work as a grid of cards. Each card has a picture, a title and a count of uses. Opens on: a click on a name or an avatar.
- `scrolled`: the grid moved up, and the tabs are out of view. The side column stays in view, so the visitor always sees whose work this is. Opens on: a scroll down the grid.
- `work`: the page of one work in the main column. A back link to the grid, the title, a large picture, one sentence, the count of uses, a like button with a count and one main button. The side column does not change. Opens on: a click on a card.
- `empty`: the profile of an owner with no content. The second tab is selected. Each box of the tab has a heading and a prompt button, such as "Add your work". A prompt button for the bio stands in the side column. A visitor does not see an empty box. Opens on: the owner's own profile before the first entry.

## Transitions

The source is a picture, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `profile` to `scrolled`. Trigger: a scroll down the grid. Moves: not seen.
- `profile` to `work`. Trigger: a click on a card. Moves: not seen.
- `work` to `profile`. Trigger: a click on the back link. Moves: not seen.

## Hard cases

- Empty: the `empty` state. It comes from the picture, which shows the "About me" tab of an owner with empty boxes and prompts.
- Narrow screen: under 820 px the side column stands above the main column. At 390 px the grid has one column of cards, and the tabs and the kind control stay in one row.
- Long name and long bio: the text wraps in the side column.
- Many works, a failed load, a slow network and a private profile: not seen.

## Notes

- Job: the visitor finds the work of the member and decides whether to follow or hire the member. The work needs a grid, and the identity stays beside it, so the visitor always sees whose work this is. Each box of the second tab holds one kind of fact. An empty box shows a prompt to the owner and does not show to a visitor.
- Until round `rev_e93e264e511e` this pattern was the variation `portfolio` of `profile/member-profile`. In that round the owner chose that each layout is its own pattern. This pattern is the two columns of the source picture.
- The picture shows the side column and the "About me" tab of an owner. These parts are the designer's choice: the grid of work, the page of one work, the follow button, the kind menu and the scrolled form. A click on the follow button shows only a toast. The two tabs change the content in place, in each state.
- The sign-in prompt is a part of the pattern `profile/member-profile`. This sketch does not draw it. A product that needs a sign-in for the follow button opens that prompt.
- No fact of this pattern was checked in a real app.
- Keep these parts when the look changes: the identity beside the work, the grid of cards, and one box for each kind of fact.
- The sketch keeps no brand, colour, text or picture of the source. The sample member is fabricated.
- The source shows a handle with the name. The sketch shows the display name only, because a sample handle can be the handle of a real account.
