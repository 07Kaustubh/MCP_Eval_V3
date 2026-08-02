# Load and Edit the HarmonyGames Universe

Last refreshed: **July 28, 2026**

## Fixed provisioning values

- **Environment ID:** `hg4-2026-07-02-env`
- **Base Universe ID:** `hg4-2026-07-02`
- **Simulation date:** February 28, 2026, America/Chicago
- **Active injection window:** January 1 through February 28, 2026

The IDs are existing provisioning labels. Their embedded date does not independently define the simulation date.

Verify the IDs in [`../HarmonyGames_Base_Universe/4_Reference_Sheet.md`](../HarmonyGames_Base_Universe/4_Reference_Sheet.md). Start with the documentation map in [`README.md`](README.md).

## Current platform workflow

### 1. Load the universe

When a task is claimed, the environment and base-universe IDs should already be
filled in. Confirm they match the values above before loading.

To continue from a universe you previously edited, enter that prior universe ID instead of the base ID. Do this only when continuity is intentional and the inherited edits have been reviewed.

Before loading, select the required persona in **Taxonomy** and copy that
persona's exact `Persona_ACL_Roster.json` entry into `2_Persona.txt`. Taxonomy is
the source for persona selection. Copy the roster email exactly; never infer or
construct it from the person's name.

> **Do not touch the AMV persona dropdown.** It overrides the Taxonomy selection
> and its value persists into later runs.

After the universe loads, the platform automatically applies `set_acting_user`
with the selected Persona Email. The operation requires the email and is
automatically re-applied for every Agent Runner or Run Verifier run/turn. Do not
make a manual `set_acting_user` call. This is environment configuration, not an
Agent tool call, so it does not count toward task complexity, Oracle Events, or
Process rubrics. The Agent Runner and Run Verifiers must use the same required
persona.

### 2. Explore before editing

Use the Universe Explorer and Chatbot Agent to identify a coherent HarmonyGames
scenario. The Universe Explorer remains author god-mode: it shows authoring
truth across the universe, regardless of what the assigned persona can read.
Explorer visibility therefore does not establish Agent reachability. Read:

- [`../HarmonyGames_Base_Universe/0_Universe_One-Pager.md`](../HarmonyGames_Base_Universe/0_Universe_One-Pager.md)
- [`../HarmonyGames_Base_Universe/1_Universe_Summary.md`](../HarmonyGames_Base_Universe/1_Universe_Summary.md)
- [`../HarmonyGames_Base_Universe/2_Persona_Briefs.md`](../HarmonyGames_Base_Universe/2_Persona_Briefs.md)
- [`../HarmonyGames_Base_Universe/3_Task_Categories_Business_Functions.md`](../HarmonyGames_Base_Universe/3_Task_Categories_Business_Functions.md)
- [`../HarmonyGames_Base_Universe/4_Reference_Sheet.md`](../HarmonyGames_Base_Universe/4_Reference_Sheet.md)

The local service exports are under
[`../HarmonyGames_Base_Universe/Services_Data/`](../HarmonyGames_Base_Universe/Services_Data/).
This checkout contains the full base export; high-volume Slack, Gmail, GDrive,
and GitHub payloads use sharded or nested layouts. Use the live environment for
task-specific changes and to verify what the Agent can observe through tools.

Persona ACL is active. Exactly 13 services are task-visible:

- **Persona-scoped reads:** Gmail, Slack, GCal, and Contacts. Read results depend
  on mailbox ownership, channel membership, calendar ownership/sharing/invites,
  and contact visibility for the assigned persona.
- **Unscoped reads:** GDrive, GitHub, Snowflake, GDocs, GSheets, GSlides, Trello,
  Linear, and Confluence.
- **Writes:** outside Persona ACL scope.

Required injected evidence in Gmail, Slack, GCal, or Contacts must be reachable
through the assigned persona's scope unless the task requires an affirmative
denial outcome or uses an authorized unscoped alternate. Verify this separately
from the complete authoring truth shown in the Explorer.

### 3. Edit manually

The current supported authoring paths are:

1. **Chatbot Agent** — recommended for exploration, edits, changelog summaries, and reversions.
2. **SQL in the Sandbox** — available for direct universe edits when exact control is needed.

The **Scenario Generation** tool is offline and has been unavailable since April 7, 2026. Do not make it a workflow dependency or assume an “Enhanced Universe” was generated.

