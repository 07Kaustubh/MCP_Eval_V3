# S3 Todos - Tasks/46_6a62ccb6ce2323b4b9e0c8d8

Universe: starpm (V4). Phase: rubrics. Ceiling: 60 criteria (AGENTS.md rule 14).

| # | Step | Status |
|---|---|---|
| 0 | Phase-readiness gate (`phase_ready.py --phase s3`) | completed |
| 1 | Create `_aux/Todos_s3.md` (this file) | completed |
| 2 | Create `_aux/Reads_s3.md` and log every spec/card/eval read | completed |
| 3 | Read `Docs_starpm/9_Common_Error.md` Part 3 rubric errors BEFORE drafting | completed |
| 4 | Read `5_Prompt.txt` + `6_Oracle_Events.txt` in full | completed |
| 5 | Read `_aux/Hardness_Plan.md` levers + `_aux/Handoff_S2_S3.md` obligations | completed |
| 6 | Read `Reference/Rubric_Format.md` + `Reference/Strict_Convention_Inventory.json` | completed |
| 7 | Read `Docs_starpm/2_Rubrics_V3_Guidelines.md` + `Docs_starpm/12_Always_Failing_Rubrics.md` | completed |
| 8 | Read every `QC_Tasks/V4_Tasks/QC_Passed/Task*/7_Rubrics.json` reference set in full | completed |
| 9 | Read `Evals_starpm/3_Rubrics_Eval.md` + `Docs_starpm/7_QC_Spec_Doc1.json` rubric sub-dims | completed |
| 10 | Ground every candidate value against `_aux/Universe_Split/` + `_aux/Fact_Ledger.json` | completed |
| 11 | Draft Outcome 1.1 per OE write action (6 write carriers) | completed |
| 12 | Draft Outcome 1.2 per named content element (19 elements across OE 30/31/33/36) | completed |
| 13 | Draft Outcome 2.1 per prompt tell-me cue | completed |
| 14 | Three-condition test on every Process candidate; default zero | completed |
| 15 | Budget L11 explicitly (no 1.1 carrier; 1.2/2.1 only) per Handoff obligation 6 | completed |
| 16 | Pin cardinality on the Linear create (F8) per Handoff obligation 6b | completed |
| 17 | Verify flat schema: exactly `{title, category, justification, evidence}` | completed |
| 18 | Run `validate.py --phase rubrics`; fix every fail | completed |
| 19 | Council A - Grounding (`_aux/Council_Reports/S3_A_grounding.md`) | completed |
| 20 | Council B - Adversarial QC, ultrabrain (`_aux/Council_Reports/S3_B_adversarial.md`) | completed |
| 21 | Loop: fixes -> validator -> both councils until clean | completed (2 rounds; A: BLOCK then GO, B: BLOCK then BLOCK, all findings applied) |
| 22 | AUDIT auto-fire, ultrabrain (`_aux/Council_Reports/AUDIT_rubrics.md`), require PASS (STRICT) | in_progress |
| 23 | `check_rubric_signal.py` reviewed BEFORE trimming to the 60 cap | completed (SKIP: no verifier export until S4; set is 35 of 60, no trim needed) |
| 24 | `check_ordering_coverage.py` exits 0 | completed |
| 25 | `check_rubric_antipatterns.py` + `check_oe_rubric_sync.py` + `check_qc_binary.py` clean | completed |
| 26 | Coverage matrix `_aux/Reasoning/Rubric_Coverage_Matrix.md` (prompt sentence -> OE -> rubric) | completed |
| 27 | Write `_aux/Verification_s3.md` to `check_verification.py`'s contract (NOT the runbook template) | completed (gate returns OK) |
| 28 | STOP gate: end response, hand off to `PIPELINE FINAL` | pending |

## Binding constraints carried into this phase

- Rule 13 single-target uniqueness: never pin a bare calendar base id; never pin OPS-10 by title.
- Rule 14: 60-criterion ceiling; never cut a lever carrier; mirror any cut into the OE's decompose directive.
- Rule 21: an all-failing criterion defaults to REMOVAL.
- Rule 23: zero Process is valid here only because all 6 ORDERING patterns return zero hits - re-check.
- Rule 28: cut zero-signal existence-only criteria first.
- Handoff 4/5: no write criterion against QuickBooks or `tblMaintenanceTickets`.
- Handoff (S2 close) 1/2: Mesa Vista 4C is Castillo's and is finished - outside the graded set.
- Handoff (Oracle) 1: occupancy is graded as a refutation, never as a reported figure.
- Handoff (Oracle) 4: Sunset Ridge corrections rest on supersession, not elapsed time.
- Handoff (Oracle) 7: never grade the number of events returned by the `fullText "Harris"` search.
