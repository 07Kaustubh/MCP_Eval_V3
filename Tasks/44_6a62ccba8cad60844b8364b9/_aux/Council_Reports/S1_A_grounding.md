# Council A — Grounding and Convention · S1 Prompt

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Deliverable:** `Tasks/44_6a62ccba8cad60844b8364b9/5_Prompt.txt` (313 words, 14 sentences)
**Persona:** Jaime Salinas · Quality Control Inspector · `p_007` · `jaime.salinas@starpm.com`
**Verdict: GO** — 0 BLOCKER, 0 MAJOR, 4 MODERATE, 6 MINOR/NOTE.

Date-anchor note: `_aux/Fact_Ledger.json` `lifecycle.today = null`, so `validate.py` emitted a Brookfield fallback of 2026-06-12. That fallback is wrong. `_aux/Universe_Index/today_horizon.json` (`"universe_today": "2026-07-01"`) and `StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md` Universe constants ("Today" = **2026-07-01**, America/Chicago) are authoritative. All checks below resolve against 2026-07-01.

---

## A1 — Grounding sweep

Every concrete claim, verified against `_aux/Universe_Split/`.

| # | Claim | Resolution |
|---|---|---|
| 1 | Initiative **"Preventive Maintenance Push"** exists | `slack.slack_messages.json`:ts `1778171944.000091` (msg id `79382e91ebb45dcbb9650de9d80f2218`); `linear.linear_projects.json`:`proj_003` name = "Preventive Maintenance Push"; `linear.linear_issues.json`:OPS-35, OPS-40, OPS-44 titles |
| 2 | Scope = **HVAC + plumbing + electrical, portfolio-wide** | `slack.slack_messages.json`:ts `1778171944.000091` — verbatim: *"kicking off the portfolio-wide HVAC, plumbing, and electrical audit before summer heat hits"* |
| 3 | **Brooke started it** | same record, `user_id` = `U9741B657FE` = Brooke Phillips (`slack.slack_users.json`); also `linear.linear_issues.json`:OPS-35/OPS-40/OPS-44 creator/assignee Brooke Phillips |
| 4 | **In early May** | same record `created_at` = `2026-05-07T16:39:04+00:00` → 2026-05-07 America/Chicago. Corroborated: `_aux/Hardness_Plan.md` kickoff date 2026-05-07 |
| 5 | **Brooke Phillips** is a real person, Jaime's supervisor lane | `contacts.contacts.json`:`c46d47256fd95ca6aca770c8dddda5eb` — job "Apartment Property Supervisor", `brooke.phillips@starpm.com`; `gcalendar.gcalendar_calendars.json`:`brooke.phillips@starpm.com` |
| 6 | **Jaime is the QC anchor on it** | `slack.slack_messages.json`:ts `1778171944.000091` @-mentions `@Jaime Salinas`; `linear.linear_issues.json`:OPS-87/OPS-96/OPS-98 `assignee_id` = `user_d3186a640f425ae0b69423f09aa4d7ec` (Jaime Salinas); OPS-51 desc *"Coordinate with Jaime or Carlos"*; `linear.linear_comments.json`:OPS-108 *"Moving this to In Review for Jaime to look over"*; `PersonaBrief.txt` "the impartial QC eye" |
| 7 | **Both cluster spot-checks logged as passing** | `linear.linear_issues.json`:**OPS-87** title *"South and North cluster HVAC QC spot-checks - both passed"*; **OPS-98** title *"QC spot-checks complete - South and North clusters closed"*; `linear.linear_comments.json`:OPS-98 ×2 (*"Everything cleared QC, so I've moved both cluster issues to Done"*) |
| 8 | **In late May** | OPS-87 `created_at` = `2026-05-24T15:45:34-05:00`; OPS-98 `created_at` = `2026-05-25T08:55:00-05:00`; OPS-98 comments 2026-05-25T09:00 and T14:00 |
| 9 | **Crew declared the HVAC run wrapped** | `slack.slack_messages.json`:ts `1779308446.000005` (Elias Navarro, *"all three clusters are done. Every unit serviced"*) and ts `1779308447.000006` (*"Summer HVAC push is a wrap. All three clusters done, 34 units total serviced"*). Elias = "Lead Maintenance Technician" per `contacts.contacts.json`:`a245b80cabe554b3aa29bce2ece73429` → "the crew" is accurate |
| 10 | **"around the same time"** | Elias wrap `created_at` = `2026-05-20T20:20:46+00:00`; Jaime's sign-off 5/24–5/25. 4–5 days apart, same week. Corroborating later wrap claims: `linear.linear_comments.json`:OPS-56 (2026-05-20, *"All South cluster units are done"*), OPS-108 (2026-05-28 / 2026-05-30, East wrapped). Soft qualifier "around" → GROUNDED |
| 11 | **End-of-June close-out target** | `linear.linear_issues.json`:**OPS-186** desc *"The goal is to have every open issue resolved and closed out before the end of June"* (created 2026-06-17); `slack.slack_messages.json`:ts `1781899601.000096` and ts `1781902061.000097` (Brooke, 2026-06-19, *"Goal is to close everything out before end of June"*) |
| 12 | **"came and went yesterday"** | today = 2026-07-01 → yesterday = 2026-06-30 = end of June. `_aux/Universe_Index/today_horizon.json` |
| 13 | **"cluster by cluster"** — four clusters exist | South (OPS-43, OPS-56, OPS-186), North (OPS-40, OPS-44), East (OPS-99, OPS-108), West (OPS-35, OPS-91, OPS-186). Prompt names no count → no artificial precision, and West discovery stays a lever |
| 14 | **"the channel the push has been running in"** | `slack.slack_channels.json`:`C001` = `#maintenance`. Push-keyword message distribution: C001 = 12, C007 = 1 (incidental). Unambiguous |
| 15 | **"our maintenance ticket log"** | `airtable.airtable_tables.json`:`tblMaintenanceTickets` name "Maintenance Tickets", desc *"System of record for maintenance work orders; Linear is secondary"*; 50 records in `airtable.airtable_records.json` |
| 16 | **"my calendar"** | `gcalendar.gcalendar_calendars.json`:`jaime.salinas@starpm.com` (primary, owner) |

