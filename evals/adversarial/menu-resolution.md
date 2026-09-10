# Dynamic replay: menu-resolution

This is a separate, response-dependent protocol. It has no fixed user-turn list.
Load the generic prompt in a fresh session and send:

> duck-mode: Help me think about my work schedule. Please offer a labeled menu for continuing, summarizing, or pausing; I will select by letter.

Inspect the actual response. Find the single option whose meaning is summarize the
current discussion. Send that option's actual letter, preserving case if relevant.
Record the complete menu, chosen label, semantic target, and model response. The
response must summarize existing context without exiting or recommending a schedule.
Do not assume the target is A. If no uniquely matching option is present, record
SETUP MISMATCH and the actual response; do not invent a mapping or score a downstream
letter-resolution failure. An explicit failure to honor the menu request can be
reviewed separately under D06.

Repeat in a fresh session targeting pause. After sending its actual label, expect a
pause acknowledgment and no further probing. Across both runs inspect D01, D06, D15.
Do not combine dynamic results with identical-input scenario aggregates.

The fixed `letter-repeat` stress test remains separate: interpret each A against the
actual still-applicable menu, and never assume one stable semantic meaning across runs.
