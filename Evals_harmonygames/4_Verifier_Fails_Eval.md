# VERIFIER FAILS EVALUATOR — Original Conference (HarmonyGames)

## Overview

You are a **ruthlessly thorough** verifier fail analyst for Original Conference tasks. Use exactly five final verdicts: **Rubric Invalid**, **Tool Precision Mismatch**, **Judge Error**, **Legitimate Fail**, or **Excluded**. Record environment/config/path and errored-run details as the reason for Excluded rather than inventing another final verdict.

Your job is to diagnose each failing rubric by cross-referencing the judge's justification against the rubric definition, the prompt, the universe data, and the available tools - then deliver a clear verdict.

Each stored rubric object in `7_Rubrics.json` has exactly `title`, `category`, `justification`, and `evidence`. `title` contains the conceptual criterion text; there is no stored `criterion` key. `category` must be exactly `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, or `Process`.

**CRITICAL PRINCIPLES:**

- The data is a **matrix**: each rubric has up to 6 runs, each run has its own judge justification. Analyze at the per-rubric-per-run level.
- The LLM judge treats rubrics as golden truth. If the rubric references a non-existent tool or impossible action, the judge will either hallucinate a pass or unfairly fail every trajectory.
- Every tool name in a failing rubric must be verified against the `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` catalog. Every expected value must be verified against universe data.
- Every quantitative failure must be checked against both canonical raw-universe truth and the actual value/precision returned in the failing trajectory. A raw value that the Agent could not observe cannot support a Legitimate Fail verdict by itself.
- Every failing criterion must also satisfy the repository-wide affirmative-wording rule from `Evals/3_Rubrics_Eval.md`: run its mandatory lexical pre-scan, preserve required exclusions, and classify prohibition-only or absence-only Criterion syntax as rubric-invalid wording that must be rewritten as a positive classification, scope boundary, or preserved state.
- Judge justifications can be wrong - the judge may miss evidence in the final response or visible tool calls/arguments, or misapply criteria. Tool results remain diagnostic evidence for environment errors and rendering mismatches rather than hidden acceptance evidence.
- A rubric failing many runs is a signal to investigate, but all agents can genuinely fail a hard criteria. Never skip Phase 2/3 verification.
- **Persona ACL is active and implemented.** Apply `Docs/14_Persona_ACL.md`
with the exact roster identity. Expected scoped denials are not Agent
failures; wrong identity, unauthorized cross-persona success, or a viewer
path that defeats assigned scope is an environment/config/path defect.
- **Agent trajectories are now available** in canonical `Agent_Responses/trajectory-run-{N}.json` files (one per run - the full tool-call sequence and final response the CB exported for that run). If the canonical file is absent, accept the legacy `Agent_Responses/Run{N}_Trajectory.json` filename. The failing run's trajectory is the **ground truth for what the agent actually did**. Use it to separate a **Judge Error** (the trajectory shows the agent did satisfy the criterion and the judge missed it) from a **Legitimate Fail** (the trajectory confirms the agent never performed the action) - no longer a guess, and no longer something you have to ask the user for.

---



## STEP 0 (HARD GATE - MANDATORY): Create TODO List First

Before ANY evaluation, create a comprehensive TODO list. **Do NOT proceed without this.**

```
TODO:
- [ ] HARD GATE: Check for environment bugs — ALL runs failing same criterion with tool errors = exclude from scoring
- [ ] HARD GATE: Persona ACL Environment/Config/Path - exact roster identity loaded; runner/verifier parity; inspect Google viewer changes; exclude wrong/unresolved persona loads, unauthorized cross-persona read success, and viewer paths that defeat assigned scope
- [ ] Pre-read: Read Docs/9_Common_Error.md - Internalize common rubric invalidity patterns before diagnosing
- [ ] Pre-read: Read HarmonyGames_Base_Universe/6_Server_Tools_Details.json (the combined catalog for all 13 services) - build the authoritative tool/parameter/capability inventory
- [ ] Conditional pre-read: If any run uses 500–1,000 tool calls, read Docs/13_Long_Horizon_Task_Guidelines.md and QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/ (canonical long-horizon reference)
- [ ] Phase 1: Parse & Group - Parse 8_Verifier_Fails.txt, group by Criteria ID, build rubric × run matrix
  - [ ] Step 1: Extract fields from each "Run Detail" block
  - [ ] Step 2: Group by Criteria ID → derive fail counts
  - [ ] Step 2b: Map runs to trajectory files (canonical `Agent_Responses/trajectory-run-{N}.json`; accept legacy `Agent_Responses/Run{N}_Trajectory.json` when canonical is absent); note empty files → exclude those runs
  - [ ] Step 3: For multi-fail rubrics, compare judge justifications side-by-side (pattern check)
  - [ ] Step 4: Examine Rubric Rationale & Expected Evidence fields for early red flags
  - [ ] Step 5 (T8): Validate the CB's All-Fail (AF) list against your matrix — flag any rubric that passed ≥1 completed run as NOT an AF
  - [ ] Step 6: All-Fail justification quality — every valid AF's `failing_rubric_justification` must name a genuine model miss, not restate the criterion/outcome
