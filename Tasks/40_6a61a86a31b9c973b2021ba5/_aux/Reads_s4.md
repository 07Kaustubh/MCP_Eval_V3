# Reads — S4

## Inputs consulted
- `Reference/Sessions/S4.md` — runbook
- `Reference/AGENTS.md` — root pipeline rules (rule 11: density tiers)
- `_aux/Universe.txt` = `starpm` → V4 dual-model routing
- `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` (49 rubrics)
- `8a_Verifier_Fails_Opus.txt`, `8b_Verifier_Fails_Gemini.txt`
- `Agent_Responses/Opus/Run{1..6}_Trajectory.json` (renamed from `trajectory-run-N (3).json`)
- `Agent_Responses/Gemini/Run{1..6}_Trajectory.json` (renamed from `trajectory-run-N (4).json`)
- `_aux/Hardness_Plan.md` (referenced; calibration deferred to REDO)

## Notes
- `Validators/parse_trajectories.py` does not yet support V4 dual-model subfolders or the 8a/8b verifier-fails split — used an ad-hoc runner (`/tmp/s4_40/parse.py`) reusing the exact same counting logic and writing `_aux/Trajectory_Stats_Opus.json` + `_aux/Trajectory_Stats_Gemini.json` per the runbook's target paths. Flag noted in verdict for pipeline-maintenance follow-up (add `--model` flag to the shared script).
- `Validators/phase_ready.py` does not yet support the `--universe starpm` flag or the `8a`/`8b` files as substitutes for `8_Verifier_Fails.txt`. Manual verification confirmed all required V4 inputs are present.
