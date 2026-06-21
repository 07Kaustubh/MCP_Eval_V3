# How to Use the MCP Eval V3

---

## What is This?

MCP Eval V3 is an AI-assisted quality evaluation system for MCP tasks. It evaluates three components of each task - **Prompt**, **Oracle Events (OEs)**, and **Rubrics** - by guiding an AI agent through structured, multi-phase checks against universe data, tool specifications, and QC standards. A fourth eval analyzes **verifier failures** from agent runs, using the per-run agent **trajectories** (`Agent_Responses/`) as direct evidence to separate broken rubrics and judge errors from legitimate model failures.

You paste commands into Cursor (or similar AI coding IDE), and the agent follows the eval guide to find issues, flag them by severity, and suggest fixes.

> **Framework note (V3):** Rubrics use two categories - **Outcome** (mandatory) and **Process** (optional and rare). The old V2 categories (Tool Selection, Query Construction) are gone. Rubrics are phrased as **agent behaviors** and must **never name tools**; tool/parameter checking lives in the Oracle Events eval.

---

## Folder Structure

```
MCP_Eval_V3/
├── Evals/                          # The eval guides (core of the system)
│   ├── 1_Prompt_Eval.md            # Prompt quality evaluation
│   ├── 2_OE_Eval.md                # Oracle Events quality evaluation
│   ├── 3_Rubrics_Eval.md           # Rubrics quality evaluation
│   └── 4_Verifier_Fails_Eval.md    # Verifier failure analysis
├── Docs/                           # Reference documents
│   ├── 1_Project_Instructions_Overall.md   # Task creation guidelines
│   ├── 2_Rubrics_V3_Guidelines.md          # V3 rubric model (Outcome/Process, three-condition test, agent-centric phrasing)
│   ├── 3_Rubrics_V3_One_Pager.md           # V3 quick reference
│   ├── 4_Prompt_Hard_Tips.md               # Tips for designing harder prompts
│   ├── 5_Prompt_Diversity_Business_Function.md # Business function categories
│   ├── 6_Prompt_Relative_Time_Updates.md   # Fixed date rules (June 12, 2026)
│   ├── 7_QC_Spec_Doc1.json                 # QC grading thresholds and dimensions
│   ├── 8_QC_Spec_Doc2.md                   # QC severity definitions and auditor notes
│   ├── 9_Common_Error.md                   # Common errors in task/rubric creation
│   ├── 10_How_To_Load_and_Edit_Universe.md # Universe loading instructions
│   ├── 11_Taxonomy.md                      # Task taxonomy and version guidance
│   └── 12_Always_Failing_Rubrics.md        # All-failing-rubric patterns
├── Brookfield_Base_Universe/       # Brookfield CPAs & Advisors universe (source of truth)
│   ├── 1_Summary.md               # Company summary, personas, clients, scenarios
│   ├── 2_Persona_Briefs.md        # Detailed per-persona profiles
│   ├── 3_Task_Categories_Business_Functions.md # Business function categories
│   ├── 4_Scenario_Storylines.md   # Scenario storylines
│   ├── 5_Artifacts_Universe_Ref_Sheet.md # Dense reference (personas, schemas, accounts)
│   ├── 6_Glossary.md              # Accounting terms and universe conventions
│   ├── 7_Brookfield_Universe_One_pager.md # Universe one-pager
│   ├── 8_Server_Tools_Details.json # All MCP tools with parameters
│   ├── 9_Universe_Schema.json     # Database schema
│   ├── Get_Universe_Data.sql      # SQL to extract universe data
│   └── Data/                      # All JSON data files (Oracle GL, SAP Subledger, BlackLine, Records Vault, Email, Slack, etc.)
├── QC_Tasks/                       # Sample tasks for reference
│   ├── V3_Tasks/                  # On-framework (V3) tasks on the Brookfield universe - primary reference
│   │   └── TaskXX_XXXXX/          # Each has: Prompt, OEs, Rubrics, Quality_Scores, Task_Info
│   └── V2_Tasks/                  # V2/Keystone samples - study structure/craft only, apply the V3 framework
├── Tasks_Template/                 # Templates for task files (includes Agent_Responses/ for run trajectories)
└── Tasks/                          # Actual tasks to evaluate
    └── TaskXX_XXXXX/              # Each task folder with its files
        └── Agent_Responses/      # Per-run agent trajectories (Run1_Trajectory.json … Run6_Trajectory.json) - feed the Verifier Fails eval
```

