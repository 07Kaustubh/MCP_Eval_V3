## **Rubric Writing Guidelines**

---

Start with the [`Docs/README.md`](README.md) index. This document is the canonical rubric-authoring guide, and [`Evals/3_Rubrics_Eval.md`](../Evals/3_Rubrics_Eval.md) is the evaluation authority. When these guidelines discuss services, actions, tool calls, or parameters, [`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json) is authoritative. The prompt and live HarmonyGames evidence define requested work and ground truth. Oracle Events are non-authoritative planning notes: they can reveal a gap, but cannot override the prompt, universe, catalogs, trajectory, or current Evals.

## **Note: This doc has undergone some changes on July 23\. Please read the change log below carefully\!**

## **💡 Change Log Last Updated:** Jul 23, 2026

| Date | Type | Description |
| ----- | ----- | ----- |
| July 23, 2026 | Rubrics | Added the missing-Process dependency gate, large audit-table spot-check scaling with no minimum count, quantifier-based atomicity clarification, and Moderate Vague Exemplar Language. |
| June 03, 2026 | Rubrics | **Updates on Process rubrics and overall alignment.** |
| May 20, 2026 | Rubrics | **Established Outcome (mandatory) and Process (optional) as the only rubric categories.** Outcome is the default training signal. Process rubrics apply only when a necessary behavior cannot be captured by a stronger Outcome rubric. Removed fixed target ratios, retained the QC safety cap of no more than 40% Process, and standardized agent-action phrasing ("The Agent reports X" instead of "The summary mentions X"). |
| Apr 30, 2026 | Rubrics | **Clarified when Process rubrics are valid or should be removed or made flexible.** Remove Process criteria that merely restate an Outcome, and phrase necessary behavior broadly enough to accept valid alternative paths. |
| Apr 10, 2026 | Rubrics | Clarified how to distinguish necessary behavioral checks from unnecessary implementation-path constraints. |
| Mar 25, 2026 | Rubrics | **Atomic rubrics for multiple write actions of the same type:** When the prompt asks for multiple write actions (e.g., update all tickets, create tickets for all follow-up items), write one Outcome rubric per item grounded in GT — never bundle into "at least N" thresholds. "At least one/N" is reward-hackable and only acceptable when GT is genuinely indeterminate. |
| Mar 12, 2026 | Rubrics | **Updated rubrics and examples:** Use an Outcome-first workflow; write all write actions as Outcome rubrics and place key facts reported to the user in 2.1. Established the three Outcome sub-categories: 1.1 write-action results, 1.2 action content, and 2.1 key facts. Clarified that "approximately" applies to calculated or rounded values, not counts, IDs, dates, or discrete quantities. |
| Mar 12, 2026 | Failure Rate | Difficulty target clarified: 0% pass rate is acceptable as long as overall rubrics are high-quality and don’t lead to false negatives/invalid model failures.  |

---

## **What Are Rubrics?**

Rubrics are specific, checkable statements about what the AI agent should accomplish, report, classify, preserve, or keep within scope. Each rubric is a simple yes-or-no claim. An LLM judge reads the agent's trajectory and checks each rubric against what it finds there.

*You write the rubrics. The judge reads the trajectory. Pass or fail.*

### How the Judge Works

**The judge sees:**

* The original task prompt — what the agent was asked to do  
* The agent's trajectory — every tool call, its parameters, its response, and the agent's reasoning at each step  
* The agent's final response — the summary text at the end  
* Your rubric criteria

**The judge does NOT see:**

* The MCP environment directly (it cannot call tools itself)  
* The universe data (it only knows what appeared in the trajectory)  
* Other agents' results

**What this means for you:** Every expected value must be in the rubric itself. If you write "The Agent posted a Slack message to the co-founder," the judge doesn't know which co-founder is intended.

Instead write "The Agent posted a Slack message to leonard.hayes@harmonygames.co (Co-founder & Creative Director)."

---

## **Persona ACL and Rubric Feasibility**

Persona ACL is active. Read [`14_Persona_ACL.md`](14_Persona_ACL.md) for the
policy and use the exact persona key/email from
[`4_Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json).
The Agent Runner and Run Verifiers use the same assigned persona; Universe
Explorer is author god-mode and proves existence, not Agent reachability.

Apply ACL inside the normal Persona, Feasibility, Universe Reachability, and
Rubric Correctness/Self-Containment checks:

* **Persona-scoped reads:** Gmail, Slack, GCal, GDrive, GDocs, GSheets, and GSlides.
* **Unscoped reads:** Contacts, GitHub, Snowflake, Trello, Linear, and
  Confluence.
