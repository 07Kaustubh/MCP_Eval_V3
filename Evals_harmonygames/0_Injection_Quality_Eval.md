# INJECTION QUALITY EVALUATOR — Original Conference (HarmonyGames)

> **Purpose:** Verify that universe edits (injections) are structurally sound, realistic, consistent across services, and create genuine difficulty for AI agents. **Hard-gate eval** — any single structural defect prevents progression. Runs AFTER injection but BEFORE prompt/OE/rubric authoring.

---

## Overview

When a CB edits the HarmonyGames universe (injects records into Slack messages, Gmail threads, Linear issues, Google Sheets, GitHub PRs, etc.), those edits must pass structural, temporal, cross-service, and realism checks before the task proceeds. A broken injection poisons everything downstream — rubrics will reference phantom data, agents will hit dead ends, and QC will flag the task.

This eval consolidates all injection validation into 7 hard gates plus a difficulty/complexity scoring phase. Every injected or modified record is checked individually. The eval produces a binary PASS/FAIL verdict (all gates must pass) plus a composite difficulty score (minimum 2.5 to proceed).

**Fixed universe date:** February 28, 2026 (America/Chicago)
**Active workflow window:** 2026-01-01 to 2026-02-28
**Services:** Slack, Linear, GitHub, Gmail, GDrive, GDocs, GSheets, GSlides, GCal, Trello, Contacts

`HarmonyGames_Base_Universe/6_Server_Tools_Details.json` is the sole authority for tool capabilities. Gmail can search/read messages and threads, read attachments, modify labels, archive threads, trash/untrash/delete messages or threads, and create/delete labels, but it has no send, reply, compose, or draft tool.

`HarmonyGames_Base_Universe/Data/` is the current full base checkout, not a sampled subset. Nine services consolidate into one `data.json` keyed by table; Gmail and Slack are split into per-object files plus shard directories; GDrive, GitHub, Linear, and Trello add a `root/` blob tree. Combine it with task injection/changelog records and live service reads to establish task-specific state and tool-visible behavior.

**`Data/` is the tool-visible view, not a table dump — never validate columns against it.** Its payloads carry the shape the MCP tools return, which is deliberately not the database shape: `linear` issues carry `labels`, `relations`, and `uuid`; `trello` cards carry `idLabels` and `badges`; `gsheets` nests the entire `sheets_sheets` table inside `sheets_spreadsheets[].sheets`. Its keys are also short names (`issues`, `actions`, `calendars`), not table names (`linear_issues`, `trello_actions`, `gcal_calendars`), except in gdocs/gsheets/gslides where they already match. `HarmonyGames_Base_Universe/7_Universe_Schema.json` is the sole authority for column names, types, and NOT NULL constraints in Phase 1. Use `Data/` only to confirm the BEFORE state, ID conventions, and tool-visible rendering.

Dropping the service prefix resolves 38 of the 44 tables that `data.json` backs. The six that do not resolve that way are listed below; a table being unresolvable here is a property of the export, never grounds for a SCHEMA_VIOLATION.

| Table | Where its data actually is |
|---|---|
| `github_pr_comments` | key is `pull_request_comments`, not `pr_comments` |
| `github_releases`, `github_tags` | absent from the export — no rows |
| `sheets_sheets` | nested inside `sheets_spreadsheets[].sheets` |
| `slides_pages`, `slides_page_elements` | nested under presentations; `slides_presentations` is itself empty |

**Persona ACL feasibility is a STRONG HARD GATE.** Apply
`Docs/14_Persona_ACL.md` (derive the scoped-service set live from its Access
matrix; do not hardcode it); `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json`
defines the exact persona records. Before scoped reachability checks,
`2_Persona.txt` must match one roster entry exactly on Persona Key, Persona
Email, Name, Role, and Department. Any required record in a scoped service that
the assigned Agent Runner persona cannot reach — with no intentional-denial
outcome and no authorized unscoped alternate — is a **standalone FAIL** for this
eval; it cannot be waived or offset by structural/realism strength, and Universe
Explorer author god-mode never satisfies it.

---

## STEP 0 — Mandatory TODO List (Hard Gate)

**Create and track this COMPLETE checklist. Every item is mandatory. Mark each as you go.**

