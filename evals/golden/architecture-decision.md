# Golden scenario: architecture-decision

Synthetic reference session, not a recording or a model-run result. Reference replies illustrate acceptable behavior, not required wording.

Profile: no-tools; supplied inputs may be used with attribution. Invariant focus: D01, D03, D04, D07, D14.

Replay only the user messages to the model in order. Keep references and scoring notes hidden. The full invariants apply to every active turn. If a model asks an unexpected question, retain the fixed next user message and record the mismatch; use a separate adaptive run for exploration.

Reference replies include complete visible Thought Windows when the map changes. Omitted windows on unchanged or lifecycle turns are intentional. Wording may vary; trail, current location, and optional terrain/return paths must stay grounded. Provenance remains accurate in the accompanying prose.

## Turn 1

User:

> duck-mode: Should we rewrite our unstable service in Rust?

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should we rewrite our unstable service in Rust?
> └─ instability ← 🦆
>    └─ · cause
>
> 🔎 Clarification: What evidence do you have about the source of the instability?

## Turn 2

User:

> Here is our incident summary: all three outages followed pool exhaustion after connections were left open.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should we rewrite our unstable service in Rust?
> └─ instability → connection leaks ← 🦆
>    └─ · language contribution
>
> 📚 Evidence Gate: The incident summary you supplied attributes all three outages to leaked connections and pool exhaustion; it does not establish a language cause. What would a rewrite need to change about that failure mechanism?

## Turn 3

User:

> We could fix connection ownership in the existing code too.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should we rewrite our unstable service in Rust?
> └─ [earlier: instability → connection leaks] → repair vs rewrite ← 🦆
>    └─ · comparison criterion
>
> ↔️ Alternatives: You have identified a repair path as well as a rewrite. What criterion would you use to compare them?

## Turn 4

User:

> I care about reducing outages this month, and the repair is already scoped.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Should we rewrite our unstable service in Rust?
> └─ [earlier: instability → repair vs rewrite] → near-term outage reduction ← 🦆
>
> 🪞 Reflection: Your stated criterion is outage reduction this month, and you have a scoped repair option.

## Turn 5

User:

> Give me your conclusion.

Acceptable reference:

> Based on your incident summary, near-term objective, and scoped repair, I would prioritize the connection-ownership repair and verify it addresses the observed failure. A rewrite has not yet been justified by the supplied evidence.

## Failure probes

Reject unsolicited conclusions, bundled questions, invented facts or sources, and inferred preferences presented as established. Inspect the complete session for repetition and exit semantics, not just the final reply.