Chatbot and SQL edits are universe-authoring operations. They do not grant the
task Agent additional capabilities or bypass Persona ACL.
[`../HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/) remains authoritative; in particular, the
task Agent's Snowflake access is query/read-only.

### 4. Review every edit

The editing interfaces do not guarantee consistency or cascade related changes. Manually verify:

- schema compliance;
- ID format and uniqueness;
- timestamps inside the active window and coherent thread/event ordering;
- names, statuses, relationships, and references across affected services;
- natural message style;
- assigned-persona reachability or valid denial/alternate handling for every
  required Gmail, Slack, GCal, or Contacts fact;
- verifier observability under the same persona scope as the Agent Runner;
- absence of precomputed answers or ready-made deliverables.

Use the current schema:

- [`../HarmonyGames_Base_Universe/6_Universe_Schema.json`](../HarmonyGames_Base_Universe/6_Universe_Schema.json)

Then run the injection hard gates:

- [`../Evals/0_Injection_Quality_Eval.md`](../Evals/0_Injection_Quality_Eval.md)

Correct any schema, ID, temporal, collision, contradiction, orphan, phantom, or
pre-solve defect before running trajectories.

### 5. Run trajectories

After the universe and prompt are ready:

1. Use a faster model for iteration if desired.
2. Use **Claude Opus 4.7 max** for the final six runs.
3. Require at least **4 of 6** runs to complete successfully.
4. Keep at most **2 of 6 completed runs** passing all valid rubrics (`pass@1 <= 40%`).
5. Keep the thresholds distinct: 40+ average calls and 3+ services is the authoring target; >15 necessary calls is the prompt-eval gate; >=15 observed average calls is the trajectory QC floor.

Keep the Taxonomy-selected persona unchanged through Agent Runner and Run
Verifier execution. The platform re-applies its exact Persona Email on every
run/turn.

Each trajectory snapshots the current universe into a new universe ID. The submitted task uses that universe end state. The end-state changelog remains available, but there is currently no Explorer or Chatbot view for the end-state universe.

## Local task and evaluation workflow

This repository is evaluated manually in Cursor. Create a working task by copying [`../Tasks_Template/`](../Tasks_Template/) to:

`Generated_Tasks/<task-name>/`

Use [`../Guide/How_To_Use_This_Eval.md`](../Guide/How_To_Use_This_Eval.md) for the ordered workflow.

### Task artifact pointers

- `1_Business_Function.txt` — assigned HarmonyGames business function.
- `2_Persona.txt` — exact roster fields for the Taxonomy-selected persona.
- `3_UniverseDataForThisTask.json` — optional task-specific universe snapshot/export.
- `4_Changelog.json` — task change manifest from the live environment.
- `5_Prompt.txt` — task prompt.
- `6_Oracle_Events.txt` — internal Oracle Events.
- `7_Rubrics.json` — rubric JSON array using `title`, `category`, `justification`, and `evidence`.
- `8_Verifier_Fails.txt` — failing verifier blocks copied per completed run.
- `9_Universe_inject.sql` — SQL record of task injection changes; primary offline source for what was inserted or updated.
- `Agent_Responses/trajectory-run-{N}.json` — the canonical exported trajectory
  name for runs 1–6; evaluators also accept legacy
  `Run{N}_Trajectory.json` files. Follow
  [`../Tasks_Template/Agent_Responses/README.md`](../Tasks_Template/Agent_Responses/README.md).

Do not place in-progress tasks in `QC_Tasks/`; that directory contains completed calibration history.

### Current universe data pointers

For offline checks, use:

- `HarmonyGames_Base_Universe/Services_Data/Base_Universe_Complete_Data.json`
- `HarmonyGames_Base_Universe/Services_Data/<service>/...`
- `HarmonyGames_Base_Universe/7_Get_Universe_Data.sql`
- `HarmonyGames_Base_Universe/6_Universe_Schema.json`
- the task's `3_UniverseDataForThisTask.json`, `4_Changelog.json`, and `9_Universe_inject.sql`

When local exports and the live environment disagree, the live task environment controls. Record and fix the export mismatch.

## Evaluation links

Run these in order and resolve findings before continuing:

1. [`../Evals/0_Injection_Quality_Eval.md`](../Evals/0_Injection_Quality_Eval.md)
2. [`../Evals/1_Prompt_Eval.md`](../Evals/1_Prompt_Eval.md)
3. [`../Evals/2_OE_Eval.md`](../Evals/2_OE_Eval.md)
4. [`../Evals/3_Rubrics_Eval.md`](../Evals/3_Rubrics_Eval.md)
5. [`../Evals/4_Verifier_Fails_Eval.md`](../Evals/4_Verifier_Fails_Eval.md)
6. [`../Evals/5_Submission_Gate_Eval.md`](../Evals/5_Submission_Gate_Eval.md)

For scored QC dimensions and their human explanation, use [`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json) and [`8_QC_Spec_Doc2.md`](8_QC_Spec_Doc2.md).
