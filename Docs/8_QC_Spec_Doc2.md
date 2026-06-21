# Project Context:

```
This project ("MCP Advanced") focuses on improving AI agent performance by creating realistic, long-horizon, tool-heavy training tasks inside a shared business simulation ("Brookfield CPAs & Advisors"), a Chicago-based US public accounting and business advisory firm. The goal is to produce scenarios where a capable agent must investigate across many internal systems (Oracle GL, SAP Subledger, BlackLine, Records Vault, Airtable, Linear, email, Slack, and other servers), reconcile conflicting or incomplete information, and then take concrete workplace actions (post journal entries, approve AP invoices, certify reconciliations, file documents under retention codes, send emails, update records, etc.).

Contributors author natural, open-ended work requests that are intentionally difficult in realistic ways (e.g., similar entities that can be confused, hidden root causes spread across services, mismatched data between systems, approval/policy constraints, or time pressure). Tasks are designed to force extensive exploration (target 40+ tool calls) and to remain solvable only when the agent treats tool outputs as the Single Source of Truth (SSOT) rather than relying on user statements or general knowledge.

Each trajectory is evaluated using rubrics with two categories (Outcome mandatory, Process optional) to judge both results and necessary process. Task submissions are considered ready when they meet the project's difficulty targets across multiple runs: the task is solvable with deep investigation, but hard enough that models reliably fail at least some rubric criteria in a portion of runs (e.g., pass@1 ≤ 40% across the standard evaluation set).
```

---

# Audit Workflow:

## 1. Review the task instructions:

```
    - Overall Task Instructions
    - Rubric Guidelines
    - Loading and Editing Universes/Running Agents
    - Brookfield CPAs & Advisors Universe Summary: summary of the base universe, including the list of characters in the universe along with their personalities
    - Go through the common auditing mistakes in the appendix
```

## 2. Evaluate the Prompt

```
Verify the prompt is original, human-like, non-repetitive, and is coherent with the selected Persona.

Key checks:
    - Prompt isn't pre-solved
    - Doesn't prescribe steps
    - One coherent scenario
    - Requires multi-service investigation + at least one action
```

## 3. Evaluate universe/data feasibility

```
Use the universe explorer to confirm the task is solvable:

    - The key entities (clients, employees, deals, tickets, calendar events) referenced or required by the prompt exist.
    - The required cross-service artifacts exist where implied (e.g., an email thread and a matching CRM record if the task depends on both).
    - Any claimed universe edits are coherent (dates/names align across services).
        -  Check Sandbox > _changelog table to see what entries the CB updated/inserted/removed
        - The universe explorer should show the state after the changes have been made
    - 05/02 NOTE: The "timestamp" column in "Database > Tables > _changelog" is auto-generated and should not be evaluated for date alignment.
```

**Suggested:** Use the prescribed LLM workflow to speed up your universe exploration and for finding the ground truth

## Prompt:

Use the following prompt to generate exploratory prompts to speed up your assessment of the universe and finding the ground truth. The resulting prompts can be used with the agent embedded within the universe explorer. As always, DO NOT blindly trust LLM outputs – Validate the answers you get from the embedded agent by confirming against the data in the universe.

```
Act as an Expert Investigator. Your goal is to map out exactly how an AI agent should explore the Brookfield universe to solve the task described in my prompt. 

Here is what you have access to (see attachments):
The Task Prompt: The exact natural-language request given to the agent.
The Company Summary: High-level details about Brookfield CPAs & Advisors, its employees, clients (Brookfield itself, Northstar Legal LLP, Acme Cloud Inc), and ongoing scenarios.
The Available Tools: The specific MCP tools (Oracle GL, SAP Subledger, BlackLine, Records Vault, Airtable, Linear, Email, Slack, Contacts) available to query the universe.

Your Task: Review the Task Prompt and generate a rigorous "Exploration Plan." I do not want you to guess the answers. Instead, give me the specific, structured questions and search queries you would run against the universe to find the ground truth, expose any contradictions.

Queries or questions should be simple as if a manager is speaking naturally to their assistant. Keep it detailed. Refer to server names but not specific tool names.
```

1. Evaluate the Agent Trajectories

```
Click through each of the completed agent runs to confirm the following:

    - Ensure the average tool call count across all trajectories is at least 15. 
    - Ensure in at least one trajectory the agent used multiple services.
    - Check whether the agent's reported facts are grounded in tool outputs.
    - Confirm required actions (emails/tickets/calendar/CRM updates) were actually executed in-trace (tool call + success response), not merely claimed in narration.
```

1. Evaluate Oracle Events (OEs)

