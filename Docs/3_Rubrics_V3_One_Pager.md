*Based on Rubric Writing V3 (last updated June 03, 2026\)*

---

## **What's Changing (V3)**

The framework shifted from three categories (TS, QC, Outcome) to two (Outcome, Process). Outcome is now the mandatory default; Process is optional and rare.

| Old framework | New framework |
| ----- | ----- |
| TS \+ QC \+ Outcome (three categories) | Outcome (mandatory) \+ Process (optional) |
| 50/50 to 80/20 outcome-to-process target | No fixed ratio - most tasks will have zero process rubrics |
| Decision Matrix based on tool mechanics | Four-condition behavioral test |
| Passive phrasing ("The email mentions X") | Agent-action phrasing ("Agent reports X") |

**Core shift:** tighten outcome rubrics with precise values (numbers, IDs, derived math) before reaching for a process rubric. If the outcome can only be hit by doing the work, the outcome alone is enough.

---

## **The Two Categories**

* **Outcome (mandatory)** - what the agent accomplished, reported, or produced. Verified from the trajectory, the final response, or both. Every explicit prompt must be covered.  
* **Process (optional)** - whether the agent did necessary work that the final result alone cannot verify. Framed as behavioral expectations, never as tool-call checklists. Process rubrics can cover both explicit and implicit prompt requirements - the defining characteristic is that no Outcome rubric can capture the property, not whether the prompt asked for it.

---

## **Outcome Sub-Categories**

| Sub-cat | What it checks | Verified from | When to use |
| ----- | ----- | ----- | ----- |
| **1.1 Write-Action Results** | The right action happened with the right details | Trajectory (tool call) | Every write action |
| **1.2 Action Content** | Content matches what was needed | Trajectory (tool-call parameters) | Only when content has specific requirements beyond 1.1 |
| **2.1 Key Facts / Findings** | Agent reported the right information | Final response text | When the user asked to be told something directly |

---

## **When to Add a Process Rubric - All Three Must Hold**

1. **Ordering constraints** can be explicit in the prompt (e.g., "notify legal before scheduling the meeting") and still require a Process rubric because no Outcome rubric can verify ordering.  
2. **Required by every valid solution path** (or phrased broadly enough to allow alternatives).  
3. **A stricter Outcome rubric cannot capture the same requirement.**  
4. **The rubric describes a verification, not an execution trace.**

If any condition fails, drop the Process rubric or tighten the Outcome instead. 

## 

---

## 

## **Worked Examples**

**❌ Reward-hackable process rubric - don't write:**

"Agent retrieves both Stripe charge data and the closing disclosure document before reporting the discrepancy."

The agent could pull unrelated artifacts from each source and still pass. 

**✅ Strict outcome rubric - write this instead:**

"Agent identifies a $264 overcharge - the difference between the $792 Stripe charge and the $528 closing disclosure amount."

All three numbers can only be right if the agent actually did the work. The outcome proves every intermediate step.

**✅ Process rubric warranted:**

"Agent notifies the legal team before scheduling the contract signing meeting." (Used “notifies” as notification could be via email/slack/messaging and prompt didn’t specify the server) 

1. Both the notification and the meeting have their own 1.1 Outcome rubrics, but both pass regardless of which happened first. No Outcome rubric can capture the ordering - only a Process rubric verified from the trajectory can confirm the prerequisite was met before the dependent action.  
2. **Note:** this applies whether the prompt explicitly asks for the ordering ("make sure to notify legal before scheduling") or the ordering is implied by professional norms. Either way, the reason it's Process is that Outcome can't verify it - not whether the prompt mentioned it.

---

## **Three Fields Per Rubric**

* **Criterion** - the specific yes/no claim.  
* **Justification** - 1–2 sentences explaining *why* this rubric exists.  
* **Evidence** - what in the trajectory or final response proves pass/fail.

---

## 

## **Service Metadata Required**

* **Email** → recipient, CC (if specified), specific content items.  
* **Slack** → recipient (channel/DM), specific content items.  
* **Linear** → title, assignee/priority/subtasks where applicable.

