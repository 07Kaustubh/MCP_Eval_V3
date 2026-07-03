# Council A — Grounding (S2 OE Task 36)

Universe: **moveops** (V2.1 framework).
Sources consulted:
- `Tasks/36_6a44224ed5d3b47d6d727cf5/6_Oracle_Events.txt` (27 OEs)
- `Tasks/36_6a44224ed5d3b47d6d727cf5/_aux/Universe_Split/*.json` (per-task universe)
- `MoveOps_Base_Universe/6_Server_Tools_Details.json` (MoveOps V2.1 tool catalog)

## Verdict: **GO**

All 27 OEs pass tool-name existence, parameter-name existence, record-ID existence, timestamp accuracy, amount accuracy, persona disambiguation, prompt-anchor verification, write-action target validity, and data-anomaly handling. Zero blockers; five non-blocking advisories captured below.

## Per-perspective findings

### 1. Tool-name existence
Every tool token walked against the MoveOps catalog (Slack MCP, Email MCP, Linear MCP, Contacts MCP, Calendar MCP, Airtable MCP, CRM MCP, Quickbooks MCP).

- OE 1: `contacts_search_contacts` — exists (Contacts MCP). **PASS**
- OE 2, 4, 5, 6, 8: `search_emails`, `get_email_by_id` — both exist (Email MCP). **PASS**
- OE 3, 7: `get_email_by_id` — exists. **PASS**
- OE 9: `airtable_list_bases`, `airtable_get_record` — both exist (Airtable MCP). **PASS**
- OE 10: `airtable_get_record` — exists. **PASS**
- OE 11: `quickbooks_read_invoice` — exists (Quickbooks MCP). **PASS**
- OE 12: `conversations_search_messages` — exists (Slack MCP). **PASS**
- OE 13: `conversations_replies` — exists. **PASS**
- OE 14: `linear_list_issues`, `linear_get_issue` — both exist (Linear MCP). **PASS**
- OE 15: `linear_get_issue` — exists. **PASS**
- OE 16: `crm_list_engagements` — exists (CRM MCP). **PASS**
- OE 17: `crm_search_contacts` — exists. **PASS**
- OE 18, 19, 21, 27: `send_email` — exists as **UNPREFIXED** MoveOps email tool (`send_email`, not `email_send_email`). **PASS**
- OE 20, 22: `airtable_update_records` — exists. **PASS**
- OE 23: `conversations_add_message` — exists. **PASS**
- OE 24: `linear_create_comment` — exists. **PASS**
- OE 25: `crm_create_engagement` — exists. **PASS**
- OE 26: `calendar_add_calendar_event` — exists (Calendar MCP). **PASS**

No invented tool names.

### 2. Parameter-name existence
All parameter tokens on every tool call are real for that tool per the MoveOps catalog. All MoveOps parameter traps handled correctly.

- OE 1: `contacts_search_contacts(query="...")` — `query` valid. **PASS**
- OE 2, 4, 5, 6, 8: `search_emails(query, folder_name)` — both valid; `get_email_by_id(email_id, folder_name)` — both valid. **PASS**
- OE 9: `airtable_list_bases()` — no params required, valid. `airtable_get_record(base_id, table_name, record_id)` — all three valid; uses `table_name` correctly (not `table_id`). **PASS**
- OE 10: same as OE 9. **PASS**
- OE 11: `quickbooks_read_invoice(invoice_id)` — valid. **PASS**
- OE 12: `conversations_search_messages(search_query, filter_in_channel, filter_users_from)` — all three valid. **PASS**
- OE 13: `conversations_replies(channel_id, thread_ts)` — both valid; correctly uses `thread_ts` (NOT `thread_ts_legacy`). **PASS**
- OE 14: `linear_list_issues(query, team)` — both valid; MoveOps trap `team` (NOT `teamId`) respected. `linear_get_issue(id)` — valid. **PASS**
- OE 15: `linear_get_issue(id)` — valid. **PASS**
- OE 16: `crm_list_engagements(company_ids)` — valid. **PASS**
- OE 17: `crm_search_contacts(full_name)` — valid. **PASS**
- OE 18, 19, 21, 27: `send_email(sender, recipients, cc, subject, content)` — all valid; MoveOps trap `content` (NOT `body`/`text`) respected. **PASS**
- OE 20, 22: `airtable_update_records(base_id, table_id, records)` — all three valid; MoveOps trap `table_id` (NOT `table_name`) on update respected. **PASS**
- OE 23: `conversations_add_message(channel_id, thread_ts, payload)` — all three valid; MoveOps trap `payload` (NOT `text`/`body`/`content`) respected. **PASS**
- OE 24: `linear_create_comment(issueId, body)` — both valid and required. **PASS**
- OE 25: `crm_create_engagement(engagement_type, body, company_ids, contact_ids, title)` — all valid; required `engagement_type` + `body` both present. **PASS**
- OE 26: `calendar_add_calendar_event(title, start_datetime, end_datetime, attendees, description)` — all valid. **PASS**

