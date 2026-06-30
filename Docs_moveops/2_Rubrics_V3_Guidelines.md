## **Rubric Writing V3**

---

## **Note: This doc has undergone some changes on June 03\. Please read the change log below carefully\!**

## **💡 Change Log Last Updated:** Jun 3, 2026

| Date | Type | Description |
| ----- | ----- | ----- |
| June 03, 2026 | Rubrics | **Updates on Process rubrics and overall alignment.** |
| May 20, 2026 | Rubrics | **Major restructure: rubric categories simplified from three (TS, QC, Outcome) to two - Outcome (mandatory) and Process (optional).**  Outcome is the default training signal. Process rubrics only apply when a necessary behavior cannot be captured by a stronger outcome rubric.  Removed fixed outcome-to-process ratio.  Rubric phrasing updated to agent-action form ("Agent reports X" instead of "The summary mentions X"). TS/QC scaffolding moved to deprecated appendix. |
| Apr 30, 2026 | AF Rubrics | **Valid AF Rubrics & When to Delete or Make them Flexible.** When all Outcomes pass but Process rubrics fail: delete TS rubrics when only a default tool was used (no TS allowed for defaults), add missing valid non-default tools as flexible. Delete QC rubrics when the query value is obvious from the prompt, make QC flexible when alternative queries also produce correct results. |
| Apr 10, 2026 | Default Tools | Added a table that explains the default and non-default tools for each universe. |
| Mar 25, 2026 | Rubrics | **Atomic rubrics for multiple write actions of the same type:** When the prompt asks for multiple write actions (e.g., update all tickets, create tickets for all follow-up items), write one Outcome rubric per item grounded in GT - never bundle into "at least N" thresholds. "At least one/N" is reward-hackable and only acceptable when GT is genuinely indeterminate. |
| Mar 12, 2026 | Rubrics | **Update to Rubrics & Examples:**  Outcome-first: write all write actions as Outcome rubrics first; key facts reported to user go into 2.1. Outcome categories simplified from 5 to 3 (1.1 write-action results, 1.2 action content, 2.1 key facts). Process Rubric Decision Matrix and Default/Non-Default Tool list added to decide when to write TS and QC rubrics. TS one-per-tool rule: one TS rubric per non-default tool regardless of how many times it's called. All TS/QC examples updated to show only read/lookup tools - write actions never appear in TS/QC context. Approximately rule updated: use for calculated/rounded values; do not use for counts, IDs, dates, or discrete quantities. |
| Mar 12, 2026 | Failure Rate | Difficulty target clarified: 0% pass rate is acceptable as long as overall rubrics are high-quality and don’t lead to false negatives/invalid model failures.  |

---

## **What Are Rubrics?**

Rubrics are specific, checkable statements about what the AI agent should (and should not) accomplish. Each rubric is a simple yes-or-no claim. An LLM judge reads the agent's trajectory and checks each rubric against what it finds there.

*You write the rubrics. The judge reads the trajectory. Pass or fail.*

### How the Judge Works

**The judge sees:**

* The original task prompt - what the agent was asked to do  
* The agent's trajectory - every tool call, its parameters, its response, and the agent's reasoning at each step  
* The agent's final response - the summary text at the end  
* Your rubric criteria

**The judge does NOT see:**

* The MCP environment directly (it cannot call tools itself)  
* The universe data (it only knows what appeared in the trajectory)  
* Other agents' results

**What this means for you:** Every expected value must be in the rubric itself. If you write "The Agent sent an email to the owner," the judge doesn't know who the owner is.

Instead write "The Agent sent an email to r.calloway@moveops.com (Owner / Licensed Mortgage Broker)."

---

## **Phrasing Convention - Agent-Centric**

Frame every rubric as a behavior of *the agent*, not a passive description of the artifact. Applies to both Outcome and Process rubrics.

