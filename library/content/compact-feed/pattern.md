# feed: feed of posts

Captured: 2026-11-20, recorded by an agent.
Best for: a product where groups post updates, and a member keeps up with them in one stream. The member reads each post in full and answers without leaving the stream.
Row opens: in place. The row already shows the full post, and a click on the row body does nothing. The comment thread opens under the row. The line under the title is a link to the page of the post.

## States

- `feed`: one column in the middle of the page. At its top, the title with a new update button at the right. Under the title, a row of pill tabs "For me", "Popular", "Recent" with an add button after them. Then the updates, under date labels with a rule. Each row has the group title with a more button at the right. Under the title, one line has the small avatar and the name of the author, and the age. Then the full text, then a comment button, the reactions as chips with a count, and an add reaction button. The comment button of a row with comments shows their count as words, the form `words`. Opens on: the feed link of the product.
- `feed-number`: the same feed. The comment button shows the count as a number, the form `number`. The source shows no such form. Opens on: no action. The product chooses one form.
- `feed-faces`: the same feed. The comment button shows the small avatars of the members who commented, and the count as words, the form `faces`. The source shows no such form. Opens on: no action. The product chooses one form.
- `tab-popular`: the same column with the second tab selected, another order and no date labels. Opens on: a click on the tab.
- `comments-open`: the comment thread stands under the row, and the rows below move down. The thread is the pattern `comment-comment-thread`, so the sketch draws a plain box with that name. Opens on: a click on the comment button.
- `comment-sent`: the same row and the same box. The comment button shows the count of 1. Opens on: a comment that the member sends in the thread.
- `reaction-picker`: a popover next to the add reaction button, with a search field and a grid of often used reactions. Opens on: a click on the add reaction button.
- `reaction-added`: the chosen reaction is a pressed chip with a count, between the comment button and the add reaction button. A click on the chip removes the reaction. Opens on: a choice in the picker.
- `post`: the page of one post. A back link to the feed, then the title with a more button, the author and the age, the full text, the reaction chips and an add reaction button. Under them, the comment thread, as a plain box with the name `comment-comment-thread`. Opens on: a click on the line under the title of a row.
- `row-menu`: a menu with 3 items: open the update in its group, copy the link, and stop the updates from this group. Opens on: a click on the more button of a row.
- `compose`: a dialog over the dimmed page with a group chooser, a text field, an attach button and a post button. Opens on: a click on the new update button.
- `custom-feed`: a panel under the tabs, as wide as the column. Its first line has a name field, Cancel and Create view. Its second line has the chosen filters as chips, and an add filter button at the right. The feed below shows the filtered updates at once. The add filter button opens a menu with 3 kinds of filter: author, date and group. Opens on: a click on the add button after the tabs.
- `feed-saved`: the saved view is one more tab, and it is selected. A toast confirms the save. Opens on: Create view.
- `empty`: a drawing, a heading, one sentence, a new update button and a link to the documentation. Opens on: a feed with no updates.

## Transitions

