# PIPELINE FINAL — Todos (Task 40_6a614767cd5b60ad96902fb4, StarPM V4)

- [x] Step 0: Create this TODO list
- [x] Step 0.5b: Create _aux/Reads_final.md (v11 E2 read-log)
- [x] Phase-readiness gate (phase_ready.py --phase final) — OK
- [x] Validators: validate.py --phase all — PASS
- [x] V4 gate: validate.py --phase injection — PASS (4 COUNCIL notes for Final Council)
- [x] V4 gate: validate.py --phase submission_gate — **FAIL (5)**; diagnosed as validator false-positives
- [x] Read exact gate logic (v4_gates.py) + mandates (Evals_starpm/5, V4_ENFORCEMENT_AUDIT.md) + regression scope
- [x] Oracle consult (bg_6a7734aa): blessed F4 Decimal-normalization + F2 triple-gate calendar exemption + confirmed regression-safe
- [x] Apply Oracle-blessed validator fix to v4_gates.py — DONE (decimal import + helpers + F2/F4 rewrite)
- [x] Re-run submission_gate — PASS (5 fails -> 0; F2 exemption emits COUNCIL confirm-day notes)
- [x] check_regression.py + test_regression_anchors.py — GREEN (anchors 62/62, reports 21/21, verdicts 7/7)
- [x] Re-run validate.py --phase all — PASS; qc_verdict selftest 128/128 (16+16+80+16)
- [x] Spawn Final Council (6 lenses) — bg_96b90e1d (oracle, StarPM V4 routing + gate COUNCIL notes)
- [x] Read council verdict — VERDICT: PASS (0 BLOCKER / 0 MAJOR / Bucket-1 0%); no REVISE round needed
- [x] Write _aux/Verification_final.md (cross-source re-check) — DONE
- [x] Exit: FINAL_council.md VERDICT: PASS + Hardness_Patterns_Log entry appended — DONE
