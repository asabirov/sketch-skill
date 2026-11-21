# Notification settings by channel

Captured: 2026-11-20, recorded by an agent.
Best for: a product that sends events on more than one channel and has more than 15 kinds of event. A member chooses which events notify them on each channel, and turns a channel off without losing the choices for its events.
Row opens: on the record's own page. A channel row opens the page of that channel, and a back link returns to the list.
Related: `settings/notification-settings-by-event` has one page for each kind of event, for a product with fewer than 13 kinds. `notifications/follow-menu` sets the alert level of one product that a member follows.

## States

- `overview`: one column in the middle of the page with a title and a search field. Then 2 groups, each with a heading. The group of the channels has one sentence and one card of 4 channel rows with a line between the rows. Each row has the channel name, a status line under the name, and a chevron. The status line says "off", "on for each event", "on for" some kinds of event, or what the channel needs. The group of the news from the product has 3 rows, each with a name, one sentence and a switch. Opens on: the notifications link of the settings.
- `find`: the search field has text. The groups give place to one card of results. Each result row has the name of a kind of event, the name of a channel under it, and a chevron. A result opens the page of its channel. Opens on: text in the search field.
- `find-none`: the search field has text that no setting matches. One sentence under the field says so and repeats the text. Opens on: text with no match.
- `channel`: a back link above the channel name, which is the title. The first card has 2 rows: a switch for the whole channel with the address under it, and a control for the format: one digest or one message at once. Then a group for the hours: a switch, 7 day buttons and 2 times. Then the kinds of event in 3 groups, each with a heading and a card: 10 kinds in the sketch, 12 in the source. Each row has a name, one sentence and a switch. The page has no save button. Opens on: a click on a channel row.
- `event-off`: the same page with the switch of one event off. The change saves at once, and the word "Saved" stands before that switch. The source shows no such word and no toast. The status line of the channel in `overview` then names the kinds that stay on. Opens on: a click on the switch of an event.
- `channel-off`: the switch of the channel is off. Each control under it is disabled and dim, and each one keeps its value. The status line in `overview` says "off". When the member turns the channel on again, each earlier choice returns. Opens on: a click on the switch of the channel.
- `format-menu`: a menu under the format control with 2 options and a check mark on the current one. Opens on: a click on the format control.
- `channel-unavailable`: the page of a channel that the member cannot use yet. A card with one row gives the reason and one button. The event switches show their values and are disabled. Opens on: a click on the row of that channel.
- `save-error`: a sentence above the groups of events says which change was not saved, with a button to try again. The switch shows the saved value. The source shows no error state. Opens on: a change that the server refuses.

## Transitions

- `overview` to `find`. Trigger: text in the search field. Moves: not seen. The capture read the search from pictures.
- `overview` to `channel`. Trigger: a click on a channel row. Moves: the header of the page changes with a fade (opacity 300 ms, cubic-bezier(0.25, 0.1, 0.35, 1)). measured. The list changes with no transition.
- `channel` to `overview`. Trigger: a click on the back link. Moves: nothing. The list shows at once. measured.
- `channel` to `event-off`. Trigger: a click on the switch. Moves: the fill of the switch changes (background-color 150 ms, ease-out), and the thumb moves to the other side (left 150 ms, ease-out). measured.
- `channel` to `channel-off`. Trigger: a click on the switch of the channel. Moves: the same switch values (background-color and left 150 ms, ease-out), and each control of the channel dims (opacity 150 ms, ease-out). measured. The way back to on has the same values.
- `channel` to `format-menu`. Trigger: a click on the format control. Moves: the menu fades in (opacity 50 ms, feed) and grows from 98% (transform 230 ms, ease-out). The source moves it with a script spring. estimated.
- `channel` to `save-error`. Trigger: a refused change. Moves: nothing. The source shows no error state, so the sketch shows the sentence at once.

## Hard cases