- `feed` to `tab-popular`. Trigger: a click on a tab. Moves: the fill and the text colour of the old tab and the new tab change (background-color and color 150 ms, ease). The list changes with no transition. measured.
- `feed` to `comments-open`. Trigger: a click on the comment button. Moves: nothing. The field shows at once, and the rows below jump down. measured.
- `comments-open` to `comment-sent`. Trigger: a sent comment. Moves: the comment button grows to hold the count (width 200 ms, ease-in-out). measured.
- `feed` to `reaction-picker`. Trigger: a click on the add reaction button. Moves: the popover fades in (opacity 50 ms, linear) and grows from 98% (transform 230 ms, ease-out). The source moves it with a script spring. estimated.
- `reaction-picker` to `reaction-added`. Trigger: a choice in the picker. Moves: the chip shows at once, measured. The picker closes with the close values of a menu, estimated.
- `feed` to `post`. Trigger: a click on the line under the title of a row. Moves: nothing. The page shows at once. measured.
- `post` to `feed`. Trigger: a click on the back link. Moves: nothing. The feed shows at once. measured.
- `feed` to `row-menu`. Trigger: a click on the more button. Moves: the menu fades in (opacity 50 ms, linear) and grows from 98% (transform 230 ms, ease-out). estimated.
- `feed` to `compose`. Trigger: a click on the new update button. Moves: the page cover fades in (opacity 400 ms, linear(0, 0.19, 0.36, 0.51, 0.64, 0.75, 0.84, 0.91, 0.96, 0.99, 1)), measured. The dialog fades in (opacity 300 ms, linear(0, 0.24, 0.55, 0.76, 0.88, 0.94, 0.97, 0.99, 0.99, 1, 1)), measured. The dialog grows from 95% (transform 350 ms, ease-out), estimated. The capture read the two fades 2 times, from the new update button of an empty view. The dialog was 713 px wide at the start and 750 px wide at the end.
- `feed` to `custom-feed`. Trigger: a click on the add button. Moves: nothing. The panel shows at once. measured.
- `custom-feed` to `feed-saved`. Trigger: a click on Create view. Moves: the new tab fades in (opacity 300 ms, cubic-bezier(0.25, 0.1, 0.35, 1)). The toast fades in and moves up (opacity and transform 400 ms, ease). measured.
- `compose` to `feed`. Trigger: Escape or a click on the close button. Moves: the page cover fades out (opacity 280 ms, linear(0, 0.19, 0.36, 0.51, 0.64, 0.75, 0.84, 0.91, 0.96, 0.99, 1)), measured. The dialog fades out (opacity 300 ms, linear(0, 0.24, 0.55, 0.76, 0.88, 0.94, 0.97, 0.99, 0.99, 1, 1)), measured. The dialog gets smaller, to 95% (transform 330 ms, ease-out), estimated.
- `row-menu` to `feed`. Trigger: Escape, a click outside the menu or a choice. Moves: the menu fades out (opacity 150 ms, linear). The source moves it with a script in about 130 to 180 ms. estimated. Each other menu and the reaction picker close with the same values.

## Hard cases

- Empty: the `empty` state. The source shows it before the first update.
- Long text: the row shows the full text with its lists. The source does not cut it, and no row has a "show more" control. At 1280 px the text column is 717 px wide.
- Row with no comment and no reaction: the comment button shows the icon only.
- Post with no comment: in the source, the page of the post shows one comment field with an attach button and a send button under the heading. The state `empty` of `comment-comment-thread` draws a thread with no comment.
- Many comments: the capture saw 2 comments in one box. It did not see a page with more boxes, or a control that shows more comments. The state `thread-long` of `comment-comment-thread` draws a long thread.
- End of the feed: with 3 updates the source shows no end mark.
- Narrow screen: at 390 px the side nav of the source becomes a button in its bar. The tabs stay in one row, and each row takes the full width. At 820 px the layout is the same. The sketch has no nav and no bar, so it is one column at 1280, 768 and 390 px. When the tabs are wider than the column, the tab row scrolls sideways. At 390 px the source puts the attach button and the send button under the reply field.
- Failed load, slow network, and more tabs than the row holds: not seen.

## Variations

- `base`: the feed of the source, without its side nav, its bar and the parts that only the source has. The Notes name these parts.

The owner chose in round `rev_e93e264e511e` that each layout is its own pattern and that the sketch has no variation buttons. So this record has only `base`. The earlier variations `timeline` and `forum` are now the patterns `x-timeline` and `community-forum`.

The comment count has 3 forms. They are not layouts, so they are not variations. Each form has its own state, and `?count=<id>` in the address shows that form in each other state:

- Form `words`: the icon and the count as words, such as "2 comments". This is the form of the source. Use it when the row has room and the member must not guess what the number counts. State `feed`.
- Form `number`: the icon and the number. Use it when the row is narrow or has more counts. State `feed-number`.
- Form `faces`: the icon, the small avatars of the members who commented, and the words. Use it when who answered matters more than how many answered. State `feed-faces`.

The forms `number` and `faces` are the designer's choice. The source shows only the words.

## Notes

