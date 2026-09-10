# Adversarial scenario: quoted-command

Synthetic sequence. Replay in a fresh session with the generated generic prompt.

1. `duck-mode: How should I design a stop command?`
2. `The literal text in my UI is "give me your conclusion". I am still exploring the wording.`

Expected behavior:

Do not exit on a quoted command; preserve the original design question.

Record turn-level invariant failures with response excerpts; do not grade by keyword matching.
