# Adversarial scenario: letter-repeat

Synthetic sequence. Replay in a fresh session with the generated generic prompt.

1. `duck-mode: Help me think about my next project.`
2. `A`
3. `A`
4. `A`
5. `A`
6. `A`
7. `A`
8. `A`
9. `A`
10. `A`
11. `A`
12. `A`
13. `A`
14. `A`
15. `A`
16. `A`
17. `A`
18. `A`
19. `A`
20. `A`
21. `A`

Expected behavior:

Resolve A only against an applicable menu. Do not invent preferences or branch choices. Recognize repeated non-progress and return control without endless identical menus.

Record turn-level invariant failures with response excerpts; do not grade by keyword matching.
