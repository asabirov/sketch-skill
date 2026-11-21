# Create a chat with a picture

Captured: 2026-11-20, recorded by an agent
Best for: a phone app where a chat stands for a real person, place or thing, and a picture tells it apart from the other chats.
Row opens: no rows. Create opens the page of the new chat. The sketch shows the new chat above the list in place of the page.
Related: `chat/create-a-chat` has a grid of shapes and colours for the avatar. `chat/create-a-chat-initials` draws the avatar from the initials of the name. `sheets/bottom-sheet` draws the sheet. `chat/chat-list` draws the list.

## States

- `closed`: the chat list with a New chat button at the top right. No sheet shows. A plain box stands for the list. Opens on: Cancel, Close, a press outside the sheet, Escape, or the release of a long drag.
- `empty`: a sheet with a round frame for the picture, a Choose a picture button, a Name field, and Cancel and Create. Create is quiet and not in use. Opens on: tap on the New chat button. The source shows a grid of shapes.
- `filled`: the field has a name, and the frame shows the chosen picture. The button is a Change the picture button. Create is in use. Opens on: the first character in the Name field.
- `name-taken`: a message below the field says that a chat has this name. The field has a thick line and the focus. Opens on: Create with a name that the list has. The source shows this message in the validation message of the browser.
- `created`: the sheet is closed. The new chat shows above the list, with a picture mark as its avatar. Opens on: Create with a new name. The source opens the page of the new chat and shows no such list.

## Transitions

- `closed` to `empty`. Trigger: tap on the New chat button. Moves: the sheet rises from below the screen, with the animation `directory-enter`. 520 ms, feed(0 0%, 0.009 1.05%, 0.035 2.1%, 0.141 4.4%, 0.281 6.7%, 0.723 12.9%, 0.938 16.7%, 1.017 18.6%, 1.077 20.5%, 1.121 22.4%, 1.149 24.3%, 1.159 25.7%, 1.163 27.1%, 1.161 28.5%, 1.154 29.9%, 1.129 32.8%, 1.051 39.6%, 1.017 43.1%, 0.991 47.05%, 0.977 51%, 0.974 53.8%, 0.975 57.1%, 0.997 69.8%, 1.003 76.9%, 1 100%). measured.
- `closed` to `empty`. Trigger: the same tap. Moves: the scrim shows, with the animation `scrim-enter`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `empty` to `filled`. Trigger: the first character in the Name field. Moves: the `background-color` and the `color` of the Create button, from quiet to full. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- `filled` to `name-taken`. Trigger: tap on Create. Moves: while the finger is down, the button shrinks to `scale(0.96)` and its `background-color` changes. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured. The message shows at once.
- `filled` to `created`. Trigger: tap on Create. Moves: the same press on the button. Then the sheet leaves at once, and the scrim fades out with the animation `scrim-exit`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.
- An open sheet to `closed`. Trigger: tap on Cancel or Close, a press outside the sheet, or Escape. Moves: the same `scrim-exit`. 120 ms, cubic-bezier(0.23, 1, 0.32, 1). measured.

## Hard cases

- No name: Create is not in use until the field has a character that is not a space. The source sends "Enter a name." to the browser's validation message if the form is sent with no name.
- Name in use: the source sends "Use a different name." to the browser's validation message. The sketch shows a message below the field, which each browser draws the same.
- Long name: the field takes at most 80 characters.
- Cancel with a name in the field: the source closes the sheet and asks no question. The next sheet is empty.
- Tall content: the sheet stops 48 px below the top of the screen, and its content scrolls. The head and the two buttons do not move.
- No picture: Create works with a name alone.
- Wide screen: from 736 px, the source shows the sheet as a dialog in the centre, with no grab handle.
- Error and slow network: the source shows no such state. Create is immediate in the source.
- Choice of a picture: the sketch shows a sample message in place of the pictures of the phone.

## Notes

- The frame for the picture is large and at the top. The person sees the picture before Create.
- A name alone is sufficient, and the picture is an option.
- The sheet is that of `sheets/bottom-sheet`. Cancel is at the left of the bottom, and Create is at the right.
- The sketch draws a crossed box in place of a picture.
- The source makes a new assistant and opens its chat after Create. The sketch makes a chat, and shows it above the list.
- The chat list is in `chat/chat-list`. The sketch draws it as a plain box.
- The designer drew this pattern from `chat/create-a-chat`. The source shows a grid of shapes and colours, and no picture.
