# S4 — Verifier-Fails Analysis TODOs (V4 dual-model)

- [ ] G0. Phase-ready + parse_trajectories gates (DONE — note Gemini parser undercount)
- [ ] G1. Compute REAL Gemini per-model density (parser schema gap) + confirm no REDO
- [ ] T3. Error-rate gate: count erroneous runs per model (>=3 => FAIL)
- [ ] T2. Agent-failure gate: pass@1 per model (>40% => REDO)
- [ ] R1. Read core inputs: 8a, 8b, 7_Rubrics, 5_Prompt, 6_Oracle_Events
- [ ] R2. Read QC chain: 9_QC_Feedback, 10_PT_Dispute, 11_Final_QC_Validation
- [ ] R3. Read Hardness_Plan + Trajectory_Stats
- [ ] Q1. Run qc_verdict.py parse|classify|audit (V4 QC-feedback stage)
- [ ] M1. Build rubric x run matrix — OPUS (pass/fail/NE per rubric per run)
- [ ] M2. Build rubric x run matrix — GEMINI
- [ ] W1. Trajectory walk every failing rubric — OPUS (cite Run X, tool call Y)
- [ ] W2. Trajectory walk every failing rubric — GEMINI
- [ ] B1. Classify each failing rubric into Bucket 1/2/3 (per model) w/ 5-point checklist
- [ ] F1. Write S4_fixes.md (Bucket 1)
- [ ] F2. Write S4_judge_errors.md (Bucket 2)
- [ ] F3. Write S4_AF_justifications.md (Bucket 3) + check_justification.py exit 0
- [ ] AF. All-Failing Rubrics sub-dim scoring (Bucket 1 ratio) per model
- [ ] C1. Update Tasks/_meta/Stump_Hypotheses.md
- [ ] C2. Update Tasks/_meta/Hardness_Patterns_Log.md
- [ ] V1. Write _aux/Verification_s4.md (cross-source check)
- [ ] VR. Write _aux/Council_Reports/S4_verdict.md (matrix + classifications + gates)

---
STATUS: COMPLETE (S4 STRONG PASS, dual-model). All exit criteria met 2026-07-23.


---
## STATUS: ALL COMPLETE (2026-07-23)
All 21 steps done. Gates: phase_ready inputs present; parse_trajectories OK (Gemini density hand-corrected to 33.0 vs parser 0). T2 pass@1 0% both models, T3 0 errored both models, density Opus 43.5 / Gemini 33.0 (both >= 15 floor). Classifications: 0 Bucket-1, 0 Bucket-2, all Bucket-3; All-Failing sub-dim 5/5. AF batch check_justification exit 0. Verdict: STRONG PASS, no REDO, no rubric edits. Deliverables: S4_verdict / S4_fixes / S4_judge_errors / S4_AF_justifications / _aux/S4_bucket3 / _aux/Verification_s4 written; Stump_Hypotheses + Hardness_Patterns_Log + Learnings (L31) appended.