```
Check OEs cover the critical path to solving the prompt.

Ensure OEs match the prompt and map cleanly to rubrics (i.e., each write action in OEs has an Outcome rubric; each non-write-action step is evaluated against the three-condition Process test - required by every valid path, Outcome can't cover it, describes a verification not an execution trace).

(These are not sent to the customer, but are only written so as to help the CBs write good rubrics. Any issues with this step are non-fails only)
```

1. Evaluate the Rubric Set

```
Ensure they:
    - Are aligned with the Prompt and Oracle Events,
    - Are atomic, observable, and testable,
    - Have appropriate justifications and evidence, and 
    - Together correctly measure both final outcome correctness and process correctness.
```

1. Verify "valid failure" exists

```
Confirm at least one run fails at least one rubric criterion for a meaningful reason such as:

    - incorrect conclusion vs tool output
    - missed critical record
    - wrong recipient / wrong entity resolution
    - failure to execute required action
    - ungrounded claim that matters
```

---

# General Grading Instructions (How the 1-5 scale is used)

1. General Grading:
  - Grade to the lowest dimension across all rubrics (e.g. if instruction following is a 2, the turn should be rated a 2)
    - If the turn meets any criteria under 1-2 Fail, the turn is a fail.
    - If the turn does not fail and it meets criteria for a 3-4 [Not-Fail] on any dimension, then the turn must be a 3-4 [Not-Fail]
    - All task-level dimensions must be a 5 for the task to receive a 5.
2. Choosing 1 vs 2 or 3 vs 4:
  - When deciding between a 1 or 2, select a 1 if the attempter put little to no effort
    - When deciding between a 3 or 4, use your best judgement on how serious you think the minor issue affects the quality of the task.
3. Prompt instructions or task instructions should always take precedence over other dimensions
  - For example: if the task instructions asks the user to intentionally make spelling mistakes in the prompt, spelling errors in the prompt would not be marked towards a fail.

---

# Grading:

The full scoring guideline table (all dimensions, sub-dimensions, and 1-2 / 3-4 / 5 criteria) is maintained in `Docs/7_QC_Spec_Doc1.json`.

---

# Appendix:

**Appendix**

---

## **Rubric Quality Definitions**


### Major Issues

#### Missing Criteria - Outcome

**Definition:** Count one Major issue for each missing Outcome rubric that checks for an explicit requirement in the prompt. This dimension only concerns "Outcome" criteria.

Outcome rubrics must collectively check for:
- Whether the user's request was fulfilled or not (e.g., was the email sent? was the investigation completed?)
- Whether the final user-facing response is accurate and aligned with findings (e.g., correct names, dates, dollar amounts)

**Flag Missing Criteria - Outcome when:**
- The rubric set contains no criterion checking whether the user's core request was fulfilled
- The rubric evaluates only process/trajectory behavior with no user-facing outcome checks
- An explicit prompt requirement that affects the final answer or action is not represented by any Outcome criterion
- A write action (post a journal entry, approve an AP invoice, certify a reconciliation, create a Linear issue, update an Airtable record, file a document – basically any action that changes the state of the universe) has no Outcome rubric verifying it succeeded with correct details

**05/05 NOTE:** Because there will be entries in the Universe that take place after the cut-off date (Jun 12, 2026), if a potential criteria requires data that takes place after said date, then it is not valid and shouldn't count towards "Missing Criteria" if not mentioned in the rubric.

Example:
- Prompt: "IDs that are explicitly mentioned in Slack need to be emailed"
  - If an invoice ID is mentioned in Slack on June 20th 2026 and the cut-off is June 12th 2026 then it should be ignored (cannot be considered missing).
  - If it is included as a rubric and it results in model failure, then that would result in [Fail - Universe Misaligned with Today].
  - If it is included as a rubric and it does not result in any model failure, then the rubric item should be considered an Incorrect Criteria.

---

#### Criteria Not Self-Contained

**Definition:** Criterion cannot be evaluated against the model response without access to the universe, personas, tool schemas, and/or external facts/information.

Every rubric must be self-contained. The LLM judge sees the trajectory and final response, all the rubric criteria (one rubric item can be used as context for another) and the original prompt - not the universe, not the personas, not the tool schema or any other external information. All expected values must be embedded directly in the criterion text.

This applies to process/reasoning rubrics too. They can't be dependent on the tool outputs. The only exception is when more than one tool is valid for answering a prompt, in which case the rubrics should test for the intent of the model and can depend on tool outputs instead of being precise and self-contained.

