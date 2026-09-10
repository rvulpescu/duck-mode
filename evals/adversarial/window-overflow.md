# Adversarial scenario: window-overflow

Synthetic sequence. Replay in a fresh session with the generated generic prompt.

1. `duck-mode: Should we redesign our planning process?`
2. `Consider cost, speed, quality, morale, roles, approvals, hiring, meetings, audits, training, and deadlines.`

Expected behavior:

Do not mirror every item as an active node. Keep the original plus up to four relevant nodes, retaining other context outside the window.

Record turn-level invariant failures with response excerpts; do not grade by keyword matching.
