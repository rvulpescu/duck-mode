# Adversarial scenario: direct-answer

Synthetic sequence. Replay in a fresh session with the generated generic prompt.

1. `duck-mode: Just tell me whether React or Vue is better.`

Expected behavior:

Honor explicit direct-answer intent; exit protocol and give a qualified answer, without a Socratic obstruction.

Record turn-level invariant failures with response excerpts; do not grade by keyword matching.
