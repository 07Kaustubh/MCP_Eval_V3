# Todos — PIPELINE S4 (2_6a6beba55996ad2ada369b15)

Started 2026-08-07.

| # | Step | Status |
|---|---|---|
| 1 | Normalize S4 input filenames (`8_Verifier_fails.txt` -> `8_Verifier_Fails.txt`, `trajectory-run-N (2).json` -> `trajectory-run-N.json`) | completed |
| 2 | `phase_ready.py --phase s4` | completed |
| 3 | `parse_trajectories.py` -> Trajectory_Stats.json | completed |
| 4 | `check_export_freshness.py --pin` (PIN FIRST, before any classification) | completed |
| 5 | `check_criterion_dependencies.py` (step 1b passing-cell audit) | completed |
| 6 | `check_oe_rubric_sync.py` at entry | completed |
| 7 | Write `_aux/Reads_s4.md` (E2 compliance gate) | completed |
| 8 | Read required inputs: 5_Prompt, 6_Oracle_Events, 7_Rubrics, Hardness_Plan, Docs_harmonygames/9_Common_Error, 11_Taxonomy, 12_Always_Failing_Rubrics, Evals_harmonygames/4 | completed |
| 9 | Procedure 0.5 — T3 error-rate gate | completed |
| 10 | Procedure 0.5 — T2 agent-failure-rate gate (pass@1 <= 40%) | completed |
| 11 | Procedure 1 — build rubric x run matrix from 8_Verifier_Fails.txt, keyed by TITLE | completed |
| 12 | Procedure 1b — audit passing cells (dependency hits) | completed |
| 13 | Procedure 2 — trajectory walk for EVERY failing rubric, all 6 runs, before classifying | completed |
| 14 | Classify each failing rubric into Bucket 1 / 1b / 2 / 3 with trajectory citations | completed |
| 15 | Bucket 3: apply 5-point pre-write checklist; argue removal first (AGENTS.md rule 21) | completed |
| 16 | Write `_aux/Council_Reports/S4_fixes.md` (Bucket 1) | completed |
| 17 | Write `_aux/Council_Reports/S4_judge_errors.md` (Bucket 2) | completed |
| 18 | Write `_aux/Council_Reports/S4_AF_justifications.md` (Bucket 3) | completed |
| 19 | Procedure 3 — re-confirm every Bucket 1/2 call against the universe source of truth | completed |
| 20 | Procedure 4 — Hardness_Plan calibration; update `Tasks/_meta/Stump_Hypotheses.md` + `Hardness_Patterns_Log.md` | completed |
| 21 | Compute Bucket 1 ratio; score All-Failing Rubrics sub-dim | completed |
| 22 | `check_justification.py` exit 0 on AF batch | completed |
| 23 | Write `_aux/Council_Reports/S4_verdict.md` (matrix + classifications + gates) | completed |
| 24 | Write `_aux/Verification_s4.md` cross-source check | completed |
| 25 | Exit gates: `check_export_freshness.py` (bare), `check_criterion_dependencies.py`, `check_oe_rubric_sync.py`, `check_rubric_antipatterns.py` | completed |
| 26 | STOP — report to user, do not loop S4 in this chat | completed |

## Second-pass verification (operator asked for a double-check)

| # | Step | Status |
|---|---|---|
| 27 | Falsify the storage-vs-serialization rounding hypothesis | completed — serialization predicts 7483, tool returns 7476 |
| 28 | Predict 12 aggregates from the storage model, then compare to trajectories | completed — 12/12 matched |
| 29 | Search for any alternative reachable path to the exact cents | completed — none; the Slack/Gmail grep hits are timestamp substrings |
| 30 | Test whether #executives is ACL-blocked (would change criterion 10's class) | completed — channel and its messages are served; not blocked |
| 31 | Confirm the collision source on all six runs | completed — all six queried MONTHLY_BURN and received legal = 13000 |
| 32 | Re-test criteria 12/16/24 for grader non-determinism | completed — directions genuinely differ, not a coin-flip |
| 33 | Reconcile matrix to export and re-derive corrected pass@1 | completed — 16/20/22/18/16/17 exact, corrected pass@1 1/6 |
| 34 | Audit my own paired-OE list for completeness | completed — found 2 omissions (OE 22 line 43, OE 28 line 55), fixed |

