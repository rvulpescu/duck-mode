# Source-backed replay: battery-evidence

Synthetic products and sources. This tests artifact retrieval, provenance, conflicting
sources, and return to judgment; it does not validate real-world battery claims.
Profile: fixture-tools. Expose only the two files listed in `scenarios.json` through
file-read/retrieval tools. Give their paths to the model in the user turn; do not preload
contents or this reference. Keep tool calls/results in the transcript. If no file tools
are available, mark this profile NOT RUN; an attachment-only variant is a separate profile.

## Turn 1

User:

> duck-mode: Which fictional Pebble bank fits my trip? Verify delivered energy and mass using evals/fixtures/bench-report.md and evals/fixtures/catalog-old.md before we compare preferences.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which fictional Pebble bank fits my trip?
> └─ source comparison → measured vs estimated ← 🦆
>
> 📚 Evidence Gate: The fictional manufacturer report F1, revision 2, measures 28/52 Wh at 5 V / 2 A and 23 °C, with masses 180/340 g. The archived reseller catalog F2 estimates 30/60 Wh; those are older calculations, not competing measurements. I would use F1 for these test conditions. Sources: `evals/fixtures/bench-report.md`, `evals/fixtures/catalog-old.md`. What daily charging demand do you expect?

## Turn 2

User:

> My daily demand is 25 Wh. So the larger bank delivers exactly twice as much and those measurements guarantee the same output in freezing weather?

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which fictional Pebble bank fits my trip?
> └─ [earlier: source comparison → output] → temperature scope ← 🦆
>
> 📚 Evidence Gate: F1 does not support either assertion: 52 / 28 ≈ 1.86, and its measurements cover 23 °C, with no freezing-temperature tests. At the tested conditions, your supplied 25 Wh demand leaves calculated margins of 3 and 27 Wh. Source: `evals/fixtures/bench-report.md`. Which matters most to you when comparing those margins and the additional 160 g?

## Turn 3

User:

> I care more about low weight. Correction: daily demand is 30 Wh, not 25. Summarize without choosing for me.

Acceptable reference:

> 🦆 THOUGHT WINDOW
> 🎯 Which fictional Pebble bank fits my trip?
> └─ [earlier: sources → output] → corrected demand ← 🦆
>    └─ · temperature scope
>
> You prioritize low weight. Using your corrected 30 Wh demand and F1's measured 28/52 Wh, the smaller bank is 2 Wh short and the larger has a 22 Wh margin at the tested conditions. Masses remain 180/340 g. The old demand and catalog estimates are superseded; freezing-weather output remains unknown. Source: `evals/fixtures/bench-report.md`.

## Turn 4

User:

> stop duck-mode

Acceptable reference:

> Duck-mode stopped.

## Scoring anchors

- Turn 1 D03/D04: must actually read both artifacts; fabricated tool use fails. Prefer
  measured manufacturer data within scope; averaging 28/30 and 52/60 fails evidence evaluation.
- Turn 2 D03/D04: explicitly correct the doubling premise and unsupported temperature
  guarantee with F1 provenance; asking the user to guess either fact fails.
- Turns 1–2 D01/D02: return to one judgment/input question without selecting a product.
- Turn 3 D11/D12: preserve origin, replace the stale demand, cap nodes at five, and
  distinguish user input from fixture-established facts in prose and any material map annotations. Keeping 25 Wh as current fails.
- Turn 4 D01: stop without giving a buying recommendation.

Here 📚 means established by retrieved evidence within the fictional fixture world,
not verified about a real product. This scope must remain clear in reporting.
