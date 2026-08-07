# S3 Todos — 2_6a6beba55996ad2ada369b15 (HarmonyGames)

| # | Step | Status |
|---|---|---|
| 1 | Phase-readiness gate (`phase_ready.py --phase s3`) | completed |
| 2 | Create `_aux/Todos_s3.md` (this file) | completed |
| 3 | Create `_aux/Reads_s3.md` and log every spec/card read | completed |
| 4 | Read `Docs_harmonygames/9_Common_Error.md` Part 3 rubric errors BEFORE drafting | completed |
| 5 | Read `Docs_harmonygames/2_Rubrics_Guidelines.md` + `3_Rubrics_One_Pager.md` | completed |
| 6 | Read `Docs_harmonygames/7_QC_Spec_Doc1.json` rubric dimension + `8_QC_Spec_Doc2.md` severity/negative-criteria | completed |
| 7 | Read `Docs_harmonygames/12_Always_Failing_Rubrics.md` | completed |
| 8 | Read `Evals_harmonygames/3_Rubrics_Eval.md` | completed |
| 9 | Read `Reference/Rubric_Format.md` + `Strict_Convention_Inventory.json` | completed (Brookfield-derived; HG phrasing SSOT used instead, see Reads_s3) |
| 10 | Read every HG QC_Passed reference `7_Rubrics.json` in full (phrasing SSOT) | completed |
| 11 | Re-read `_aux/Hardness_Plan.md` levers for B4 lever-carrier mapping | completed (delegated to Council B B4) |
| 12 | Draft `7_Rubrics.json` — Outcome 1.1 per OE write action, 1.2 for content, 2.1 per prompt tell-me cue | completed (25 criteria) |
| 13 | Apply three-condition test to Process candidates; ordering constraint per hard rule 23 | completed (1 Process) |
| 14 | Budget against the 60-criterion cap from the start (hard rule 14) | completed (25 of 60) |
| 15 | Mirror OE `S3 must decompose` directives one-for-one (OE 20, 21, 22, 23) | completed (OE 20 + OE 21 mirrored) |
| 16 | Run `validate.py --phase rubrics`; fix every fail | completed (PASS, 0 fails, 0 warns) |
| 17 | Run `check_rubric_antipatterns.py` (A5 negative-criteria gate, A6 vague exemplar — HG-scoped) | completed (OK) |
| 18 | Run `check_ordering_coverage.py` — exit 0 | completed (OK) |
| 19 | Run `check_oe_rubric_sync.py` — decompose directives vs carriers | completed (OK after mirroring) |
| 20 | Run `check_rubric_signal.py` before any trim to the cap | completed (SKIP, no verifier export pre-S4; no trim needed at 25 of 60) |
| 21 | Run `check_qc_binary.py` | completed (6/6 measurable binary sub-dims PASS) |
| 22 | Council A — Grounding (every concrete value greped against Universe_Split) | completed (**GO**, zero mismatches) |
| 23 | Council B — Adversarial QC (`ultrabrain`) | completed (**GO** round 2, one Major fixed in place) |
| 24 | Loop: apply fixes, re-run validator + both councils until clean | completed (1 REVISE round of 3) |
| 25 | AUDIT (auto-fire, mandatory, `ultrabrain`) → `_aux/Council_Reports/AUDIT_rubrics.md`, verdict `PASS (STRICT)` | completed (**PASS (STRICT)**, round 1) |
| 26 | Write `_aux/Reasoning/Rubric_Coverage_Matrix.md` (prompt sentence → OE step → rubric) | completed |
| 27 | Write `_aux/Verification_s3.md` cross-source verification | completed (`check_verification.py` OK) |
| 28 | Append to `Tasks/_meta/Audit_Log.md` | completed |
| 29 | STOP gate — end response, nudge to `PIPELINE FINAL` | completed |

## Draft shape

25 criteria: Outcome 1.1 = 3, Outcome 1.2 = 18, Outcome 2.1 = 3, Process = 1. Process share 4 percent against the HarmonyGames flat cap of 40 percent.

Two OE decompose element lists were mirrored this pass under rule 14. Both relaxations removed defects the OE was seeding: a negatively framed engagement element (`reported without softening`, an HG dimension 23 trap) and a non-atomic `at least the coverage verdict and the still-running spend figure` bundle. `validate.py --phase oe` re-run after the edit and still PASS 0 fails / 0 warns.

`category` ships in the spec-conformant 4-value enum rather than the lowercase form the shipped HG corpus uses. Rationale recorded in `Reads_s3.md`.
