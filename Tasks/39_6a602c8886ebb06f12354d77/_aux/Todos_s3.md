# S3 — Rubrics TODO (Tasks/39_6a602c8886ebb06f12354d77, universe=starpm/V4)

- [x] 0. Phase-readiness gate (phase_ready.py --phase s3) + resolved upstream Verification_s2.md hygiene
- [x] 1. Read V4 QC_Passed reference rubric (Task2) + Rubric_Format + Docs_starpm 2_Rubrics_V3_Guidelines + Evals_starpm 3_Rubrics_Eval + tool catalog
- [x] 2. Read task inputs: 5_Prompt, 6_Oracle_Events, Hardness_Plan, Fact_Ledger, Universe_Index, Universe_Split
- [x] 3. Drafted Outcome rubrics first - OE write action -> 1.1 (+1.2 content); prompt tell-me cue -> 2.1; atomic per item, grounded, no 'at least N' (15 rubrics)
- [x] 4. Three-condition test for Process candidates -> ZERO process (SoR verification folded into R14 Outcome)
- [x] 5. Wrote 7_Rubrics.json in FLAT schema (title, category, justification, evidence)
- [x] 6. Validator (validate.py --phase rubrics) -> PASS, 0 fails, 0 warns
- [x] 7. Council A - Grounding GO (every value grounded; near-miss excluded; decoy unused) -> S3_A_grounding.md
- [x] 8. Council B - Adversarial QC (ultrabrain) GO (sub-dims 5/5; alt-path/reverse/forward/atomicity clean; density ~47; 5 levers) -> S3_B_adversarial.md
- [x] 9. Applied 5 preemptive hardening tweaks + 2 AUDIT REVISE fixes; re-ran validator -> PASS
- [x] 10. AUDIT (ultrabrain, strict veteran) PASS (STRICT), 10/10 sub-dims 5/5, anchors 62/62 -> AUDIT_rubrics.md
- [x] 11. Coverage matrix -> _aux/Reasoning/Rubric_Coverage_Matrix.md (prompt -> OE -> rubric -> lever)
- [x] 12. Step 0.5 cross-source Verification_s3.md written + boxes checked; check_verification s3 exit 0
- [x] 13. STOP gate - end response, nudge PIPELINE FINAL

STATUS: COMPLETE - all S3 exit criteria met; FINAL-ready (phase_ready --phase final green).