**A1: PASS — zero NOT FOUND. Zero ungrounded concrete claims.**

---

## A2 — Convention sweep

### Hard rules (`Reference/Prompt_Format.md`)

| Rule | Result |
|---|---|
| 500-word cap | **PASS** — 313 words |
| No em-dash / en-dash | **PASS** — 0 U+2014, 0 U+2013 |
| No tool names | **PASS** — systems named naturally only: "tracking item", "our maintenance ticket log", "the channel", "an email", "my calendar" |
| No MCP-server names | **PASS** — zero |
| No internal IDs | **PASS** — no `OPS-nn`, no `C001`, no `ts` values, no `rec…`/`tbl…`/`proj_…`/`state_…`, no `MT-2026-…`. (Regex hits on `ts ` and `rec` are substrings of "spot-checks " and "records"/"re-inspect") |
| No pre-solving | **PASS** — no root cause, no culprit, no count, no named open item. The only state assertion ("it is still sitting open") is public knowledge Brooke posted on 6/19 |
| First person, natural voice | **PASS** — matches `PersonaBrief.txt` (formality 0.55, verbosity 0.30, observation-first, zero emoji) |
| One coherent situation | **PASS** — see removal test |
| Plain prose, no headings/bullets | **PASS** |
| Anti-pattern clichés | **PASS** — no "go through everything and surface every", no "loop in", no "CC our CEO", no "before it blows up", no over-signalled service list |

### Three-movement structure

- **Trigger** (S1–S2): deadline passed yesterday, push still open.
- **Context** (S3–S5): Brooke started it in early May, scope, Jaime's role, what she logged, what the crew said.
- **Asks** (S6–S14): investigate → correct tracking → raise items → notes on her records → Airtable ticket → calendar slot → Slack post → Gmail draft → retraction beat.

Matches the V4 QC_Passed samples (Task1 through Task4) on shape. Task4 in particular has the same anatomy: withheld sign-off, three investigation strands, then "tell me straight whether we are clear … or whether I am holding it". **PASS.**

### Sentence-removal test — all 14 sentences

| # | Sentence | Rest still makes sense without it? | Bolt-on? |
|---|---|---|---|
| 1 | "End of June was the target to have the Preventive Maintenance Push closed out." | **NO** — S2's "That" and "it" lose their antecedent; the prompt would open on a dangling pronoun and the initiative would never be named | **NO** |
| 2 | "That came and went yesterday and it is still sitting open." | NO — the trigger (deadline passed, still open) disappears | NO |
| 3 | "Brooke started this in early May, HVAC, plumbing and electrical across the whole portfolio, and I have been the QC eye on it." | NO — "Brooke" in S11 becomes unintroduced; scope and role vanish | NO |
| 4 | "I logged both cluster spot-checks as passing in late May and my read is that my part of it is finished." | NO — S9 "My own spot-check records" and S14 "my earlier sign-off" lose their referents; the Lever 9 anchor disappears | NO |
| 5 | "The crew called the HVAC run wrapped around the same time." | Grammatically yes; situationally no | **NO** — see adjudication |
| 6 | "Before I put my name to this closing out, I need to know where every piece of it stands as of today, cluster by cluster…" | NO — the whole investigation frame goes | NO |
| 7 | "Work out what is actually finished and what is not, and get our tracking to match." | NO — S9 "part of that" loses its antecedent | NO |
| 8 | "Anything still open gets its own tracking item raised…" | NO — one of five write asks | NO |
| 9 | "My own spot-check records are part of that…" | NO — one of five write asks | NO |
| 10 | "Anything flagged in the field … maintenance ticket log … put a slot on my calendar…" | NO — two of five write asks | NO |
| 11 | "Then post where this stands in the channel … and draft an email to Brooke…" | NO — two of five write asks; S12's "Brooke's email" loses its antecedent | NO |
| 12 | "I do not want Brooke's email written so it can be read either way." | NO — topic sentence for S13/S14 | NO |
| 13 | "If my QC side is a pass, say pass." | NO — S14's "If it is not" loses "it" | NO |
| 14 | "If it is not, say straight out that my earlier sign-off does not hold…" | NO — the primary Gemini-selective differentiator | NO |

### Adjudication of the validator WARN on sentence 1 — **FALSE POSITIVE, no change required**

Validator text: *"bolt-on candidate: sentence `End of June was the target to have the Preventive Maintenance Push closed out.` shares no named entities with the rest of the prompt."*

The heuristic is entity-overlap, not the actual removal test, and it misses the coreference chain. S1 is the only sentence that names the initiative as a proper noun; every later reference is a lowercase coreference — "That" and "it" (S2), "this" (S3), "it" (S4, S6), "this" (S7), "this" (S11, S14), and critically "**the push**" in S11 ("the channel the push has been running in"). Because the entity extractor only matches capitalised multi-word spans, it scores the anaphora as zero overlap.

Run the real test: delete S1 and the prompt opens **"That came and went yesterday and it is still sitting open."** — "That" has no referent, "it" has no referent, and no reader can tell what came and went or what is open. The remainder does **not** make sense. S1 is the Trigger movement of the three-movement structure and is load-bearing for four downstream coreferences.

**Verdict: NOT a bolt-on. Coherence PASS. Do not edit S1.** Recommend recording this as a known heuristic limitation so it is not re-litigated in AUDIT/FINAL.

### Sentence 5 adjudication

S5 ("The crew called the HVAC run wrapped around the same time.") is the only sentence that survives a strict grammatical removal. It is nonetheless **not** a bolt-on: it is inside the Context movement, describes the *same* situation (whether the push is actually finished), introduces no new ask, and plants Lever 1 (the loudest wrap claim) as persona-held belief. The V4 QC_Passed samples carry equivalent removable context sentences (Task4: *"A few things landed on me this week that I am not comfortable waving through"*). **NOTE only.**

