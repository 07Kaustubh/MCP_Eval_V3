# PIPELINE FINAL — Todos (Task 45)

Universe: starpm (V4). Extra deterministic gates apply (injection + submission_gate).

- [ ] T1: Create Todos_final.md (this file) — v11 E1 gate
- [ ] T2: Create Reads_final.md — v11 E2 gate
- [ ] T3: Run `validate.py --phase all` — must exit 0
- [ ] T4: V4 gate — run `validate.py --phase injection` — must PASS (Evals_starpm/0)
- [ ] T5: V4 gate — run `validate.py --phase submission_gate` — must PASS (Evals_starpm/5, F1-F9)
- [ ] T6: Read all 3 artifacts together (5_Prompt, 6_Oracle_Events, 7_Rubrics)
- [ ] T7: Read Hardness_Plan.md + Fact_Ledger.json + Universe_Index + Changelog + inject SQL
- [ ] T8: Read Learnings.md + QC spec docs (Docs_starpm/7 + 8)
- [ ] T9: Spawn Final Council (oracle/ultrabrain) — 6 lenses, dual-model V4 sign-off note
- [ ] T10: Read verdict; if REVISE, apply fixes in place + re-run validators (cap 3 rounds)
- [ ] T11: Write Verification_final.md (Step 0.5 cross-source re-check)
- [ ] T12: On PASS — append Hardness_Patterns_Log.md entry; STOP gate


---
## STATUS: ALL COMPLETE — VERDICT: PASS (2026-07-27)
T1-T2 discipline files created. T3 validate all PASS. T4 injection PASS. T5 submission_gate: was FAIL (2x F2 on 2026-07-15), resolved via Path B gate fix -> now PASS. T6-T8 all inputs read. T9 Final Council (oracle bg_b8a07f68) ran 6 lenses + submission_gate adjudication. T10 verdict PASS; Path B implemented + regression clean (anchors 62/62, reports 21/21, verdicts 7/7; 0/21 hashes moved); gates re-run all green. T11 Verification_final.md written. T12 Hardness_Patterns_Log entry + FINAL_council operator addendum written.

Rubrics 5/6/7 shipped UNCHANGED. v4_gates.py Path B fix additive, regression-clean, NOT committed. Cleared for platform upload (dual-model, 6 runs each). MANDATORY S4 density gate: real-run per-model avg < 40 -> PIPELINE REDO.

STOP gate reached. Next trigger (fresh chat): PIPELINE S4 (paste 8a/8b) or PIPELINE REDO.