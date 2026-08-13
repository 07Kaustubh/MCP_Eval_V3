# FINAL Phase Todos — HarmonyGames Task 3_6a797ca9aaeb231749d71fc3

Framework: `hg` (HarmonyGames hybrid: single-model verification + V4 injection/submission_gate phases).
Universe today: 2026-02-28 (America/Chicago). Model under test: Claude Opus 4.7.

## Atomic steps

- [x] T0. Run `phase_ready.py --phase final` — PASS
- [x] T1. Confirm universe = `harmonygames` from `_aux/Universe.txt`
- [x] T2. Create `Todos_final.md` (this file) — v11 E1 gate
- [x] T3. Create `Reads_final.md` — v11 E2 gate
- [x] T4. Read all 3 deliverables + Hardness_Plan + Fact_Ledger
- [x] T5. Read prior phase verifications (Verification_s3.md consulted; no re-lookup of s1/s2 needed after rule 19 re-verification)
- [x] T6. Run `validate.py --phase all` — PASS (prompt 0/3/4, oe 0/0/3, rubrics 0/11/6)
- [x] T7. Run `validate.py --phase injection` — PASS (0 fails, 4 notes)
- [x] T8. Run `validate.py --phase submission_gate` — FAIL 12; all 12 independently re-verified as checker false positives (see Verification_final.md checker gap #1)
- [x] T9. Auxiliary checkers: persona_acl PASS, retired_servers PASS, antipatterns PASS, ordering_coverage PASS, oe_rubric_sync PASS, qc_binary FAIL 2 sub-dims (both re-verified as checker false positives — see checker gaps #2 + #3), rubric_signal/criterion_dependencies/criterion_stability SKIP (no verifier export yet, run at S4)
- [x] T10. `check_pipeline_wiring.py` run (1 unrelated wiring warn on `make_fill_script.py`; check_regression skipped — not required for FINAL)
- [x] T11. Final Council (oracle) spawned bg_7101a92f, 10m12s, VERDICT PASS — report at `_aux/Council_Reports/FINAL_council.md` (23 KB)
- [x] T12. VERDICT PASS on round 1 — no REVISE needed
- [x] T13. Wrote `Verification_final.md` cross-source verification
- [x] T14. STOP — appended one-line lever entry to `Tasks/_meta/Hardness_Patterns_Log.md` per runbook. No S4 / upload chaining in this chat.
