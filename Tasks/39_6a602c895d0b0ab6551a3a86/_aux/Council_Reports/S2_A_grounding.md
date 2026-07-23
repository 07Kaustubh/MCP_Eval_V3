# S2 Council A: Oracle Events Grounding Sweep

- **Universe:** starpm (V4)
- **Today:** 2026-07-01 (Wednesday, America/Chicago)
- **Target of review:** `Tasks/39_6a602c895d0b0ab6551a3a86/6_Oracle_Events.txt` (29 OEs)
- **Prompt anchor:** `5_Prompt.txt` (R5)
- **Scope:** grounding only (tool names, parameter names, universe atoms, conventions, prompt anchoring). Completeness / Accuracy / density / lever preservation are Council B's job.

---

## A1 — Tool-name sweep

Every tool named in OE1-OE29 checked against `StarPM_Base_Universe/7_Server_Tools_Details.json` and root `AGENTS.md` StarPM section (for Slack tools not in the JSON catalog).

| OE | Tool | Server | Exists? |
|---|---|---|---|
| OE2-OE5 | `contacts_search_contacts` | contacts | Y |
| OE6 | `list_bases`, `list_tables_for_base` | airtable | Y |
| OE7 | `get_table_schema` | airtable | Y |
| OE8 | `search_records` | airtable | Y |
| OE9 | `list_issues` | linear | Y |
| OE10-OE12 | `get_issue` | linear | Y |
| OE13-OE15 | `list_comments` | linear | Y |
| OE16 | `list_issue_statuses` | linear | Y |
| OE17, OE19, OE21 | `save_comment` | linear | Y |
| OE18, OE20, OE22 | `save_issue` | linear | Y |
| OE23 | `update_records_for_table` | airtable | Y |
| OE24 | `search_threads`, `get_thread` | gmail | Y |
| OE25 | `create_draft` | gmail | Y |
| OE26 | `slack_read_channel` | slack | Y (per AGENTS.md StarPM Slack docs) |
| OE27 | `slack_send_message` | slack | Y (per AGENTS.md StarPM Slack docs) |
| OE28 | `list_events` | gcalendar | Y |
| OE29 | `create_event` | gcalendar | Y |

Negative references (contra-instructions, do-not-use):
- OE23 negative reference to `create_record_comment` — valid airtable tool, correctly instructed against.
- OE27 negative reference to `slack_send_message_draft` — valid StarPM Slack tool, correctly instructed against (draft-only trap).

**A1 verdict: PASS.** All 15 distinct tool names resolve on the correct server. No unknown tools.

---

## A2 — Parameter-name sweep

Every parameter binding checked against tool signatures. Zero-tolerance on StarPM-specific traps.

| OE | Tool | Params bound | Signature match? |
|---|---|---|---|
| OE2-OE5 | `contacts_search_contacts` | `query` | Y |
| OE6 | `list_tables_for_base` | `baseId` | Y (camelCase) |
| OE7 | `get_table_schema` | `baseId`, `tables[]` | Y |
| OE8 | `search_records` | `baseId`, `table`, `query` | Y (note: uses `table` not `tableId` per schema) |
| OE9 | `list_issues` | `team`, `query` | Y (`team` not `teamId`) |
| OE10-OE12 | `get_issue` | `id` | Y |
| OE13-OE15 | `list_comments` | `issueId` | Y (camelCase) |
| OE16 | `list_issue_statuses` | `team` | Y |
| OE17, OE19, OE21 | `save_comment` | `issueId`, `body` | Y (NOT `content`, NOT `text`, NOT `issue_id`) |
| OE18, OE20, OE22 | `save_issue` | `id`, `state` | Y (state is workflow-state-id string) |
| OE23 | `update_records_for_table` | `baseId`, `tableId`, `records[]` (with `recordId`, `fields{}`) | Y (camelCase) |
| OE24 | `search_threads`, `get_thread` | `query`, `threadId` | Y |
| OE25 | `create_draft` | `to[]`, `cc[]`, `subject`, `replyToMessageId`, `body` | Y (`body`, NOT `content`) |
| OE26 | `slack_read_channel` | `channel_id` | Y |
| OE27 | `slack_send_message` | `channel_id`, `thread_ts`, `message` | Y (`message`, NOT `payload`, NOT `text`) |
| OE28 | `list_events` | `calendarId`, `startTime`, `endTime`, `timeZone`, `fullText` | Y (camelCase) |
| OE29 | `create_event` | `calendarId`, `summary`, `startTime`, `endTime`, `timeZone`, `description` | Y (camelCase) |

