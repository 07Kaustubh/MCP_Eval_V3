# S4 Bucket 1 fixes (Task 36)

**Count: 0 rubrics classified as Bucket 1 (rubric invalid).**

All 12 distinct failing rubrics ground on shipped OE + universe values and cite verifiable trajectory actions. See `S4_verdict.md` for the classification detail and `S4_AF_justifications.md` for the per-rubric writeup.

## Non-blocking observation (not a fix, not a Bucket 1)

R7 and R8 ("Slack reply on Mina's audit thread references [Marcus content] / [Simone content]") both fail on 4/6 runs solely because R6 (Slack location correctness) failed on those same 4 runs. Content was in the payload on all 4 wrong-thread runs; the failure is entirely the location gate.

This is defensible as written — the semantic goal is "close the audit by posting the recovery status on the audit thread", and location + content are both load-bearing for that goal. But if a future task needs cleaner AF-scoring math, R7 and R8 could be split into location-agnostic "the Slack post payload references [X]" rubrics with R6 alone covering location.

No action required for Task 36.
