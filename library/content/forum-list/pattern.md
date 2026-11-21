# community: forum of posts

Captured: 2026-11-20, from public pictures.
Best for: a product where each post starts a discussion that members come back to. A member finds a discussion or starts one.
Row opens: in a pane. On a wide screen the list stays beside the post. Under 1000 px the pane takes the place of the list, and a back link returns to the list.

## States

- `feed`: a bar with the product name. Under it, the title, and a field that searches the posts or starts a new post, with a New post button. Then a sort control and the tags as chips, and the posts as cards. Each card has a tag, a more button, a title, two lines of the text with the name of the author, and a small picture if the post has one. Its last row has the count of reactions, the count of comments, a mark for new comments and the age. Opens on: the link of the forum.
- `sorted`: the sort control shows the second order, and the cards stand in that order. Opens on: a choice in the sort control.
- `tag-filter`: one tag chip is pressed, and the list shows only the cards with that tag. The filter applies at once. The source shows no pressed tag. Opens on: a click on a tag chip.
- `post`: the pane of one post. On a wide screen it stands at the right of the list, and the open card has a fill. The pane has a copy link button and a close button, then the title, the tag, the author with the avatar, the mark "Author" and the age, the text and the picture. Then a row with the reactions as chips with a count, an add reaction button and a follow button. Under them, the comments, as a plain box with the name `comment-comment-thread`. Opens on: a click on the title of a card.
- `reaction-added`: one reaction chip of the post is pressed, and its count is one more. A click on the chip removes the reaction. Opens on: a click on a reaction chip.
- `empty`: a heading and one sentence under the field. The source shows no empty state. Opens on: a forum with no posts.

## Transitions

The source is a picture, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `feed` to `sorted`. Trigger: a choice in the sort control. Moves: not seen.
- `feed` to `tag-filter`. Trigger: a click on a tag chip. Moves: not seen.
- `feed` to `post`. Trigger: a click on the title of a card. Moves: not seen.
- `post` to `feed`. Trigger: a click on the close button, or on the back link on a narrow screen. Moves: not seen.
- `post` to `reaction-added`. Trigger: a click on a reaction chip. Moves: not seen.

## Hard cases

- Empty: the `empty` state. It is the designer's choice.
- Long text: a card shows two lines of the text and cuts the rest. The pane shows the full text.
- Narrow screen: under 1000 px the pane takes the place of the list. At 390 px the sort control and the tags wrap to two rows, and each card takes the full width.
- Many tags, failed load and slow network: not seen.

## Variations

- `base`: the layout of the source picture.

Until round `rev_e93e264e511e` this pattern was the variation `forum` of `feed-feed`. In that round the owner chose that each layout is its own pattern, so this record has only `base`.

## Notes

- Job: the member finds a discussion or starts one. The title and the tag carry the subject, so a card needs only two lines of the text. The pane keeps the list in view, so the member reads one discussion and then moves to the next one.
- The owner chose one pattern for each part of a screen in round `rev_e93e264e511e`. So the comments are the pattern `comment-comment-thread`. The row menu, the composer and the reaction picker are parts of the pattern `feed-feed`. The sketch draws a plain box for each. The more button of a card opens a menu with a box, and the New post button and the add reaction button each open a popover with a box.
- A post of a forum needs a title and tags. The composer of `feed-feed` has a group chooser and a text field. A product that uses this pattern adds a title field and the tags to that composer.
- The picture shows the cards with their tags, the field with its button and the sort control. These parts are the designer's choice: the tag filter, the pressed reaction and the empty state.
- No fact of this pattern was checked in a real app.
- Keep these parts when the look changes: the title and the tag on each card, the field that searches and starts a post, and the "Row opens" value.
- The sketch keeps no brand, colour, text or picture of the source. The sample posts are fabricated.
