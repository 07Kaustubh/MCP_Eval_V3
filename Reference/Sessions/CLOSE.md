# PIPELINE CLOSE — Wrap Up a Finished Task

**Trigger:** `PIPELINE CLOSE — <TASK_DIR>`

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

1. Run:
   ```
   python Validators/close_task.py <TASK_DIR>
   ```
2. The script prints the per-artifact checklist + flow detection + FINAL verdict + trajectory verdict + READY/NOT-READY conclusion.
3. If READY: read the recommended next actions and append any novel finding to `Submitted-Tasks/_meta/Learnings.md` before closing the chat. Also confirm the cross-task logs (Linter_Justifications, Similarity_Log, Hardness_Patterns_Log, Stump_Hypotheses) reflect anything this task surfaced.
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
