# TODOs — PIPELINE S3 (Rubrics) — Tasks/43_6a62ccaf5853030245ac9d53

Universe: **starpm** (V4 framework)
Created as first action per S3 runbook Step 0 (v11 E1 operator-discipline gate).

| # | Step | Status |
|---|---|---|
| 0 | Create `_aux/Todos_s3.md` (this file) | completed |
| 0b | Run `phase_ready.py --phase s3` gate | completed |
| 1 | Create `_aux/Reads_s3.md`, log every spec/reference doc read (v11 E2) | completed |
| 2 | Read `5_Prompt.txt` in full | completed |
| 3 | Read `6_Oracle_Events.txt` (28 OEs) in full | completed |
| 4 | Read `_aux/Hardness_Plan.md` — enumerate every lever | completed |
| 5 | Read `_aux/Verification_s2.md` + `Verification_audit_oe.md` for OE-rubric consistency | completed |
| 6 | Read `Reference/Rubric_Format.md` | completed |
| 7 | Read `Docs_starpm/2_Rubrics_V3_Guidelines.md` | completed |
| 8 | Read `Docs_starpm/12_Always_Failing_Rubrics.md` | completed |
| 9 | Read `Evals_starpm/3_Rubrics_Eval.md` (full, both pages) | completed |
| 10 | Read `Docs_starpm/7_QC_Spec_Doc1.json` Rubric dimension (5 sub-dims) | completed |
| 11 | Read all four `QC_Tasks/V4_Tasks/QC_Passed/*/7_Rubrics.json` in full | completed |
| 12 | Read `Reference/Strict_Convention_Inventory.json` | completed |
| 13 | Read `StarPM_Base_Universe/7_Server_Tools_Details.json` (verify every cited tool + param) | completed |
| 14 | Ground every atom against `_aux/Fact_Ledger.json` + `_aux/Universe_Split/` | completed |
| 15 | Build OE write-action inventory → 1.1 per write, 1.2 where content specified | completed |
| 16 | Build prompt tell-me inventory → 2.1 per user-facing fact | completed |
| 17 | Three-condition test on Process candidates → **zero process** (affirmed by Council B B2d + AUDIT) | completed |
| 18 | Draft `7_Rubrics.json` in FLAT schema | completed |
| 19 | Run `validate.py --phase rubrics`; fix every fail | completed — **PASS, 0 fails** |
| 20 | Council A — Grounding | completed — **GO** (r1, r2, r3, r4) |
| 21 | Council B — Adversarial QC | r1 **BLOCK** → r2 **GO** → r3 **BLOCK** → r4 **GO** |
| 22 | Loop: apply fixes, re-run validator + BOTH councils until clean | completed |
| 23 | AUDIT (strict veteran, `--phase rubrics`) → `PASS (STRICT)` required | r1 REVISE → r2 REVISE → r3 REVISE → **PASS (STRICT)** (3 of 3 cap rounds used) |
| 24 | Write `_aux/Reasoning/Rubric_Coverage_Matrix.md` | completed — rewritten for the final 25-rubric set |
| 25 | Write `_aux/Verification_s3.md` (v16 cross-source verification) | completed — `check_verification.py --phase s3` OK |
| 26 | Confirm exit criteria; append `Tasks/_meta/Audit_Log.md`; STOP gate | completed |

## Supporting gates run
| Gate | Result |
|---|---|
| `test_regression_anchors.py` (AUDIT Lens 8) | **62/62 PASS** |
| `calc_similarity.py` | max composite **27.4** — all < 40 ceiling |
| `phase_ready.py --phase s3` | OK; eval hashes 18/18 match pinned baseline |

## Revision history
- **r1 → r2** (Council B): rubric[8] evidence dropped the `SyncToken` clause (catalog marks it optional — evidence was stricter than criterion); rubric[15] gained the Ready-status Selection-Logic discriminator (old wording let an agent updating only the stale In Progress row pass). Council A minor: rubric[13] evidence dropped the credit-memo clause. Accuracy fix: three titles re-attributed `$1,140`/`$190`/`$1,622` from "the summary she received" to "originally billed" (OE 7 establishes the belief email states no dollar figures).
- **r2 → r3** (AUDIT REVISE, 5 findings): channel closed set widened to four adding `#maintenance` (MAJOR lock-in — the stale 4C row OE 4 forces the agent to read says progress is coordinated there); second negative guard deleted and folded into rubric[9] evidence (26 → 25 rubrics); rubric[13] wrapped Task1-style; all 12 possessive titles converted to `The Agent + verb + context` (QC spec lists the possessive as its Non-Fail 3/4 exemplar); anti-approximation guidance added to rubric[0] + rubric[5] evidence.

