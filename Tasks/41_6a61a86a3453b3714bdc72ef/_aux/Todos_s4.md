# S4 Todos — Tasks/41_6a61a86a3453b3714bdc72ef (V4 dual-model: Opus + Gemini) — post-fix re-grade

- [x] Phase-readiness gate (phase_ready.py --phase s4) — PASS (5 dual-model artifacts present)
- [x] parse_trajectories.py — Verdict OK (pass@1=0.0 both models, density 43.4; 12/12 ok)
- [x] Read 5_Prompt / 6_Oracle_Events / 7_Rubrics (post-fix rubric set)
- [x] Read 8a (Opus) + 8b (Gemini) verifier fails; build rubric×run matrix per model
- [x] Read S4 runbook + Hardness_Plan + prior S4 artifacts (fixes/judge_errors/verdict/Bucket3)
- [x] Trajectory hard gates: T3 (0/6 both, PASS) + T2 (pass@1 0% both, PASS) recorded per model
- [x] Build rubric×run matrix (Opus + Gemini) — S4_verdict.md
- [x] For EVERY failing rubric, walk trajectory BEFORE classifying (raw tool-call extraction, both models)
- [x] Verify ground truth in raw Universe_Split: balance trap (QR-2026-0441 847/925/210/-150 vs invoice 7214 1125/975/187.50), owner (Castillo via EVF-2026-014 vs Harris Linear decoy; both role=Property Owner)
- [x] Confirm R6 fix effective in re-grade (now passes 6/6; prior Bucket-1 defect CLOSED)
- [x] Apply 5-point pre-write checklist before each AF justification (all YES for balance rubrics)
- [x] Classify each failing rubric — ALL 8 Bucket 3 (R1/R2/R16 AF both models; R4/R11/R15/R18 Opus; R14 Gemini); zero Bucket 1, zero Bucket 2
- [x] Compute Bucket 1 ratio (0/3 AF = 0%) → All-Failing Rubrics sub-dim = 5/5 PASS
- [x] Update S4_fixes.md (fix confirmed effective, none outstanding), S4_judge_errors.md (zero this run), S4_Bucket3.md (R6 dropped), keep S4_AF_justifications.md
- [x] Run check_justification.py on AF batch → exit 0
- [x] Append re-run calibration delta → Stump_Hypotheses.md + Hardness_Patterns_Log.md
- [x] Write S4_verdict.md (matrix + classifications + calibration) + Verification_s4.md
- [x] STOP — do not loop S4
