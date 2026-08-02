# HarmonyGames Common Errors and Fixes

Use this guide with [`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json), [`8_QC_Spec_Doc2.md`](8_QC_Spec_Doc2.md), and the ordered [`../Evals/`](../Evals/) playbooks. Validate every capability against [`../HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/). Examples explain a rule; they never create a tool, entity, or accepted grading path.

## Prompt errors

### Giving away discoveries

**Problem:** The prompt includes the ticket, repository, channel, value, or cause the Agent should discover.

❌ “Check ENG-2319 and tell me why the Season Pass rewards were broken.”

✅ “The Season Pass rewards still seem wrong after the latest fixes. Figure out what is actually unresolved and get the right follow-up moving.”

Keep realistic context, but remove answer-bearing details and internal IDs a colleague would not naturally supply.

### Writing a tool script

**Problem:** A command list prescribes the search path and removes investigation.

❌ “Search Gmail, then inspect Linear, then check GitHub, then post in Slack.”

✅ “The Zombie Match launch status does not line up across the team. Reconcile what shipped, what is still blocked, and make sure the owners have an accurate next step.”

Prompts describe a situation and goal. Oracle Events—not prompts—record exact tools and parameters.

### Naming MCP functions or parameters

❌ “Call `linear_list_issues` with the `query` parameter, then use `slack_send_message`.”

✅ “Review the open live-ops work and notify the responsible owner.”

A natural product reference can still be awkward enough for a Non-Fail finding when it says “use the Linear MCP server” or “use the Slack tool.”

### Pre-solving the root cause

❌ “The latest `match3d` change caused the reward regression; create a follow-up issue.”

✅ “The reward regression returned after the latest release. Work out whether the code, ticket status, and team discussion agree, then take the needed follow-up actions.”

The Agent should connect evidence rather than repeat the prompt's conclusion.

### Bolting unrelated asks together

❌ “Check a Zombie Match bug, summarize the Mattel pitch, schedule an unrelated design meeting, and update a Trello card for Combo Fighter.”

✅ “The Zombie Match release review is tomorrow. Reconcile the open reward bugs, make sure the release tracker reflects reality, and get the unresolved ownership gaps in front of the people who need to act.”

Every ask in the good version supports one release-review outcome. Remove-any-sentence is a useful test: if a sentence has no causal relationship to the rest, it is probably a bolt-on.

### Requesting unavailable actions

Gmail can read, search, inspect attachments, and perform mailbox or label triage. It cannot send, reply, compose, or draft.

❌ “Reply to the Mattel email.”

✅ “Review the Mattel thread, capture the outstanding points in a Drive brief, and notify the founders through an enabled collaboration surface.”

Snowflake is query/read-only. Products without a catalog—Singular, AppLovin, Firebase, BigQuery, Metabase, Figma, Stripe, and others—may appear as topics or evidence inside enabled services, but they are not direct tools.

### Creating action ambiguity

**Problem:** Two readings lead to different writes or act-versus-defer outcomes.

❌ “I’ll post the release update once you check the tickets.”

This normally reserves the post for the user, while another reader may treat it as part of the delegation.

✅ “Check the tickets and post the release update.”

Also fail prompts where the literal request says to act now but a referenced record plausibly says to wait for approval, unless the prompt resolves which instruction controls.

### Using broken relative time

HarmonyGames today is **February 28, 2026**, America/Chicago.

❌ “Summarize what happened next week.”

✅ “Summarize the February release activity and schedule the review for next Friday.”

“Next Friday” resolves to March 6, 2026. Verify that future work is treated as future and that any requested historical window contains relevant records. See [`6_Prompt_Relative_Time_Updates.md`](6_Prompt_Relative_Time_Updates.md).

### Confusing the complexity thresholds

Do not substitute one threshold for another:

- Authoring target: **40+ average calls and 3+ services**.
- Prompt-eval hard gate: **>15 necessary calls**, 2+ genuine services, multiple meaningful writes, and information friction.
- Trajectory QC floor: **>=15 average observed calls**.

A task that can be solved in 12 calls fails the prompt gate even when an inefficient run makes 42 calls.

## Persona ACL errors

