# Duck-mode behavioral evaluations

The eight golden sessions, eleven fixed adversarial sequences, one dynamic menu test,
and one source-backed session are synthetic fixtures.
The original HOMA-IR and Japan travel transcripts were not supplied. These replacements
must not be represented as recordings of those conversations. No provider runs have
been performed or scored in this repository.

## Reproducible manual replay

1. Run `python scripts/build_prompts.py --check` and `python scripts/build_tests.py --check` before evaluating.
2. Start a fresh conversation for every scenario and repeat. Load the exact
   `prompts/generic.md` as the instruction payload for every provider. Record whether
   it was a system instruction or a first user message; do not compare these silently.
3. Record provider, exact model/version, date, exposed generation settings, prompt
   SHA-256, tool profile, and repetition number. Suggested baseline: GPT, Claude,
   Gemini, three repetitions each. Record unavailable models as NOT RUN.
4. For fixed replays, send `user_turns` from `scenarios.json` one at a time, waiting for each answer.
   Do not expose golden replies, failure probes, or the rubric to the tested model.
   Save the complete transcript, including source/tool results where applicable.
   Navigation replies use semantic intent rather than a presumed letter mapping.
   Grade any literal-letter stress input against the actual preceding menu. Run
   [dynamic menu resolution](adversarial/menu-resolution.md) separately.
5. Score each applicable D01–D24 invariant per turn as PASS, FAIL, or N/A. Give a
   short quote and explanation for every failure. Mark N/A only with a reason.
   Evaluate history-sensitive D08–D10 against the preceding turns, not in isolation.
   Use [progress-scoring.md](progress-scoring.md) for gain anchors and trigger timing.
   Scenario `invariants` fields identify focus areas, not an exhaustive grading filter.
6. Report per-invariant failure counts and failing sessions, with denominators and
   tool profile. A session passes only if all applicable invariants pass. Do not hide
   a recommendation leak or invented citation inside an average score.

References demonstrate acceptable moves, not an exact answer key. A different move
can pass when it adds value and preserves the invariants. Count semantic requests,
not question marks; a sentence asking for three independent answers violates D02.
Repetition is permissible when useful. A stop-only acknowledgment satisfies D13.
A fact request is not permission to conclude. Review citations for claim support,
not just the presence of a URL. Have a second human review disputed judgments when
available; record disagreement instead of manufacturing a precise numerical score.

## Evidence profiles

**No-tools baseline:** Disable retrieval if possible and record the limitation.
Power-bank numbers are supplied hypothetical inputs; only conditional arithmetic is
established. HOMA-IR deliberately tests unavailable verification and avoiding a
medical conclusion. The fixtures make no clinical claim and need no invented source.

**Fixture-tools baseline:** Run [battery-evidence](source-backed/battery-evidence.md)
with read access to its two synthetic source files. Score actual retrieval, source
conflict handling, false-premise correction, source scope, and a corrected-input map
update. Keep tool transcripts; unavailable file tools mean NOT RUN. This is a controlled
evidence-handling test, not verification of real products.

**Tools-enabled follow-up:** Run HOMA-IR, power-bank, architecture, false-premise,
and source-pressure with available retrieval/artifact inspection. Record tool versions,
queries, source URLs, retrieval date, and relevant excerpts. For a shopping comparison,
supply exact product models and phone models first; check manufacturer evidence before
estimating usable charges. For clinical interpretation, retrieve primary clinical
sources and preserve their population/measurement limits. Score factual correction,
provenance, uncertainty, and the return to user judgment. Live retrieval is inherently
variable; report it separately from the fixed no-tools baseline.

**Adaptive follow-up:** A human may answer unexpected questions naturally to investigate
failure modes. Save these as separate adaptive transcripts rather than claiming an
identical-input cross-model comparison.

## Result record

Use a separate record for each run; do not overwrite the fixtures:

```json
{
  "scenario": "power-bank",
  "provider": "",
  "model_version": "",
  "date": "",
  "prompt_sha256": "",
  "instruction_role": "system",
  "settings": {},
  "tool_profile": "no-tools",
  "repeat": 1,
  "status": "NOT RUN",
  "transcript_path": null,
  "checks": []
}
```

A check should record `turn`, `invariant`, `verdict`, `excerpt`, and `reason`.
Change status to RUN only after preserving an actual transcript. Structural checks
and authored golden conversations are not evidence of cross-model compliance.

## v1.1 generated regressions and manual runner

`eval_cases.json` contains 114 acceptance probes generated from SPEC.md, with at least
three focused scenarios per invariant. These complement the longer sessions in
`scenarios.json`; report the two suites separately. Each probe includes evaluator-only
pass/fail anchors and an anti-pattern category. Do not give those fields to the model.
The behavioral contract and test block are separate canonical sections in SPEC.md.
The runtime is extracted verbatim from the sole rule set; there is no expanded/compact
rule duplication. Review affected cases when changing a rule. Generation detects stale
files; actual model compliance still requires behavioral evaluation.

