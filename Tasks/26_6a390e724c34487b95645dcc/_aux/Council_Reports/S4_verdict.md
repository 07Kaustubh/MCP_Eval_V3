# Verifier Fails — S4 verdict — Task 26_6a390e724c34487b95645dcc

**Date:** 2026-06-22
**Verdict:** SHIP. Density 79.8 avg tool calls (well over 40 floor), pass@1 = 0/6 (well under the 40% bar). All 14 always-failing rubrics classified as legitimate model failures (Bucket 3) requiring AF justifications. Zero Bucket 1 (rubric invalid). Zero Bucket 2 (judge error).

## Trajectory measurements

- Runs evaluated: 6 / 6
- Avg total tool calls: **79.8** (range 67–98). Avg MCP-only: 65.5. Density gate PASS (40+).
- pass@1: **0.0** (0/6 runs passed all rubrics). Difficulty gate PASS (≤40%).
- Per-run rubrics passed: R1 8/23, R2 2/23, R3 3/23, R4 4/23, R5 8/23, R6 8/23.

## Run matrix (23 rubrics × 6 runs)

| # | id prefix | rubric (short) | R1 | R2 | R3 | R4 | R5 | R6 | pass |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 7c8e5a12 | posts closed-period SALT JE in northstar_legal_FP-2025-12 | F | F | F | F | F | F | 0/6 |
| 2 | 8d9f6b23 | JE binds to email_scen_068 via late_post_authorization_id | F | F | F | F | F | F | 0/6 |
| 3 | 9e0a7c34 | vault upload kind=memo, restricted, IRS_TAX_7Y, related=journal_entry | F | F | F | F | F | F | 0/6 |
| 4 | af1b8d45 | memo body: $4,820.30 + 230000/103000 trace | F | F | F | F | F | F | 0/6 |
| 5 | b02c9e56 | memo body: William's email + posted JE id+entry_number | F | F | F | F | F | F | 0/6 |
| 6 | c13d0f67 | email Hannah + CC William (or reply on email_scen_068) | P | F | F | P | P | P | 4/6 |
| 7 | d24e1078 | email confirms $4,820.30 late-post is posted | F | F | F | F | F | F | 0/6 |
| 8 | 7e8d9c2b | email references posted JE id and entry_number | F | F | F | F | F | F | 0/6 |
| 9 | e35f2189 | email references memo + restricted + IRS_TAX_7Y | P | F | F | F | P | P | 3/6 |
| 10 | 8f9e0d3c | email confirms package can move + e-file unblocked | P | F | F | F | P | F | 2/6 |
| 11 | f46a328a | updates exc_652c to reclassification (not dismissal) | F | F | F | F | F | F | 0/6 |
| 12 | a57b439b | deletes reminder_scen_012_orphan_exception_0000 | F | F | F | F | F | P | 1/6 |
| 13 | b68c54ac | deletes reminder_scen_001_orphan_exception_0000 | P | F | P | P | P | P | 5/6 |
| 14 | c79d65bd | adds Linear follow-up comment on polling-bug tracker | F | F | F | F | F | F | 0/6 |
| 15 | d8ae76ce | Linear comment body: occurrence + Mar auth + reminder disposal | F | F | F | F | F | F | 0/6 |
| 16 | e9bf87df | posts status in channel C006 | P | P | P | P | P | P | 6/6 |
| 17 | 0a008e90 | C006 SALT close-out cluster (posted + memo + package cleared) | F | F | F | F | F | F | 0/6 |
| 18 | 1b119fa1 | C006 exception cluster (652c reclass + 151b dismissed + polling) | F | F | F | F | F | F | 0/6 |
| 19 | 2c220ab2 | identifies $4,820.30 supported by GL (230000 + 103000 trace) | P | F | F | F | P | P | 3/6 |
| 20 | 3d331bc3 | identifies period closed + William's email_scen_068 as authorization | P | P | F | F | P | P | 4/6 |
| 21 | 4e442cd4 | identifies doc_8f821bbad10c4eb4 as title-only placeholder | F | F | F | F | F | F | 0/6 |
| 22 | 5f553de5 | identifies documented disposition for exc_652c is reclassification | F | F | F | F | F | F | 0/6 |
| 23 | 60664ef6 | identifies exc_151b closed + March 16 partner auth chain | P | F | P | P | P | P | 5/6 |

**Always-failing (0/6) rubrics:** 14 of 23 (61%). All classified Bucket 3.

## Classifications

| Bucket | Count | Where |
|---|---|---|
| Bucket 1 — Rubric Invalid | **0** | (none) |
| Bucket 2 — Judge Error | **0** | (none — judge calls accurate under strict reading) |
| Bucket 3 — Legitimate Model Failure (AF) | **14** | see S4_AF_justifications.md |

The 14 AF rubrics in Bucket 3 (by id prefix):
- 7c8e5a12 — posts closed-period SALT JE
- 8d9f6b23 — JE binds to email_scen_068 as late_post_authorization_id
- 9e0a7c34 — vault memo upload with correct kind / classification / retention / related_resource_type
- af1b8d45 — memo body contains the $4,820.30 figure and the GL trace across 230000 and 103000
- b02c9e56 — memo body references William's email and the posted JE id + entry_number
- d24e1078 — email confirms the $4,820.30 late-post is posted
- 7e8d9c2b — email references the posted JE id and entry_number
- f46a328a — exception update records reclassification disposition
- c79d65bd — Linear follow-up comment on the polling-bug tracker (create-then-comment fallback)
- d8ae76ce — Linear comment body references this week's occurrence + March auth + reminder disposal
- 0a008e90 — C006 SALT close-out cluster
- 1b119fa1 — C006 exception cluster
- 4e442cd4 — identifies the doc_8f821bbad10c4eb4 forward-looking stub
- 5f553de5 — identifies documented disposition for exc_652c is reclassification

