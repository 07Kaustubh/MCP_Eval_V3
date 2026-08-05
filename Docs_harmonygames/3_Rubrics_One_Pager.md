## **Rubric Writing — One Pager**

---

This is a quick reference derived from [`Docs/2_Rubrics_Guidelines.md`](2_Rubrics_Guidelines.md). **If this page conflicts with Docs/2, Docs/2 wins.** Start from the [`Docs/README.md`](README.md) index; use [`Evals/3_Rubrics_Eval.md`](../Evals/3_Rubrics_Eval.md) for evaluation policy. [`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json) is authoritative for service availability and capabilities. Keep exact tool names out of prompts and rubric criteria.

**Last updated:** July 30, 2026

## **Core Guidance**

Outcome and Process are the only rubric categories. Outcome is the mandatory
default; Process is optional, rare, and may not exceed 40% of the set. This is
a safety cap, not a target ratio; zero Process is valid. Tighten Outcome rubrics
with precise values (numbers, IDs, derived math) before considering a Process
rubric. If the Outcome can only be satisfied by doing the work, the Outcome
alone is enough.

---

## **Persona ACL Quick Check**

Persona ACL is active. Use [`14_Persona_ACL.md`](14_Persona_ACL.md) and the
exact key/email in
[`4_Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json).

* Gmail, Slack, GCal, GDrive, GDocs, GSheets, and GSlides reads are
  persona-scoped.
* Contacts, GitHub, Snowflake, Trello, Linear, and Confluence reads are unscoped. Writes
  are outside ACL scope.
* Explorer author god-mode proves that a record exists, not that the assigned
  Agent Runner can reach it. Agent Runner and Run Verifiers use the same
  persona.
* Required evidence from any of the eight scoped services that is inaccessible
  to that persona hard-fails feasibility, except when the intended outcome is
  an affirmative denial finding plus reporting, escalation, or an authorized
  alternative.
* A verifier must grade from the trajectory/final response, visible write
  arguments, or evidence visible to that same persona—not hidden cross-persona
  state.
* `set_acting_user` is environment configuration, not Agent work, an OE,
  rubric/Process requirement, or a call-count item.

---

## **The Two Categories**

* **Outcome (mandatory)** — what the agent accomplished, reported, or produced. Verified from the trajectory, the final response, or both. Every explicit prompt must be covered.  
* **Process (optional)** — whether the agent did necessary work that the final result alone cannot verify. Framed as behavioral expectations, never as tool-call checklists. Process rubrics can cover both explicit and implicit prompt requirements — the defining characteristic is that no Outcome rubric can capture the property, not whether the prompt asked for it.

---

## **Outcome Coverage Types**

All rows below use the single stored category **`Outcome`**:

| Coverage type | What it checks | Verified from | When to use |
| ----- | ----- | ----- | ----- |
| **Write-action result** | The right action happened with the right details | Trajectory (tool call) | Every write action |
| **Action content** | Content matches what was needed | Trajectory (tool-call parameters) | When the write has specific content requirements |
| **Key facts / findings** | Agent reported the right information | Final response text | When the user asked to be told something directly |

---

## **When to Add a Process Rubric — All Three Must Hold**

1. **Required by every valid solution path** (or phrased broadly enough to allow alternatives).  
2. **A stricter Outcome rubric cannot capture the same requirement.**  
3. **The rubric describes a verification, not an execution trace.**

**Note: Ordering constraints can be explicit in the prompt (e.g., "notify legal before scheduling the meeting") and still require a Process rubric because no Outcome rubric can verify ordering.**

If any condition fails, drop the Process rubric or tighten the Outcome instead. 

---

## **Worked Examples — HarmonyGames**

**❌ Reward-hackable process rubric — don't write:**

"The Agent searches live-ops records before reporting the Axe Arena timer discrepancy."

The behavior is vague and adds no signal beyond the precise finding.

