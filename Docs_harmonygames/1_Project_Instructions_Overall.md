# **Overall Instructions**

---

## **💡 Change Log Last Updated:** Jul 28, 2026

| Date | Type | Description |
| :---- | :---- | :---- |
| **Jul 28, 2026** | **Documentation refresh** | Clarified authority, active Persona ACL read visibility, complexity targets versus evaluator/QC floors, rubric storage, OE non-authority, and HarmonyGames examples. |
| **Jul 17, 2026** | **HarmonyGames Universe** | Docs updated for the HarmonyGames universe. Environment ID: `hg4-2026-07-02-env`, Base Universe ID: `hg4-2026-07-02`, fixed simulation date: February 28, 2026. The IDs retain legacy provisioning labels. |

## **Where Rules Come From**

Start with the [`Docs/README.md`](README.md) reading path. Use the following hierarchy instead of treating every guide or example as equally authoritative:

1. [`HarmonyGames_Base_Universe/Tool_Access/*.json`](../HarmonyGames_Base_Universe/Tool_Access/) controls enabled services, exact tools, parameters, and operations.
2. [`Docs/15_Persona_ACL.md`](15_Persona_ACL.md) and its exact linked roster control task-visible identity and persona-scoped read visibility.
3. The live service data, task injection/changelog,
   [`HarmonyGames_Base_Universe/`](../HarmonyGames_Base_Universe/), and
   [`6_Universe_Schema.json`](../HarmonyGames_Base_Universe/6_Universe_Schema.json)
   control live task/universe facts and database structure.
4. The prompt and any uniquely discoverable company record it validly incorporates control what the Agent was asked to do.
5. [`Evals/`](../Evals/) provide the current procedures and repository-level
   policy overrides; [`7_QC_Spec_Doc1.json`](7_QC_Spec_Doc1.json) and
   [`8_QC_Spec_Doc2.md`](8_QC_Spec_Doc2.md) define the scored dimensions and
   their interpretation.
6. These authoring docs and `QC_Tasks/` are guidance and calibration. Current authorities above override stale example wording.

Oracle Events are internal planning notes. They help prove solvability, but never override the prompt, universe, catalogs, trajectory evidence, rubrics, or current Evals.

## **Your Goal**

Create complex tasks for an AI agent operating inside the **HarmonyGames** universe — a founder-led mobile game studio. The agent has access to the company's Slack, Linear, GitHub, Gmail, Google Drive/Docs/Sheets/Slides, Trello, Confluence, Contacts, Google Calendar, and Snowflake.

You're looking for situations where the AI agent could fail — where it misses something, gets confused, makes a wrong assumption, or doesn't explore deeply enough. A good task is one where the agent needs to dig through many data sources and still gets something wrong.

**What this means concretely:**

* **Authoring target:** average 40+ necessary tool calls across runs and genuine use of 3+ enabled services.  
* The task should involve investigation and action — the agent reads data from several sources, reasons about it, then takes actions (posts Slack messages, creates Linear issues, updates Trello cards, creates Drive docs, etc.)  
* The agent must fail on at least some rubric criteria. If the agent solves your entire task perfectly, it's not hard enough. Iterate.

These are design targets, not the lower rejection floors. [`Evals/1_Prompt_Eval.md`](../Evals/1_Prompt_Eval.md) rejects a prompt that does not require **more than 15** calls or genuine use of **at least 2** enabled services. QC separately fails trajectories averaging **fewer than 15** calls and uses a **2-service** cross-service floor. Thus `40+ / 3+` is the authoring goal; `>15 / 2+` is the prompt-evaluation floor; `>=15 average / 2+` is the QC floor. Merely clearing a floor does not meet the authoring target.

### **Long-Horizon Tasks**

If a task is assigned or proposed as long-horizon, read `Docs/14_Long_Horizon_Task_Guidelines.md` before designing, attempting, or reviewing it. A long-horizon task has at least one agent run with 500–1,000 tool calls. The volume must come from necessary work over a source-defined cohort or separately exposed evidence—not repeated reads, arbitrary checkpoints, unnecessary writes, or instructions designed to manufacture calls.