* **Writes:** outside ACL scope. Determine write feasibility from
  [`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json); never infer a write denial from read
  scoping.
* **Required persona-scoped evidence:** hard-fail a task when it is
  inaccessible to the assigned persona, unless the intended outcome is an
  affirmative access-denial finding plus reporting, escalation, or an
  authorized alternative.
* **Gradeable evidence:** a scoped verifier must be able to grade from the
  trajectory, final response, visible write arguments, or evidence visible to
  that same persona. Hidden cross-persona state cannot define passing.

`set_acting_user` is environment configuration applied from the exact roster
email. It is not Agent work, an Oracle Event, a rubric or Process requirement,
or a task/call-count item.

---

## **Phrasing Convention — Agent-Centric and Affirmative**

Frame every rubric as an affirmative behavior or observable state attributable to *the agent*, not a passive description of the artifact. This applies to both Outcome and Process rubrics.

| Avoid: tool/artifact-centric | Required: agent-centric |
| ----- | ----- |
| "A message was sent using a specific messaging function to Brian…" | "The Agent sends the summary to Brian Foster at brian.foster@harmonygames.co." |
| "The message body includes the bug details and status." | "The Agent's message to Brian includes the Season Pass reward bug details and a status comparison (fixed vs still open)." |
| "The Brian summary mentions the ZOM-299 daily login bug." | "The Agent reports in the summary to Brian Foster that ZOM-299 (daily login reset) is a known open issue." |

**Six phrasing rules:**

1. Subject \= *The Agent* (not the artifact).  
2. Drop implementation annotations and parameter callouts.  
3. Read it aloud — should sound natural, not like a test assertion.  
4. Process rubrics describe behavior, not execution traces ("checks Linear" — not "calls a specific listing function third").  
5. State acceptance affirmatively. Rewrite “The Agent does not change production” as “The Agent confines production activity to inspection” or “The Agent leaves the production configuration unchanged.” Likewise, reject prohibition-only ACL criteria such as “The Agent does not access another mailbox”; grade the requested finding, scope boundary, report, escalation, or authorized alternative instead. Negative factual states such as “unresolved” or “access denied” remain valid when the Agent affirmatively reports or classifies them.
6. Preserve source formatting: `ENG-2349`, `$6.99`, `Zombie Match 3D`, `Marcus Bennett`.

Affirmative wording does not remove exclusion coverage. If the prompt forbids a write, excludes a decoy, or limits scope, keep an atomic rubric for that requirement and express it as a classification, scope boundary, or preserved state.

---

## **Verb Cheat Sheet**

* **1.1 Write actions:** sends, creates, updates, posts, schedules, assigns  
* **1.2 Action content:** includes, mentions, states, covers, references, names  
* **2.1 Key facts:** identifies, reports, flags, lists, recommends, concludes  
* **Process:** verifies, confirms, checks, reviews, reconciles, notifies (before X)

---

### **Two Rubric Categories**

Every rubric belongs to one of two categories: Outcome or Process. These categories provide downstream ML teams with labeled training signals.

**Core rule:**

* Outcome rubrics are the default training signal, and should be encouraged.  
* Process rubrics are only for necessary, observable verification steps that cannot be captured cleanly by stronger outcome rubrics.  
* Default to making outcomes stricter and more specific (unguessable) rather than adding process rubrics.  
* **No rubric \- Outcome or Process \- penalizes a valid alternative solution path.** Where the prompt names a goal not a method, the rubric matches the prompt: "The Agent briefs Brian Foster," not "The Agent posts in #season-pass." A rubric that locks in one method will fail correct solutions that took a different valid route. See Handling Flexibility for the full pattern.
* There is no target Outcome/Process ratio, but Process may not exceed 40% of
  the set. Zero Process rubrics is valid.

---

### **Category 1: Outcome**

**What it checks:** What was accomplished? What does the user see?

This is where almost all of your rubrics live. Outcome rubrics describe what should have been achieved — verified from the trajectory, the final response, or both.

---

**Writing Outcome Rubrics**

Outcome rubrics use three sub-categories. Use only the ones that apply to your task.

**1.1 — Action Results**

Did the right action happen with the right details? Verified from the trajectory (tool call).

`The Agent posted a Slack message from julia.lawson@harmonygames.co to brian.foster@harmonygames.co.`

Use for: every write action. Always required when a write action exists.

**1.2 — Action Content**

Does the content match what was needed? Verified from the trajectory (tool call parameters).

`The Agent’s Slack message to Brian Foster includes which Season Pass reward bugs are fixed vs still open and mentions the specific ZOM ticket IDs.`

Use when: the write action has specific content requirements to be met. Only write 1.2 if it adds a distinct check beyond 1.1.

**2.1 — Key Facts / Findings (Final Response)**

Did the agent correctly report the right information to the user? Verified from the final response text.

`The Agent identifies that Owen Baker (match3d) is assigned to the sprite-optimization sprint (ENG-2370).`

Use when: the user asked to be told a specific fact — whether or not the task also includes write actions.

**Which Sub-Categories Apply**

| Task Type | 1.1 | 1.2 | 2.1 |
| ----- | ----- | ----- | ----- |
| Pure write action (post a Slack message, create an issue) | ✅ Always | ✅ If content requirements exist | ❌ |
| Pure investigation / summary to user | ❌ | ❌ | ✅ |
| Mixed: research then write | ✅ | ✅ | ✅ Only if user also asked to be told findings directly |

---

**A note about Tool Names in Task Sections**

Use natural language in prompts and rubric criteria. Do not mention implementation-specific tool names.

| Context | Rule |
| ----- | ----- |
| Task prompts | Never mention tool names |
| Rubrics | Never mention tool names |

✅ Adequate: `The Agent posted a Slack message to brian.foster@harmonygames.co.` 

❌ Avoid: `A message was sent via a specific messaging function to Brian.`

---

### **The Outcome-First Workflow**

Follow this sequence every time you write rubrics:

* **Step 1:** Write all Outcome rubrics first. For every action in your OEs, write 1.1 (action result) \+ 1.2 (content, if specific requirements exist). For every key fact the user asked to be told directly, write 2.1 (final response).  
* **Step 2 — Review the full rubric set for gaps no Outcome can cover.** After writing all Outcomes, ask: is there any requirement — explicit or implicit — that none of my Outcome rubrics can verify? The primary case is ordering between actions (A must happen before B, but both 1.1s pass regardless of sequence). In rare cases, source verification may also qualify — where the correct answer is available in a shallow source and the Outcome genuinely cannot be made specific enough to prove the agent checked the authoritative source. These are your candidates for Process rubrics.  
* **Step 3:** Apply the three-condition test to each candidate.   
  * Required by every valid solution path (or phrased broadly enough to allow alternatives).   
  * A stricter Outcome rubric cannot capture the same requirement.  
  * The rubric describes a behavioral property, not an execution trace.

---

### **Category 2: Process (Optional)**

**What it checks:** Whether the agent did necessary work that the final result alone cannot verify.

Process rubrics evaluate behaviors that are required for a trustworthy completion but invisible from the final state. They are framed as behavioral expectations (what the agent verified, confirmed, or did), not as checklists of specific tool calls.

**Verification that Outcomes alone cannot prove (Non-Exhaustive)**

1. **Ordering between actions.**   
   * "Notify legal before scheduling the meeting." The scheduling outcome doesn't prove the notification came first.  
2. **Investigation steps the agent could fabricate.**   
   * When the outcome can't be made specific enough to prove the underlying retrieval happened, a process rubric forces the legitimate path.

In most tasks neither situation applies and no process rubrics are needed.

**Bottom Line:**

Only add a Process rubric when a correct final output alone will not reliably prove that the request was done correctly, and the Outcome rubric cannot be tightened to capture the same requirement more cleanly.

## **Process Rubric Decision Flow**

**Before writing a Process rubric**, all **three conditions** below must be **true**:

1. **Required by every valid path**  
   * The behavior is necessary for trustworthy completion AND every valid solution path requires it — or the rubric is phrased broadly enough to pass any valid path. Prompt says "brief Brian before scheduling"? Rubric says "The Agent briefs Brian Foster," not "The Agent posts in #season-pass." A correct solution using another enabled collaboration surface should still pass.  
     1. **Note**: “Agent posts in #legal” is still a valid rubric if the prompt specifically requests a Slack post in `#legal`.  
2. **Outcome can't cover it**  
   * A stricter outcome rubric cannot capture the same requirement. When the outcome can check precise values pulled from available structured sources (a Snowflake amount, a GDrive PDF figure, derived math), the agent cannot fake the outcome without doing the underlying work — and the outcome alone is preferable.  
3. **The rubric describes a verification, not an execution trace.**  
   * The rubric describes what the agent did or verified in a way the judge can confirm from the trajectory — not which specific tool was called, or what the agent was "thinking."  
     1. ✅ "Agent confirmed the vendor terms in Gmail match the signed agreement in GDrive before updating the Trello card."  
     2. ❌ "Agent called specific Gmail, GDrive, and Trello functions in sequence." *(locks in one tool path; a valid agent using different tools would fail)*  
     3. ❌ "Agent understood the wire instructions could be a phishing attempt." *(no observable evidence — can't grade intent)*

If any condition fails, **do not write the process rubric** — either drop it or rewrite   
the corresponding outcome rubric to be stricter.

**Missing Process note (07/23):** Only identify a Process criterion as missing when the prompt contains a sequential or causal dependency related to it (staged steps, an earlier step gating a later one, etc.). If no such dependency exists, do not report a missing Process criterion. A genuinely missing dependency check is Non-Fail.

---

**Default to Stricter Outcome Rubrics**

Before considering any process rubric, consider **Step 2** of the *Process Rubric Decision Flow* 

* Can I make my outcome rubric more specific so that achieving it proves the behavior happened?

If the outcome can check precise values pulled from structured sources 

* a Snowflake amount, a figure from a GDrive PDF, a derived calculation, etc.

then the agent cannot fake the outcome without performing the underlying work. 

In those cases, a stricter outcome is always preferable to a process rubric.

---

### Examples:

**Example 1 / Outcome is enough (grounded HarmonyGames pattern):**

| Prompt context: |
| :---- |
|  `The Agent needs to reconcile the Axe Arena infinite-lives reward against the tracked intended value.`  |
| **❌ Do NOT write a Process rubric like:** |
|  `"The Agent searches the live-ops records and build discussion before reporting the timer discrepancy."` **Why this is bad:** The behavior is vague and adds no signal beyond the precise finding. |
| **✅ Instead, write a Strict Outcome rubric:** |
|  `"The Agent reports that ENG-2349 records the Axe Arena infinite-lives reward as 10 minutes in the build and 15 minutes as intended."` **Why this works:** The exact issue and direction make the Outcome specific enough to prove the relevant reconciliation. |

**Example 2 / Process is warranted (HarmonyGames workflow):**

|  Prompt context:  |
| :---- |
|  `The Agent must brief Brian Foster before scheduling the live-ops review.`  |
| **✅ Process rubric is appropriate:** |
|  `"The Agent briefs Brian Foster at brian.foster@harmonygames.co before scheduling the live-ops review."` **Why this works:** The communication and meeting each have an Outcome, but those Outcomes do not prove the required order. |

---

## **Handling Flexibility: How Strict Should a Rubric Be?**

***Outcome (1.1 / 1.2) — verified from trajectory:***

Write-action result — Strict: `The Agent posts a Slack message from leonard.hayes@harmonygames.co to brian.foster@harmonygames.co.`

Slack message topic — Flexible: `The Agent’s Slack message communicates the current Season Pass reward-bug status; wording may vary without changing that meaning.`

Action content — Strict (exact value from data): `The Agent’s message states that ENG-2349 records the Axe Arena timer as 10 minutes shipped and 15 minutes intended.`

Action content — Flexible (calculated or rounded value): `The Agent’s message includes an estimated monthly impact of approximately $12,500.`

Action content — Flexible (Required Elements): `The Agent’s message must include: (a) which bugs are fixed, (b) which bugs are still open, and (c) the assignee for unresolved tickets.`

***Outcome (2.1) — verified from final response:***

Key facts — Strict: `The Agent identifies Owen Baker (match3d) as the assignee for the sprite-optimization sprint (ENG-2370).`

Key facts — Flexible: `The Agent identifies the Zombie Match 3D retention trend as broadly flat; wording may vary without changing that meaning.`

**Quick Reference**

| Situation | Pattern | Example |
| ----- | ----- | ----- |
| One correct value / fact | Strict (EM) | "brian.foster@harmonygames.co" |
| Freetext parameter or agent-generated label | Flexible (Fuzzy) | Define an objective meaning: "a title semantically equivalent to Zombie Match 3D live-ops health" |
| Agent content with specific requirements | Required Elements | "must state the shipped timer, intended timer, and issue ID" |
| Similar entities, one correct | Selection Logic | "Marcus Lee, the UA manager, rather than Marcus Bennett, the artist" |
| Goal named, not method | Method-agnostic | "The Agent notifies Brian Foster" rather than "The Agent posts in #season-pass" if the prompt did not name a channel |

---

## **Stored Schema and Conceptual Criterion**

Each rubric object in `7_Rubrics.json` stores exactly four required fields:

1. **`title`** — stores the criterion text: the specific yes/no claim the judge evaluates. It must be self-contained, objective, atomic, affirmative, agent-centric, and verifiable.
2. **`category`** — `Outcome 1.1`, `Outcome 1.2`, `Outcome 2.1`, or `Process`.
3. **`justification`** — 1–2 sentences explaining why the rubric exists and connecting it to an authorized requirement.
4. **`evidence`** — where a reviewer should look in the trajectory or final response.

“Criterion” is a conceptual term, not a separate storage key. The criterion is the acceptance statement stored in `title`. Hiding `justification` and `evidence` must leave the full accepted answer clear; those support fields cannot introduce an ID, value, status, destination, or other fact needed to know what passes.

```json
{
  "title": "The Agent reports that ZOM-387 is the Giant Analytics Ticket.",
  "category": "Outcome 2.1",
  "justification": "This checks the requested analytics-ticket identification against HarmonyGames ground truth.",
  "evidence": "Check the Agent's requested deliverable for the exact ticket identity."
}
```

---

**Service Metadata Requirements**

Rubrics missing metadata are incomplete. Always include the required fields per service.

Gmail triage — must include: target message/thread, mailbox/user when relevant, and the requested triage operation or label

Slack — must include: Recipient (channel name or DM recipient), Content (specific items the message must mention — list individually)

Linear — must include: Title (what the issue title should contain), Assignee (if specified), Priority (if specified), Subtasks (count and coverage if applicable)

| Incomplete | Complete |
| ----- | ----- |
| "Agent messaged the product owner" | "The Agent sends the live-ops brief to Brian Foster at brian.foster@harmonygames.co." |
| "Message sent about live-ops bugs" | Two atomic criteria: "The Agent posts in `#season-pass`." and "The Agent distinguishes fixed Season Pass bugs from open Season Pass bugs in that message." |

---

## **How to Write Good Rubrics — Rules**

**Rule 1: Be Self-Contained**

The judge can't look anything up. Include all expected values.

| Bad | Good |
| ----- | ----- |
| "Message sent to the CTO" | "The Agent posted a Slack message to arthur.blake@harmonygames.co (CTO, Arthur Blake)" |
| "The timer is correct" | "The Agent reports that ENG-2349 records the Axe Arena timer as 10 minutes shipped and 15 minutes intended." |
| "Slack message has enough context" | "The Agent's Slack message to Brian Foster states the Axe Arena shipped timer and intended timer." |
| "Agent contacted the right person" | "The Agent posts a Slack message to brian.foster@harmonygames.co (Brian Foster)" |

**Rule 2: One Thing Per Rubric, No Overlaps, No Gaps**

Each rubric must check exactly one independent claim.

Quantifier-based bundling such as `"at least N"` is not atomic when it compresses multiple independently pass/fail items into one criterion. The same applies to any compound phrasing that packs multiple pass/fail conditions into one criterion, outside the bundling exceptions below.

| Bad | Good |
| ----- | ----- |
| "The Agent's Slack message mentions the Axe Arena timer, Collect & Win reward mismatch, and Leaderboard bug" | Three rubrics: one per independently verifiable content item |
| "The Agent created a Linear issue for Douglas and posted a Slack message to Brian" | Two rubrics: (1) Linear issue created for Douglas / (2) Slack message sent to Brian |

**Bundling exception:** 

* Tightly coupled facts may be bundled in two cases  
* Same action: identifiers checked together in one action   
  * (for example, "The Agent posted a Slack message mentioning brian.foster@harmonygames.co and leonard.hayes@harmonygames.co" — both are visible in the same message parameters);   
  * Same data point: facts from a single record that are meaningfully inseparable   
  * (e.g., "The Agent identifies Owen Baker (match3d) as the assignee for the sprite-optimization sprint" — name, repo, and sprint assignment all come from the same Linear ticket and would pass or fail together).   
* Use judgment: if two claims could plausibly fail independently, split them.

**Rule 3: Must Be Verifiable from the Trajectory or Final Response**

| Bad (unverifiable) | Good (verifiable) |
| ----- | ----- |
| "Message exists in Slack channel" | "The Agent posted a Slack message to brian.foster@harmonygames.co" |
| "Calendar event was created" | "The Agent creates the live-ops review event for March 6, 2026 with Brian Foster and Leonard Hayes as attendees." |
| "The Agent understood the problem" | "The Agent identifies ZOM-387 as the Giant Analytics Ticket." |

**Rule 4: Use "Approximately" for Calculated or Rounded Numbers**

✅ `Cost is approximately $12,500`

✅ `Cost is between $12,000 and $13,000`

❌ `Cost is $12,487.50` — too precise, agent won't match this exactly

Do NOT use "approximately" for fixed, static values:

* Counts: "3 overdue tasks" — not approximately 3  
* IDs: "issue OPS-312" — not approximately OPS-312  
* Dates: "February 24, 2026" — not approximately Feb 24  
* Discrete quantities from the data: "5 live-ops features" — if the data has exactly 5, say 5

**Rule 5: Handle Multiple Valid Answers Explicitly**

| Phrasing | Meaning |
| ----- | ----- |
| "must be one of: `#season-pass` or `#zombie-bugs`" | Closed — only these are correct |
| "any grounded open Zombie Match 3D live-ops discrepancy" | Open — use an objective semantic rule rather than an illustrative list |
| "at least one of: ENG-2402 or ENG-2349" | Any single one is sufficient |

Never use `"such as"`, `"e.g."`, or `"for example"` in a rubric. Each affected rubric counts as one **Moderate — Vague Exemplar Language** issue. Define the accepted set or semantic rule directly.

---

## **Before Writing Rubrics: Plan Your Oracle Events**

Before writing any rubrics, map out the Oracle Events (OEs) — the key steps a perfect agent would take to solve the task. Write these as free-form text describing:

* What critical actions need to happen (post a Slack message, create an issue, triage a Gmail thread, etc.)  
* What information needs to be discovered (which clients, what dates, what conflicts)  
* What tools and parameters are needed for each key step  
* What the correct final answer looks like

Oracle Events serve two purposes:

* **Prove solvability** — demonstrate that the task can be solved and that you understand the correct solution path  
* **Drive the rubric workflow** — OEs identify which actions exist, and the three-condition test decides which process rubrics to write.

OEs do not establish authority or ground truth. Verify their claims against the prompt, live universe, and tool catalogs; correct the OE when they conflict. See [`Evals/2_OE_Eval.md`](../Evals/2_OE_Eval.md).

**Example OEs** for *"post a status update about the Season Pass bugs in the right Slack channel"*:

OE: Post a Slack message in #season-pass (or #zombie-bugs) summarizing the open vs fixed Season Pass reward bugs.

*→ The write action maps to Outcome 1.1 and, when content requirements exist, Outcome 1.2. Add 2.1 only if the user also requested that fact in the final response.*

*→ Outcome 1.1: "The Agent posts a message in #season-pass or #zombie-bugs about Season Pass reward bugs."* 

*→ Outcome 1.2: "The Agent distinguishes fixed Season Pass bugs from open Season Pass bugs in the Slack message."*

---

## **Writing Rubrics: Step by Step**

**Step 1: Identify What the Prompt Asks For**

Read the prompt and list every explicit and implicit ask.

Explicit asks — directly requested:

* What actions should be taken? (post a Slack message, create an issue, schedule a meeting)  
* What information should be reported? (findings, summaries, recommendations)  
* What constraints exist? (budget limits, specific recipients, exclusions)

Implicit asks — reasonably expected but not stated:

* Units or context for numbers (dollars, dates)  
* Disambiguation when multiple entities could match  
* Flagging problems discovered during investigation

**Step 2: Write Oracle Events**

Map the key steps a perfect agent would take. OEs help demonstrate solvability but do not establish ground truth. For each OE, note what action happens, what information is discovered, and what tools and parameters are needed, then verify those claims against authoritative sources.

**Step 3: Write All Outcome Rubrics**

For every authorized write action in your OEs, write 1.1 (action details) and 1.2 (content, if specific requirements exist). For every key fact the user asked to be told directly, write 2.1 rubrics.

For mixed tasks (research then write): write 1.1 \+ 1.2 for the write action. Add 2.1 only if the prompt also explicitly asks the agent to report findings to the user directly.

**Step 4: Review for Gaps No Outcome Can Cover**

After writing all Outcomes, review the full rubric set and ask: is there any requirement — explicit or implicit — that none of my Outcome rubrics can verify? The primary case is ordering between actions (A must happen before B, but both 1.1s pass regardless of sequence). In rare cases, source verification may also qualify — where the correct answer is available in a shallow source and the Outcome genuinely cannot be made specific enough to prove the agent checked the authoritative source. Apply the three-condition test to each candidate. If all three hold, write a Process rubric. When in doubt, tighten the Outcome instead.

**Step 5: Check Flexibility**

For each rubric, determine if the expected value is EM, Fuzzy, Selection Logic, or Required Elements. Apply the correct pattern.

**Step 6: Verify Checklist**

Before submitting, confirm:

* Every rubric object has all four stored fields: `title` (criterion text), `category`, `justification`, and `evidence`  
* Every rubric belongs to one of two categories: Outcome or Process  
* Outcome rubrics written first — Process rubrics only added when no Outcome rubric can verify the requirement (e.g., ordering between actions)  
* Every write action has a 1.1 rubric; 1.2 if specific content requirements exist  
* 2.1 used only when the user asked to be told a specific fact  
* Every criterion is self-contained (all expected values embedded)  
* Every criterion is objective (no banned words)  
* Every criterion is atomic (one claim per rubric)  
* Every criterion is affirmative and agent-centric; prohibition-only or absence-only wording is rewritten as an action, classification, scope boundary, or preserved state  
* No two rubrics penalize the same error (no overlaps)  
* Every explicit prompt ask is covered by at least one rubric (no gaps)  
* Implicit asks covered where they test reasoning or synthesis  
* Every criterion is verifiable from the trajectory or final response  
* Persona-scoped criteria are gradeable from the trajectory/final response or evidence visible to the same assigned persona, never hidden cross-persona state
* Required Gmail, Slack, GCal, and Drive-family (GDrive/GDocs/GSheets/GSlides) facts are reachable by the exact roster persona, or the prompt intentionally asks for an affirmative denial outcome plus reporting, escalation, or an authorized alternative
* Contacts, GitHub, Snowflake, Trello, Linear, and Confluence reads remain unscoped; no rubric invents ACL read scoping for them
* Write feasibility comes from `HarmonyGames_Base_Universe/6_Server_Tools_Details.json`, not Persona ACL
* Environment `set_acting_user` configuration is absent from OEs, rubrics, Process criteria, and call counts
* Gmail triage rubrics identify the target message/thread and requested triage operation or label  
* Slack rubrics list specific content items  
* Linear rubrics include title and relevant fields  
* Calculated/rounded numbers use "approximately" or a range; counts, IDs, and dates use exact values  
* Flexible values define a complete accepted set or objective semantic acceptance rule; criteria do not use `such as`, `e.g.`, or `for example`  
* Multiple valid answers use a closed set or an objective open semantic rule  
* No rubric — Outcome or Process — penalizes a valid alternative solution path. Where the prompt names a goal not a method, the rubric matches the prompt: "The Agent notifies Brian Foster," not "The Agent posts in #season-pass."  
* Process rubrics checked against the three-condition test (required by every valid path, Outcome can't cover it, describes a behavioral property not an execution trace)

---

## **Edge Cases**

**When an ordinary prompt specifies an explicit count or names specific items:** Write one atomic Outcome rubric per item, each naming the specific ticket ID, record, or entity and what the update should reflect. Do not bundle into "at least N" thresholds.

✅ Correct \- one rubric per ticket:

* "The Agent adds a comment to ENG-2402 reflecting the current Collect & Win reward mismatch."  
* "The Agent adds a comment to ENG-2349 reflecting the current Axe Arena timer mismatch."

❌ Wrong:

* "At least 5 of the 9 Linear tickets were updated with current status." → **Not Atomic.** The quantifier bundles nine independently pass/fail updates, and an agent can update five arbitrary tickets and pass.

**When the prompt is open-ended ("create tickets for anything needing follow-up"):** Go to the universe, identify the actual GT items that need follow-up, and write one rubric per item naming it explicitly. "At least one" is only acceptable if the GT is genuinely indeterminate — which is rare. If the universe shows 3 specific items needing tickets, write 3 rubrics.

**Large audit-table exception:** A qualifying long-horizon audit may use overall total/reconciliation checks plus representative atomic record-level spot checks under `Docs/13_Long_Horizon_Task_Guidelines.md`. The Oracle Events and execution remain exhaustive. There is no minimum spot-check count and no one-rubric-per-row requirement. This exception does not apply to distinct write actions or other non-repetitive requirements.

**The key principle:** Rubrics should be grounded in GT, not in what feels like a "reasonable threshold." Outside the documented large audit-table exception, an agent that updates 8 of 9 tickets should fail — the prompt asked for all 9\. Gradation comes from having 9 separate rubrics, not from setting an arbitrary pass threshold on one bundled rubric.

---

# Common Mistakes

**Mistake 1:** **Subjective Language** 

"Enough context," "professional tone," "thorough investigation", replace with specific, countable items.

**Mistake 2: Missing Service Metadata** 

Gmail triage without a target message/thread or operation. Calendar without attendees. Slack without a recipient or specific content items.

**Mistake 3: Can't Verify from Trajectory** 

"The Gmail thread is archived" without a visible triage action — the judge reads the trajectory, not the post-run environment.

**Mistake 4:** **All Rubrics Check the Same Thing** 

If all your rubrics are "~~final response mentions~~ Agent identifies X," you're missing write-action coverage. Add 1.1 and 1.2 rubrics for any write actions in the task. Cover multiple dimensions.

**Mistake 5:** **No Justification** 

Every rubric needs a WHY. Helps reviewers understand your reasoning and catch gaps.

**Mistake 6:** **Stacked Rubrics** 

"The Agent posted a Slack message to Brian and created a Linear issue for Douglas", 2 rubrics in 1\. Split independent claims.

**Mistake 7: Reformulating an outcome-verifiable prompt ask as a process rubric..** 

If the prompt asks the Agent to identify ZOM-387, a Process rubric saying “The Agent searches Linear” adds nothing: the Outcome “The Agent reports that ZOM-387 is the Giant Analytics Ticket” already checks the requested fact. Apply the three-condition test before adding any Process rubric.

**Mistake 8:** **Passive / Artifact-Centric Phrasing** 

"The message mentions the timer." — rewrite as "The Agent states the Axe Arena timer discrepancy in the Slack message to Brian Foster." The Agent is the subject, not the artifact.

**Mistake 9: Tool-Name Annotations in Outcome Rubrics** 

"The Agent posts a Slack message via a specific function..." — drop the implementation annotation. "The Agent includes ENG-2349, visible in function parameters..." — drop the parameter callout. Outcome rubrics describe what the Agent accomplished, not which tool it called or where the data is visible.

**Mistake 10:** **Overlapping Rubrics** 

If the agent gets the recipient wrong, how many rubrics fail? If more than one, you have overlaps. Each error should be caught by exactly one rubric.

**Mistake 11: Writing Process Rubrics When Outcomes Suffice** If you have Process rubrics, challenge each one: can you make an Outcome stricter and more specific? If the Outcome checks precise values from structured data that the Agent must retrieve, it usually proves the intermediate work. For ZOM-387, “The Agent reports that ZOM-387 is the Giant Analytics Ticket” is stronger than “The Agent searches Linear.” Apply the three-condition test before adding any Process rubric.

**Mistake 12: Over-specific phrasing that penalizes valid alternatives.**

Writing “The Agent posts in #season-pass” when the prompt says “brief Brian” can reject a valid direct message or another authorized collaboration path. Match the prompt's specificity: “The Agent briefs Brian Foster at brian.foster@harmonygames.co” is method-agnostic.

---

## **Difficulty Target**

We run the agent 6 times with **Claude Opus 4.7 max**. Your task is ready when:

* All fails is good (pass@1 \= 0%)  
* At most 2 runs pass — pass@1 ≤ 40% (proves difficulty)

All 6 pass → too easy, iterate. All 6 fail is fine (pass is 0%).

*Tip: Use Haiku for quick iteration. Switch to Opus for the final 6 runs.*

---

**The examples below show how to write rubrics for simple prompts. These aren't exhaustive and don't ensure the accuracy/high-quality we expect from your tasks.**

## **Example: Simple Task**

Prompt: *"Post a status update about the Season Pass bugs in the right Slack channel"*

**Outcome**

| \# | Criterion |
| ----- | ----- |
| 1 | The Agent posts a message in `#season-pass` or `#zombie-bugs` about Season Pass reward bugs. \[1.1 — write-action result\] |
| 2 | The Agent distinguishes fixed Season Pass bugs from open Season Pass bugs in that message. \[1.2 — action content\] |

Process rubrics: None.

Why no process rubrics:

The prompt's deliverable IS the Slack message. The 1.1 Outcome rubric already verifies it was sent — a process rubric would just reformulate the outcome.

Shortcut risk: None. The recipient (Brian) and context (Season Pass) are given in the prompt. The deliverable IS the Slack message, it either happened or it didn't.

---

## **Example: Grounded Investigation**

Prompt: *"Work out what the Zombie Match Giant Analytics Ticket is actually tracking and tell me how it connects to the implementation."*

**Outcome**

| \# | Criterion |
| ----- | ----- |
| 1 | The Agent reports that ZOM-387 is the Giant Analytics Ticket. \[2.1\] |
| 2 | The Agent reports that the corresponding implementation is match3d pull request #319. \[2.1\] |

Process rubrics: None.

* **Process Rubric Decision Flow:** The exact ticket identity and linked implementation are strict Outcomes. A generic criterion requiring Linear or GitHub searches would add no signal and would lock in an execution path.

---

## **When to Write Rubrics**

Write rubrics during and after the agent run, not before.

1. Write your prompt and submit it  
2. The agent runs  
3. While the agent runs, start drafting rubrics based on what you expect should happen  
4. After the agent finishes, review the trajectory  
5. Finalize rubrics — adjust based on what you actually see  
6. The LLM judge grades the rubrics against the trajectory

You can iterate: tweak prompt → re-run → adjust rubrics. If the agent passes everything, the task isn't hard enough — iterate.