Non-blocking advisory: OE 12 uses the prose descriptor `thread_ts_legacy` when naming the parent ts ("The rubric-canonical parent is thread_ts_legacy `1776997200.000000`"). This is narrative text, not a tool-call parameter, and OE 13's actual tool call correctly cites `thread_ts`. Consider renaming the descriptor for reader clarity.

### 3. Record ID existence
Every cited record ID resolves in Universe_Split (see evidence table below).

- Airtable records: `recSimoneRichterBrightloop`, `recMarcusWebbBrightloop` — **PASS**
- Base + table: `appMoveOpsOps001` (bases.json), `tblRelocations01` (tables.json) — **PASS**
- Emails: `email_email_6d0501ac647f`, `email_email_bedc44dbea30`, `email_email_ab2391d62ab1`, `email_email_a3ca1b6dd238`, `email_email_b6ce20dc2587`, `email_email_ca010e9c9446` — **PASS**
- Linear issues: `linear_issue_f85be674c9b8`, `linear_issue_c16357d188c6` — **PASS**
- CRM: `engagement_brightloop_apr2026_relocations`, `company_brightloop`, `contact_brightloop_simone_richter`, `contact_brightloop_marcus_webb`, `contact_brightloop_hr` — **PASS**
- QB: invoice `1008` = DocNumber `INV-2026-0308`, customer `cust_brightloop` — **PASS**
- Contacts: `contacts_contact_00589cf8404a` (Carmen Reyes @ UrbanNest) — **PASS**

### 4. Slack timestamp accuracy
Parent ts `1776997200.000000` retrieved from `slack.slack_messages.json`:
- `channel_id`: `C002` (= `#customer-engagement`, confirmed via `slack.slack_channels.json`) **matches OE 12 filter_in_channel** ✓
- `user_id`: `moveops_mina_hashimoto` **matches OE 12 filter_users_from** ✓
- `thread_ts`: `null` → this row IS a parent, not a reply — **matches OE 12 claim** ✓
- Text opens: "*I just did a BrightLoop audit after Tessa's expansion note and we have a real exposure here. The April batch is not actually clean.*" — **verbatim match** with OE 12 quote ✓
- OE 13 `conversations_replies(channel_id="C002", thread_ts="1776997200.000000")` — parameters correctly bound to the parent above. **PASS**
- OE 23 `conversations_add_message(channel_id="C002", thread_ts="1776997200.000000", payload=...)` — correctly attaches to the same parent, does not open a fresh top-level. **PASS**

### 5. Amount accuracy
QB invoice `1008` (`quickbooks.invoices.json`):
- `Id`: 1008 · `DocNumber`: INV-2026-0308 ✓
- `TotalAmt`: **11350** ✓ matches OE 11 / OE 24
- `TxnDate`: 2026-04-02 ✓ · `DueDate`: 2026-05-02 ✓
- `CustomerRef`: `{"value": "cust_brightloop", "name": "BrightLoop Analytics"}` ✓
- `BillEmail`: `tessa.moreno@brightloopanalytics.com` ✓
- Line items (5) sum to **$11,350** exactly:
  - `$4,500.00` Standard Relocation Package – Simone Richter, Chicago → Boston ✓
  - `$750.00` Rush Coordination Surcharge – Simone Richter (5-day turnaround, lease end April 6) ✓
  - `$4,500.00` Standard Relocation Package – Marcus Webb, Atlanta → Boston ✓
  - `$1,100.00` Vehicle Shipping Add-On – Marcus Webb (2019 Honda Civic VIN 2HGFC2F53KH123456, Road Runner, enclosed) ✓
  - `$500.00` Stipend Platform Fee – 2 employees (Simone Richter, Marcus Webb) ✓
- Per-employee exposure split cited in OE 11 / OE 24 validated: Simone $5,250 (4500+750), Marcus $5,600 (4500+1100), platform $500 → **$11,350 exact**. **PASS**

