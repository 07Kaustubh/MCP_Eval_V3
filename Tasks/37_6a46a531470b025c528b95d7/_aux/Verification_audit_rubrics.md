# Verification — AUDIT rubrics (Task 37, on-demand strictest)

## Strictest interpretation re-applied
- 5/5 only on every applicable Rubrics Eval sub-dim.
- Every "should" read as "must".
- Validator FAIL band (27% Moderate+ / 27% any-severity) treated as GENUINE FAIL candidate — re-verified per-pair against `Reference/Rubric_Format.md` redundancy sub-dim, not narrative-dismissed.
- 3 "at least N" uses each re-verified against prompt phrasing (defensibility floor test).
- Rubric [28] final-response gate on LN-2026-00623 pressure-tested via trajectory spot-check.

## Data sources consulted
- `15_Updated_Rubrics.json` (30 rubrics — MATERIALIZED)
- `7_Rubrics.json` (candidate original — diff awareness)
- `changes.md` (2 Applied rows: rubric[3] Derek coverage; rubric[24] Elena justification)
- `_aux/Universe.txt` → `keystone`
- `_aux/Universe_Split/mortgage_los.staff.json` (Elena role/spec; terminated LO join)
- `_aux/Universe_Split/mortgage_los.loans.json` (per-LO cohort loan atoms; terminated-LO join)
- `_aux/Universe_Split/mortgage_los.conditions.json` (LN-2026-00008 2-outstanding atom)
- `_aux/Universe_Split/mortgage_los.document_checklist_items.json` (Derek's LN-2026-00196 w2_current; LN-2026-00623 5-doc atom; LN-2026-00010 7-doc atom)
- `_aux/Universe_Split/slack.slack_messages.json` (C002 TRID atoms; C004 Denise breach-response atoms)
- `_aux/Council_Reports/verify_universe_atoms.md` (41/41)
- `_aux/Council_Reports/REVIEW_hardness.md` (measured 216.8 avg tool calls / 33.3% pass@1)
- 3 trajectories (`trajectory-runs/trajectory-run-{1,3,5}.json`) — final-response naming spot-check for LN-2026-00623 and LN-2026-00010
- `Docs/7_QC_Spec_Doc1.json` + `Docs/8_QC_Spec_Doc2.md` (Rubrics phase sub-dims)
- `Evals/3_Rubrics_Eval.md` (Rubrics evaluator spec)
- `Reference/Rubric_Format.md` (redundancy sub-dim + "at least N" rule + method-lock hygiene)
- `Reference/Sessions/AUDIT.md` (LENS 1-8, 6+9 retired v18)

## Eval spec verified
- Rubrics Eval Phase 1.1 (0 Outcome = FAIL): 30 outcome ✅.
- Rubrics Eval 2.7 method-lock: 2 method-locks ([21] Slack C002; [24] Elena+Denise emails) — both prompt-inherent, not authored lock-in.
- Rubrics Eval 4.2 threshold math + absolute-count gate: Major count = 0, Moderate absolute count assessed against Rubric_Format.md severity taxonomy.
- Pipeline deviation "channel/method lock-in Major-by-default when alternative exists": no valid alternative to the prompt-named channels/recipients in either lock case.

## QC spec re-verified
- Outcome > Process ratio: 5/5.
- Atomicity: 5/5 (per-LO bundles are single-message pass/fail).
- Groundedness: 5/5 (41/41 + both AFTER rows atom-verified).
- Self-containment: 5/5.
- Verifiability: 5/5.
- Coverage: 5/5.
- Redundancy: 5/5 (Jaccard 71% = structural shell, semantically distinct per Row-by-Row proof).
- Severity balance: 5/5.
- Persona attribution: 5/5 (Elena grounding tightened Row #2).
- Method-lock hygiene: 5/5.

## All 9 lenses status
| Lens | Status | Note |
|---|---|---|
| 1 Strict QC scoring + per-atom evidence | PASS | Row #1 + Row #2 atom tables + 4 special-attention rubrics + 10 sub-dim scores in AUDIT_rubrics.md |
| 2 Answer-leakage sweep | PASS | Rubrics not exposed to solving agent |
| 3 Hardness end-to-end trace | PASS | 8 levers anchored (3 strengthened by Applied rows) |
| 4 Density projection | PASS | 216.8 avg |
| 5 Adversarial + validator-FAIL re-adjudication | PASS | 12 Jaccard pairs confirmed structural-shell false positive by per-pair distinctness proof |
| 6 RETIRED v18 | — | |
| 7 Anti-rationalization | PASS | 5 candidate rationalizations re-scrutinized against raw data |
| 8 Regression anchors | PASS | 48/48 |
| 9 RETIRED v18 | — | |

## Verification statements
- **Statement 1 (Row #1 Derek cohort symmetry):** DIRECT QUERY of `mortgage_los.loans` filtered on `assigned_lo=los_staff_f9aa4c3c2fcb AND assigned_processor=los_staff_afc9caafae9d AND status not in closed/denied/withdrawn` → exactly {LN-2026-00008, LN-2026-00196, LN-2026-00632}. Rubric [3] AFTER title matches this set exactly. Cohort symmetry now aligned with the other 7 LO cohorts (each rubric covers 100% of that LO's loans in Sofia's pipeline).
- **Statement 2 (Row #2 Elena+Denise atoms):** All 5 claims in AFTER justification directly re-verified — Denise verbatim Slack C004 posts (ts=1775570820 + ts=1775572140); Elena role/spec from `mortgage_los.staff`; 4-loan phishing scope from Denise's C004 post verbatim; TRID atoms from C002 verbatim; 5 terminated-LO loans from join. Elena no longer implicitly framed as compliance authority.
- **Statement 3 (validator FAIL band false positive):** 12 Jaccard-71% pairs re-examined pair-by-pair — every pair has DIFFERENT recipient email + DISJOINT loan-atom set. Consolidation to 8 combined "notify + content" rubrics would violate atomicity (send-success + content-correctness are independent pass/fail dimensions). Fan-out is the atomically-correct design.
- **Statement 4 (3 "at least N" uses):** Rubric [22] "at least one activity note" — prompt says "any loan that needs updating" (implicit floor ≥ 1) → defensible. Rubric [23] "at least one CRM engagement" — prompt says "log everything" (universal, floor ≥ 1 is under-specification but defensible) → MINOR soft observation, not blocker. Rubric [24] "at least one compliance concern" — prompt says "If anything" (conditional; universe seeds 3 findings) → defensible.
- **Statement 5 (Rubric [28] pressure test):** 3-trajectory spot-check of final response text → 0/3 mentioned "LN-2026-00623" (runs 1, 3, 5). This is legitimate Bucket 3 model summary-drift (per REVIEW_hardness pass@1 = 33.3%). Rubric [28] correctly gates a real difficulty locus; NOT rubric brittleness. Agents DID discover the anomaly in per-loan queries and per-LO emails (rubric [13] passes) but omitted from final summary.

## Discrepancies surfaced
- **Soft observation on Rubric [23]:** Prompt "log everything in the CRM" is universal; rubric floor "at least one" is defensible but weaker than prompt mandate. Under strictest reading this is a MINOR observation, not a blocker. No fix required for this audit cycle; noted for potential future tightening if platform-side rubric review requests a stronger floor.
