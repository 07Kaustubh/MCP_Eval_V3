# Reads — S2 (v11 E2 compliance log)

Task: `Tasks/44_6a62ccba8cad60844b8364b9` · Universe: `starpm` (V4) · Date anchor: **2026-07-01** America/Chicago (from `_aux/Universe_Index/today_horizon.json`, NOT Fact_Ledger)

## Project / pipeline docs

- `AGENTS.md` :: hard rules 1-13 re-read. Rule 11 density is framework-scoped: **StarPM V4 = 40+ average per model**, 15 = QC-spec fail floor. The V3-family 50/40 bands do NOT apply to this task (confirmed against `_aux/Hardness_Plan.md:4`). Rule 13 single-target uniqueness / every-service sweep / naive-agent simulation applied at step T8. Rule 4: no universe edits; `4_Changelog.json` is `[]` and `9_Universe_inject.sql` is the comment-only template header, so no injection is in play.
- `Reference/Sessions/S2.md` :: phase contract, Step 0 / Step 0.5 gates, 9-step procedure, exit criteria, StarPM-only parameter traps in the Bootstrap block.
- `Reference/OE_Format.md` :: numbered-prose structure, what each step must carry (action, exact tool, params with concrete values, what the agent concludes), hard rules (no dashes, real tool names, real params, real values), OE-to-rubric mapping table, StarPM v4 trap list.
- `Reference/Knowledge_Flow.md` :: not re-read in full; path ownership taken from the S2 runbook's required-inputs table.

## Eval specs

- `Evals_starpm/2_OE_Eval.md` :: OE Completeness (PASS 5 = full critical path: discovery + dependency chain + every write action) and OE Accuracy (PASS 5 = every tool / service / parameter / expected value matches the universe). Both dimensions are NON-FAIL-only but propagate into rubric quality. Phase 1.2 anti-patterns absorbed: **no pure-reasoning OE steps** (every OE must carry a tool call; deductions fold into the step that produced the data). Phase 2.4 T9 act-vs-defer hard gate applied: swept C001 + C004 + Gmail for any documented decision to defer the push close-out. Phase 2.5 date consistency resolved against 2026-07-01.
- `Evals_starpm/1_Prompt_Eval.md` :: not re-scored (S1 owns it); consulted only for the sub-dim names quoted in `_aux/Verification_s1.md`.
- `Evals_starpm/5_Submission_Gate_Eval.md` :: F7 AMBIGUOUS_TARGET / F8 NON_ATOMIC_ENUM / F9 UNRECONCILED_FUTURE_EVT carried as design-time constraints on the OE (see Verification_s2 T8 row).

## QC specs

- `Docs_starpm/7_QC_Spec_Doc1.json` :: Oracle Event dimension. OE Completeness and OE Accuracy grading bands taken verbatim; both scored in `_aux/Council_Reports/S2_B_adversarial.md`.
- `Docs_starpm/2_Rubrics_V3_Guidelines.md` :: OE-to-rubric mapping (write action -> Outcome 1.1 + 1.2; key fact the user asked to be told -> Outcome 2.1; read/lookup -> Process only via the three-condition test). Used to build the rubric-preview map in `_aux/Reasoning/OE_solvability.md`.
- `Docs_starpm/1_Project_Instructions_Overall.md` :: Step 3.5 OE writing rules; density statement "AVERAGE TOOL CALL COUNT OF ALL AGENT RUNS MUST BE 40+".
- `Docs_starpm/9_Common_Error.md` :: consulted for the phantom-tool and wrong-service error families.
- `Docs_starpm/13_QC_Companion.md` :: **deliberately NOT used as SSOT** (Brookfield-contaminated per `Validators/regression_baseline/ROUTING_DECISIONS.md`).

## Reference corpus

- `QC_Tasks/V4_Tasks/QC_Passed/Task1_6a26c29d5f5b7cf1ea90c0cc/6_Oracle_Events.txt` :: 22 OEs. Voice baseline: "OE N: <verb> ... using <tool> (<param>: "<value>", ...) to discover <expected values>. <what the agent should conclude>." Confirms concrete-id-per-step convention and a write-heavy finale.
- `QC_Tasks/V4_Tasks/QC_Passed/Task2_6a27b70a80b7729ca5d6d88d/6_Oracle_Events.txt` :: 28 OEs. Confirms "(or similar)" query-alternative phrasing and the pattern of stating the derived conclusion inline on the step that produced it.
- Note: both reference files are **Brookfield-fixture flavored** (per `AGENTS.md` StarPM section). Structure and voice adopted; tool names and universe facts taken only from StarPM sources.

## Tool catalog (SSOT for every tool name and parameter in the OE)

- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: full signature dump taken for airtable, contacts, gcalendar, gmail, linear, slack. Verified in this phase:
  - `slack_send_message(channel_id*, message*)` — text param is `message`; `payload`/`text` do not exist. `slack_read_channel(channel_id*)`, `slack_read_thread(channel_id*, message_ts*)`, `slack_search_channels(query*)`, `slack_search_public(query*)`.
  - `gmail create_draft(to[], cc, bcc, subject, body, ...)` — `body`, not `content`. **No send tool exists** in the gmail server (draft-only confirmed by enumeration).
  - `linear save_issue(id, title, description, team, assignee, priority, state, project, ...)` — **`assignee` has type `null`**, i.e. it cannot carry a value. This independently confirms the S1 Council B binding that the follow-up item's owner must be written into `description` text.
  - `linear save_comment(issueId, body)`, `list_issue_statuses(team*)`, `list_issues(assignee, team, project, query, state, ...)`, `get_issue(id)`, `list_comments(issueId)`, `list_teams()`, `list_projects()`.
  - `airtable list_bases()`, `list_tables_for_base(baseId*)`, `get_table_schema(baseId*, tables*)`, `search_records(baseId*, table*, query*)`, `list_records_for_table(baseId*, tableId*)`, `create_records_for_table(baseId*, tableId*, records*)` — camelCase confirmed.
  - `gcalendar list_events(calendarId, startTime, endTime, fullText, ...)`, `create_event(summary*, startTime*, endTime*, calendarId, description, attendeeEmails, ...)`.
  - `contacts_search_contacts(query*, limit, cursor)`.
  - Phantom-tool check: no `linear_create_issue`, no `slack_conversations_add_message`, no `gmail_send_email`, no `airtable_list_records`, no `*_by_id` variant exists in this catalog. None appear in the OE.

## Per-task universe (the only source of truth for expected values)

- `_aux/Universe_Split/linear.linear_workflow_states.json` :: 5 states on team_001 — `state_OPS_0` Backlog, `state_OPS_1` Todo, `state_OPS_2` In Progress, `state_OPS_3` In Review, `state_OPS_4` Done.
- `_aux/Universe_Split/linear.linear_teams.json` :: single team `team_001` key `OPS` name "Operations". Description states Airtable Maintenance Tickets is the system of record and Linear is secondary.
- `_aux/Universe_Split/linear.linear_projects.json` :: `proj_001` Property Ops, `proj_002` Summer Make-Ready Program, `proj_003` Preventive Maintenance Push.
- `_aux/Universe_Split/linear.linear_issues.json` :: 230 rows. Every issue cited in the OE pulled and its `state_id`, `assignee_id`, `project_id`, `title`, `description` recorded (sign-off table in `_aux/Verification_s2.md`). **Exactly 3 issues carry `assignee_id` = Jaime Salinas: OPS-87, OPS-96, OPS-98.**
- `_aux/Universe_Split/linear.linear_comments.json` :: 48 rows; per-issue comment walk for OPS-34, OPS-43, OPS-56, OPS-96, OPS-97, OPS-98, OPS-108.
- `_aux/Universe_Split/linear.linear_users.json` :: Jaime = `user_d3186a640f425ae0b69423f09aa4d7ec`.
- `_aux/Universe_Split/slack.slack_channels.json` :: C001 #maintenance, C002 #leasing, C003 #general, C004 #make-ready, C005 #vendors, C006 #owner-relations, C007 #budget-review, C008 #applications.
- `_aux/Universe_Split/slack.slack_messages.json` :: 580 rows, 104 in C001, **37 distinct thread parents in C001**. Every `ts` in the OE verified, and thread parentage verified via `thread_parent_id` (not `thread_ts`, which is null throughout this dataset).
- `_aux/Universe_Split/slack.slack_users.json` :: Jaime has 1 message in C001 and 6 in C004 (channel-lock-in trap live).
- `_aux/Universe_Split/airtable.airtable_bases.json` / `airtable_tables.json` / `airtable_fields.json` :: base `appPropertyOps` "Property Operations"; table `tblMaintenanceTickets` (system of record, Linear secondary) with exactly 4 fields — `fldTicketNumber` Ticket Number (primary, singleLineText), `fldDescription` Description (multilineText), `fldPriority` Priority (singleSelect Low/Medium/High), `fldCompletionDate` Completion Date (date). **No owner field, no status field.**
- `_aux/Universe_Split/airtable.airtable_records.json` :: 170 rows, 50 in `tblMaintenanceTickets`. **Corrected at Council round 1:** an earlier note here said "23 match an HVAC keyword ... Building C 304, Palomar 312, Pinecrest 12, Rio Bend, Las Palmas 8D, Sunridge". The 23 came from a wide keyword family (`HVAC|coil|filter|condensate|water heater|hose bib|panel|refriger`); the literal token `HVAC` matches **18** rows. The property list was also wrong: **Sunridge appears in zero rows** of this table (it appears in Slack), Rio Bend appears in one non-HVAC row and Las Palmas in two non-HVAC rows. Verified distribution of the 18: Building C 9 (incl. unit 304 and the lobby), Palomar 4 (incl. unit 312), Pinecrest 12 / Elmwood / Riverside 1 each. The tally is **not a partition**: four rows name no property at all (`MT-2026-043` and `MT-2026-1257` "Unit 204", `MT-2026-082` compressor belt, `MT-2026-1320` budget review), and two standup rows name more than one site (`MT-2026-1219` Pinecrest + Elmwood, `MT-2026-062` Palomar + Riverside). **None is push-linked**, and zero rows anywhere in the table reference a cluster, the push, a condensate drain, 20x25 filters or a hose bib. Confirms the new ticket is unique by construction.
- `_aux/Universe_Split/gcalendar.gcalendar_calendars.json` :: 20 per-persona calendars including `jaime.salinas@starpm.com` (America/Chicago).
- `_aux/Universe_Split/gcalendar.gcalendar_events.json` :: all 565 rows swept. Three push events (Kick-Off 2026-05-08T16:45, Mid-Sprint Check-In 2026-05-25T15:11:27, Mid-Initiative Check-In 2026-06-02T16:45). **9 unique confirmed events on or after 2026-07-01; none touches the push, the clusters, or Jaime. Jaime's calendar has zero events on or after 2026-07-01** — F9 clean and the re-inspection slot is unique by construction.
- `_aux/Universe_Split/gmail.gmail_messages.json` :: 484 rows. Keyword sweep returns 15 HVAC-adjacent threads, **all unrelated to the push** (Ridgeline, Crestwood, Building 7, Maple Street, Pinecrest). Gmail is a write target only, never a source — consistent with the Hardness Plan constraint 4 (base64 bodies, snippet-only plaintext).
- `_aux/Universe_Split/contacts.contacts.json` :: 61 rows. Brooke Phillips / Apartment Property Supervisor / brooke.phillips@starpm.com; Jaime Salinas / Quality Control Inspector; Elias Navarro and John Smith and Tony Reyes / Lead Maintenance Technician; Carlos Mendez and Lisa Smith and Patricia Nguyen / Onsite Property Manager; Wesley Tran / Assistant Maintenance Technician; Teresa Wood / Executive Secretary.
- `_aux/Universe_Split/Universe_complete_data.json` :: answer-leakage grep re-run in this phase across 13 aggregate-conclusion phrasings — all zero hits. The single `coverage gap` hit is an unrelated after-hours staffing item on OPS-121.
- `_aux/Universe_Index/today_horizon.json` :: `universe_today` 2026-07-01, `universe_timezone` America/Chicago. **This is the date anchor for the phase.**
- `_aux/Fact_Ledger.json` :: consulted; `lifecycle.today` is still `null` (pre-declared defect A-11 / N6). Backfilled to `"2026-07-01"` in this phase per the AUDIT instruction that the fix land before S2. The `validate.py:464` code change remains out of scope for a task phase.