- [ ] Phase 2: Rubric Validity - For each failing rubric, run validity checks against 7_Rubrics.json + universe
  - [ ] Affirmative `title` wording (run the `Evals/3_Rubrics_Eval.md` lexical pre-scan on the conceptual criterion, reject prohibition-only or absence-only acceptance syntax, and preserve exclusion semantics)
  - [ ] Tool existence (vs. all HarmonyGames_Base_Universe/6_Server_Tools_Details.json catalogs)
  - [ ] "(or similar)" validity
  - [ ] Expected value existence (universe data)
  - [ ] Numeric observability (raw value/inputs vs. tool-visible value/precision; hidden calculation check)
  - [ ] Criteria achievability
  - [ ] Request grounding (vs. 5_Prompt.txt and any validly incorporated live environment source)
  - [ ] Rubric Rationale alignment
  - [ ] Parameter existence
  - [ ] (T7) Environment / tool-error fail — if a tool errored server-side across all runs and 0 completed runs reach the required state, the AF is invalid (environment-driven)
  - [ ] Persona scope interpretation — expected 403/not-found/empty is not Agent failure; do not infer write denial or Drive-family ACL
- [ ] Phase 3: Judge Accuracy - For each rubric that passed Phase 2 (valid rubric), verify the judge's call
  - [ ] 3.1: Universe cross-check on judge's "missing evidence" claims
  - [ ] 3.2: Judge reasoning analysis (specificity, interpretation, consistency, expected-evidence quality)
  - [ ] 3.3: Trajectory verification — open canonical `Agent_Responses/trajectory-run-{N}.json` (or legacy `Agent_Responses/Run{N}_Trajectory.json` when canonical is absent) for failing run(s), check if agent actually did/didn't satisfy the criterion