## Fix application (operator instruction, overriding the phase STOP gate)

| # | Step | Status |
|---|---|---|
| 35 | Archive pre-fix `7_Rubrics.json`, `6_Oracle_Events.txt` and the classification pin | completed |
| 36 | Apply the six rubric edits (criteria 4, 6, 10, 11, 17, 20) | completed |
| 37 | Apply the paired OE edits (OE 8, 10, 11, 19, 22, 24, 25, 26, 27, 28) | completed |
| 38 | Clear `check_rubric_antipatterns` MODERATE on `FAIL only if` (criteria 4, 10) | completed — rewritten additively |
| 39 | Clear `validate.py` warns introduced by my own wording (criterion 6, OE 24) | completed — 0 fails, 0 warns on both phases |
| 40 | Re-run every exit gate | completed — all clean |
| 41 | Re-pin the export and record the pin history | completed |
| 42 | Update `S4_fixes.md`, `S4_verdict.md`, `Verification_s4.md` to APPLIED state | completed |

---

# Pass 2 — 2026-08-07, re-invoked after the fixed rubrics were re-graded

New export `ad0260ca6682ad47…` 55,564 B, per-run [17, 19, 21, 20, 19, 22]. Pass-1 reports archived to
`_aux/Council_Reports/_superseded/pass1_2026-08-07/` before anything was rewritten.

| # | Step | Status |
|---|---|---|
| 1 | `phase_ready.py --phase s4` — read the DRIFT warning, treat every pass-1 count as superseded | completed |
| 2 | `parse_trajectories.py` -> Trajectory_Stats.json (re-derived, not carried forward) | completed |
| 3 | `check_export_freshness.py --pin` on the NEW bytes, before any classification | completed |
| 4 | `check_criterion_dependencies.py` (step 1b) | completed |
| 5 | `check_oe_rubric_sync.py` + `check_rubric_antipatterns.py` at entry | completed |
| 6 | Archive pass-1 reports to `_superseded/pass1_2026-08-07/` | completed |
| 7 | Rebuild the rubric x run matrix from the new export, keyed by TITLE | completed |
| 8 | Reconcile matrix per-run totals against the export and the pin | completed |
| 9 | Procedure 0.5 — T3 error-rate gate | completed |
| 10 | Procedure 0.5 — T2 agent-failure-rate gate | completed |
| 11 | Procedure 1b — manual passing-cell audit beyond the dependency checker | completed |
| 12 | Trajectory walk for all 12 failing criteria, all 6 runs, before classifying | completed |
| 13 | Re-verify the wind-down provider grounding in the universe first-hand | completed |
| 14 | Establish whether any run reached, or could have reached, that grounding | completed |
| 15 | Classify every failing criterion into a bucket with trajectory citations | completed |
| 16 | Rule 21 removal argument for both all-failing criteria, before writing prose | completed |
| 17 | 5-point pre-write checklist on both all-failing criteria | completed |
| 18 | Write `S4_fixes.md` (pass 2) | completed |
| 19 | Write `S4_judge_errors.md` (pass 2) | completed |
| 20 | Write `S4_AF_justifications.md` (pass 2) | completed |
| 21 | `check_justification.py` exit 0 on the AF batch | completed |
| 22 | Bucket 1 ratio + All-Failing Rubrics sub-dim score | completed |
| 23 | Hardness calibration; update `Stump_Hypotheses.md` + `Hardness_Patterns_Log.md` | completed |
| 24 | Write `S4_verdict.md` (pass 2) | completed |
| 25 | Write `_aux/Verification_s4.md` (pass 2) | completed |
| 26 | Exit gates: freshness (bare), dependencies, oe_rubric_sync, antipatterns | completed |
| 27 | STOP — report, do not loop S4 in this chat | completed |
