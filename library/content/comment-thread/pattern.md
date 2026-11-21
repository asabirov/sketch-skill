# Comment thread

Captured: 2026-11-20, from public pictures. An agent took the pictures of the public page at 1280, 768 and 390 px.
Best for: a product where members discuss one post. A reader follows each line of talk, answers in the right place and reacts without a new comment.
Row opens: in place. The earlier replies of a long thread and the reply field open in the thread.
Related: `content/comment-tree` is a tree of comments with votes, and each comment has its own Reply button. `content/feed-full-posts` draws the post and the reaction picker.

## States

- `thread`: a plain box for the post, a part of `content/feed-full-posts`. Under it, a heading and one box for each thread. A box holds a comment, its replies in one level and a reply field, and a line at the left joins the replies. A comment has one line with the avatar and the name of the author and the age, and an add reaction button and a more button at the right. Its text takes the full width of the box. Under the text, one line has the reactions at the left and the count of the replies at the right. A reaction is a chip with an emoji and a count, and no word. A reply has the same parts in a smaller size, and no count of replies. A comment of the author of the post has the mark "Author". Each age is short, such as "2 h". A long thread shows its 2 newest replies and a control with the count of the earlier replies. Under the last box, a comment field of one line has the avatar of the member before it and a Comment button next to it. The field grows with its text, and the button is off until the field has text. Opens on: the page of a post, or the comment button of a row in a feed.
- `thread-long`: the second box shows each of its 6 replies, and the control is gone. Opens on: a click on the control.
- `reply-form`: the reply field of the first box has the focus. It stays one line, and a Cancel button and a Reply button stand next to it. The field grows when the member types. Reply is off until the field has text. Opens on: a click on the reply field.
- `reply-sent`: the reply of the member is the last reply of the first box, and the reply field has no buttons again. Opens on: Reply.
- `comment-reaction`: the reaction chip of the first comment is pressed, and its count is one more. A click on the chip removes the reaction. Opens on: a click on a reaction chip, or a choice in the reaction picker.
- `comment-menu`: a menu with 3 items, each with an icon: copy the link, quote the comment in a reply, and report. Opens on: a click on the more button of the first comment.
- `empty`: the heading, the sentence "No comments yet." and the comment field. The source page has comments, so the capture did not see this state. Opens on: a post with no comment.

## Transitions

The capture read the source from pictures, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `thread` to `thread-long`. Trigger: a click on the control of the earlier replies. Moves: not seen.
- `thread` to `reply-form`. Trigger: a click on the reply field. Moves: not seen.
- `reply-form` to `reply-sent`. Trigger: a click on Reply. Moves: not seen.
- `reply-form` to `thread`. Trigger: a click on Cancel. Moves: not seen.
- `thread` to `comment-reaction`. Trigger: a click on a reaction chip. Moves: not seen.
- `thread` to `comment-menu`. Trigger: a click on the more button of the first comment. Moves: not seen.

## Hard cases

- Long thread: the `thread-long` state. The source shows the newest replies and one control with the count of the earlier ones, such as "Show 2 previous replies".
- Empty: the `empty` state. It is the designer's choice.
- Reply to a reply: the source has one level of replies. An answer to a reply is the next reply of the same thread, and it can name a member in its text.
- Long text: the text wraps in the box. A long word breaks at the edge of the box.
- Long reply: the reply field and the comment field grow with their text to 196 px. Then the text scrolls in the field.
- Narrow screen: at 768 and 390 px the source keeps the same box, and the text takes the full width of the box. In the sketch at 390 px, the replies stand closer to the line, the name of an author stays whole, and the Cancel button and the Reply button stay next to the reply field. The avatar before the comment field leaves.
- Edited comment: the source shows the word "edited" on the line of the author. The sketch does not draw it.
- Failed send, slow network, a deleted comment and more comments than one page holds: not seen.

## Notes

- Job: the reader sees which comment an answer belongs to, and answers in that place. One level of replies keeps each line of talk in one box, so a long discussion does not move to the right.
- The owner asked for new comments in round `rev_c484fd4be6db`. In round `rev_e93e264e511e` the owner chose one pattern for each part of a screen, so the thread is a pattern of its own.
- The designer compared the threads of 4 public products. The first indents each level of a tree and has no reactions. The second has a deep tree with votes and a control for more replies, and it is the source of `content/comment-tree`. The third has one flat box for a comment and its replies, and shows the reaction button on hover. It is the source of `content/feed-full-posts`. The source of this pattern is the base, because it has each part that the owner asked for: replies, a control for a long thread, a reply field in each thread and reactions on each comment.
- The source has these parts, and the sketch leaves them out: a count of votes on each comment, the word "edited", and a sort control above the comments.
- These parts differ from the source. The source puts the add reaction button before the reaction chips, under the text. The sketch puts it on the author line, so a comment with no reaction has no empty line. The source has a rule between a comment and its replies and a fill behind the replies. The sketch has only the line at the left of the replies. The items of the more menu are the designer's choice, because the capture read the page signed out.
- The capture read the page signed out, so it did not open a form and did not react. These parts are the designer's choice: the open reply field, the sent reply, the comment field, the pressed reaction and the empty state. The Reply button and the Comment button are off until the field has text, so a member cannot send an empty comment.
- The owner said in round `rev_7719a47974c2` that the reply form was too big: a tall text area with an attach button, and Cancel and Reply under it. Now the reply field starts as one line and grows when the member types, and Cancel and Reply stand next to it. The comment field has the same form. The attach button is gone from both.
- The owner chose one pattern for each part of a screen in round `rev_e93e264e511e`. So the post above the thread and the reaction picker are parts of the pattern `content/feed-full-posts`, and the sketch draws a plain box for each. The add reaction button opens a popover with a box.
- In the sketch, only the first thread opens the reply field, takes a reaction and opens the more menu. The reply field of the second thread shows a toast.
- Keep these parts when the look changes: one box for each thread, one level of replies on a line, the reply field at the foot of each thread, and the reactions under each comment.
- The sketch keeps no brand, colour, text or picture of the source. The sample comments are fabricated. The pictures are not committed.