### 6. Persona-attribution disambiguation
- **Wrong Simone (StormCloud):** `contacts_contact_4d531c818e2a` — Simone Richter, `simone.richter@stormcloud.io`, StormCloud PMM — exists as a decoy identity. OE 17 explicit rejection **verified correct**. ✓
- **Wrong Marcus (Ironclad):** `contact_ironclad_001` (CRM) + `ext_prospect_ironclad` (Contacts) — Marcus Webb, `m.webb@ironcladsec.com`, Ironclad Cybersecurity — exists as decoy. OE 17 explicit rejection **verified correct**. ✓
- **Right Simone (BrightLoop):** `contact_brightloop_simone_richter` at `simone.richter@brightloopanalytics.com` ✓
- **Right Marcus (BrightLoop):** `contact_brightloop_marcus_webb` at `marcus.webb@brightloopanalytics.com` ✓
- **Carmen at UrbanNest:** `contacts_contact_00589cf8404a` at `carmen.reyes@urbannestsolutions.com` ✓
- Julian sender identity: `moveops_julian_brooks` = `julian.brooks@moveops.com` ✓
- Internal cc: `moveops_mina_hashimoto` = `mina.hashimoto@moveops.com` ✓

Recurring MoveOps landmine (per user memory `persona_attribution_landmine.md`) handled correctly. **PASS**

### 7. Prompt-anchor timestamps
- **Simone Airtable Special Requirements (OE 9):** *"URGENT — lease ends April 6. 5-day turnaround. Employee needs 2 weeks furnished temp housing on arrival in Boston. Rush surcharge applies. Expedited packing scheduled April 4-5."* → **silent on unit type (studio vs 1BR)**. OE 9's claim ("the Airtable record does not confirm the one-bedroom promise") **verified**. ✓
- **Marcus Airtable Special Requirements (OE 10):** Confirms 2019 Honda Civic VIN 2HGFC2F53KH123456, Road Runner Auto Transport third-party at ~$1,100, Swift Relocations does NOT handle auto transport. Silent on Indianapolis stall / April 18-20 window → correctly triggers OE 22 update. ✓
- **Road Runner email `email_email_a3ca1b6dd238` (OE 8):**
  - Folder: `INBOX` ✓
  - `is_read`: **False** → unread ✓ matches OE 8
  - Sender: `dispatch@roadrunnerautotransport.com`
  - Content states: "*unit is sitting at our Indianapolis transfer hub awaiting reassignment to an eastbound carrier*" ✓ (Indianapolis transfer hub)
  - Content states: "*As of this morning, the earliest revised delivery window we can offer is April 18-20*" ✓ (April 18–20 window, no hard date)
  - Original ETA was April 8; current status is delay with no committed replacement date — matches OE 8 framing exactly. **PASS**

### 8. Write-action target verification
Every write-target and every cc recipient resolved:
- **OE 18 (Simone email):** sender `julian.brooks@moveops.com` (moveops_julian_brooks) ✓; recipient `simone.richter@brightloopanalytics.com` (contact_brightloop_simone_richter) ✓; cc `mina.hashimoto@moveops.com` (moveops_mina_hashimoto) ✓.
- **OE 19 (Carmen email):** recipient `carmen.reyes@urbannestsolutions.com` (contacts_contact_00589cf8404a) ✓; cc `mina.hashimoto@moveops.com` ✓. Six numbered questions match exactly the six questions in the original `email_email_ab2391d62ab1` body (verified verbatim). ✓
- **OE 20 (Airtable Simone update):** base_id `appMoveOpsOps001` ✓, table_id `tblRelocations01` ✓, record id `recSimoneRichterBrightloop` ✓.
- **OE 21 (Marcus email):** recipient `marcus.webb@brightloopanalytics.com` (contact_brightloop_marcus_webb) ✓; cc `mina.hashimoto@moveops.com` ✓. Content anchors match: 2019 Honda Civic, Indianapolis transfer hub since April 11, April 18–20, no hard date. ✓
- **OE 22 (Airtable Marcus update):** base_id + table_id + record_id all resolved. ✓
- **OE 23 (Slack post):** channel_id `C002`, thread_ts `1776997200.000000` (parent verified in perspective 4). ✓
- **OE 24 (Linear comment):** issueId `linear_issue_f85be674c9b8` (Chloe Vance / team_operations / due 2026-04-22 / title matches OE 14). ✓
- **OE 25 (CRM engagement create):** engagement_type `NOTE`, company_ids `["company_brightloop"]` (verified), contact_ids `["contact_brightloop_hr"]` = Tessa Moreno at BrightLoop Analytics (**verified**). ✓
- **OE 26 (Calendar):** attendee `julian.brooks@moveops.com` ✓; start_datetime `2026-04-28T16:30:00-07:00` and end_datetime `2026-04-28T17:00:00-07:00` are ISO-valid; US/Pacific offset consistent with MoveOps universe today (2026-04-26 US/Pacific per `today_horizon`). ✓
- **OE 27 (Mina internal summary):** recipient `mina.hashimoto@moveops.com` ✓; no external cc. ✓