```
- [ ] Phase 0: Load & Pre-Read
  - [ ] 0.1: Read 9_Universe_inject.sql (PRIMARY — the injection SQL) + 4_Changelog.json (if exists) + 3_UniverseDataForThisTask.json (if populated) + HarmonyGames_Base_Universe/Data/ (always for base comparison) — catalog every injected/modified record
  - [ ] 0.2: Read 4_Changelog.json — extract the CB's change manifest
  - [ ] 0.3: Read HarmonyGames_Base_Universe/7_Universe_Schema.json — load column names, types, NOT NULLs, FKs. This is the ONLY column authority for Phase 1
  - [ ] 0.4: Read every JSON file in HarmonyGames_Base_Universe/6_Server_Tools_Details.json (combined tool catalog) — build the authoritative tool, parameter, and capability inventory for reachability
  - [ ] 0.5: Read base data for each affected service in HarmonyGames_Base_Universe/Data/ — open `<service>/data.json` and select the table's key (strip the service prefix: `linear_issues` → `issues`, `gcal_calendars` → `calendars`; gdocs/gsheets/gslides keys already match). Gmail and Slack are per-object files plus shard directories instead. Treat what you find as the BEFORE state and tool-visible shape only, not as the column list
  - [ ] 0.6: Read 5_Prompt.txt (if available) — understand what scenario the injection supports
  - [ ] 0.7: Build inventory: list every injected record (table, ID, operation: insert/update/delete)
  - [ ] 0.8: If the task is long-horizon, read Docs/13_Long_Horizon_Task_Guidelines.md and apply its injection, discoverability, and anti-inflation rules
  - [ ] 0.9: Read 2_Persona.txt + HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json; require Persona Key, Persona Email, Name, Role, and Department to match one roster entry exactly
  - [ ] 0.10: Read Docs/14_Persona_ACL.md; only after the five-field roster match, bind the assigned taxonomy persona for scoped reachability checks

- [ ] Phase 1: Schema & Structural Validation
  - [ ] 1.1: For EACH injected record, verify all columns match the table's schema
  - [ ] 1.2: For EACH injected record, verify column data types (string/number/boolean/array)
  - [ ] 1.3: For EACH injected record, verify all NOT NULL columns are populated
  - [ ] 1.4: For EACH foreign key field, verify the referenced record exists
  - [ ] 1.5: For EACH enum/select field, verify the value is in the allowed set
  - [ ] 1.6: Record verdict per record: VALID / SCHEMA_VIOLATION

- [ ] Phase 2: ID Format & Convention
  - [ ] 2.1: Sample 3+ existing IDs from the same table to establish the pattern
  - [ ] 2.2: For EACH injected ID, verify it follows the established pattern
  - [ ] 2.3: For EACH injected ID, verify uniqueness (no collision with base universe)
  - [ ] 2.4: For Slack ts fields, verify they resolve to valid dates in 2026-01-01 to 2026-02-28
  - [ ] 2.5: For Gmail message IDs, verify format matches existing messages
  - [ ] 2.6: Record verdict per record: VALID / ID_VIOLATION

- [ ] Phase 3: Date & Time Consistency
  - [ ] 3.1: For EACH injected timestamp, verify it falls within 2026-01-01 to 2026-02-28
  - [ ] 3.2: For Slack/Gmail business comms, verify timestamps land on weekdays (Mon-Fri)
  - [ ] 3.3: For Slack reply chains, verify chronological ordering (parent ts < child ts)
  - [ ] 3.4: For Gmail threads, verify sent_at < received_at and thread ordering is coherent
  - [ ] 3.5: For GCal events, verify start < end and times are within the workflow window
  - [ ] 3.6: Check business-hour plausibility (06:00-22:00 CT for routine comms)
  - [ ] 3.7: Record verdict per record: VALID / TEMPORAL_VIOLATION

- [ ] Phase 4: Base Universe Integrity & Cross-Service Consistency (MOST CRITICAL)
  - [ ] 4.1: DIFF injected data against base universe — identify every record that was added, modified, or deleted
  - [ ] 4.2: For EACH modified base record: does the change contradict any OTHER existing base record?
  - [ ] 4.3: For EACH injected record: does it collide with (duplicate) any existing base record? (same ID, same entity key)
  - [ ] 4.4: For EACH injected record: does it contradict established facts in the base universe? (e.g., injecting a "project cancelled" email when base Linear shows active tickets)
  - [ ] 4.5: For EACH injected record referencing existing entities: are names, IDs, statuses, amounts consistent with base data?
  - [ ] 4.6: Check for timeline collisions — does injected data create impossible timelines with existing events? (e.g., injecting a meeting at the same time as an existing calendar event)
  - [ ] 4.7: Check for status/state contradictions — does injection change an entity's state in one service but leave it unchanged in another? (e.g., marking a ticket "resolved" in Linear but not updating the corresponding Trello card)
  - [ ] 4.8: Extract all entities (people, companies, properties, tickets) that appear in 2+ services (base + injected combined)
  - [ ] 4.9: For EACH cross-service entity, verify name spelling, email format, and status are identical across ALL appearances
  - [ ] 4.10: For EACH cross-service reference (Slack → Linear ticket, email → GSheets budget entry), verify target exists in base OR injected data
  - [ ] 4.11: Record verdict: CONSISTENT / COLLISION / CONTRADICTION / CROSS_SERVICE_VIOLATION

- [ ] Phase 5: Naturalness & Anti-AI-Tell
  - [ ] 5.1: Read EVERY injected text field (Slack messages, email bodies, comments, notes)
  - [ ] 5.2: Check for overly formal language in casual channels (e.g., #eng-general)
  - [ ] 5.3: Check for perfect grammar where abbreviations/casual tone are expected
  - [ ] 5.4: Check for generic corporate phrases ("circle back", "per our earlier discussion")
  - [ ] 5.5: Check for unnaturally long messages for the medium
  - [ ] 5.6: Check for repeated syntactic structures across injected messages
  - [ ] 5.7: Check for emoji usage in injected messages — real business comms don't use them
  - [ ] 5.8: Count AI-tell instances — 3+ = FAIL
  - [ ] 5.9: Record verdict: NATURAL / AI_TELL_DETECTED

- [ ] Phase 6: Phantom & Reachability Check
  - [ ] 6.1: For EACH injected record, identify the MCP tool(s) that can surface it
  - [ ] 6.2: For EACH injected record, trace a tool call chain (max 5 calls) from prompt context to record
  - [ ] 6.3: Verify injected records are indexed by an exact available discovery tool (for example, gmail_search_messages, linear_list_issues, or slack_conversations_search_messages)
  - [ ] 6.4: Check for orphaned records — data that exists but no tool path leads to it
  - [ ] 6.5: For every required record in a persona-scoped service (derive the scoped set live from the `Docs/14_Persona_ACL.md` Access matrix — do not hardcode it), verify reachability as the assigned persona using the visibility test appropriate to that service type: mailbox ownership for mail; membership or implemented public visibility for chat; ownership, share, or invitation for calendars; file ownership or share for a Drive-family service (Drive-family inherits Drive's file ACL, and a known object ID does not bypass it)
  - [ ] 6.6: Treat required evidence visible only to another persona as ORPHANED unless the intended outcome is access denial or an authorized unscoped alternate source supplies the evidence
  - [ ] 6.7: Keep Universe Explorer author god-mode separate from Agent Runner reachability
  - [ ] 6.8: Record verdict per record: REACHABLE / ORPHANED / PHANTOM

- [ ] Phase 7: Pre-Solve & Information Leakage Check
  - [ ] 7.1: Check for smoking-gun records (single record that states the conclusion)
  - [ ] 7.2: Check whether task is solvable in 1-2 tool calls (trivially discoverable)
  - [ ] 7.3: Verify critical data is distributed across 2+ services (information friction)
  - [ ] 7.4: Check for decoys/near-matches that create genuine filtering difficulty
  - [ ] 7.5: Record verdict: PROPERLY_OBSCURED / PRE_SOLVED / NO_FRICTION

- [ ] Phase 8: Injection Difficulty & Complexity Scoring
  - [ ] 8.1: Score each of the 7 difficulty dimensions (1-5)
  - [ ] 8.2: Compute composite score (average)
  - [ ] 8.3: Map to rating band (Too Easy / Medium / Hard / Very Hard)
  - [ ] 8.4: If composite < 2.5, flag for injection rework

- [ ] Phase 9: Final Verdict
  - [ ] 9.1: Fill in gate results for all 7 structural checks
  - [ ] 9.2: Record difficulty score and rating
  - [ ] 9.3: Produce final verdict (PASS only if all 7 gates pass AND difficulty >= 2.5)
```