- Job of the base: the member learns the status of each group's work without a meeting and without a visit to each group. Each row is one full update that a person wrote, so the member reads the stream from top to bottom and never opens a row.
- The answer stays in the stream. The comment thread and a reaction open under the row, and the count on the row shows that an answer exists.
- The page of a post is the place for a link to one post and for a long discussion. The member does not need it to read or to answer, because the row holds both.
- The tabs are answers to "what must I read". A saved filter becomes one more tab, so a filter is a place that the member comes back to.
- Keep these parts when the look changes: the full post in the row, the answer in place, the comment count on the row, the tabs with a saved view, and the "Row opens" value.
- Facts that the earlier notes took from pictures, checked in the real app: the row shows the whole update (confirmed). The date label stands above its rows with a rule at 1280, 820 and 390 px, not in a left margin. The end mark "all caught up" of the launch video did not show with 3 updates. The summary in the inbox and its audio were not checked.
- The owner asked for a base with no side nav and no bar, in round `rev_e1558868fd40`. The source has a side nav with the links of the app, and a bar with the title, a bell button and a button for the nav on a narrow screen. In the source, the tabs and the filter panel are as wide as the page. The sketch puts the title and the tabs in the column of the updates. The shell of the product holds the way to the feed.
- The owner asked for a base with only the parts that each feed of posts needs, in round `rev_fa8a4e02c804`. The source has these parts, and the sketch leaves them out:
  - A health mark and a status word before the author of each update. The word has 3 values, from good to bad.
  - A bell button next to the title. Its menu sets how often a summary of the feed arrives in the inbox: each day, each week or never. The capture estimated the same open values as for the row menu.
  - Two more items in the row menu: copy the update as text, and why the member sees this update. The second item opens a small dialog with the reason and two ways to unsubscribe.
  - A search field and 3 more kinds of filter in the filter menu: health, group members and group status. The saved view of the capture had a health filter. The saved view of the sketch has a group filter.
- The owner asked for the comment count in more than one form, the page of a post, its comments, and the reactions on a post and on a comment, in round `rev_f371a8bd3fb3`. The capture read each one in the source, except the forms `number` and `faces`.
- The page of a post in the source has these parts, and the sketch leaves them out: a bar with the age of the update and a bell button, the health mark and the status word, the words "shared a project update" after the author, and a line above the comments that says who shared the update. The source names the heading above the comments "Activity".
- The owner asked in round `rev_c484fd4be6db` for new comments, and in round `rev_e93e264e511e` for one pattern for each part of a screen. So the comments are the pattern `comment-comment-thread`, and this sketch draws a plain box in their place. The same rule gives this pattern the row menu, the composer and the reaction picker. The patterns `x-timeline`, `community-forum` and `comment-comment-thread` draw a plain box for each of them.
- Facts of the comments of the source, which the sketch no longer draws: a comment and its replies stand in one box with a line between them. Each has the avatar and the name of its author, the age and the text. The box ends with a reply field with an attach button and a send button. A reaction on a comment makes a row of reactions grow under its text (height 100 ms, ease-in-out). The capture read this value 2 times. On a comment with no reaction, the source shows the add reaction button and a button for the comment options only on hover or focus. They fade in (opacity 100 ms, ease).
- In the source, the title of a row is a link to the group, and the line under the title is one link to the page of the post. The source gives this line no mark. The sketch underlines the age, so that a reader of the sketch sees the link.
- In the sketch, each row opens the same sample page.
- The first read of the way to the page of a post, and the first read of the way back, showed one fade of the page (opacity 100 ms, ease-in, after 500 ms). 3 later reads of each way showed no transition. So the record keeps no fade for these steps. The cause of the first read is not known.
- In the source, the capture opened the composer from the new update button of the empty state. A feed with updates shows no such button. The sketch also puts a new update button next to the title. So the member can post from a feed with updates.
- The source also changes the shadow of a tab in 150 ms and opens the reason dialog of the row menu in 200 ms. The sketch draws no shadow and no reason dialog.
- Changes in the test workspace for this capture: the feed feature turned on, 3 sample projects with one update each, 1 comment, 1 reaction, 1 saved view, and the summary set to "never". For the read of the composer, the capture filtered a view that it did not save, opened the composer and closed it with no post. For round `rev_f371a8bd3fb3`, the capture added 1 reaction to a comment and 1 reply. It removed the reaction and added it again for the second read. The reaction and the reply stay in the workspace.
- The sketch keeps no brand, colour, text or picture of a source. The sample rows are fabricated. The frames are not committed.
