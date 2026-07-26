# Todos — PIPELINE S3 (Rubrics) — Tasks/44_6a62ccba8cad60844b8364b9

Universe: starpm (V4)

| # | Step | Status |
|---|---|---|
| 0 | Run `phase_ready.py --phase s3` gate | completed |
| 1 | Create `_aux/Todos_s3.md` (this file) | completed |
| 2 | Create `_aux/Reads_s3.md` reference-read log | completed |
| 3 | Read `Reference/Rubric_Format.md` (flat schema + thresholds) | completed |
| 4 | Read `Docs_starpm/2_Rubrics_V3_Guidelines.md` (framework rules) | completed |
| 5 | Read `Docs_starpm/12_Always_Failing_Rubrics.md` (AF patterns) | completed |
| 6 | Read `Evals_starpm/3_Rubrics_Eval.md` (eval spec sub-dims, all 1079 lines) | completed |
| 7 | Read `Docs_starpm/7_QC_Spec_Doc1.json` Rubric dimension + appendix issue types | completed |
| 8 | Read ALL 4 V4 reference rubric sets `QC_Tasks/V4_Tasks/QC_Passed/Task1..4/7_Rubrics.json` in full | completed |
| 9 | Read `Reference/Strict_Convention_Inventory.json` allowed phrasings | completed |
| 10 | Re-read `5_Prompt.txt` + `6_Oracle_Events.txt` + `_aux/Hardness_Plan.md` + `_aux/Verification_s2.md` | completed |
| 11 | Confirm tool catalog `StarPM_Base_Universe/7_Server_Tools_Details.json` write-action params | completed |
| 12 | Build prompt-ask inventory (every "tell me" cue + every write action) | completed |
| 13 | Draft Outcome 1.1 rubrics — one per OE write action, atomic per item | completed |
| 14 | Draft Outcome 1.2 rubrics where write has content requirements beyond 1.1 | completed |
| 15 | Draft Outcome 2.1 rubrics — one per prompt tell-me cue | completed |
| 16 | Apply three-condition test to any Process candidate (result: zero process) | completed |
| 17 | Ground every concrete value against `_aux/Universe_Split/` + `_aux/Fact_Ledger.json` | completed |
| 18 | Write `7_Rubrics.json` in FLAT schema (title, category, justification, evidence) | completed |
| 19 | Run `validate.py --phase rubrics`; read report; fix every fail | completed |
| 20 | Spawn Council A — Grounding → `_aux/Council_Reports/S3_A_grounding.md` | completed (R1 BLOCK) |
| 21 | Spawn Council B — Adversarial QC → `_aux/Council_Reports/S3_B_adversarial.md` | completed (R1 BLOCK) |
| 22 | Loop: apply fixes, re-run validator + both councils until clean | completed (3 rounds, both GO) |
| 23 | Spawn strict veteran AUDIT (`--phase rubrics`) → `_aux/Council_Reports/AUDIT_rubrics.md` | completed |
| 24 | Resolve AUDIT verdict (PASS STRICT / REVISE cap 3 / REBUILD stop) | completed (1 REVISE round → PASS STRICT) |
| 25 | Write `_aux/Reasoning/Rubric_Coverage_Matrix.md` (prompt → OE → rubric, no gaps/surplus) | completed |
| 26 | Write `_aux/Verification_s3.md` cross-source verification doc | completed (check_verification.py OK) |
| 27 | Append AUDIT verdict to `Tasks/_meta/Audit_Log.md` + 2 cross-task learnings | completed |
| 28 | Confirm exit criteria; STOP gate (do not chain to FINAL) | completed |

## Iteration log

### Round 1 — 56 rubrics, validator PASS (0/0/5), both councils BLOCK

**Council A (grounding) — 2 blocks, same defect family.** Rubrics asserting the second round of North cluster
tenant access notices was "never confirmed" / "still pending" are falsified by Slack `ts 1779832537.000013`,
Carlos Mendez, C001, 2026-05-26: "48-hour notice letters are out to all affected tenants." That message appears
in no Oracle Event and in no prior council report; a compliant agent paging the full 104-message C001 history
surfaces it and correctly declines to write "never confirmed" — a false-fail. Verified independently before
acting on it. All 54 other rubrics grounded; overclaim sweep clean; persona scope clean.

**Council B (adversarial) — 3 Major, 5 Moderate, 3 Minor. Overall Rubric Quality 3 (NON-FAIL).**
1. Major: no criterion graded the "what is actually finished" half of "Work out what is actually finished and
   what is not" — all 56 graded an open/gap finding. Anti-overclaim guards lived only in `evidence`.
2. Major: the South no-access unit was locked to tracking-item routing, which OE 28 forbids verbatim.
3. Major: the email South criterion bundled the open item and its remedy; East and West had no
   "what has to happen" criterion at all, which OE 38 requires per cluster.
4. Moderate: the plumbing budget criterion pinned an elective past-dated calendar read (highest AF risk).
5. Moderate: the East owner criterion demanded an owner inside a Linear comment under OE 33's permitted path.
6+7. Moderate: two criteria graded an absence ("were never dispositioned") as the answer, against OE 16 and
   Hardness constraint 7.
8. Moderate: no final-response criterion for the plumbing findings or the filter run.

### Round 2 — 63 rubrics, validator PASS (0 fails, 0 warns)

Fixes applied: falsifiable access-notice clause removed from indices 12 / 33 / 44 with explicit judge guards;
absence-as-answer reframed positively at 32 / 56; routing lock opened at 11; email South split into 41 + 42;
per-cluster "what has to happen" added for East (46) and West (48); budget criterion at 18 de-pinned from the
calendar; East owner at 23 made location-flexible and the now-redundant email East-owner criterion deleted;
final-response coverage added for plumbing (58) and filter run (59); two positive-completion criteria added at
60 (condensate drain cleared) and 61 (East coil cleaning and A/C checks completed); West-coverage criteria at
3 / 35 / 47 scoped and differentiated per artifact; ticket-shape over-specification removed from 0.

Both councils re-running against the revised set with round-1 context retained.