---

## Input Files

| File | Purpose |
|---|---|
| `9_Universe_inject.sql` | **PRIMARY INPUT** — the SQL INSERT/UPDATE statements that inject the scenario into the base universe. This is the source of truth for what was changed. |
| `4_Changelog.json` | CB's change manifest (auto-generated from the platform) — what was added, modified, or deleted |
| `3_UniverseDataForThisTask.json` | Task-specific universe snapshot (may be empty if CB did not export). Combine it with the full/sharded base checkout in `HarmonyGames_Base_Universe/Data/`, `4_Changelog.json`, `9_Universe_inject.sql` when present, and live service reads. |
| `HarmonyGames_Base_Universe/Data/` | Current full base export for comparison — the BEFORE state, not a sample. One `data.json` keyed by table per service (for example, `HarmonyGames_Base_Universe/Data/linear/data.json` → `issues`), with Gmail and Slack split per object and GDrive/GitHub/Linear/Trello carrying a `root/` blob tree. Tool-shaped, so it is evidence of the BEFORE state and of tool-visible rendering — never a column authority |
| `HarmonyGames_Base_Universe/7_Universe_Schema.json` | **Sole column authority** — all 57 tables with column names, types, NOT NULLs, defaults. Validate every injected column against this, never against `Data/` |
| `HarmonyGames_Base_Universe/6_Server_Tools_Details.json` | **Authoritative MCP tool inventory** — Read the combined catalog for exact service availability, tool names, parameters, and reachability/discovery support |
| `2_Persona.txt` | **Required persona artifact** — Persona Key, Persona Email, Name, Role, and Department must exactly match one roster entry before scoped reachability checks |
| `Docs/14_Persona_ACL.md` | **Authoritative persona ACL semantics** — scoped read services, visibility rules, runner/verifier identity parity, and author god-mode separation |
| `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json` | **Authoritative identity roster** — exact taxonomy Persona Key, Persona Email, Name, Role, and Department values |
| `5_Prompt.txt` | The prompt (if written already) — for reachability chain tracing |
| `Docs/13_Long_Horizon_Task_Guidelines.md` | Conditional reference for tasks with a 500–1,000-call run |