Use [`15_Persona_ACL.md`](15_Persona_ACL.md) with the exact
[`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json)
entry. Persona ACL is active and applies to reads only.

### Guessing or rewriting the persona email

**Problem:** The selected name is paired with a constructed, normalized, or
wrong email instead of the roster value.

✅ Copy the exact `persona_key` and `email` from the 17-entry roster into the
task identity. A wrong email changes Gmail, Slack, GCal, and Contacts
visibility and is a Persona, Truthfulness, and Feasibility defect.

### Letting AMV override Taxonomy

**Problem:** The AMV persona dropdown is changed after Taxonomy selection. Its
persisting override can run the Agent and verifier as the wrong person.

✅ Leave AMV untouched. Keep the Taxonomy-selected roster persona unchanged for
Agent Runner and every Run Verifier. Automatic `set_acting_user` application is
environment configuration, not Agent work or a rubric/process/call-count item.

### Using Explorer-only proof of feasibility

**Problem:** Universe Explorer or a local export contains the required record,
so the author assumes the Agent can read it.

✅ Explorer is author god-mode. Re-test required Gmail, Slack, GCal, and Contacts
evidence from the assigned persona's Runner/Verifier view. Required
scoped-service evidence that persona cannot reach hard-fails the task unless
the intended outcome is an affirmative access-denial finding plus reporting,
escalation, or an authorized alternative.

### Applying ACL to the public-service group

**Problem:** The author invents persona read filters for GDrive, GitHub,
Snowflake, GDocs, GSheets, GSlides, Trello, Linear, or Confluence—or interprets
“public-service group” as public outside the evaluation environment.

✅ Those nine services are unscoped across task personas. Only Gmail, Slack,
GCal, and Contacts reads are persona-scoped. “Unscoped” means shared across task
personas, not Internet-public.

### Assuming ACL denies writes

**Problem:** A prompt, OE, or rubric assumes that read scoping prevents a write,
including writes on Drive, Docs, Sheets, or Slides.

✅ Writes are outside Persona ACL scope. Determine every write solely from
[`HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/); never infer write denial from persona read
visibility.

### Blocked-call inflation

**Problem:** The task clears a call target only by probing inaccessible records
or repeating a denied read.

✅ Build membership-aware searches from persona-visible anchors or authorized
unscoped sources. ACL-denied calls and denied retries are not necessary work and
do not count toward prompt complexity, long-horizon scale, or useful trajectory
depth.

## Oracle Event errors

### Treating OEs as ground truth

**Problem:** An OE is used to override the prompt or live data.

Oracle Events are contributor-internal plans. If an OE says a ticket is open but the live, tool-visible issue is closed, the OE is inaccurate. If an OE says two paths are valid, that statement alone does not prove the prompt has multiple ground truths.

An OE-only error is Non-Fail. Investigate whether it propagated into prompt feasibility, rubric correctness, or missing coverage.

### Skipping discovery steps

❌ “Post the blocker update to the responsible engineer.”

✅ “Resolve the responsible engineer and valid collaboration destination from the relevant HarmonyGames records, then post the blocker update to that destination.”

The OE should include the exact cataloged tools and parameters once the intended path is known.

### Writing conclusions instead of tool-use events

❌ “The Agent discovers that the Season Pass issue is unresolved.”

✅ “Retrieve the relevant Linear issue using the exact cataloged Linear read operation; expected result: the issue's current state and assignee are returned.”

The second form is an observable lookup with an expected result.

### Turning a prohibition into an event

❌ “The Agent does not modify the production configuration.”

No action occurs, so this is not an Oracle Event.

✅ “Inspect the production configuration and confirm the affected setting remains unchanged.”

This is valid only when the lookup itself is required and observable. Preserve the prompt's exclusion in an affirmative Outcome rubric such as “The Agent leaves the production configuration unchanged.”

### Ignoring numeric visibility

For every OE amount, rate, count, or derived number, verify:

1. the canonical value and inputs in the universe;
2. the exact value and precision the cataloged tool path exposes;
3. whether the prompt explicitly authorizes any derivation.

A raw decimal hidden behind a rounded service response cannot support an exact OE claim.

## Rubric errors