### Minor convention notes

- **N1 (MINOR):** Opening is a deadline statement in past tense rather than a person/event mid-thought entry as in Task1 ("The subledger decommission review with Andrea is tomorrow") and Task4 ("Ryan has the Northstar interim partner package ready"). Still trigger-first and in-register for a verbosity-0.30 persona. No change required.
- **N2 (NOTE):** Validator NOTE "distinct services referenced: 2" is a regex artifact. The prompt naturally reaches five services: Linear ("tracking item"), Airtable ("our maintenance ticket log"), Google Calendar ("my calendar"), Slack ("the channel"), Gmail ("an email"). No defect.
- **N3 (NOTE):** 313 words is over the 300 "tighten" advisory but well under the 500 hard cap. Every sentence passes the removal test, so there is nothing to cut without losing a write ask or a coreference anchor.

**A2: PASS.**

---

## A3 — Narrative State Consistency

| # | State claim | Underlying record | Verdict |
|---|---|---|---|
| 1 | *"End of June was the target to have the Preventive Maintenance Push closed out."* | `linear.linear_issues.json`:OPS-186 desc; `slack.slack_messages.json`:ts `1781899601.000096`, ts `1781902061.000097` | **CONSISTENT** (past-tense statement of a stated target) |
| 2 | *"That came and went yesterday"* | today 2026-07-01; end of June = 2026-06-30 | **CONSISTENT** |
| 3 | **"it is still sitting open"** (the push) | `linear.linear_projects.json`:`proj_003` `state` = `"backlog"`. Of 60 `proj_003` issues: In Progress 17, Todo 16, In Review 10, Backlog 8, Done 9. Named open push issues: OPS-17 In Progress, OPS-35 In Progress, OPS-43 In Progress, OPS-44 Backlog, OPS-56 In Progress, OPS-87 Todo, OPS-96 Todo, OPS-97 Todo, OPS-98 In Progress, OPS-99 In Progress, OPS-108 Backlog, OPS-186 Todo | **CONSISTENT — verified TRUE of the universe.** Not contradicted by OPS-40 (Done) or OPS-91 (Done): those are individual cluster issues, not the initiative. The claim is about the initiative, which is demonstrably open |
| 4 | *"Brooke started this in early May"* | ts `1778171944.000091`, 2026-05-07 | **CONSISTENT** |
| 5 | *"I have been the QC eye on it"* | OPS-87 / OPS-96 / OPS-98 assignee = Jaime; kickoff @-mention | **CONSISTENT** |
| 6 | *"I logged both cluster spot-checks as passing in late May"* | OPS-87 title/desc, OPS-98 title/desc + 2 comments. This asserts only what she **logged** — literally true of the prose in those records | **CONSISTENT** |
| 7 | **"my read is that my part of it is finished"** | Actual universe state: **OPS-87 `state_OPS_1` Todo, OPS-96 `state_OPS_1` Todo, OPS-98 `state_OPS_2` In Progress; all three `completed_at` = null** | **CONSISTENT AS A BELIEF STATEMENT.** The soft verb "my read is that" marks this as the persona's reading, not a factual assertion about the record. It is exactly the framing mandated by Hardness_Plan constraint 8 (Learnings L24). It is *false as a fact* — which is the point, that is Lever 9 — and *true as a statement of her belief*, which is what is asserted. **Not a truthfulness defect** |
| 8 | *"The crew called the HVAC run wrapped around the same time."* | ts `1779308446.000005`, ts `1779308447.000006` | **CONSISTENT** (reported speech, literally true) |

**Requested pairwise adjudication, explicitly:**
- **FIRST claim ("it is still sitting open") — TRUE of the universe.** `proj_003.state = "backlog"`; 51 of 60 project issues in non-completed states; OPS-186 (2026-06-17) and Brooke's 6/19 posts both describe live open work.
- **SECOND claim ("my read is that my part of it is finished") — a BELIEF statement with a soft verb, not a false factual assertion.** Hedged by "my read is that". The hard claim in the same sentence ("I logged both cluster spot-checks as passing") is verifiably true of OPS-87/OPS-98 prose.

Also verified against Hardness_Plan constraint 3 (F9): the prompt makes **no** claim that Jaime's QC queue is otherwise clear, and **no** claim that the maintenance-budget question is settled. The 2026-07-15 Make-Ready QC Inspection (Mesa Vista 4C) and 2026-07-23 Q3 Make-Ready Planning & Budget Review are not contradicted. Zero of the 9 confirmed future events touch the push.

**A3: PASS — zero contradictions.**

---

## A4 — Action-vs-Universe-Prescription

| Prompt action | Relevant universe prescription | Verdict |
|---|---|---|
| "get our tracking to match" (status correction) | No record prescribes a different disposition. OPS-87/OPS-96/OPS-98 prose *claims* Done/In Review; the `state_id` column disagrees. Reconciling them is the intended work | **ALIGNED** |
| "Anything still open gets its own tracking item raised, with the person who owns that work named on it" | `linear.linear_comments.json`:OPS-43 (*"need to get a reschedule coordinated"*, names Carlos); OPS-56 (*"Carlos, can you get a second round of access notices out to those two remaining tenants"*); OPS-97 (*"I'll flag those for Brooke to get vendor quotes lined up"*); `slack`:ts `1779569323.000012` (Elias to count filter stock). Every one of these names an owner. The prompt's ask is **additive and owner-consistent** | **ALIGNED — no divergence** |
| "belongs in our maintenance ticket log rather than sitting as a tracking item" | `linear.linear_teams.json`:`team_001` desc — *"Maintenance work orders are tracked in the Airtable Maintenance Tickets table, which is the system of record. Linear is secondary for maintenance items and is used for broader operations and project tracking."* `airtable.airtable_tables.json`:`tblMaintenanceTickets` desc — same | **ALIGNED — the prompt is following the universe's own routing rule, not overriding it** |
| "put a slot on my calendar to go back out and re-inspect" | No prescription anywhere; `gcalendar.gcalendar_calendars.json`:`jaime.salinas@starpm.com` exists | **ALIGNED** |
| "post where this stands in the channel the push has been running in" | C001 is where Brooke, Elias, John, Lisa, Carlos and Jaime have all posted push updates | **ALIGNED** |
| "draft an email to Brooke" | Brooke is Apartment Property Supervisor and the initiative owner; Category 3 authoring checklist lists "Brooke Phillips (escalation and reporting)". `draft`, not `send` — correct | **ALIGNED** |
| "say straight out that my earlier sign-off does not hold" | The authority being overridden is Jaime's own logged judgement (OPS-98 comments). Overriding your own prior sign-off requires no external grant | **ALIGNED** |

