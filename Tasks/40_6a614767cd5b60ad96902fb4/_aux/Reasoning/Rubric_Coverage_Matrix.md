# Rubric Coverage Matrix — S3 — Tasks/40_6a614767cd5b60ad96902fb4 (StarPM V4)

**AUDIT verdict:** PASS (STRICT) (`_aux/Council_Reports/AUDIT_rubrics.md`) · **Council A:** GO · **Council B:** GO (5/5) · **Validator:** exit 0 · **Regression anchors:** 62/62 · **Timestamp:** 2026-07-23

16 Outcome rubrics, 0 Process. Every prompt ask maps forward to at least one rubric; every rubric maps back to a prompt ask (no gap, no surplus). Rubric indices are 0-based against `7_Rubrics.json`.

## Forward map (prompt sentence -> OE step(s) -> rubric index)

| Prompt sentence | Intent | OE step(s) | Rubric(s) |
|---|---|---|---|
| L1 "we are past the holdup ... time to get that unit back in shape and ready to re-rent" | Stump / wrong-belief guard (account is NOT cleared; turn must NOT advance) | OE 1-13 discovery; OE 14 | [1] status stays Scheduled; [4]/[8] account in active eviction (Slack + email) rebut "nonpayment cleared" |
| L3 "pull up the current make-ready record on Unit 14 and confirm where it genuinely stands ... do not want it marked further along ... keep everything tied to Tanya Mitchell's unit" | Correct-record update, no advance, hold note | OE 2 (disambiguate), OE 3 (hold from notes), OE 14 (update) | [0] correct record recc83c05d889b354/reca8230a8fd9ff51, bar Rio Bend rec94e86a3007dd5e; [1] status stays Scheduled; [2] notes document hold |
| L5 "team current on where her account really landed ... post a clean status in the make-ready channel" | Slack account status | OE 4-9 (account discovery), OE 15 (post) | [3] post to #make-ready; [4] account active eviction / plan breached / not-on-plan; [5] turn held |
| L7 "draft me an email to Brooke that walks through where Unit 14 sits end to end, the account, the turn, and anything still open on it ... Do not send it" | Draft-only owner-review briefing | OE 13 (contacts), OE 16 (draft), OE 19 (content facts) | [6] draft to brooke.phillips@starpm.com, no send; [7] disambiguation Sunset Ridge not Rio Bend; [8] delinquent / active eviction (not resolved by invoice 7214); [9] $2,132.00 arrears on QR-2026-0441; [10] turn held; [11] EVF-2026-014 owner-approved but still in JP coordination; [12] approved ESA fair-housing |
| L9 "set a reminder on my Google Calendar to come back to Unit 14 early next week, and update the ticket we have open on it ... I will take it from there" | Calendar reminder + ticket comment | OE 17 (calendar), OE 18 (OPS-32 comment) | [13] reminder 2026-07-06/07; [14] comment on OPS-32 (not a new issue); [15] comment reflects hold |

## Reverse map (rubric -> prompt ask) — no surplus

Every rubric [0]-[15] ties to a prompt ask in the table above; no rubric goes beyond the prompt. L1's "before I escalate anything ... I will take it from there" is the persona's own deferred action, correctly NOT rubric-covered (the validator `escalat` / `forwar` write-verb warns are benign false-positives, adjudicated by Council B + AUDIT).

## Hardness lever coverage (Council B-B4 / AUDIT LENS 3)

| Lever | Rubric(s) whose pass/fail depends on traversing it |
|---|---|
| Cross-property Unit 14 ambiguity (Sunset Ridge vs Rio Bend decoy) | [0] (bar rec94e86a3007dd5e), [7] (email names Sunset Ridge not Rio Bend) |
| Hold from NOTES not selSched status / stale fldMoveOut 2026-05-02 | [1] (status stays Scheduled), [2] (hold note) |
| Invoice 7214 zero-balance decoy | [8] (not resolved by 7214 zero balance) |
| QB bill QR-2026-0441 vendor-label decoy (Alamo HVAC) | [9] (keyed on $2,132.00 + Tanya, not the vendor label) |
| Approved-ESA-on-record fair-housing | [12] |
| Payment-plan-breach supersedes earlier commitment | [4], [8] |

All 6 levers covered; AUDIT LENS 3 traced each end-to-end (prompt -> OE -> rubric -> atom). No HARDNESS_REGRESSION.

## Density (Council B-B3 / AUDIT LENS 4)

StarPM 40+ per-model bar: Opus ~41 (range 38-45) PASS; Gemini ~44 (range 40-48) PASS. Both far above the 15 floor. The rubric set is density-positive: content rubrics [8]/[9]/[11]/[12] force distinct cross-service reads and the 1.1 rubrics enforce all 5 writes.