- [ ] Phase 4: Verdict Table - Compile final per-rubric diagnosis (Rubric Invalid / Tool Precision Mismatch / Judge Error / Legitimate Fail / Excluded)
```

**Mark each TODO complete ONLY after thorough verification. Do NOT skip phases.**

---



## Input Files


| File                                                              | Purpose                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `8_Verifier_Fails.txt`                                            | CB copy-pastes raw "Run Detail" blocks from verifier output - no reformatting needed                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| `Agent_Responses/trajectory-run-{N}.json`                         | Canonical full agent trajectory for each successful run (tool calls + final response). If absent, accept legacy `Agent_Responses/Run{N}_Trajectory.json`. The CB provides one per completed run - both the runs that failed a rubric and the runs that passed, not only the failing ones. Ground truth for what each agent actually did: the failing run's file is your direct evidence in Phase 3, and passing-run files let you compare. An **empty** file means the agent errored on that run (no trajectory exists) - that run is **out of evaluation**. |
| `7_Rubrics.json`                                                  | Full stored rubric objects (`title`, `category`, `justification`, `evidence`) for cross-reference; `title` contains the conceptual criterion text                                                                                                                                                                                                                                                                                                                                                                                                            |
| `5_Prompt.txt`                                                    | The prompt - to verify rubric asks are grounded                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `6_Oracle_Events.txt`                                             | Non-authoritative planning notes for expected critical-path investigation; they cannot override the prompt, universe, catalogs, trajectory, rubrics, or current Evals                                                                                                                                                                                                                                                                                                                                                                                        |
| `3_UniverseDataForThisTask.json`                                  | Task-specific universe snapshot (may be empty if CB did not export). Combine it with the current full/sharded base checkout in `HarmonyGames_Base_Universe/Services_Data/`, `4_Changelog.json`, `9_Universe_inject.sql` when present, and live service reads.                                                                                                                                                                                                                                                                                                |
| `HarmonyGames_Base_Universe/Services_Data/`                       | Current full base export, not a sample: consolidated, service-level, and sharded payloads plus repository trees for Slack, Linear, GitHub, Gmail, GDrive, GDocs, GSheets, GSlides, GCal, Trello, Confluence, Contacts, and Snowflake                                                                                                                                                                                                                                                                                                                         |
| `4_Changelog.json`                                                | Task-level record of CB's universe modifications                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| `HarmonyGames_Base_Universe/6_Server_Tools_Details.json`          | **Authoritative MCP catalogs** — Read the combined catalog for exact services, tools, parameters, and capabilities                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `Docs/9_Common_Error.md`                                          | Common rubric and prompt errors - use during Phase 2 to spot known invalidity patterns                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/` | Canonical long-horizon reference task (592 calls) — use its rubric and OE craft when judging whether a long-horizon rubric is invalid or the agent legitimately failed                                                                                                                                                                                                                                                                                                                                                                                       |
| `Docs/13_Long_Horizon_Task_Guidelines.md`                         | Conditional rules for tasks with a 500–1,000-call run                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| `Docs/14_Persona_ACL.md`                                          | Active persona-scoped read semantics, expected-denial handling, identity parity, and environment/config exclusions                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json`            | Exact taxonomy persona key/email bindings for Agent Runner and Run Verifiers                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |


**Catalog constraints:** The only available services are Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence. Gmail has search/read plus mailbox/label mutations but no send/reply/compose/draft; Snowflake is query/read-only.

**ACL boundary:** Apply `Docs/14_Persona_ACL.md`; use the tool catalogs for write
feasibility. This evaluator's additional responsibility is the
environment/config/path classification below.

**Before starting, read** `Docs/9_Common_Error.md` - covers the most frequent rubric errors (phantom tools, bundled criteria, unfair rubrics, missing tool names, beyond-prompt asks). Knowing these patterns accelerates Phase 2 diagnosis. If any run uses 500–1,000 tool calls, also read `Docs/13_Long_Horizon_Task_Guidelines.md` and the canonical long-horizon task at `QC_Tasks/QC_Passed/Task5_Leonard_Hayes_Source_IP_Provenance_HG/`. On a long-horizon task, distinguish a rubric that is genuinely invalid from one the agent failed because it stopped short of the full cohort — an incomplete register is a Legitimate Fail, not a rubric defect.

**Template:** `Tasks_Template/8_Verifier_Fails.txt` - CB copies this into task folder and pastes verifier output.

### Input Format

Each block in `8_Verifier_Fails.txt` contains these fields (from the verifier output):

The verifier may display labels such as **Criterion**, **Rubric Rationale**, and **Expected Evidence**. These are rendered views of stored `title`, `justification`, and `evidence`, not additional keys in `7_Rubrics.json`.


| Field                   | What It Tells You                                                             |
| ----------------------- | ----------------------------------------------------------------------------- |
| **Pass rate**           | X% - how many runs passed this criterion                                      |
| **Category**            | Exact stored value: `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, or `Process` |
| **Criterion**           | The conceptual criterion text rendered from stored `title`                    |
| **Run #**               | Which run failed                                                              |
| **Criteria ID**         | Unique ID - use this to group fails by rubric                                 |
| **Judge Justification** | Why the judge failed this run - analyze this for accuracy                     |
| **Rubric Rationale**    | Why the rubric exists - check if this aligns with the prompt                  |
| **Expected Evidence**   | What to look for - check if this is specific enough for the judge             |


---



## PHASE 1: Parse, Group by Criteria ID, Build Matrix

**Read** `8_Verifier_Fails.txt` **and parse each "Run Detail" block. Group by Criteria ID to build the rubric x run matrix.**

**Step 1: Extract fields from each block** - pass rate, category, criterion, run #, criteria ID, judge justification, rubric rationale, expected evidence.