---

## Task-Context Injection Rules

A small task-specific Slack message, meeting note, checklist, or policy record may supply detailed requirements that would sound unnatural in the prompt. This is valid only when all of the following hold:

1. **Prompt-directed:** The prompt directs the Agent to follow the source rather than merely mentioning a related record.
2. **Actually present:** The record exists in the task's live environment and is supported by either the base universe or the task changelog/injection. Local text that is absent from the live environment does not count.
3. **Uniquely discoverable:** The prompt provides a natural anchor from which one source can be found with available tools. A vague reference that matches several records is not sufficient.
4. **Plausible and isolated:** The addition belongs in that service, affects only the assigned task environment, and does not conflict with existing records.
5. **Instructional, not precomputed:** The record may define policy, schema, flags, or prior requests, but must not contain final findings, computed totals, or ready-to-submit deliverables.
6. **Grounded and task-relevant:** Ground truth identifies the injected source and the task-relevant obligations it establishes. Oracle Events may point reviewers to that source, but they are non-authoritative planning notes and cannot create or override obligations. Do not create rubrics for incidental facts merely because they appear in the injected record.

When local exports and the live environment disagree, treat the live environment as authoritative and flag the injection/export mismatch.

**Reference injection:** `Docs/13_Long_Horizon_Task_Guidelines.md` walks through the canonical example of rules-in-the-environment injection for a long-horizon task. The injection is one private Slack channel and a fourteen-message thread — nothing else — with every row recorded in both `9_Universe_inject.sql` and `4_Changelog.json`. Its "Tier 3 — What actually shipped" section shows the payoff: because the repositories, cutoff, evidence surfaces, flag vocabulary, and totals scope all live in that thread, the prompt shrinks to four sentences and the agent has to read Slack before it can start. Check that the injection seeds only rules and prior requests — the reference contains no register row, no flag total, and no cohort size, which is what keeps it instructional rather than precomputed.

---

## Phase 1: Schema & Structural Validation (HARD GATE)

**For EVERY injected or modified record, verify schema compliance.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Unknown column | Injected record has a column not in the table's schema | `linear_issues` record has `priority_level` but schema only has `priority` | **SCHEMA_VIOLATION** |
| Wrong type | Column value doesn't match the schema's declared type | `amount` field contains string `"$3,200"` but schema declares `number` | **SCHEMA_VIOLATION** |
| Missing NOT NULL | A required column is null or absent | `slack_messages` record missing `channel_id` (NOT NULL in schema) | **SCHEMA_VIOLATION** |
| Broken FK | Foreign key points to a record that doesn't exist | `channel_id: "C999"` but no channel with that ID in `slack_channels` | **SCHEMA_VIOLATION** |
| Invalid enum | Select/enum field uses a value outside the allowed set | `status: "pending_review"` but allowed values are `["open", "in_progress", "closed"]` | **SCHEMA_VIOLATION** |
| Extra nested fields | JSON object fields that don't match the expected structure | `attendees` array contains objects missing required `email` field | **SCHEMA_VIOLATION** |

**Any SCHEMA_VIOLATION → FAIL. No exceptions.**

**Resolve every check in this phase against `7_Universe_Schema.json`.** A field
present in `Data/<service>/data.json` is not evidence that a column exists — the
export is tool-shaped and carries denormalized extras (`labels`, `relations`,
`idLabels`, `badges`, nested `sheets`). Equally, a schema column absent from the
export is not an unknown column. Both mistakes are live failure modes: the first
passes an INSERT that will not execute, the second fails a valid injection.

---

## Phase 2: ID Format & Convention (HARD GATE)

**Injected IDs must be indistinguishable from existing universe IDs.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Pattern mismatch | Injected ID doesn't follow the table's existing convention | Existing Linear issues: `LIN-1234`; injected: `ISSUE-5678` | **ID_VIOLATION** |
| Duplicate ID | Injected ID collides with an existing record | Injected `slack_message` with `ts: "1719504000.000100"` already exists in base | **ID_VIOLATION** |
| Slack ts invalid | Slack `ts` doesn't resolve to a date within 2026-01-01 to 2026-02-28 | `ts: "1609459200.000001"` → resolves to 2021-01-01 | **ID_VIOLATION** |
| Gmail ID format | Message ID doesn't match existing format | Existing: `msg_001`, `msg_002`; injected: `email-new-1` | **ID_VIOLATION** |
| Sequential gap | Injected ID creates an obvious gap in existing numbering | Existing invoices: `INV-0001` through `INV-0089`; injected: `INV-0500` | **ID_VIOLATION** |

**Procedure (mandatory):**
1. For each affected table, sample at least 3 existing IDs to establish the pattern. Sample from `Data/<service>/data.json` under the table's key; IDs are identical in the tool view and the database, so the export is a valid source here.
2. Compare every injected ID against that pattern.
3. Grep every injected ID against the base universe to confirm no duplicates.