**Authority check — Jaime Salinas, Quality Control Inspector, mid seniority, Portfolio Operations:**

| Write | Authority evidence | Verdict |
|---|---|---|
| Create Linear issues | Precedent: OPS-224 / OPS-225 / OPS-226, `creator_id` = Jaime. Category 3.1: *"`linear_mock_create_issue` (any surprise issues found during QC)"* | **OK** |
| Comment on / correct her own three QC issues | She is `assignee_id` on all three | **OK** |
| Create an Airtable maintenance ticket | `airtable.airtable_users.json`:`usr_jaime_salinas`. Category 3 primary system: Airtable | **OK** |
| Create an event on her own calendar | Own primary calendar | **OK** |
| Post in `#maintenance` | She has posted there: ts `1779562423.000092` | **OK** |
| Draft an email to her supervisor | Category 3: Gmail (Onsite PM / escalation correspondence) | **OK** |

**No AUTHORITY_GAP.** One MODERATE watch item recorded below (M2).

**A4: PASS — zero ACTION_DIVERGENCE, zero AUTHORITY_GAP.**

---

## A6 — Persona Scope (AGENTS.md hard rule 13 / Evals_starpm F7)

**Jaime's assignment set, built from `_aux/Universe_Split/`:**

- Linear, `assignee_id = user_d3186a640f425ae0b69423f09aa4d7ec`: **OPS-87** (Todo, `proj_003`), **OPS-96** (Todo, `proj_003`), **OPS-98** (In Progress, `proj_001`).
- Linear, `creator_id` = Jaime: OPS-224, OPS-225, OPS-226 (all Done, Las Vistas 3C make-ready — outside the push).
- Slack, authored by `U2CD1BC03B2` (7 messages): C004 ×6 (`1779501872.000004`, `1779543703.000086`, `1779563023.000006`, `1779832536.000039`, `1781620200.000000`, `1781809200.000000`) and **C001 ×1** (`1779562423.000092`, the North-cluster walk-through note).
- Calendar: `jaime.salinas@starpm.com` primary; attendee (declined) on the 2026-06-02T16:45 Preventive Maintenance Push Mid-Initiative Check-In.
- Airtable: `usr_jaime_salinas`.

**Possessive-scope resolution:**

| Possessive phrase | Resolves to | In scope? |
|---|---|---|
| "my part of it" | Her QC slice of the push = OPS-87 + OPS-96 + OPS-98 | **YES** |
| **"my own spot-check records"** | **Exactly 3 records: OPS-87, OPS-96, OPS-98** — the only three Linear issues assigned to Jaime whose titles are spot-checks ("South and North cluster HVAC QC spot-checks", "HVAC filter replacements QC spot-check - portfolio-wide", "QC spot-checks complete") | **YES** |
| "my calendar" | `gcalendar.gcalendar_calendars.json`:`jaime.salinas@starpm.com` | **YES** |
| "my QC side" | The same three issues plus her 5/23 field note (ts `1779562423.000092`) | **YES** |
| "my earlier sign-off" | `linear.linear_comments.json`:OPS-98, 2026-05-25T09:00 (*"Everything cleared QC, so I've moved both cluster issues to Done"*) and 2026-05-25T14:00 | **YES** |

**Requested count and classification — "my own spot-check records" resolves to exactly 3 records.**

This is **NOT a uniqueness problem and F7 AMBIGUOUS_TARGET does not fire.** The ask is *"with a short note left on each one"* — an explicitly exhaustive **set WRITE** over the full set, not a single-target write where one of several candidates must be picked. Rule 13 fires only when "the prompt names the target only by entity" and a rubric would pin one row id; here the prompt names the entire set and the correct behaviour is three comments.

**What this obligates downstream (F8 NON_ATOMIC_ENUM, A13):** S3 must carry **three atomic Outcome rubrics**, one per issue (OPS-87, OPS-96, OPS-98), each graded on content ("where it landed and why"), never a single "at least one comment" or "comments on her spot-check issues" bundle. Any criterion whose two facts come from different issues must be split.

**Residual (MODERATE, M1):** OPS-99 and OPS-108 both carry the title *"East cluster HVAC service complete - QC passed"* and their descriptions state that Jaime walked the East-cluster spot-check — but both are assigned to **Elias Navarro**, not Jaime. An agent enumerating "spot-check records mentioning Jaime" could reach 5 rather than 3. The word "**own**" plus assignee ownership makes 3 the clear leading reading, and the divergence is additive (two extra comments) rather than contradictory, so no rubric grading the three assigned issues can false-fail. Recorded as MODERATE with an optional tightening below, not a BLOCK.

**A6: PASS — zero SCOPE_DRIFT. Every possessive-scoped ask resolves to records Jaime actually owns.**

---

## A7 — Clarity & Specificity holistic

Re-read cold. No second reading produces a *contradictory* write-action set. Findings:

**(a) "our maintenance ticket log" vs "tracking item" — reliably distinguishes Airtable from Linear. MINOR only.**

