# Long-Horizon Task Guidelines

> **Only read this document if you are assigned to attempt or review a long-horizon task.**  
> A task is classified as **long-horizon when at least one agent run uses 500–1,000 tool calls**. Long-horizon tasks are expected to be a minority of the workload (roughly 20%). For ordinary tasks, follow the standard project and rubric guidelines instead.
>
> **All examples in this guide are for reference only. Never copy or reuse them in a task; create original scenarios, prompts, and deliverables grounded in the assigned environment.**

## Purpose

A long-horizon task requires sustained, accurate work across a large number of records or several connected systems. Its length must come from a realistic business need and the structure of the available evidence—not from artificial instructions designed only to increase the tool-call count.

Start with the [`Docs/README.md`](README.md) reading path. This specialist guide
supplements:

- [`1_Project_Instructions_Overall.md`](1_Project_Instructions_Overall.md)
- [`2_Rubrics_Guidelines.md`](2_Rubrics_Guidelines.md)
- The [HarmonyGames universe guides](../HarmonyGames_Base_Universe/) and
  reference sheet
- The ordered [`Evals/`](../Evals/) and
  [`Guide/How_To_Use_This_Eval.md`](../Guide/How_To_Use_This_Eval.md)

The normal rules still apply: prompts must sound natural, all requested work must form one coherent situation, the task must be grounded in the environment, and rubrics must be outcome-first.

[`HarmonyGames_Base_Universe/6_Server_Tools_Details.json`](../HarmonyGames_Base_Universe/6_Server_Tools_Details.json) is authoritative for every enabled service, exact operation, parameter, pagination control, and batch capability. A long-horizon design must use only those documented capabilities; examples in this guide do not imply additional tools.

Persona ACL is active. Read [`14_Persona_ACL.md`](14_Persona_ACL.md) and bind
the task to the exact key/email in
[`4_Persona_ACL_Roster.json`](../HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json).
Gmail, Slack, GCal, GDrive, GDocs, GSheets, and GSlides reads are
persona-scoped; Contacts, GitHub, Snowflake, Trello, Linear, and Confluence
reads remain unscoped. Writes are outside ACL scope.

For task facts, the live task state and its injection/changelog take precedence
over the base export. For scoring, the current Evals and scored QC
specifications take precedence over this supplement and historical task
examples.

## Canonical Worked Example

Every pattern in this guide is illustrated end to end by one worked example, developed inline through the sections below: a February 28, 2026 source-control preservation pack in which Leonard Hayes asks for every open and closed pull request in two repositories to be captured as a spreadsheet Register plus a Markdown memo. It exercises prompt naturalness, environment injection, `BATCH` Oracle Events, runtime bindings, and large-audit-table rubric coverage.

The walkthrough that follows covers, in order: where its 592 tool calls come from, how the repetition is expressed as `BATCH` Oracle Events with runtime bindings, and how 116 records are graded with 79 outcome-first criteria rather than one rubric per row.

> **Reuse the structure, never the content.** Do not copy this example's scenario, cohort, repositories, evidence surfaces, flag vocabulary, column set, or totals — those belong to it alone. What transfers is the shape: a source-defined cohort, separately exposed evidence surfaces, operating rules discovered in the environment, and totals reconciled against a saved artifact.

### Where the 592 Calls Come From

| Segment | Calls |
|---------|-------|
| Locate and read the instruction thread, the wind-down decision, and the Drive checklist | 4 |
| Enumerate both repository cohorts (37 and 79 pull requests) | 2 |
| Create the Register spreadsheet | 1 |
| Record-level evidence: 116 pull requests × 5 separately exposed GitHub surfaces | 580 |
| Write the Register, read it back, create the memo, and verify it | 5 |
| **Total** | **592** |

The 580 record-level calls are the task. The other twelve are the discovery, creation, and verification that turn a retrieval loop into a deliverable. No call in the list can be removed without changing the correctness, completeness, or verifiability of the result.

### How the Repetition Is Expressed in Oracle Events

Writing 580 near-identical Oracle Events would be unreadable. The exemplar instead writes one `BATCH` OE per repository-and-surface pair, each stating the fixed arguments, the varied key, the expected coverage, and how empty results are represented:

> OE 008 — BATCH github_get_pull_request_reviews fixed({"owner":"harmonygames-Games","repo":"Combo-Fighters"}); vary pullNumber over each integer 1..37. Expected: retrieve the individual submitted review decisions once for every pull request in harmonygames-Games/Combo-Fighters, preserving empty results as checked absence. […] exact value: 37 distinct PR keys; NONE FOUND=27; populated=10 […] Calls: 37.