**Any ID_VIOLATION → FAIL.**

---

## Phase 3: Date & Time Consistency (HARD GATE)

**All injected timestamps must be within the active workflow window (2026-01-01 to 2026-02-28, America/Chicago) and chronologically coherent.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Outside window | Timestamp before January 1 or after February 28, 2026 | Email `sent_at: "2026-03-15T10:00:00Z"` — after the universe cutoff | **TEMPORAL_VIOLATION** |
| Weekend business comm | Slack message or email timestamped on Saturday/Sunday | Slack DM in #eng-general at `2026-02-14T09:30:00` (Saturday) | **TEMPORAL_VIOLATION** |
| Reply before parent | Child message timestamp precedes parent | Parent `ts: 1772064000` (Feb 26); reply `ts: 1771977600` (Feb 25) | **TEMPORAL_VIOLATION** |
| sent_at > received_at | Email sent timestamp after received timestamp | `sent_at: "2026-02-20T14:00:00Z"`, `received_at: "2026-02-20T13:55:00Z"` | **TEMPORAL_VIOLATION** |
| Event time illogical | Calendar event start >= end, or outside workflow window | Meeting `start: "2026-02-25T15:00"`, `end: "2026-02-25T14:00"` | **TEMPORAL_VIOLATION** |
| Implausible hour | Routine business comm at 3:00 AM on a weekday | Slack message in #eng-general at `2026-02-18T03:15:00-05:00` | Flag (soft) |

**Any TEMPORAL_VIOLATION → FAIL.**

---

## Phase 4: Base Universe Integrity & Cross-Service Consistency (HARD GATE — MOST CRITICAL)

**This is the most important phase. Injections MUST NOT contradict, collide with, or break the integrity of existing base universe data.**

### 4A: Injection vs Base Universe Integrity

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Record collision | Injected record has same ID or key as an existing base record | Injecting a contact with `contact_id: "cnt_042"` when that ID already exists in base Contacts | **COLLISION** |
| Fact contradiction | Injection contradicts an established fact in the base universe | Base GSheets shows active contract with AppLovin through Sept 2026; injection adds email saying "AppLovin contract terminated last month" | **CONTRADICTION** |
| Status/state conflict | Injection changes entity state in one service but not others | Injecting a Linear ticket status `"Done"` but Trello card still says `"In Progress"` for the same feature | **CONTRADICTION** |
| Timeline collision | Injection creates impossible timeline with existing events | Injecting a sprint planning at 2pm Feb 25 when base Calendar already has an all-day hackathon for the same person | **COLLISION** |
| Amount conflict | Injected financial data contradicts existing records | Base GSheets budget shows design contractor cost = $3,200; injected email says "the $2,800 design invoice" | **CONTRADICTION** |
| Relationship break | Injection changes a relationship established in base data | Base Linear shows engineer assigned to Domino Delights; injection places them on Zombie Match 3D with no reassignment record | **CONTRADICTION** |
| Orphaned update | Injection modifies a record but leaves dependent records stale | Injecting a new assignee on a Linear ticket but not updating the Slack thread where the old assignee was discussed | **CONTRADICTION** |

### 4B: Cross-Service Consistency (injected + base combined)

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Name spelling mismatch | Same person/entity spelled differently across services | Slack: `"Brian Foster"`, Gmail: `"Brian Forster"`, Linear: `"Brian Fosters"` | **CROSS_SERVICE_VIOLATION** |
| Email format mismatch | Different email for the same person across services | Contacts: `m.lopez@harmonygames.co`, Gmail from: `maria.lopez@harmonygames.co` | **CROSS_SERVICE_VIOLATION** |
| Status inconsistency | Entity active in one service, inactive in another | Contacts: `is_active: true`, but Slack messages reference this person as having left the company | **CROSS_SERVICE_VIOLATION** |
| Broken cross-reference | Slack message references a Linear ticket that doesn't exist | Slack: `"see MT-2026-0147 for details"` but no such issue in Linear | **CROSS_SERVICE_VIOLATION** |
| Broken issue ref | Slack message references a Linear issue that doesn't exist | Slack message: `"see LIN-0092 for details"` but no LIN-0092 in Linear issues | **CROSS_SERVICE_VIOLATION** |
| Project data conflict | Same project has different details across services | Linear project: `"Zombie Match 3D — v2.1"`, Trello board: `"Zombie Match 3D v2.0"` | **CROSS_SERVICE_VIOLATION** |

**Procedure (mandatory):**
1. DIFF injected data against base universe — identify every record added, modified, or deleted.
2. For EACH injected/modified record, search ALL services in the base universe for the same entity.
3. Verify no fact, status, amount, relationship, or timeline contradicts existing data.
4. Verify no ID collision with existing records.
5. Verify cross-service consistency for every entity that appears in 2+ services (base + injected combined).

**Any COLLISION, CONTRADICTION, or CROSS_SERVICE_VIOLATION → FAIL.**

---

