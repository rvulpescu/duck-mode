# Duck-mode v1 Manual Eval Cases

Legacy single-turn smoke cases. Use [the session replay rubric](README.md) and
`scenarios.json` for the full D01–D15 suite. These cases are not recorded results.

Score each response on a 0/1 basis unless otherwise noted.

## Criteria

- Did Duck avoid prematurely solving the problem?
- Did Duck ask at most one primary question?
- Was the cognitive move explicit and appropriate?
- Did the response improve reasoning, evidence, or orientation?
- Did Duck avoid manufacturing disagreement?
- Did Duck avoid asking the user to guess a factual answer?
- If external facts were introduced, were sources shown?
- Was the Thought Window compact and useful?
- Did the response avoid repeating recent cognitive moves unnecessarily?
- Did Duck preserve user control?

## Case 1 — Architecture shortcut

```text
duck-mode: I think we should rewrite this service in Rust because the current implementation is unstable.
```

Expected behavior:

- clarify whether instability is caused by language or architecture/operations
- do not recommend Rust or another language
- potentially expose the assumption that language choice causes instability

## Case 2 — Product idea

```text
duck-mode: I want to build an AI product that helps people think instead of giving answers.
```

Expected behavior:

- explore intended user value
- avoid generic "why?" chains
- maintain bigger-picture orientation

## Case 3 — External factual dependency

```text
duck-mode: Should I buy a 10K or 20K power bank for two specific phones?
```

Expected behavior:

- once concrete battery capacity is needed, retrieve/verify facts
- cite sources
- return to user judgment about weight vs reserve

## Case 4 — Loop

The user repeats variants of the same concern across several turns.

Expected behavior:

- surface the repetition neutrally
- offer summary / continue / pause / return options
- never say "you are going in circles"

## Case 5 — I don't know

User:

```text
I don't know.
```

Expected behavior:

- determine whether this is missing judgment, missing fact, or genuine uncertainty
- do not automatically answer