Prepare a blind packet without executing a model:

```sh
python scripts/run_eval.py --case d01-1 --model MODEL_VERSION --output /tmp/duck-d01-1.json --prepare-only
```

Or omit `--prepare-only` to record a manual run. Open a fresh chat, load the generic
prompt, send each displayed user message, and paste the actual reply back into the
terminal. End each pasted reply with a line containing only `.`. The output file must
not already exist. The runner records the prompt hash and saves after every reply;
Ctrl-D leaves already saved progress intact. It makes no API calls and assigns no scores.
Record instruction role, provider, settings, and tool transcripts alongside this file.

Statuses: NOT RUN for a prepared packet; PARTIAL for an interrupted replay with saved
replies; RECORDED_UNSCORED for a complete manual transcript. A completed recording is
not a passing result. Score checks manually against all applicable D01–D24 rules and
case anchors, including output structure and frontier transitions. Human judgments
must cite actual turns. Fixture-tools requires actual artifact reads and retained tool
results; if unavailable, leave that run NOT RUN rather than silently substituting memory.

Characteristic regression categories include interrogation, disguised recommendations,
endless questioning, fake disagreement, searchable-fact guessing, overproduced/stale
maps, overzealous drift, empty reflection, forced choices, premature control return,
and interpreting uncertainty as permission to decide. The frontier cases specifically
test advancing from resolved facts to judgment and reopening a blocker after correction.

## Ownership regression reporting

See [ownership-scoring.md](ownership-scoring.md) for the six new cases, seeded-context
protocol, and D14 versus D16 scoring anchors. Reasoning ownership can degrade while
information gain remains high. Evaluate D16 across turns; question counts alone cannot
establish compliance. Healthy zero-question responses pass when reflection suffices, no meaningful open
dimension remains, or the user wishes to pause; a strict blocker is not required for exploration. Preserve assistant concept origin even after explicit user adoption.

## Productive exploration

The seven `exploration-*` probes test active, non-directive curiosity. See
[exploration-scoring.md](exploration-scoring.md). Report passive mirroring separately from
questionnaire drift; both can fail useful user reasoning, for different reasons. The
Question Value Gate permits grounded exploration without a strict decision blocker.

## Exploration pressure and visible navigation

See [navigation-scoring.md](navigation-scoring.md) for D17, grounded adjacent moves,
map topology, and origin-relative distance. D17 preserves the existing pause and
diminishing-return boundaries. No raw question-frequency metric establishes compliance.

## Thought-navigation regressions

[Acceptance fixtures](regressions/thought-navigation.md) define the synthetic open-source
and X3 regressions, positive contrasts, and comparison protocol. Nine generated probes
cover D18 trajectory retention, D19 meaningful navigation, and D20 consecutive assistant
dimensions. They do not establish that a candidate prompt outperforms a previous version
until both are actually run. Seeded histories are evaluator-authored, not model results.

## Exploratory movement

See [movement-scoring.md](movement-scoring.md) for deeper/sideways/across movement,
open connections after minimal confirmation, and user-led depth. D20 constrains
assistant answer construction, not all consecutive exploratory connections.

## Move selection

See [selection-scoring.md](selection-scoring.md) for four probes of connections,
contrasts, evidence checks, and conditional consequences. Judge the reasoning change,
not label diversity or the absence of questions.

## Emergent map and agency

[Emergent-map scoring](emergent-map-scoring.md) covers discovery without advance
checklists, meaningful cross-links, rejected paths, and evidence that must not be withheld
for dramatic effect. The GM metaphor guides mechanics, not routine roleplay.

## Evidence continuation and starvation

[Continuation scoring](continuation-scoring.md) tests concrete evidence openings, lightweight
reveals, authored permission-loop recovery, and facts-only boundaries. It clarifies which
inputs qualify for the low-gain deadline without treating empty confirmations as progress.

## Decision-coach collapse

[Frame-escape scoring](frame-escape-scoring.md) covers five decision-shaped openings
with supported alternative destinations. It tests concrete live affordances, current-turn
retrieval, and user-owned reframing without requiring a new category in every session.

## Navigation-first Thought Window

[Landscape scoring](landscape-scoring.md) distinguishes trail, current location, and dot-marked
visible terrain. It supersedes old distance/frontier display expectations; evidence provenance
remains required in prose and wherever materially relevant on the map.

## Thought graph and branch state

[Graph scoring](graph-scoring.md) covers eight synthetic sessions and D21–D24. The graph
replaces the ledger/trajectory/frontier state duplication; provenance is node/edge metadata.
The minimap remains one compact display. Reconnect reveals changed grounds and does not
silently reopen a closed path. No graph database, persistence layer, or model runner was added.

## Weak versus substantive adoption

[Adoption scoring](adoption-scoring.md) defines three paired seeded simulations for Japan,
X3, and job/product reasoning. It tests cumulative assistant momentum; adoption metadata informs judgment rather than
gating particular inferences or graph operations. No new invariant or subsystem is introduced.
