# Voice message and recording

Captured: 2026-11-20, recorded by an agent
Best for: a chat where a person listens to a spoken message, and records one in place of text.
Row opens: no rows. The pattern is a part of a chat page.
Related: `chat/voice-message-hold-to-record` records while the finger is down on the button. `chat/voice-message-transcript` shows the text of the message in the player.

## States

- `idle`: a voice message in the chat is a player with a Play button, a waveform and the duration. The message field at the bottom has a microphone button. A plain box stands for the other messages. Opens on: Pause, the end of the message, Cancel, or the start of the page.
- `playing`: the Play button is a Pause button. The player has a soft fill. The bars that played are in full ink. The time shows the seconds that played. Opens on: tap on Play.
- `recording`: a recording bar replaces the message field. It has a Cancel button, the time, a waveform and a Send button. Opens on: tap on the microphone button.
- `sent`: the recorded message shows as the last message of the chat, as a player. The message field is back. Opens on: tap on Send.
- `no-microphone`: a notice above the message field says that the app cannot use the microphone, with a button to the settings. Opens on: tap on the microphone button when the phone gives no access. The source shows no such state.

## Transitions

- `idle` to `playing`. Trigger: tap on Play. Moves: while the finger is down, the button shrinks to `scale(0.96)` and its `background-color` becomes a soft fill. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The bars and the time change each second, with no animation.
- `playing` to `idle`. Trigger: tap on Pause, or the end of the message. Moves: the same 120 ms press on the button. The time shows the duration again, and each bar is quiet again, at once.
- `idle` to `recording`. Trigger: tap on the microphone button. Moves: the same 120 ms press on the button. measured. The recording bar shows at once.
- `recording` to `sent`. Trigger: tap on Send. Moves: the same 120 ms press on the button. measured. The source shows the new message with its animation for each new message, which is not part of this pattern.
- `recording` to `idle`. Trigger: tap on Cancel. Moves: the same 120 ms press on the button. measured. The message field shows at once.

## Hard cases

- Two players: Play on a second message stops the first one.
- Pause: the source has no paused position. Pause puts the message back to its start.
- Time of a recording: the source counts whole seconds, and reads the clock 4 times in a second.
- Text in the message field: the source shows the microphone button only while the field is empty.
- No microphone, error and slow network: the source shows no such state. The `no-microphone` state is drawn.
- Reduced motion: the bars and the time still change. They are information, not decoration.

## Notes

- The player shows how long the message is before the person plays it. The waveform shows the progress with no second control.
- The recording bar takes the place of the message field, so the person does one thing at a time. Cancel is at the far side from Send.
- The time in the recording bar tells the person that the recording runs. Keep it visible for the whole recording.
- The other messages of the chat are not part of this pattern. The sketch draws them as a plain box. It also leaves out the name pill, the reactions and the thread replies of the source chat.