**PASS**

### 9. Data-anomaly handling
OE 4 correctly notes the sender-field anomaly on `email_email_ab2391d62ab1`:
- Actual `sender`: `carmen.reyes@urbannestsolutions.com` (anomaly)
- Actual `recipients_json`: `["carmen.reyes@urbannestsolutions.com"]` (recipient-to-self anomaly — bonus data glitch not called out but consistent with the sender anomaly)
- `cc_json`: `["mina.hashimoto@moveops.com", "chloe.vance@moveops.com"]`
- Body opens: "*Hi Carmen, I need your help untangling an active issue on the BrightLoop placement for Simone Richter in Boston.*"
- Signed: "*Thanks, Julian Brooks · Lead Customer Support Specialist · MoveOps*"

→ Body is authored by Julian, not Carmen. OE 4's instruction ("*The body opens 'Hi Carmen' and is signed by Julian, so treat body content as truth. Do not accept the sender field for identity.*") is **grounded and correct**. No downstream OE binds Carmen or Julian identity to this record's sender field — OE 5, 17, 19 all bind Carmen via the contacts record (`contacts_contact_00589cf8404a`) or via the six-question body content, not via this email's sender. **PASS**

## Cited-ID evidence table

| OE | Tool | Cited ID / Value | Universe_Split file | Verified? |
|---|---|---|---|---|
| 1 | contacts_search_contacts | `julian.brooks@moveops.com` (moveops_julian_brooks) | contacts.contacts.json | ✓ |
| 1 | contacts_search_contacts | `mina.hashimoto@moveops.com` (moveops_mina_hashimoto) | contacts.contacts.json | ✓ |
| 2 | get_email_by_id | email_email_6d0501ac647f (SENT, Julian→Simone 4/23, parent=b6ce20dc2587) | email.emails.json | ✓ |
| 3 | get_email_by_id | email_email_b6ce20dc2587 (INBOX, Simone→Mina 4/8, "studio not 1BR") | email.emails.json | ✓ |
| 4 | get_email_by_id | email_email_ab2391d62ab1 (SENT anomaly: sender=carmen, body=Julian, six Qs) | email.emails.json | ✓ |
| 6 | get_email_by_id | email_email_bedc44dbea30 (SENT, Julian→Marcus 4/23, parent=ca010e9c9446) | email.emails.json | ✓ |
| 7 | get_email_by_id | email_email_ca010e9c9446 (SENT from Marcus, "Checking in on my car delivery status") | email.emails.json | ✓ (see advisory 2) |
| 8 | get_email_by_id | email_email_a3ca1b6dd238 (INBOX unread, Road Runner delay, Indy hub, 4/18–20) | email.emails.json | ✓ |
| 9 | airtable_list_bases | appMoveOpsOps001 | airtable.bases.json | ✓ |
| 9 | airtable_get_record | recSimoneRichterBrightloop (Special Reqs silent on unit type) | airtable.records.json | ✓ |
| 10 | airtable_get_record | recMarcusWebbBrightloop (2019 Civic VIN, Road Runner ~$1,100) | airtable.records.json | ✓ |
| 11 | quickbooks_read_invoice | invoice_id 1008 = INV-2026-0308 = $11,350 total | quickbooks.invoices.json | ✓ |
| 11 | (customer) | cust_brightloop BrightLoop Analytics | quickbooks.customers.json | ✓ |
| 12 | conversations_search_messages | ts 1776997200.000000, channel C002, user moveops_mina_hashimoto, thread_ts=null | slack.slack_messages.json + slack.slack_channels.json | ✓ |
| 13 | conversations_replies | channel_id C002, thread_ts 1776997200.000000 | slack.slack_messages.json | ✓ |
| 14 | linear_get_issue | linear_issue_f85be674c9b8 (title matches; assignee Chloe Vance; team_operations; due 2026-04-22) | linear.linear_issues.json | ✓ (labels advisory — see below) |
| 15 | linear_get_issue | linear_issue_c16357d188c6 (Mina audit; priority 1; due 2026-04-22) | linear.linear_issues.json | ✓ |
| 16 | crm_list_engagements | engagement_brightloop_apr2026_relocations (NOTE, createdate 2026-04-02T16:00:00Z) | crm.crm_engagements.json | ✓ |
| 17 | crm_search_contacts | contact_brightloop_simone_richter | crm.crm_contacts.json | ✓ |
| 17 | crm_search_contacts | contact_brightloop_marcus_webb | crm.crm_contacts.json | ✓ |
| 17 | (decoy reject) | contact_ironclad_001 + ext_prospect_ironclad (WRONG Marcus, Ironclad) | crm.crm_contacts.json + contacts.contacts.json | ✓ decoy exists |
| 17 | (decoy reject) | contacts_contact_4d531c818e2a (WRONG Simone, StormCloud) | contacts.contacts.json | ✓ decoy exists |
| 17 | (contacts) | contacts_contact_00589cf8404a (Carmen @ UrbanNest) | contacts.contacts.json | ✓ |
| 18–22, 27 | (sender) | julian.brooks@moveops.com | contacts.contacts.json | ✓ |
| 20, 22 | airtable_update_records | base_id appMoveOpsOps001, table_id tblRelocations01 | airtable.bases.json + airtable.tables.json | ✓ |
| 24 | linear_create_comment | issueId linear_issue_f85be674c9b8 | linear.linear_issues.json | ✓ |
| 25 | crm_create_engagement | company_ids [company_brightloop], contact_ids [contact_brightloop_hr] (= Tessa Moreno) | crm.crm_companies.json + crm.crm_contacts.json | ✓ |
| 26 | calendar_add_calendar_event | attendee julian.brooks@moveops.com; datetimes 2026-04-28T16:30/17:00-07:00 | contacts.contacts.json | ✓ |