| ❌ Old (tool/artifact-centric) | ✅ New (agent-centric) |
| ----- | ----- |
| "An email was sent (via send\_email) to Grace…" | "The Agent sends the summary to Grace Yamamoto at grace.yamamoto@moveops.com." |
| "The email body includes the loan amount and rate comparison." | "The Agent's email to Grace includes the rate lock extension amount ($375) and a comparison to the original lock fee ($250)." |
| "The Grace summary mentions Carlos Martinez is a rate lock case." | "The Agent reports in the Grace summary that Carlos Martinez is a rate lock extension or expiration case." |

**Five phrasing rules:**

1. Subject \= *The Agent* (not the artifact).  
2. Drop `(via tool_name)` and `(visible in parameters)`.  
3. Read it aloud - should sound natural, not like a test assertion.  
4. Process rubrics describe behavior, not execution traces ("consults the CRM" - not "calls crm\_search\_contacts third").  
5. Preserve source formatting: `INV-2026-0401`, `$350`, `LN-2026-00847`, `Langford's`.

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
* **No rubric \- outcome or process \- penalizes a valid alternative solution path.** Where the prompt names a goal not a method, the rubric matches the prompt: "Agent notifies legal," not "Agent emails legal." A rubric that locks in one method will fail correct solutions that took a different valid route. See Handling Flexibility for the full pattern.

---

### **Category 1: Outcome**

**What it checks:** What was accomplished? What does the user see?

This is where almost all of your rubrics live. Outcome rubrics describe what should have been achieved - verified from the trajectory, the final response, or both.

---

**Writing Outcome Rubrics**

Outcome rubrics use three sub-categories. Use only the ones that apply to your task.

**1.1 - Action Results**

Did the right action happen with the right details? Verified from the trajectory (tool call).

`The Agent sent an email from amy.chen@moveops.com to grace.yamamoto@moveops.com.`

Use for: every write action. Always required when a write action exists.

**1.2 - Action Content**

Does the content match what was needed? Verified from the trajectory (tool call parameters).

`The Agent’s email body to Grace includes the recommended alternative lender name and a rate comparison referencing the approximately 6.25% original rate.`

Use when: the write action has specific content requirements to be met. Only write 1.2 if it adds a distinct check beyond 1.1.

**2.1 - Key Facts / Findings (Final Response)**

Did the agent correctly report the right information to the user? Verified from the final response text.

`The Agent identifies that Carlos Martinez (LN-2026-00847) is refinancing the property at 1847 Elm Street.`

Use when: the user asked to be told a specific fact - whether or not the task also includes write actions.

**Which Sub-Categories Apply**

| Task Type | 1.1 | 1.2 | 2.1 |
| ----- | ----- | ----- | ----- |
| Pure write action (send email, create issue) | ✅ Always | ✅ If content requirements exist | ❌ |
| Pure investigation / summary to user | ❌ | ❌ | ✅ |
| Mixed: research then write | ✅ | ✅ | ✅ Only if user also asked to be told findings directly |

---

**A note about Tool Names in Task Sections**

Tool names are not required anymore. The project is shifting to a more natural process of writing prompts and rubrics. 

| Context | Rule |
| ----- | ----- |
| Task prompts | Never mention tool names |
| Rubrics | Never mention tool names |

✅ Adequate: `The Agent sent an email to grace.yamamoto@moveops.com.` 

❌ Deprecated:  `An email was sent (via send_email) to Grace.`

---

### **The Outcome-First Workflow**

Follow this sequence every time you write rubrics:

