# Onboarding Webinar Guide — Harmony Games Universe

## 1. Understand the business

Harmony Games is a small, founder-led mobile game studio focused on casual puzzle games.

- Founded in 2023 and raised a $3M seed round.
- Main games: **Domino Delights** and **Zombie Match 3D**.
- Other experiments include **Combo Fighter**, **Zombie Match Lite**, a **Mattel/Barbie pitch**, and a **4X crypto concept**.
- By February 2026, the company is facing a failed bridge round, reduced runway, and wind-down.

### Main business functions

1. Engineering & Live-Ops
2. Product & Design
3. Growth, User Acquisition & Marketing
4. Founders, Executive & Strategy
5. Finance, Legal, HR & Operations
6. Analytics & Data

## 2. Understand the personas and ACL

The selected persona controls the identity and data the agent can read. Use only the 17 ACL personas and their exact configured emails. Assign the persona whose role best matches the task.

### Business and leadership

- **Leonard Hayes** — business strategy, fundraising, runway, partnerships and wind-down
- **Arthur Blake** — technology strategy, engineering architecture, board and equity
- **Robert** — game strategy, creative direction, economy and difficulty
- **Frederick Stone** — user acquisition, marketing, vendors and distribution

### Product and design

- **Julia Lawson** — product management, GDDs, prototypes and feature scoping
- **Claire Morgan** — art direction and art assets
- **Marcus Bennett** — character art, VFX and marketing creative
- **Samuel Turner** — game design, UI and internal tools
- **Martin Walsh** — UI/UX, live-ops event design and store assets

### Engineering and live-ops

- **Brian Foster** — live-ops features and difficulty tuning
- **Vincent Parker** — QA, game systems, economy and live-bug triage
- **Victor Barnes** — engineering persona with strong art/animation storyline involvement
- **Douglas** — backend, analytics pipelines and player compensation
- **Owen Baker** — Unity, data infrastructure and live-ops delivery
- **Oliver Brooks** — senior Unity engineering, Season Pass and prototypes
- **Calvin Price** — Unity/VFX, Daily Login and support integration

### Analytics

- **Simon Walker** — analytics, retention, attribution and data reconciliation

> Example: assign **Leonard Hayes** to a business or fundraising task, **Brian Foster** to a live-ops task, and **Simon Walker** to an analytics task.

## 3. Explore the datasets for complex prompt areas

The strongest prompts require evidence from several systems. A decision may start in Slack, become a Linear issue, ship through GitHub, and be documented in Drive, Gmail, Trello, Confluence or Snowflake.

Good complex areas include:

- **Feature truth:** compare the design document, ticket status, code merge and team discussion to determine what actually shipped.
- **Live-ops and economy:** investigate Season Pass, Collect & Win, Win Streak, Leaderboards, offers or Daily Login across both games.
- **Fundraising and runway:** reconstruct the seed round, failed bridge round, founder loans, investor updates and wind-down.
- **Growth and vendors:** evaluate AppLovin, Adjoe, Node Media or PlayableX using emails, campaign discussions, roadmap records and performance data.
- **Analytics gaps:** reconcile internal player data with attribution reports and identify instrumentation or pipeline issues.
- **Prototype decisions:** explain why Mattel/Barbie, Zombie Match Lite, 4X Crypto, Telegram or Combo Fighter progressed, stalled or ended.
- **Legal and operations:** trace the patent matter, contractor payroll, hiring, equity, vendor contracts or Helpshift termination.

### Prompt-design rule

Choose the business function first, assign the matching ACL persona, and then build a cross-system question with a clear outcome. Confirm that all required evidence is visible to that persona; inaccessible data cannot be required.

## 4. Build a strong prompt

Use this simple formula:

**Context + Read Asks + Write Asks**

- **Context:** Explain the business situation, why it matters and what is uncertain.
- **Read asks:** State what the agent must discover or reconcile, without prescribing search steps.
- **Write asks:** Define the required end state—what must be created or updated, for whom and by when.

Keep the prompt conversational. The service plan belongs in the author's notes, not as a command list in the prompt.

### Quality checks

- **Feasibility:** Every fact exists, every action is supported and required scoped data is visible to the assigned persona.
- **Truthfulness:** Verify all names, relationships, dates, amounts and identifiers in the live universe.
- **Unique ground truth:** Reasonable readers must reach the same findings and final actions. Clarify recipients, date, time zone, duration and destination when they affect the result.
- **Business function and persona:** Classify the work first, then assign an exact ACL persona whose role naturally owns it.
- **Complexity:** Aim for 40+ necessary calls across 3+ services. The hard floor is more than 15 calls, 2+ services, information friction and multiple meaningful writes.
- **Naturalness:** Avoid tool names, step-by-step instructions, pre-solved conclusions and unrelated bolt-on requests.

