# Agent_Responses/Gemini — Per-Run Trajectories (Gemini Model)

One trajectory file per successful run (`Run1_Trajectory.json` … `Run6_Trajectory.json`).

Used by the Verifier Fails eval (`Evals_starpm/4_Verifier_Fails_Eval.md`) under the Gemini model column.

## How to export

1. Open the agent run environment, select the **Gemini** model run.
2. Click the run in the sidebar (e.g., "Run #1").
3. Click **"Trajectory"** to download the JSON.
4. Paste its contents into the matching `RunN_Trajectory.json`.
5. Repeat for all 6 runs.

## Empty file

An empty run file = the agent errored on that run (no trajectory). That run is out of evaluation.

> **Note:** This subfolder is for StarPM (V4) tasks only. V3 universe tasks (Brookfield, Keystone, MoveOps) use the flat `Agent_Responses/Run*.json` layout in the parent directory.
