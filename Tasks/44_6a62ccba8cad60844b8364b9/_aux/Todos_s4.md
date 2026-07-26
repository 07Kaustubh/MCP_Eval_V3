# S4 TODOs - Task 44 (`44_6a62ccba8cad60844b8364b9`) · StarPM V4, dual-model · PASS 4

Re-invocation after two input changes: the 14:42 AUDIT rubric edits (13 criteria, all widening accept-sets)
and a fresh platform regrade at 16:18 / 16:19 on the SAME trajectories. New `8a` (28/33/43/31/32/37) and `8b`
(20/19/22/17/16/18) supersede the exports the 13:42 verdict was built on. Prior reports archived to
`_aux/Council_Reports/_superseded/pass3_2026-07-26_1342/`.

- [x] 0. Phase-readiness gate (`phase_ready.py --phase s4`) - 5/5 upstream artifacts present, exit 0
- [x] 0b. `parse_trajectories.py` - 12/12 runs parsed; per-run tool counts identical to pass 3, confirming trajectories unchanged
- [x] 0c. Input delta established - rubric diff vs `7_Rubrics.pre_audit_fixes.json` (13 criteria: 8 titles, 11 evidence, 3 justifications, all widening); verifier per-run score delta computed
- [x] 0d. Step 0 TODO list (this file)
- [x] 0.5a. T3 Error Rate gate - 0/6 errored per model, PASS both
- [x] 0.5b. T2 pass@1 gate - Opus 0/6 = 0.0% PASS; Gemini 0/6 = 0.0% PASS
- [x] 0.5c. T1 Density gate - Opus 62.5, Gemini 79.8 against the V4 40+ target, PASS both
- [x] 1. Rubric x run matrix rebuilt from the new exports - 720/720 decisions matched by title, 0 unmatched, 0 duplicate titles
- [x] 2. Cell-level diff vs pass 3 - 74 cells moved (28 Fail to Pass, 46 Pass to Fail); 12 attributable to the 13 text edits, 62 grader variance on unchanged text
- [x] 3. Trajectory walk - Opus, all 50 failing criteria; write payloads and final-response text extracted per run, every moved cell re-walked
- [x] 4. Trajectory walk - Gemini, all 50 failing criteria; same treatment
- [x] 5. Linear uuid to identifier map built from tool results across all 12 runs (257 uuids resolved) so comment targets given by internal id could be checked
- [x] 6. Bucket classification - union of 50 failing criteria: **B1 = 0, B2 = 0 at criterion level, B3 = 50**
- [x] 7. Contested run-cells identified and evidenced - 21 of 404 fail cells (5.2%), across criteria 22, 28, 32, 36, 43, 45, 46, 48, 55, 56, 58, 59
- [x] 8. 5-point pre-write checklist before every justification - 34 of 34 returned YES on all five
- [x] 9. Bucket calls re-confirmed against `_aux/Universe_Split/` (Linear states by id, Slack ts to exact text, returned identifiers read from tool results)
- [x] 10. All-Failing Rubrics sub-dim - Bucket 1 ratio 0.0% on all four bases, score **5/5**
- [x] 11. `_aux/Council_Reports/S4_fixes.md` - 0 open Bucket 1 entries; 14:42 widening verified as landed and measurable; 3 watch items recorded
- [x] 12. `_aux/Council_Reports/S4_judge_errors.md` - 21 contested cells in 3 groups, 18 recommended for appeal, plus 10 cells checked and found genuine
- [x] 13. `_aux/Council_Reports/S4_AF_justifications.md` - 34 all-failing criteria (6 both models, 28 Gemini-only)
- [x] 14. `check_justification.py` exit 0 on the AF batch; 0 em-dashes across all four S4 reports
- [x] 15. Hardness calibration - 3 confirmed / 1 falsified, unchanged by the regrade; new note on the measurable effect of the evidence widening
- [x] 16. Appended to `Tasks/_meta/Stump_Hypotheses.md` (pass-4 entry, supersedes prior entries)
- [x] 17. Appended to `Tasks/_meta/Hardness_Patterns_Log.md` (pass-4 regrade block)
- [x] 18. Appended to `Tasks/_meta/Learnings.md` (L34 accept-set widening recovers agent work; L35 grader variance is unstable in direction)
- [x] 19. `_aux/Verification_s4.md` rewritten for pass 4
- [x] 20. `_aux/Council_Reports/S4_verdict.md` rewritten for pass 4
- [x] 21. `check_regression.py` - PASS
- [x] 22. QC 5/5 fix pass: 3 Bucket 1 defects fixed in place (criteria 6, 58, 59), criterion 33 hardened, OE 29 mirrored. Snapshots at `_aux/7_Rubrics.pre_qc5_fixes.json` and `_aux/6_Oracle_Events.pre_qc5_fixes.txt`
- [x] 23. Every edited criterion re-graded by hand against all 12 trajectories: 2 widenings flip only satisfied cells, 1 tightening corrects 4 wrongly-passing cells, 0 legitimate fails flipped
- [x] 24. Validator re-run after the edits: PASS on prompt, oe, rubrics, all, submission_gate, injection
- [x] 25. S4 verdict, fixes, judge-errors, AF and verification reports all updated for the post-fix state

**Phase status: COMPLETE.** Both models classified against the current grading and the current rubric text.
Three Bucket 1 fixes applied in place, set held at 60 criteria. No REDO.