### Review of the accounting example

The example has useful context, a read ask and a write ask, but it is not valid for Harmony Games as written:

- Gmail can read and organize mail, but it **cannot send, reply, compose or draft** an email.
- “Accounting lead” and “finance lead” are ambiguous and must resolve to verified contacts.
- Harmony Games has no selectable Finance persona or CFO. Use **Leonard Hayes** or **Arthur Blake** for suitable finance-level work.
- “Yesterday” resolves to **February 27, 2026** and “tomorrow” to **March 1, 2026**, a Sunday. The email and meeting context must exist and make business sense on those dates.
- The 5 PM meeting needs a clear time zone and duration.
- Rohan, the accounting email and every recipient must be verified in the selected persona's visible data.
- Reading one email and creating one meeting is likely too easy for the required complexity.
- The service plan should be: Gmail read, Contacts read, Calendar write, plus a supported surface such as a Drive brief or Slack update. “Contact” should not be listed twice.

### Harmony Games version

> We're closing out Helpshift, and I don't want unpaid invoices or an unfinished migration to become a loose end. Please confirm what we still owe, whether both games have actually moved off it, and reconcile that with our internal tracking. Put the confirmed state, open items and owners in a short closeout brief, then schedule a 30-minute review with Arthur and Frederick for Monday, March 2 at 5:00 PM Central and include the brief in the event.

**Suggested assignment:** Finance, Legal, HR & Operations · **Leonard Hayes**

**Why it works:** One coherent business outcome drives investigation across external correspondence, internal discussion, implementation history and tracking records, followed by two clear writes: a durable brief and a calendar event.

## 5. Oracle Events

Oracle Events describe the critical tool-use steps a correct agent would take to produce the full response. They are internal planning notes that help prove solvability and guide rubric writing; they are **not ground truth**.

Each OE should include:

1. The affirmative action: search, read, create, update or post.
2. The exact available tool and important parameters.
3. The expected observable result.
4. Any dependency on an earlier discovery or runtime-created ID.

### Important rules

- **Complete:** Cover the full critical path, including required discovery, dependencies and every write action.
- **Accurate:** Verify every tool, parameter, entity, date, count and expected result against the catalogs and live universe.
- There is **no fixed number or read/write ratio**. “10 OEs: 4 reads + 6 writes” is valid only if the prompt genuinely requires those exact steps.
- Every OE must represent a real tool-use event. Pure reasoning, final-response wording, prohibitions and no-ops are not OEs.
- `set_acting_user` is environment configuration, not an OE or counted call.
- Scoped reads must be reachable by the assigned persona.
- OEs cannot override the prompt, universe, tool catalogs, trajectory or rubrics.

### Grading

OEs are graded on two dimensions:

- **OE Completeness — 5:** The complete affirmative critical path and all required writes are covered. Missing steps receive 3–4.
- **OE Accuracy — 5:** Tools, services, parameters and expected results are fully correct and observable. Wrong or imprecise details receive 3–4.

An OE-only issue is normally **Non-Fail**, but it must be corrected because it can produce inaccurate rubrics and grading.

### OE-to-rubric mapping

- Each write-action OE → **Outcome 1.1** for the action, plus **Outcome 1.2** when specific content is required.
- Each fact the user asks to receive → **Outcome 2.1**.
- A read OE becomes a **Process** rubric only when every valid path requires it, no stronger Outcome can verify it and the criterion describes verification rather than a tool trace. Most read OEs need no Process rubric.

### Review of the Rohan examples

> “Search Contacts for Rohan and get his email address.”

This is only a valid OE if `contacts_search_contacts` with query `Rohan` returns the intended contact for the assigned persona. The current base Contacts data does not contain Rohan, so this expected result is inaccurate unless the task injects and verifies that contact. A Gmail thread may provide an address, but that requires a different OE and evidence path.

> “The model should give the summary (XYZ content) of Rohan's accounting email.”

This is not a complete OE. The email-reading OE must identify the correct Gmail search/read action and the exact expected facts found in the verified thread. If the user requests the summary in the final response, grade its individual facts with atomic **Outcome 2.1** rubrics. If the summary is written into a document, message or event, add write-action and action-content Outcomes.
