# Follow menu with alert levels

Captured: 2026-11-20, from a documentation page. The capture did not open the menu in the real app, because the menu needs a sign-in.
Best for: a product where a member follows a product, a topic or a person with one button, and sets how many alerts come.
Row opens: no rows.
Related: `notifications/subscribe-popover` lets a person with no account follow a product. `settings/notification-settings-by-event` and `settings/notification-settings-by-channel` set where the alerts go. `content/feed-full-posts` draws the feed under the head.

## States

- `follow`: the head of the page of a product. It has the mark and the name of the product, the count of its followers, and a Follow button with a bell and an arrow. Under the head, the feed of the product, as a plain box with the name `content/feed-full-posts`. Opens on: the page of a product that the member does not follow.
- `menu`: a menu under the button, with one row for each level. A row has an icon, a name and one short line. The levels are "All updates", "Custom", "Mentions only" and "Mute". The level of the member has a check and a bold name. Opens on: a click on the button.
- `following`: the button is an outline button with a bell that rings and the word "Following". A toast confirms the level. Opens on: the level "All updates".
- `custom`: a popover in the place of the menu. It has a back button and the name "Custom", one check box for each kind of event, Cancel and Apply. The events are releases, posts, comments and security alerts. Apply is off when no event has a check. Opens on: the level "Custom".
- `custom-set`: the button has a sliders icon and the word "Custom". A toast confirms the save. Opens on: Apply.
- `muted`: the button has a bell with a line across it and the word "Muted". A toast confirms the level. Opens on: the level "Mute".

## Transitions

The source is a documentation page, and it shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `follow` to `menu`. Trigger: a click on the button. Moves: not seen.
- `menu` to `following`. Trigger: a click on "All updates". Moves: not seen.
- `menu` to `custom`. Trigger: a click on "Custom". Moves: not seen.
- `custom` to `custom-set`. Trigger: a click on Apply. Moves: not seen.
- `custom` to `menu`. Trigger: a click on the back button or on Cancel. Moves: not seen.
- `menu` to `muted`. Trigger: a click on "Mute". Moves: not seen.
- `menu` to `follow`. Trigger: a click on "Mentions only". Moves: not seen.

## Hard cases

- No event in the custom level: Apply is off, because that level sends nothing. The member chooses "Mentions only" or "Mute".
- Narrow screen: at 390 px the button stays beside the name when it fits, and stands under the name when it does not. The menu takes the width of the screen less a margin.
- Where the alerts go: the source sets the channels, such as the inbox of the product and email, in the notification settings of the member, not in this menu. The patterns `settings/notification-settings-by-event` and `settings/notification-settings-by-channel` draw such settings.
- A product that the member owns, a failed save and a slow network: not seen.

## Notes

- Job: the member decides in one place whether to follow and how loud the product is. One button shows the answer at each moment, so the member does not open a settings page to learn the level.
- The owner asked in round `rev_4b4cb0185c58` how a person can follow a product, and for more research. The designer studied 7 products: the source and the 6 products that the Source line names. Each page was read on 2026-11-20. The 2 best are drawn: this pattern for a member with an account, and `notifications/subscribe-popover` for a person with no account.
- Facts of the 6 other products, in the order of the Source line:
  - Product 1: a person follows a channel. It has a Subscribe button, then a bell with 3 levels: all, personalized and none. It needs an account.
  - Product 2: a person follows a topic, a category or a tag. It has one control with a list of 5 levels: watching, tracking, watching first post, normal and muted. It needs an account.
  - Product 3: a person follows a person. It has a Follow button, then a bell next to it for alerts on the new posts of that person. It needs an account.
  - Product 4: a person follows the public status page of a product. It has one button that opens a popover with one tab for each channel, and no levels. It needs no account. It is the source of `notifications/subscribe-popover`.
  - Product 5: a person follows a product. A follower gets a notification of the next launches of the product. The designer found no official help page, so the control, the levels and the need for an account are not known.
  - Product 6: a person follows a project. It has a row menu item that unsubscribes from a project, and a bell that sets how often a summary comes. It has no levels for one project. It needs an account. It is the source of `content/feed-full-posts`.
- What the designer reads in these facts: 4 of the 7 products use one button that shows the follow state, with a menu or a bell for the level. The source, product 1 and product 2 have 3 to 5 named levels, and each of the 3 has a level for all alerts and a level for no alerts. Only product 4 lets a person follow with no account.
- The menu of the sketch is the menu of the source, with the words of a product in place of the words of a repository.
- The source names the levels "Participating and @mentions", "All Activity", "Ignore" and "Custom". Its custom events are issues, pull requests, releases, discussions and security alerts. The sketch uses the words of a product: "Mentions only", "All updates", "Mute", and the events releases, posts, comments and security alerts.
- These parts are the designer's choice: the icon of each level, the icon and the word of the button in each level, the toasts, and Apply that is off with no event. The source names its button "Watch" or "Unwatch", with a count.
- In the sketch, each level opens its own state, and each state opens the menu again.
- Keep these parts when the look changes: one button that shows the level, the levels in one menu with one short line each, and the custom events behind one more step.
- The sketch keeps no brand, colour, text or picture of the source. The sample product is fabricated.
