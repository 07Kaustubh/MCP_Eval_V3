# HarmonyGames Human QC Specification

Last refreshed: **July 28, 2026**

This document explains the machine-readable dimensions in [`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json). Run the six current evaluator playbooks in [`../Evals/`](../Evals/) in the order defined by [`../Guide/How_To_Use_This_Eval.md`](../Guide/How_To_Use_This_Eval.md). A hard-gate defect prevents submission even when an older example passed with that pattern.

## Authority order

1. [`../HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json) — enabled services, exact tools, parameters, and capabilities.
2. [`14_Persona_ACL.md`](14_Persona_ACL.md) and the exact 17-entry
   [`4_Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json)
   — task-visible identity and persona-scoped read visibility.
3. [`../HarmonyGames_Base_Universe/Services_Data/`](../HarmonyGames_Base_Universe/Services_Data/),
   task `4_Changelog.json`, task `9_Universe_inject.sql`, and
   [`../HarmonyGames_Base_Universe/7_Universe_Schema.json`](../HarmonyGames_Base_Universe/7_Universe_Schema.json)
   — live task/universe facts and database structure.
4. The prompt and any live, uniquely discoverable source it validly
   incorporates — the requested work.
5. [`../Evals/0_Injection_Quality_Eval.md`](../Evals/0_Injection_Quality_Eval.md)
   through [`../Evals/5_Submission_Gate_Eval.md`](../Evals/5_Submission_Gate_Eval.md)
   — current procedures and repository-level policy overrides; plus
   [`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json) and this document for scored
   dimensions and their interpretation.
6. Other authoring guides and [`../QC_Tasks/`](../QC_Tasks/) — explanation and calibration only.

Oracle Events and historical examples never override the prompt, live universe, schema, tool catalogs, or current Evals.

