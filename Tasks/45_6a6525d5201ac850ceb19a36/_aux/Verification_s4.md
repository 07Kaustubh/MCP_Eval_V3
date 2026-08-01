# S4 Cross-Source Verification — Task 45 (StarPM V4)

## Data sources consulted
- 7_Rubrics.json :: 20-criterion rubric set being classified (pinned sha fa2912c664d0e2db)
- 8a_Verifier_Fails_Opus.txt :: Opus verifier output, 6 runs, all 20/20 (pinned sha 1526b9dbae6095e3)
- 8b_Verifier_Fails_Gemini.txt :: Gemini verifier output, 6 runs [18,14,20,15,20,20] (pinned sha 4bb5dc1d09b83fc7)
- Agent_Responses/Opus/Run*.json + Agent_Responses/Gemini/Run*.json :: 12 trajectories, 12/12 parsed ok, 0 errors
- _aux/Trajectory_Stats.json :: machine metrics (per-model pass@1 + density)
- _aux/Hardness_Plan.md :: stump hypothesis to calibrate against
- 5_Prompt.txt :: read line-by-line to locate the root cause of the too-easy outcome

## Eval spec verified
- Evals_starpm/4 (dual-model, run once per model) :: applied per-model pass@1
- S4 Procedure 0.5 T2/T3 hard gates :: evaluated BEFORE classification
- AGENTS.md rule 11 (per-model density) + Hardness_Plan mitigation #2 :: applied

## QC spec sub-dims verified
- Trajectory T3 Error Rate: 0/12 errored -> PASS
- Trajectory T2 Agent Failure Rate: Opus 100%, Gemini 50%, overall 75% -> FAIL (per model, both fail > 40%)
- Trajectory T1 density: Opus 37.0 THIN (<40 design, >15 floor), Gemini 43.3 PASS
- All-Failing Rubrics sub-dim: empty AF set (not dispositive; T2 fail is dispositive)

## Verification statements
- [x] T2 + T3 hard gates evaluated and recorded FIRST, before any bucket classification.
- [x] Machine verdict REBUILD_CANDIDATE_DIFFICULTY reproduced by hand arithmetic (9/12 = 0.75).
- [x] Run matrix built for all 20 rubrics x 12 cells; every Gemini fail traced to its run/criterion.
- [x] Passing-cell audit (check_criterion_dependencies.py) exit 0 — no dependent passed where antecedent failed.
- [x] Anti-pattern scan (check_rubric_antipatterns.py) exit 0.
- [x] No AF justifications authored (Bucket 3 empty) — voice gate correctly skipped.
- [x] Root cause identified and grounded in 5_Prompt.txt: prompt names every rubric discriminator.
- [x] Input pin re-verified at exit (rule 15).
- [x] No rubric edits made this pass, so check_oe_rubric_sync / anti-pattern re-run not required post-edit.

## Discrepancies surfaced
- None between the pasted verifier text and the parsed trajectories (per-run pass counts match the pin exactly).
- The task FAILS the T2 difficulty gate on both models. This is a hard STOP to PIPELINE REDO; S4 classification cannot save a too-easy task. The rubric set itself graded cleanly (0 Bucket-1, 0 Bucket-2) — the defect is prompt information content, not the rubrics.
