# How to Use the MCP Eval V4 (StarPM)

---

## What is This?

MCP Eval V4 (StarPM) is an AI-assisted quality evaluation system for MCP tasks. It includes **6 evals** that cover the full task lifecycle — from universe injection quality through prompt, oracle events, rubrics, verifier failures, and a final submission gate. Each eval guides an AI agent through structured, multi-phase checks against universe data, tool specifications, and QC standards.

You paste commands into Cursor (or similar AI coding IDE), and the agent follows the eval guide to find issues, flag them by severity, and suggest fixes.

> **Framework note (V3):** Rubrics use two categories - **Outcome** (mandatory) and **Process** (optional and rare). The old V2 categories (Tool Selection, Query Construction) are gone. Rubrics are phrased as **agent behaviors** and must **never name tools**; tool/parameter checking lives in the Oracle Events eval.

---

## Folder Structure

```
MCP_Eval_V4_StarPM/
├── Evals/                    # 6 eval guides — the core of the system (0-5, run in order)
├── Docs/                     # Reference docs — project instructions, QC spec, rubric guidelines, common errors, taxonomy
├── StarPM_Base_Universe/     # Universe source of truth — summary, personas, scenarios, tools, schema, and Data/ folder
├── QC_Tasks/                 # Sample tasks for reference (QC_Passed, QC_Non_Fails, QC_True_Fails)
├── Tasks_Template/           # Templates for task files (includes Agent_Responses/ for trajectories)
└── Tasks/                    # Your actual tasks to evaluate
```

---

## Prerequisites

- **Cursor IDE** with agent mode enabled (claude opus 4.7 max)

---

## Step 1: Set Up the Task Folder

Create a folder under `Tasks/` for the task (e.g., `Tasks/Task30_69c1cf16a2f45785f047023e/`) and populate it:


| Step | What to Do                                                                                                                      | Target File                                                                          |
| ---- | ------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
| 1    | Copy-paste the persona metadata                                                                                                 | `2_Persona.txt`                                                                      |
| 2    | Copy-paste the business function                                                                                                | `1_Business_Function.txt`                                                            |
| 3    | Extract the changelog (task-specific universe edits) into a changelog file, OR extract the complete universe data for this task | `4_Changelog.json` or `3_UniverseDataForThisTask.json`                               |
| 4    | Copy-paste the prompt                                                                                                           | `5_Prompt.txt`                                                                       |
| 5    | Copy-paste the oracle events                                                                                                    | `6_Oracle_Events.txt`                                                                |
| 6    | Copy-paste the rubrics (JSON array)                                                                                             | `7_Rubrics.json`                                                                     |
| 7    | Copy-paste the failed rubric verifier results per run, per model (if available)                                                 | `8a_Verifier_Fails_Opus.txt` and `8b_Verifier_Fails_Gemini.txt`                        |
| 8    | Export each run's agent trajectory per model (tool calls + final response) per run (if available)                               | `Agent_Responses/Opus/Run{N}_Trajectory.json` and `Agent_Responses/Gemini/Run{N}_Trajectory.json` (see `Agent_Responses/README.md`) |


Once the task folder is set up, proceed to evaluation.

---

## Step 2: Evaluation Commands

Run these phases **in order**. Replace `TaskXX_XXXXX` with your actual task folder name. Fix issues between steps before moving on.

### PHASE 0: INJECTION QUALITY (validates the injection)

```
Evaluate my universe injection using @MCP_Eval_V4_StarPM/Evals/0_Injection_Quality_Eval.md . Read @Tasks/TaskXX_XXXXX/9_Universe_inject.sql + @Tasks/TaskXX_XXXXX/4_Changelog.json , compare against @MCP_Eval_V4_StarPM/StarPM_Base_Universe/Data/ . MUST create and strictly follow ALL to-dos mentioned in 0_Injection_Quality_Eval.md. Do NOT deviate from the eval's instructions & checklist. Every HARD GATE must be executed.
```

```
Deep recheck injection integrity against base universe. For EVERY injected/modified record: (1) DIFF against existing base records in ALL 8 services — check for ID collisions, name spelling mismatches, amount conflicts, status contradictions, timeline collisions, and broken cross-service references, (2) verify no injected data orphans existing records (e.g., changing a ticket assignee without updating the Slack thread about it), (3) verify injected timestamps are within 2026-05-01 to 2026-07-01 window, on weekdays, and chronologically valid (parent before child in reply chains), (4) verify no AI-tells in injected text — no emojis, no overly formal Slack messages, no repeated syntactic patterns, no corporate filler phrases. Any contradiction, collision, or integrity violation = FAIL.
```