Explicit trap-affirmations in OE bodies (each is correctly worded):
- OE17: "issueId (camelCase) and body (not content, not text)" — matches Linear signature.
- OE23: "camelCase (baseId, tableId, records)" — matches Airtable signature.
- OE25: "The Gmail parameter for the message text is body, not content. There is no send tool" — matches Gmail signature; no send tool exists in the catalog.
- OE27: "message, not payload and not text" — matches StarPM Slack convention (differs from Brookfield's `payload`).

**A2 verdict: PASS.** All parameter bindings align with tool signatures. All four hard StarPM traps (Airtable camelCase, Gmail `body` + draft-only, Slack `message`, Linear `save_comment(issueId, body)` + `list_issue_statuses(team)`) are correctly bound.

---

## A3 — Universe-atom grounding

Every named atom queried against `_aux/Universe_Split/`.

**Contacts (`contacts.contacts.json`)** — all confirmed:

| Persona | email | contact_id | job |
|---|---|---|---|
| Brooke Phillips | brooke.phillips@starpm.com | `c46d47256fd95ca6aca770c8dddda5eb` | Apartment Property Supervisor |
| Carlos Mendez | carlos.mendez@starpm.com | `8608e0778a655232982787cef4fac0b2` | Onsite Property Manager |
| James Bennett | james.bennett@starpm.com | `9f49e592505f5fac8e91d72c7c745f26` | Assistant Maintenance Technician |
| Sandra Allen | sandra.allen@starpm.com | `ae1dbd31ad1450a3b781c8c96c0ecf43` | Leasing Agent |
| Jaime Salinas | jaime.salinas@starpm.com | `3ebf03fa155253deb123bb334fb1bd03` | Quality Control Inspector |

All contact_ids in OE2-OE5 match exactly. Sandra's role (Leasing Agent) matches OE5 as authored.

**Airtable (`airtable.airtable_bases.json`, `_tables.json`, `_fields.json`, `_records.json`)** — all confirmed:

- Base `appPropertyOps` name "Property Operations" — matches OE6.
- Table `tblMakeReady` name "Make-Ready Turns" — matches OE6.
- Fields on `tblMakeReady`: `fldUnit`, `fldTurnStatus`, `fldMoveOut`, `fldTargetReady`, `fldNotes2` — all 5 fields named in OE7 exist and typing is consistent (`fldTurnStatus` singleSelect, `fldNotes2` multilineText).
- Record `rec291f423370e2a2db` present with:
  - `fldUnit` = "Las Vistas 3C" ✓
  - `fldMoveOut` = "2026-06-09" ✓
  - `fldTurnStatus` = "selReady" ✓
  - `fldTargetReady` = "2026-06-18" ✓
  - `fldNotes2` narrative ends on Brooke's supervisory sign-off (no active Jaime second-pass line) ✓ — matches OE8 read.

**Linear (`linear.linear_issues.json`, `_comments.json`, `_workflow_states.json`)** — all confirmed:

- OPS-224 "Correct living room baseboard paint touch-ups — Las Vistas 3C", state `state_OPS_3`, team `team_001`, completed_at null ✓
- OPS-225 "Reclean refrigerator and oven interiors — Las Vistas 3C", state `state_OPS_3`, team `team_001`, completed_at null ✓
- OPS-226 "Reinstall bathroom towel ring correctly — Las Vistas 3C", state `state_OPS_3`, team `team_001`, completed_at null ✓
- Bennett comments (all three):
  - `comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02` on OPS-224 @ 2026-06-17T16:44:00-05:00, body verbatim match ✓
  - `comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13` on OPS-225 @ 2026-06-17T11:19:00-05:00, body verbatim match ✓
  - `comment_c3e69a4f5bad63a8d1f43e1b6c709d24` on OPS-226 @ 2026-06-16T15:34:00-05:00, body verbatim match ✓
  - All three carry `user_id=null` — Bennett attribution must lean on body content (OE13-15 do this correctly: they refer to "Bennett's observation" and match observed body against ticket subject; no user_id claim).
- Workflow states on team_001: `state_OPS_0` Backlog, `_1` Todo, `_2` In Progress, `_3` In Review (started), `_4` Done (completed) ✓ — OE16 correctly names `state_OPS_4` as Done.

**Gmail (`gmail.gmail_threads.json`, `_messages.json`)** — all confirmed:

- Thread `b8e4d0a3f2c5b9e7` subject "Las Vistas 3C - closeout package" — canonical closeout thread ✓
- Message `d0e6f2c5b4a70b19` on that thread, subject matches ✓
- Distractor threads `a7f3c92e1b4d8e56` (subject "QC Inspection Failed - Las Vistas 3C") and `9f0bd31ccf588236` (subject "Las Vistas 3C QC punch list") both exist and are correctly identified as pre-rework fail threads ✓

**Slack (`slack.slack_channels.json`, `_messages.json`, `_users.json`)** — all confirmed:

- Channel `C004` name `#make-ready` ✓
- Brooke's 6/18 closeout parent: message id `03e5b7c4a9fb5d803c7e1b4a52d69f7c`, ts `1781788320.000202`, ch `C004`, text begins "Jaime, Las Vistas 3C came off rework yesterday…" ✓ — text matches OE26 quotation verbatim.
- Distractor 6/16 QC-FAIL parent: message id `01c3f5a2e7d94b681a5c9f2e30b47d5a`, ts `1781645520.000200`, ch `C004`, text begins "Ran QC on Las Vistas 3C this afternoon…" ✓ — correctly identified in OE26 as not the closeout target.
- Sandra Allen's Slack user id `UADB2B4E045` ✓ — real_name "Sandra Allen", email `sandra.allen@starpm.com`. Correct format for OE27 mention `<@UADB2B4E045>`.

**Gcalendar (`gcalendar.gcalendar_calendars.json`, `_events.json`)** — all confirmed:

- Calendar `jaime.salinas@starpm.com` exists, primary=True ✓
- No 3C-referenced events on jaime.salinas@starpm.com in 2026-07-01..2026-07-08 window — OE28 declares "A null result... is a valid outcome" so this is consistent grounding.

**A3 verdict: PASS.** Every named atom (5 contacts + 1 base + 1 table + 5 field ids + 1 record id + 3 ticket identifiers + 3 comment ids + 5 workflow state ids + 3 thread ids + 1 gmail message id + 2 slack parent ids + 2 slack ts values + 1 slack user id + 1 calendar id) is grounded in `_aux/Universe_Split/`.

---

## A4 — Convention sweep

Checked against `Reference/OE_Convention_Inventory.json`.

- **Line prefix** `^OE\d+:` — 29 OEs, all prefixed correctly, sequential.
- **Free-form prose, no structured JSON** — every OE is prose. PASS.
- **Em-dash / en-dash ban** — full-file scan: 0 em-dashes (U+2014), 0 en-dashes (U+2013). PASS.
- **Opening phrases** — matches inventory patterns: "Call contacts_search_contacts…" (OE2-5, lookup-first), "Call list_bases…" (OE6, action-first), "Call search_records…" (OE8), "Call list_issues…" (OE9), "Call get_issue…" (OE10-12), "Call list_comments…" (OE13-15), "Post…" (OE17, OE19, OE21), "Move…" (OE18, OE20, OE22), "Append…" (OE23), "Draft…" (OE25), "Post…" (OE27), "Create…" (OE29), "Orient the closeout on today…" (OE1, inspect-first frame). PASS.
- **"Conclude:" clauses** — used in OE8 (fldTurnStatus selReady still requires append), OE13 (item matches / per-item comment mandate), OE14, OE15, OE18 (out-of-queue). Each is a one-sentence downstream-applicable reasoning line — matches inventory pattern. PASS.
- **"(or similar)" for free-text queries** — used in OE2/3/4/5 (contact queries), OE8, OE9, OE24, OE26, OE28. All applied to free-text `query`/`fullText` params. PASS.
- **Concrete values on all named ids** — every id in OE bodies quoted with concrete value; no placeholders. PASS.
- **Tool-name-with-param-aliases anti-pattern** — none observed. PASS.

**Observation (non-blocking):** OPS-224/225/226 titles in the base universe contain em-dashes ("… — Las Vistas 3C"). OE10-OE12 describe the ticket subject in paraphrase (e.g., "the living room baseboard rework ticket") rather than transcribing the title verbatim, so the em-dash never enters the OE file. This is the defensible transcription documented under project rule 5.

**A4 verdict: PASS.**

---

## A5 — Prompt-anchor sweep

Every OE traced back to at least one prompt sentence in `5_Prompt.txt` (R5).

| OE | Prompt anchor |
|---|---|
| OE1 | L1 "Circling back today to finish closing 3C out before the week is over" + L7 supervisory-line preservation |
| OE2 | L1 "Brooke's followed up since"; L7 "not just Brooke's supervisory note"; L11 cc Brooke |
| OE3 | L11 "Carlos needs an email from us" |
| OE4 | L5 "Bennett dropped a completion note on each of the three 3C punch items" |
| OE5 | L13 "tag Sandra so leasing sees it" |
| OE6 | L7 "Pull the make-ready record on 3C" |
| OE7 | L7 "get my second-pass sign-off written into it" (fldNotes2 target) |
| OE8 | L7 "Read what's already sitting in the notes so my sign-off reads as a continuation" |
| OE9 | L5 "each of the three 3C punch items" |
| OE10-OE12 | L5 "make sure the item he's writing up actually matches what the ticket is about" |
| OE13-OE15 | L5 "Pull his note off each ticket" + subject-match instruction |
| OE16 | L5 "get each ticket moved through my sign and out of my queue" (Done state) |
| OE17-OE22 | L5 "with the pass called out for each item, not a blanket close" |
| OE23 | L7 full paragraph on fldNotes2 continuation append |
| OE24 | L11 "Carlos needs an email" (canonical closeout thread) |
| OE25 | L11 "Copy Brooke", "Keep it short, this is a hand-off, not a report" |
| OE26 | L13 "Post in the #make-ready channel" |
| OE27 | L13 "the formal close is done and 3C is live for showings, and tag Sandra" |
| OE28 | L15 "Check the calendar for any 3C showings booked between now and next Wednesday" |
| OE29 | L15 "set me a reminder for Friday morning to spot-check 3C's fridge and oven interiors" |

No orphan OEs. Every OE has a prompt anchor.

**A5 verdict: PASS.**

---

## Summary

| Sweep | Verdict |
|---|---|
| A1 Tool-name | PASS |
| A2 Parameter-name | PASS |
| A3 Universe-atom | PASS |
| A4 Convention | PASS |
| A5 Prompt-anchor | PASS |

Zero blocking issues. Zero missing atoms. Zero convention drift. Zero HubSpot references (L6 lever cleanly dropped per S1.5). Zero em-dashes. All four StarPM-specific parameter traps (Airtable camelCase, Gmail `body`+no-send, Slack `message`, Linear `save_comment(issueId, body)` / `list_issue_statuses(team)`) correctly handled.

**VERDICT: GO**
