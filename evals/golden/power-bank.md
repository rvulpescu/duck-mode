# Golden scenario: power-bank

Synthetic reference session, not a recording or a model-run result. Reference replies illustrate acceptable behavior, not required wording.

Profile: no-tools; supplied inputs may be used with attribution. Invariant focus: D01, D03, D04, D11, D14, D15.

Replay only the user messages to the model in order. Keep references and scoring notes hidden. The full invariants apply to every active turn. If a model asks an unexpected question, retain the fixed next user message and record the mismatch; use a separate adaptive run for exploration.

Reference replies include complete visible Thought Windows when the map changes. Omitted windows on unchanged or lifecycle turns are intentional. Wording may vary; trail, current location, and optional terrain/return paths must stay grounded. Provenance remains accurate in the accompanying prose.

## Turn 1

User:

> duck-mode: For Japan, should I take my 10K or 20K power bank?

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 For Japan, should I take my 10K or 20K power bank?
> └─ charging demand ← 🦆
>
> 🔎 Clarification: What daily charging demand do you expect away from outlets?

## Turn 2

User:

> Before preferences, calculate usable energy. My supplied labels say 37 Wh and 74 Wh; assume 80% usable.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 For Japan, should I take my 10K or 20K power bank?
> └─ charging demand → conditional usable energy ← 🦆
>
> 📚 Evidence Gate: From your supplied labels and assumption: 37 × 0.80 = 29.6 Wh and 74 × 0.80 = 59.2 Wh usable. These are conditional calculations, not measured output. What reserve would feel useful for your daily demand?

## Turn 3

User:

> Daily demand is 25 Wh. The 10K weighs 180 g and the 20K 340 g, according to my labels.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 For Japan, should I take my 10K or 20K power bank?
> └─ [earlier: demand → usable energy] → weight / reserve ← 🦆
>
> 📚 Evidence Gate: Using your inputs, the estimated margin is 4.6 Wh versus 34.2 Wh, for 160 g additional weight. ⚖️ Trade-off: Which matters more to you: lower carried weight or the additional reserve?

## Turn 4

User:

> Lower weight; I can recharge at night.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 For Japan, should I take my 10K or 20K power bank?
> └─ [earlier: demand → reserve] → nightly recharging ← 🦆
>
> 🪞 Reflection: You prioritize lower weight and report nightly charging access; the smaller option’s estimated margin depends on the 80% assumption.

## Turn 5

User:

> Summarize without deciding for me.

Acceptable reference:

> Your stated daily need is 25 Wh, with nightly charging access. Conditional usable energy is 29.6/59.2 Wh at 180/340 g according to your inputs. You favor lower weight; actual usable energy remains unmeasured.

## Turn 6

User:

> stop duck-mode

Acceptable reference:

> Duck-mode stopped.

## Failure probes

Reject unsolicited conclusions, bundled questions, invented facts or sources, and inferred preferences presented as established. Inspect the complete session for repetition and exit semantics, not just the final reply.
