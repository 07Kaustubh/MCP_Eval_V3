# S4 Todos - Task 40_6a614767cd5b60ad96902fb4 (StarPM V4, dual-model)

- [x] Bootstrap: read S4 runbook + AGENTS.md; run phase_ready + parse_trajectories
- [x] Blocker fix 1: parse_trajectories.py Gemini flat-format tool_use counting (additive; regression 62/62 / 21/21 / 7/7 PASS)
- [x] Blocker fix 2: Verification_final.md conformance -> phase_ready s4 EXIT 0
- [x] Create Reads_s4.md (v11 E2 gate)
- [x] Load core artifacts: 5_Prompt, 6_Oracle_Events, 7_Rubrics, Hardness_Plan, universe today
- [x] T3 Error-Rate gate per model (Opus 0/6, Gemini 0/6 errored < 3)
- [x] T2 Agent-Failure-Rate gate per model (Opus 0%, Gemini 0% pass@1 <= 40%)
- [x] Build rubric x run matrix - Opus (8a)
- [x] Build rubric x run matrix - Gemini (8b)
- [x] Walk trajectories for EVERY failing rubric - Opus (R1,R5,R8,R10,R12,R13,R15,R16)
- [x] Walk trajectories for EVERY failing rubric - Gemini (R8,R10,R12,R13)
- [x] Classify each failing rubric into Bucket 1/2/3 - Opus (5-point checklist before any AF)
- [x] Classify each failing rubric into Bucket 1/2/3 - Gemini (5-point checklist before any AF)
- [x] All-Failing-Rubrics sub-dim: Bucket-1 ratio + score per model (Opus 0/1, Gemini 0/2 -> 5/5)
- [x] Re-grep universe to confirm every classification value (R1 recs, R10 QR-2026-0441, R13 ESA)
- [x] Update Hardness_Plan calibration vs actual AF rubrics (in S4_verdict.md)
- [x] Write S4_AF_justifications.md / S4_judge_errors.md / S4_fixes.md (per model, buckets)
- [x] check_justification.py exit 0 on AF batch
- [x] Write S4_verdict.md (matrix + classifications + T2/T3 + All-Failing score + calibration + actions)
- [x] Write Verification_s4.md (check_verification.py --phase s4 EXIT 0)
- [x] Update Tasks/_meta/Stump_Hypotheses.md + Hardness_Patterns_Log.md + Learnings.md

## Correction pass (v2) - skeptical re-verification (2026-07-23)
- [x] Full read of 8a + 8b (all runs), not just the programmatic matrix
- [x] Per-rubric tool_use/tool_result walk on all 12 trajectories
- [x] Tool-catalog reachability check for R10 (search_bills/get-bill exist)
- [x] Corrected R10 Opus AF justification (surfaced-but-unused, not "never opened")
- [x] Corrected R13 Gemini AF justification (surfaced-but-omitted, not "did not query")
- [x] Re-classified R12 Bucket 3 -> Bucket 1 (non-atomic + judge inconsistency); wrote split fix
- [x] Re-ran voice gate (0 hits) + check_verification (EXIT 0)
- [x] Updated S4_verdict.md, S4_fixes.md, S4_judge_errors.md, Verification_s4.md, Learnings.md


## Post-split re-verify pass (v3) - new Opus 8a on the 17-rubric split (2026-07-23)
- [x] Detect input-version mismatch: 8a Opus = 17-criterion split (mtime 21:56, post-split); 8b Gemini = 16-criterion combined (mtime 19:22, pre-split)
- [x] Re-run phase_ready s4 (EXIT 0) + parse_trajectories (pass@1 0% both, density 40.8, 0 errors)
- [x] Rebuild Opus rubric x run matrix from the NEW 17-criterion 8a
- [x] Confirm 7_Rubrics.json R12a/R12b text == Opus-graded 8a criterion text (no rubric drift)
- [x] Validate the R12 split on Opus: R12a 6/6 pass; R12b atomic, fail run 1 only; EVF-id inconsistency eliminated (old run 5 combined-fail now passes both halves)
- [x] Log R12b Opus run-1 as Bucket 3 partial; scope R12 Bucket-1 to the stale Gemini 8b
- [x] Confirm OPS-32 R15/R16 individually (both pass runs 1-4, fail 5,6) - unchanged Bucket 3
- [x] Update S4_verdict.md / S4_fixes.md / S4_judge_errors.md / Verification_s4.md for the post-split state
- [x] Re-run gates: voice gate 0 hits, check_verification --phase s4 EXIT 0, validate --phase all PASS
- [x] Append the rubric-atomicity calibration to Learnings + Hardness_Patterns_Log
- [x] Record the one open action: platform re-verify Gemini on the 17-rubric split set

## Gemini re-verify closure pass (v4) - post-split Gemini 8b arrived (2026-07-23)
- [x] Detect new 8b (mtime 22:31) = post-split 17-criterion Gemini re-verify (the v3 pending action)
- [x] Re-run phase_ready s4 (EXIT 0) + parse_trajectories (pass@1 0% both, density 40.8, 0 errors)
- [x] Confirm 8b is a RE-GRADE of the same Gemini trajectories (tool-call counts 47/45/37/38/33/40 unchanged), not a fresh run
- [x] Rebuild Gemini matrix from the NEW 17-criterion 8b: R12a 6/6 pass + R12b 6/6 pass; R8 partial (run 5); R10 + R13 AF unchanged
- [x] Correct Opus pass/run counts in S4_verdict (runs 5,6 are 12/17 each - prior verdict had a 10/11 typo)
- [x] R12 split VALIDATED on BOTH models; retire the stale combined-R12 8b caveat + the one pending platform action
- [x] AF batch unchanged (R10 Opus, R10 Gemini, R13 Gemini still 6/6); re-run voice gate (0 hits)
- [x] Update S4_verdict / S4_fixes / S4_judge_errors / Verification_s4 for the dual-model-validated state
- [x] Re-run check_verification --phase s4 (EXIT 0)
- [x] Append the dual-model closure to Learnings + Hardness_Patterns_Log + Stump_Hypotheses