---

## Prerequisites

- **Cursor IDE** with agent mode enabled

---

## Step 1: Set Up the Task Folder

Create a folder under `Tasks/` for the task (e.g., `Tasks/Task30_69c1cf16a2f45785f047023e/`) and populate it:


| Step | What to Do                                                                                                                      | Target File                                                                   |
| ---- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| 1    | Copy-paste the persona metadata                                                                                                 | `2_Persona.txt`                                                               |
| 2    | Copy-paste the business function                                                                                                | `1_Business_Function.txt`                                                     |
| 3    | Extract the changelog (task-specific universe edits) into a changelog file, OR extract the complete universe data for this task | `4_Changelog.json` or `3_UniverseDataForThisTask.json`                        |
| 4    | Copy-paste the prompt                                                                                                           | `5_Prompt.txt`                                                                |
| 5    | Copy-paste the oracle events                                                                                                    | `6_Oracle_Events.txt`                                                         |
| 6    | Copy-paste the rubrics (JSON array)                                                                                             | `7_Rubrics.json`                                                              |
| 7    | Copy-paste the failed rubric verifier results per run (if available)                                                            | `8_Verifier_Fails.txt` (use `Guide/Verifier_Fails_Template.txt` as reference) |
| 8    | Export each run's agent trajectory (tool calls + final response) per run (if available)                                          | `Agent_Responses/Run{N}_Trajectory.json` (see `Agent_Responses/README.md` for steps) |


Once the task folder is set up, proceed to evaluation.

---

## Step 2: Evaluation Workflow

Evaluate tasks in this order: **Prompt → Oracle Events → Rubrics**. Each phase builds context for the next.

### 2.1 Prompt Evaluation

Point the agent to the task's prompt file and the eval guide:

```
Lets evaluate the quality of @Tasks/TaskXX_XXXXX/5_Prompt.txt using @MCP_Eval_V3/Evals/1_Prompt_Eval.md
```

The agent checks persona coherence, feasibility, truthfulness, structural anti-patterns, date/time grounding, and grammar/typos - then scores across all QC dimensions.

After the initial eval, run a deep feasibility + truthfulness recheck:

```
deep check for feasibility. verify every entity, event, scenario, and data point referenced in the prompt actually exists in the universe. also deep check truthfulness.
```

Fix any issues found, then move to Phase 2.

### 2.2 Oracle Events Evaluation

```
Okay so now lets evaluate the quality of @Tasks/TaskXX_XXXXX/6_Oracle_Events.txt using @MCP_Eval_V3/Evals/2_OE_Eval.md
```

The agent verifies every tool name, parameter, and value against `8_Server_Tools_Details.json` and universe data, checks completeness, accuracy, and date/time consistency.

Run completeness and accuracy rechecks after the initial eval. Fix any issues, then move to Phase 3.

### 2.3 Rubrics Evaluation

```
Okay, so now evaluate quality of @Tasks/TaskXX_XXXXX/7_Rubrics.json using @MCP_Eval_V3/Evals/3_Rubrics_Eval.md
```

The agent checks each rubric for atomicity, self-containment, correctness, flexibility, agent-centric phrasing (no tool names in criteria), over-specificity / valid-path preservation, completeness (both forward and reverse), overlap/redundancy, and Outcome/Process category balance - then scores using severity taxonomy and percentage thresholds.

After initial eval, run deep rechecks on: atomicity, self-containment, flexibility, accuracy, completeness. Fix all issues, then add rubric numbers.

### 2.4 Final QC Spec Assurance

```
Now lets evaluate the prompt, oracle events, and rubrics on each dimensions of QC spec doc for a final assurance. @MCP_Eval_V3/Docs/7_QC_Spec_Doc1.json @MCP_Eval_V3/Docs/8_QC_Spec_Doc2.md
```

### 2.5 Verifier Fails Analysis (Optional)

If you have verifier output from agent runs, use this eval to analyze failures:

1. Copy the `Guide/Verifier_Fails_Template.txt` into the task folder as `8_Verifier_Fails.txt`
2. Paste the raw "Run Detail" blocks for failing rubrics into it
3. Export each **successful run's** trajectory into `Agent_Responses/Run{N}_Trajectory.json` (every run that completed, not just the failing ones - steps in `Agent_Responses/README.md`). This lets the eval read what the agent actually did and decide judge-error vs. legitimate-model-failure directly, instead of guessing.
4. Run:

