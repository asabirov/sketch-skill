# Feed of short posts

Captured: 2026-11-20, from public pictures.
Best for: a product where members post short messages many times a day and the feed has no end. A member sees what happens now and decides on each post in a few seconds.
Row opens: on the record's own page. A click on a row opens the page of the post. The reply button of a row opens a reply field of one line under the row.
Related: `content/feed-full-posts` has a full post with a title in each row, and its row opens in place. `content/feed-topic-cards` has a card with a title for each post, and its card opens the post in a pane. `content/comment-thread` draws the replies.

## States

- `feed`: a bar with the product name. Under it, one column. First the field for a new post, with the avatar of the member, a picture button and a Post button. Post is off until the field has text. Then the posts. Each row is a short post with the author's avatar at the left. One line has the name, the age and a more button. The text stands under that line. The name, the age and the text are plain text, and none of them is a link. A row with a picture shows a plain box under the text, and a row with a video shows a plain box with a play button and the length of the video. A long text shows its first 3 lines and a "Show more" button. Then an action row with a reply button, a repost button, a like button, a view count and a share button. Each one is an icon and a number with no frame and no word, and they spread across the width of the row. The first row is the pinned post, with a pin mark and the word "Pinned" above its author line. Opens on: the home link of the product.
- `text-open`: the long row shows its full text and a "Show less" button. The rows below move down. Opens on: a click on "Show more".
- `reply-field`: a reply field of one line stands under the action row of the second row, and the rows below move down. A Cancel button and a Reply button stand next to the field. The field has the focus, and it grows with its text. Reply is off until the field has text. The source shows no such state. Opens on: a click on the reply button of the row.
- `reply-sent`: the field is closed, the reply count of the row is one more, and a toast says "Reply sent". Opens on: a click on Reply.
- `liked`: the like button of the second row is pressed. Its heart is filled, its number is bold, and its count is one more. A click on the button removes the like. Opens on: a click on the like button.
- `post`: the page of one post. A back link with the title "Post", then the author with the avatar and the name, the text in a larger size, the time, and the action row with the counts. The text and the time are plain text. Under them, the replies with their comment field, as a plain box with the name `content/comment-thread`. Opens on: a click on a row.
- `empty`: the field for a new post, a heading and one sentence. The source shows no empty state. Opens on: a feed with no posts.

## Transitions

The source is a set of pictures, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `feed` to `text-open`. Trigger: a click on "Show more". Moves: not seen.
- `feed` to `reply-field`. Trigger: a click on the reply button of a row. Moves: not seen.
- `reply-field` to `reply-sent`. Trigger: a click on Reply. Moves: not seen.
- `feed` to `liked`. Trigger: a click on the like button. Moves: not seen.
- `feed` to `post`. Trigger: a click on a row. Moves: not seen.
- `post` to `feed`. Trigger: a click on the back link. Moves: not seen.

## Hard cases

- Empty: the `empty` state. It is the designer's choice.
- Long text: the row shows the first 3 lines of a long post and a "Show more" button. The button opens the full text in place, and "Show less" closes it. The owner asked for this in round `rev_7719a47974c2`. The pictures show no long post.
- Picture and video: a picture stands under the text of its row. A video is a box with a play button and its length, and it plays in place. The sketch draws each as a plain box.
- Long reply: the reply field grows with its text to 196 px. Then the text scrolls in the field.
- Pinned post: it is the first row, also when newer posts exist. The mark above the author line comes from the second source.
- Narrow screen: the layout is one column at each width. At 390 px each row takes the full width, and the counts stay in one row. The Cancel button and the Reply button stay next to the reply field.
- End of the feed, failed load and slow network: not seen.

## Notes

- Job: the member sees what happens now. A post is short, so each row holds the whole post, and the member decides on each row in a few seconds. The counts on each row show how other members reacted. The replies do not fit in the row, so the row opens the page of the post.
- Until round `rev_e93e264e511e` this pattern was the variation `timeline` of `content/feed-full-posts`. In that round the owner chose that each layout is its own pattern.
- The owner chose one pattern for each part of a screen in round `rev_e93e264e511e`. So the replies are the pattern `content/comment-thread`, and the row menu is a part of the pattern `content/feed-full-posts`. The sketch draws a plain box for each. The more button of the second row opens a menu with a box.
- The pictures show the rows, the more button, a round compose button, and 2 tabs with a plus button after them. The tabs are "For you" and "Following", and they share the width of the column. The owner removed the tabs in round `rev_7719a47974c2`. These parts are the designer's choice: the pressed like button, the reply field and the empty state.
- The owner asked for these changes in round `rev_4b4cb0185c58`: a better post row from the references, no side column with search and trends, no panel that pins a topic as a tab, and a pinned post at the top. The earlier sketch drew each count as a chip with a word, such as "Like 31". The row now follows the pictures: icons with numbers and no frame.
- The field for a new post in the timeline is the designer's choice. The pictures of the phone app show a round compose button. The capture did not see the web app, because its home timeline needs a sign-in. The sketch draws the field at each width, so a member posts from the feed with one step. It differs from the composer of `content/feed-full-posts`, which is a dialog with a group chooser.
- The source needs a sign-in for the home timeline, and the capture never signs in. So no fact of this pattern was checked in the real app. A signed-out public profile on the web shows the same row parts: avatar, name, handle, age, more button, text, picture and action row. The sketch shows the display name only, because a sample handle can be the handle of a real account.
- The owner asked for these changes in round `rev_7719a47974c2`: no tabs, a row with a picture and a row with a video, a cut for a long text, a way to leave a comment from the feed, and no plain text as a link. The earlier sketch made the text of a row a link to the page of the post. Now a link with no text covers the row, so a click on a row opens the page, and each button of the row stays a button.
- The owner named 2 ways to leave a comment: a short field under the post, or the page of the post. The sketch has the short field, as the designer's choice. The member answers in one step and keeps their place in the feed. The page of the post stays the place to read the replies.
- In the sketch, one row has the live reply button, the live like button and the live menu. The reply button of each other row shows a toast that names the live row.
- Keep these parts when the look changes: the whole post in the row, the action row with counts on each row, the reply field under the row, the field for a new post above the rows, the pinned post at the top, and the "Row opens" value.
- The sketch keeps no brand, colour, text or picture of the source. The sample rows are fabricated.
