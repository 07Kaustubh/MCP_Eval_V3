# Todos - S2 (Oracle Events) - Task 43_6a62ccaf5853030245ac9d53

Runbook: `Reference/Sessions/S2.md`. Status legend: `pending` / `in_progress` / `completed`.

| # | Step | Status |
|---|---|---|
| 0 | Run phase-readiness gate (`phase_ready.py --phase s2`) | completed |
| 1 | Create `_aux/Todos_s2.md` (this file) | completed |
| 2 | Create `_aux/Reads_s2.md` (v11 E2 reference-read log) | completed |
| 3 | Read bootstrap: `AGENTS.md`, `Reference/OE_Format.md`, `_aux/Universe.txt` (starpm) | completed |
| 4 | Read upstream: `5_Prompt.txt`, `_aux/Hardness_Plan.md`, `_aux/Verification_s1.md`, `_aux/Fact_Ledger.json`, `_aux/Universe_Index/*` | completed |
| 5 | Read StarPM tool catalog `StarPM_Base_Universe/7_Server_Tools_Details.json` (names + exact param signatures) | completed |
| 6 | Read reference OE corpus (`QC_Tasks/V4_Tasks/QC_Passed/Task2`, `Tasks/41_.../6_Oracle_Events.txt`) | completed |
| 7 | Read eval spec `Evals_starpm/2_OE_Eval.md` + QC spec `Docs_starpm/7_QC_Spec_Doc1.json` OE dimension | completed |
| 8 | Step 1: Decompose `5_Prompt.txt` sentence by sentence into explicit + implicit asks; map to discovery vs write steps | completed |
| 9 | Step 2: Verify every record / amount / id / channel / recipient against `_aux/Universe_Split/` | completed |
| 10 | Step 2b: Resolve the 4 S1 carry-forward watch-items (Slack channel pin, 4C Airtable row pin, Airtable write mechanism, closet-vs-Alamo rationale) | completed |
| 11 | Step 3: Draft `6_Oracle_Events.txt` (28 numbered steps, no em-dashes, real tools + params) | completed |
| 12 | Step 4: Run `validate.py --phase oe`; read `_aux/Validator_Reports/oe.md`; fix all fails; re-run clean | completed (0 fails / 0 warns) |
| 13 | Step 4b: Run `verify_universe_atoms.py` on the OE | completed (0 fails / 0 warns / 16 atoms; coverage gap recorded in Verification_s2) |
| 14 | Step 5: Council A (Grounding) -> `_aux/Council_Reports/S2_A_grounding.md` | completed (round 1 BLOCK on 4 Major; round 2 GO, 0 NOT FOUND, 0 solvability breaks) |
| 15 | Step 6: Council B (Adversarial QC: B1 / B2 / B3 density / B4 levers / B6 / B8 forward+reverse / B9) -> `_aux/Council_Reports/S2_B_adversarial.md` | completed (round 1 BLOCK; round 2 GO, both sub-dims 5/5, no PROPAGATE) |
| 16 | Step 7: Loop - apply fixes, re-run validator + BOTH councils until clean | completed (council round 1: 13 fixes; council round 2 residuals: 8 fixes; AUDIT round 1: 15 fixes; validator clean after each) |
| 17 | Step 8: Strict veteran AUDIT (`AUDIT.md --phase oe`) -> `_aux/Council_Reports/AUDIT_oe.md`; require `PASS (STRICT)` (cap 3 REVISE rounds). MANDATORY here (Track F condition d: OE revised this pass) | completed: round 1 REVISE (5 Major / 10 Minor, all independently verified then applied); round 2 PASS (STRICT), both sub-dims 5/5, 1 of 3 cap used |
| 17b | AUDIT Lens 8 prerequisite: run `test_regression_anchors.py` | completed (62/62 PASS) |
| 18 | Step 0.5: Write `_aux/Verification_s2.md` cross-source verification | completed (check_verification.py: all sections present, all statements checked, 8 discrepancies surfaced) |
| 19 | Step 9: Append final report to `_aux/Reasoning/OE_solvability.md` (coverage map + rubric-mapping preview + AUDIT verdict) | completed |
| 20 | Exit criteria re-check, then STOP (wait for `PIPELINE S3`) | completed; one-line entry appended to `Tasks/_meta/Audit_Log.md` |