Four independent disambiguators:
1. `airtable.airtable_tables.json`:`tblMaintenanceTickets` is literally named **"Maintenance Tickets"** and its description reads *"System of record for maintenance work orders; Linear is secondary."*
2. `linear.linear_teams.json`:`team_001` description says the same from the other side: *"Maintenance work orders are tracked in the Airtable Maintenance Tickets table, which is the system of record. Linear is secondary for maintenance items and is used for broader operations and project tracking."*
3. Staff usage in Slack maps "ticket" → Airtable and "issue" → Linear consistently: Carlos ts `1778849489.000014` *"I just logged the ticket in Airtable"*; Carlos ts `1779571123.000019` *"Marked it complete in Airtable"*; John ts `1779716376.000079` *"marked the ticket Completed in Airtable"*; versus Jaime ts `1779562423.000092` *"flagged on the Linear issue"* and OPS-51 *"each of you has individual issues assigned"*.
4. The prompt itself draws the contrast explicitly (*"rather than sitting as a tracking item"*), and only Linear issues can satisfy S8's *"with the person who owns that work named on it"* — `tblMaintenanceTickets` has exactly four fields (Ticket Number, Description, Priority, Completion Date) and **no owner field**.

**Watch item (MODERATE, M3):** `StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md` Universe-constants table lists *"Linear (maintenance tickets)"* as a system of record — which contradicts both live in-universe descriptions. That line is a stale authoring-guide artifact and agents never read it; they read the MCP data, which is unanimous. Recommend S3 does not fail an agent that additionally mirrors the item in Linear, and that the OE pins the Airtable ticket explicitly.

**(b) Delegation clarity — HARD GATE PASS.**

Full scan for "I'll [verb]" / "I need to [verb]" / "I want to [verb]" / "I'm going to [verb]":
- **Zero** "I'll [verb]" constructions. No self-action statements at all.
- S6: *"I need to know where every piece of it stands"* — a request **for information from the agent**, the canonical delegation form; it is immediately followed by imperatives ("Work out…", "get our tracking to match").
- S6: *"I need our records saying the same thing"* — restated as an explicit imperative in S7 (*"get our tracking to match"*), so no ambiguity about who acts.
- S10: *"…to go back out and re-inspect…"* — an infinitive describing the *purpose* of the calendar slot (Jaime's future physical site visit), not an action the agent could perform. Unambiguous.
- S12: *"I do not want Brooke's email written so it can be read either way"* — a constraint on the deliverable the agent produces.

No Action Decision Ambiguity. **PASS.**

**(c) "put a slot on my calendar" — MINOR.**

Resolvable: "my calendar" → `jaime.salinas@starpm.com` (primary, owner). "a slot" → a calendar event. Referent of "whatever ends up in that follow-up" → the items routed to the maintenance ticket log in the immediately preceding clause. Two residual under-specifications:
- **No date/time given.** The agent must choose. Normal for this prompt family (Category 3.3 worked example: *"put it on my calendar"*), and the persona would not dictate a slot before knowing what is open.
- **Singular "a slot" vs N items.** Leading reading is one re-inspection visit covering the follow-up set. Both readings produce a calendar event on Jaime's calendar for a re-inspection of the flagged items, so a content-graded rubric passes either way.

Classified **MINOR** (same write action, different count/framing). S3 guidance: grade "≥1 event on Jaime's calendar, future-dated, describing the re-inspection of the follow-up items"; do not pin a specific date or a specific event count.

**(d) Additional read — "get our tracking to match" scope breadth. MODERATE (M2).**

Reading A: correct the state on Jaime's own three QC issues. Reading B: correct state across every push-adjacent issue (~20 rows, including Elias's OPS-43/OPS-56, Carlos's OPS-97, Lisa's OPS-91). Different volumes of Linear updates, and Reading B has Jaime editing colleagues' records.

Not a MAJOR gap, because the prompt's **concrete** write asks are enumerated in the sentences that follow and they bound the graded surface: S8 (new tracking items with owners), S9 (notes on *her own* spot-check records), S10 (Airtable + calendar), S11 (Slack + Gmail). "Get our tracking to match" reads as the umbrella intent whose instantiation is S8+S9. Reading B is additive, never contradictory — no write under B undoes a write under A. Recorded as MODERATE for S2/S3: the OE should scope status corrections to Jaime's three QC issues, and rubrics should not penalise extra corrections elsewhere.

**(e) "the channel the push has been running in" — MINOR.**