* **Step 1:** Write all Outcome rubrics first. For every action in your OEs, write 1.1 (action result) \+ 1.2 (content, if specific requirements exist). For every key fact the user asked to be told directly, write 2.1 (final response).  
* **Step 2 - Review the full rubric set for gaps no Outcome can cover.** After writing all Outcomes, ask: is there any requirement - explicit or implicit - that none of my Outcome rubrics can verify? The primary case is ordering between actions (A must happen before B, but both 1.1s pass regardless of sequence). In rare cases, source verification may also qualify - where the correct answer is available in a shallow source and the Outcome genuinely cannot be made specific enough to prove the agent checked the authoritative source. These are your candidates for Process rubrics.  
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
   * The behavior is necessary for trustworthy completion AND every valid solution path requires it - or the rubric is phrased broadly enough to pass any valid path. Prompt says "notify legal before scheduling"? Rubric says "Agent notifies legal," not "Agent emails legal." A correct solution using Slack should still pass.  
     1. **Note**: “Agent emails legal” is still a valid rubric if the prompt requests “Send an email to legal".  
2. **Outcome can't cover it**  
   * A stricter outcome rubric cannot capture the same requirement. When the outcome can check precise values pulled from structured sources (a Stripe amount, a PDF figure, derived math), the agent cannot fake the outcome without doing the underlying work - and the outcome alone is preferable.  