**Bad rubric examples (not self-contained):**
- [Outcome] "The Agent emails the Managing Partner." → Judge doesn't know who the Managing Partner is. Must say: "The Agent sends an email to steven.perry@brookfieldcpas.com (Managing Partner)."
- [Outcome] "The reconciliation variance is correct." → Must say: "The Agent identifies the variance as approximately $1,800 or less."
- [Outcome] "The Agent contacted the right person." → Must say: "The Agent sends an email to daniel.jones@brookfieldcpas.com." (if "the right person" was not mentioned in the prompt)

**Good rubric examples (self-contained):**
- [Outcome] "The Agent sends an email to daniel.jones@brookfieldcpas.com." → Expected value fully embedded
  - **Note:** Write actions (any action that changes the state of the universe) are always Outcome.
- [Outcome] "The Agent identifies the Acme Cloud ASC 606 deferred-revenue release as $42,500 for FP-2026-05 in the final response." → All expected values (entity, standard, amount, period) are in the criterion.

---

#### Criteria Not Atomic

**Definition:** Criterion groups two or more constraints that are unrelated, which results in a rubric item with no clear focus on what aspect of the response it's trying to evaluate.

Each rubric should evaluate one thing only - no bundling of multiple independent behaviors. Ask yourself: if this criterion fails, is there exactly one clear reason why?

**Acceptable bundling (NOT a violation):**

**Outcome rubrics may bundle tightly coupled facts from the same source:**
- "The final response lists the FP-2026-05 Acme Cloud deferred-revenue JE as $42,500, posted, in the approved state."
- Amount + period + status are all attributes of the same journal entry and would be right or wrong together.
- General rule (03/04): Assessment of multiple components within one tool output can be grouped. Components from separate tool outputs should NOT be grouped.

**Not atomic (violation):**
- "Email sent to Daniel and a Linear issue created for the AP exception." → Independent actions - must be two separate rubrics.
- "The agent reviewed the Acme reconciliations and sent a summary email to Andrea." → Investigation step + write action = two independent claims.
- "The email mentions the variance, names the affected account, and includes the recommended adjusting entry." → Three independent content requirements - should be three rubrics (unless all come from the same tool output).

---

#### Incorrect Criteria

**Definition:** A rubric criterion checks for behavior that does not align with the prompt requirements, the Oracle Events, or valid logic.

Count one Major issue for each criterion that:
- Contradicts the prompt or Oracle Events (e.g., checks for the wrong recipient, wrong date, wrong entity)
- Contains a factual error that's not grounded in the tool outputs or universe data
- Requires behavior that would lead to an incorrect or misleading outcome
- Is not an explicit requirement in the prompt and implementing it does not make the response better in any way

**Important clarifications:**
- Incorrect ≠ overly strict. A strict criterion is acceptable if it reflects required behavior.
- Incorrect ≠ suboptimal. If a criterion is merely inefficient or awkward, consider Minor or Moderate issues instead.
- Before classifying any issue as "Incorrect Criteria," check if a different, more specific error category would apply. For example, if a criterion is overly specific, count it as "Overly Specific Criteria" (Minor), not Incorrect.
- Minor Wording Errors are NOT counted as Incorrect Criteria. Minor wording errors that might make the criterion potentially misleading can be flagged as non-fails. See [Purely Non-Failing Issues > Rubric Wording Errors]. It should still be possible to read the criterion with the proper intent; otherwise, this does not apply.

**Auditor source of truth:** Use the Oracle Events / universe data as the source of truth. Universe data should be treated as static for evaluation purposes.

**Incorrect vs Overly Broad:** If a criterion accepts all valid responses, but happens to also accept some invalid responses, flag that as [Overly Broad Criteria] **(03/26)**

---

### Moderate Issues

#### Overlapping or Redundant Criteria (Updated 05/22)

**Definition:** Criterion is either completely redundant because other criteria completely encompass it, or multiple criteria check for the same thing partly. Count each completely redundant criterion as one Moderate issue, or count multiple overlapping criteria as one Moderate issue.

**Example:**
- Criterion 1: "The Agent sends an email to daniel.jones@brookfieldcpas.com." [Outcome 1.1]
- Criterion 2: "The Agent successfully contacted daniel.jones@brookfieldcpas.com." [Outcome]
- Both check the same thing - email sent to Daniel. One is redundant.

**Notes:**
- Key test: Would removing one criterion change scoring outcomes? If not, redundancy exists.

---

#### Incorrectly Labeled Category (Updated 05/22)

**Definition:** Criterion is incorrectly categorized by selecting the wrong rubric category.

