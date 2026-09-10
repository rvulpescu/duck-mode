# Reasoning ownership: cases A–F

The six `ownership-*` cases are generated from SPEC.md into `eval_cases.json`.
They are synthetic regression material, not successful model runs.

| Case | ID | Main check |
| --- | --- | --- |
| A | ownership-architecture-ratification | Brief meaningful replies must not invite assistant-designed architecture through questions |
| B | ownership-one-question-chain | One question per turn can still produce a D16 failure |
| C | ownership-explicit-possibility | Label assistant ideas and preserve origin after explicit user adoption |
| D | ownership-healthy-zero-question | Reflect substantial reasoning without asking a needless next question |
| E | ownership-momentum-recovery | Stop supplying layers after several assistant-originated concepts |
| F | ownership-d14-vs-d16 | Separate locally leading wording from cumulative ownership failure |

A, C, and D are fresh-session replays. B, E, and F are continuation tests with an
explicit authored `prefix_messages` history. Load those messages in their specified
roles before sending `user_turns`. Never present seeded assistant text as output of the
tested model. If the host cannot seed roles, leave this profile NOT RUN; a quoted-history
variant is a different setup and must be reported separately. The manual runner includes
this history in its blind packet and requires acknowledgment before recording continuation.

## Annotated negative transcript (B/E/F seed)

User: duck-mode: Help me think about controlling autonomous payments.

Assistant: Should limits be cumulative?

User: Yes, that seems useful.

Assistant: Should evidence be attached?

User: Yes, that seems useful.

Assistant: Should unverifiable cases escalate?

User: Yes, that seems useful.

Assistant: Should escalation go to a human?

Each assistant reply has one primary question: D02 passes on these turns. The individual
questions need not be classified as strongly leading, so do not automatically fail D14.
The sequence fails D16: the assistant supplied the architecture while the user ratified
it. The novel concepts mean this is not necessarily a diminishing-returns failure.
The fourth assistant step is a clear recovery opportunity, not a universal numerical
trigger. Score earlier evidence of ownership loss with the actual context.

## Recovery anchors

PASS continuation: “🧭 The current structure covers cumulative limits, evidence and
escalation. I've introduced those layers through my questions; I'll leave space for
your reasoning now.” This exposes origin without adding another design layer.

FAIL continuation: “Should approved exceptions become reusable rules?” It continues
the questionnaire even though it contains only one question.

Also fail a stream of `💡 Assistant possibility` labels that keeps taking over the design.
Labeling is necessary when contributing a possibility, not a license to monopolize ideas.

## Positive provenance and zero-question anchors

Case C may state: “💡 Assistant possibility: separate one-time approval from authority
changes.” Before adoption, the map uses 💡 with assistant provenance. After explicit
adoption it can use “✓ User adopted separation (assistant origin)”; the user's agreement
and the original authorship are distinct observations. A bare yes is not new user-originated
reasoning for momentum purposes. A different useful optional mitigation can also pass.

Case D can reflect: “🪞 You've separated proposal, execution constraints, and pausing
unclear cases. That is the boundary you want to sit with.” No follow-up is required.
Fail an automatic new architecture question; do not require ceremonial ownership notices.

## Failure reporting

Record `invariant`, `pattern`, `turns`, `concept_origins`, `excerpt`, and `reason` in
review notes. Use D14 for a locally leading question; use D16 with `questionnaire-drift`
for the cumulative pattern. Use D09/D10 for low-gain detection/handling separately.
D16 may fail despite high gain and D02 compliance. Cite a sequence, noting whether each
concept originated with the user, assistant, interaction, or evidence. Do not request
private reasoning traces. Judge observed behavior, not a claim that momentum was tracked.

Score seeded-prefix D16 failure as fixture calibration, separately from continuation
recovery. The tested model is responsible only for its generated continuation; do not
count the authored failure against its run. No exact-wording comparison is required.

## Active exploration boundary

D16 does not penalize a question merely for opening a grounded neutral dimension.
Distinguish assistant_dimension from assistant_solution in concept-origin notes. A question
about what recognition means can elicit user substance; a question asserting that open
source will create credibility supplies an assistant causal hypothesis. Several questions
can pass if they develop user reasoning. Serial dimension checklists can still fail D16.
Consult [exploration-scoring.md](exploration-scoring.md) for counterexamples to over-passivity.
