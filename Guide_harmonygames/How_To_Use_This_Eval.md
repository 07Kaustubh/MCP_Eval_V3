# How to Run the HarmonyGames Evaluation

Original Conference is a manual, AI-assisted QC workflow for HarmonyGames MCP
tasks. This runbook owns the operating sequence and copy-paste commands. It
does not redefine the rules inside [`Docs/`](../Docs/) or
[`Evals/`](../Evals/).

Start with [`../README.md`](../README.md) and
[`../Docs/README.md`](../Docs/README.md).

## Authority

1. [`../HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/) controls exact tool capabilities.
2. [`../Docs/15_Persona_ACL.md`](../Docs/15_Persona_ACL.md) and
   [`../HarmonyGames_Base_Universe/Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json)
   control task-visible identity and persona-scoped read visibility.
3. The live task state, task changelog/injection,
   [`../HarmonyGames_Base_Universe/`](../HarmonyGames_Base_Universe/), and
   [`../HarmonyGames_Base_Universe/6_Universe_Schema.json`](../HarmonyGames_Base_Universe/6_Universe_Schema.json)
   control live task/universe facts and database structure.
4. The prompt and any live, uniquely discoverable source it validly
   incorporates control the requested work.
5. [`../Evals/`](../Evals/) provides current procedures and repository-level
   policy overrides; [`../Docs/7_QC_Spec_Doc1.json`](../Docs/7_QC_Spec_Doc1.json)
   and [`../Docs/8_QC_Spec_Doc2.md`](../Docs/8_QC_Spec_Doc2.md) define scored
   dimensions and their interpretation.
6. Other Docs and [`../QC_Tasks/`](../QC_Tasks/) explain or calibrate; examples
   are guidance only.

For every feasibility or tool check, read all 13 JSON catalogs in
`HarmonyGames_Base_Universe/Tool_Access/`. Oracle Events are internal plans and cannot override the
prompt, universe, catalogs, trajectories, or current Evals.

## Prerequisites

- Cursor IDE with Agent mode enabled.
- **Claude Opus 4.7 max** for the final six task runs.
- A local copy of this repository and the task artifacts to evaluate.

This repository has no automated eval runner. Run the phases below manually in
Cursor.

## Repository layout

```text
<repository-root>/
├── Docs/                       # Normative rules and QC specifications
├── Evals/                      # Six eval playbooks, numbered 0–5
├── Guide/                      # This operational runbook
├── Generated_Tasks/            # In-progress task workspaces
├── HarmonyGames_Base_Universe/ # Narrative, schema, and Services_Data
├── QC_Tasks/                   # Completed calibration examples
├── QC_Tasks_Archive/           # Legacy non-HarmonyGames examples
├── Tasks_Template/             # Canonical task scaffold
└── HarmonyGames_Base_Universe/Tool_Access/                # Thirteen authoritative tool catalogs
```

Keep in-progress tasks in `Generated_Tasks/`. Do not add them to `QC_Tasks/`,
whose folders represent completed QC outcomes.

## Set up a task

Copy `Tasks_Template/` to `Generated_Tasks/<task-name>/`, then populate:

1. `1_Business_Function.txt` — assigned business function.
2. `2_Persona.txt` — exact Persona Key, Persona Email, Name, Role, and
   Department copied from one `Persona_ACL_Roster.json` entry.
3. `3_UniverseDataForThisTask.json` — optional task-specific universe export.
4. `4_Changelog.json` — task injection/change manifest.
5. `5_Prompt.txt` — prompt under evaluation.
6. `6_Oracle_Events.txt` — non-authoritative solution plan.
7. `7_Rubrics.json` — rubric array using `title`, `category`,
   `justification`, and `evidence`.
8. `8_Verifier_Fails.txt` — raw per-run verifier failure blocks, when
   available.
9. `9_Universe_inject.sql` — SQL record of injected or modified rows.
10. `Agent_Responses/trajectory-run-{N}.json` — exported trajectories for
    runs 1–6.

`trajectory-run-{N}.json` is canonical for new exports. The evaluators also
accept legacy `Run{N}_Trajectory.json` files. An empty trajectory means that
run errored and is excluded from rubric fail counts. Follow
[`../Tasks_Template/Agent_Responses/README.md`](../Tasks_Template/Agent_Responses/README.md).

### Historical calibration compatibility

Original QC calibration folders may retain a free-text persona artifact or a
non-roster identity. Those artifacts are craft/history references only: they
are not evidence of current ACL compliance or performance, and their persona
format must not be copied. Every new or current task requires `2_Persona.txt`
with exact Persona Key, Persona Email, Name, Role, and Department values from
one roster entry. The long-horizon Task5 example remains a craft baseline, but
its persona artifact is not the current task template.

## Configure and check Persona ACL

Persona ACL is active. Use this order for every task:

1. Select the required persona in Taxonomy. Taxonomy is the selection source.
2. Copy the full matching `Persona_ACL_Roster.json` entry into `2_Persona.txt`.
   Copy the Persona Email exactly; never infer it from the name.
3. **Do not touch the AMV persona dropdown.** It overrides the Taxonomy
   selection and persists into later runs.
4. Load the intended universe. After load, the platform automatically applies
   `set_acting_user` with the roster email. It requires the email and is
   automatically re-applied on every Agent Runner or Run Verifier run/turn; do
   not call it manually.
5. Author against complete Universe Explorer truth, then check task feasibility
   separately through the assigned persona's Agent scope.
