# S3 Todos — Task 45 (StarPM V4) — Rubrics

Correct end-state: HOLD / kick-back on Mesa Vista 4C current turn recbd087a4abd605b (selProg). NOT marketing-ready.

- [x] 0. Phase-ready gate (fixed upstream Verification_s2.md header hygiene to canonical shape; no S2 re-run)
- [x] 1. Create Todos_s3.md (this file) + Reads_s3.md
- [ ] 2. Read all S3 required inputs (Hardness_Plan, Rubric_Format, Docs_starpm 2_Rubrics_V3_Guidelines, 9_Common_Error Part 3, 12_Always_Failing_Rubrics, 4x V4 QC_Passed reference rubric sets, Strict_Convention_Inventory, Fact_Ledger atoms, S2 council + AUDIT_oe carry-forwards) — log each to Reads_s3.md
- [ ] 3. Build coverage skeleton: every prompt ask + every OE write action (OE10-15) + every final-response fact -> planned rubric; map Hardness levers to carrier rubrics
- [ ] 4. Draft 7_Rubrics.json (flat 4-field schema; Outcome-first; 1.1 per write, 1.2 for content beyond 1.1, 2.1 per final-response fact; atomic multi-item; three-condition test for any process; every concrete value grounded in Fact_Ledger; <= 60 cap)
- [ ] 5. Run validate.py --phase rubrics; fix every fail (schema, agent-centric, no tool names in title, no 'at least N', outcome>process, grounded sweep, F7/F8/F9)
- [ ] 6. Run check_rubric_signal.py (before any 60-cap trim); cut existence-only zero-signal criteria whose content a sibling already grades
- [ ] 7. Run check_ordering_coverage.py (exit 0)
- [ ] 8. Spawn Council A (grounding) -> _aux/Council_Reports/S3_A_grounding.md; block on any ungrounded value
- [ ] 9. Spawn Council B (adversarial QC, ultrabrain) -> _aux/Council_Reports/S3_B_adversarial.md; block on Major/Moderate; B3 density >=50 (or THIN carry); B4 all levers covered
- [ ] 10. Loop: apply fixes, re-run validator + both councils until clean
- [ ] 11. Spawn AUDIT (ultrabrain, --phase rubrics) -> _aux/Council_Reports/AUDIT_rubrics.md; require PASS (STRICT); handle REVISE (cap 3) / REBUILD / PROPAGATE
- [ ] 12. Write _aux/Reasoning/Rubric_Coverage_Matrix.md (prompt sentence -> OE step -> rubric; no gaps/surplus; AUDIT verdict in header)
- [ ] 13. Write _aux/Verification_s3.md (canonical shape)
- [ ] 14. Confirm all exit criteria; STOP gate (wait for PIPELINE FINAL)
