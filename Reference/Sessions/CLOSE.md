# PIPELINE CLOSE — Wrap Up a Finished Task

**Trigger:** `PIPELINE CLOSE — Tasks/<TASK_DIR>`

## What this phase does

Final sanity check before declaring a task done. Read-only — does NOT modify, move, or delete files. Refuses to greenlight if any required artifact is missing or the FINAL/trajectory verdicts aren't OK.

Auto-detects flow (CB or REVIEW) from the artifacts present:
- **CB flow**: requires `1/2/3/5/6/7` populated + FINAL council = PASS + (if trajectories) `Trajectory_Stats.json` verdict = OK.
- **REVIEW flow**: same as CB + `changes.md` + `13_Feedback.txt` populated. 14/15 optional (only emitted when Applied rows existed).

## Required inputs

| File | Source |
|---|---|
| Whatever the task has built so far | the script audits what's there |

## Phase-readiness gate

None needed — CLOSE is a read-only audit. It tells you what's missing instead of refusing to run.

## Procedure

1. **Verify tool catalog version-pin (v19).** Confirm the pinned tool catalogs (Brookfield, KeyStone, MoveOps, StarPM) haven't drifted upstream:
   ```
   python Validators/check_tool_catalog.py
   ```
   All pinned universes should report `[OK] <universe>: catalog hash matches`. DRIFT = upstream tool catalog changed since last pinned hash; before greenlight, re-run validate.py + verify_universe_atoms.py on the corrected set, then `python Validators/check_tool_catalog.py --update` to re-pin.

2. Run:
   ```
   python Validators/close_task.py Tasks/<TASK_DIR>
   ```
2. The script prints the per-artifact checklist + flow detection + FINAL verdict + trajectory verdict + READY/NOT-READY conclusion.
3. If READY: read the recommended next actions and append any novel finding to `Tasks/_meta/Learnings.md` before closing the chat. Also confirm the cross-task logs (Linter_Justifications, Similarity_Log, Hardness_Patterns_Log, Stump_Hypotheses) reflect anything this task surfaced.
4. If NOT READY: fix the items the script listed before re-running CLOSE.

## STOP gate

This phase ends here. End your response.

Three next-trigger paths:
- READY + you appended any cross-task learnings → EXIT (task is done).
- NOT READY because a required artifact is missing → run the upstream phase first (`PIPELINE S0`, S1, S2, S3, FINAL, S4, or REVIEW depending on what's missing), then re-invoke `PIPELINE CLOSE`.
- NOT READY because FINAL says REVISE or trajectory verdict is REBUILD_CANDIDATE → run `PIPELINE FINAL` (iterate) or `PIPELINE REDO` (full rebuild) per the script's output.

Do NOT modify the task contents in this chat.

## Bootstrap

Read root `AGENTS.md` first. CLOSE is the final trigger in the workflow; nothing runs after it for a given task version.

## HarmonyGames (`hg`) artifact set

HG tasks live under `Generated_Tasks/`. The expected set is the V3-family one: `1`, `2`, `3`
(a pointer), `4_Changelog.json`, `5`, `6`, `7`, `8_Verifier_Fails.txt`, `9_Universe_inject.sql`,
and flat `Agent_Responses/trajectory-run-{1..6}.json`. There is no `8a`/`8b` split and no
per-model trajectory subdirectory — that is StarPM's shape, not this one.

`check_tool_catalog.py` pins five catalogs now; HarmonyGames' is
`HarmonyGames_Base_Universe/5_Server_Tools_Details.json` (prefix **5**).
