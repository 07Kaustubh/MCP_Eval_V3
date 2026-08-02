# Platform UI Workflow Reference

This is a concise reference for moving through the task-authoring platform. Start
with the [`Docs/README.md`](README.md) reading path. This file does not define
prompt, Oracle Event, rubric, QC, or tool policy.

## Authority

When wording differs, follow the current sources in this order:

1. [`HarmonyGames_Base_Universe/Tool_Access/*.json`](../HarmonyGames_Base_Universe/Tool_Access/) for enabled services, operations,
   parameters, pagination, and read/write limits.
2. [`15_Persona_ACL.md`](15_Persona_ACL.md) and
   [`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json)
   for task-visible identity and persona-scoped read visibility.
3. Live task data, its injection/changelog,
   [`HarmonyGames_Base_Universe/`](../HarmonyGames_Base_Universe/), and
   [`6_Universe_Schema.json`](../HarmonyGames_Base_Universe/6_Universe_Schema.json)
   for live task/universe facts and database structure.
4. The prompt and any live, uniquely discoverable source it validly
   incorporates for the requested work.
5. [`Evals/`](../Evals/) for current procedures and repository-level policy
   overrides, plus the scored QC specifications
   ([`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json) and
   [`8_QC_Spec_Doc2.md`](8_QC_Spec_Doc2.md)) for scored dimensions and their
   interpretation.
6. The remaining authoring docs, this UI reference, and historical examples as
   supplementary guidance only.

Use [`../Guide/How_To_Use_This_Eval.md`](../Guide/How_To_Use_This_Eval.md) to
run the evaluation sequence. Current Evals and QC rules override stale wording
in an example or screenshot.

## Correct Platform Order

### 1. Confirm the assignment

- Check the assigned business function and required persona in Taxonomy.
- Treat the Taxonomy persona selection as the source. Copy one exact
  `Persona_ACL_Roster.json` entry into `2_Persona.txt`, including Persona Key,
  Persona Email, Name, Role, and Department. Never derive the email.
- **Do not touch the AMV persona dropdown.** It overrides the Taxonomy selection
  and persists into later runs.
- Confirm the prefilled Environment ID and Base Universe ID.
- If continuing an edited universe, load the intended prior Universe ID before
  making changes.

After universe load, the platform automatically applies `set_acting_user` with
the selected Persona Email. It requires the email and is automatically
re-applied on every Agent Runner or Run Verifier run/turn. Authors and Agents
must not call it manually. This environment configuration is not an Agent tool
call and does not count toward complexity, Oracle Events, or Process rubrics.

### 2. Explore and edit the universe

- Enter fullscreen mode for the universe explorer.
- Use the platform chatbot or sandbox editor to inspect and, when needed,
  strengthen one coherent HarmonyGames situation.
- Treat Universe Explorer results as author god-mode authoring truth, not proof
  that the assigned persona can read the same records.
- Keep names, dates, identifiers, and cross-service facts consistent.
- Check every required Gmail, Slack, GCal, or Contacts fact through the assigned
  persona's Agent scope, including intentional affirmative denial handling or
  an authorized unscoped alternate where applicable. Reads in those four
  services are persona-scoped; GDrive, GitHub, Snowflake, GDocs, GSheets,
  GSlides, Trello, Linear, and Confluence reads are unscoped. Writes are
  outside Persona ACL scope. These are the 13 task-visible services.
- Review the ChangeLog before advancing. See
  [`10_How_To_Load_and_Edit_Universe.md`](10_How_To_Load_and_Edit_Universe.md)
  for the loading, editing, snapshot, and rollback workflow.

### 3. Draft and save the prompt

- Write a natural request in the assigned persona's voice.
- Ground every concrete identifier in the task environment.
- Keep implementation-specific tool names and parameters out of the prompt.
- Save the prompt step before moving forward.

### 4. Write Oracle Events before any agent run

Record the key affirmative tool-use steps a correct Agent would take, including
the important discovery and write actions, expected facts, and exact tool
parameters used for feasibility planning.

**Do not run trajectories first and backfill Oracle Events afterward.** OEs must
precede the agent runs because they establish the intended solvable path and
drive later rubric coverage. OEs are internal planning notes, not authority:
the prompt, universe, tool catalogs, trajectory evidence, and current Evals
override them.

Use [`Evals/2_OE_Eval.md`](../Evals/2_OE_Eval.md) for OE validation. A
prohibition or no-op is not an OE; a real lookup that confirms a negative fact
or checked absence is.

### 5. Run agent trajectories

- Open the agent-run area and start the trajectory batch once the prompt and OEs
  are saved.
- Confirm the Runner still shows the required Taxonomy persona. The platform
  re-applies the exact Persona Email on each run/turn.
- The platform runs six trajectories. Keep the browser session available while
  they run.
- At least four runs must complete without an execution error. A completed run
  that misses a valid rubric is a model failure, not an erroneous run.
- Use fast iteration models while developing and **Claude Opus 4.7 max** for
  the final six runs.
- Review each trajectory and final response before judging task difficulty.

Each run snapshots the current universe into its end-state Universe ID. Follow
the current snapshot behavior described in
[`10_How_To_Load_and_Edit_Universe.md`](10_How_To_Load_and_Edit_Universe.md).

### 6. Author and save rubrics

Use [`2_Rubrics_Guidelines.md`](2_Rubrics_Guidelines.md); this file intentionally
does not duplicate its tutorial. In the UI, confirm that every rubric has a
criterion, category, justification, and evidence. In saved `7_Rubrics.json`,
the criterion text is stored in `title`, with `category`, `justification`, and
`evidence`; use `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, or `Process` as
the category.

### 7. Run rubric verifiers

- Save the preceding agent-run/rubric step before opening the verifier tab.
- Use the same required persona as the Agent Runner so verifier evidence is
  evaluated under the same read scope.
- Run the verifier batch once.
- Review every failure against the prompt, ground truth, trajectory, and tool
  catalogs.
- For any rubric that fails all completed runs, add the required short
  justification and determine whether it is a genuine model failure, a rubric
  defect, a judge error, or an environment/tool-observability problem. Use
  [`12_Always_Failing_Rubrics.md`](12_Always_Failing_Rubrics.md) and
  [`Evals/4_Verifier_Fails_Eval.md`](../Evals/4_Verifier_Fails_Eval.md).

### 8. Evaluate and submit

Run the phases in
[`../Guide/How_To_Use_This_Eval.md`](../Guide/How_To_Use_This_Eval.md) in order,
fixing findings before the next phase. Submit only after the final QC and
submission-gate checks pass.

## UI Handoff Checklist

- [ ] Taxonomy has the correct persona and business function; the AMV persona
      dropdown was not touched.
- [ ] `2_Persona.txt` contains the exact five-field roster entry and exact email.
- [ ] Universe edits are coherent and visible in the ChangeLog.
- [ ] Required Gmail, Slack, GCal, or Contacts evidence is reachable by the
      assigned persona, intentionally denied with an affirmative outcome, or
      available from an authorized unscoped alternate, independently of
      Explorer god-mode visibility.
- [ ] Prompt is saved.
- [ ] Oracle Events were written and saved before trajectories were run.
- [ ] Six trajectories were attempted and at least four completed.
- [ ] Rubrics are saved in the current schema.
- [ ] Agent Runner and Run Verifiers used the same required persona.
- [ ] All-failing rubrics have been investigated and justified.
- [ ] The ordered Evals and submission gate have passed.
