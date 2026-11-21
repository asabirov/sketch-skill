# App in a chat: inline app card

Captured: 2026-11-12, read by an agent from the frames of the keynote video
Best for: an assistant that puts a small working app into a conversation. Use it when a person does a short task in an app without leaving the chat, and a longer task needs the whole screen.
Row opens: no rows.

## States

- `card-inline`: the chat. The user asked for something. The assistant's turn starts with an app icon and a tool-call label, then a plain inline card with a title, a content area, one action and an expand button. The composer stays at the bottom. Opens on: the user's message. Shown by the learning app, the design app and the homes app.
- `card-action`: one interaction inside the card. The content area answers the action, and the card stays in the chat. Opens on: the card's one action. Shown by the learning app and the homes app.
- `fullscreen`: the card opened to a full screen. A top bar holds a close button, the app name and an "Open in [App]" button. The body shows the content area enlarged. The composer stays at the bottom as "Ask [App]". Opens on: the expand button (the homes app only), or a click on a design (the design app). Shown by the design app and the homes app.
- `return-chat`: the chat again after the full screen closes. Only the homes app shows the card inline again; the design app shows the new message and a "Thinking" label, with no card. Opens on: the close button in `fullscreen` (the homes app), or a message sent from the full-screen composer (the design app). Shown by the design app and the homes app.

## Transitions

- `card-inline` to `card-action`. Trigger: the card's one action. Moves: the content area updates. 200 ms, easing not seen. Estimated (the homes app, map zoom, frames 00:23.46 to 00:23.66, video 11:58.46 to 11:58.66).
- `card-action` to `fullscreen`. Trigger: the expand button (the homes app), or a click on a design (the design app). Moves: the full screen sheet rises and covers the chat. 160 ms, easing not seen. Estimated (the source video). The homes app opens in 160 ms (frames 00:26.63 to 00:26.79, video 12:01.63 to 12:01.79); the design app opens in 430 ms (frames 03:43.49 to 03:43.92, video 10:13.49 to 10:13.92). The sketch plays the value of the homes app.
- `fullscreen` to `return-chat`. Triggers: the close button in `fullscreen` (the homes app, video 13:32.42 to 13:32.78), or a message sent from the full-screen composer (the design app, video 10:49.73 to 10:49.86). Moves: the full screen closes. Only the homes app shows the inline card again; the design app shows the new message and a "Thinking" label, with no card. 360 ms, easing not seen. Estimated (the source video).

## Hard cases

- A long list: the inline card shows a short list and does not scroll inside itself. More items belong in full screen, where the list scrolls.
- Empty result: not seen.
- Narrow screen: not seen (the video shows only the desktop app).
- Slow network: the homes app shows a loading placeholder before the card (video 11:40.77 to 11:46.58). The design app shows a "Thinking" label in the chat after the return (video 10:49.73). The learning app shows none.

## Notes

- Keep the app inline first, and offer the expand when the task needs more room.
- Keep the composer available in full screen, so the user can keep talking to the app. The design app and the homes app each show "Ask" and the name of the app.
- Use the system close button in full screen, not a custom one.
- Steps that only one app shows:
  - Connect: the learning app shows a "[Assistant] wants to connect to [App]" screen with Continue and Do not connect (video 6:30). The homes app shows a "Connecting to app" label (video 11:40). The design app shows none.
  - Inline content: the learning app shows a course card with an embedded video and an "Enroll for free" button (video 6:42.31). The design app shows poster design options (video 9:59.01). The homes app shows a map with price markers and two property cards (video 11:51.48).
  - Card action: the learning app plays the course video inside the card (video 6:58.03 to 7:12.11). The design app shows none; a click on a design opens the full screen instead (video 10:13.49 to 10:13.92). The homes app zooms the map out (video 11:58.46 to 11:58.66).
  - Full screen content: the design app shows the poster in an editor (video 10:13.92). The homes app shows a property list and a map (video 12:02.43).
  - Return: the homes app closes the full screen with the close button and shows the card inline again (video 13:32.42 to 13:32.78). The design app returns when the user sends a message in the full-screen composer; the chat shows the new message and a "Thinking" label, with no card (video 10:49.73 to 10:49.86).
  - Follow-up action: the design app turns the poster into a pitch deck (video 10:46.72). The homes app answers a chat question about a dog park (video 13:28.58).
- Steps that no frame shows:
  - The learning app shows no open to full screen and no return to the chat. Its card has an "explore the full course here" link, but the frames never show it opening.
  - The easing of each estimated transition is not seen. The sketch plays a plain default motion, not a measured curve.
