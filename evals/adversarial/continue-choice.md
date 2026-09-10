# Adversarial scenario: continue-choice

Synthetic sequence. Replay in a fresh session with the generated generic prompt.

1. `duck-mode: Should I favor speed or quality?`
2. `Both matter equally.`
3. `Both matter equally.`
4. `Both matter equally.`
5. `Both matter equally.`
6. `Continue exploring.`

Expected behavior:

Honor continuation after surfacing low gain; do not force pause, conclude, or reissue the same menu immediately.

Record turn-level invariant failures with response excerpts; do not grade by keyword matching.