### PHASE 1: PROMPT EVALUATION

```
Evaluate @Tasks/TaskXX_XXXXX/5_Prompt.txt using @MCP_Eval_V4_StarPM/Evals/1_Prompt_Eval.md . MUST create and strictly follow ALL to-dos mentioned in 1_Prompt_Eval.md. Do NOT deviate from the eval's instructions & checklist. Every HARD GATE must be executed. Do NOT skip any phase or sub-check.
```

```
Deep recheck the prompt on these critical dimensions: (1) FEASIBILITY — for EVERY explicit ask in the prompt, verify the data exists in the universe AND is discoverable via MCP tools. If ANY ask can't be fulfilled = FAIL, no "minor secondary" escape. (2) TRUTHFULNESS — extract every tight identifier (channel names, entity names, IDs, amounts, dates) and grep each against the universe JSON files. No match = phantom = FAIL. Near-matches don't count. (3) UGT — enumerate the end-states under each reasonable reading. If all 6 agent runs converge, apply deeper scrutiny before failing. Wording variations that lead to the same writes are NOT multiple valid answers. (4) DELEGATION — scan for "I'll [verb]" mixed with agent imperatives. If ambiguous who acts = Action Decision Ambiguity = FAIL. (5) COMPLEXITY — must need >15 tool calls, 2+ services, multiple write actions. Single-service investigate+email = Too Easy = FAIL.
```

### PHASE 2: ORACLE EVENTS EVALUATION

```
Evaluate @Tasks/TaskXX_XXXXX/6_Oracle_Events.txt using @MCP_Eval_V4_StarPM/Evals/2_OE_Eval.md . MUST create and strictly follow ALL to-dos mentioned in 2_OE_Eval.md. Do NOT deviate from the eval's instructions & checklist. Every HARD GATE must be executed.
```

```
Deep recheck OEs on these critical dimensions: (1) COMPLETENESS — decompose the prompt sentence by sentence. Every explicit ask must map to at least one OE step. Every OE step must map back to a prompt ask. Nothing missing, nothing extra. (2) ACCURACY — every tool name must exist exactly in 7_Server_Tools_Details.json. Every parameter must exist for that tool. Every entity name, amount, ID, and email in OE steps must match universe data exactly. (3) OE AUTHORITY — remember OEs are CB internal docs, NOT ground truth. If an OE contradicts the prompt or universe data, the OE is wrong, not the prompt. Flag any OE-rubric contradictions as investigation signals.
```

### PHASE 3: RUBRICS EVALUATION

```
Evaluate @Tasks/TaskXX_XXXXX/7_Rubrics.json using @MCP_Eval_V4_StarPM/Evals/3_Rubrics_Eval.md . MUST create and strictly follow ALL to-dos mentioned in 3_Rubrics_Eval.md. Do NOT deviate from the eval's instructions & checklist. Every HARD GATE must be executed. Do NOT skip any phase or sub-check.
```

```
Deep recheck rubrics on ATOMICITY: ML confirmed "split completely" (Muskan/Sunjie/Razvan, July 2026). Read each criterion word by word. Count the independently-verifiable claims it makes. If >1 and they can pass/fail independently = MUST be split. Examples of violations: "Email mentions the storm damage AND includes the new city AND has flight details" (3 independent items), "Agent updates the status AND adds a note about the vendor delay" (2 independent items). This is the #1 QC failure pattern — do NOT let bundled criteria through.
```

```
Deep recheck rubrics on ACCURACY + COMPLETENESS + OVERLY BROAD: (1) ACCURACY — verify every dollar amount, email address, entity name, ticket ID, property name against universe data. Any mismatch = FAIL. Tool names in evidence must exist in 7_Server_Tools_Details.json; criterion text must contain NO tool names. (2) FORWARD COVERAGE — decompose prompt sentence by sentence. Every explicit deliverable must map to at least one Outcome rubric. Missing = FAIL (Major). (3) OVERLY BROAD — for each criterion IN ISOLATION: could a factually wrong answer still pass? If yes and the wrong path is plausible = FAIL. NEVER argue "sibling criterion covers it" — QC has rejected this 3+ times. (4) DESTINATION — if prompt says "email to X" but rubric checks "final response" = wrong artifact = FAIL. (5) BLANK FIELDS — Category, Criterion, Justification, Evidence must all be non-blank. Any blank = auto-FAIL.
```

