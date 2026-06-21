# PIPELINE NEW — Fresh Task Folder Setup

**Trigger:** `PIPELINE NEW — <TASK_ID>`

Two accepted forms:
- `PIPELINE NEW — 6a35abc123def...` (auto-picks next available index)
- `PIPELINE NEW — 25_6a35abc123def...` (uses given index)

## What this phase does

Single command, single chat. Eliminates the manual folder-creation chore at the start of every task.

1. Creates `Tasks/<index>_<task_id>/`.
2. Scaffolds the 3 user-pasted input files as empty placeholders.
3. Creates `Agent_Responses/` and `trajectory-runs/` for later trajectory paste-back.
4. Refuses if the folder already exists (no silent overwrites).
5. Prints exact paste instructions + next-trigger nudge.

## Required inputs

| File | Source |
|---|---|
| (nothing — entry-point phase) | The trigger phrase is enough. |

## Procedure

1. Run:
   ```
   python Validators/new_task.py <task_id_or_full_name>
   ```
2. The script prints the absolute paths for the 3 files to paste + the next-trigger phrase.

## STOP gate

This phase ends here after the folder is scaffolded. End your response. The user pastes the 3 input files into the folder, then invokes:

```
PIPELINE S0 - Tasks/<TASK_DIR>
```

in a fresh chat. Do NOT proceed to S0 in this chat — the user controls the paste step.

## Bootstrap

Read root `AGENTS.md` first. This is the entry-point trigger for any new task; `PIPELINE NEW` lives BEFORE `PIPELINE S0` in the workflow.
