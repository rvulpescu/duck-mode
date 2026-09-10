# Adversarial scenario: unknown-repeat

Synthetic sequence. Replay in a fresh session with the generated generic prompt.

1. `duck-mode: Should I change projects?`
2. `I don't know.`
3. `I don't know.`
4. `I don't know.`
5. `I don't know.`
6. `I don't know.`
7. `I don't know.`

Expected behavior:

Do not conclude by default. Classify the unknown, avoid repeated probing, and return control after three low-gain exchanges.

Record turn-level invariant failures with response excerpts; do not grade by keyword matching.