## Phase 5: Naturalness & Anti-AI-Tell (HARD GATE)

**Injected text fields must sound like real humans wrote them. AI-generated-sounding injections break task realism and get flagged by QC.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Formality mismatch | Overly formal language in casual Slack channels | #eng-general: `"I wanted to formally bring to your attention that the build pipeline for Domino Delights requires immediate attention."` — real eng chat would be: `"Domino Delights build is broken again, can someone take a look?"` | **AI_TELL** |
| Perfect grammar | No abbreviations/typos where casual tone is expected | Slack DM: `"Would you be able to review the build report I have prepared for the Domino Delights release?"` — real DM would use contractions and be shorter | **AI_TELL** |
| Corporate filler | Generic phrases that add no information | `"I wanted to circle back on our earlier discussion regarding the outstanding sprint items."` | **AI_TELL** |
| Message length | Unnaturally long for the medium | 5-paragraph Slack message in a channel where existing messages average 1-2 sentences | **AI_TELL** |
| Repeated structure | Same syntactic pattern across 3+ injected messages | Three messages all follow: `"Hi [name], I wanted to let you know that [situation]. Could you please [action]? Thanks!"` | **AI_TELL** |
| Vocabulary mismatch | Language inconsistent with the persona's role/seniority | QA engineer using: `"synergize our remediation efforts"` | **AI_TELL** |
| Emoji usage | Injected messages contain emojis — real internal business comms in this universe don't use them | `"The build pipeline is fixed! 🎉👍 Let me know if anything else comes up! 😊"` | **AI_TELL** |

**Counting rule:** 3+ injected text fields showing clear AI-generation patterns → FAIL. Isolated instances are flagged but not blocking.

---

## Phase 6: Phantom & Reachability Check (STRONG HARD GATE)

**Every injected record must have an ordinary cataloged discovery path, and every required record in a persona-scoped service (derive the scoped set live from the `Docs/14_Persona_ACL.md` Access matrix — do not hardcode it) must be reachable by the assigned Agent Runner persona, support an intentional denial outcome, or have an authorized unscoped alternate. Orphaned required data creates phantom entity failures downstream.** A scoped-service record intentionally outside the assigned persona's view is not orphaned when the task requires the Agent to affirmatively report or escalate the denial, or to use an authorized unscoped alternate. Universe Explorer author god-mode can inspect all records for authoring and does not prove Agent Runner reachability.

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| No discovery path | Injected record has no tool call chain leading to it | GSheets budget entry exists but no search/list tool returns it when querying by any available filter | **ORPHANED** |
| Search tool blind spot | Record not indexed by the relevant search tool | Injected Slack message in a channel, but `slack_conversations_search_messages` doesn't match its content with any plausible query | **ORPHANED** |
| Wrong mailbox | Required Gmail evidence exists only in another persona's mailbox | Assigned persona cannot read the required thread and no authorized alternate source exists | **ORPHANED** |
| Slack visibility mismatch | Required Slack evidence is outside the assigned persona's channel membership/public visibility as implemented | Author sees a private channel in Universe Explorer, but the assigned runner persona cannot | **ORPHANED** |
| Calendar visibility mismatch | Required GCal evidence is neither owned, shared with, nor invited to the assigned persona | Another persona's private event is the only source of a required scoped-service fact | **ORPHANED** |
| Drive-family visibility mismatch | Required GDrive/GDocs/GSheets/GSlides evidence is neither owned by nor shared with the assigned persona (Drive-family inherits Drive file ACL; a known object ID does not bypass it) | A Sheet or Doc never shared with the persona is the only source of a required scoped-service fact | **ORPHANED** |
| Chain too deep | Discovery requires >5 sequential tool calls from any prompt-referenced starting point | Agent must: list channels → find channel → get messages → find reference → search Linear → get issue → list comments (7 calls minimum, no shortcut) | Flag (soft) |
| Orphaned thread | Injected Gmail thread has no connection to any entity the prompt references | New email thread about a vendor not mentioned in prompt, contacts, or any other service | **PHANTOM** |
| Dead-end reference | Injected record references an entity that itself is unreachable | Slack message says `"see the GSheets row for PlayableX"` but PlayableX has no GSheets records | **PHANTOM** |

**Procedure (mandatory):**
1. Read `2_Persona.txt` and require Persona Key, Persona Email, Name, Role, and
   Department to match all five values of one
   `HarmonyGames_Base_Universe/4_Persona_ACL_Roster.json` entry exactly. A
   missing field, mixed entry, inferred email, or value mismatch fails this
   gate before any scoped reachability check.
2. Bind the assigned taxonomy persona to that exact roster entry and apply
   `Docs/14_Persona_ACL.md`.
3. For each injected record, identify the MCP tool(s) that can return it.
4. For every required read in a persona-scoped service (derive the scoped set
   live from the `Docs/14_Persona_ACL.md` Access matrix — do not hardcode it),
   test the path under the assigned persona's implemented visibility rules. Do
   not invent scoping beyond [`Docs/14_Persona_ACL.md`](../Docs/14_Persona_ACL.md),
   and do not treat a doc-scoped service as unscoped.