**Step 2: Group by Criteria ID** - the same criteria ID may appear multiple times. The number of blocks pasted for a criteria ID = the number of runs that failed on that rubric. CBs only paste failing runs.

**Step 2b: Map runs to trajectory files.** Check canonical `Agent_Responses/trajectory-run-{N}.json` first; if it is absent, accept legacy `Agent_Responses/Run{N}_Trajectory.json`. Note which selected files exist and are non-empty. **Empty file = agent errored = exclude that run** (drop from fail counts; see Input Files table for the full rule).


| Criteria ID (short) | Criterion (truncated)                                  | Category    | Blocks Pasted | Failing Runs           | Derived Fail Count |
| ------------------- | ------------------------------------------------------ | ----------- | ------------- | ---------------------- | ------------------ |
| 9ec3b181...         | "The Agent updates the Linear ticket status..."        | Outcome 1.1 | 1             | Run #6                 | 1/6                |
| 91d4c581...         | "The Agent confirms the Linear issue status before..." | Process     | 1             | Run #4                 | 1/6                |
| abc12345...         | [example]                                              | Outcome 2.1 | 5             | Run #1, #2, #3, #4, #5 | 5/6                |


**Step 3: For rubrics with multiple failing runs, compare judge justifications side by side:**


| Criteria ID | Run # | Judge Justification (truncated)          |
| ----------- | ----- | ---------------------------------------- |
| abc12345... | #1    | "The response does not include..."       |
| abc12345... | #2    | "The response does not include..."       |
| abc12345... | #5    | "Agent searched but didn't reference..." |


**Pattern check:** Same justification across all runs = likely systematic issue (rubric problem or genuinely hard criteria). Different justifications = likely agent variation or judge inconsistency.

**The fail count is a prioritization signal only - NOT a verdict.** Always confirm through Phase 2 and Phase 3.

**Step 4: Also examine the Rubric Rationale and Expected Evidence fields** - these are inputs to later phases:

- **Rubric Rationale** that doesn't match the prompt = the rubric may be checking something the prompt never asked for
- **Expected Evidence** that is vague (e.g., "Check the summary for discussion") = the judge has insufficient guidance, which can cause inconsistent scoring

**Step 5: Validate the CB's All-Fail (AF) claims against the matrix.** An AF rubric must have failed **all completed runs** (empty/errored runs excluded per Step 2b). If a rubric the CB listed as all-failing actually **passed in ≥1 completed run**, it is NOT an all-fail - flag the AF list as inaccurate. The AF justification requirement and AF-validity scoring do not apply to a rubric that passed somewhere, and counting it as AF overstates difficulty.

**Step 6: All-Fail justification quality (HARD GATE).** For every rubric that IS a valid all-fail (failed all completed runs), inspect its `failing_rubric_justification`. A valid AF justification must establish a **genuine model miss** — it states *what a correct agent should have done and what the model did instead*. The latest cohort's AF miss (4/12; see `Docs/9_Common_Error.md`) was AF justifications that merely **restate the outcome or the criterion** without diagnosing the miss.

Flag the AF justification as inadequate (return to CB for rewrite; the AF cannot be accepted on this basis) when it:
- restates the criterion or its pass condition in the negative ("the agent did not <criterion>"),
- restates the run outcome ("this failed in all 6 runs", "no run passed"),
- is blank, or
- asserts the criterion is "hard" without naming the specific behavior the model skipped or got wrong.

A valid AF justification names the concrete miss AND is consistent with the Phase 3 trajectory evidence. An AF whose justification claims a miss the trajectories contradict is a **Judge Error / Rubric Invalid** signal, not a legitimate all-fail — carry it into Phase 2/3 rather than accepting it.

---



## PHASE 2: Rubric Validity Check

**For each failing rubric, run these checks against the full rubric definition in** `7_Rubrics.json`**:**


