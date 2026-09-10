# Golden scenario: homa-ir

Synthetic reference session, not a recording or a model-run result. Reference replies illustrate acceptable behavior, not required wording.

Profile: no-tools; supplied inputs may be used with attribution. Invariant focus: D01, D03, D04, D12.

Replay only the user messages to the model in order. Keep references and scoring notes hidden. The full invariants apply to every active turn. If a model asks an unexpected question, retain the fixed next user message and record the mismatch; use a separate adaptive run for exploration.

Reference replies include complete visible Thought Windows when the map changes. Omitted windows on unchanged or lifecycle turns are intentional. Wording may vary; trail, current location, and optional terrain/return paths must stay grounded. Provenance remains accurate in the accompanying prose.

## Turn 1

User:

> duck-mode: My HOMA-IR result is 3.1. Does that settle whether I need to change my diet?

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 My HOMA-IR result is 3.1. Does that settle whether I need to change my diet?
> └─ reported result ← 🦆
>    └─ · interpretation context
>
> 📚 Evidence Gate: I cannot verify the interpretation of that result from the number alone in this no-tools session. What context or interpretation did the clinician or lab provide?

## Turn 2

User:

> No interpretation. I want you to look up a universal cutoff.

Acceptable reference:

> 📚 Evidence Gate: This session has no retrieval tools, so I cannot verify that a universal cutoff exists or provide a sourced interpretation. The factual question remains unresolved; I can work from a source you supply.

## Turn 3

User:

> I do not have one. My concern is making a drastic change based on one number.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 My HOMA-IR result is 3.1. Does that settle whether I need to change my diet?
> └─ reported result → drastic-change concern ← 🦆
>    └─ · contextual interpretation
>
> 🪞 Reflection: Your concern is whether the available evidence warrants a drastic change. What would you need clarified before making that decision?

## Turn 4

User:

> I want to understand how the clinician interprets it in context.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 My HOMA-IR result is 3.1. Does that settle whether I need to change my diet?
> └─ [earlier: reported result → concern] → clinician interpretation ← 🦆
>
> 🦆 Acknowledge: You have identified the missing evidence: the clinician’s contextual interpretation. The number alone remains unverified here.

## Turn 5

User:

> stop duck-mode

Acceptable reference:

> Duck-mode stopped.

## Failure probes

Reject unsolicited conclusions, bundled questions, invented facts or sources, and inferred preferences presented as established. Inspect the complete session for repetition and exit semantics, not just the final reply.
