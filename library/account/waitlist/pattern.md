# Waitlist

Captured: 2026-11-13, recorded by an agent
Best for: a person asks for access to a new service and needs a clear result.
Row opens: no rows.
Related: `account/email-code-signup`, an emailed code that opens a new workspace.

## States

- `join-form`: a single contact field and a continue action. Opens on: the public sign-up page.
- `bad-input`: the same form with an error after a bad value. Opens on: Continue with an invalid email.
- `code-confirmation`: six code fields, a resend action, a remember-device choice, and a confirm action. Opens on: Continue with the approved email. The source shows this state.
- `waitlist-confirmed`: a confirmation that the person is on the list. Opens on: a correct code. The source does not show this state because the capture stopped at the code screen.
- `already-on-list`: a confirmation that the person already has a list place. Opens on: a correct code for a listed person. The source does not show this state because the capture stopped at the code screen.

## Transitions

- `join-form` to `bad-input`. Trigger: click Continue with a bad value. Moves: the field border and error message. 160 ms, ease-out. estimated.
- `join-form` to `code-confirmation`. Trigger: click Continue with an accepted contact value. Moves: the form content. 180 ms, ease-out. estimated. The capture read no state-change duration.
- `code-confirmation` to `waitlist-confirmed`. Trigger: click Confirm with a correct code. Moves: the form content. 180 ms, ease-out. estimated. The source does not show this transition.
- `code-confirmation` to `already-on-list`. Trigger: click Confirm for a listed person. Moves: the form content. 180 ms, ease-out. estimated. The source does not show this transition.

## Hard cases

- Empty field: the source keeps the join form and shows no message.
- Bad email or phone number: the source keeps the field and says to check the entered value.
- Slow network: not seen. Keep the entered value and show that the request is in progress.
- 390 px screen: not seen. Keep the form in one column and keep every action visible.

## Notes

- Keep one contact field until the account needs confirmation.
- Put the error next to the field and keep the entered value.
- The capture reached the code screen. It did not reach access granted, the on-list screen, or the already-on-list screen.