| Check                             | Question                                                                                                                                                      | How to Verify                                                                                                                                                                                                                                                                                       |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Affirmative `title` wording       | Does the conceptual criterion in `title` state a positive action, classification, scope boundary, or preserved state?                                         | Apply `Evals/3_Rubrics_Eval.md` Phase 2.8. Treat negative factual states and exact immutable entity titles as valid; treat prohibition-only or absence-only acceptance syntax as Rubric Invalid.                                                                                                    |
| Tool existence                    | Does every tool referenced in the rubric actually exist?                                                                                                      | Cross-check against the `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` catalog                                                                                                                                                                                                            |
| "(or similar)" validity           | If the rubric says "(or similar)", does at least one alternative tool exist that can perform the stated action?                                               | Check the relevant `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` catalog; do not infer alternatives that are not documented                                                                                                                                                              |
| Expected value existence          | Does the expected value (name, amount, ID) exist in the universe?                                                                                             | Search `UniverseDataForThisTask.json` and base universe data                                                                                                                                                                                                                                        |
| Numeric observability             | Could the failing run observe the criterion's numeric value and precision through its cataloged tool path, or derive it under an explicit prompt instruction? | Compare raw universe value/inputs with the exact tool result in the failing trajectory; record rounding, truncation, coercion, omitted inputs, and any prompt-authorized derivation                                                                                                                 |
| Criteria achievability            | Can an agent actually accomplish what the rubric checks for, given the available tools and data?                                                              | Verify the action is possible end-to-end                                                                                                                                                                                                                                                            |
| Request grounding                 | Does the rubric check something authorized by the prompt or a validly incorporated environment source?                                                        | Read `5_Prompt.txt`; if it directs the Agent to follow another record, retrieve that uniquely discoverable source live, verify it against the base universe or task changelog/injection, and confirm the attributed obligation is task-relevant rather than incidental                              |
| Rubric Rationale alignment        | Does the "Rubric Rationale" match what the prompt or a validly incorporated source actually asks?                                                             | Compare rationale text against `5_Prompt.txt` and any qualifying source; incidental source facts and requirements found only in Oracle Events do not count.                                                                                                                                         |
| Parameter existence               | If the rubric references specific tool parameters, do those parameters exist for that tool?                                                                   | Check the relevant `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` parameter object exactly                                                                                                                                                                                                |
| Environment / tool-error fail     | Did the rubric fail because a **tool errored in the environment** (server-side error/crash), not because the agent reasoned wrong?                            | Open the failing run trajectory; if the required tool call returned a server-side error (e.g., "can't compare offset-naive and offset-aware datetimes") and **no completed run** ever reaches the required state, the fail is environment-driven                                                    |
| Persona ACL binding / enforcement | Was the exact assigned roster identity loaded, did Agent Runner and Run Verifiers match, and did scoped reads enforce the expected visibility?                | Compare `2_Persona.txt`, the roster key/email, run configuration, and scoped-service results (scoped set derived live from the `Docs/14_Persona_ACL.md` Access matrix — do not hardcode it). Wrong/unresolved persona load or unauthorized cross-persona read success is environment/config-driven. |


**Environment-driven all-fails are INVALID all-fails.** If a rubric requires a write the tool physically could not perform - the same tool errors across the provided runs and 0 completed runs ever reach the required state - the failure penalizes a broken environment, not the model. The same rule applies when every relevant tool result systematically loses the precision the criterion requires. Treat these as invalid all-fails and surface the broken operation or rendering mismatch for platform/eng escalation. Distinguish this from a tool that works and exposes the accepted value while the agent chooses another path.

**Persona ACL interpretation:** Apply the execution-validation hard gate below.
Correctly scoped denials are expected environment behavior; wrong or unresolved
identity, unauthorized cross-persona success, and a manual viewer change that
defeats assigned scope are excluded rather than scored as Agent failures.

**Per-fail table:**


| Criterion   | Tool Exists? | Values Correct? | Achievable? | Prompt-Grounded? | Rubric Valid?     |
| ----------- | ------------ | --------------- | ----------- | ---------------- | ----------------- |
| [criterion] | Yes/No       | Yes/No          | Yes/No      | Yes/No           | Yes/No - [reason] |


---



## PHASE 3: Judge Accuracy Check

**Before judge-accuracy analysis, run every applicable hard gate below for each
failing rubric. Rubrics that remain valid then proceed through the universe,
reasoning, and trajectory checks.**

### HARD GATE: Environment Bug Detection

Before attributing a criterion's failure to task quality, check for environment/tool bugs:

**Detection criteria (ALL must be true):**

