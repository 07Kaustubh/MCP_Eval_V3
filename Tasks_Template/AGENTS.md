# Tasks_Template

Empty scaffold for a new task folder. Copy into `Tasks/<TASK_DIR>/` when starting a new task — but the pipeline runbooks will populate `_aux/` and the deliverable files automatically, so most operators don't need to interact with this template directly.

## Files

| File | What goes in it |
|---|---|
| `1_Business_Function.txt` | One-line business function name (e.g., "Accounting Services") |
| `2_Persona.txt` | One-line persona name + role (e.g., "George McAdam - Accounts Senior") |
| `3_UniverseDataForThisTask.json` | The per-task pgweb export. SINGLE SOURCE OF TRUTH for universe facts. |
| `4_Changelog.json` | Optional, scripted-scenario changelog if used by the platform |
| `5_Prompt.txt` | The prompt (S1 produces) |
| `6_Oracle_Events.txt` | The OEs (S2 produces) |
| `7_Rubrics.json` | The rubrics (S3 produces) |
| `8_Verifier_Fails.txt` | Verifier output after agent runs (user pastes from platform, S4 consumes) |
| `9_Universe_inject.sql` | Optional, SQL to recreate the universe state |
| `Agent_Responses/Run{1..6}_Trajectory.json` | Trajectory exports from the 6 final Opus runs |

## Templates that matter

- `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` in this template are deliberately empty / minimal — the pipeline writes them.
- `Agent_Responses/README.md` describes the trajectory export format.

## What the pipeline adds

Once `PIPELINE S0` runs on a task folder, the pipeline creates `_aux/Universe_Split/`, `_aux/Universe_Index/`, and `_aux/S0_Setup_Report.md`. These are NOT in the template — they are per-task working state.

## When to update this template

When the platform adds a new required deliverable file. Otherwise this is stable.
