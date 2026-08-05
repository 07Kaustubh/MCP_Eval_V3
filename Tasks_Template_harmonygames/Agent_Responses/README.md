# Agent_Responses — Per-Run Trajectories

Store one trajectory file per successful run. The canonical filenames are
`trajectory-run-1.json` through `trajectory-run-6.json`. Evaluators also accept
the legacy names `Run1_Trajectory.json` through `Run6_Trajectory.json`.

These files are used by the Verifier Fails eval
(`Evals/4_Verifier_Fails_Eval.md`) to distinguish a broken rubric or judge error
from a real model failure.

## Persona record and access behavior

Associate each exported trajectory with the task's `../2_Persona.txt`. The
exported JSON is not required to contain Persona Key or Persona Email metadata.
Where platform or run context exposes identity, verify that Agent Runner and
Run Verifiers used the same required persona. Never hand-edit an exported
trajectory to add, remove, or normalize persona fields. After universe load,
the platform automatically applies the email-required `set_acting_user`
configuration and re-applies it on every run/turn; it must not appear as a
manual Agent tool call.

Gmail, Slack, GCal, and Drive-family (GDrive/GDocs/GSheets/GSlides) reads are persona-scoped. If a trajectory
unexpectedly succeeds in reading data that its assigned persona is not
authorized to see, classify it as **Excluded (environment/config defect)**,
drop it from model scoring, and rerun it with the required persona scope. An
expected access denial can be valid task behavior and does not by itself make
a trajectory erroneous.

## How to export

1. Open the agent run environment.
2. Click the run in the sidebar (e.g., "Run #1").
3. Click **"Trajectory"** to download the JSON.
4. Paste its contents into the matching canonical `trajectory-run-{N}.json`.
5. Repeat for every successful run.

## Empty file

An empty run file = the agent errored on that run (no trajectory). That run is out of evaluation.