Correctly descriptive per Hardness_Plan constraint 5 (channel-lock-in). Resolves to C001 `#maintenance` (12 of 13 push-keyword messages; Jaime's habitual channel is C004, which carries none). The OE must still pin C001 explicitly.

**(f) "draft an email to Brooke" — PASS.** "Draft", not "send". Matches the intended `create_draft` write. Recipient resolvable via `contacts.contacts.json`.

**A7: PASS — zero MAJOR clarity gaps.** 1 MODERATE (M2), 3 MINOR.

---

## A10 — Business Function Match

`StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md`, five categories: 1 Property Operations · 2 Portfolio Coordination & Owner Relations · **3 Quality Control & Field Services** · 4 Maintenance & Repairs · 5 Leasing & Applicant Intake.

Persona → function mapping in that doc: **Jaime Salinas → 3 Quality Control & Field Services**, and *"tasks are always authored from a persona's home Business Function, not from participant appearances."*

The prompt's primary scenario is a **QC sign-off validation**: whether Jaime's own spot-check pass holds, what her QC coverage actually reached, correcting QC tracking, opening follow-ups for items that failed QC, scheduling a **re-inspection**, and issuing a pass-or-kick-back verdict to the supervisor. That is Category 3, closest to subcategory **3.2 Property Inspections & Compliance** ("routine standing-property inspections not tied to a turn, cross-property scope"), with the Category 3 signature move — *"either signs off on marketing-ready status or kicks work back"* — as the prompt's climax (S13/S14).

Adjacency noted and rejected: the underlying work is HVAC/plumbing/electrical (Category 4), and the initiative is Brooke's (Category 2). But the acting lens, the persona, the verdict authority and every write are QC. Not a reassignment.

**BUSINESS_FUNCTION: assigned=3 prompt_primary=3 match=true.**

---

## A11 — End-to-End Solvability

Every link in the `_aux/Hardness_Plan.md` projected trajectory, checked against `_aux/Universe_Split/`:

| Step | Required link | Materialized? |
|---|---|---|
| 1 | Linear workflow-states table (to decode `state_id`) | **YES** — `linear.linear_workflow_states.json`, 5 rows: `state_OPS_0` Backlog, `_1` Todo, `_2` In Progress, `_3` In Review, `_4` Done |
| 2 | Jaime's three issues + their states | **YES** — OPS-87 `state_OPS_1`, OPS-96 `state_OPS_1`, OPS-98 `state_OPS_2`; all `completed_at` null |
| 3 | Comments on those issues | **YES** — OPS-96 ×1 (2026-05-30, *"filters look good across the board"*), OPS-98 ×2 (2026-05-25 09:00 and 14:00). **OPS-87 has 0 comments** — its contradicting prose lives in the `description` (*"moved both from In Review to Done"*), which is materialized. Not a break |
| 4 | Elias's wrap posts | **YES** — ts `1779308446.000005`, ts `1779308447.000006` |
| 5 | Lisa's 5/27 ask | **YES** — ts `1779884437.000093`, `created_at` 2026-05-27, Lisa Smith |
| 6 | Brooke's 6/19 posts | **YES** — ts `1781899601.000096` and ts `1781902061.000097` |
| 7 | South-cluster thread replies | **YES** — parent ts `1779308442.000001` (id `8ce45073c71f56ae89c859c0f3f6fc09`, `reply_count` = 2); replies ts `1779308444.000003` and ts `1779308445.000004`, both `thread_parent_id` = `8ce45073c71f56ae89c859c0f3f6fc09`. Corroborated by OPS-43 comments ×2 and OPS-56 comments ×2 |
| 8 | Filter-restock thread | **YES** — parent ts `1779567943.000011` (id `7b8f161126065f47bf66e3e0326ef2ea`, `reply_count` = 1, John Smith, *"restock before I can finish the run"*); reply ts `1779569323.000012` (`thread_parent_id` = `7b8f161126065f47bf66e3e0326ef2ea`, Brooke). Contradicts OPS-96's *"all units"* comment |
| 9 | Carlos's plumbing findings | **YES** — Slack ts `1780256425.000094` (2026-05-31); OPS-97 (`state_OPS_1` Todo) + comment 2026-05-25T17:19; escalation ts `1780494075.000095` (2026-06-03) |
| 10 | OPS-186 | **YES** — `state_OPS_1` Todo, created 2026-06-17, desc names *"the West Cluster work still underway"* and the end-of-June goal |
| 11 | 2026-06-02 calendar check-in | **YES** — `gcalendar.gcalendar_events.json`, **"Preventive Maintenance Push Mid-Initiative Check-In"**, 2026-06-02T16:45:00-05:00, organiser `carlos.mendez@starpm.com`, attendees Brooke (tentative), Carlos (accepted), **Jaime (declined)**; description names *"the budget implications of the water heater replacements Carlos flagged"* |
| 12 | Airtable Maintenance Tickets table | **YES** — `tblMaintenanceTickets` in base `appPropertyOps`, 50 records, fields `fldTicketNumber` / `fldDescription` / `fldPriority` (Low/Medium/High) / `fldCompletionDate`. Write target is unique by construction: no existing ticket references the push, the clusters, condensate drains, the no-access unit, or Carlos's water heaters |
| 13 | Jaime's 5/23 field note (Lever 8 hop A) | **YES** — ts `1779562423.000092` |
| 14 | Slack destination channel | **YES** — C001 `#maintenance` |
| 15 | Gmail recipient resolution | **YES** — `contacts.contacts.json`:`c46d47256fd95ca6aca770c8dddda5eb`. `gmail.gmail_messages.json` has **0** push-related messages across 484 rows, so Gmail is correctly a write-only surface (Hardness_Plan constraint 4 satisfied) |
| 16 | Four clusters discoverable | **YES** — South/North/East/West across OPS-28/35/40/43/44/56/66/81/87/91/98/99/108/186 |
| 17 | Airtable decoy noise (Lever 4) | **YES** — 22 of 50 tickets match HVAC/water-heater/coil/filter keywords, all on unrelated properties (Building C 304, Palomar 312, Pinecrest 12, Riverside, Oakdale) |

**Zero SOLVABILITY_BREAK.** Similarity independently clear: `_aux/Similarity_Report.json` max composite **27.2** against a corpus of 44, under the 40 ceiling.

**A11: PASS.**

---

## Escape-valve check (Hardness_Plan constraint 9 / Learnings L29)

**Result: NO VIOLATION.** No sentence invites the agent to look for contradictions in the Linear workflow-state column, or in any named surface.

Closest candidates, quoted and adjudicated:

1. > *"…I need to know where every piece of it stands as of today, cluster by cluster, and I need our records saying the same thing."*

   Names no system, no field, no status, and no contradiction. It states an outcome requirement (records should agree with reality), not a discovery hint. An agent that latches on Elias's wrap plus Jaime's own sign-off satisfies this sentence with "the QC side is clean, West is open" and never opens the state column — which is exactly the predicted stump. **Not an escape valve.**

2. > *"Work out what is actually finished and what is not, and get our tracking to match."*

   The nearest miss and the one MODERATE watch item (M4). "Get our tracking to match" is a *write* instruction, and it is the instruction the Hardness Brief itself mandates ("a Linear follow-up for the open work plus **a correction on her own QC record**") — the correction write cannot be graded without it. It says "our tracking" generically, not "the status field", not "Linear", not "the workflow state". It does not say "flag anything inconsistent" or "tell me if anything contradicts what I've said", which is the forbidden L29 shape. It is also answer-neutral: it does not assert that tracking *is* wrong. **Not an escape valve**, but it is the sentence closest to the line; if a later gate wants more margin, see the optional tightening below.

3. > *"If my QC side is a pass, say pass. If it is not, say straight out that my earlier sign-off does not hold and this should not be treated as closeable yet, with the reasons."*

   This is the **mandated** retraction beat (Hardness_Plan line 166, the deliberate Gemini-selective differentiator per Learnings L31), so it cannot be removed. It is also answer-**neutral** and symmetric: it presents "pass" first and does not hint which branch is correct, name any evidence, or point at any surface. An agent must already have derived the answer for the conditional to bite. Constraint 9's concern is a clause that *tips* the answer; a symmetric conditional does not. **Not an escape valve.**

Positively confirmed absent: no sentence contains "check whether", "look for", "see if anything contradicts", "flag any discrepancies", "the statuses may be out of date", "verify the states", or any reference to Linear, issues, statuses, or workflow states.

**Lever 2 (structured-DB skip) is intact.** Levers 1, 5, 8 and 9 are likewise unhinted: the prompt names Elias's wrap only as a thing "the crew called" (Lever 1 latch preserved), never mentions threads (Lever 5), never mentions her 5/23 field note or the two North units (Lever 8), and states her belief in soft-verb form (Lever 9).

---

## Findings

| ID | Sev | Perspective | Location | Issue | Fix |
|---|---|---|---|---|---|
| M1 | MODERATE | A6 | prompt S9 | "my own spot-check records" resolves cleanly to 3 issues (OPS-87/96/98), but OPS-99 and OPS-108 describe Jaime's East-cluster spot-check while being assigned to Elias Navarro; an agent could over-include and comment on 5 | No prompt edit required. Bind it in S2/S3: OE pins the three issues Jaime is assignee on; S3 writes **three atomic per-issue Outcome rubrics** graded on note content, and accepts (does not penalise) extra comments on OPS-99/OPS-108 |
| M2 | MODERATE | A4 / A7(d) | prompt S7 | "get our tracking to match" is scope-unbounded; a literal reading extends status corrections to ~20 push issues owned by Elias, Carlos, Lisa and Brooke | No prompt edit required (additive, non-contradictory). OE scopes status correction to Jaime's three QC issues; rubrics grade only those and do not fail extra corrections. Optional prompt tightening if a later gate wants it: *"…and get our tracking to match, starting with mine."* |
| M3 | MODERATE | A7(a) | cross-doc | `StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md` Universe-constants row says "Linear (maintenance tickets)" is a system of record, contradicting `linear_teams.team_001.description` and `airtable_tables.tblMaintenanceTickets.description`, which both name Airtable | Live universe data wins and agents only see the live data. OE pins the Airtable ticket explicitly; S3 accepts an agent that additionally mirrors it in Linear. Optionally correct the base-universe doc line out of band |
| M4 | MODERATE | escape-valve | prompt S7 | "Work out what is actually finished and what is not, and get our tracking to match" is the sentence closest to the constraint-9 line | Keep as written — it is the mandated correction-write ask, names no surface, and is answer-neutral. Recorded so AUDIT/FINAL do not re-litigate it as new |
| N1 | MINOR | A7(c) | prompt S10 | "put a slot on my calendar" gives no date/time and is singular where N items may qualify | S3 grades "≥1 future-dated event on `jaime.salinas@starpm.com` describing the re-inspection of the follow-up items"; do not pin a date or a count |
| N2 | MINOR | A7(e) | prompt S11 | "the channel the push has been running in" is correctly descriptive (constraint 5) but the OE must resolve it | OE pins C001 `#maintenance`; rubric accepts the equivalent path |
| N3 | MINOR | A2 | prompt S1 | Validator WARN "bolt-on candidate" on sentence 1 | **False positive — no action.** Removal test fails: S2's "That" and "it" lose their antecedent and the initiative is never named. Heuristic misses the lowercase coreference chain (including "the push" in S11) |
| N4 | NOTE | A2 | prompt S5 | "The crew called the HVAC run wrapped around the same time" is the only sentence that survives a strict grammatical removal | Keep. Same situation, no new ask, plants Lever 1. Equivalent removable context sentences appear in QC_Passed Task4 |
| N5 | NOTE | A1 | prompt S5 | "around the same time" spans 2026-05-20 (Elias) to 2026-05-25 (Jaime), 4–5 days | Soft qualifier, grounded. Note that `_aux/Hardness_Plan.md` line 25 says Lisa's 5/27 ask was "five days after Elias declared all clusters done"; the actual gap is 7 days (Elias 2026-05-20). Plan-side arithmetic nit only, no deliverable impact |
| N6 | NOTE | infra | `_aux/Fact_Ledger.json` | `lifecycle.today = null`, so `validate.py` emits a Brookfield fallback of 2026-06-12 as "the single date-alignment source for prompt + OE + rubrics". Against 2026-06-12, "yesterday" would be 2026-06-11, not end of June | Set `lifecycle.today = "2026-07-01"` before S2/S3 so OE and rubric date alignment do not inherit the wrong anchor. Does not affect the prompt, which is correct against the authoritative 2026-07-01 |

---

## Verdict

**GO.**

A1 PASS (zero ungrounded claims) · A2 PASS (zero hard-rule violations; the validator's bolt-on WARN is adjudicated a false positive) · A3 PASS (zero state contradictions; "still sitting open" verified true, "my read is … finished" verified as a soft-verb belief) · A4 PASS (zero divergence, zero authority gap) · A6 PASS (all possessive scope resolves to owned records; "my own spot-check records" = exactly 3, a set-write not a uniqueness problem) · A7 PASS (zero MAJOR clarity gaps; delegation hard gate clean) · A10 PASS (assigned 3 = primary 3) · A11 PASS (zero solvability breaks) · escape-valve PASS (Lever 2 intact).

Four MODERATE findings are all downstream-binding constraints for S2/S3 rather than prompt defects. **No edit to `5_Prompt.txt` is required.**

```json
{
  "phase": "prompt",
  "council": "A",
  "task_dir": "Tasks/44_6a62ccba8cad60844b8364b9",
  "verdict": "GO",
  "perspectives": {
    "A1": { "status": "PASS", "findings": [] },
    "A2": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MINOR",
          "location": "5_Prompt.txt:1",
          "issue": "Validator WARN flags sentence 1 as a bolt-on candidate on named-entity overlap",
          "fix": "False positive - removal test fails (S2 'That'/'it' lose antecedent, initiative never named); heuristic misses the lowercase coreference chain including 'the push' in S11. No edit.",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "5_Prompt.txt:5",
          "issue": "Sentence 5 is the only sentence surviving a strict grammatical removal test",
          "fix": "Keep - same situation, no new ask, plants Lever 1; matches QC_Passed sample practice.",
          "propagate_to": null
        }
      ]
    },
    "A3": { "status": "PASS", "findings": [] },
    "A4": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "5_Prompt.txt:7",
          "issue": "'get our tracking to match' is scope-unbounded; literal reading extends status corrections to ~20 push issues owned by Elias, Carlos, Lisa and Brooke",
          "fix": "Additive not contradictory. OE scopes status correction to OPS-87/OPS-96/OPS-98; rubrics grade only those and do not penalise extra corrections.",
          "propagate_to": "S2"
        }
      ]
    },
    "A6": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "5_Prompt.txt:9",
          "issue": "'my own spot-check records' resolves to exactly 3 (OPS-87, OPS-96, OPS-98) but OPS-99/OPS-108 describe Jaime's East spot-check while assigned to Elias Navarro; agent could over-include to 5",
          "fix": "Set-write not uniqueness problem, so F7 does not fire. S3 must carry three atomic per-issue Outcome rubrics graded on note content and accept extra comments on OPS-99/OPS-108.",
          "propagate_to": "S3"
        }
      ]
    },
    "A7": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "5_Prompt.txt:10",
          "issue": "StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md lists Linear as system of record for maintenance tickets, contradicting linear_teams.team_001.description and airtable_tables.tblMaintenanceTickets.description which both name Airtable",
          "fix": "Live universe data wins; agents only read live data. OE pins the Airtable ticket explicitly; S3 accepts an agent that additionally mirrors it in Linear.",
          "propagate_to": "S2"
        },
        {
          "severity": "MINOR",
          "location": "5_Prompt.txt:10",
          "issue": "'put a slot on my calendar' gives no date/time and is singular where N follow-up items may qualify",
          "fix": "S3 grades >=1 future-dated event on jaime.salinas@starpm.com describing the re-inspection; do not pin date or count.",
          "propagate_to": "S3"
        },
        {
          "severity": "MINOR",
          "location": "5_Prompt.txt:11",
          "issue": "'the channel the push has been running in' is descriptive per channel-lock-in constraint and must be resolved downstream",
          "fix": "OE pins C001 #maintenance; rubric accepts the equivalent path.",
          "propagate_to": "S2"
        }
      ]
    },
    "A10": { "status": "PASS", "findings": [] },
    "A11": { "status": "PASS", "findings": [] },
    "escape_valve": {
      "status": "PASS",
      "findings": [
        {
          "severity": "MODERATE",
          "location": "5_Prompt.txt:7",
          "issue": "'Work out what is actually finished and what is not, and get our tracking to match' is the sentence closest to the constraint-9 escape-valve line",
          "fix": "Keep as written - it is the mandated correction-write ask, names no system/field/contradiction, and is answer-neutral. Recorded so AUDIT/FINAL do not re-litigate as new.",
          "propagate_to": null
        }
      ]
    },
    "infra": {
      "status": "NOTE",
      "findings": [
        {
          "severity": "NOTE",
          "location": "_aux/Fact_Ledger.json:lifecycle.today",
          "issue": "lifecycle.today is null so validate.py emits a Brookfield fallback of 2026-06-12 as the single date-alignment source for prompt + OE + rubrics",
          "fix": "Set lifecycle.today = '2026-07-01' before S2/S3 so OE and rubric date alignment do not inherit the wrong anchor.",
          "propagate_to": null
        }
      ]
    }
  },
  "scores": {
    "grounding_truthfulness": { "score": 5, "scheme": "1/3/5", "reason": "All 16 concrete claims resolve to Universe_Split records; zero NOT FOUND" },
    "narrative_state_consistency": { "score": 5, "scheme": "1/3/5", "reason": "'still sitting open' true of proj_003 (backlog, 51/60 issues non-completed); 'my read is ... finished' correctly soft-verbed as belief" },
    "convention_compliance": { "score": 5, "scheme": "1/3/5", "reason": "313 words, zero dashes, zero tool names, zero IDs, no pre-solving, three-movement structure; validator bolt-on WARN adjudicated false positive" },
    "clarity_specificity": { "score": 5, "scheme": "1/3/5", "reason": "Zero MAJOR gaps; delegation hard gate clean (no 'I'll [verb]'); ticket-vs-issue routing disambiguated by four independent universe surfaces" },
    "persona_scope": { "score": 5, "scheme": "1/3/5", "reason": "All five possessive-scoped asks resolve to Jaime-owned records; 'my own spot-check records' = 3, a set-write, F7 does not fire" },
    "business_function_match": { "score": 5, "scheme": "1/5", "reason": "assigned=3 prompt_primary=3 match=true" },
    "solvability": { "score": 5, "scheme": "1/3/5", "reason": "All 17 trajectory links materialized in Universe_Split; zero SOLVABILITY_BREAK" }
  },
  "density_projection": null,
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": []
  },
  "bucket_1_risk_pct": null,
  "iteration": 1,
  "timestamp": "2026-07-26T00:00:00-05:00"
}
```