```
Deep recheck rubrics on SELF-CONTAINMENT: For each criterion, ask: can a judge evaluate pass/fail using ONLY the criterion text + the agent's trajectory, WITHOUT looking up universe data or solving the task themselves? Every expected value (dollar amounts, email addresses, entity names, IDs, counts, dates) must be embedded directly in the criterion text. If a judge would need to grep the universe or compute a calculation to know the right answer = NOT self-contained = FAIL.
```

```
Deep recheck rubrics on OVERLAP + REDUNDANCY: Compare every pair of criteria. Do any two criteria check the same thing with different wording? If removing one criterion would not change the scoring outcome for ANY possible agent behavior = redundant = flag for removal. Also check: do any two criteria contradict each other (one requires X, another penalizes X)? Contradicting criteria = FAIL.
```

```
Deep recheck rubrics on MISSING + EXTRA: (1) MISSING — decompose every explicit prompt ask into the write actions and key findings it requires. For each, verify at least one Outcome rubric covers it. If a prompt ask has zero rubric coverage = Missing Criteria = FAIL (Major). Pay special attention to multi-part asks where one part got a rubric but others didn't. (2) EXTRA — does any rubric check something the prompt never asked for? A rubric that goes beyond the prompt's explicit asks = beyond-prompt = flag. The rubric set should match the prompt exactly — nothing missing, nothing extra.
```

```
Deep recheck rubrics on FLEXIBILITY + OVER-SPECIFICITY: (1) Does each rubric match the prompt's level of specificity? A goal-level ask ("notify the owner") must NOT be locked to one method ("email the owner") — an agent who posts in #owner-relations should also pass. (2) Are exact matches used only for values from data (IDs, amounts, dates)? "Approximately" only for calculated/rounded values. "(or similar)" only for free-text, never for data values. (3) Does any rubric pin a specific tool path, query parameter, or structured ID format when the tool also accepts alternatives? Check 7_Server_Tools_Details.json to confirm. Over-specificity that would fail a valid alternative path = FAIL (Major).
```

### PHASE 4: VERIFIER FAILS ANALYSIS (after agent runs — run once per model)

**Opus:**
```
Analyze @Tasks/TaskXX_XXXXX/8a_Verifier_Fails_Opus.txt and trajectories in @Tasks/TaskXX_XXXXX/Agent_Responses/Opus/ using @MCP_Eval_V4_StarPM/Evals/4_Verifier_Fails_Eval.md . MUST follow ALL to-dos mentioned in 4_Verifier_Fails_Eval.md. Do NOT deviate. Classify each: Rubric Invalid / Judge Error / Legitimate Fail.
```

**Gemini:**
```
Analyze @Tasks/TaskXX_XXXXX/8b_Verifier_Fails_Gemini.txt and trajectories in @Tasks/TaskXX_XXXXX/Agent_Responses/Gemini/ using @MCP_Eval_V4_StarPM/Evals/4_Verifier_Fails_Eval.md . MUST follow ALL to-dos mentioned in 4_Verifier_Fails_Eval.md. Do NOT deviate. Classify each: Rubric Invalid / Judge Error / Legitimate Fail.
```

### PHASE 5: FINAL QC SPEC ASSURANCE

```
Evaluate prompt, oracle events, and rubrics on EVERY dimension of @MCP_Eval_V4_StarPM/Docs/7_QC_Spec_Doc1.json and @MCP_Eval_V4_StarPM/Docs/8_QC_Spec_Doc2.md . Score each sub-dimension explicitly. Any single FAIL dimension = task FAILS.
```

### PHASE 6: SUBMISSION GATE (final check before submitting)

```
Run submission gate on @Tasks/TaskXX_XXXXX/ using @MCP_Eval_V4_StarPM/Evals/5_Submission_Gate_Eval.md . MUST create and strictly follow ALL to-dos mentioned in 5_Submission_Gate_Eval.md. Do NOT deviate. Check ALL 6 families, all 32 patterns. ZERO TOLERANCE — any single defect = FAIL.
```

