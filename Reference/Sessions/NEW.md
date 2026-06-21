# PIPELINE NEW — Fresh Task Folder Setup

**Trigger (CB mode):**       `PIPELINE NEW — <TASK_ID>`
**Trigger (Review mode):**   `PIPELINE NEW REVIEW — <TASK_ID>`

`<TASK_ID>` is one of:
- `6a35abc123def...` — bare hex; auto-picks next available index
- `25_6a35abc123def...` — given index

## What this phase does

Single command, single chat. Eliminates the manual folder-creation chore at the start of every task.

1. Creates `<index>_<task_id>/`.
2. Scaffolds the input files as empty placeholders:
   - **CB mode**: 1, 2, 3 (3 files — business function, persona, universe data)
   - **Review mode**: 1, 2, 3, 5, 6, 7, 8 (7 files — adds candidate-prefilled prompt + OE + rubrics + verifier-fails)
3. Creates `Agent_Responses/` and `trajectory-runs/` for later trajectory paste-back.
4. Refuses if the folder already exists (no silent overwrites).
5. Prints exact paste paths + next-trigger nudge (`PIPELINE S0` for CB; `PIPELINE REVIEW` for review).

## Required inputs

| File | Source |
|---|---|
| (nothing — entry-point phase) | The trigger phrase is enough. |

## Procedure

1. Run one of:
   ```
   python Validators/new_task.py <task_id_or_full_name>            # CB mode (3 files)
   python Validators/new_task.py <task_id_or_full_name> --review   # Review mode (7 files + trajectory drop point)
   ```
2. The script prints the absolute paths for each file to paste + the next-trigger phrase (`PIPELINE S0` for CB, `PIPELINE REVIEW` for review).

## STOP gate

This phase ends here after the folder is scaffolded. End your response. The user pastes the required files into the folder, then invokes the next trigger per mode:

- **CB mode**: `PIPELINE S0 — <TASK_DIR>` in a fresh chat.
- **Review mode**: `PIPELINE REVIEW — <TASK_DIR>` in a fresh chat.

Do NOT proceed to the next phase in this chat — the user controls the paste step.

## Bootstrap

Read root `AGENTS.md` first. This is the entry-point trigger for any new task; `PIPELINE NEW` lives BEFORE `PIPELINE S0` in the workflow.