## Open items — all closed
- Council A r3 MINOR 1 (rubric[9] no-fourth-line guard evidence-only): **declined, and the decline upheld then vindicated.** Council A withdrew it on its own evidence — `TotalAmt == sum(Line.Amount)` holds 385/385 across all QuickBooks invoices/bills/credit_memos with zero counterexamples, so a four-line invoice declaring $1,812 is unrepresentable and the guard is a genuine entailment. The proposed edit would have added an independently-failable second claim; the composition alternative would have duplicated rubrics[10]-[12].
- Council B r4 N13 (rubric[22] evidence closing "None of these choices is penalised" readable as exhaustive): **not applied.** Non-failing; the criterion text grades "a StarPM team channel" and evidence cannot be stricter than the criterion it supports. Left untouched deliberately so the shipped artifact is byte-identical to the one AUDIT stamped — this phase produced three regressions from well-intentioned post-review edits.

## Carry-forward to FINAL / S4 (not S3 blockers)
- **Density, adjudicated:** AUDIT's initial ~37 blended Opus figure was **withdrawn** — it conceded to Council B on repo evidence (Task 39 Opus 43.5 at 0/6; Task 41 Opus 48.0 at 0/6 on the identical L2 vendor-linked-AP-bill flagship; minimum across all recorded 0%-pass sets 41.5; a stumped agent keeps searching rather than skipping the AP leg). **Record: Opus ~42 (32-48) PASS knife-edge; Gemini ~32 THIN**, accepted under the plan's documented `## THIN density acceptance`. AUDIT's r1-F3 governance finding is withdrawn as a defect and retained only as a prudential watch-item. S4 re-open triggers per model: **Gemini < 24, Opus < 32**; remedy is a grounded fifth write or an added OE cross-service read, **not** rubric padding.
- **Instrumentation gaps (tooling, compensated by hand — full detail in `Verification_s3.md`):** Fact_Ledger indexes no QuickBooks vendor/customer names, so four entity-name atoms were ungated by any automated check; `validate.py` X2 is `$`-anchored while V4 OEs write amounts unprefixed, self-disabling on every StarPM task; the Slack service-metadata check is bypassed rather than satisfied by rubric[22]; density thresholds are inconsistent across four files (the V3-family 50/40 wording in `S3.md` and `AUDIT.md` is a live trap on StarPM tasks).
- **Pipeline item N15** (endorsed independently by AUDIT and Council B): add a `gate_on_write` assertion for every negative or `keeps`-phrased criterion plus a criterion/evidence polarity check, since exhaustive `fails only if …` lists silently make a criterion vacuously true; and on any wording change, re-run every open note whose discharge depended on that wording.
- AUDIT F5 / Council B: lever L1 (latching) is now live and graded via rubric[14]-[16], but `Hardness_Plan.md` still labels it "reserve". L1 is now spent as a margin-deepener.
- Council B: delivered service breadth is **5**, not the 6 the Hardness Plan projects (nothing forces Linear or HubSpot).
- Council B N7: pre-upload dry-run of the four writes whose evidence requires "returned a success response" (rubrics 8, 14, 17, 22).
- Council B: a stale-row latch fails rubrics 14, 15 and 16 together — a genuine Bucket 3 model failure, not a bundled-rubric artifact. Do not misread at the All-Failing review.
- Council A: the owner email grades four of OE 26's five body elements (defensible under the prompt's "short note"); `2026-519` appears in no title (self-containment holds via a unique amount+scope+vendor triple).
- OE-prose nit for FINAL only (do NOT re-run S2): OE 26/27 attribute dollar figures to the summary email, which OE 7 correctly records as carrying none.