```
Analyze the verifier fails using @Tasks/TaskXX_XXXXX/8_Verifier_Fails.txt, the agent trajectories in @Tasks/TaskXX_XXXXX/Agent_Responses/ , and @MCP_Eval_V3/Evals/4_Verifier_Fails_Eval.md
```

The agent will build a rubric x run matrix, check rubric validity, verify judge accuracy against universe data, and produce a verdict table (Rubric Invalid / Judge Error / Legitimate Fail).

---

## Boilerplate Commands

Use these commands sequentially for each task evaluation. Replace `TaskXX_XXXXX` with the actual task folder name. Fix any issues found between steps before moving on.

### PHASE 1: PROMPT EVALUATION

**1.1 Full Prompt Evaluation**

```
Lets evaluate the quality of @Tasks/TaskXX_XXXXX/5_Prompt.txt using @MCP_Eval_V3/Evals/1_Prompt_Eval.md . Must create and follow all to-dos very regressively. . Lets also focus more on checking for feasibility and truthfulness - every factual claim the persona makes must exist in the universe data. 
```

**1.2 Deep Feasibility + Truthfulness**

```
deep check for feasibility. verify every entity, event, scenario, and data point referenced in the prompt actually exists in the universe. also deep check truthfulness - every factual claim and assumption in the prompt must be grounded in universe data. and business function persona alignment check.
```

### PHASE 2: ORACLE EVENTS EVALUATION

**2.1 Full OE Evaluation**

```
Okay so now lets evaluate the quality of @Tasks/TaskXX_XXXXX/6_Oracle_Events.txt using @MCP_Eval_V3/Evals/2_OE_Eval.md . Must create and follow all to-dos regressively. focus deeply on: feasibility (every tool name, parameter, value must exist and be correct), completeness (every prompt ask has a corresponding OE step), accuracy (every entity, amount, ID matches universe data exactly), verify each tool and parameter exists in 8_Server_Tools_Details.json, no required parameters missing.
```

**2.2 Completeness + Accuracy Re-check**

```
lets recheck completeness and accuracy. decompose the prompt sentence by sentence - every ask maps to at least one OE, nothing missing, nothing extra. all tool calls, tool names, parameters, values must be correct and exist in universe data and 8_Server_Tools_Details.json. 
```

### PHASE 3: RUBRICS EVALUATION

**3.1 Full Rubric Evaluation**

```
Okay, so now evaluate quality of @Tasks/TaskXX_XXXXX/7_Rubrics.json using @MCP_Eval_V3/Evals/3_Rubrics_Eval.md . Must create and follow all to-dos regressively. Focus on atomicity, completeness (forward and reverse), self-containment, correctness against universe JSON data, flexibility, no overlapping/extra rubrics, agent-centric phrasing (no tool names in criteria), over-specificity / valid-path preservation, and V3 compliance (Outcome mandatory with write actions in Outcome 1.1; Process optional and only when the three-condition test holds; Outcome must outnumber Process).
```

**3.2 Deep Atomicity Recheck**

```
Recheck each rubric on atomicity in depth. Read each sentence word by word - does this rubric check exactly ONE independent thing? If a rubric bundles two verifiable claims, flag it.
```

**3.3 Deep Self-Containment Recheck**

```
Recheck each rubric on self-containment in depth. Can a verifier evaluate this rubric using only the criterion text + agent trajectory, without needing to look up universe data? All expected values (emails, amounts, names, IDs) must be embedded in the criterion itself.
```

**3.4 Deep Flexibility Recheck**

```
Recheck each rubric on flexibility in depth. Is "approximately" used for calculated/rounded values? Are exact matches used for IDs, dates, counts? Does the rubric match the prompt's level of specificity - a goal-level ask ("notify legal") must not be locked to one method ("email legal")? Flag any over-specificity that would fail a valid alternative path.
```

**3.5 Deep Accuracy Recheck**

```
Recheck each rubric on accuracy in depth. Verify every dollar amount, email address, entity name, ticket ID, company name against universe data. Any tool name appearing in evidence/justification must exist in 8_Server_Tools_Details.json - and no tool name should appear in the criterion text at all. Flag any mismatch.
```

