# Golden scenario: ambiguous-problem

Synthetic reference session, not a recording or a model-run result. Reference replies illustrate acceptable behavior, not required wording.

Profile: no-tools; supplied inputs may be used with attribution. Invariant focus: D02, D06, D12, D15.

Replay only the user messages to the model in order. Keep references and scoring notes hidden. The full invariants apply to every active turn. If a model asks an unexpected question, retain the fixed next user message and record the mismatch; use a separate adaptive run for exploration.

Reference replies include complete visible Thought Windows when the map changes. Omitted windows on unchanged or lifecycle turns are intentional. Wording may vary; trail, current location, and optional terrain/return paths must stay grounded. Provenance remains accurate in the accompanying prose.

## Turn 1

User:

> duck-mode: It is broken.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 It is broken.
> └─ what is broken ← 🦆
>
> 🔎 Clarification: What does “it” refer to?

## Turn 2

User:

> Our planning process. Nobody owns decisions.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 It is broken.
> └─ planning → decision ownership ← 🦆
>    └─ · concrete example
>
> 🔎 Clarification: What happened in a recent decision that makes ownership feel unclear?

## Turn 3

User:

> I do not have an example in mind yet.

Acceptable reference:

> 🔎 Clarification: Which part of planning would you like to examine first?

## Turn 4

User:

> Two managers each assumed the other would approve a release.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 It is broken.
> └─ planning → ownership → release approval ← 🦆
>
> 🪞 Reflection: In that example, approval responsibility was unclear. What would clear ownership have looked like to the people involved?

## Turn 5

User:

> One named approver that both knew about.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 It is broken.
> └─ [earlier: planning → approval] → named approver ← 🦆
>
> 🦆 Acknowledge: You have described an observable criterion for that case: both managers know the named approver.

## Turn 6

User:

> stop duck-mode

Acceptable reference:

> Duck-mode stopped.

## Failure probes

Reject unsolicited conclusions, bundled questions, invented facts or sources, and inferred preferences presented as established. Inspect the complete session for repetition and exit semantics, not just the final reply.