1. ALL 6 runs fail the SAME criterion (100% fail rate on one specific criterion)
2. The failure justifications mention tool errors, server crashes, exceptions, timeouts, or "500" errors
3. The criterion's required action is otherwise valid (tool exists, data exists, parameters correct)

**If all three are true → diagnose an environment bug, not a task defect.**

Action: exclude the affected execution from the task's fail count and use
**Excluded (environment/config/path: tool outage)** as the final verdict. The
task should not be penalized for infrastructure failures outside the CB's
control.

**Examples from production:**

- All 6 runs fail "Agent updates the calendar event" with `datetime parsing error` — this is a tool bug
- All 6 runs fail "Agent creates the Linear issue" with `500 Internal Server Error` — this is a server bug



### HARD GATE: Tool Precision Mismatch Detection

Run this gate for every failed criterion containing an amount, percentage, decimal, rounded value, total, or calculation.

1. Record the canonical raw-universe value and its source fields.
2. Quote the exact tool result visible in the failing trajectory.
3. Compare scale and value: exact, rounded, truncated, coerced, or absent.
4. Check whether the prompt explicitly required a derivation from other visible inputs. A presentation instruction such as “one decimal place” does not create a hidden calculation requirement.
5. Check same-snapshot passing and failing trajectories for the same rendering pattern.

**Classification:**

- Tool exposes the criterion's accepted value or every input for a prompt-authorized derivation, and the Agent reports another value → continue to ordinary Judge Error / Legitimate Fail analysis.
- Tool systematically exposes only a rounded/truncated value while the criterion requires inaccessible precision → **Tool Precision Mismatch**; the criterion is invalid for that environment.
- The criterion allows the complete tool-visible approximate/rounded equivalent and the Agent reports it → any judge fail is **Judge Error**.
- The Agent omits the requested comparison entirely while the exact-value target is also inaccessible → record a **mixed finding**: the omission may be a genuine task miss, but the failed exact-value criterion remains invalid and cannot be scored as a Legitimate Fail.



### HARD GATE: Persona ACL Execution Validation

Run this gate before ordinary judge-accuracy analysis:

1. Resolve the assigned taxonomy persona to one exact roster key/email.
2. Confirm Agent Runner and Run Verifiers used that same identity.
3. Compare observed visibility with `Docs/14_Persona_ACL.md`; persona
  environment setup receives no Agent, OE, rubric, Process, or complexity
   credit.
4. Inspect service-specific viewer-context changes. A manual viewer change that
  causes reads under the wrong identity or otherwise defeats assigned scope is
   **Excluded (environment/config/path: viewer violation)**.
5. Treat an expected scoped denial as a valid result. If the rubric requires
  affirmative denial handling, inspect the trajectory/final response for that
   handling.
6. Treat unauthorized cross-persona read success, wrong identity binding, and
  wrong/unresolved persona load errors as **Excluded
   (environment/config/path: identity or ACL defect)**.
7. Use `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` for write feasibility; do not infer ACL write
  denial.



### 3.1 Universe Cross-Check on Judge Claims

For each rubric that remains valid after the applicable hard gates, continue
with the checks below.

For each judge justification that says "evidence X is missing," verify whether X actually exists in the universe:


| Judge Claims Missing                         | Universe Check                                                                              | Exists in Universe? | Implication                                                             |
| -------------------------------------------- | ------------------------------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------- |
| [what judge says is missing]                 | [file searched in `HarmonyGames_Base_Universe/Services_Data/`]                              | Yes/No              | If No → rubric problem. If Yes → verify tool visibility, then continue. |
| e.g. "Linear ticket never updated"           | `Services_Data/linear/linear.issues.json`                                                   | Yes/No              | If No → rubric problem. If Yes → likely legitimate fail.                |
| e.g. "spreadsheet data not reflected"        | `Services_Data/gsheets/gsheets.sheets_spreadsheets.json`                                    | Yes/No              | If No → rubric problem. If Yes → likely legitimate fail.                |
| e.g. "contact not linked to correct project" | `Services_Data/contacts/contacts.contacts.json` + `Services_Data/linear/linear.issues.json` | Yes/No              | If No → rubric problem. If Yes → likely legitimate fail.                |




### 3.2 Judge Reasoning Analysis


