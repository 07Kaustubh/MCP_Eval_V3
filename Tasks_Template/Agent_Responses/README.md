# Agent_Responses — Per-Run Trajectories

One trajectory file per successful run (`Run1_Trajectory.json` … `Run6_Trajectory.json`), used by the Verifier Fails eval (`Evals/4_Verifier_Fails_Eval.md`) to tell a broken rubric / judge error from a real model failure.

## How to export

1. Open the agent run environment.
2. Click the run in the sidebar (e.g., "Run #1").
3. Click **"Trajectory"** to download the JSON.
4. Paste its contents into the matching `RunN_Trajectory.json`.
5. Repeat for every successful run.

## Empty file

An empty run file = the agent errored on that run (no trajectory). That run is out of evaluation.
