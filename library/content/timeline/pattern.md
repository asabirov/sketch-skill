# X: timeline of short posts

Captured: 2026-11-20, from public pictures.
Best for: a product where members post short messages many times a day and the feed has no end. A member sees what happens now and decides on each post in a few seconds.
Row opens: on the record's own page. A click on the text or on the reply count of a row opens the page of the post.

## States

- `feed`: a bar with the product name. Under it, the title, the tabs "For you" and "Following" with a plus button after them, and the posts. Each row is a short post with the author's avatar at the left. It has the name, the handle, the age and a more button, then the text, a picture if the post has one, and an action row. The action row has a reply count, a repost count, a like count, a view count and a share button. A round compose button stays at the bottom right. A wide screen adds a column with a search field and a list of trends. Opens on: the home link of the product.
- `tab-following`: the second tab is selected, and the list shows only the posts of the members that the member follows. Opens on: a click on the tab.
- `liked`: the like button of the first row is pressed, and its count is one more. A click on the button removes the like. Opens on: a click on the like button.
- `post`: the page of one post. A back link with the title "Post", then the author with the avatar, the name and the handle, the text in a larger size, the time, a row of counts, and an action row with repost, like and share. Under them, the replies, as a plain box with the name `comment-comment-thread`. Opens on: a click on the text or on the reply count of a row.
- `custom-feed`: a panel under the tabs with a heading, a search field for a topic, the topics as chips, Cancel and Pin. The source shows no such panel. Opens on: a click on the plus button after the tabs.
- `feed-saved`: the pinned topic is one more tab, and it is selected. The list shows the posts of that topic, and a toast confirms the pin. The source shows no such state. Opens on: Pin.
- `empty`: a heading, one sentence and a button that opens the panel of topics. The source shows no empty state. Opens on: a feed with no posts.

## Transitions

The source is a set of pictures, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `feed` to `tab-following`. Trigger: a click on the tab. Moves: not seen.
- `feed` to `liked`. Trigger: a click on the like button. Moves: not seen.
- `feed` to `post`. Trigger: a click on the text or on the reply count of a row. Moves: not seen.
- `post` to `feed`. Trigger: a click on the back link. Moves: not seen.
- `feed` to `custom-feed`. Trigger: a click on the plus button. Moves: not seen.
- `custom-feed` to `feed-saved`. Trigger: a click on Pin. Moves: not seen.

## Hard cases

- Empty: the `empty` state. It is the designer's choice.
- Long text: the sketch cuts a long post in the row and ends it with "Show more". The page of the post shows the full text.
- Narrow screen: under 1000 px the column with the search field and the trends does not show. At 390 px each row takes the full width, and the compose button stays at the bottom right.
- End of the feed, failed load, slow network, and more tabs than the row holds: not seen.

## Variations

- `base`: the layout of the source pictures.

Until round `rev_e93e264e511e` this pattern was the variation `timeline` of `feed-feed`. In that round the owner chose that each layout is its own pattern, so this record has only `base`.

## Notes

- Job: the member sees what happens now. A post is short, so each row holds the whole post, and the member decides on each row in a few seconds. The counts on each row show how other members reacted. The replies do not fit in the row, so the row opens the page of the post.
- The owner chose one pattern for each part of a screen in round `rev_e93e264e511e`. So the replies are the pattern `comment-comment-thread`, and the row menu and the composer are parts of the pattern `feed-feed`. The sketch draws a plain box for each: the more button opens a menu with a box, and the compose button opens a dialog with a box.
- The pictures show the rows, the more button, the compose button and a plus button after the tabs. These parts are the designer's choice: the panel that pins a topic as a tab, the pressed like button and the empty state.
- X needs a sign-in for the home timeline, and the capture never signs in. So no fact of this pattern was checked in the real app. A signed-out public profile on the web shows the same row parts: avatar, name, handle, age, more button, text, picture and action row.
- Keep these parts when the look changes: the whole post in the row, the action row with counts on each row, the compose button that stays on the feed, and the "Row opens" value.
- The sketch keeps no brand, colour, text or picture of the source. The sample rows are fabricated.
