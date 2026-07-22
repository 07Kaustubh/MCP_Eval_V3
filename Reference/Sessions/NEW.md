# PIPELINE NEW — Fresh Task Folder Setup

**Trigger (CB mode):**       `PIPELINE NEW — <TASK_ID>`
**Trigger (Review mode):**   `PIPELINE NEW REVIEW — <TASK_ID>`

`<TASK_ID>` is one of:
- `6a35abc123def...` — bare hex; auto-picks next available index
- `25_6a35abc123def...` — given index

## What this phase does

Single command, single chat. Eliminates the manual folder-creation chore at the start of every task.

1. Creates `Tasks/<index>_<task_id>/`.
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

- **CB mode**: `PIPELINE S0 — Tasks/<TASK_DIR>` in a fresh chat.
- **Review mode**: `PIPELINE REVIEW — Tasks/<TASK_DIR>` in a fresh chat.

Do NOT proceed to the next phase in this chat — the user controls the paste step.

## Bootstrap

Read root `AGENTS.md` first. This is the entry-point trigger for any new task; `PIPELINE NEW` lives BEFORE `PIPELINE S0` in the workflow.

## V4 (StarPM) scaffolding

For a StarPM task, pass the universe explicitly - the scaffolder produces the V4 dual-model shape from `Tasks_Template_starpm/`:

```
python Validators/new_task.py <task_id_or_full_name> --universe starpm            # V4 CB mode
python Validators/new_task.py <task_id_or_full_name> --universe starpm --review  # V4 review mode
```

V4 shape adds over V3: `4_Changelog.json`, `8a_Verifier_Fails_Opus.txt`, `8b_Verifier_Fails_Gemini.txt`, `9_Universe_inject.sql`, `Agent_Responses/{Opus,Gemini}/Run1-6_Trajectory.json`, and the QC dispute placeholders `9_QC_Feedback.txt` / `10_PT_Dispute_To_QC_Feedback.txt` / `11_Final_QC_Validation_On_PT_Dispute.txt`. Injection (`9_Universe_inject.sql` + `4_Changelog.json`) is a FIRST-CLASS authoring artifact in V4: it is designed during task build and gated by `validate.py --phase injection` (Evals_starpm/0) at S0 re-run and FINAL.