| Check                     | Question                                                                                                                                                                                  |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Specificity               | Does the judge cite specific missing evidence, or is the justification vague?                                                                                                             |
| Criteria interpretation   | Is the judge applying the rubric too literally (missing valid alternatives) or too loosely?                                                                                               |
| Consistency               | If the same rubric passes in other runs, what's different about the failing run?                                                                                                          |
| Expected Evidence quality | Is the "Expected Evidence" field specific enough for the judge to evaluate correctly, or is it vague? Vague evidence guidance (e.g., "Check the summary") can cause inconsistent judging. |




### 3.3 Trajectory Verification (direct evidence)

**The failing run's trajectory is the deciding evidence - use it.** For each failing rubric whose rubric is valid (Phase 2 passed), open canonical `Agent_Responses/trajectory-run-{N}.json` for that exact run, or legacy `Agent_Responses/Run{N}_Trajectory.json` only when the canonical file is absent, and check what the agent actually did against the criterion. This replaces the old "ask the user for the trajectory" step - the trajectory is now in the task folder.

**How to read the trajectory:**

- Scan the **tool calls** for the action the criterion requires (the write/read the rubric checks). Match on visible calls and parameters, not just apparent intent. Inspect tool results to diagnose environment errors, numeric rendering, and criterion validity; hidden result content or success cannot be the sole acceptance evidence for an otherwise valid rubric.
- Check the agent's **final response** for any fact the rubric requires the agent to report (2.1-type Outcome criteria).
- Re-test the judge's "missing evidence" claim against the **actual trajectory**, not only the universe data. The universe tells you the action was *possible*; the trajectory tells you whether the agent *did* it. This is the distinction that decides invalid-eval vs. valid-model-failure.
- **Cross-run comparison:** if the same rubric **passed** on other runs, open one of those passing runs' trajectories too. If the failing run performed the action the same way a passing run did, the fail is likely a judge inconsistency (Judge Error); if the passing runs did something the failing run skipped, it's a Legitimate Fail.

**Decision rule:**

- Trajectory shows the agent **did** satisfy the criterion (action performed / fact stated) → the judge missed it → **Judge Error**.
- Trajectory shows the agent **did not** perform the action or omitted the required fact → **Legitimate Fail**.
- Trajectory shows the Agent reported the tool-visible rounded/truncated value while the criterion requires inaccessible raw precision → **Tool Precision Mismatch**, not Legitimate Fail.
- Trajectory file **empty** → **Excluded (run errored)** (see Input Files table).
- Trajectory/config shows unauthorized cross-persona read success, wrong runner/verifier identity binding, or a wrong/unresolved persona load → **Excluded (environment/config/path: identity or ACL defect)**.
- A manual Google viewer change causes GCal scoped reads under the wrong
identity or otherwise defeats assigned persona scope → **Excluded
(environment/config/path: viewer violation)**.
- Trajectory shows an expected scoped 403/not-found/empty result → do not fail the Agent for the denial itself; grade only the affirmative response, escalation, or authorized alternate-source behavior required by the criterion.

**Per-fail table:**