## Partial-fail observations (not AF, no justification required)

- **a57b439b (delete reminder_scen_012):** 1/6 pass. Only Run 6 deleted the correct reminder; the other five deleted only scen_001 (or scen_013 in Run 2). Indicates light disambiguation effort across the two stale-tickler IDs.
- **b68c54ac (delete reminder_scen_001):** 5/6 pass. Run 2 deleted the wrong reminder (scen_013) because it worked on the wrong underlying exception entirely.
- **2c220ab2 (identifies $4,820.30 supported by GL):** 3/6 pass. Runs 2, 3, 4 concluded the records did NOT support the figure (interpreted "zero December movement on 230000" as inability to verify rather than as evidence the accrual must be booked).
- **3d331bc3 (period closed + William's email as authorization):** 4/6 pass. Runs 3 and 4 rejected William's email as valid authorization on persona-seniority grounds, missing that the email body explicitly states "treat this reply as my authorization of record".
- **8f9e0d3c (email confirms package can move + e-file unblocked):** 2/6 pass. The e-file path read as "blocked pending accrual" in three runs, "OK to circulate" in two.
- **e35f2189 (email references memo + classification + retention):** 3/6 pass. Cascades from the memo-upload step: runs that filed no memo could not reference one.
- **60664ef6 (identifies exc_151b closed + March auth chain):** 5/6 pass. Run 2 worked on the wrong exception (exc_1ec70e0d938b4f) entirely.
- **c13d0f67 (email Hannah + CC William):** 4/6 pass. Run 2 used messaging_send_message_to_conversation instead of email; Run 3 sent no email at all.

## Hardness Plan calibration

Hardness predictions (from `_aux/Hardness_Plan.md`) vs actuals:

| # | Prediction | Predicted | Actual | Verdict |
|---|---|---|---|---|
| 1 | Agent fails to stage closed-period SALT JE — L25 existing-output anchor via doc_8f821bbad10c4eb4 | HIGH | 0/6 stage success across both R1 (JE) and R21 (stub recognition). doc_8f821bbad10c4eb4 was never even discovered in any run. | CONFIRMED — mechanism partially inverted: agents wanted to post but failed the late_post_authorization_id parameter contract (PERIOD_CLOSED tool errors in 3/6) rather than refusing entirely. The "Signed/E-Filed" stub anchor fired hardest as a recognition gap, not as a write-refusal anchor. |
| 2 | Agent confirms dismissal of exc_652c instead of reclassification — L9 + L27 | HIGH | 0/6 on R11 (resolution disposition) and R22 (override recognition). | CONFIRMED — strongest single-mechanism stump on this task. |
| 3 | Agent uses $4,820.30 verbatim without GL verification — L13 + L11 | MED | All runs quoted $4,820.30 (figure not invented), but only 3/6 confirmed support via the 230000 + 103000 trace; 3/6 concluded the records did NOT support the figure. | CONFIRMED with mechanism refinement — the lever fires on verification depth, not on figure quoting. |
| 4 | Agent treats orphan reminder for exc_151b as live — L13 + L4 search-result-cap | MED | R23 (closed + auth chain recognition) 5/6 pass; R13 (reminder deletion) 5/6 pass. | OVER-PREDICTED — agents found the scen_001 authorization chain via direct grep on the exception id; the search-result-cap eviction lever did not fire on this surface. |

**Hit rate:** 2/4 clean (Pred 1, Pred 2 confirmed). Pred 3 confirmed with mechanism refinement. Pred 4 over-predicted.

**Surprises (failed, did not predict):**
- **R3 (memo upload kind):** 0/6. Agents who attempted the upload picked kind 'journal_entry_support' over the convention's 'memo' (Runs 1, 5, 6). NEW pattern: tool-enum specificity drift — when an enum variant closely matches the noun in the prompt ("support memo" → 'journal_entry_support'), agents pick the more-specific variant over the canonical generic ('memo') specified by convention. Cascade to R4, R5 (memo content rubrics tied to a memo that was filed under the wrong kind).
- **R2 (JE binding via late_post_authorization_id):** 0/6. Agents referenced William's email in the business_justification free-text rather than the structured parameter. NEW pattern: free-text shelter — agents satisfy a binding requirement in narrative text rather than as the structured parameter, even when the parameter exists in the tool spec. The PERIOD_CLOSED tool error in three runs confirms the parameter was the gate. Cascades to R1.
- **R14 + R15 (Linear comment):** 0/6. The one run that opened a new issue (Run 5, CAO-3116) baked the follow-up content into the issue description rather than calling linear_create_comment. NEW pattern: two-step write reduction — agents collapse a create-issue + create-comment workflow into a single create call.

**Lessons for next task lever catalog:** see `Tasks/_meta/Hardness_Patterns_Log.md` for the L16/L17/L18 additions.

## Action items

- **Ship the 14 AF justifications back to the platform** (`_aux/Council_Reports/S4_AF_justifications.md`). All clean under `check_justification.py`.
- **No rubric fixes needed** (zero Bucket 1).
- **No judge appeals needed** (zero Bucket 2).
- **Append calibration lessons** to `Tasks/_meta/Stump_Hypotheses.md` and `Tasks/_meta/Hardness_Patterns_Log.md`.
- **Task is shippable as-is.** Density and difficulty both pass with margin. The 14 AF rubrics are the intended stump surface for this task.