Artifacts that only receive identifiers at runtime are referenced by binding rather than by an invented ID:

> OE 018 — gsheets_values_update({"range":"Register!A1:P117","spreadsheetId":"BIND[OE007.spreadsheetId]", …

Every OE carries its own `Calls:` count and the file closes with `FINAL EXACT MINIMUM CALL TOTAL: 592`, so a reviewer can check the arithmetic without reconstructing a trajectory.

### How 116 Records Are Graded Without 116 Rubrics

`7_Rubrics.json` grades a 116-row register with 79 criteria. It reaches complete coverage through five devices rather than row-by-row expansion:

- **Exact cohort multisets.** "The Agent records the Combo-Fighters PR-number multiset as every integer from 1 through 37 exactly once" rejects missing, duplicate, and extra keys in one independently verifiable claim.
- **Whole-column accuracy.** "The Agent records the exact source-grounded first SHA in every Commit summary" grades all 116 values of a single field as one atomic claim.
- **Aggregate invariants.** Each of the five provenance flags gets an exact row count — 30, 105, 78, 21, and 22 — which only reconciles if every record-level classification is right.
- **Atomic spot checks.** One row is pinned by name: dominoes PR #79 must read exactly `MULTI_COMMIT_WITHOUT_APPROVAL`. There is no required number of these.
- **Exclusions.** Leonard limited totals to per-repository and combined, so two criteria confirm the memo carries no state-level or contributor-level breakdown.

Every non-repetitive requirement — tab name, cutoff, memo links, source anchors, handoff facts — still gets its own direct rubric. The exception compresses repetition, not coverage.

### Explicit Spot-Check Rule for Large Redundant Audits

Do **not** create one rubric for every repeated row, record, or field. For
example, a 166-PR audit does not need 166 rubrics for each audited field.
Instead, combine:

- an exact cohort or artifact-row-total criterion;
- exact reconciliation controls such as key multisets, whole-column accuracy,
  and aggregate invariants; and
- source-grounded atomic spot checks for selected PRs.

There is **no required minimum number of spot checks**, either overall or per
group/component. Choose enough grounded checks to make the task objectively
reviewable without recreating the full audit as hundreds of rubrics. Oracle
Events and intended execution must still cover the complete cohort, and every
non-repetitive requirement still needs direct rubric coverage.

Do not replace this policy with an “at least N records are correct” rubric.
`At least N` usually packs independent pass/fail items into one threshold and
is non-atomic. Tightly coupled facts from one source record may remain bundled
when they necessarily pass or fail together; the same applies to shared
content across repeated destinations when discovery of that content determines
all instances together.

## What Qualifies as Long-Horizon

The operational definition is exact: **at least one run must contain 500–1,000 tool calls**. Within that range, the work should arise from many necessary, dependent retrievals, reconciliations, or writes. Common patterns include:

- Auditing every member of a large, source-defined cohort.
- Checking several distinct evidence surfaces for every record.
- Reconciling records across services when no authoritative bulk view contains the answer.
- Producing a large register whose totals and classifications depend on record-level evidence.
- Completing a broad closeout or handoff where omissions would make the deliverable unreliable.

Meeting the 500–1,000-call threshold establishes the classification, but it does not by itself establish task quality. Repeatedly opening the same record, splitting one useful query into many smaller queries, or adding arbitrary checkpoints solely to reach the threshold is artificial inflation.

ACL-denied reads, repeated retries against inaccessible records, and automatic
`set_acting_user` environment configuration do not count toward the threshold.
The high call count must come from reachable, necessary Agent work.

### Practical Design Pattern: Record × Evidence-Surface Matrix

The most reliable way to design legitimate long-horizon work is to identify a large, source-defined cohort and require several distinct, necessary evidence surfaces to be checked for every cohort member:

`number of records × separate evidence surfaces per record = core record-level calls`

For example, 116 pull requests requiring five individually exposed GitHub evidence checks naturally produce 580 core calls — the arithmetic worked through in [Canonical Worked Example](#canonical-worked-example). The governing constraint is that a cohort listing or summary cannot substitute for record-level verification when it does not contain the requested evidence.

The same pattern can apply to incident closeouts, vendor wind-downs, access handoffs, release audits, customer escalations, or contract reconciliations. In each case, every surface must be separately exposed by the available tools and must materially affect the requested deliverable. If one bulk call contains the complete evidence, require the bulk call instead.

> **DO NOT COPY THESE EXAMPLES EXACTLY. Do not reuse their wording, numbers, cohorts, evidence-surface combinations, or deliverable structure. They are reference patterns only. Every task must be original and grounded in its assigned environment.**

## Keep the Prompt Natural

Long-horizon tasks fail quality checks when the prompt reads like a spec sheet. The agent should receive a realistic work request; the detailed operating rules, field definitions, checkpoint mechanics, and classification vocabulary should live in the environment whenever possible.

**Unnatural prompts** over-specify:

- Exact channel names, file paths, and internal artifact titles.
- Column-by-column spreadsheet schemas.
- Process choreography (“save 20 rows at a time,” “six checkpoint slots,” “re-open each range before the next block”).
- Full policy text that employees would already have recorded elsewhere.
- Verification scripts embedded in the user message.

**Natural prompts** state:

- The business situation and urgency.
- What outcome is needed and by when.
- Which source anchors to follow (“the wind-down decision,” “the task list on my Drive”).
- The deliverables in plain language (spreadsheet + memo).
- Enough constraints to grade the result, without walking the agent through every step.

The natural version should still produce the same long-horizon work. The complexity comes from the data and the deliverable, not from the prompt acting as an operations manual.

### Worked Example: Source-Code / IP Provenance Closeout

The same underlying task — 116 pull requests, five evidence surfaces, a Register and a memo — can be requested three ways. All three demand the same 580 record-level evidence calls; they differ only in how much of the reasoning the user does on the agent's behalf. Only the third version is natural enough to ship; it appears as Tier 3 below.

#### Tier 1 — Unnatural: the prompt as a runbook

**Do not write prompts like this:**

> We’re freezing the priority source-control evidence for the wind-down. Pick up the existing internal closeout trail, the #executives decision that the company needs to wind down and the shared Drive checklist Task List.xlsx under Wind Down, so this stays tied to our actual closeout record. I need a founder-level source-code and IP provenance pack as it stood on February 28, 2026, covering every open and closed pull request in harmonygames-Games/Combo-Fighters and harmonygames-Games/game-of-dominoes-backend. The verified cohort sizes belong in the completed pack rather than being assumed up front.
>
> This is preservation work rather than a code-quality review, and Arthur retains the technical judgment. For every pull request, preserve five separate evidence surfaces: its commit chain; submitted review decisions; inline discussion attached to the diff; the general pull-request conversation; and lifecycle history, including assignments, labels, review requests, closes, and merges where present. Silence carries no approval weight. An empty surface should appear as NONE FOUND. A pull request is complete only after all five surfaces have been opened from that pull request’s individual record; repository listings establish the cohort but cannot substitute for those individual checks.
>
> The data-room handoff has six reserved checkpoint slots: two for Combo-Fighters and four for game-of-dominoes-backend. Divide each listed repository cohort across its slots in PR-number order, with contiguous, non-overlapping blocks, in a spreadsheet titled “Priority Source-Code/IP Provenance Register, 2026-02-28” with a Register tab. Each saved checkpoint needs its repository-and-PR keys confirmed after it lands and before another block is added; this keeps completed preservation work recoverable.
>
> The completed Register should have exactly one row per pull request and these sixteen columns: Repository, PR number, Source link, Title, State, Author, Created at, Merged at, Commit summary, Review summary, Inline discussion summary, General conversation summary, Lifecycle summary, Provenance flags, Evidence status, and Cutoff. Keep summaries compact while retaining counts and useful boundaries: first and last SHA for commits; states and authors for reviews; authors and paths for inline discussion; authors for general conversation; and event types plus first and last timestamps for lifecycle history.
>
> Use only these provenance flags: NO_SUBMITTED_REVIEW, NO_INLINE_REVIEW_DISCUSSION, NO_GENERAL_CONVERSATION, NO_REVIEW_REQUEST_EVENT, and MULTI_COMMIT_WITHOUT_APPROVAL. Leave the flag cell as NONE when none applies. Treat each flag as a preservation gap, not a conclusion about code quality or the people involved.
>
> Create a companion document titled “Priority Source-Code/IP Preservation Memo, 2026-02-28.” Anchor it to both existing wind-down records, link the register, state each repository total and the overall total, report the total for each of the five flags, and explain that these are preservation gaps rather than code-quality conclusions. The handoff is ready only when the six checkpoint ranges and the full completed Register have all been read back. Send me both usable links, the verified register row count, and confirmation that all six saved checkpoints were verified.

Why it fails: it names internal systems, prescribes checkpoint slots, lists every column, repeats flag definitions, and reads like a QA script—not something Leonard would actually send an assistant.

#### Tier 2 — Better, but still a specification

**Closer, yet still over-specified:**

> We’re getting close to handing over the last company access, and I don’t want the source-control history to become a loose end. Build a February 28, 2026 closeout pack for every open and closed pull request in harmonygames-Games/Combo-Fighters and harmonygames-Games/game-of-dominoes-backend. Use the wind-down decision and the task list on my Drive as the source anchors, and work out the cohort totals from the repository records.
>
> This is preservation work, not a code review; Arthur still owns the technical judgment. For each PR, track the commit chain, submitted reviews, inline diff discussion, lifecycle history, and general PR conversation. If something is missing, use NONE FOUND. Where a surface has multiple records, roll them into one concise block with counts and the dates, contributors, states, or file context that will help someone follow the history.
>
> Share the results in a spreadsheet with a Register tab: one row per PR, grouped by repository and PR number, with enough source metadata to find the PR again. Keep the five evidence summaries separate, include a completion marker and the cutoff, and only mark a row complete when all five checks are covered.
>
> These are our standard flags for record gaps: NO_SUBMITTED_REVIEW, NO_INLINE_REVIEW_DISCUSSION, NO_GENERAL_CONVERSATION, NO_REVIEW_REQUEST_EVENT, and MULTI_COMMIT_WITHOUT_APPROVAL. Use them only for record gaps, and use NONE when none applies. For the multi-commit flag, treat an APPROVED review anywhere in the PR record as approval.
>
> Also send a short TL;DR memo as a Markdown file. It should tie back to the relevant wind-down message and Drive task list, link the Register, summarize the repository and flag totals, and give someone enough context to understand what we’re preserving and why. Once you’re done, send me the spreadsheet and memo with the verified Register row count.

Why it still falls short: it sounds like a well-written ticket rather than a message. It restates the flag vocabulary, the completion rule, the approval convention, and the Register layout — all things this team would already have agreed somewhere. Every sentence a founder has to write about his own internal conventions is a sentence that should have been discoverable in the environment.

#### Tier 3 — What actually shipped

The delivered prompt is four sentences:

> can you get the source handoff pack Arthur and I talked about over the line? the details are in #source-handoff. use his preservation notes and my totals note for the February 28 snapshot, then send me the finished pack and checked PR count. this is record keeping, not a code review

Everything the two earlier tiers spelled out lives in an injected private Slack channel, `#source-handoff`, where Leonard and Arthur work the requirements out between themselves. Abridged from `Prompt_and_Injected_Conversation.md`:

> **Leonard:** can we make sure the source handoff and source control history dont become a loose end
>
> **Arthur:** you mean all open and closed prs in Combo-Fighters and game-of-dominoes-backend?
>
> **Leonard:** yes, snapshot it as of February 28. I want one spreadsheet with a Register tab, one row per pr grouped by repo and pr number
>
> **Arthur:** ok. for every pr we should keep commits, submitted reviews, inline diff comments, general pr conversation and lifecycle history separate
>
> **Arthur:** if one has nothing put NONE FOUND so we know it was checked. if there are multiple records roll them up with the count […]
>
> **Arthur:** undated lifecycle stuff still counts but shouldnt set the dates. only mark complete after all 5 have a result
>
> **Arthur:** for gaps use NO_SUBMITTED_REVIEW, NO_INLINE_REVIEW_DISCUSSION, NO_GENERAL_CONVERSATION, NO_REVIEW_REQUEST_EVENT and MULTI_COMMIT_WITHOUT_APPROVAL. use NONE if nothing applies
>
> **Leonard:** for totals I just need Combo-Fighters, dominoes backend and both combined. not by state or contributor

Why it works: the agent must read Slack before it can even name the repositories, and it still performs the identical 580 record-level evidence calls. The prompt sounds like a founder chasing a loose end, because that is all it is.

#### What Moved from the Prompt to the Environment

| Detail | Tier 1 and 2 | Shipped task |
|--------|--------------|--------------|
| Which repositories, and the open-and-closed scope | Prompt | Arthur's reply in the thread |
| The February 28 cutoff | Prompt | Leonard's message in the thread |
| The five evidence surfaces to preserve | Prompt | Arthur's preservation notes |
| `NONE FOUND` and the roll-up conventions | Prompt | Arthur's preservation notes |
| The five-flag closed vocabulary | Prompt | Arthur's preservation notes |
| The `MULTI_COMMIT_WITHOUT_APPROVAL` approval rule | Prompt | Arthur's preservation notes |
| "Complete" means all five surfaces have a result | Prompt | Arthur's preservation notes |
| Register tab, one row per PR, grouped by repo and number | Prompt | Leonard's spreadsheet message |
| Which totals to report — and which to leave out | Prompt | Leonard's totals note |
| Preservation framing, not a code review | Prompt | Both, deliberately |
| What Leonard wants handed back | Prompt | Prompt |

Only the last two rows stay in the prompt. The framing stays because it sets the agent's posture; the hand-back stays because it is what the user is actually asking for.

### Generalizing the Pattern

The same compression applies to any long-horizon scenario. Once the conventions live in the environment, a prompt can shrink to something like:

> Can you prep the handoff spreadsheet John asked for? Follow Jane's recommendations from the meeting notes, include a blurb I can send via Slack, and drop a summary `.md` file when you're done.

That still requires hundreds of tool calls, because the agent must find John's request, read Jane's recommendations, discover the vocabulary and deliverable shape from those sources, and then execute the full cohort audit. The call count comes from investigation and record-level work, not from repeating instructions in the prompt.

## Environment Injection

**Most of the detail in an unnatural long-horizon prompt should live in the environment, not in the user message.**

“Injection” means adding a small amount of **synthetic task context** to that task’s **unique environment**. It does **not** mean prompt injection or adversarial instruction hijacking.

### Why Inject Instead of Over-Specifying the Prompt?

Long prompts become unnatural when they contain every policy, flag definition, column schema, and process constraint. In a real company, those details already exist somewhere:

- A Slack thread where the team agreed on preservation flags.
- Meeting notes with Jane’s register recommendations.
- A Drive checklist or policy doc for wind-down closeouts.
- A Linear comment or Confluence page defining evidence standards.

Put them there. The prompt becomes a short, realistic delegation; the agent discovers the rules by reading the environment—adding legitimate retrieval calls without turning the prompt into a command list.

### What to Inject vs What to Keep in the Prompt

| Belongs in the environment | Can stay in the prompt |
|----------------------------|------------------------|
| Flag definitions and approval rules | Business situation and deadline |
| Column schemas and naming conventions | Repositories or cohort scope |
| “Follow Jane’s recommendations” source content | Deliverable types (spreadsheet, memo) |
| Prior requests (“John asked for this last night”) | High-level evidence areas to preserve |
| Team conventions (`NONE FOUND`, completion rules) | Source anchors in plain language |
| Register formatting standards | Request to verify row count at handoff |

**Example:** Instead of pasting this into the prompt:

> Use these preservation-gap flags so the roll-up stays consistent: NO_SUBMITTED_REVIEW, NO_INLINE_REVIEW_DISCUSSION, NO_GENERAL_CONVERSATION, NO_REVIEW_REQUEST_EVENT, and MULTI_COMMIT_WITHOUT_APPROVAL. Use NONE when no flag applies. Apply MULTI_COMMIT_WITHOUT_APPROVAL when a pull request has more than one commit and no submitted review anywhere in its record has state APPROVED; later commits do not cancel that approval. Treat the flags as record gaps, not judgments about the code or people involved.

**Inject** a realistic Slack exchange—for example, Arthur or Jane posting the team’s standard flag list and rules in `#engineering-bots` or a wind-down thread. The prompt then says:

> Use our standard flags for record gaps—check the thread where we defined them.

The agent must read Slack to learn the vocabulary. That adds tool calls **and** keeps the prompt natural.

### Injection Rules

- **Task-isolated:** Each task has its own environment copy. Synthetic additions affect only that task, not other contributors’ universes or the shared base export.
- **Small and plausible:** The OBI spec allows a limited amount of synthetic content. Keep injected records realistic and proportionate.
- **Discoverable, not prescriptive:** Seed policies, requests, and constraints—not the final register contents or pre-computed totals.
- **Cross-service consistent:** If Slack references `Task List.xlsx` or a specific PR, that record must exist (or be intentionally seeded) in Drive/GitHub.
- **Persona-reachable:** Required Gmail, Slack, GCal, or Drive-family (GDrive/GDocs/GSheets/GSlides) records must
  be visible to the exact assigned persona unless the intended outcome is an
  affirmative denial finding plus reporting, escalation, or an authorized
  alternative. Universe Explorer author god-mode and local exports prove global
  existence only.
- **Documented in ground truth:** Record every injected row in
  `9_Universe_inject.sql` and `4_Changelog.json`. Include injected facts in
  Oracle Events and rubrics only when they are needed for the authorized
  solution path or acceptance criteria.
- **No adversarial hidden instructions:** Injection supports realistic work discovery; it must not trick the model.

A compliant injection for this example is small — one private channel, one thread, fourteen messages, each recorded as an individual row in the task's own `9_Universe_inject.sql` and `4_Changelog.json`. Nothing in that injection contains a register row, a flag total, or a cohort size; it seeds only the rules the agent must discover.

### Synthetic Data Is Acceptable

Injected Slack messages, meeting notes, or checklist rows are synthetic additions to a task-specific environment. That is expected and allowed in small amounts. Reviewers grade against ground truth derived from the full environment (real + injected), not against whether every byte predated the task.

## Correct GitHub Example: Necessary Work, Not Inflation

Consider this realistic request:

> Prepare a source-code provenance register for every open and closed pull request in two repositories. For each PR, preserve its commit chain, submitted reviews, inline diff discussion, general PR conversation, and lifecycle history.

The repository listings establish the cohort: 37 PRs in `Combo-Fighters` and 79 in `game-of-dominoes-backend`, for 116 PRs total. The five requested evidence surfaces are separate GitHub records:

1. Commit chain
2. Submitted review decisions
3. Inline review comments attached to the diff
4. General PR conversation
5. Lifecycle or timeline events

If the available GitHub interface exposes those surfaces only per PR, then the core work naturally requires:

`116 PRs × 5 distinct evidence checks = 580 record-level calls`

Those calls are justified because each one answers a different required question for a specific cohort member. A repository PR listing cannot prove that an individual PR has no submitted review, no inline discussion, or a particular lifecycle event. An empty result is also evidence, but only after that surface has actually been checked.

This remains non-inflated when:

- The cohort comes from the repository records rather than a number inserted to force volume.
- Every requested surface materially affects the output.
- Each PR is checked once per required surface.
- Listing, pagination, artifact creation, and final verification add only the calls genuinely needed.
- The output preserves a checked absence distinctly from an unchecked field.

### Artificially Inflated Version

The same task becomes artificial if it requires the agent to:

- Open every PR three times without a business reason.
- Search separately for each commit when one PR-commit call returns the complete chain.
- Save after every row solely to increase write calls.
- Re-read arbitrary ranges that do not protect against a realistic failure mode.
- Check files, statuses, or branches that do not affect any requested finding.
- Target a specific call count instead of a complete business outcome.

The test is simple: if removing a call cannot change the correctness, completeness, recoverability, or verification of the requested deliverable, that call probably should not be required.

## Other Valid Long-Horizon Examples

### Portfolio Closeout

A founder asks for a wind-down register covering all active products, vendor obligations, source archives, operating evidence, and unresolved owners. The work may require Slack decisions, Drive agreements, GitHub status, Linear ownership, Trello roadmap records, and Snowflake evidence. This is valid when every source contributes to one closeout decision and the final register reconciles the findings.

It is not valid to attach unrelated requests—such as an employee review, a marketing analysis, and a code audit—merely to use more services.

### Invoice and Contract Reconciliation

A finance or operations handoff may require matching every vendor invoice to its contract, approval trail, payment evidence, termination status, and current account owner. Many calls are justified when records are distributed across Gmail, Drive, Slack, and an internal tracker and each vendor needs a defensible disposition.

The task should not request one search per dollar amount when a single source query can retrieve the complete invoice set.

### Release or Incident Evidence Register

A release owner may ask for every incident in a defined period to be matched against alerts, tickets, fixes, deployment records, and customer communications. Record-level checks are justified if each surface is separate and the output must distinguish fully resolved, partially evidenced, and missing records.

### Large Data-Room or Access Handoff

A wind-down or acquisition handoff can legitimately require a complete inventory of repositories, Drive artifacts, vendor accounts, owners, access-removal evidence, and unresolved legal or technical dependencies. The complexity is coherent because every action supports the same handoff.

## Guidance for Attempters

### 1. Translate the Request into Completion Conditions

Before beginning repetitive retrieval, identify:

- The authoritative cohort and how it will be enumerated.
- The evidence surfaces required for each cohort member.
- Which scoped-service records are visible to the exact assigned persona,
  including mailbox ownership, Slack conversation visibility, calendar
  ownership/sharing/invites, and Contacts visibility.
- The classifications, flags, or calculations that depend on those surfaces.
- The requested artifacts and their required structure.
- The final counts, links, and confirmations needed for handoff.

Do not assume cohort sizes from the prompt, a prior memo, or a partial search
result when the authoritative source can establish them.

Membership-aware planning is mandatory. Establish persona-visible search
anchors before launching a batch, and use an authorized unscoped source when it
is part of the intended task. If the task intentionally expects an access
denial, record the denial once and proceed to the required report, escalation,
or authorized alternative; repeated denied retries are not progress.

### 2. Build a Deterministic Work Plan

Use a stable order such as repository then PR number, vendor name, issue key, or date. Track a compact ledger containing:

- Record key
- Required surfaces
- Checked or not checked state
- Retrieved result, including an explicit empty result
- Derived classification
- Saved artifact range or destination

“NONE FOUND” and “NOT CHECKED” are different states. Never convert an unfinished lookup into an absence claim.

### 3. Respect Source Boundaries

In HarmonyGames:

- Slack is the primary decision record.
- Linear is the work record.
- GitHub is the code and PR record.
- Drive, Docs, Sheets, and Slides hold design, financial, legal, and presentation records.
- Gmail is external evidence and is read/triage-only.
- Snowflake is analytical evidence and is read-only.
- Trello and Confluence may contain roadmap and durable operating context.

These are source roles, not ACL rules. Gmail, Slack, GCal, and the Drive-family (Drive, Docs, Sheets, Slides) reads
are persona-scoped. Contacts, GitHub, Snowflake, Trello,
Linear, and Confluence reads remain unscoped, and Persona ACL does not grant or
deny writes.

The local
[`HarmonyGames_Base_Universe/Services_Data/`](../HarmonyGames_Base_Universe/Services_Data/)
checkout contains the full base export. High-volume surfaces use two actual
layouts:

- **Full service-level JSON files**, including
  `linear/linear.issues.json`, `github/github.pull_requests.json`,
  `github/github.reviews.json`, and `gdrive/gdrive.drive_files.json`.
- **Sharded full payloads**, including
  `slack/messages/<channel-or-DM-id>/<YYYY-MM>.json` and
  `gmail/threads/<owner-or-service>_EMAIL_<thread-id>.json`.

`Base_Universe_Complete_Data.json` is the combined base export. The checkout
does not use a legacy `Data/` directory or `__sample30` files.

Full base data is not the same as the live task state. Task-specific injection
or changelog records may add or modify facts, and a service can render,
paginate, or omit fields differently from raw JSON. Use the local full/sharded
data for exhaustive base grounding, cohort planning, Oracle Event authoring,
and offline validation; use the live task state and actual service responses to
verify injected facts and what the exact assigned Agent persona can observe.

Be careful with redacted identities and CodeRabbit-only reviews. A bot review or silence must not be upgraded into human approval unless the task’s governing evidence explicitly supports that conclusion.

### 4. Work in Recoverable Units

Long sessions can fail after substantial progress. Save durable output in sensible blocks when the destination supports incremental writes. A useful checkpoint:

- Contains complete records rather than partial evidence surfaces.
- Has stable keys that can be read back.
- Is large enough to avoid excessive overhead.
- Is small enough that retrying it after a failure is affordable.

The exact block size should follow the tool and artifact limits. Do not mechanically use 20 rows, 50 rows, or any other number unless it is appropriate for that task.

After a write, verify the keys and dimensions needed to prove it landed correctly. Do not repeatedly re-read data that has no realistic risk of loss or corruption.

### 5. Preserve Runtime Dependencies

Created artifacts receive identifiers only at runtime. Create each destination once, retain its returned ID or URL, and use that same value for later writes and verification. In Oracle Events, represent this dependency with a binding such as `BIND[OE005.spreadsheetId]` rather than inventing a future ID.

For large repeated retrievals, Oracle Events may describe a parameterized `BATCH` over the complete source-defined key set. The batch description must identify the fixed arguments, varied key, expected coverage, and empty-result behavior. `BATCH` documents legitimate repetition; it must not conceal an unknown cohort or an inflated loop. Both notations are shown in use under [How the Repetition Is Expressed in Oracle Events](#how-the-repetition-is-expressed-in-oracle-events).

### 6. Reconcile Before Handoff

At minimum, check:

- Source cohort total equals artifact record total.
- Every source key appears exactly once.
- No repository, page, range, or final remainder was skipped.
- Every required evidence surface has a checked result.
- Derived flags follow their stated rules.
- Per-group totals sum to the overall total.
- Artifact titles, tabs, links, columns, and cutoff dates are correct.
- Created records can be reopened.

For spreadsheets, read back the completed range or use an equivalent complete verification. For documents, reopen the saved document and confirm its links and rollups.

### 7. Hand Back the Outcome Clearly

Report the usable artifact links, verified row or record counts, important limitations, and any required confirmation of completed verification. Do not bury an incomplete cohort, failed write, or unresolved mismatch behind a confident summary.

## Guidance for Reviewers

Review the business logic before counting calls.

### Confirm the Task Is Legitimately Long-Horizon

- Is the request realistic for the persona and company situation?
- Does the prompt sound natural, or does it read like a spec sheet / command list?
- Are detailed rules in the environment where employees would have recorded them?
- Does the environment contain the referenced source trail?
- Is there one coherent outcome?
- Does each repeated lookup contribute necessary evidence?
- Is every required scoped read reachable to the assigned persona, or is the
  designed outcome an affirmative denial plus reporting, escalation, or an
  authorized alternative?
- Is the task difficult because of real scale or reconciliation rather than arbitrary process constraints?
- Could a bulk call validly replace hundreds of record-level calls? If so, require the efficient route.
- Conversely, does a bulk listing omit the evidence the prompt actually asks to preserve? If so, record-level calls are justified.

### Confirm the Ground Truth Is Complete

- Derive cohort sizes from authoritative records.
- Account for pagination and cutoff dates.
- Verify empty surfaces as carefully as populated ones.
- Check exact flag or classification totals.
- Confirm synthetic environment additions are internally consistent.
- Make Oracle Events sufficient to prove solvability without forcing one invalidly narrow execution trace.

### Review Outcomes First

Follow the normal rubric guidelines:

- Cover created or updated artifacts with Outcome 1.1 and relevant content with Outcome 1.2.
- Use Outcome 2.1 for facts the user asked to receive directly.
- Add Process rubrics only when a necessary behavior cannot be verified by a stricter outcome.
- Do not write a rubric for every expected tool call.
- Do not reward a model merely for producing a high call count.

For a large register, assess completeness through source-defined keys, exact totals, required columns, classification rules, and verified artifact contents. The deliverable—not the length of the trajectory—is the primary result. See [How 116 Records Are Graded Without 116 Rubrics](#how-116-records-are-graded-without-116-rubrics) for what that looks like in practice.

For repetitive row-level checks, use the
[explicit spot-check rule](#explicit-spot-check-rule-for-large-redundant-audits):
exact cohort/row controls plus selected grounded spot checks, with no mandatory
minimum count. Do not create one rubric per record-field cell.

## Common Failure Modes

- Starting record-level work before establishing the complete cohort.
- Missing a second page or the final partial group.
- Treating a repository listing as proof that detailed PR surfaces were checked.
- Confusing inline review comments with general PR conversation.
- Treating an empty review result, bot comment, or silence as approval.
- Losing undated lifecycle events while calculating dated boundaries.
- Marking rows complete when one required surface was never opened.
- Writing the entire artifact only at the end and losing all recoverable progress.
- Saving many tiny checkpoints that add overhead without reducing material risk.
- Constructing one oversized write that exceeds practical tool or context limits.
- Repeating searches after the relevant record has already been identified.
- Counting ACL-denied calls or repeated denied retries toward long-horizon
  scale.
- Treating Explorer/local-export visibility as proof of assigned-persona
  reachability.
- Allowing context drift to change field names, flag rules, cutoff dates, or ordering midway through the task.
- Reporting totals that were not reconciled against the final saved artifact.
- Injecting synthetic facts that conflict with the existing universe.
- Exposing task ground truth directly in the prompt instead of requiring discovery.
- Writing an over-specified prompt with checkpoint slots, exact column lists, or process choreography that belongs in the environment.
- Leaving flag definitions, schemas, or team conventions only in the prompt when they should be discoverable in Slack, Drive, or meeting notes.
- Creating hundreds of redundant row-level rubrics instead of using exact
  cohort/reconciliation controls plus selected atomic spot checks.
- Using an `at least N` threshold to bundle independently pass/fail records.

## Final Checklist

### Attempter

- [ ] I established the source-defined cohort and pagination.
- [ ] I bound the exact roster persona and planned scoped searches around
      membership/visibility.
- [ ] I identified every required evidence surface and completion rule.
- [ ] I used a deterministic order and tracked progress.
- [ ] I kept checked absence separate from unchecked work.
- [ ] I saved progress in sensible, recoverable units.
- [ ] I did not add calls that cannot affect correctness or recoverability.
- [ ] I excluded denied reads, denied retries, and environment identity setup
      from the necessary call count.
- [ ] I reconciled source keys, artifact rows, classifications, and totals.
- [ ] I reopened and verified the final artifacts.
- [ ] I returned usable links, exact counts, and honest limitations.

### Reviewer

- [ ] The scenario is realistic, coherent, and grounded in the environment.
- [ ] The prompt is natural; detailed rules live in the environment where appropriate.
- [ ] The high call count follows from necessary work rather than inflation.
- [ ] Scoped evidence is reachable to the exact assigned persona, with no
      Explorer-only feasibility assumption.
- [ ] Any injected context is limited, plausible, isolated, and documented.
- [ ] The Oracle Events cover the complete ground truth.
- [ ] Bulk and record-level retrieval choices match the available evidence surfaces.
- [ ] Rubrics evaluate outcomes and do not reward call count or one arbitrary procedure.
- [ ] The expected artifacts, totals, and verification conditions are objectively checkable.