5. Trace a call chain (max 5 calls) from a prompt-referenced entity to the record.
6. A scoped record visible only to another persona is not a defect when the task
   intentionally asks the Agent to encounter and affirmatively report/escalate
   the denial, or when an authorized unscoped alternate source supports
   successful completion.
7. Otherwise, if no assigned-persona path exists for a required scoped-service record → the record is orphaned → FAIL.

**Any ORPHANED or PHANTOM record → FAIL.** This is a standalone, non-waivable blocker: one required scoped-service record unreachable by the assigned persona (with no affirmative-denial outcome and no authorized unscoped alternate) fails the eval on its own, regardless of structural, temporal, cross-service, or realism quality.

---

## Phase 7: Pre-Solve & Information Leakage Check (HARD GATE)

**The injection must create genuine difficulty — not hand the agent the answer.**

| Check | What to look for | Audit example | Verdict |
|---|---|---|---|
| Smoking gun | A single record that explicitly states the conclusion | Slack message: `"FYI the $4,200 discrepancy on the ad spend is because AppLovin double-billed us in June"` — agent reads one message and has the full answer | **PRE_SOLVED** |
| Trivial discovery | Task solvable in 1-2 tool calls with no cross-referencing | All relevant data is in Gmail and one `gmail_search_messages` call reveals everything | **PRE_SOLVED** |
| No information friction | The overall task's critical evidence is concentrated in one service | Bug report, root cause, affected feature, and resolution all in one Linear issue with comments — no need to check Slack, Gmail, or GitHub | **NO_FRICTION** |
| No decoys | Zero near-matches or misleading records that could misdirect an agent | Only one invoice from the vendor in question — no similar invoices to confuse with | **NO_FRICTION** |
| Answer in injection | Injected record contains the exact text the agent should produce as output | A GDocs document contains the ready-to-submit summary the agent is supposed to produce | **PRE_SOLVED** |

**PRE_SOLVED → FAIL. NO_FRICTION alone is not a hard fail but feeds into Phase 8 difficulty scoring (will lower the composite).** A context-only injection may legitimately live in one service; judge cross-service friction across the complete task, not the injected policy record by itself.

---

## Phase 8: Injection Difficulty & Complexity Scoring

> **This is NOT a pass/fail gate — it is a quality assessment.** Score the injection to gauge how challenging it will be for AI agents and help the CB strengthen weak tasks.

**Score each dimension 1-5:**

| Dimension | What it measures | 1 (Low) | 3 (Medium) | 5 (High) |
|---|---|---|---|---|
| **Cross-Service Spread** | How many services does the injected scenario touch? | Single service (e.g., only Slack messages) | 3 services (e.g., Slack + Linear + Gmail) | 5+ services (e.g., Slack + Linear + Gmail + GitHub + GSheets) |
| **Information Scattering** | Is critical info distributed or concentrated? | All in one record (e.g., one Linear issue has everything) | Across 2-3 records in different services | Scattered across 5+ records in 3+ services — agent must collect fragments |
| **Trap Density** | Does the injection include decoys or misleading data? | No traps — only the correct data exists | 1-2 decoys (e.g., a similar project name, a nearly-matching budget figure) | 3+ realistic traps (e.g., two contractors with similar names, overlapping Linear tickets, stale vs current PR statuses) |
| **Temporal Complexity** | Does the injection create timeline reasoning demands? | No time dimension — all data is current | Some date reasoning (e.g., distinguish January vs February invoices) | Complex timeline with ordering dependencies (stale vs current status, overlapping events, superseded approvals) |
| **Tool Call Depth** | Minimum tool calls to discover all injected scenario data? | <5 calls (one search surfaces everything) | 10-20 calls across multiple services | 25+ calls required, multi-hop discovery chains |
| **Reasoning Chain** | Does the agent need to connect dots, not just retrieve? | Retrieve and report — answer is in one tool response | Cross-reference 2 sources (e.g., match Slack mention to GSheets budget entry) | Multi-hop reasoning across 3+ sources (e.g., Slack → Linear ticket → GSheets entry → Contacts to identify the responsible vendor) |
| **Write Action Diversity** | How many different write tools would a correct solution need? | One write action (e.g., post one Slack message) | 2-3 writes across services (e.g., Slack post + Linear update + Trello card move) | 4+ writes across 3+ services (e.g., Slack + Linear issue + Trello card + GDoc + GCal event) |

**Composite Score:** Average of all 7 dimensions (round to 1 decimal).

| Composite | Rating | Recommendation |
|---|---|---|
| 1.0–2.0 | **Too Easy** | Injection needs more complexity — add traps, scatter data across services, require multi-hop reasoning |
| 2.1–3.0 | **Medium** | Acceptable but could be stronger — consider adding decoys, temporal reasoning, or additional write targets |
| 3.1–4.0 | **Hard** | Good injection quality — proceed to prompt authoring |
| 4.1–5.0 | **Very Hard** | Excellent injection — high model failure probability expected |

