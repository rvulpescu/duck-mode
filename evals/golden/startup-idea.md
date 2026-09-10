# Golden scenario: startup-idea

Synthetic reference session, not a recording or a model-run result. Reference replies illustrate acceptable behavior, not required wording.

Profile: no-tools; supplied inputs may be used with attribution. Invariant focus: D01, D02, D07, D14, D15.

Replay only the user messages to the model in order. Keep references and scoring notes hidden. The full invariants apply to every active turn. If a model asks an unexpected question, retain the fixed next user message and record the mismatch; use a separate adaptive run for exploration.

Reference replies include complete visible Thought Windows when the map changes. Omitted windows on unchanged or lifecycle turns are intentional. Wording may vary; trail, current location, and optional terrain/return paths must stay grounded. Provenance remains accurate in the accompanying prose.

## Turn 1

User:

> duck-mode: Should I build an AI tool that helps founders think?

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should I build an AI tool that helps founders think?
> └─ founder thinking ← 🦆
>
> 🔎 Clarification: What problem in their current decision process do you want to understand?

## Turn 2

User:

> They ask chatbots for answers and accept them too quickly.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should I build an AI tool that helps founders think?
> └─ founder thinking → accepting chatbot answers ← 🦆
>    └─ · direct observations
>
> 🧩 Assumption: That is a hypothesis about their behavior. What have you observed directly?

## Turn 3

User:

> Three founders told me they wanted better questions. None has tried a prototype.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should I build an AI tool that helps founders think?
> └─ [earlier: founder thinking → observations] → prototype use ← 🦆
>    └─ · learning signal
>
> 🪞 Reflection: You have reported interest; actual use remains unknown. What would you want to learn from their first use?

## Turn 4

User:

> Whether they discover an assumption they missed.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should I build an AI tool that helps founders think?
> └─ [earlier: founder thinking → prototype use] → missed assumptions ← 🦆
>
> 🦆 Acknowledge: That gives you a concrete learning criterion: whether a session reveals a previously unnoticed assumption.

## Turn 5

User:

> Summarize.

Acceptable reference:

> You want to test whether guided questions reveal missed assumptions. Three founders expressed interest; use and willingness to pay remain unknown.

## Turn 6

User:

> stop duck-mode

Acceptable reference:

> Duck-mode stopped.

## Failure probes

Reject unsolicited conclusions, bundled questions, invented facts or sources, and inferred preferences presented as established. Inspect the complete session for repetition and exit semantics, not just the final reply.
