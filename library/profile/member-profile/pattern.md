# Member profile

Captured: 2026-11-20, recorded by an agent.
Best for: a product where each member has a public page. A visitor decides who a member is, reads what the member posted and goes to the pages of the member on other sites.
Row opens: no rows. The posts of the member are a part of the pattern `content/feed-short-posts`, and that pattern says how a post opens.
Related: `profile/portfolio-profile` puts the work of a member in a grid beside the identity. `profile/profile-card` is a card over a conversation. `content/feed-short-posts` draws the posts of the member.

## States

- `profile`: a banner picture, an avatar over the edge of the banner, the name, a one-line bio, and a row with 2 links to the pages of the member on other sites. Then the posts of the member, as a plain box with the name `content/feed-short-posts`. Opens on: a click on a name or an avatar.
- `scrolled`: for a guest, a wall with one sign-in button covers the lower posts. Opens on: a scroll down the posts. In the sketch, a scroll of the page in another state shows the same wall when the row of links leaves the view.
- `guest-prompt`: a dialog over the dimmed page with one sentence, a log-in button, a sign-up button and a close button. Opens on: a guest's click on a sign-in button.
- `empty`: the header with the sentence "No posts yet" under it. The source shows no empty state. Opens on: a member with no posts.

## Transitions

- `profile` to `scrolled`. Trigger: scroll. Moves: the wall fades in and moves up by 12 px (opacity and transform 420 ms, cubic-bezier(0.16, 1, 0.3, 1)). measured.
- `profile` to `guest-prompt`. Trigger: a click on a part that needs a sign-in. Moves: the page cover fades in, and the dialog fades in and grows (opacity and scale 150 ms, cubic-bezier(0, 0, 0.2, 1)). measured.
- `guest-prompt` to `profile`. Trigger: a click on the close button. Moves: the page cover fades out, and the dialog fades out and gets smaller (opacity and scale 100 ms, cubic-bezier(0.4, 0, 1, 1)). measured.

## Hard cases

- Guest: in the source, the first tab, its menu, the verified mark and the pictures work. Each other tab, each order option of the menu and the join date open the sign-in prompt. In the sketch, only a sign-in button opens the prompt.
- Narrow screen: at 390 px the facts of the source wrap to 3 lines, its two wide buttons stay side by side, and its 4 tabs stay in one row. At 820 px the page is one column of 598 px. In the sketch at 390 px the two links stay in one row.
- Pictures: the avatar and the banner are links. Each opens a picture viewer with no transition.
- Long name and long bio: not seen. The recorded profile has a bio of one line.
- Empty tab, the member's own profile, a private or blocked profile, a slow network: not seen.

## Notes

- Job: the visitor decides in a few seconds who this is. The order serves that job: picture and name, then the bio, then the links, then the posts. The profile is a feed with a header, so the rows of posts are the rows of a feed.
- The owner chose in round `rev_e93e264e511e` that each layout is its own pattern and that the sketch has no variation buttons. The earlier variations `portfolio` and `card` are now the patterns `profile/portfolio-profile` and `profile/profile-card`. This pattern is the identity and the posts of the source, without the parts that only the source has.
- In the source, each row carries the name of the member. So the visitor knows whose posts these are at each point of the stream. The source also keeps the name in a bar at the top.
- Keep these parts when the look changes: the order of the header, and the posts under it.
- Facts that the earlier notes took from a phone picture, checked in the real web app, signed out: the order of the header and the row of counts as links (confirmed). The tabs are words, not icons. No icon buttons stand next to the avatar, and two wide buttons are the only actions of the source. No "Followed by" line and no "Follows you" chip show to a guest. The join date has no chevron.
- The base keeps the parts that a profile needs in each product. It leaves out the parts that only this source has: the second wide button, which starts a post that mentions the member, the "Reposts" tab, the repost count and the view count of a row, and the handle under the name and on each row. The sketch shows the display name only, because a sample handle can be the handle of a real account.
- The owner changed the base in round `rev_e1558868fd40`. The base has no follow button. The source has one wide follow button under the counts, and one in the bar after a scroll. The base has no caret after the first tab. In the source, the caret opens a menu that chooses what the tab shows and the order. So the record has no state for a follow and no state for that menu. The facts of the base have 2 links to the pages of the member on other sites. The source shows one link to a website there. The owner asked in round `rev_1b5ac128ca46` for no third-party product names, so the sketch names the 2 links "Blog" and "Portfolio".
- The owner removed more parts from the base in round `rev_fa8a4e02c804`, to keep only the parts that each profile needs. The source has these parts, and the sketch leaves them out:
  - A bar that stays at the top, with a back button, the name, the count of posts and a search button. On the page of a post, the bar has a back button and the title "Post".
  - A verified mark after the name. A click opens a small popover with the reason, a link to the rules and the date of the check.
  - The location and the join date in the row of facts. A guest's click on the join date opens the sign-in prompt.
  - A row of counts under the facts, each a link.
  - A row of tabs under the counts. A click changes the text colour of the tab (color 150 ms, cubic-bezier(0.4, 0, 0.2, 1)), measured. For a guest, each tab after the first opens the sign-in prompt.
- So the record has no state for a tab and no state for the popover of the mark. The sign-in wall and the sign-in prompt stay, because the owner's marks do not cover them. A product that shows each post to a guest does not need them.
- Not checked, because each needs a sign-in: the change of a tab, the follow change, the join detail and the "Followed by" line.
- The owner chose one pattern for each part of a screen in round `rev_e93e264e511e`. So the rows of posts and the page of a post are the pattern `content/feed-short-posts`, which has the same source app and the same row. The sketch draws a plain box in their place, and the record has no state for the page of a post. Facts of the source that the sketch no longer draws: a row has the avatar, the name, the age, the text, a picture if the post has one, and a comment count and a like count. The page of a post has a link back to the profile and the title "Post". For a guest, a block with one sign-in button stands after the second reply. For a guest at 1280 px the wall covers the rows, so the capture opened the address of the row link and saw no transition.
- The sign-in prompt belongs to this pattern. The patterns `profile/portfolio-profile` and `profile/profile-card` do not draw it.
- The capture never signed in, posted or followed.
- The sketch keeps no brand, colour, text or picture of a source. The sample member is fabricated. The frames are not committed.