## 

## **Phrasing Convention - Agent-Centric**

Frame every rubric as a behavior of *the agent*, not a passive description of the artifact. Applies to both Outcome and Process rubrics.

| ❌ Old (tool/artifact-centric) | ✅ New (agent-centric) |
| ----- | ----- |
| "An email was sent (via send\_email) to Chloe…" | "The Agent sends the summary to Chloe Vance at chloe.vance@moveops.com." |
| "The email body includes the city and cost comparison." | "The Agent's email to Chloe includes the alternative city (Boston) and a cost comparison (approximately $12,000 vs $17,000)." |
| "The Chloe summary mentions Joaquín Reyes is a permit case." | "The Agent reports in the Chloe summary that Joaquín Reyes is a permit or oversize paperwork case." |

**Five phrasing rules:**

1. Subject \= *The Agent* (not the artifact).  
2. Drop `(via tool_name)` and `(visible in parameters)`.  
3. Read it aloud - should sound natural, not like a test assertion.  
4. Process rubrics describe behavior, not execution traces ("consults the CRM" - not "calls crm\_search\_contacts third").  
5. Preserve source formatting: `INV-2026-0401`, `$350`, `Joaquín`, `Langford's`.

---

## **Verb Cheat Sheet**

* **1.1 Write actions:** sends, creates, updates, posts, schedules, assigns  
* **1.2 Action content:** includes, mentions, states, covers, references, names  
* **2.1 Key facts:** identifies, reports, flags, lists, recommends, concludes  
* **Process:** verifies, confirms, checks, reviews, reconciles, notifies (before X)

## 

## **Core Writing Rules**