6. Keep the same required persona in Agent Runner and Run Verifiers.

The Universe Explorer remains author god-mode. Its visibility does not prove
that the task Agent or verifier can read a record. For every required injected
fact in Gmail, Slack, GCal, or Contacts, confirm that the assigned persona has
a natural discovery path and the needed ownership, membership, share, invite,
or visibility relationship, or that the task requires an affirmative denial
outcome or uses an authorized unscoped alternate.

Exactly 13 services are task-visible. Gmail, Slack, GCal, and Contacts reads are
persona-scoped. GDrive, GitHub, Snowflake, GDocs, GSheets, GSlides, Trello,
Linear, and Confluence reads are unscoped. Writes are outside Persona ACL scope.
Evaluate feasibility using these read boundaries and the exact capabilities in
all 13 `HarmonyGames_Base_Universe/Tool_Access/` catalogs.

Automatic acting-user setup is environment configuration, not an Agent tool
call. Do not count it toward complexity, Oracle Events, or Process rubrics.

## Run order

There are **six eval files** but **seven workflow phases**:

- Phases 0–4 invoke Evals 0–4.
- Phase 5 is a separate full QC-spec scorecard.
- Phase 6 invokes Eval 5, the final submission gate.

Run every phase in order. Replace `TaskXX_XXXXX` with the actual folder name,
complete every checklist required by the referenced Eval, and resolve findings
before continuing.

### Long-horizon condition

If at least one run uses 500–1,000 calls, read
[`../Docs/14_Long_Horizon_Task_Guidelines.md`](../Docs/14_Long_Horizon_Task_Guidelines.md)
before Phase 0 and calibrate against
[`../QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/`](../QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/).
Reuse its task craft structure, never its persona artifact, scenario, data,
wording, or totals.

### Phase 0 — Injection quality

Run before prompt, OE, or rubric evaluation:

```text
Evaluate @Generated_Tasks/TaskXX_XXXXX/9_Universe_inject.sql and @Generated_Tasks/TaskXX_XXXXX/4_Changelog.json using @Evals/0_Injection_Quality_Eval.md. Compare against @HarmonyGames_Base_Universe/6_Universe_Schema.json and @HarmonyGames_Base_Universe/Services_Data/, read every JSON catalog in @HarmonyGames_Base_Universe/Tool_Access/, create every required TODO, and execute every HARD GATE without deviation.
```

### Phase 1 — Prompt

```text
Evaluate @Generated_Tasks/TaskXX_XXXXX/5_Prompt.txt using @Evals/1_Prompt_Eval.md. Read the task universe artifacts, @HarmonyGames_Base_Universe/, and every JSON catalog in @HarmonyGames_Base_Universe/Tool_Access/. Create every required TODO and execute every phase and HARD GATE without deviation.
```

The prompt gate requires more than 15 necessary calls, 2+ genuine services,
multiple meaningful writes, and information friction. The higher 40+ call and
3+ service numbers are authoring targets, not replacements for this gate.

### Phase 2 — Oracle Events

```text
Evaluate @Generated_Tasks/TaskXX_XXXXX/6_Oracle_Events.txt using @Evals/2_OE_Eval.md. Read the prompt, task universe artifacts, and every JSON catalog in @HarmonyGames_Base_Universe/Tool_Access/. Create every required TODO and execute every phase without deviation. Treat OEs as internal plans, not ground truth.
```

### Phase 3 — Rubrics

```text
Evaluate @Generated_Tasks/TaskXX_XXXXX/7_Rubrics.json using @Evals/3_Rubrics_Eval.md. Read the prompt, OEs, task universe artifacts, and every JSON catalog in @HarmonyGames_Base_Universe/Tool_Access/. Create every required TODO and execute every phase and HARD GATE without deviation.
```

The stored rubric fields are `title` (criterion text), `category`,
`justification`, and `evidence`. Use `Outcome 1.1`, `Outcome 1.2`,
`Outcome 2.1`, or `Process` as the category. Current rules require atomic,
self-contained, affirmative, agent-centric criteria; Process remains rare and
must pass the three-condition test. Outcome is mandatory and Process may not
exceed 40% of the set.

### Phase 4 — Verifier failures

Run after trajectories and verifier results exist:

```text
Analyze @Generated_Tasks/TaskXX_XXXXX/8_Verifier_Fails.txt and @Generated_Tasks/TaskXX_XXXXX/Agent_Responses/ using @Evals/4_Verifier_Fails_Eval.md. Read every JSON catalog in @HarmonyGames_Base_Universe/Tool_Access/, follow every required TODO, and classify each failing rubric/run as Rubric Invalid, Judge Error, Legitimate Fail, Tool Precision Mismatch, or Excluded.
```

### Phase 5 — Full QC specification

This phase is not an additional file in `Evals/`:

```text
Evaluate @Generated_Tasks/TaskXX_XXXXX/ on every dimension of @Docs/7_QC_Spec_Doc1.json and @Docs/8_QC_Spec_Doc2.md. Score every sub-dimension explicitly, apply current Eval overrides, and treat any hard-failing dimension as a task failure.
```

### Phase 6 — Submission gate

```text
Run the final submission gate on @Generated_Tasks/TaskXX_XXXXX/ using @Evals/5_Submission_Gate_Eval.md. Read every JSON catalog in @HarmonyGames_Base_Universe/Tool_Access/, create every required TODO, check all six defect families and every listed pattern, and execute every HARD GATE without deviation.
```

Submit only when Phase 6 passes with zero hard failures.