Persona identity and read visibility are governed by
[`14_Persona_ACL.md`](14_Persona_ACL.md) and the exact 17-entry
[`4_Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json).
Use the selected roster entry's Persona Key, Persona Email, Name, Role, and
Department exactly; never infer an email from a name.

## The three complexity thresholds

These numbers apply at different stages:

- **40+ calls and 3+ services — authoring target.** Build a naturally deep task likely to average at least 40 calls across three or more services.
- **More than 15 necessary calls — prompt-eval hard gate.** Before running the Agent, the task must necessarily require **>15 calls**, genuine work across **2+ enabled services**, multiple meaningful writes, and information friction. A task estimated at 15 or fewer calls fails even if a run later wanders past 15.
- **At least 15 average calls — trajectory QC floor.** After completed runs exist, the average must be **>=15**. This observed floor does not replace the prompt-eval gate or the 40+ authoring target.

## Fixed HarmonyGames boundaries

- Today: **February 28, 2026**, America/Chicago.
- Injection window: **January 1 through February 28, 2026**.
- Exactly 13 services are enabled: Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence.
- Gmail supports reading, searching, attachments, and mailbox/label triage. It has no send, reply, compose, or draft capability.
- Snowflake is query/read-only.
- Product names outside the 13 catalogs may be business topics or evidence stored in an enabled service; they are not direct tools.
- Persona ACL is active and implemented and scopes reads only for Gmail, Slack,
  GCal, and the Drive-family (GDrive, GDocs, GSheets, GSlides, which inherit
  Drive's file ACL). Contacts, GitHub, Snowflake, Trello, Linear, and Confluence
  reads remain unscoped; writes are outside ACL scope.
- Universe Explorer is author god-mode. Agent Runner and Run Verifiers use the
  same assigned persona.
- Automatic `set_acting_user` application is environment configuration, not
  Agent work, an Oracle Event, a rubric/Process requirement, or a call-count
  item.

Use [`6_Prompt_Relative_Time_Updates.md`](6_Prompt_Relative_Time_Updates.md) for exact relative-time resolution.

## Injection hard gates

Run [`../Evals/0_Injection_Quality_Eval.md`](../Evals/0_Injection_Quality_Eval.md) before prompt evaluation.

An injection fails when any of these holds:

1. A record violates the schema, type, nullability, foreign-key, or enum rules.
2. An ID collides with base data or breaks the same-table convention.
3. A timestamp is outside the active window or chronology is impossible. Routine Slack and Gmail business communication on a weekend is a temporal violation.
4. An edit contradicts base facts, leaves required dependent records stale, or breaks a cross-service reference.
5. Three or more injected text fields show clear AI-tell patterns.
6. A required record is orphaned or unreachable through cataloged tools.
7. A record pre-solves the conclusion or contains the ready-made deliverable.
8. The seven-dimension injection difficulty score is below **2.5**.

Local exports support offline validation, but the live task environment controls when it disagrees with an export. Explorer or local-export visibility proves that a record exists globally, not that the assigned persona can read it.

## Prompt QC

Run [`../Evals/1_Prompt_Eval.md`](../Evals/1_Prompt_Eval.md).

### Unique ground truth

Enumerate the concrete writes and final deliverables under every reasonable reading. Different paths are valid when they converge on the same end state. The prompt fails when two readings produce materially different correct writes, act-versus-defer choices, or deliverables.

Before failing, apply both guardrails:

- Confirm the difference is material rather than a wording or label variation already accepted by the rubric.
- If all completed runs converge, investigate the alleged alternative more deeply. Convergence is evidence, not proof.

There is no leading-interpretation middle band.

### Feasibility

Every explicit ask must be achievable with enabled tools and live data. There is no “minor secondary request” exception.

For each ask, verify:

- the operation exists in `HarmonyGames_Base_Universe/6_Server_Tools_Details.json`;
- the needed entity and facts exist and are discoverable;
- each requested “by X” or “per X” breakdown has an actual queryable X dimension;
- each exact number or precision is exposed by the Agent's tool path, or every input for a prompt-authorized derivation is visible.
- every required Gmail, Slack, GCal, or Drive-family (GDrive/GDocs/GSheets/GSlides) fact is visible to the exact
  assigned roster persona.

A value in raw JSON does not make an ask feasible when the tool-visible response rounds, truncates, coerces, or omits it.

Required Gmail, Slack, GCal, or Drive-family (GDrive/GDocs/GSheets/GSlides)
evidence inaccessible to the assigned persona is a hard feasibility failure
unless the intended task outcome is an affirmative access-denial finding plus
reporting, escalation, or an authorized alternative. Do not apply persona read
scoping to the other six services (Contacts, GitHub, Snowflake, Trello, Linear,
Confluence), and do not infer write denial from Persona ACL.

### Clarity, truthfulness, and time

- Different reasonable readings that produce different writes are **Action Decision Ambiguity** and fail.
- Scan first-person statements such as “I'll post the update” beside Agent imperatives. If the user could reasonably be reserving the action, the prompt is ambiguous.
- One wrong tight identifier—channel, repository, file path, document ID, email, date, ticket or issue ID—is a major factual error.
- Resolve relative dates from February 28, 2026 and verify that the relevant records exist in the resolved window.
- Ignore the auto-generated `_changelog.timestamp` value for date-alignment scoring.

### Natural complexity

The prompt must require >15 necessary calls, 2+ genuine services, multiple meaningful writes, and information friction. It also must be:

- tool-dependent;
- investigative rather than pre-solved;
- one causally connected situation rather than bolted asks;
- natural for the assigned persona and business function;
- free of MCP function names and parameter instructions;
- difficult because of the data and reasoning, not arbitrary formatting, scripted search order, repeated reads, or call inflation.

### Persona

Resolve the taxonomy-selected persona through one exact roster entry and keep
its five identity fields unchanged through Agent Runner and Run Verifiers. The roster
covers Design, Engineering, Executive, and Product; it has no Finance persona
or CFO. A Finance/Legal/HR business-function task therefore needs a plausible
assigned roster role, not an invented identity. Do not use the AMV persona
dropdown because it overrides the taxonomy selection.

## Universe QC

Use the live environment for existence and tool visibility. For Gmail, Slack,
GCal, and the Drive-family (GDrive/GDocs/GSheets/GSlides), test visibility as the
assigned roster persona; author god-mode is not a reachability check. Current
HarmonyGames paths include:

- `HarmonyGames_Base_Universe/Services_Data/slack/messages/<channel>/<YYYY-MM>.json`
- `HarmonyGames_Base_Universe/Services_Data/linear/linear.issues.json`
- `HarmonyGames_Base_Universe/Services_Data/github/github.<table>.json`
- `HarmonyGames_Base_Universe/Services_Data/github/root/`
- `HarmonyGames_Base_Universe/Services_Data/gmail/threads/<thread>.json`
- `HarmonyGames_Base_Universe/Services_Data/gdrive/gdrive.drive_files.json`
- `HarmonyGames_Base_Universe/Services_Data/gdocs/gdocs.docs_documents.json`
- `HarmonyGames_Base_Universe/Services_Data/gsheets/gsheets.sheets_spreadsheets.json`
- `HarmonyGames_Base_Universe/Services_Data/gslides/gslides.slides_presentations.json`
- `HarmonyGames_Base_Universe/Services_Data/gcal/gcal.events.json`
- `HarmonyGames_Base_Universe/Services_Data/trello/trello.<table>.json`
- `HarmonyGames_Base_Universe/Services_Data/confluence/confluence.<table>.json`
- `HarmonyGames_Base_Universe/Services_Data/contacts/contacts.contacts.json`
- `HarmonyGames_Base_Universe/Services_Data/snowflake/snowflake.tables.json`

This checkout contains the full base export. High-volume payloads are stored in
full service-level JSON files or shards (for example, Slack messages and Gmail
threads). Use task `3_UniverseDataForThisTask.json`, `4_Changelog.json`,
`9_Universe_inject.sql`, and live service responses for task-specific changes
and tool-visible rendering.

## Oracle Event QC

Run [`../Evals/2_OE_Eval.md`](../Evals/2_OE_Eval.md).

### Authority

OEs are internal plans. They prove intended solvability and help map work to rubrics, but they are not ground truth.

- An OE cannot override prompt language or universe data.
- An OE saying two paths are valid is not evidence that the prompt is ambiguous.
- An OE-only error is Non-Fail.
- If the OE error propagates into prompt feasibility, rubric correctness, or coverage, score the resulting prompt or rubric defect.

### Completeness and accuracy

Each OE should state an affirmative tool-use event, the exact tool and relevant parameters, and its expected observable result. Verify all of those against the catalogs and live data.

Prohibitions and inactivity are not events. Do not create an OE that only says the Agent refrains from a write. A real lookup that confirms an unresolved or absent implementation is valid because the lookup is observable.

OEs are Non-Fail dimensions, but inaccuracies must be corrected before rubric evaluation.

### Negative events

Oracle Events must describe an observable action or discovery; a non-action is not an event. Scan each OE for `does not`, `must not`, `never`, `no action`, and `refrains from`. A lookup that confirms an absent or negative factual state stays valid because the lookup is observable.

- Bad: “The Agent does not change the ticket status.”
- Valid: “The Agent looks up the ticket status and finds it unresolved.”

This dimension is purely non-failing: flag any non-action-as-event as a `[Non-Fail - OE Framing]` concern.

## Rubric JSON schema

The stored task object has exactly four fields:

```json
{
  "title": "The Agent reports that ZOM-387 is the Giant Analytics Ticket.",
  "category": "Outcome 2.1",
  "justification": "The user asked the Agent to identify the relevant Zombie Match analytics issue.",
  "evidence": "Inspect the Agent's final response for the stated issue identity."
}
```

`title` stores the criterion text. Evaluator prose may refer to it as the **Criterion** field; do not add a separate `criterion` key.

Valid category values:

- `Outcome 1.1` — write-action result;
- `Outcome 1.2` — write-action content;
- `Outcome 2.1` — a fact or conclusion the user asked to receive;
- `Process` — rare, non-write verification that passes the three-condition test.

All four values must be non-blank. `justification` explains why the rubric exists. `evidence` tells the reviewer where to inspect. Neither may add an acceptance-bearing value or requirement missing from `title`.

## Rubric hard gates

Run [`../Evals/3_Rubrics_Eval.md`](../Evals/3_Rubrics_Eval.md), then the final gate in [`../Evals/5_Submission_Gate_Eval.md`](../Evals/5_Submission_Gate_Eval.md).

### Self-containment

Hide `justification` and `evidence`. The `title` must still define the complete accepted answer, including every needed identifier, value, status, destination, and action target.

Acceptance must be verifiable from the trajectory, final response, visible
action arguments, or evidence visible to the same assigned verifier persona. A
criterion cannot depend on hidden tool-return content, merely require that a
tool reported success, or rely on hidden cross-persona state.

### Atomicity

One criterion tests one independently pass/fail condition. Split independent actions, facts, recipients, records, and content requirements completely.

“At least N” is non-atomic when it compresses independently gradable items. Valid exceptions are:

- tightly coupled facts that necessarily pass or fail together;
- one naturally atomic record or cell value;
- one exact global invariant.

For a qualifying large audit table, overall totals or reconciliation plus representative **atomic** spot checks may replace one criterion per repeated cell. There is no minimum number of spot checks. All non-repetitive requirements still need direct coverage.

### Forward coverage and destination

Map every authorized requirement from the prompt or a validly incorporated live source:

- actions and write content;
- facts, findings, and conclusions;
- recipients and destinations;
- conditions, qualifiers, timing, order, and format;
- exclusions and prohibited actions.

Coverage on the wrong artifact does not count. A fact required in a Slack post is not covered by a final-response-only rubric.

### Specificity and accepted answers

The prompt and validly incorporated live sources set the specificity ceiling. A rubric may embed the universe-grounded answer to an authorized question, but it may not add a method, format, threshold, destination, qualifier, or content item the request did not require.

- Use exact matching for IDs, emails, dates, counts, and other one-correct structured values.
- Use an objective semantic acceptance rule for Agent-generated text.
- Define the complete accepted set when several values are valid.
- Do not use `such as`, `e.g.`, or `for example` in any rubric field. Each affected rubric is one Moderate **Vague Exemplar Language** issue.
- Verify quantitative values at both raw-universe and tool-visible layers.

### Agent-centric, affirmative criteria

Every `title` must attribute an affirmative action or observable state to **The Agent** and must not name a tool.

Valid patterns:

- “The Agent reports that the Season Pass issue remains unresolved.”
- “The Agent classifies the CodeRabbit-only review outside the human-approved set.”
- “The Agent leaves the production configuration unchanged.”
- “The Agent confines repository activity to inspection.”

Invalid passing conditions define only prohibition or absence: “The Agent does not…”, “makes no…”, “never…”, “avoids…”, “refrains from…”, or equivalent `without` constructions.

ACL criteria of the form “The Agent does not access…” are likewise invalid when
the prohibition alone defines passing. Grade an affirmative access-denial
finding, scope boundary, report, escalation, or authorized alternative.
Negative factual states such as `unresolved`, `unimplemented`, `unconfirmed`,
and `access denied` remain valid when the Agent affirmatively reports or
classifies them. Affirmative wording must preserve exclusion coverage.

### Negative criteria

This is a focused, standalone check on affirmative framing, scored separately from Agent-centric phrasing. Every rubric `title` tied to a normal prompt instruction must be affirmatively framed; only an explicit non-action or prohibition instruction may be graded through negative wording. Pre-scan for `does not`, `must not`, `never`, `no`, `without`, `fails to`, and `avoids`, then review each hit.

A negative indicator that only describes the reported content is acceptable:

- Valid: “The Agent reports that PR #438 had no human-submitted review.” The actor and action (“The Agent reports…”) are affirmative and “no human-submitted review” only names the content being checked.
- Bad: “The Agent does not omit the ENG-1797 link.”

A criterion fails `[Fail - Criteria Framing]` only when it does not correspond to an explicit non-action or prohibition instruction yet is framed negatively.

### Process rubrics: three conditions

Write a Process rubric only when all three are true:

1. **Required by every valid path** — or phrased broadly enough to accept every valid path.
2. **Outcome cannot cover it** — a stricter Outcome cannot prove the same requirement.
3. **Verification, not execution trace** — it describes observable verification, not a tool, query, parameter, call sequence, or thought trace.

Write actions are always Outcome. Most tasks should have zero Process rubrics.
Exactly one invalid Process criterion is Non-Fail for the Process Rubrics scored
dimension (and remains a Moderate issue in the quality tally); two or more
invalid Process criteria fail that dimension. A missing Process criterion is
reported only for a sequential or causal dependency that Outcomes cannot
verify, and remains Non-Fail. Outcome is mandatory and Process must be no more
than 40% of the rubric set. This is a safety cap, not a target ratio; zero
Process is valid.

### Duplicates and all-failing rubrics

Compare every rubric pair. Exact copies and semantic paraphrases grading the same requirement on the same artifact are defects.

An all-failing rubric is one that fails every **completed** run; errored runs are excluded. Review each all-failing rubric for grounding, feasibility, affirmative wording, self-containment, numeric visibility, and fairness. An environment-driven failure is not a valid model failure.

## Rubric quality thresholds

For counted quality issues, use the number of authored criteria as denominator and count each criterion once at its highest severity:

- Fail when **>10%** contain Major issues.
- Fail when **>15%** contain Moderate-or-Major issues.
- Fail when **>20%** contain Minor-or-higher issues.
- Pass quality when there are no Major or Moderate issues and **<5%** contain Minor issues.

Independent hard gates still block submission even when a percentage threshold would not.

## Trajectory QC

- At least **4 of 6** runs must complete successfully. Three or more errors fail.
- Empty trajectory files are errored runs, not rubric failures.
- At most **2 of 6 completed runs** may pass all valid rubrics: `pass@1 <= 40%`.
- The completed-trajectory average must be **>=15 calls**.
- Review failure matrices at the per-rubric, per-run level. Use [`../Evals/4_Verifier_Fails_Eval.md`](../Evals/4_Verifier_Fails_Eval.md) to classify Rubric Invalid, Tool Precision Mismatch, Judge Error, Legitimate Fail, or Excluded.
- Exclude automatic `set_acting_user` configuration from call counts and do not
  credit ACL-denied calls or repeated denied retries as useful complexity.
- Diagnose access-sensitive failures under the same persona as the run. A
  record visible only to Universe Explorer or another persona cannot turn an
  environment/reachability defect into a valid model failure.

## Legacy-example rule

Older tasks, screenshots, external links, and changelog prose are historical context only. If a legacy example contains another universe's entities, negative criterion wording, a non-current Process rule, a tool-gated rubric, or a capability absent from the current catalogs, label it legacy and do not copy it. Current HarmonyGames data, machine QC, and Evals control.

See [`README.md`](README.md) for the documentation map and [`9_Common_Error.md`](9_Common_Error.md) for current HarmonyGames examples.
