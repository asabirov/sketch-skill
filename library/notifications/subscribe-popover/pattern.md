# Subscribe popover with channels

Captured: 2026-11-20, recorded by an agent on the public page at 1280 px. The capture opened each tab and sent no form.
Best for: a product that a person follows with no account. The person chooses where the alerts go: an email address, a phone number or a feed reader.
Row opens: no rows.
Related: `notifications/follow-menu` lets a member with an account follow a product and set the alert level.

## States

- `page`: a bar with the product name and a Subscribe button with a bell at the right. Under it, the public page of the product, as an empty box. Opens on: the public page of the product.
- `email`: a popover under the button. Its first line has one tab for each channel and a close button. A tab is an icon with no word: a letter, a phone and a feed mark. The first tab is selected. Under the tabs, an email field and a Subscribe button. Opens on: a click on the Subscribe button of the bar.
- `email-error`: the field is marked as wrong, and one line under it says how to correct it. Opens on: Subscribe with no full address in the field.
- `email-sent`: the part under the tabs has a check and one sentence with the address, and a button for another address. The person is a subscriber only after a click on the link in the email. Opens on: Subscribe with an address in the field.
- `sms`: the second tab is selected. The part has a chooser for the country code, a phone field and a Subscribe button. Opens on: a click on the phone tab.
- `feed`: the third tab is selected. The part has 2 links: the Atom feed and the RSS feed. Opens on: a click on the feed tab.

## Transitions

The source opens the popover with no transition. The capture read a transition duration of 0 s on the popover. So the sketch plays no transition, and `transitions.json` is empty.

- `page` to `email`. Trigger: a click on the Subscribe button. Moves: nothing. The popover shows at once. measured.
- `email` to `sms`, and `email` to `feed`. Trigger: a click on a tab. Moves: not seen. The capture did not measure the tab change.
- `email` to `email-sent`. Trigger: a click on Subscribe. Moves: not seen. The capture sent no form.
- `email` to `email-error`. Trigger: a click on Subscribe with no full address. Moves: not seen.
- `email` to `page`. Trigger: a click on the close button or outside the popover, or Escape. Moves: nothing. measured.

## Hard cases

- Wrong address: the `email-error` state. It is the designer's choice.
- Confirmation: the `email-sent` state. The documentation of the source says that an email subscriber confirms the address with a link, and that a phone subscriber gets a code. The capture did not see these steps.
- Narrow screen: at 390 px the popover takes the width of the screen less a margin, and the two phone fields stay in one row.
- More channels: the source page has 6 tabs. The sketch draws 3. When a product has more channels than the row holds, the designer chooses which ones show.
- A person who is a subscriber already, the way to unsubscribe, a failed send and a slow network: not seen. The documentation says that each email has a link to manage the subscription.

## Notes

- Job: a person who uses the product, but has no account for this page, gets the news where the person already reads: the inbox, the phone or a feed reader. One button is the whole way in, and the page asks for nothing but the address.
- The owner asked in round `rev_4b4cb0185c58` how a person can follow a product, and for more research. The designer studied 7 products. The record of `notifications/follow-menu` holds the study with its links. The 2 best are drawn: this pattern for a person with no account, and `notifications/follow-menu` for a member with an account.
- The source page has 6 tabs, and the sketch draws 3 of them. It leaves these out: a team chat app, a webhook address and a link to the support site. The source also has a heading in the popover, one sentence above the field that says when an email comes, and a line with the privacy policy under the button. A product adds the legal line that its law needs.
- The source names the button "Subscribe to Updates" and the button of the form "Subscribe via Email". The sketch names each "Subscribe", because the tab already shows the channel.
- These parts are the designer's choice: the error line, the sentence after the send, the button for another address, and the fields of the phone tab in one row.
- In the sketch, the Subscribe button of the phone tab shows only a toast, and the feed links lead nowhere.
- Keep these parts when the look changes: one button on the public page, one tab for each channel, one field for each channel, and no account.
- The sketch keeps no brand, colour, text or picture of the source. The pictures are not committed.