3. **The rubric describes a verification, not an execution trace.**  
   * The rubric describes what the agent did or verified in a way the judge can confirm from the trajectory - not which specific tool was called, or what the agent was "thinking."  
     1. ![:white\_check\_mark:][image1] "Agent confirmed the wire instructions in the email match the wire instructions on file before initiating the transfer."  
     2. ![:x:][image2] "Agent called contacts\_get\_contact and then email\_get\_thread before stripe\_create\_transfer." *(locks in one tool path; a valid agent using different tools would fail)*  
     3. *![:x:][image3]* "Agent understood the wire instructions could be a phishing attempt." *(no observable evidence - can't grade intent)*

If any condition fails, **do not write the process rubric** - either drop it or rewrite   
the corresponding outcome rubric to be stricter.

---

**Default to Stricter Outcome Rubrics**

Before considering any process rubric, consider **Step 2** of the *Process Rubric Decision Flow* 

* Can I make my outcome rubric more specific so that achieving it proves the behavior happened?

If the outcome can check precise values pulled from structured sources 

* a Stripe amount, a figure from a PDF, a derived calculation, etc.

then the agent cannot fake the outcome without performing the underlying work. 

In those cases, a stricter outcome is always preferable to a process rubric.

---

### Examples:

**Example 1 / Outcome is enough:**

| Prompt context: |
| :---- |
|  `The agent needs to find a rate lock extension overcharge on the Flores loan by comparing a Stripe charge against the closing disclosure PDF.`  |
| **❌ Do NOT write a Process rubric like:** |
|  `"Agent retrieves both Stripe charge data and the closing    disclosure document before reporting the discrepancy."`  **Why this is bad:**  The agent could pull a random unrelated artifact from each source and still pass this rubric. It's reward-hackable. |
| **✅ Instead, write a Strict Outcome rubric:** |
|  `"Agent identifies a $264 overcharge on the Flores file - the difference between the $792 Stripe charge and the $528 closing disclosure amount."`  **Why this works:**  $792 is from Stripe.  $528 is from a PDF.  $264 is derived math.  The agent cannot get all three values right without actually pulling from both systems and doing the comparison.  The outcome proves every intermediate step happened. |

**Example 2 / Process is warranted:**

|  Prompt context:  |
| :---- |
|  `The agent must notify the legal team before scheduling a contract signing meeting.`  |
| **✅ Process rubric is appropriate:** |
|   `"Agent notifies the legal team before scheduling the contract signing meeting."`  **Why this works:**   The meeting being scheduled (the Outcome) does not prove the email was sent first.  The prerequisite behavior is necessary but invisible from the final state - no Outcome rubric can capture it.  |

---

## 

## **Handling Flexibility: How Strict Should a Rubric Be?**

***Outcome (1.1 / 1.2) - verified from trajectory:***

Write-action result - Strict: `Agent sends an email from r.calloway@moveops.com to grace.yamamoto@moveops.com.`

Email subject - Flexible: `The Agent’s email subject relates to a rate lock extension request (e.g., "Rate Lock Extension - Martinez File" or similar).`

Action content - Strict (exact string from data): `The Agent’s email includes the client name "Martinez file (LN-2026-00847)."`

Action content - Flexible (calculated or rounded value): `The Agent’s email includes the approximately $15,000 original budget figure.`

Action content - Flexible (Required Elements): `The Agent’s email must include: (a) the reason for the delay (e.g., appraisal issue or similar), (b) the revised closing date, and (c) a cost impact summary.`

***Outcome (2.1) - verified from final response:***

Key facts - Strict: `The Agent identifies Carlos Martinez (LN-2026-00847) as refinancing the property at 1847 Elm Street.`

Key facts - Flexible: `The Agent identifies the most cost-effective option (e.g., "the 15-year fixed has the lowest total interest" or similar comparison).`

**Quick Reference**

| Situation | Pattern | Example |
| ----- | ----- | ----- |
| One correct value / fact | Strict (EM) | "grace.yamamoto@moveops.com" |
| Freetext parameter or agent-generated label | Flexible (Fuzzy) | "related to rate lock extension request (or similar)" |
| Agent content with specific requirements | Required Elements | "must: (a) reason for delay, (b) revised closing date, (c) cost impact summary" |
| Similar entities, one correct | Selection Logic | "elena.marchetti@... - the Martinez with the active loan file" |
| Goal named, not method | Method-agnostic | "Agent notifies legal" not "Agent emails legal" if prompt said to notify (and didn’t name a specific form of communication) |

---

## **Three Fields Per Rubric**

Every rubric needs three fields.

**1\. Criterion** The specific yes/no claim the judge evaluates. Must be self-contained, objective, atomic, and verifiable.

**2\. Justification** 1–2 sentences explaining why this rubric exists. Connects to the prompt or a known failure mode. *"This rubric exists because the prompt explicitly says 'CC Elena.' If Elena doesn't see the proposal, she can't approve it."*

**3\. Evidence** What to look for in the trajectory. Points to the specific tool call, parameter, or response text that proves pass or fail. *"Look for send\_email tool call. Check the CC field for r.calloway@moveops.com."*

---

**Service Metadata Requirements**

Rubrics missing metadata are incomplete. Always include the required fields per service.

Email - must include: Recipient (full email address), CC (if specified), Content (specific items the email must contain - list individually)

Slack - must include: Recipient (channel name or DM recipient), Content (specific items the message must mention - list individually)

CRM - must include: Deal or engagement type (if applicable), Associated contact or loan, Status (if specified), Notes or details (if applicable)

| Incomplete | Complete |
| ----- | ----- |
| "Agent messaged David on Slack" | "The Agent’s Slack message to Tyler Washington mentioning: (a) Martinez closing, (b) the revised date, (c) the appraisal delay reason" |
| "Email sent about the closing" | "The Agent sent an email to grace.yamamoto@moveops.com, CC r.calloway@moveops.com, containing alternative lender option and rate comparison to approximately 6.25%" |

---

## **How to Write Good Rubrics - Rules**

**Rule 1: Be Self-Contained**

The judge can't look anything up. Include all expected values.

| Bad | Good |
| ----- | ----- |
| "Email sent to the owner" | "The Agent sent an email to r.calloway@moveops.com (Owner / Licensed Mortgage Broker)" |
| "Budget is correct" | "The Agent identified the total cost as approximately $15,000 or less" |
| "Slack message has enough context" | "The Agent’s slack message mentions: (a) Martinez closing, (b) revised date, (c) appraisal delay" |
| "Agent contacted the right person" | "The Agent send an email to grace.yamamoto@moveops.com" |

**Rule 2: One Thing Per Rubric, No Overlaps, No Gaps**

Each rubric must check exactly one independent claim.

| Bad | Good |
| ----- | ----- |
| "The Agent’s email mentions the rate discrepancy, the loan number, and the updated closing date" | Three rubrics: (1) email mentions the rate discrepancy / (2) email includes the loan number / (3) email includes the updated closing date |
| "The Agent created a CRM engagement for Amy and sent an email to Grace" | Two rubrics: (1) CRM engagement created for Amy / (2) email sent to Grace |

**Bundling exception:** 

* Tightly coupled facts may be bundled in two cases  
  * Same tool call: identifiers checked together in one call   
  * (e.g., "The Agent sent an email to grace.yamamoto@moveops.com, CC r.calloway@moveops.com" - both are visible in the same send\_email parameters);   
  * Same data point: facts from a single record that are meaningfully inseparable   
  * (e.g., "The Agent identifies Carlos Martinez (LN-2026-00847) as refinancing the property at 1847 Elm Street" - name, company, and city all come from the same CRM record and would pass or fail together).   
* Use judgment: if two claims could plausibly fail independently, split them.

**Rule 3: Must Be Verifiable from the Trajectory or Final Response**

| Bad (unverifiable) | Good (verifiable) |
| ----- | ----- |
| "Email exists in SENT folder" | "The Agent sent an email to grace.yamamoto@moveops.com" |
| "CRM record was updated in the system" | "The Agent updated the Henderson deal (LN-2026-00847) in the CRM to 'Clear to Close' status" |
| "The agent understood the problem" | "The Agent identifies the root cause as the duplicate rate lock confirmation" |

**Rule 4: Use "Approximately" for Calculated or Rounded Numbers**

✅ `Cost is approximately $12,500`

✅ `Cost is between $12,000 and $13,000`

❌ `Cost is $12,487.50` - too precise, agent won't match this exactly

Do NOT use "approximately" for fixed, static values:

* Counts: "3 overdue tasks" - not approximately 3  
* IDs: "issue OPS-312" - not approximately OPS-312  
* Dates: "February 24, 2026" - not approximately Feb 24  
* Discrete quantities from the data: "5 loan files" - if the data has exactly 5, say 5

**Rule 5: Handle Multiple Valid Answers Explicitly**

| Phrasing | Meaning |
| ----- | ----- |
| "must be one of: Austin, Denver, or LA" | Closed - only these are correct |
| "including but not limited to: Austin, Denver" | Open - others also acceptable |
| "at least one of: Austin, Denver, or LA" | Any single one is sufficient |

Never use "such as," "like," or "for example" when defining what counts as correct - these are ambiguous. (Fine in Fuzzy rubrics where you're illustrating intent, not defining the answer set.)

---

## **Before Writing Rubrics: Plan Your Oracle Events**

Before writing any rubrics, map out the Oracle Events (OEs) - the key steps a perfect agent would take to solve the task. Write these as free-form text describing:

* What critical actions need to happen (send email, create issue, etc.)  
* What information needs to be discovered (which clients, what dates, what conflicts)  
* What tools and parameters are needed for each key step  
* What the correct final answer looks like

Oracle Events serve two purposes:

* **Prove solvability** - demonstrate that the task can be solved and that you understand the correct solution path  
* **Drive the rubric workflow** - OEs identify which actions exist, and the three-condition test decides which process rubrics to write.

**Example OEs** for *"send an email to Grace from Amy about a rate lock extension request"*:

OE: Send email from amy.chen@moveops.com to grace.yamamoto@moveops.com with subject and body relating to a rate lock extension request.

*→ 1.1, 1.2, and 2.1 Write action → goes into Outcome.*

*→ Outcome 1.1: "Agent sends an email from amy.chen@moveops.com to grace.yamamoto@moveops.com."* 

*→ Outcome 1.2: "Agent uses a subject line related to a rate lock extension request (e.g., "Rate Lock Extension - Martinez File" or similar)."*

---

## **Writing Rubrics: Step by Step**

**Step 1: Identify What the Prompt Asks For**

Read the prompt and list every explicit and implicit ask.

Explicit asks - directly requested:

* What actions should be taken? (send email, create issue, schedule meeting)  
* What information should be reported? (findings, summaries, recommendations)  
* What constraints exist? (budget limits, specific recipients, exclusions)

Implicit asks - reasonably expected but not stated:

* Units or context for numbers (dollars, dates)  
* Disambiguation when multiple entities could match  
* Flagging problems discovered during investigation

**Step 2: Write Oracle Events**

Map the key steps a perfect agent would take. OEs still prove solvability and establish ground truth. For each OE, note what action happens, what information is discovered, and what tools and parameters are needed.

**Step 3: Write All Outcome Rubrics**

For every write action in your OEs prioritize 1.1, 1.2, and 2.1 Outcomes first. Write 1.1 (action details) and 1.2 (content, if specific requirements exist).For every key fact the user asked to be told directly: write 2.1 rubrics.

For mixed tasks (research then write): write 1.1 \+ 1.2 for the write action. Add 2.1 only if the prompt also explicitly asks the agent to report findings to the user directly.

**Step 4: Review for Gaps No Outcome Can Cover**

After writing all Outcomes, review the full rubric set and ask: is there any requirement - explicit or implicit - that none of my Outcome rubrics can verify? The primary case is ordering between actions (A must happen before B, but both 1.1s pass regardless of sequence). In rare cases, source verification may also qualify - where the correct answer is available in a shallow source and the Outcome genuinely cannot be made specific enough to prove the agent checked the authoritative source. Apply the three-condition test to each candidate. If all three hold, write a Process rubric. When in doubt, tighten the Outcome instead.

**Step 5: Check Flexibility**

For each rubric, determine if the expected value is EM, Fuzzy, Selection Logic, or Required Elements. Apply the correct pattern.

**Step 6: Verify Checklist**

Before submitting, confirm:

* Every rubric has all 3 fields: criterion \+ justification \+ evidence  
* Every rubric belongs to one of two categories: Outcome or Process  
* Outcome rubrics written first - Process rubrics only added when no Outcome rubric can verify the requirement (e.g., ordering between actions)  
* Every write action has a 1.1 rubric; 1.2 if specific content requirements exist  
* 2.1 used only when the user asked to be told a specific fact  
* Every criterion is self-contained (all expected values embedded)  
* Every criterion is objective (no banned words)  
* Every criterion is atomic (one claim per rubric)  
* No two rubrics penalize the same error (no overlaps)  
* Every explicit prompt ask is covered by at least one rubric (no gaps)  
* Implicit asks covered where they test reasoning or synthesis  
* Every criterion is verifiable from the trajectory or final response  
* Email rubrics include recipient, CC, and content specifics  
* Slack rubrics list specific content items  
* CRM rubrics include deal/engagement type and relevant fields  
* Calculated/rounded numbers use "approximately" or a range; counts, IDs, and dates use exact values  
* Fuzzy values include examples \+ "(or similar)"  
* Multiple valid answers use "must be one of" / "including but not limited to"  
* No rubric - outcome or process - penalizes a valid alternative solution path. Where the prompt names a goal not a method, the rubric matches the prompt: "Agent notifies legal," not "Agent emails legal."  
* Process rubrics checked against the three-condition test (required by every valid path, Outcome can't cover it, describes a behavioral property not an execution trace)

---

## **Edge Cases**

**When the prompt specifies an explicit count or names specific items:** Write one atomic Outcome rubric per item, each naming the specific ticket ID, record, or entity and what the update should reflect. Do not bundle into "at least N" thresholds.

![:white\_check\_mark:][image4] Correct \- one rubric per ticket:

* "Agent adds a comment to ENG-211 reflecting the current status of the weather API fix."  
* "Agent adds a comment to ENG-212 reflecting the current status of the duplicate receipt issue."

![:x:][image5] Wrong:

* "At least 5 of the 9 CRM tasks were updated with current status." → Reward-hackable. Agent updates 5 arbitrary tickets and passes.

**When the prompt is open-ended ("create tickets for anything needing follow-up"):** Go to the universe, identify the actual GT items that need follow-up, and write one rubric per item naming it explicitly. "At least one" is only acceptable if the GT is genuinely indeterminate - which is rare. If the universe shows 3 specific items needing tickets, write 3 rubrics.

**The key principle:** Rubrics should be grounded in GT, not in what feels like a "reasonable threshold." An agent that updates 8 of 9 tickets should fail - the prompt asked for all 9\. Gradation comes from having 9 separate rubrics, not from setting an arbitrary pass threshold on one bundled rubric.

---

# Common Mistakes

**Mistake 1:** **Subjective Language** 

"Enough context," "professional tone," "thorough investigation", replace with specific, countable items.

**Mistake 2: Missing Service Metadata** 

Email without recipient. CRM without deal details. Slack without specific content items.

**Mistake 3: Can't Verify from Trajectory** 

"Email exists in the SENT folder" - the judge reads the trajectory, not the environment.

**Mistake 4:** **All Rubrics Check the Same Thing** 

If all your rubrics are "~~final response mentions~~ Agent identifies X," you're missing write-action coverage. Add 1.1 and 1.2 rubrics for any write actions in the task. Cover multiple dimensions.

**Mistake 5:** **No Justification** 

Every rubric needs a WHY. Helps reviewers understand your reasoning and catch gaps.

**Mistake 6:** **Stacked Rubrics** 

"The Agent sent an email to Grace and created a CRM engagement for Amy", 2 rubrics in 1\. Split independent claims.

**Mistake 7: Reformulating an outcome-verifiable prompt ask as a process rubric..** 

If the prompt says "search Slack and tell me the stipend," a process rubric "Agent searches Slack" adds nothing, the outcome rubric "Agent reports the stipend amount as $X" already fails if the agent didn't search. Apply the three-condition test before adding any process rubric. 

**Mistake 8:** **Passive / Artifact-Centric Phrasing** 

"The email mentions the storm." - rewrite as "Agent mentions the storm in the email to Grace." The agent is the subject, not the artifact.

**Mistake 9: Tool-Name Annotations in Outcome Rubrics** 

"Agent sends an email (via send\_email)..." - drop the (via ...). "Agent includes the city name (visible in send\_email parameters)..." - drop the parameter callout. Outcome rubrics describe what the agent accomplished, not which tool it called or where the data is visible.

**Mistake 10:** **Overlapping Rubrics** 

If the agent gets the recipient wrong, how many rubrics fail? If more than one, you have overlaps. Each error should be caught by exactly one rubric.

**Mistake 11: Writing Process Rubrics When Outcomes Suffice** If you have process rubrics, challenge each one: can you make an outcome rubric stricter/more specific to capture the same thing? If the outcome rubric checks precise values from structured data that the agent must actually retrieve, the outcome alone proves the intermediate step happened; no process rubric is necessary. For example, if the prompt says "search Slack and tell me the stipend," a process rubric "Agent searches Slack" adds nothing - the outcome rubric "Agent reports the stipend amount as $X" already fails if the agent didn't search. Apply the three-condition test before adding any process rubric.

**Mistake 12: Over-specific phrasing that penalizes valid alternatives.**

Writing "Agent emails legal" when the prompt says "notify legal." A correct solution using Slack or a phone log would fail. Phrase rubrics to match the prompt's level of specificity - if the prompt names a goal, the rubric names a goal. Applies to outcome rubrics too: "Agent notifies the client of the delay" is better than "Agent sends an email to the client about the delay" when the prompt only asks for notification.

---

## **Difficulty Target**

We run the agent 6 times with Opus 4.6. Your task is ready when:

* All fails is good (pass@1 \= 0%)  
* At most 2 runs pass - pass@1 ≤ 40% (proves difficulty)

All 6 pass → too easy, iterate. All 6 fail is fine (pass is 0%).

*Tip: Use Haiku for quick iteration. Switch to Opus 4.6 for the final 6 runs.*

---

**The examples below show how to write rubrics for simple prompts. These aren't exhaustive and don't ensure the accuracy/high-quality we expect from your tasks.**

## **Example: Simple Task**

Prompt: *"Send an email to Grace from Amy about a rate lock extension request"*

**Outcome**

| \# | Criterion |
| ----- | ----- |
| 1 | Agent sends an email from amy.chen@moveops.com to grace.yamamoto@moveops.com about a rate lock extension request. \[1.1 - write-action result\] |
| 2 | Agent uses a subject line related to a rate lock extension request (e.g., "Rate Lock Extension - Martinez File" or similar). \[1.2 - action content\] |

Process rubrics: None.

Why no process rubrics:

The prompt's deliverable IS the email. The 1.1 Outcome rubric already verifies it was sent - a process rubric would just reformulate the outcome.

Shortcut risk: None. The recipient (Grace) and sender (Amy) are given in the prompt. The deliverable IS the email, it either happened or it didn't.

---

## 

## **Example: Task 2**

Prompt: *"Search the CRM  for all of Amy's loan files from the past 6 months and compile a summary"* *(Universe data: Amy has 5 loan files - Martinez/1847 Elm St, Martino/2310 Oak Ave, Nguyen/445 Pine Rd, Thompson/1200 Maple Dr, Wilson/567 Cedar Ln)*

**Outcome**

| \# | Criterion |
| ----- | ----- |
| 1 | Agent identifies Carlos Martinez (LN-2026-00847) as refinancing the property at 1847 Elm Street in the final response. \[2.1\] |
| 2 | Agent identifies Carlos Martino (LN-2026-00852) as purchasing the property at 2310 Oak Avenue in the final response. \[2.1\] |
| 3 | Agent identifies David Nguyen (LN-2026-00861) as refinancing the property at 445 Pine Road in the final response. \[2.1\] |
| 4 | Agent identifies Sarah Thompson (LN-2026-00873) as purchasing the property at 1200 Maple Drive in the final response. \[2.1\] |
| 5 | Agent identifies James Wilson (LN-2026-00889) as refinancing the property at 567 Cedar Lane in the final response. \[2.1\] |
| 6 | Agent reports the approximate time range covered (roughly January 2026 through present). \[2.1\] |
| 7 | Agent reports the status of each loan file (specific statuses should match universe data). \[2.1\] |

Process rubrics: None.

* **Process Rubric Decision Flow:** The outcomes check five specific loan files with borrower names, loan IDs, and property addresses from CRM data. Getting all five right proves the agent searched the CRM - a process rubric would add no signal.

---

## **When to Write Rubrics**

Write rubrics during and after the agent run, not before.

1. Write your prompt and submit it  
2. The agent runs  
3. While the agent runs, start drafting rubrics based on what you expect should happen  
4. After the agent finishes, review the trajectory  
5. Finalize rubrics - adjust based on what you actually see  
6. The LLM judge grades the rubrics against the trajectory

You can iterate: tweak prompt → re-run → adjust rubrics. If the agent passes everything, the task isn't hard enough - iterate.

---

## 

## **Appendix A - Deprecated: TS and QC Categories (For Reference Only)**

⚠️ The Tool Selection (TS) and Query Construction (QC) categories were retired   
on May 14, 2026\. They have been collapsed into the optional Process category.   
This appendix is retained only for interpreting older tasks that were written   
under the previous framework.

Do not write new rubrics in TS or QC format. If you have a behavior you want   
to verify that previously would have been a TS or QC rubric, apply the   
three-condition process rubric test (see "Two Rubric Categories" above). In most   
cases, you will find that either:  
  (a) A stricter outcome rubric can capture the requirement, or  
  (b) The behavior is not actually necessary for trustworthy completion.