**What you are NOT creating:**

* Simple lookups ("How many unread emails do I have?"). Too easy, too few tool calls.  
* Single-service tasks ("Search for PRs in the match3d repo"). We need cross-service reasoning.  
* Command lists ("Step 1: search emails. Step 2: check Linear. Step 3: send Slack message."). The agent should figure out the steps.  
* Tasks solvable without tools ("What's the best way to handle a failed fundraise?"). We must require actual data.  
* Contrived or artificial scenarios that trick the model rather than test real capability.

**You will:**

* Explore the universe to understand the data and find interesting situations  
* Edit the universe to add complexity (encouraged — the base universe has limited natural difficulty)  
* Write a prompt — a natural work request that requires broad exploration  
* Run the agent  
* Write rubrics — during and after the agent run, write specific criteria to grade the agent (see Rubric Guidelines)

---

## **Step 1: Understand the Universe**

### **Your Universe**

You will receive the HarmonyGames base universe. This is your universe to explore, edit, and build tasks from. Other CBs have their own copies. Your edits won't affect theirs. This prevents task overlap and lets you build deep familiarity with your data over time. The first few tasks may take longer as you learn the universe; subsequent tasks should be faster.

### **The Universe Guide**

Read the Universe Guides to understand the company's background, key personas and their relationships, all pre-built scenarios and storylines, and what data exists across services (Slack, Linear, GitHub, Gmail, Drive, Trello, Confluence, etc.)

* [HarmonyGames — Universe Summary](../HarmonyGames_Base_Universe/1_Universe_Summary.md) — company, org chart, storylines by lens, and systems.
* [HarmonyGames — One-Pager](../HarmonyGames_Base_Universe/0_Universe_One-Pager.md) — quick overview.
* [HarmonyGames — Persona Briefs](../HarmonyGames_Base_Universe/2_Persona_Briefs.md) — per-persona active work, relationships, and open threads.
* [HarmonyGames — Task Categories](../HarmonyGames_Base_Universe/3_Task_Categories_Business_Functions.md) — 6 business functions, write-tool matrix, and worked prompts.
* [HarmonyGames — Reference Sheet](../HarmonyGames_Base_Universe/4_Reference_Sheet.md) — personas, externals, service structures, and environment/universe IDs.

**Fixed date for the HarmonyGames universe:**

* HarmonyGames Universe — fixed date as **February 28, 2026**

### **Your Assigned Persona**

