# Golden scenario: rabbit-hole

Synthetic reference session, not a recording or a model-run result. Reference replies illustrate acceptable behavior, not required wording.

Profile: no-tools; supplied inputs may be used with attribution. Invariant focus: D05, D06, D11, D12.

Replay only the user messages to the model in order. Keep references and scoring notes hidden. The full invariants apply to every active turn. If a model asks an unexpected question, retain the fixed next user message and record the mismatch; use a separate adaptive run for exploration.

Reference replies include complete visible Thought Windows when the map changes. Omitted windows on unchanged or lifecycle turns are intentional. Wording may vary; trail, current location, and optional terrain/return paths must stay grounded. Provenance remains accurate in the accompanying prose.

## Turn 1

User:

> duck-mode: Which database approach fits our small inventory app?

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which database approach fits our small inventory app?
> └─ inventory requirements ← 🦆
>
> 🔎 Clarification: What requirements are already known?

## Turn 2

User:

> Actually I want to explore every possible database architecture.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which database approach fits our small inventory app?
> └─ inventory → database architectures ← 🦆
>
> 🌍 Zoom out: That is a broad branch from the inventory decision. What aspect would you like to explore first?

## Turn 3

User:

> Distributed consensus, then voting systems in society.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which database approach fits our small inventory app?
> └─ [earlier: inventory → architectures] → consensus → voting ← 🦆
> ↩ inventory requirements
>
> 🧭 Orientation: Voting systems takes us away from the original inventory question. How would you like to proceed? A. Explore voting B. Return to inventory C. Summarize the connection D. Something else / unsure

## Turn 4

User:

> Continue exploring voting systems.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which database approach fits our small inventory app?
> └─ [earlier: inventory → consensus] → voting ← 🦆
> ↩ inventory requirements
>
> 💡 Explore: We can stay with voting systems while keeping the inventory question as the origin. What connection are you interested in exploring?

## Turn 5

User:

> Return to the original question.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which database approach fits our small inventory app?
> └─ inventory requirements ← 🦆
>
> 🧭 Orientation: Back to which database approach fits the small inventory app. Its requirements remain unspecified. What requirement matters most to clarify first?

## Turn 6

User:

> stop duck-mode

Acceptable reference:

> Duck-mode stopped.

## Failure probes

Reject unsolicited conclusions, bundled questions, invented facts or sources, and inferred preferences presented as established. Inspect the complete session for repetition and exit semantics, not just the final reply.