**✅ Strict outcome rubric — write this instead:**

"The Agent reports that ENG-2349 records the Axe Arena infinite-lives reward as 10 minutes in the build and 15 minutes as intended."

The exact issue and direction make the Outcome specific enough to prove the reconciliation.

**✅ Process rubric warranted:**

"The Agent briefs Brian Foster at brian.foster@harmonygames.co before scheduling the live-ops review."

The prompt or a validly incorporated source must establish the dependency. The
brief and meeting have separate Outcome criteria, but both pass regardless of
order, so no Outcome can verify the prerequisite.

---

## **Stored Schema**

Every rubric object stores four fields:

* **`title`** — the conceptual criterion: the self-contained yes/no claim.
* **`category`** — exactly `Outcome` or `Process`.
* **`justification`** — 1–2 sentences explaining *why* the rubric exists.
* **`evidence`** — where to verify pass/fail in the trajectory or final response.

There is no separate stored `criterion` key. `title` contains the criterion text, and neither `justification` nor `evidence` may supply a missing acceptance fact.

---

## **Service Metadata Required**

* **Gmail triage** → target message/thread, mailbox/user when relevant, and requested triage operation or label.  
* **Slack** → recipient (channel/DM), specific content items.  
* **Linear** → title, assignee/priority/subtasks where applicable.

## **Phrasing Convention — Agent-Centric and Affirmative**

Frame every rubric as an affirmative behavior or observable state attributable to *the Agent*, not a passive artifact description. Applies to both Outcome and Process.

| Avoid: tool/artifact-centric | Required: agent-centric |
| ----- | ----- |
| "A message was sent using a specific messaging function to Brian…" | "The Agent sends the summary to Brian Foster at brian.foster@harmonygames.co." |
| "The message body includes the bug details and status." | "The Agent's message to Brian includes the Season Pass reward bug details and a status comparison (fixed vs still open)." |
| "The Brian summary mentions the timer issue." | "The Agent reports in the summary to Brian Foster that ENG-2349 records the Axe Arena timer discrepancy." |

**Six phrasing rules:**

1. Subject \= *The Agent* (not the artifact).  
2. Drop implementation annotations and parameter callouts.  
3. Read it aloud — should sound natural, not like a test assertion.  
4. Process rubrics describe behavior, not execution traces ("checks Linear" — not "calls a specific listing function third").  
5. Rewrite prohibition-only syntax affirmatively: “The Agent confines production activity to inspection” or “The Agent leaves the production configuration unchanged,” not “The Agent does not change production.” Reject ACL criteria whose only condition is “The Agent does not access…”; grade an affirmative finding, boundary, report, escalation, or authorized alternative. Affirmative reports of factual states such as “unresolved” or “access denied” remain valid.
6. Preserve source formatting: `ENG-2349`, `$6.99`, `Zombie Match 3D`, `Marcus Bennett`.

Affirmative wording does not remove coverage of exclusions, decoys, or prohibited writes; keep those requirements as atomic criteria phrased as classifications, scope boundaries, or preserved states.

---

## **Verb Cheat Sheet**

* **Outcome — write actions:** sends, creates, updates, posts, schedules, assigns  
* **Outcome — action content:** includes, mentions, states, covers, references, names  
* **Outcome — key facts:** identifies, reports, flags, lists, recommends, concludes  
* **Process:** verifies, confirms, checks, reviews, reconciles, notifies (before X)

## **Core Writing Rules**