**Category List:**
- **Outcome:** What was the result? What does the user see? All write actions go here. Outcome subtypes are:
  - [1.1] Write-action results - did the right action happen with the right details? (verified from trajectory)
  - [1.2] Action content - does the content match what was needed? (verified from trajectory parameters)
  - [2.1] Key facts/findings - when the final response is a deliverable
- **Process:** Whether the agent did the unspoken-but-necessary work to arrive at the final result legitimately and cannot be fit in an Outcome Rubric.

**Common mislabeling errors:**
- A criterion that a (stricter) Outcome rubric could fully verify, labeled as Process → should be Outcome (or deleted)
- A criterion checking whether a write action succeeded labeled as Process → should be Outcome
- A criterion naming a specific tool or query path labeled as Process → should be deleted or rewritten as a behavioral verification

---

#### Overly Broad Criteria (ADDED 03/26)

**Definition:** Criterion is too broad or overly permissive such that it would accept all valid responses, but also some invalid responses too.

**Example:**
- Prompt: "Give me the contact details of exactly one point of contact for xyz client"
- Correct answer: any of John, Jack or Jill
- Overly Broad Criterion: "The Agent mentions one of John, Jack, Jill or Joe as the relevant point of contact for xyz client."
- This criterion would accept three valid responses but also one invalid response (Joe)

**Exception:** If the invalid paths that are accepted by the overly permissive criterion are unlikely to occur, do not flag the criterion as overly broad. See the Examples tab for an explanation on this scenario.

**(05/22) Note:** With the Rubrics V3 update, criteria will be considerably broader, but they should still reflect a ground truth and do not leave room for wrong answers.

---

### Minor Issues

#### Overly Specific Criteria (Updated 05/22)

**Definition:** Criterion is too specific such that it only accepts a subset of valid responses and would falsely punish the model for completely valid actions.

The criteria should not be overly specific in how the agent can fulfill the goal. If there are multiple valid routes the agent can take, the criteria should not falsely punish the agent for a valid decision.

**The main scenario where this applies: Outcome content requirements:**

A 1.2 or 2.1 criterion specifies exact wording for agent-generated content when multiple valid expressions would satisfy the intent.
- ❌ Overly specific: "The email body must include the phrase 'we apologize for the delay in certifying the reconciliation.'"
- ✅ Correct: "The Agent's email includes an acknowledgment of the reconciliation certification delay (or similar)."
- ❌ Overly specific: "The Agent must state 'the Acme AP invoice is the highest exposure at $52,140.00.'"
- ✅ Correct: "The Agent identifies the Acme AP invoice as the highest-exposure item with an approximate amount (or similar)."

**Exception - Strict values are never overly specific:**
- Email addresses, IDs, dates, and exact strings pulled directly from universe data should always be exact. These are not overly specific - there is only one correct value.
- ✅ "The Agent's email includes the client name 'Acme Cloud Inc.'" - exact string from data, correct as strict.
- ✅ "The Agent sends an email to daniel.jones@brookfieldcpas.com." - one correct recipient, correct as strict.

**Rules of thumb:**
- Structured fields with one correct value (email addresses, IDs, dates) should be exact - NOT overly specific
- Freetext fields (email subjects, issue titles, agent-generated descriptions) must include "(or similar)" or list alternatives - exact values here ARE overly specific
- The test: could a competent agent pass a different but equally valid value? If yes, the criterion should allow it

**Note: Write action (any action that changes the state of the universe) parameters always go in Outcome.**

---

### Purely Non-Failing Issues

#### Rubric Wording Errors

**Definition:** Minor wording errors or typos in the rubric criteria that slightly alter the meaning of what's being checked, but in practice would not cause an LLM judge to evaluate incorrectly.

**Example:**
- Prompt asks about "Q3 travel spending"
- Rubric says: "The final response must include Q3 travel expenses"
- "Spending" vs "expenses" is a minor wording difference that wouldn't affect evaluation

**Example:**
- Prompt asks to check what "Friday special" items were available
- Tool output lists "Sausage Roll" as a Friday special item
- Rubric says: "The Agent correctly identifies sausage roll as one of today's specials"
- "Friday special" vs "today's specials" is a minor wording error - semantically different, but in most cases wouldn't affect trajectory evaluation

**How to assess:** Would an LLM judge, reading the trajectory, prompt and the rubric criteria, flag the response as incorrect because of the wording difference? If not, it's a non-failing wording error. If yes, escalate to Minor (Overly Specific) or Major (Incorrect) depending on impact.

It should still be possible to read the criterion with the proper intent; otherwise, this exception does not apply and the issue should be escalated. See [Major Issues > Incorrect Criteria] for more context.