### Using the wrong JSON field names

Task `7_Rubrics.json` objects use:

```json
{
  "title": "The Agent reports that ZOM-387 is the Giant Analytics Ticket.",
  "category": "Outcome 2.1",
  "justification": "The user requested the identity of the relevant analytics issue.",
  "evidence": "Inspect the Agent's final response for the issue identity."
}
```

`title` is the criterion text. Evaluator prose may call it the **Criterion** field; do not serialize a separate `criterion` key. All four values must be non-blank.

### Hiding acceptance rules in justification or evidence

**Problem:** `title` says “the right issue,” while `evidence` supplies `ZOM-387`.

❌ **title:** “The Agent reports the correct unresolved issue.”

✅ **title:** “The Agent reports that ZOM-387 is the Giant Analytics Ticket.”

Hide `justification` and `evidence`; the title must still define exactly what passes.

### Writing non-agent-centric or negative criteria

❌ “A status update was posted.”

❌ “The Agent does not treat the CodeRabbit review as human approval.”

✅ “The Agent posts the status update.”

✅ “The Agent classifies the CodeRabbit-only review outside the human-approved set.”

Every title must express an affirmative action, classification, scope boundary, or preserved state attributable to **The Agent**. Do not name tools. Negative factual states remain valid when affirmatively reported: “The Agent reports that implementation remains unconfirmed.”

### Bundling independent conditions

❌ “The Agent posts the release summary, updates the Linear issue, and creates the calendar event.”

✅ Split into three criteria, one per write.

Also split independent content requirements and records. “At least three issues are updated” is non-atomic when each issue can pass or fail independently.

Valid bundling is narrow: tightly coupled facts with one shared result, one naturally atomic record or cell, or one exact global invariant.

### Missing requirement-level coverage

“Message posted” does not cover:

- the required recipient or destination;
- each required content item;
- an order or timing rule;
- a requested user-facing conclusion;
- a prohibited action or decoy exclusion.

Map every authorized requirement to the correct artifact. A final-response fact does not cover content required in a Slack post. Every required write needs Outcome 1.1; prompt-specified write content needs Outcome 1.2; every requested fact or conclusion in the reply needs Outcome 2.1.

For a qualifying large audit table, overall reconciliation plus representative atomic spot checks may replace one rubric per repeated cell. There is no minimum spot-check count, but all non-repetitive requirements still need direct coverage.

### Writing a Process rubric that Outcome can cover

Use the Outcome-first workflow:

1. Write all Outcome 1.1, 1.2, and 2.1 criteria.
2. Identify any remaining sequential or causal dependency that the Outcomes cannot verify.
3. Add Process only when all three conditions pass.

The three-condition Process test:

1. **Required by every valid path** — or broad enough to accept every valid path.
2. **Outcome cannot cover it** — a stricter Outcome cannot prove the same requirement.
3. **Verification, not execution trace** — no tool, query, parameter, call order, or thought trace.

❌ “The Agent calls `linear_get_issue` before `slack_send_message`.”

✅ “The Agent verifies the current issue state before notifying the release owner.”

The good criterion is valid only when every correct path requires that ordering
and no Outcome can prove it. Most tasks need zero Process rubrics. Write actions
are always Outcome, Outcome is mandatory, and Process may not exceed 40% of the
set.

### Locking a goal to one method

If the prompt says “notify Brian,” a rubric must not force one service when several prompt-authorized enabled surfaces are valid.

❌ “The Agent posts in `#season-pass`.”

✅ “The Agent notifies Brian Foster at brian@harmonygames.co through an enabled collaboration surface.”

Use the exact method only when the prompt or a validly incorporated live source requires it.

### Using vague exemplar language

Rubric fields must not use `such as`, `e.g.`, or `for example`.

❌ “The Agent's summary covers risks such as stale tickets and missing review.”

✅ Split or state the complete accepted meaning explicitly.

Each affected rubric is one Moderate **Vague Exemplar Language** issue, regardless of the number of phrases or fields.

### Using “approximately” for exact values

❌ “The Agent reports approximately 3 unresolved issues.”

✅ “The Agent reports 3 unresolved issues.”