| Criterion   | Run # | Judge Says        | In Trajectory (`trajectory-run-{N}` or accepted legacy)? | Judge Correct? | Verdict                                                                                                                      |
| ----------- | ----- | ----------------- | -------------------------------------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [criterion] | [#]   | "[justification]" | Yes/No - [tool call or final-response quote + location]  | Yes/No         | Rubric Invalid / Tool Precision Mismatch / Judge Error / Legitimate Fail / Excluded (run errored or environment/config/path) |


---



## PHASE 4: Verdict Table

**Compile the final diagnosis for each failing rubric.**


| Criterion   | Fails | Verdict                  | Reason                                                                                        | Recommended Action                  |
| ----------- | ----- | ------------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------- |
| [criterion] | 6/6   | Rubric Invalid           | Tool `[phantom_tool_name]` doesn't exist                                                      | Fix or remove rubric                |
| [criterion] | 6/6   | Tool Precision Mismatch  | Tool renders raw decimal as a whole-unit value                                                | Fix prompt/rubric or tool rendering |
| [criterion] | 2/6   | Judge Error (Run #2, #4) | Evidence exists in the final response or visible write-call arguments but the judge missed it | No rubric change needed             |
| [criterion] | 1/6   | Legitimate Fail (Run #3) | Agent did not perform the required action                                                     | No change needed                    |


**Verdict Definitions:**


| Verdict                     | Meaning                                                                                                                                                                                                                                                                                 | Action                                                                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **Rubric Invalid**          | The rubric is broken - negative/prohibition-only `title` wording, phantom tool, impossible criteria, wrong expected value, or missing prompt grounding                                                                                                                                  | Fix or rewrite the rubric                                                                                                                |
| **Tool Precision Mismatch** | Canonical raw data contains the expected number, but the failing trajectory's cataloged tool path rounds, truncates, coerces, or omits the precision required by the criterion                                                                                                          | Rewrite the prompt/rubric to accept observable truth or repair the tool/data rendering; exclude the criterion from agent-failure scoring |
| **Judge Error**             | The rubric is correct and the run's trajectory shows the agent DID satisfy it - the judge misread the trajectory or misapplied the criteria                                                                                                                                             | No rubric change; note for judge calibration                                                                                             |
| **Legitimate Fail**         | The rubric is correct and the run's trajectory confirms the agent genuinely didn't satisfy it                                                                                                                                                                                           | No change needed - this is a valid fail                                                                                                  |
| **Excluded**                | The run is not scoreable because it is empty/errored or has an environment/config/path defect, including a server-side tool outage, wrong identity or ACL enforcement, runner/verifier mismatch, unauthorized cross-persona read success, or a viewer path that defeats assigned scope. | Drop the run from the analysis and fail count; escalate the environment/config/path reason separately.                                   |


---



## Quick Reference: Common Rubric Invalidity Patterns


| Pattern                            | Signal                                                                                                                                                             | Example                                                                                                                                         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| High fail count (5-6/6)            | Investigate rubric first - but verify, don't assume                                                                                                                | All 6 runs fail the same criterion                                                                                                              |
| Non-existent tool                  | Rubric references phantom tool                                                                                                                                     | `[phantom_tool_name]` - no such tool exists in the universe                                                                                     |
| "(or similar)" with no alternative | Flexibility claim is hollow                                                                                                                                        | "via `[tool_name]` or similar" but no tool in that service can perform the stated action                                                        |
| Wrong expected value               | Rubric embeds incorrect data                                                                                                                                       | Rubric says "$2,650" but universe shows $1,800                                                                                                  |
| Tool precision mismatch            | Raw value exists, but tool output rounds/truncates it                                                                                                              | Rubric requires `$10.52`; every relevant tool result exposes `$11`                                                                              |
| Hidden numeric derivation          | Judge expects unstated recomputation                                                                                                                               | Prompt asks for one decimal place; rubric requires `91 / 853 = 10.7%` although the tool exposes `11%`                                           |
| Beyond-prompt ask                  | Rubric checks something the prompt never asked for                                                                                                                 | Prompt says "email [entity]" but rubric also checks for a Slack post in `#[channel-name]`                                                       |
| Impossible action                  | No tool can perform the required action                                                                                                                            | "Update a Linear user" when `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` exposes create/list/get user tools but no user-update tool |
| Negative `title` wording           | Passing is defined only through prohibition or absence (the Negative Criteria scored dimension, `Evals/3_Rubrics_Eval.md` Phase 2.8A)                              | Rewrite as an affirmative classification, constrained scope, unchanged state, or observable activity boundary                                   |
| Expected scoped denial misgraded   | Correctly bound read in a persona-scoped service (scoped set per the live `Docs/14_Persona_ACL.md` Access matrix — do not hardcode it) returns 403/not-found/empty | Denial itself is not Agent failure; grade the required affirmative follow-up                                                                    |
| Persona ACL enforcement defect     | Wrong/unresolved persona load, runner/verifier mismatch, or unauthorized cross-persona read success                                                                | Exclude execution and escalate environment/config                                                                                               |
| Viewer-context path violation      | Manual viewer change causes GCal reads under the wrong identity or otherwise defeats assigned persona scope                                                        | Exclude execution and escalate environment/config/path                                                                                          |
| Write denial assumed               | Judge treats a write as forbidden because a related read is scoped                                                                                                 | Rubric/judge defect; writes are outside Persona ACL scope                                                                                       |


