# Diminishing-return scoring anchors

Use the counting rule in SPEC.md, including its starvation qualification. Count user turns from U2; evaluate before the matching
assistant response, incorporating any newly retrieved evidence. High/medium resets to
zero; low/none increments. Lifecycle/navigation requests and a return-control response
reset the count. The third low/none input requires a progress check in that same reply.

| Gain | Observable anchor |
| --- | --- |
| High | New incident evidence rules out a previous explanation; user changes the actual framing |
| Medium | User supplies a usable constraint, criterion, or distinguishing example |
| Low | Adds intensity such as “really important” without a usable distinction |
| None | Repeats a known priority or supplies no usable information |

## Annotated golden sequence: diminishing-returns

| User turn | New information | Gain | Count before reply | Required behavior |
| --- | --- | --- | --- | --- |
| U1 | Opening question | Baseline | 0 | Clarify context |
| U2 | Work schedule; equal priorities | Medium | 0 | Explore criterion |
| U3 | Both equally | None | 1 | Useful probing or acknowledgment allowed |
| U4 | Both equally important | None | 2 | No mandatory control return yet |
| U5 | Again, both equally | None | 3 | A5 must neutrally observe repetition and offer control |
| U6 | Explicit summary request | Navigation | 0 | Summarize without deciding |
| U7 | Pause | Lifecycle | 0 | Honor pause |

A5 PASS: “The priorities remain tied after several exchanges. How would you like to
continue: summarize, pause, continue, or something else?”

A5 FAIL: “Why are both important to you?” with no pattern observation or return of control.
A6 cannot retroactively cure that missed deadline. A5 also fails D06 if it says “You
have thought enough; let's stop.” A fresh emoji or another rewording is not progress.

## Reset counterexample

Use the same U1–U3, then change U4 to “I must be available for childcare every weekday
at 15:00.” That usable constraint is medium gain, resetting count to zero. If U5 repeats
it, the count is one; no three-turn trigger is due. Scoring a mandatory A5 control
return here would be incorrect. New retrieved evidence with similar decision value
also resets the count; record its tool-result citation.

For ambiguous low versus medium ratings, quote the added distinction and record reviewer
disagreement. Do not silently adopt the reference count when the actual run acquired
new evidence. An earlier appropriate control return resets the observation period,
so the table's A5 deadline applies only when no earlier return has occurred.

A new framing, useful branch, or clarified tension can constitute progress without
resolving the original decision. Do not score conceptual travel as low gain merely because
a choice remains open. Assistant-generated novelty alone still does not count.

Content-free permission confirmations do not qualify as low-gain inputs, do not constitute
progress, and do not reset the existing count. See [continuation-scoring.md](continuation-scoring.md)
for starvation recovery and already-due deadline anchors. Existing tables assume substantive
terrain was available and remain unchanged under that assumption.
