# Notification settings by event

Captured: 2026-11-20, from public pictures.
Best for: a product that sends fewer than 13 kinds of event on 2 or 3 channels. A member chooses how each kind of event reaches them, and from whom.
Row opens: on the record's own page. A row opens the page of one kind of event, and a back link returns to the list.
Related: `settings/notification-settings-by-channel` has one page for each channel, for a product with more than 15 kinds of event. `notifications/follow-menu` sets the alert level of one product that a member follows.

## States

- `overview`: one column in the middle of the page with a title and the kinds of event in 3 groups, each with a heading and a card. Each row has the name of the kind, one sentence, a status line and a chevron. The status line names the channels that are on and the senders, or says "Off". Opens on: the notifications link of the settings.
- `event`: the page of one kind of event. A back link above the name of the kind, which is the title, and one sentence. Then a group with one switch for each channel: push, the app and email. Each switch row has a sentence under its name. Then a group with the choice of senders: everyone, or the members that the member follows. The page has no save button. Opens on: a click on a row.
- `channel-off`: the same page with the switch of one channel off. The change saves at once, and the word "Saved" stands before that switch. The status line of the kind in `overview` then names the channels that stay on. Opens on: a click on the switch of a channel.
- `all-off`: each switch of the page is off. The choice of senders is disabled and keeps its value. The status line in `overview` says "Off". Opens on: a click on the last switch that is on.
- `from-choice`: the second choice of senders is selected. The status line in `overview` then names these senders. Opens on: a click on that choice.
- `channel-unavailable`: the switch of a channel that the member cannot use yet is disabled. The sentence under its name gives the reason and a link. Each other control works. Opens on: the page of a kind, when a channel needs a set-up.
- `save-error`: a sentence above the switches says which change was not saved, with a button to try again. The switch shows the saved value. Opens on: a change that the server refuses.

## Transitions

The source is a picture, and a picture shows no motion. So the sketch plays no transition, and `transitions.json` is empty.

- `overview` to `event`. Trigger: a click on a row. Moves: not seen.
- `event` to `overview`. Trigger: a click on the back link. Moves: not seen.
- `event` to `channel-off`. Trigger: a click on the switch of a channel. Moves: not seen.
- `event` to `all-off`. Trigger: a click on the last switch that is on. Moves: not seen.
- `event` to `from-choice`. Trigger: a click on the second choice. Moves: not seen.
- `event` to `save-error`. Trigger: a refused change. Moves: not seen.

## Hard cases

- Each channel off: the `all-off` state. The choice of senders stays in view, so the member sees what returns with the first switch.
- Channel that needs a set-up: the `channel-unavailable` state.
- Many events: the source has 10 kinds in one list with no search and no filter. So the sketch has no search field. A product with more than 15 kinds needs the pattern `settings/notification-settings-by-channel`.
- A kind with no choice of senders: an event of the account, such as a sign-in alert, has no sender. The status line of such a row names only the channels.
- Narrow screen: at 390 px the order is the same in one column. The chevron and each switch stay at the right, and a long sentence wraps.
- Failed save, slow network and a long name: not seen.

## Notes

- Job: the member decides how much each kind of event matters. The list answers "what reaches me, and how" with one row for each kind, because each row names its channels and its senders. The page of a kind is short, so the member changes one kind in a few controls.
- Until round `rev_e93e264e511e` this pattern was the variation `by-event` of `settings/notification-settings-by-channel`. In that round the owner chose that each layout is its own pattern. The owner set its limit in round `rev_f371a8bd3fb3`: fewer than 13 kinds of event. This pattern is the list of kinds and the page of one kind of the source picture.
- A product with many channels needs `settings/notification-settings-by-channel`, because a page with one switch for each channel becomes long. A product with many kinds of event also needs it, because the list of kinds becomes long.
- The picture shows a list of 10 kinds of event, each with an icon, a status line and a chevron. It also shows the page of one kind, with one sentence, a switch for push, a switch for the app, and a choice between everyone and the people that the member follows. The sketch leaves out the icons, the 3 "New" marks and the bar of the picture.
- The owner asked for fuller settings in round `rev_c484fd4be6db`. The 10 rows, the status line, the sentence of a kind and the 2 switches come from the picture. These parts are the designer's choice: the 3 groups with their headings, the sentence on each row of the list, the sentence under each switch, the email switch, the word "Saved", the disabled choice of senders, the notice of the phone app and the error sentence.
- No fact of this pattern was checked in a real app.
- Keep these parts when the look changes: the status line on each row, one page for each kind, and the save at once.
- The sketch keeps no brand, colour, text or picture of the source. The sample events are fabricated.