**Minimum threshold: Composite must be >= 2.5 to proceed. Below 2.5 → return to injection phase and strengthen.**

---

## Phase 9: Final Verdict

```
┌─────────────────────────────────────────────────────┐
│           INJECTION QUALITY VERDICT                 │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Schema & Structure:      PASS / FAIL                │
│ ID Format & Convention:  PASS / FAIL                │
│ Date & Time:             PASS / FAIL                │
│ Cross-Service:           PASS / FAIL                │
│ Naturalness:             PASS / FAIL                │
│ Reachability:            PASS / FAIL                │
│ Pre-Solve Check:         PASS / FAIL                │
│                                                     │
│ ─── Difficulty Assessment ───                       │
│ Cross-Service Spread:    ___ / 5                    │
│ Information Scattering:  ___ / 5                    │
│ Trap Density:            ___ / 5                    │
│ Temporal Complexity:     ___ / 5                    │
│ Tool Call Depth:         ___ / 5                    │
│ Reasoning Chain:         ___ / 5                    │
│ Write Action Diversity:  ___ / 5                    │
│                                                     │
│ Difficulty Score:         ___ / 5.0                 │
│ Rating:                  Too Easy / Medium /        │
│                          Hard / Very Hard           │
│                                                     │
│ VERDICT:  PASS / FAIL                               │
│ PASS = all 7 gates pass AND difficulty >= 2.5       │
│ Any single gate failure = FAIL.                     │
│ Difficulty < 2.5 = FAIL (Too Easy).                 │
└─────────────────────────────────────────────────────┘
```

---

## Quick Reference: 15 Common Injection Defects

| # | Defect | Phase | Auto-flag |
|---|---|---|---|
| 1 | Wrong column type in injected record (e.g., string `"$3,200"` in a `number` field) | P1 | SCHEMA_VIOLATION |
| 2 | Duplicate ID with existing record (e.g., injected `ts` already in `slack_messages`) | P2 | ID_VIOLATION |
| 3 | Timestamp outside universe window (before 2026-01-01 or after 2026-02-28) | P3 | TEMPORAL_VIOLATION |
| 4 | Weekend timestamp on business communication (Slack/email on Saturday) | P3 | TEMPORAL_VIOLATION |
| 5 | Reply chain with child before parent (`reply_ts < parent_ts`) | P3 | TEMPORAL_VIOLATION |
| 6 | Name spelled differently across services (`"Maria Lopez"` vs `"Maria Lopes"`) | P4 | CROSS_SERVICE_VIOLATION |
| 7 | Cross-service reference to non-existent record (Slack cites `MT-2026-0147` but Linear has no such issue) | P4 | CROSS_SERVICE_VIOLATION |
| 8 | Overly formal Slack message in a casual ops channel (AI tell) | P5 | AI_TELL |
| 9 | Same sentence structure repeated in 3+ injected messages (`"Hi [X], I wanted to let you know..."`) | P5 | AI_TELL |
| 10 | Orphaned record with no tool discovery path (GSheets entry unreachable by any search/list tool) | P6 | ORPHANED |
| 11 | Injection pre-solves the task — single smoking-gun record states the conclusion | P7 | PRE_SOLVED |
| 12 | All critical data in one service — no cross-service friction required | P7 | NO_FRICTION |
| 13 | No decoys or near-matches — correct records trivially filterable | P7/P8 | Low trap density score |
| 14 | Email `sent_at` after `received_at` (chronologically impossible) | P3 | TEMPORAL_VIOLATION |
| 15 | Slack `ts` resolves to a date outside the universe window (e.g., epoch → 2021) | P2 | ID_VIOLATION |

---

## Key Rules

1. **All 7 structural gates must PASS** — any single failure blocks the task. No "minor injection defect" exception exists.
2. **Difficulty score >= 2.5 required** — tasks that are too easy waste evaluation resources and fail to differentiate model capabilities.
3. **Naturalness matters** — AI-generated-sounding injections break task realism and get flagged by QC. Real Slack messages in #eng-general are short, casual, and use abbreviations.
4. **Every injected record must be reachable** — orphaned data creates phantom entity failures downstream. If an agent can't discover it via MCP tools, it doesn't exist for evaluation purposes.
5. **Cross-service consistency is non-negotiable** — a team member named "Foster" in Slack and "Forster" in Gmail will cause agent confusion that isn't part of the intended difficulty.
6. **Pre-solving kills task value** — if one record hands the agent the answer, the task measures retrieval speed, not reasoning ability. Scatter the signal, add noise, require synthesis.
7. **Author visibility is not runner visibility** — Universe Explorer has author god-mode. Required evidence in a persona-scoped service (per the live `Docs/14_Persona_ACL.md` Access matrix — derive the set from the doc, do not hardcode it) must still be reachable to the assigned Agent Runner persona under the active read ACL, subject only to intentional denial outcomes or authorized unscoped alternate sources.
