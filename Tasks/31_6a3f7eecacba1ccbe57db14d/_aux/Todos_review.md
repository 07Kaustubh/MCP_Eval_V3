# Todos — REVIEW (v11 E1 gate) — second pass (materialization)

Task: 31_6a3f7eecacba1ccbe57db14d
Trigger: PIPELINE REVIEW — Tasks/31_6a3f7eecacba1ccbe57db14d
Mode: materialization pass (both rows Applied)

## First-pass (intake + scoring) — 2026-06-27 14:46
- [completed] All 12 first-pass steps (see prior version of this file in git history if needed)
- Verdict: SALVAGEABLE, 2 rubric-phase rows in changes.md (R9 wording + R4 anchor), both originally Pending

## Second-pass (materialization) — 2026-06-27 15:09
- [completed] M0. User marked both changes.md rows Applied
- [completed] M1. Read 7_Rubrics.json, identified R9 (idx 8) + R4 (idx 3) edit sites
- [completed] M2. Materialized 15_Updated_Rubrics.json with both surgical fixes (R9 title `such as` → `any of the Brookfield-internal partners`; R4 evidence prefix `PASS via either path.` → `Look for either path.`)
- [completed] M3. validate.py --phase rubrics on corrected set: PASS (0 fails / 17 warns / 3 notes)
- [completed] M4. test_regression_anchors.py: 33/33 PASS
- [completed] M5. calc_similarity.py: all composites < 40 (clear)
- [completed] M6. AUDIT --phase rubrics on corrected materialization: PASS (STRICT) — _aux/Council_Reports/AUDIT_rubrics.md
- [completed] M7. Appended one-line entry to Tasks/_meta/Audit_Log.md
- [completed] M8. changes.md updated with materialization-complete section
- [completed] M9. Scratch validation dir cleaned
- [completed] M10. Originals 5/6/7 verified untouched

## Artifacts produced this pass
- 15_Updated_Rubrics.json (corrected rubric set, shipped)
- _aux/Validator_Reports/rubrics_corrected.md (validator detailed report on corrected set)
- _aux/Council_Reports/AUDIT_rubrics.md (strict audit on corrected set, PASS STRICT)
- _aux/Similarity_Report.json (updated)
- Tasks/_meta/Audit_Log.md (one-line entry appended)

## Next trigger
- PIPELINE FEEDBACK — Tasks/31_6a3f7eecacba1ccbe57db14d (fresh chat) to write 13_Feedback.txt
- After FEEDBACK: PIPELINE CLOSE — Tasks/31_6a3f7eecacba1ccbe57db14d