* **Self-contained**: embed every expected value (the judge can't look anything up).  
* **Atomic**: one independent claim per rubric. Bundle only when two facts come from the same tool call or the same data record and would fail together.  
* **Verifiable** from trajectory or final response.  
* Use **"approximately"** or a range for calculated/rounded numbers; use **exact values** for counts, IDs, dates, and discrete quantities.  
* **Match the prompt's level of specificity**: if the prompt names a *goal* ("notify legal"), the rubric names the goal - don't lock in a method ("email legal").  
* **Never mention tool names** in either prompts or rubrics.  
* For multiple write actions of the same type, write **one Outcome rubric per item** grounded in ground truth - never "at least N".

---

## **Flexibility Patterns**

| Situation | Pattern | Example |
| ----- | ----- | ----- |
| One correct value / fact | Strict (EM) | `chloe.vance@moveops.com` |
| Free-text or agent-generated label | Fuzzy \+ "(or similar)" | `related to relocation proposal (or similar)` |
| Multiple valid answers | Closed / Open / Any-one | `must be one of` · `including but not limited to` · `at least one of` |
| Content with specific requirements | Required Elements | `must include: (a) reason, (b) city, (c) cost comparison` |
| Goal named, not method | Method-agnostic | `Agent notifies legal` (not "emails legal") |

## **Workflow**

1. Plan **Oracle Events** - map the steps a perfect agent would take.  
2. Write all **Outcome rubrics** first: 1.1 \+ 1.2 for each action, 2.1 for each fact the user asked for with the new agent-centric phrasing rules.  
3. Review the full rubric set for gaps no Outcome can cover (e.g., ordering between actions). Apply the three-condition test to each candidate. If all three hold, write a Process rubric.  
4. Check flexibility for each rubric.  
5. Run the verification checklist.

---

## **Top Mistakes to Avoid**

* Subjective language ("thorough," "professional," "enough context").  
* Missing service metadata (email without recipient, Slack without content items).  
* Passive / artifact-centric phrasing ("the email mentions…" → say "Agent mentions… in the email").  
* Overlapping rubrics where one error trips multiple.  
* Writing a Process rubric when a stricter Outcome would prove the same thing.  
* Over-specific phrasing that fails valid alternative paths.

---

## **TL;DR**

Two categories. **Outcome** is the standard and should be tightened aggressively. **Process** is optional, rare, and gated by a three-condition test. Phrase everything as agent behaviors. Most tasks will have zero process rubrics - that's correct.

---

## **Prompt and Rubrics example**

Below you can check how Rubrics would look like for a prompt in V2 and V3 format:

*Hey, compliance just pinged me about Daniela Voss, apparently there's some kind of mismatch between what she put on her application and what's actually in her verification docs. Something about her income numbers not lining up. Can you look into it? Check her loan file, pull whatever docs we have, and tell me if it's a real issue or not. Also see if anyone on the team has already been talking about this internally. If it turns out there is a discrepancy, flag it on her loan so underwriting can see it, loop in Robert from compliance with what you found, and get a review meeting on the calendar with the underwriting team for this week.*

| V2 Rubric | V3 Rubric |
| :---- | :---- |
| The model must use \`mortgage\_los\_search\_loans\` or \`mortgage\_los\_get\_loan\` to retrieve Daniela Voss's loan record. | TS removed in V3. The prompt explicitly says "Check her loan file" (Decision Flow condition 1 fails). The strict outcome ($9,200, LN-2026-04417) already proves the agent accessed the LOS. |
| The model must use \`filesystem\_read\_file\` (or similar filesystem tool) to access Daniela Voss's pay stub or verification documents. | Same as rubric 1\. The prompt explicitly says "pull whatever docs we have" (condition 1 fails). The strict outcome ($8,450 pay stub figure) proves the agent read the documents. |
| The model must search for the loan using a query related to "Daniela Voss" or "Voss" (or similar). | QC removed in V3. "Daniela Voss" is given in the prompt, no inference needed. A wrong query would cause all Outcome rubrics (LN-2026-04417, $9,200, $8,450) to fail, so the outcomes already enforce this. |
| The model must use \`calendar\_add\_calendar\_event\` to schedule the underwriting review meeting. | The Agent schedules a review meeting with the underwriting team for the current week. (Outcome) |
| The model must search Slack or email using terms related to "Daniela Voss" or "income" or "discrepancy" (or similar) to find prior internal discussion. | The prompt explicitly asks to check internal discussions (condition 1 fails). Outcome rubric 5 (V3) covers the result, if the agent didn't search, it can't report accurately. |
| The model must identify that the application (1003) shows monthly income of $9,200 while the pay stubs on file show $8,450/month, confirming a discrepancy of $750/month. | The Agent identifies that the application (1003) shows monthly income of $9,200 while the pay stubs on file show $8,450/month, confirming a discrepancy of $750/month.(Outcome) |
| The model must add an activity note on Daniela Voss's loan (Loan ID: LN-2026-04417) flagging the income inconsistency. | The Agent adds an activity note on Daniela Voss's loan (Loan ID: LN-2026-04417) flagging the income inconsistency.(Outcome) |
| The model must send an email to \`robert.hayward@keystonemortgage.com\`. | The Agent sends an email to [robert.hayward@keystonemortgage.com](mailto:robert.hayward@keystonemortgage.com). (Outcome) |
| The email to Robert Hayward must include the specific dollar amounts ($9,200 application income vs $8,450 pay stub income) and mention that the loan file has been flagged. | The Agent's email to Robert Hayward includes the specific dollar amounts ($9,200 application income vs $8,450 pay stub income) and mentions that the loan file has been flagged. (Outcome) |
| The model must report whether any prior internal discussion (email or Slack) about this discrepancy was found, citing specific messages or threads if they exist. | The Agent reports whether any prior internal discussion (email or Slack) about the Daniela Voss income discrepancy was found, citing specific messages or threads if they exist. (Outcome) |
| V2 only had TS (did the agent use the right tool?) and QC (did it pass the right parameters?). Neither category could check the order in which actions happened. This is a gap that V3's Process category fills. | The Agent flags the loan (LN-2026-04417) and notifies Robert (robert.hayward@keystonemortgage.com) before scheduling the underwriting review meeting. (Process) |

