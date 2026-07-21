# Agent_Responses — Per-Run Trajectories

Two models run per task — **Opus** and **Gemini**. Each produces up to 6 trajectories, stored in its own subfolder:

```
Agent_Responses/
  Opus/
    Run1_Trajectory.json … Run6_Trajectory.json
  Gemini/
    Run1_Trajectory.json … Run6_Trajectory.json
```

Used by the Verifier Fails eval (`Evals/4_Verifier_Fails_Eval.md`) to tell a broken rubric / judge error from a real model failure. Run the eval once per model.

## How to export

1. Open the agent run environment.
2. Click the run in the sidebar (e.g., "Run #1").
3. Click **"Trajectory"** to download the JSON.
4. Paste its contents into the matching model subfolder: `Opus/RunN_Trajectory.json` or `Gemini/RunN_Trajectory.json`.
5. Repeat for every successful run, for both models.

## Empty file

An empty run file = the agent errored on that run (no trajectory). That run is out of evaluation.