* **Self-contained**: embed every expected value (the judge can't look anything up).  
* **Atomic**: one independent claim per rubric. Bundle only when two facts come from the same action or the same data record and would fail together.  
* **Verifiable** from trajectory or final response.  
* Use **"approximately"** or a range for calculated/rounded numbers; use **exact values** for counts, IDs, dates, and discrete quantities.  
* **Match the prompt's level of specificity**: if the prompt names a *goal* ("brief Brian"), the rubric names the goal — don't lock in a method ("post in #season-pass").  
* **Never mention tool names** in either prompts or rubrics.  
* For multiple write actions of the same type, write **one Outcome rubric per item** grounded in ground truth — never "at least N".

---

## **Flexibility Patterns**

| Situation | Pattern | Example |
| ----- | ----- | ----- |
| One correct value / fact | Strict (EM) | `brian.foster@harmonygames.co` |
| Free-text or agent-generated label | Objective semantic rule | `a title semantically equivalent to Zombie Match 3D live-ops health` |
| Multiple valid answers | Closed / Open / Any-one | State a complete set, an objective semantic rule, or an explicit any-one set |
| Content with specific requirements | Required Elements | `must state the shipped timer, intended timer, and issue ID` |
| Goal named, not method | Method-agnostic | `The Agent briefs Brian Foster` (not "posts in #season-pass") |

## **Workflow**

1. Plan **Oracle Events** — map the steps a perfect agent would take.  
2. Write all **Outcome rubrics** first: cover each write action, its required
   content, and each fact the user asked to receive, using agent-centric
   phrasing.  
3. Review the full rubric set for gaps no Outcome can cover (e.g., ordering between actions). Apply the three-condition test to each candidate. If all three hold, write a Process rubric.  
4. Check flexibility for each rubric.  
5. Run the verification checklist.

OEs are non-authoritative planning notes. Verify their tools and claims against the catalogs, prompt, and live universe; see [`Evals/2_OE_Eval.md`](../Evals/2_OE_Eval.md).

---

## **Top Mistakes to Avoid**

* Subjective language ("thorough," "professional," "enough context").  
* Missing service metadata (Gmail triage without a target or operation, Slack without recipient/content items).  
* Passive / artifact-centric phrasing ("the message mentions…" → say "The Agent mentions… in the Slack message").  
* Prohibition-only wording ("The Agent does not…") instead of an affirmative action, classification, scope boundary, or preserved state.  
* Overlapping rubrics where one error trips multiple.  
* Writing a Process rubric when a stricter Outcome would prove the same thing.  
* Over-specific phrasing that fails valid alternative paths.

---

## **TL;DR**

Two conceptual categories and four stored fields. **Outcome** is the standard and should be tightened aggressively. **Process** is optional, rare, and gated by all three conditions. Phrase every criterion affirmatively as an Agent behavior or observable state. Most tasks will have zero Process rubrics — that's correct.

---

## **Prompt and Rubric Example**

*The Season Pass on Zombie Match keeps throwing weird reward bugs after launch and I can't tell what's actually been fixed vs still open. Can you get to the bottom of it, make sure the right tickets reflect reality, and flag anything that's slipped through so the right engineer picks it up? Also check if anyone on the team has already been discussing this internally. Brief Brian with what you found, and get a sync on the calendar with the live-ops team for this week.*

**Canonical Outcome criteria:**

* The Agent schedules a sync meeting with the live-ops team for the current
  week. \[Outcome\]
* The Agent identifies which Season Pass reward bugs are fixed and which remain
  open, citing the specific ZOM ticket IDs. \[Outcome\]
* Write one Outcome criterion per relevant Linear issue, naming the exact ticket
  ID and required status from ground truth.
* The Agent sends a Slack message to brian.foster@harmonygames.co (Brian Foster).
  \[Outcome\]
* The Agent's Slack message to Brian Foster includes which bugs are fixed versus
  still open and states that ticket statuses were updated. \[Outcome\]
* The Agent reports whether prior internal discussion about the Season Pass
  reward bugs was found, citing specific messages or threads when they exist.
  \[Outcome\]

The strict findings criteria prove the necessary research occurred, so separate Process criteria for searches or retrieval methods are not warranted.

**Process criterion only if the task requires this dependency:**

* The Agent briefs Brian Foster at brian.foster@harmonygames.co before scheduling the live-ops sync meeting.

