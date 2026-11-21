# Comment tree with votes

Captured: 2026-11-20, from public pictures. An agent took a picture of the public page at 1280 px.
Best for: a product where many members answer one post, and an answer gets its own answers. A reader follows one branch and closes a branch that does not help.
Row opens: in place. A branch closes and opens in the tree, and the reply field opens under its comment.
Related: `content/comment-thread` has one level of replies in a box for each thread, and reactions in place of votes. `content/feed-full-posts` draws the post.

## States

- `thread`: a plain box for the post, a part of `content/feed-full-posts`. Under it, the field for a new comment and its Comment button, in one row. The field is one line, and it grows with its text. The button is off until the field has text. Clear space stands after this group. Then the sort control stands right above the comments that it sorts, and the comments are a tree. A comment has the avatar and the name of the author and the age on one line, then the text, then one row of actions: a vote up button, the points, a vote down button, a Reply button and a more button. A line runs down from the avatar, and the replies stand at the right of that line. So each level moves the width of one avatar to the right. The first comment has a round button with a minus on its line. A comment of the author of the post has the mark "Author". A branch with more replies ends with a control that has their count. Opens on: the page of a post.
- `vote`: the vote up button of the first comment is pressed. Its arrow stands in a filled circle, and the points are one more. A click on the button removes the vote. Opens on: a click on the vote up button.
- `collapsed`: the first comment is one line with a round plus button, the author, the age and the count of its replies. Its text, its actions and its replies do not show. Opens on: a click on the round minus button.
- `more-replies`: the 2 hidden replies of the first comment show, and the control is gone. Opens on: a click on the control.
- `reply-form`: a reply field of one line under the actions of the first comment, above its replies. It has the focus, and a Cancel button and a Reply button stand next to it. The field grows when the member types. Reply is off until the field has text. Opens on: a click on the Reply button of the first comment.
- `reply-sent`: the reply of the member is the first reply of the first comment. Opens on: Reply.
- `comment-menu`: a menu with 3 items, each with an icon: copy the link, follow the replies, and report. Opens on: a click on the more button of the first comment.
- `empty`: the field for a new comment and the sentence "No comments yet.". The sort control does not show. The source page has comments, so the capture did not see this state. Opens on: a post with no comment.

## Transitions

The capture read the source from a picture, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `thread` to `vote`. Trigger: a click on the vote up button. Moves: not seen.
- `thread` to `collapsed`. Trigger: a click on the round minus button. Moves: not seen.
- `collapsed` to `thread`. Trigger: a click on the round plus button. Moves: not seen.
- `thread` to `more-replies`. Trigger: a click on the control with the count. Moves: not seen.
- `thread` to `reply-form`. Trigger: a click on Reply. Moves: not seen.
- `reply-form` to `reply-sent`. Trigger: a click on Reply next to the field. Moves: not seen.
- `thread` to `comment-menu`. Trigger: a click on the more button. Moves: not seen.

## Hard cases

- Deep tree: each level moves the width of one avatar to the right. At 390 px the avatar is smaller, so 3 levels keep a column of text that a person can read. The source ends a deep branch with a control for more replies, and the sketch does the same.
- Comment with no reply: it has no line under its avatar.
- Empty: the `empty` state. It is the designer's choice.
- Long text: the text wraps in its column. A long word breaks at the edge.
- Long reply: the reply field and the comment field grow with their text to 196 px. Then the text scrolls in the field.
- Narrow screen: at 390 px the Cancel button and the Reply button stay next to the reply field, also in a reply of the second level.
- Negative points, a deleted comment with replies, a failed send and a slow network: not seen.

## Notes

- Job: the reader sees which comment an answer belongs to at each depth, and the votes put the best answers first. The round button closes a branch, so a long discussion stays short for a reader who wants only one part of it.
- The owner did not like the earlier comments, in round `rev_4b4cb0185c58`, and asked for variants of the feed parts. The pattern `content/comment-thread` has one level of replies in a box, and reactions. This pattern is the second thread: a tree with votes and no reactions. A product chooses one.
- The source has these parts, and the sketch leaves them out: an Award button and a Share button in the row of actions, a mark for an archived comment, the word "Edited", and a search field for the comments.
- These parts differ from the source. The source shows the round button at the height of the actions. The sketch puts it at the top of the line, under the avatar. The source shows the mark "OP" for the author of the post. The sketch uses the word "Author", as `content/comment-thread` does.
- The capture read the page signed out, so it did not vote and did not open a form. These parts are the designer's choice: the pressed vote, the reply field, the sent reply, the items of the more menu and the empty state.
- The owner asked for 2 changes in round `rev_7719a47974c2`. The reply form was too big, so the reply field now starts as one line and grows when the member types, with Cancel and Reply next to it. The sort control stood closer to the comment field than to the comments, in one row with the Comment button. Now the field and its button are one group, clear space follows, and the sort control stands right above the comments.
- The post above the tree is a part of the pattern `content/feed-full-posts`, so the sketch draws a plain box for it.
- In the sketch, only the first comment takes a vote, closes, opens the reply field and opens the more menu. The Reply button of each other comment shows a toast.
- Keep these parts when the look changes: the line from each avatar with the replies at its right, the votes with the points on each comment, the button that closes a branch, and the control for more replies.
- The sketch keeps no brand, colour, text or picture of the source. The sample comments are fabricated. The pictures are not committed.