- Channel off: the event choices stay in view and keep their values. The member sees what returns when the channel is on again.
- Channel that needs a set-up: the `channel-unavailable` state. The member sees the event choices before the set-up.
- Many events: the source has 12 general kinds and 1 feature kind on one page, in groups that do not close. The search finds a kind on each channel without a scroll.
- No match: the `find-none` state. The source says "No matching settings".
- Narrow screen: at 390 px the order is the same in one column. The switch stays at the right, and a long name or sentence wraps. The format control moves under its sentence and takes the full width. The 7 day buttons wrap to 2 rows. The header of the source gets a button for the settings nav and a back link. The back link to the list stands above the title. The sketch has no nav and no header, so it is one column at 1280, 768 and 390 px.
- Hours: the source has the schedule on the page of the phone channel. It has a switch, 7 round day buttons and two times. The sketch draws it on the page of each channel that the member can use.
- Failed save, slow network, and a channel that an admin locked: not seen.

## Notes

- Job: the member decides how loud each channel is. The list answers "what reaches me where" in 4 rows, because each row says what its channel sends. The member opens a page only for the channel that is wrong.
- In round `rev_f371a8bd3fb3` the owner kept 2 layouts: by channel for a product with more than 15 kinds of event, and by event for a product with fewer than 13. The owner gave no rule for a product with 13, 14 or 15 kinds. In round `rev_e93e264e511e` the owner chose that each layout is its own pattern and that the sketch has no variation buttons. So the layout by event is the pattern `settings/notification-settings-by-event`. This pattern is the list of channels and the page of a channel of the source, without its settings nav and the parts that only the source has.
- The page of a channel holds each choice for that channel. So the member thinks about one channel at a time, and a long list of events fits.
- A channel that is off keeps and shows its event choices. This is the part to keep: the switch of the channel is a pause, not a reset. A member can turn a channel off for a week and lose nothing.
- Each change saves at once, so the page needs no save button. The price is that a failed save needs its own message, and the source shows none.
- Keep these parts when the look changes: the status line on each channel row, the values that stay when a channel is off, and the save at once.
- The owner asked for fuller settings in round `rev_c484fd4be6db`. Each part that this round added comes from the source, and these parts are the designer's choice: the word "Saved", the sample kinds of event and the names of their 3 groups.
  - Search: the source has one search field at the top of the settings nav. It searches each page of the settings. For the text "repl" it lists each channel with the matching kind of event under it. A click on a result opens the page of that channel. The sketch has no nav, so the field stands under the title and searches only the notification settings.
  - Groups: the list of the source has 3 groups, each with a heading and one sentence: the order of the inbox in the app, the 4 channels, and the news from the product. The sketch draws the last 2. The group of the news of the source has 3 headings with switches under each. The sketch draws 3 switches under one heading.
  - Description: each switch row of the source has one sentence under its name.
  - Hours: see "Hard cases".
  - Events: the page of a channel of the source has one group of 12 general kinds and one group of 1 feature kind. The sketch draws 10 fabricated kinds in 3 groups.
- The source has these parts, and the sketch leaves them out: a settings nav at the left, an icon in a tile on each channel row, a small round mark in a colour before the status line, a switch that limits the channel to the important events, and a card with 2 switches for the digest. The owner asked for a base with no side nav and with fewer parts in round `rev_e1558868fd40`. The shell of the product holds the way to the settings.
- Facts that the earlier notes took from the help picture, checked in the real app: the list of channels with a summary on each row (confirmed). The summary stands under the channel name, not at the right. The page of a channel is a page of its own with a back link, not a panel.
- The first read of the way back to the list showed one fade of the page (opacity 100 ms, ease-in, after 500 ms). 3 later reads of the same step showed no transition, also directly after a change of a switch. So the record keeps no fade for this step. The cause of the first read is not known.
- Changes in the test workspace for this capture: one event of the email channel turned off and on, the email channel turned off and on, and the format menu opened. For the later reads of the way back, one more event turned off and on. Each value is back at its start. For the search, the capture typed 2 texts and opened one result, which changes no setting.
- The sketch keeps no brand, colour, text or picture of the source. The sample events are fabricated. The frames are not committed.
