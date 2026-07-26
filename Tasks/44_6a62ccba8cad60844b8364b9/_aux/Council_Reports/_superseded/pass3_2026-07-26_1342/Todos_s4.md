# S4 TODOs — Task 44 (`44_6a62ccba8cad60844b8364b9`) · StarPM V4, dual-model · PASS 3

Re-invocation after the 12:58 evidence clarifications (criteria 11, 22, 23, 24, 34, 48) and a platform
re-grade of the SAME trajectories. New `8a` (34/33/44/26/30/46) and `8b` (20/19/22/19/20/21) supersede
the exports the 12:45 verdict was built on. Prior reports archived to
`_aux/Council_Reports/_superseded/pass2_2026-07-26_1245/`.

- [x] 0. Phase-readiness gate (`phase_ready.py --phase s4`) — 5/5 upstream artifacts present, exit 0
- [x] 0b. `parse_trajectories.py` — 12/12 runs parsed; counts identical to pass 2, confirming trajectories unchanged
- [x] 0c. Input delta established — rubric diff vs `7_Rubrics.pre_s4_b1fix.json` (6 evidence fields, 0 titles); verifier per-run score delta computed
- [x] 0d. Step 0 TODO list (this file)
- [x] 0.5a. T3 Error Rate gate — 0/6 errored per model, PASS both
- [x] 0.5b. T2 pass@1 gate — Opus 0/6 = 0.0% PASS; Gemini 0/6 = 0.0% PASS
- [x] 0.5c. T1 Density gate — Opus 62.5, Gemini 79.8 against the V4 40+ target, PASS both
- [x] 1. Rubric x run matrix rebuilt from the new exports — 720/720 decisions matched by title, 0 unmatched
- [x] 2. Cell-level diff vs pass 2 — 67 cells moved (42 Fail to Pass, 25 Pass to Fail); 6 attributable to the evidence edits, 61 grader variance
- [x] 3. Trajectory walk — Opus, all 41 failing criteria; every newly-failing cell re-walked against the write payload
- [x] 4. Trajectory walk — Gemini, all 46 failing criteria; every newly-failing cell re-walked against the final-response text
- [x] 5. Bucket classification — union of 48 failing criteria: **B1 = 0, B2 = 0 at criterion level, B3 = 48**
- [x] 6. Contested run-cells identified and evidenced — 10 of 386 fail cells (2.6%), across criteria 6, 18, 34, 52, 58, 59
- [x] 7. 5-point pre-write checklist before every justification — 33 of 33 returned YES on all five
- [x] 8. Bucket calls re-confirmed against `_aux/Universe_Split/` (Linear states by id, Slack ts to exact text, returned issue identifiers read from tool results)
- [x] 9. All-Failing Rubrics sub-dim — Bucket 1 ratio 0.0% on all four bases, score **5/5**
- [x] 10. `_aux/Council_Reports/S4_fixes.md` — 0 open Bucket 1 entries; pass-2 fix verified landed; criterion 5 recorded as a watch item
- [x] 11. `_aux/Council_Reports/S4_judge_errors.md` — 10 contested cells, plus 8 cells checked and found genuine
- [x] 12. `_aux/Council_Reports/S4_AF_justifications.md` — 33 all-failing criteria (8 both models, 25 Gemini-only)
- [x] 13. `check_justification.py` exit 0 on the AF batch; 0 em-dashes across all four S4 reports
- [x] 14. Hardness calibration — 2 confirmed / 1 split / 1 falsified, unchanged by the regrade; prediction 4 mechanism sharpened
- [x] 15. Appended to `Tasks/_meta/Stump_Hypotheses.md` (pass-3 entry, supersedes both prior entries)
- [x] 16. Appended to `Tasks/_meta/Hardness_Patterns_Log.md` (pass-3 regrade block)
- [x] 17. Appended to `Tasks/_meta/Learnings.md` (L33, grader non-determinism)
- [x] 18. `_aux/Verification_s4.md` rewritten for pass 3
- [x] 19. `_aux/Council_Reports/S4_verdict.md` rewritten for pass 3
- [x] 20. `check_regression.py` — PASS, anchors 62/62, reports 21/21, verdicts 7/7

**Phase status: COMPLETE.** Both models classified against the current grading. No Bucket 1 fixes. No REDO.
