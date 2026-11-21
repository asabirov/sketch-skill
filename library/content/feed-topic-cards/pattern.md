# Feed of topic cards

Captured: 2026-11-20, from public pictures.
Best for: a product where each post starts a discussion that members come back to. A member finds a discussion or starts one.
Row opens: in a pane. On a wide screen the list stays beside the post. Under 1000 px the pane takes the place of the list, and a back link returns to the list.
Related: `content/feed-full-posts` has a full post in each row, and its row opens in place. `content/feed-short-posts` has short posts with a row of counts, and its row opens the page of the post. `content/comment-thread` draws the comments, and `notifications/follow-menu` draws the follow menu.

## States

- `feed`: a bar with the product name. Under it, the title, and a field that searches the posts or starts a new post, with a New post button. Then a sort control and the tags as chips, and the posts as cards. Each card has a tag, a more button, a title and two lines of the text with the name of the author. A card of a post with a picture has a small plain box at its right. A card of a post with a video has a small plain box with a play mark. The mark is no control, because the whole card opens the post. Its last row has the most used reaction as an emoji with the count of the reactions, a comment icon with the count of the comments, a mark for new comments and the age. A count has no word. The first card is the pinned post, with a pin mark before its tag. The whole card opens the post. Opens on: the link of the forum.
- `sorted`: the sort control shows the second order, and the cards stand in that order. Opens on: a choice in the sort control.
- `tag-filter`: one tag chip is pressed, and the list shows only the cards with that tag. The filter applies at once. The source shows no pressed tag. Opens on: a click on a tag chip.
- `post`: the pane of one post. On a wide screen it stands at the right of the list, and the open card has a fill. The pane has a copy link button and a close button, then the title, the tag, the author with the avatar, the mark "Author" and the age, the full text and the picture as a plain box. Then a row with the reactions, an add reaction button and a follow button. A reaction is a chip with an emoji and a count, and no word. The follow button opens a popover with a plain box with the name `notifications/follow-menu`. Under them, the comments with their comment field, as a plain box with the name `content/comment-thread`. Opens on: a click on a card.
- `reaction-added`: one reaction chip of the post is pressed, and its count is one more. A click on the chip removes the reaction. Opens on: a click on a reaction chip.
- `compose`: the form of a new post stands in the place of the field. It has a title field with the focus, a message field, the tags as chips with one pressed, an attach button, Cancel and Post. Post is off until the title has text. The list stays under the form. Opens on: a click on the New post button.
- `empty`: a heading and one sentence under the field. The source shows no empty state. Opens on: a forum with no posts.

## Transitions

The source is a picture, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `feed` to `sorted`. Trigger: a choice in the sort control. Moves: not seen.
- `feed` to `tag-filter`. Trigger: a click on a tag chip. Moves: not seen.
- `feed` to `post`. Trigger: a click on a card. Moves: not seen.
- `feed` to `compose`. Trigger: a click on the New post button. Moves: not seen.
- `compose` to `feed`. Trigger: a click on Cancel or on Post. Moves: not seen.
- `post` to `feed`. Trigger: a click on the close button, or on the back link on a narrow screen. Moves: not seen.
- `post` to `reaction-added`. Trigger: a click on a reaction chip. Moves: not seen.

## Hard cases

- Empty: the `empty` state. It is the designer's choice.
- Pinned post: it is the first card in each order and with each tag filter that holds it. The pin mark before the tag comes from the source picture.
- Long text: a card shows two lines of the text and cuts the rest with 3 dots. The pane shows the full text. The card has no "Show more" button, because the whole card opens the post.
- Picture and video: a card shows a small box for a picture, and a small box with a play mark for a video. The pane shows the picture at the width of the pane. The source picture shows a small picture on a card and no video.
- Narrow screen: under 1000 px the pane takes the place of the list. At 390 px the sort control and the tags wrap to two rows, and each card takes the full width.
- Many tags, failed load and slow network: not seen.

## Notes

- Job: the member finds a discussion or starts one. The title and the tag carry the subject, so a card needs only two lines of the text. The pane keeps the list in view, so the member reads one discussion and then moves to the next one.
- Until round `rev_e93e264e511e` this pattern was the variation `forum` of `content/feed-full-posts`. In that round the owner chose that each layout is its own pattern.
- The owner chose one pattern for each part of a screen in round `rev_e93e264e511e`. So the comments are the pattern `content/comment-thread`. The row menu and the reaction picker are parts of the pattern `content/feed-full-posts`, and the follow menu is the pattern `notifications/follow-menu`. The sketch draws a plain box for each. The more button of a card opens a menu with a box, and the add reaction button and the follow button each open a popover with a box.
- A post of a forum needs a title and tags, so this pattern has its own form of a new post. It opens in the place of the field. The picture does not show the open form. The composer of `content/feed-full-posts` is a dialog with a group chooser and no title.
- The owner asked for these changes in round `rev_4b4cb0185c58`: a better post row from the references, reactions as emoji with no word, and a pinned post at the top. The earlier card had the counts as words, such as "5 reactions" and "12 comments". The card now follows the picture: an emoji with a count, a comment icon with a count, and the age. The sketch has one ink, so it draws each emoji in grey.
- The picture shows the cards with their tags, the field with its button and the sort control. These parts are the designer's choice: the tag filter, the pressed reaction, the fields of the open form and the empty state.
- The owner asked in round `rev_7719a47974c2` for a post with a picture and a post with a video, an answer for a long text, and a way to leave a comment from the feed. A card is a summary of a post, so the member leaves a comment in the pane. The comment field is a part of the pattern `content/comment-thread`, and the plain box in the pane names it. The other 2 feed patterns open a comment field under the row.
- No fact of this pattern was checked in a real app.
- Keep these parts when the look changes: the title and the tag on each card, the counts with no word, the pinned post at the top, the field that searches and starts a post, and the "Row opens" value.
- The sketch keeps no brand, colour, text or picture of the source. The sample posts are fabricated.