You will be assigned one of the 17 task-visible personas through the taxonomy. Use the exact identity and email in [`Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/Persona_ACL_Roster.json); never derive an email from a name. Your tasks should make sense from this persona's perspective — Leonard wouldn't debug VFX animations, Julia wouldn't audit financials, Douglas wouldn't negotiate vendor deals.

If your assigned persona is "saturated" (you've exhausted the interesting situations for that role), you may switch to a different roster persona through the taxonomy. When you do, mark which persona the task is written for so we can track the distribution. Do not touch the AMV persona dropdown: it overrides the taxonomy selection and persists.

Every persona receives the same 13-service catalog, but Persona ACL actively scopes reads on Gmail, Slack, GCal, and Contacts. Reads on GDrive, GitHub, Snowflake, GDocs, GSheets, GSlides, Trello, Linear, and Confluence are unscoped. Writes are outside Persona ACL scope; use the tool catalogs, not ACL, to determine write capability. See [`Docs/15_Persona_ACL.md`](15_Persona_ACL.md).

The environment automatically applies `set_acting_user` with the roster's exact email after universe load and reapplies it for every run and turn. This is environment configuration, not an Agent tool, Oracle Event or rubric process requirement, or task-call contribution. The Agent Runner and Run Verifiers use the same required persona.

There is no task-visible Finance persona or CFO. Finance is a business function and must be paired with an appropriate persona from the roster.

### **Personas** 

* In the universe summaries you will see them like this:

| Name | Title | Location | Best for |
| ----- | ----- | ----- | ----- |
| Leonard Hayes | Co-founder & Creative Director | Remote | Fundraising, live-ops strategy, vendor/partner arcs, runway/wind-down, Mattel pitch |
| Arthur Blake | Co-founder & CTO | Remote | Engineering tooling, difficulty-sim, WebGL/build-size, backend, board/equity |

  Leonard and Arthur are central to the HarmonyGames universe.


* In the persona briefs documents, you will have access to detailed information about each persona, like Brian Foster:

***Brian Foster -- Game Engineer***

***Active work:** Drives cross-title live-ops features (Win Streak, Leaderboards, Collect & Win, Season Pass, Daily Login/Gift) and difficulty-tuning workstreams across GoD and match3d. Owns live-ops UI optimization tickets.*

***Key relationships:** Owen Baker, Oliver Brooks, Calvin Price, Douglas (engineering); Martin Walsh/Marcus Bennett (art); Leonard Hayes/Robert (product direction).*

***Open threads:***

* *Live-ops UI optimization (ENG-2404) · Collect & Win Magical Wings tuning · Combo Fighter UX proposal.*

***Recent activity:** `#winandcollect`/`#season-pass`/`#zm-collect-win` threads, Linear ENG/ZOM live-ops tickets, reward-table specs (Sheets).*

**Explore the universe and be familiarized with how it works and behaves\!**

### **Important note**: You do not need to write "I am Leonard Hayes" in the prompt. The platform supplies the taxonomy-selected identity. That persona shapes both the work request and read visibility on Gmail, Slack, GCal, and Contacts.

### **What Data Can the Agent Access?**

The agent has exactly 13 task-visible services: Slack, Linear, GitHub, Gmail, GDrive, GDocs, GSheets, GSlides, Trello, Confluence, Contacts, GCal, and Snowflake. For prompt writing, you do not need to specify tool names or parameters. Required evidence must both exist in the universe and be readable by the assigned persona; author visibility in Universe Explorer is not sufficient for a scoped service.

**⚠️ Important tool constraints for HarmonyGames:**
* [`HarmonyGames_Base_Universe/Tool_Access/`](../HarmonyGames_Base_Universe/Tool_Access/) is the authority for enabled tools; see the concise [Tool Access Guide](0_Tool_Access_Guide.md).
* **Gmail is triage-capable, but cannot send** — it supports read/search, attachments, label changes, archive, trash/untrash/delete, and label creation/deletion. There is no send/reply/compose tool.
* **Snowflake is read/query-only** — it lists and describes warehouse objects and runs queries; it is not a write surface.
* **Exactly 13 service catalogs are enabled:** Gmail, GDrive, GitHub, Snowflake, Slack, GCal, GDocs, GSheets, GSlides, Trello, Linear, Contacts, and Confluence.
* **Persona-scoped reads apply only to Gmail, Slack, GCal, and Contacts.** List and search results are filtered, and a known object ID does not bypass visibility; inaccessible by-ID reads are denied or return not found.
* **The other nine services are unscoped for reads. Persona ACL does not govern writes.**
* **No direct tools exist for CRM, Airtable, QuickBooks, Firebase, BigQuery, Metabase, App Store Connect, Google Play, AppLovin, Singular, Figma, Carta, or Stripe.** Those names may appear as business topics or evidence recorded inside enabled services, but the agent cannot query them directly.

---

## **Step 2: Explore and Edit the Universe**

### **Explore**

**The HarmonyGames Universe**

* [**HarmonyGames — Universe Summary**](../HarmonyGames_Base_Universe/1_Universe_Summary.md) (please read carefully)
* [**HarmonyGames — One-Pager**](../HarmonyGames_Base_Universe/0_Universe_One-Pager.md)
* [**HarmonyGames — Reference Sheet**](../HarmonyGames_Base_Universe/4_Reference_Sheet.md) (personas, channels, repos, env/uni IDs)

Use Universe Explorer author god-mode and the chat agent to understand what data exists. Before relying on Gmail, Slack, GCal, or Contacts evidence, confirm it from the assigned persona's Agent/Verifier view:

* Search Gmail for interesting investor threads, vendor negotiations, legal closings  
* Browse Slack channels for product decisions, feature debates, live-ops incidents  
* Check Linear for open issues, stalled tickets, shipped-vs-stuck status  
* Look at GitHub for PR history, CodeRabbit-only reviews, merge activity  
* Check Drive for GDDs, financial models, pitch decks, legal docs  
* Browse Trello for roadmap boards, sprint status, feature cards  
* Read Confluence for architecture docs, GDDs, OKRs, runbooks

Here's a non-exhaustive list of what to look for:

* Someone made a mistake: Wrong PR merged, mixed-up entities, missed follow-up on a ticket  
* Incomplete work: Stalled prototypes (Zombie Match Lite, 4X, RPG), unfinished features, abandoned branches  
* Conflicting information: GDD says one thing, implementation says another, Slack discussed a third  
* Business pressure: Failed bridge round, wind-down, the Mattel pitch, vendor churn  
* Hidden root causes: The obvious explanation is wrong; the real cause is buried across Linear + GitHub + Slack + Drive

### **Edit**

Here's a non-exhaustive list of what you can add:

* Slack messages that surface a new problem or miscommunication  
* Linear issues that the agent needs to discover and triage  
* GitHub issues or PR comments that create contradictions  
* Trello cards with stale/wrong status  
* Drive docs with conflicting specs  
* Confluence pages with outdated architecture decisions

**Danger Zone:** The chat agent for editing is currently unconstrained — it will make whatever changes you ask for without checking for conflicts. This means:

* It won't detect if your new data contradicts existing data (dates, names, relationships)  
* It won't cascade changes — if you rename a person in Slack, their Linear/GitHub/Drive data won't update automatically

You must manually review edits for:

* Universe consistency: Do dates, names, and facts align across services?  
* Storyline consistency: Does the new data make sense in this universe story?  
* Cross-service coherence: If you add a Slack discussion about a PR, does that PR exist in GitHub?

**Current platform status:** use the Chatbot Agent or Sandbox SQL for edits and
review the resulting ChangeLog manually. Scenario Generation has been offline
since April 7, 2026 and must not be treated as an available workflow step.

---

## **Step 3: Write the Prompt**

### **The Goal**

Write a natural, open-ended work request that requires the agent to explore broadly across the universe data. The prompt should be solvable if the agent explores deeply enough, pays attention to detail, and reasons correctly, but we expect the agent should fail on at least some aspects. Design for an average of 40+ necessary calls across 3+ enabled services. Do not inflate volume: every call and service must contribute to the coherent business outcome. See the lower evaluator/QC floors under [Your Goal](#your-goal).

### **Good Prompts vs Bad Prompts**

**GOOD: Simple question, deep investigation required**

*"The Season Pass on Zombie Match keeps throwing weird reward bugs after launch and I can't tell what's actually been fixed vs still open. Can you get to the bottom of it, make sure the right tickets reflect reality, and flag anything that's slipped through so the right engineer picks it up?"*

Why it works: Simple ask, but answering it correctly requires checking Linear ZOM tickets, match3d PRs, `#season-pass`/`#zombie-bugs` Slack, and the reward spec sheet — and the agent has to notice fixed-but-still-open tickets and a minutes-vs-days unit bug. The agent needs to cross-reference data from multiple sources to catch this.

**GOOD: Investigation + action**

*"Something's off between the Singular figures the team recorded and what our own dashboards show for installs — figure out where the gap is and write up what we think is real."*

Why it works: Requires investigation across Singular reconciliation evidence in Slack/Gmail, Snowflake funnel tables, and analytics docs. Singular is a business topic here, not a directly accessible service. Root cause is a ~15–38% user-level gap from pseudo-userid/region issues. Agent must investigate then take write actions (doc, instrumentation ticket).

**GOOD: Open-ended performance review**

*"Where did the Mattel Barbie pitch actually end up, and what's outstanding if they come back? Put together a tight status brief for the founders."*

Why it works: Requires checking `#mattel_proposal`, pitch decks (Slides/Drive), Gmail Mattel thread, and investor-update emails. Agent must synthesize across many data points and produce a write-up.

**BAD: Pre-solved**

*"The Giant Analytics Ticket, ZOM-387, already proves the instrumentation gap. Close it."*

Why it fails: It pre-solves the conclusion and prescribes the action. **Grounding correction:** ZOM-387 is the **Giant Analytics Ticket**, not a Season Pass issue.

**BAD: Command list**

*"Search Linear for ZOM tickets. Check the match3d PRs. Post a summary in #zombie-bugs."*

Why it fails: Tells the agent exactly what steps to take.

**BAD: Bolted-together requests**

*"Check the Mattel pitch status, audit the Snowflake analytics tables, review Calvin's PRs, and look up Arthur's equity docs."*

Why it fails: Four unrelated requests stapled together. Each sub-request should causally flow from the same situation.

**BAD: Not tool-dependent**

*"What's the best strategy for re-engaging lapsed mobile game players?"*

Why it fails: Answerable from general knowledge. Doesn't need HarmonyGames data.

**BAD: Contrived difficulty**

*"Find the Slack message from January 15th at exactly 3:47 PM that mentions a budget of $14,237.89, and cross-reference it with the third comment on Linear issue ENG-417."*

Why it fails: Artificially specific. A real person would never phrase a request this way.

### **Core Rules for Prompt Writing**

* Don't name tools or parameters — say "check what Leonard sent me," not "use gmail\_search\_messages"  
* Don't pre-solve — the agent should investigate and discover  
* Don't include internal IDs unless a real employee would naturally use them — say "the analytics instrumentation backlog," not "issue ZOM-387"  
* Write naturally — like a real person talking to their assistant, not a command list  
* Detailed requirements may live in a referenced Slack message, Drive file, Linear issue, or other realistic company record. This is valid only when that source actually exists in the task's live environment, is uniquely discoverable from the prompt, and is supported by the base universe or task changelog/injection.  
* One coherent situation — every sub-request should flow from the same problem  
* The agent must fail — if it solves everything perfectly, the task isn't hard enough. Iterate.  
* Not contrived — difficulty comes from real data complexity, not artificial constraints  
* "*Leonard sent me this email 3 days ago*" means the email was received February 25, 2026\.  
* "*... and schedule a meeting for next Friday*" is referring to March 6, 2026\.  
* Fixed dates are also valid; just beware anything before February 28, 2026, is in the past, and after it is obviously in the future.

### **Prompt Patterns That Create Difficulty**

**Branching:** The agent makes a decision based on what it finds, then takes different actions depending on the outcome.

"The Season Pass rollout for Zombie Match has been messy and I don't know what state things are in. Check what's actually shipped vs still broken, make sure our tracking reflects reality, and if anything critical has slipped through, get it in front of the right engineer."

**Write tools:** `linear_update_issue`, `slack_send_message`

**Step-by-step dependency:** Figure out A before you can do B, and B before C.

"Before the board call, I need a clean picture of where the Adjoe UA test landed — spend, retention, and why we paused. But first check whether the Singular attribution figures recorded in our internal sources actually match what our dashboards show, because I don't want to brief the board on garbage data. Then put together the summary."

**Write tools:** `gdocs_create_document`, `slack_send_message` (if posting to a channel)

**Stacking:** Multiple related asks unified by a single purpose. Stacking is NOT the same as bolting — stacked asks share a common context, while bolted requests are unrelated.

"I'm meeting the Griffin partners next week and I need to walk in prepared. Get me caught up on where the bridge round stands, what happened with the Mattel pitch, and make sure our internal docs are current. Drop a brief in the founders channel so Arthur and Robert are on the same page."

**Write tools:** `gdocs_create_document`, `slack_send_message`

### **Further Improving Your Prompts**

**Investigation + Action:** The agent must figure something out then do something about it.

*"What's causing the reward bugs in Season Pass? Once you figure it out, update the ticket and brief Brian with what you found."*

**Implicit Requirements:** Things the agent should obviously do that you don't explicitly say.

*"Post the status update in the Season Pass channel."* Implicit: Include the actual bug details, not just "we're looking into it." CC the assignee. Check if the fix PR was actually merged.

**Information Friction:** The answer isn't all in one place.

*"Who dropped the ball on the Collect & Win rollout for Zombie Match?"*

The answer requires connecting: a Linear ticket assigned but never started, a Slack thread where the feature was discussed, a GitHub PR that was merged incomplete, and a Sheets spec that disagrees with what shipped.

**Constraints:** Budget limits, timeline pressure, approval requirements.

*"The CrazyGames WebGL deal depends on getting the build size under their limit, but I'm not sure we're going to make it. Check where Arthur's optimization work stands, whether the sprite-optimization sprint actually landed, and flag anything that could block the deal."*

---

## **Step 3.5: Plan Your Oracle Events**

Before you run the agent, write down the Oracle Events (OEs) — the key steps a correct agent would take to solve your task.

This should be free-form text, not structured JSON. It proves you've thought through the solution path and makes writing rubrics much easier afterward.

OEs are non-authoritative internal plans. Prompt language and live universe evidence define correctness; exact tool feasibility comes from `HarmonyGames_Base_Universe/Tool_Access/*.json`. An OE contradiction is a signal to investigate and correct the OE, not permission to reinterpret the prompt or ground truth. Validate OEs with [`Evals/2_OE_Eval.md`](../Evals/2_OE_Eval.md).

For each important step, note:

* What action needs to happen — post a Slack message, create a Linear issue, update a Trello card, write a Drive doc  
* What information needs to be discovered — what does the agent need to find before it can act?  
* What tools and parameters are needed for each key step

Oracle Events serve two purposes:

1. **Prove solvability** — demonstrate that the task can be solved and that you understand the correct solution path  
2. **Drive rubric writing** — OEs identify which actions exist, and the three-condition test decides which process rubrics to write

**How OEs connect to rubrics:**

**Step 1:** Write all Outcome rubrics first. For every action in your OEs, write 1.1 (action result) \+ 1.2 (content, if specific requirements exist). For every key fact the user asked to be told directly, write 2.1 (final response).

**Step 2:** Review the full rubric set for gaps no Outcome can cover. After writing all Outcomes, ask: is there any requirement — explicit or implicit — that none of my Outcome rubrics can verify? The primary case is ordering between actions (A must happen before B, but both 1.1s pass regardless of sequence). In rare cases, source verification may also qualify — where the correct answer is available in a shallow source and the Outcome genuinely cannot be made specific enough to prove the agent checked the authoritative source. These are your candidates for Process rubrics.

**Step 3:** Apply the three-condition test to each candidate:

* Required by every valid solution path (or phrased broadly enough to allow alternatives).  
* A stricter Outcome rubric cannot capture the same requirement.  
* The rubric describes a behavioral property, not an execution trace.

If any condition fails, tighten the Outcome instead. If all three hold, write a Process rubric. When in doubt, default to Outcome.

**Example:**

If the prompt is: "Post a status update about the Season Pass bugs in the right Slack channel"

Your Oracle Events might look like:

***OE 1:** Search Linear for ZOM Season Pass tickets to find the current bug status.*  
*→ Read/lookup action. The Outcome rubrics for the Slack post already prove this happened — no Process rubric needed.*

***OE 2:** Post a message in `#season-pass` (or `#zombie-bugs`) summarizing the open vs fixed Season Pass reward bugs.*  
*→ Action → goes into Outcome rubrics.*  
*→ Outcome 1.1: "The Agent posts a message in `#season-pass` or `#zombie-bugs` about Season Pass reward bugs."*  
*→ Outcome 1.2: "The Agent distinguishes fixed bugs from open bugs in the Slack message."*

***Process rubrics:** None. The prompt's deliverable is the Slack message. The 1.1 Outcome rubric already verifies it was sent — no ordering constraint exists, and no stricter Outcome is needed.*

**Note**: A single action in your OEs can generate both an Outcome rubric and a Process rubric. For example, if the prompt requires the Agent to check the GDD before updating a Linear ticket, the ticket update gets an Outcome rubric in Step 1 (1.1: "The Agent updates the Linear issue..."), and the ordering requirement gets a Process rubric in Step 2 ("The Agent checks the GDD before updating the ticket") — because the update Outcome alone cannot prove the GDD check came first.

* The rule is not "write actions → Outcome, reads → Process."   
* It is "Outcome first, Process only when no Outcome can verify the requirement" — and that requirement can attach to any action in your OEs, regardless of whether it's a write or a read.

---

## **Step 4: Run the Agent and Iterate**

### **The Workflow**

1. Submit your prompt and the agent runs (expect 30+ minutes)  
2. While the agent runs, start thinking about rubrics based on your Oracle Events (see Rubrics Guidelines)  
3. After the agent finishes, review the trajectory — what did the agent do? What did it miss?  
4. If the agent solved everything perfectly: your task isn't hard enough. Options:  
   * Make the prompt more open-ended so the agent explores more broadly  
   * Add more data to the universe that creates confusion or complexity  
   * Ask for more things in the prompt (stacking)  
   * Introduce conflicting information across services  
5. If the agent failed: Good\! Write rubrics that capture both what it got right and what it got wrong.  
6. Iterate until you have a task where the agent fails on some rubric criteria.

Use the same taxonomy-selected persona for every trial run, final Agent Runner
run, and Run Verifier. Do not count the environment's acting-user configuration
as task work.

*Tip: Use Haiku for quick iteration while designing the task (faster, cheaper).
Use **Claude Opus 4.7 max** for the final 6 runs that determine pass@1.*

### **Difficulty Target**

We run the agent 6 times with **Claude Opus 4.7 max**. Your task is ready to submit when:

* Average 40+ necessary tool calls across 3+ enabled services  
* All 6 fail is fine (pass is 0%)  
* At most 2 runs pass (pass@1 ≤ 40%, proves the task is hard enough)

If all 6 runs pass: the task is too easy. Iterate.

### **Where AIs Might Fail**

* Two entities have similar names and the agent confuses them (e.g., Marcus Lee vs Marcus Bennett)  
* The obvious answer is wrong and the real answer requires deeper digging  
* Information is scattered across many services and the agent doesn't find all of it  
* The agent makes correct observations but draws the wrong conclusion  
* The agent takes some actions correctly but misses others  
* CodeRabbit-only reviews are mistaken for human approval

---

## **Step 5: Write the Rubrics**

See the Rubrics Guidelines for full instructions. Quick summary:

### **Two Conceptual Categories**

* **Outcome** — what the Agent accomplished or reported; mandatory and the default.
* **Process** — necessary behavior an Outcome cannot prove; optional and rare.

### **Core Rule: Outcome First**

* Write all Outcome rubrics first: write actions go into 1.1/1.2, key facts reported to the user go into 2.1. Then add Process only when all three conditions hold: every valid solution path requires the behavior (or the wording allows valid alternatives), no stricter Outcome can capture it, and the criterion describes a behavioral verification rather than an execution trace.  
* Outcome rubrics are the top priority — they are the most reliable training signal  
* No target split is required (❌80% Outcome / 20% Process), but the QC safety
  cap still requires Process to be no more than 40% of the set.  
* If Outcome already covers an explicit ask from the prompt, do NOT write a Process rubric 

### **Outcome Sub-Categories (3, not 5\)**

* **1.1** Write-action results — did the right action happen with the right details? (verified from trajectory)  
* **1.2** Action content — does the content match what was needed? (verified from trajectory parameters)  
* **2.1** Key facts/findings — only when the final response is the deliverable (pure investigation tasks)

**Do NOT write:**

* Grounding checks — not required. Write Outcome rubrics based on what the agent reports and does.  
* Confirmation of actions in the final response — if 1.1 passes, the action happened. No separate confirmation needed.

### **Other Rubric Rules**

* **Stored JSON uses four fields:** `title`, `category`, `justification`, and `evidence`. `title` stores the criterion text; there is no separate stored `criterion` key.
* **Conceptually**, the criterion is the yes/no acceptance statement contained
  in `title`. It alone must be self-contained. Use `Outcome 1.1`, `Outcome 1.2`,
  `Outcome 2.1`, or `Process` in `category`; `justification` and `evidence`
  support review but cannot supply missing acceptance facts.
* Phrase every criterion affirmatively and agent-centrically: “The Agent posts…,” “The Agent identifies…,” or “The Agent confines production activity to inspection….” Do not use prohibition-only wording such as “The Agent does not…,” and do not name tools in criteria.
* Scoring: A run passes only if ALL rubrics pass (any single rubric failure \= run failure). Target: pass@1 ≤ 40%.  
* Every rubric must be: specific, self-contained, objective, verifiable from the trajectory  
* Subjective language is banned in rubric criteria ("enough," "professional," "thorough," "helpful," "good")

[`Docs/2_Rubrics_Guidelines.md`](2_Rubrics_Guidelines.md) is the canonical authoring guide; [`Evals/3_Rubrics_Eval.md`](../Evals/3_Rubrics_Eval.md) is the evaluation authority.

---

## **Step 6: Verify Before Submitting**

* Global existence only: Universe Explorer proves that every referenced fact exists globally; it does not prove persona reachability  
* Persona-readable: Every required Gmail, Slack, GCal, and Contacts fact is proven reachable in the taxonomy-selected persona's Agent/Verifier view
* Persona consistent: Agent Runner and Run Verifiers use the same exact roster persona and email; the AMV dropdown was not used
* Authoring target: Task is designed for 40+ necessary average calls across 3+ enabled services  
* Evaluation floors understood: Prompt requires >15 calls and 2+ services; trajectory QC requires >=15 average calls and 2+ services  
* Tool-dependent: Cannot be answered from general knowledge alone  
* No tool names: Prompt doesn't mention MCP tools or parameter names  
* No pre-solving: Prompt doesn't tell the agent the answer  
* No internal IDs: No database IDs unless a real person would know them  
* Natural language: Reads like a real person, not a command list  
* Not bolted: Every request causally connects to the same situation  
* Not contrived: Difficulty comes from real data complexity, not artificial constraints  
* Agent fails: The agent does NOT pass all rubric criteria on at least one run  
* Universe edits consistent: Any changes you made are consistent with existing data  
* Rubrics written: Outcome first — write actions covered by 1.1/1.2 and requested final-response facts by 2.1; Process added only after the full three-condition test.
* ACL assumptions sound: No prompt, OE, rubric, or call count treats acting-user setup as Agent work or assumes ACL write-side enforcement

---

## **Common Mistakes**

**Mistake 1: Agent Solves It Perfectly** If the agent passes all rubric criteria, the task is too easy. Add complexity to the universe, make the prompt more open-ended, or ask for more things.

**Mistake 2: Command Lists Instead of Tasks** "Search Linear. Check GitHub. Post in Slack." — This is a script. State the goal: "The Season Pass is a mess. Figure out what's still broken and get it in front of the right people."

**Mistake 3: Data Doesn't Exist** You write about a Linear ticket that isn't in the universe, or reference a PR that doesn't exist. Always verify in the explorer.

**Mistake 4: Contrived Difficulty** Adding weird formatting constraints, demanding exact numerical precision, or creating unrealistic scenarios to trick the model. Difficulty should come from the natural complexity of the business situation.

Examples of contrived (BAD):

* "Respond in exactly 3 sentences using only passive voice" — format constraint, not business complexity  
* "Find the Slack message from January 15th at 3:47 PM" — unrealistic precision, no real person remembers exact timestamps  
* "Intentionally post an incorrect status update so we can test the error handling" — asking the agent to do something a real employee wouldn't do

Examples of natural difficulty (GOOD):

* Two UA managers named Marcus (Marcus Lee vs Marcus Bennett) causing a mix-up in attribution data  
* A stalled prototype (Zombie Match Lite) whose status requires connecting a Slack decision, a GitHub branch, a Linear ticket, and a Trello card  
* A cost question whose root cause requires connecting a Slack vendor discussion, a Gmail invoice, internally recorded Singular figures, and Snowflake funnel data

**Mistake 5: Bolted-Together Requests** Four unrelated tasks crammed together. Every sub-request should flow from the same situation.

**Mistake 6: Pre-Solved** "The reward table has a unit bug — fix it" — tells the agent the answer. Say instead: "The Season Pass rewards seem off. Figure out why."

**Mistake 7: Too Short / Too Simple** "Update the ticket" — too terse. Real work requests come with context (what's happening), constraints (urgency, who needs to know), and multiple asks (update the ticket, brief the team, flag anything else).
