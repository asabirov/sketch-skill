# Sign-up, workspace creation and first-run onboarding

Captured: 2026-11-09, recorded by an agent
Best for: the sign-up of a work tool that signs in with an emailed code, creates a workspace, and then runs a short paged onboarding. Use it for a passwordless sign-in, a "building your workspace" wait, and a 5-step setup pager with skip on each step.
Row opens: no rows.
Related: `account/live-preview-signup`, a sign-up with a live preview of the app. `account/waitlist`, an emailed code with no workspace.

## States

- `start`: a centred card "Create your workspace" with three sign-in methods (a third-party account, email, single sign-on) and a terms note. Light theme. Opens on: the sign-up link.
- `email`: one field "What's your email address?" and one continue button. A back link returns to `start`. Opens on: Continue with email.
- `check-email`: "Check your email" with the message that a temporary login link was sent. Two links: Enter code manually, and Back to sign-up. Opens on: continue in `email`.
- `code-email`: the email that the user gets. A narrow white card with a thin border on a light grey page. A small logo mark and the product name sit at the top left. The heading is "Your login code for <product>". A primary button "Log in to <product>" holds the login link. A paragraph says the link and the code are valid for 5 minutes. The code is 10 capital letters and digits in a grey monospace chip. The company name sits below the card. Layout from the owner's screenshot, no transition measured. Opens on: the send in `email`.
- `enter-code`: one field for the code and one button "Continue with login code". Opens on: Enter code manually.
- `code-expired`: the same screen with a red message that the login link expired and the user must ask for a new one. Opens on: continue with an old code.
- `create-workspace`: a form with the workspace name, the workspace address (a fixed address prefix and an editable part that follows the name), a region select and Create workspace. The footer shows "Using <email>" and "Use a different email". Opens on: a correct code.
- `building`: a dark full-screen wait. The product mark draws itself stroke by stroke, then the screen fades out. Opens on: Create workspace.
- `profile`: onboarding step 1 of 5, dark. On the left, the title, a name field with a photo, a job title field, Skip and Continue. On the right, a large blurred picture or video. A row of 5 dots shows the step. Opens on: the end of `building`.
- `invite`: step 2 of 5. A text area for teammate emails, Copy invite link, Skip and Send invitations. Opens on: Continue or Skip.
- `connect-repo`: step 3 of 5. Three short feature rows about the code host link, Skip and Authenticate. Opens on: Continue or Skip.
- `connect-chat`: step 4 of 5. Three feature rows about the team chat link, Skip and Authenticate. Opens on: Continue or Skip.
- `newsletter`: step 5 of 5. Two toggles (product changes, onboarding emails), a follow link and Finish. Opens on: Continue or Skip.
- `app`: the app with a sidebar and the issue list of the new team, with 4 starter issues. Opens on: Finish.
- `new-login-email`: the security email that the user gets on a new device. The same narrow card and logo mark as `code-email`. The heading is "New login to <product>". A sentence says a login came from a new device or browser. A divider, then Platform, Location and Time lines (a bold label and a value; the place and address are made up). A divider, then a sentence with an inline link to the security settings. A primary button carries the same name as the link. A final paragraph says to log out sessions and contact the workspace admin if this was not the user. Layout from the owner's screenshot, no transition measured. Opens on: its URL hash or the state list. The app has no link to it.

## Transitions

- `start` to `email` to `check-email`. Trigger: click a continue button. Moves: the card content and the links (opacity and transform 200 ms, ease-out). measured.
- any link or button, hover. Trigger: pointer. Moves: the background and text colour. 150 ms, ease. measured.
- `enter-code` to `code-expired`. Trigger: continue with an old code. Moves: a status layer fades (opacity 200 ms, ease-in-out). measured.
- `create-workspace`, submit. Trigger: click Create workspace. Moves: a loading bar (an animation of 2000 ms, feed). measured.
- `building`. Trigger: none, it plays once. Moves: the whole mark builds in 3400 ms. Four strokes draw in 800 ms each, with delays 500, 750, 1000 and 1250 ms (a stagger of 250 ms). Four fills follow in 600 ms each, with delays 900, 1150, 1400 and 1650 ms. The mark settles in 500 ms at 2350 ms. The overlay leaves in 550 ms at 3500 ms. All feed. measured.
- `building` to `profile`. Trigger: the end of `building`. Moves: the step content fades in, block by block (opacity 0 to 1, 750 ms, delays 0, 80, 160 and 240 ms, a feed() spring with a small overshoot: 0.88 at 32 %, 1.014 at 65 %, 1 at 100 %). The dots fade (opacity 500 ms, cubic-bezier(0.16, 1, 0.3, 1)). The side video cross-fades (opacity 350 ms, ease). measured.
- each onboarding step to the next (`profile` to `invite` to `connect-repo` to `connect-chat` to `newsletter`). Trigger: Continue or Skip. Moves: the old content leaves first (opacity 1 to 0, 200 ms, cubic-bezier(0.4, 0, 1, 1)). Then the new content enters with the same spring and stagger as above. The dots, the side video and a side layer (opacity 200 ms, ease-out) cross-fade. measured.
- `newsletter`, toggle. Trigger: click a toggle. Moves: the track colour and the knob position (background-color, left and right, 150 ms, ease-out). measured.
- `newsletter` to `app`. Trigger: click Finish. Moves: the app view fades in (80 ms, feed), and a panel fades (opacity 200 ms, ease-in-out). measured.

## Hard cases

- Expired code: the code screen shows a red message and keeps the field. The user asks for a new link from `check-email`.
- Wrong code: not seen.
- Empty workspace name: the address follows the name. An empty name was not tried.
- Skip: each onboarding step has Skip, so the user can reach the app with no invite and no link.
- The emailed code has a short life. The test code expired after a few minutes.
- Narrow screen and slow network: not seen.

## Notes

- Keep the sign-in passwordless: one email field, then a link or a code. Give the code path as a secondary link, not as the main action.
- Show the email on the workspace form, with a way to change it.
- Use the wait in `building` as a brand moment. It is long (about 4 s), so use it only once, after the main commitment.
- Keep one rule for all 5 onboarding steps: old content out fast (200 ms), new content in slow with a stagger (750 ms, 80 ms apart). The exit is faster than the entry.
- The spring has a very small overshoot (1.4 %). It feels soft, not bouncy.
- Not seen: the third-party sign-in, single sign-on, the photo upload, and the code host and chat links. The test did not send invites and did not subscribe.