**3.6 Deep Completeness Recheck**

```
Recheck each rubric on completeness in depth. Decompose the prompt sentence by sentence - does every explicit ask map to at least one rubric? Is there any rubric that goes beyond what the prompt asked? No missing, no extra.
```

### PHASE 4: FINAL QC SPEC ASSURANCE

```
Now lets evaluate the prompt, oracle events, and rubrics on each dimensions of Qc spec doc for a final assurance. @MCP_Eval_V3/Docs/7_QC_Spec_Doc1.json @MCP_Eval_V3/Docs/8_QC_Spec_Doc2.md
```

### PHASE 5: VERIFIER FAILS ANALYSIS (if verifier output available)

Paste raw "Run Detail" blocks for failing rubrics into `@Tasks/TaskXX_XXXXX/8_Verifier_Fails.txt` (use `Guide/Verifier_Fails_Template.txt` as reference), export each **successful run's** trajectory into `@Tasks/TaskXX_XXXXX/Agent_Responses/Run{N}_Trajectory.json` (every completed run, not just the failing ones - steps in `Agent_Responses/README.md`), then run:

```
Analyze the verifier fails using @Tasks/TaskXX_XXXXX/8_Verifier_Fails.txt, the agent trajectories in @Tasks/TaskXX_XXXXX/Agent_Responses/ , and @MCP_Eval_V3/Evals/4_Verifier_Fails_Eval.md . For each failing rubric, determine if the failure is due to a broken rubric, a judge error, or a legitimate agent failure - using the run's trajectory as direct evidence of what the agent did.
```

---

## Tips & Reminders

**General:**

- The context built during Prompt evaluation carries into OE and Rubric evaluation. The deep universe exploration done in Phase 1 is the foundation for all subsequent phases.
- Always verify dollar amounts by doing the math yourself from the raw data rather than trusting summaries.
- When the prompt references "my team" or "my clients", verify persona-scoped data vs company-wide totals.
- Universe date is June 12, 2026. All relative time references should resolve against this date.
- Check the QC_Tasks for reference if unsure what good prompts/OEs/rubrics look like (`V3_Tasks/` are on-framework, Brookfield; `V2_Tasks/` are V2/Keystone samples - study craft, apply the V3 framework).

**Prompt:**

- Check for explicit tool/MCP server mentions - natural references to systems are Non-Fail, explicit tool names are Fail.
- Bolt-on test: remove any sentence - if the rest still makes perfect sense, that sentence is a bolt-on.
- No relative date-time references in the prompt.
- Verify persona actually has the role/access to make the request described.

**Oracle Events:**

- Every tool name must exist exactly in `8_Server_Tools_Details.json`.
- Every parameter name must exist for that tool. No required parameters missing.
- Watch parameter names: `email_reply_to_email` and `messaging_send_message` use `content`; `slack_conversations_add_message` uses `payload` (not `text`).
- OEs describe tool-use steps, not what the final response should say.

**Rubrics (V3):**

- Two categories only: **Outcome** (mandatory) and **Process** (optional, rare). No Tool Selection / Query Construction.
- Rubrics are **agent-centric** and must **never name tools** in the criterion (e.g., "The Agent sends an email to…", not "calls email_reply_to_email"). Tool/parameter checking belongs to the OE eval.
- Write actions go in **Outcome (1.1)** - every write action gets its own Outcome rubric (never "at least N").
- Tighten Outcome with precise values (numbers, IDs, derived math) before reaching for a Process rubric.
- Add a **Process** rubric only when ALL THREE hold: (1) it captures ordering/behavior no Outcome can verify, (2) it's required by every valid solution path, (3) a stricter Outcome rubric cannot capture the same requirement.
- "Approximately" ONLY for calculated/rounded values - NOT for counts, IDs, dates, or exact static values.
- "(or similar)" for free-text/agent-generated content, NOT for exact values from data.
- Match the prompt's level of specificity - a goal-level ask ("notify legal") must not be locked to one method ("email legal"); over-specificity that fails a valid alternative path is a Major issue.
- Any tool name in an evidence/justification field must exist in `8_Server_Tools_Details.json`; the criterion text must contain no tool names at all.
- Category balance: **no fixed ratio** - most tasks have ZERO Process rubrics. Outcome must outnumber Process; >50% Process is a FAIL.

