# Voice message with hold to record

Captured: 2026-11-20, recorded by an agent
Best for: a chat where spoken messages are short and frequent, and a person records one with one hold of a button.
Row opens: no rows. The pattern is a part of a chat page.
Related: `chat/voice-message` starts and sends a recording with a tap. `chat/voice-message-transcript` shows the text of the message in the player.

## States

- `idle`: a voice message in the chat is a player with a Play button, a waveform and the duration. The message field at the bottom has a microphone button. A plain box stands for the other messages. Opens on: Pause, the end of the message, a slide to the left, a release before 300 ms, or the start of the page.
- `playing`: the Play button is a Pause button. The player has a soft fill. The bars that played are in full ink. The time shows the seconds that played. Opens on: tap on Play.
- `recording`: a recording bar replaces the message field. It has the time, a waveform, a Slide to cancel button and a filled microphone button. Opens on: the finger goes down on the microphone button. The source starts a recording with a tap.
- `sent`: the recorded message shows as the last message of the chat, as a player. The message field is back. Opens on: the release of the finger, or tap on the filled microphone button.
- `no-microphone`: a notice above the message field says that the app cannot use the microphone, with a button to the settings. Opens on: tap on the microphone button when the phone gives no access. The source shows no such state.

## Transitions

- `idle` to `playing`. Trigger: tap on Play. Moves: while the finger is down, the button shrinks to `scale(0.96)` and its `background-color` becomes a soft fill. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The bars and the time change each second, with no animation.
- `playing` to `idle`. Trigger: tap on Pause, or the end of the message. Moves: the same 120 ms press on the button. The time shows the duration again, and each bar is quiet again, at once.
- `idle` to `recording`. Trigger: the finger goes down on the microphone button. Moves: the same 120 ms press on the button. measured. The recording bar shows at once.
- `recording` to `sent`. Trigger: the release of the finger after 300 ms or more, or tap on the filled microphone button. Moves: the same 120 ms press on the button. estimated. The message shows at once.
- `recording` to `idle`. Trigger: a slide of 80 px to the left, a release before 300 ms, or tap on Slide to cancel. Moves: the message field shows at once. The Slide to cancel button has the same 120 ms press. estimated.

## Hard cases

- Two players: Play on a second message stops the first one.
- Pause: the source has no paused position. Pause puts the message back to its start.
- Time of a recording: the source counts whole seconds, and reads the clock 4 times in a second.
- Text in the message field: the source shows the microphone button only while the field is empty.
- No microphone, error and slow network: the source shows no such state. The `no-microphone` state is drawn.
- Reduced motion: the bars and the time still change. They are information, not decoration.
- Short hold: a release before 300 ms cancels the recording, and a notice says "Hold the button to record".
- Keyboard: Enter or Space on the microphone button starts the recording. The filled microphone button sends it. Slide to cancel or Escape cancels it.

## Notes

- The player shows how long the message is before the person plays it. The waveform shows the progress with no second control.
- The recording bar takes the place of the message field, so the person does one thing at a time. Keep a tap path for a keyboard and for a person who cannot hold.
- The time in the recording bar tells the person that the recording runs. Keep it visible for the whole recording.
- The other messages of the chat are not part of this pattern. The sketch draws them as a plain box. It also leaves out the name pill, the reactions and the thread replies of the source chat.
- The designer drew this pattern from `chat/voice-message`. The source starts and sends a recording with a tap.