## Block issues (Major)
**None.**

## Non-blocking advisories
1. **[OE 12 wording]** OE 12 uses `thread_ts_legacy` as a prose descriptor for the parent ts. This is not a tool-call parameter and OE 13's actual invocation correctly uses `thread_ts`, but the naming could mislead a reader into thinking the parameter is called `thread_ts_legacy`. Suggest renaming the descriptor to plain `thread_ts` for clarity. Not a blocker — no invalid tool call is generated.
2. **[OE 7 characterization]** OE 7 refers to the parent record as "*Marcus's original 'second follow-up: I need an actual ETA for my car' note*". The parent record `email_email_ca010e9c9446` has actual subject `"Checking in on my car delivery status"`. Julian's reply `email_email_bedc44dbea30` is subject-lined `"Re: Second follow-up: I need an actual ETA for my car"`, so the "second follow-up" phrasing is drawn from Julian's reply subject rather than the parent's actual subject. The ID + the OE's intent (establish prior-silence context) are correct; the quoted phrase is slightly loose. Not a blocker.
3. **[OE 8 addressee]** The Road Runner delay email `email_email_a3ca1b6dd238` is addressed to `blessing.okafor@moveops.com`, not to Julian directly. Workspace `search_emails` still surfaces it (shared workspace inbox), so OE 8 is executable, but a real agent will need to search a shared query rather than "my inbox". Not a blocker — OE 8 correctly instructs `search_emails` with an INBOX folder query and does not gate on Julian being the addressee.
4. **[OE 14 labels]** OE 14 asserts `labels brightloop plus service-recovery` on `linear_issue_f85be674c9b8`, but the record's `labels` field is `null` in Universe_Split. Title + assignee (Chloe Vance) + team + due date all match, and OE 24's `linear_create_comment` does not require label existence, so this is advisory only. Consider dropping the labels claim from OE 14 or verifying label seeding.
5. **[Data glitch not flagged]** `email_email_ab2391d62ab1` also has `recipients_json = ["carmen.reyes@urbannestsolutions.com"]` — i.e. addressed-to-self in addition to the sender-field anomaly OE 4 already flags. Not a blocker (OE 4's headline anomaly is captured; downstream identity binding is done via `contacts_search_contacts` and body content), but worth noting for S3 rubric authors so a rubric doesn't grade the recipient list on this email.