## Upstream phase artifacts

- `_aux/Hardness_Plan.md` :: 5 selected levers, 10 pre-registered constraints, density projection, dual-model mix, stump hypotheses. All 5 levers mapped to OE steps in `_aux/Reasoning/OE_solvability.md`.
- `_aux/Verification_s1.md` :: 5 discrepancies carried; items 1 (date anchor), 3 (density tighter than planned, prefer non-Linear reads) and 5 (Lever 8 hop B resolves to OPS-34, title actively misleading) are binding on this phase.
- `_aux/Council_Reports/S1_A_grounding.md` :: M1 (three-vs-five spot-check records), M2 (scope status correction to Jaime's three), M3 (Airtable is system of record, pin it), N1 (calendar slot: no date, no count), N2 (pin C001).
- `_aux/Council_Reports/S1_B_adversarial.md` :: owner goes in the issue description, never `assignee`; accept-band for extra comments on OPS-99 / OPS-108 / OPS-51; `tblMaintenanceTickets` has no owner field.
- `_aux/Council_Reports/AUDIT_prompt.md` :: A-1 owner accept-sets, A-2 routing partition (two North units -> Airtable; West coverage gap -> Linear; boundary items either way), A-3 retraction split into two atomic criteria graded on substance plus the S4 re-attribution pre-registration, A-5 no required or penalised state flip, A-6 Airtable graded on content, A-7 no Linear-only additions without cross-service compensation, A-8 never require naming OPS-34, A-11 date anchor. **Correction found at Council round 1:** `AUDIT_prompt.md:486` states OPS-34 carries 18 comments; the true count is **16**, verified in `linear.linear_comments.json`. The A-8 binding itself is unaffected (the title is still uninformative and the record must never be a graded identification), but the 18 was inherited into the OE draft and has been corrected there. The upstream artifact is left as written since this phase does not edit prior-phase reports.
- `_aux/Reasoning/prompt_design.md` :: consulted for the prompt-sentence-to-ask decomposition used in the forward coverage map.