Use exact matching for counts, IDs, dates, emails, and other one-correct structured values. Use approximate or range matching only for calculations or rounded values where variation is expected and tool-visible.

### Depending on hidden tool results

❌ “The Agent's update succeeds.”

The judge cannot grade hidden infrastructure success as the acceptance target.

✅ “The Agent posts the required update to the specified destination.”

Final-response content and visible write arguments are gradeable. Tool results may be used by evaluators to diagnose feasibility or environment errors, not as hidden acceptance evidence.

### Keeping duplicate rubrics

Compare every pair. If two criteria have the same pass/fail signal for the same requirement on the same artifact, remove or rewrite one.

Outcome 1.1 action-result and Outcome 1.2 content checks are distinct. The same fact required in two different deliverables is also distinct.

### Trusting all-failing criteria automatically

A rubric that fails every completed run may reflect:

- a genuine model miss;
- a wrong expected value;
- inaccessible precision;
- negative or non-agent-centric wording;
- an impossible action;
- a judge error;
- an environment failure.

Exclude errored runs, inspect the trajectories, and add a grounded 1–2 line justification only when the rubric is valid. Use [`../Evals/4_Verifier_Fails_Eval.md`](../Evals/4_Verifier_Fails_Eval.md).

## Current HarmonyGames data checks

Use the live environment for final truth. Common local verification paths are:

- [`../HarmonyGames_Base_Universe/Services_Data/slack/`](../HarmonyGames_Base_Universe/Services_Data/slack/)
- [`../HarmonyGames_Base_Universe/Services_Data/linear/`](../HarmonyGames_Base_Universe/Services_Data/linear/)
- [`../HarmonyGames_Base_Universe/Services_Data/github/`](../HarmonyGames_Base_Universe/Services_Data/github/)
- [`../HarmonyGames_Base_Universe/Services_Data/gmail/`](../HarmonyGames_Base_Universe/Services_Data/gmail/)
- [`../HarmonyGames_Base_Universe/Services_Data/gdrive/`](../HarmonyGames_Base_Universe/Services_Data/gdrive/)
- [`../HarmonyGames_Base_Universe/Services_Data/gdocs/`](../HarmonyGames_Base_Universe/Services_Data/gdocs/)
- [`../HarmonyGames_Base_Universe/Services_Data/gsheets/`](../HarmonyGames_Base_Universe/Services_Data/gsheets/)
- [`../HarmonyGames_Base_Universe/Services_Data/gslides/`](../HarmonyGames_Base_Universe/Services_Data/gslides/)
- [`../HarmonyGames_Base_Universe/Services_Data/gcal/`](../HarmonyGames_Base_Universe/Services_Data/gcal/)
- [`../HarmonyGames_Base_Universe/Services_Data/trello/`](../HarmonyGames_Base_Universe/Services_Data/trello/)
- [`../HarmonyGames_Base_Universe/Services_Data/confluence/`](../HarmonyGames_Base_Universe/Services_Data/confluence/)
- [`../HarmonyGames_Base_Universe/Services_Data/contacts/`](../HarmonyGames_Base_Universe/Services_Data/contacts/)
- [`../HarmonyGames_Base_Universe/Services_Data/snowflake/`](../HarmonyGames_Base_Universe/Services_Data/snowflake/)

This checkout contains the full base export in service-level JSON and sharded
payloads. Combine it with task `3_UniverseDataForThisTask.json`,
`4_Changelog.json`, `9_Universe_inject.sql`, and live service reads for
task-specific state and tool-visible behavior. For Gmail, Slack, GCal, and
Contacts, test that behavior as the exact assigned roster persona; Explorer or
another persona's view is insufficient.

## Legacy examples

Examples from other universes, archived tasks, old screenshots, and external QC documents are **legacy calibration only**. Do not copy:

- other-universe entities, workflows, identifiers, or data models as HarmonyGames ground truth;
- any Process decision rule other than the current three-condition test;
- Query Construction or Tool Selection rubric categories;
- negative criterion wording;
- any capability absent from the current 13 catalogs.

Use [`README.md`](README.md) to locate the current documentation and [`../QC_Tasks/`](../QC_Tasks/) only for labeled calibration history.
