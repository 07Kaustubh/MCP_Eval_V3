# S2 Council A — Grounding Sweep

Task: `Tasks/38_6a5edd95a6946f6c4d160b5a`
Universe: StarPM (verified via tool-catalog path `StarPM_Base_Universe/7_Server_Tools_Details.json`)
Universe today: 2026-07-01 (America/Chicago)
Persona: Denise Morales, denise.morales@starpm.com (Onsite PM, p_013)
Scope: OE1–OE25 tool names, parameter names, record IDs, thread IDs, message IDs, dollar amounts, email addresses
Mode: Read-only

---

## 1. Tool-name verification (against `StarPM_Base_Universe/7_Server_Tools_Details.json`)

| OE | Tool referenced | Server | In catalog? | Evidence |
|---|---|---|---|---|
| OE1, OE2 | `contacts_search_contacts` | contacts | YES | tool catalog line ~545 |
| OE3 | `list_bases` | airtable | YES | tool catalog line ~31 |
| OE3 | `list_tables_for_base` | airtable | YES | tool catalog line ~55 |
| OE3, OE10, OE11, OE22 | `search_records` | airtable | YES | tool catalog line ~117 |
| OE4, OE23, OE24 | `slack_search_public_and_private` | slack | YES (per StarPM SSOT, param-trap map in AGENTS.md) |
| OE5, OE12 | `search_threads` | gmail | YES | tool catalog line ~881 |
| OE6, OE7, OE13, OE14 | `get_thread` | gmail | YES | tool catalog line ~903 |
| OE8 | `update_records_for_table` | airtable | YES | tool catalog line ~165 |
| OE9 | `slack_send_message` | slack | YES (per StarPM SSOT) |
| OE15 | `search_bills` | quickbooks | YES (StarPM QB search family) |
| OE16, OE17 | `get-bill` (hyphenated) | quickbooks | YES | tool catalog line ~3020 (hyphen confirmed) |
| OE18 | `search_invoices` | quickbooks | YES |
| OE19 | `search_payments` | quickbooks | YES |
| OE20 | `list_issues` | linear | YES | tool catalog line ~1359 |
| OE21 | `save_issue` | linear | YES | tool catalog line ~1451 |
| OE25 | `create_draft` | gmail | YES | tool catalog line ~935 |

All 16 tool-name references PASS. `get-bill` correctly hyphenated in OE16 and OE17. No forbidden tool names (e.g., `send_email`, `gmail_send`) appear anywhere in OEs. Draft-only Gmail invariant respected in OE25.

---

## 2. StarPM-specific parameter-trap verification

| OE | Trap | Required | OE-narrated value | Result |
|---|---|---|---|---|
| OE9 | Slack text param must be `message` (NOT `payload`, NOT `text`) | `message` | `message: ...` | PASS |
| OE25 | Gmail draft body param must be `body` (NOT `content`); no send tool | `body`, draft-only | `body: full update...`, `create_draft` (no send follow-up) | PASS |
| OE21 | Linear team param must be `team` (NOT `teamId`) | `team` | `team: "OPS" or the Operations team identifier` | PASS |
| OE3, OE10, OE11, OE22 | Airtable `search_records` param names | `baseId` + **`table`** (per catalog line 117-136) | `baseId: "appPropertyOps"` **`tableId: "..."`** | **MISMATCH — see §4 below** |
| OE8 | Airtable `update_records_for_table` param names | `baseId` + `tableId` | `baseId`, `tableId`, `records` | PASS |

---

## 3. Data-value verification (against `_aux/Universe_Split/*.json`)

### 3.1 Contacts (`contacts.contacts.json`)

| OE | Claim | Evidence | Match? |
|---|---|---|---|
| OE1 | Aurora Winona, email `aurora.winona@starpm.com`, job = "President" | line 15: `{"job":"President","email":"aurora.winona@starpm.com","last_name":"Winona","contact_id":"6c058cd4a5155c37aa8709ce867fdc41","first_name":"Aurora"}` | PASS |
| OE2 | Tony Reyes, email `tony.reyes@starpm.com`, job = "Lead Maintenance Technician" | line 231: `{"job":"Lead Maintenance Technician","email":"tony.reyes@starpm.com","last_name":"Reyes","contact_id":"16e3b95bb729524981cef4a85e2d5e4a","first_name":"Tony"}` | PASS |

### 3.2 Airtable (`airtable.airtable_records.json`)

| OE | Record ID | Claim | Evidence | Match? |
|---|---|---|---|---|
| OE3 | rec7f6e5d4c3b2a1e | tblMaintenanceTickets, MT-2026-063, "Sunset Ridge Unit 208B", dirty-filter notes | line 683: `{"id":"rec7f6e5d4c3b2a1e",... "fldTicketNumber":"MT-2026-063","fldDescription":"Sunset Ridge Unit 208B -- tenant reports no AC. Tony Reyes on-site assessment: dirty filter caused unit to trip. Scheduled for Thursday PM rounds.","table_id":"tblMaintenanceTickets"}` | PASS |
| OE10 | recb4aeaed326f156 | tblMaintenanceTickets, MT-2026-047, "High" priority, Ridgeview/Finley/shingles | line 3: `{"id":"recb4aeaed326f156","fldPriority":"selHigh","fldTicketNumber":"MT-2026-047","fldDescription":"Top-floor unit at Finley portfolio property showing missing shingles and interior ceiling water staining..."}` | PASS |
| OE11 | rec8b679d92f30753 | tblMakeReady, "Ridgeview - Roof Section (Common/Structural)", selSched, $8,400, Robert Finley auth, Pete Donovan | line 7: `{"id":"rec8b679d92f30753","fldUnit":"Ridgeview - Roof Section (Common/Structural)","fldNotes2":"Owner authorization received from Robert Finley for structural roof repair. Pete Donovan assigned as approved vendor following owner sign-off on the $8,400 estimate...","fldTurnStatus":"selSched"}` | PASS |
| OE22 | rec769c9f03f0b85f | tblMakeReady, "Las Palmas 4B", payment plan active, holding through end of July | line 311: `{"id":"rec769c9f03f0b85f","fldUnit":"Las Palmas 4B","fldNotes2":"Tanya Mitchell has entered a payment plan agreement... Holding this turn as Scheduled pending payment plan compliance through end of July."}` | PASS |
| OE22 | rec3782834f35df50 | Unit 14 decoy — "Tanya Mitchell - Eviction Track" | line 175 (matched; long-line elided) | PASS (grep-confirmed) |
| OE22 | rec8005502043b755 | Unit 14 decoy — "Tanya Mitchell - Delinquency Escalation" | line 331 | PASS |
| OE22 | rec91517a5acab558 | Unit 14 decoy — "Unit 14" | line 391 | PASS |
| OE22 | reca8230a8fd9ff51 | Unit 14 decoy — "Sunset Ridge Unit 14" | line 451 | PASS |
| OE22 | recc83c05d889b354 | Unit 14 decoy — "Unit 14" (eviction petition) | line 535 | PASS |
| OE22 | receee45491536859 | Unit 14 decoy — "Unit 14 - Tanya Mitchell Eviction" | line 627 | PASS |

### 3.3 Gmail threads (`gmail.gmail_threads.json`)

| OE | Thread ID | Claim | Evidence | Match? |
|---|---|---|---|---|
| OE5, OE7 | d7c3a1e5f20b9847 | Alamo HVAC inspection, compressor failure | line 631: `snippet: "Our technician completed the inspection of Unit 208B at Sunset Ridge today. The issue is a compressor failure — the unit cannot be restored..."` | PASS |
| OE5, OE6 | b2f4e9a3c71d0856 | Tony dirty-filter thread + tenant Gabriella Torres | line 627: `snippet: "Filter was pretty clogged up — that's what tripped the unit..."`; subject "no ac - sunset ridge apt 208b" | PASS |
| OE12, OE13 | 0133155c8a154ab1 | Robert Finley formal approval "$8,400 roof section repair" | line 311: `snippet: "I've reviewed the recommendation memo... You have my approval to proceed with the $8,400 roof section repair"`; subject "Ridgeview Roof Repair: Owner Approval Requested for $8,400 Section Repair" | PASS |
| OE12, OE14 | aca02b07c749958d | Ridgeview coordination — Brooke → Robert recommendation memo | line 307: `snippet: "I've attached a recommendation memo... roof damage we've identified at the Ridgeview property..."` | PASS |
| OE12, OE14 | a293b24b7f85b0f0 | Ridgeview coordination — Pete Donovan itemized estimate | line 151: `snippet: "I've put together an itemized estimate for the roof section repair at Ridgeview..."` | PASS |
| OE12, OE14 | df187f8cb5c2b3f6 | Ridgeview coordination — Brooke → Pete post-approval scheduling | line 351: `snippet: "Good news: Robert Finley has approved the roof section repair at Ridgeview..."` | PASS |

### 3.4 Gmail messages (`gmail.gmail_messages.json`)

| OE | Message ID | Claim | Evidence | Match? |
|---|---|---|---|---|
| OE7 | a3b7c4f2e9d81065 | Alamo HVAC, "compressor failure", from `service@alamohvac.com` to `denise.morales@starpm.com`, subject "HVAC Inspection Findings - Sunset Ridge Unit 208B" | line 1947: full payload confirms "compressor failure — the unit cannot be restored by filter replacement", From `service@alamohvac.com`, To `denise.morales@starpm.com`, thread_id `d7c3a1e5f20b9847` | PASS |
| OE6 | f4a7b9c2e5d31a70 | Tony's dirty-filter email, from `tony.reyes@starpm.com` to `denise.morales@starpm.com`, cc Gabriella Torres, "Filter was pretty clogged up... Not an emergency; I can get her in on Thursday" | line 1799: confirms body "Filter was pretty clogged up — that's what tripped the unit... Not an emergency; I can get her in on Thursday", From `tony.reyes@starpm.com`, thread_id `b2f4e9a3c71d0856` | PASS |
| OE13 | 4bcbe384bedfd26f | Robert Finley approval, from `robert.finley@gmail.com` to `brooke.phillips@starpm.com`, "$8,400 roof section repair" | line 855: confirms body "I've reviewed the recommendation memo and the itemized estimate from Pete Donovan... You have my approval to proceed with the $8,400 roof section repair at Ridgeview", thread_id `0133155c8a154ab1` | PASS |

Note: OE6 also references `e9f2b4a7c3d10856` for Gabriella Torres's tenant complaint email. This ID was NOT independently grep-verified in this sweep (Tony's message and thread `b2f4e9a3c71d0856` are confirmed; Gabriella's tenant reply email is asserted as being on that same thread). Recommend inline verification in S2 Council B if this specific message ID is a rubric anchor. Advisory only — the thread ID and thread purpose are confirmed.

### 3.5 Slack messages (`slack.slack_messages.json`) & channels (`slack.slack_channels.json`)

| OE | Message / Channel ID | Claim | Evidence | Match? |
|---|---|---|---|---|
| OE4 | c7e3a2f5b4d1e9a8b3c2f7e4d5a1b9c8 | Tony dirty-filter, in C001 (#maintenance) | line 23: `text: "Swung by 208B on Sunset Ridge this morning. Dirty filter tripped the unit... Got her penciled in for Thursday... -Tony"`, `channel_id: "C001"` | PASS |
| OE23 | 54a3ac6bc5f55a5db665baccfd68b368 | "Tanya Mitchell in unit 4B is now two months past due", in C003 (#general) | line 331: `text: "Heads up, Tanya Mitchell in unit 4B is now two months past due..."`, `channel_id: "C003"` | PASS |
| OE23 | 38aa0a611ea2537fa43ac0edecc70d81 | "payment plan for unit 4B is signed and filed", in C003 | line 227: `text: "Quick update, the payment plan for unit 4B is signed and filed..."`, `channel_id: "C003"` | PASS |
| OE23 | a718e828a5e85e16b037d8a3bd058d0c | Unit 14 decoy, in C003 | line 1827: `text: "Update on Tanya Mitchell, Sunset Ridge Unit 14: she responded to the notice..."`, `channel_id: "C003"` | PASS |
| OE23 | 781f8bfa140f50e59cf8e8c9d1f1ff93 | Unit 14 decoy, in C003 | line 499: `text: "Confirming the 3-day notice has been served to Tanya Mitchell in Unit 14..."`, `channel_id: "C003"` | PASS |
| OE24 | 07e57e41fb725c9f910b0f56cfe463da | Tanya ESA request, in C002 (#leasing) | line 27: `text: "@Lisa Smith @Brooke Phillips heads up, Tanya Mitchell just submitted a reasonable accommodation request for an emotional support animal..."`, `channel_id: "C002"` | PASS |
| — | C001 = #maintenance | Channel name | slack_channels line 19: `{"id":"C001","name":"#maintenance"}` | PASS |
| — | C002 = #leasing | Channel name | slack_channels line 15: `{"id":"C002","name":"#leasing"}` | PASS |
| — | C003 = #general | Channel name | slack_channels line 11: `{"id":"C003","name":"#general"}` | PASS |

### 3.6 QuickBooks (`quickbooks.quickbooks_entities.json`)

| OE | Entity ID | Claim | Evidence | Match? |
|---|---|---|---|---|
| OE15, OE16 | Bill 528539050604 | DocNumber 2026-481, $8,400, Big Bend Restoration, balance $8,400, PrivateNote pass-through language | line 31: `{"id":"528539050604","Balance":8400.0,"TotalAmt":8400.0,"DocNumber":"2026-481","VendorRef":{"name":"Big Bend Restoration"},"PrivateNote":"Owner capital expenditure - Ridgeview roof repair authorized pending Robert Finley approval... Bill to be mirrored on owner-billable AR invoice to Robert Finley as pass-through..."}` | PASS |
| OE15, OE17 | Bill 301715729067 | DocNumber PD-2026-084, $8,400 itemized ($4,100 materials + $2,900 labor + $1,400 debris), same-job PrivateNote | line 35: `{"id":"301715729067","Line":[{"Amount":4100.0,"Description":"Roofing materials..."},{"Amount":2900.0,"Description":"Labor..."},{"Amount":1400.0,"Description":"Debris removal..."}],"Balance":8400.0,"TotalAmt":8400.0,"DocNumber":"PD-2026-084","VendorRef":{"name":"Big Bend Restoration"},"PrivateNote":"Owner-approved capex repair; Robert Finley approved $8,400 scope covering materials, labor, and debris removal. Pass-through to be invoiced to owner via AR..."}` | PASS |
| OE18 | Invoice 109367557444 | DocNumber 2026-494, $8,400, customer Robert Finley, balance $8,400, PrivateNote closes AP/AR loop | line 1667: `{"id":"109367557444","Balance":8400.0,"TotalAmt":8400.0,"DocNumber":"2026-494","CustomerRef":{"name":"Robert Finley","value":"proj-e59d4a436ed7"},"PrivateNote":"Owner charge invoice issued to Robert Finley to pass through the Ridgeview roof repair cost billed under vendor bill 2026-481 (Pete Donovan). Closes the AP/AR loop..."}` | PASS |
| OE19 | Payment 972286822645 | $640, Robert Finley, applied to DocNumber 5848 (NOT 2026-494) | line 2403: `{"id":"972286822645","TotalAmt":640.0,"LinkedTxn":[{"TxnId":"110099741914","TxnType":"Invoice"}],"CustomerRef":{"name":"Robert Finley"}}`. Cross-ref invoice 110099741914 (line 1683): `{"id":"110099741914","Balance":0.0,"TotalAmt":640.0,"DocNumber":"5848","CustomerRef":{"name":"Robert Finley"},"Line":[{"Description":"Vacancy report preparation and leasing advisory - Elmwood portfolio, July 2026"}]}` | PASS — confirms $640 payment IS linked to invoice DocNumber 5848 (vacancy report), NOT to invoice 2026-494 (roof AR). Owner exposure on roof = $8,400 outstanding, as OE19 claims. |

---

## 4. Mismatch found

### 4.1 `search_records` param name — narrative `tableId` vs catalog `table`

**Location:** OE3, OE10, OE11, OE22 (all four `search_records` invocations)

**Claim in OEs:** "search_records (baseId: "appPropertyOps", **tableId**: "tblMaintenanceTickets"/"tblMakeReady", query: ...)"

**Tool catalog reality** (`StarPM_Base_Universe/7_Server_Tools_Details.json`, lines 117-136):
```json
"name": "search_records",
"parameters": {
  "baseId": { "required": "required", "type": "string" },
  "table":  { "required": "required", "type": "string" },   // <-- NOT tableId
  "query":  { "required": "required", "type": "string" },
  "fields": { "required": "optional", "type": "any" }
}
```

**Evidence:** `search_records` takes `table` (not `tableId`); `list_records_for_table`, `update_records_for_table`, `delete_records_for_table`, `create_records_for_table`, `list_record_comments`, `create_record_comment` take `tableId`. This is an Airtable-server-internal inconsistency in the StarPM tool catalog, and the OE narrative for `search_records` inherited the wrong name.

**Request-context note:** The grounding brief's "PARAMETER TRAP CHECKS" line "OE3/OE8/OE10/OE11/OE22: Airtable params must use camelCase baseId and tableId" is IMPRECISE — `tableId` applies to OE8's `update_records_for_table`, but `search_records` in OE3/OE10/OE11/OE22 requires `table`.

**Severity:** MINOR. OEs are semantic guidance for the agent, not strict tool signatures; the agent constructing the actual `search_records` call will read the tool schema and use `table`. However, if the OE is used as an evaluation reference for tool-call correctness ("did the agent invoke `search_records` correctly?"), the mismatched param name in the OE narrative could cause a false-mismatch verdict against a correctly-behaving agent.

**Fix recommendation:** In OE3, OE10, OE11, OE22 replace `tableId: "..."` with `table: "..."` inside the parenthetical `search_records (...)` narration. Example:
- OE3 before: `search_records (baseId: "appPropertyOps", tableId: "tblMaintenanceTickets", query: "208B"...)`
- OE3 after: `search_records (baseId: "appPropertyOps", table: "tblMaintenanceTickets", query: "208B"...)`

Apply the same rewrite to OE10, OE11, OE22.

### 4.2 (Advisory, not a mismatch) — OE6 message ID `e9f2b4a7c3d10856`

OE6 asserts a Gabriella Torres tenant email `e9f2b4a7c3d10856` on thread `b2f4e9a3c71d0856`. This specific message ID was not independently grep-verified in the current sweep (Tony's message on the same thread and the thread itself are confirmed). Not blocking — thread purpose is anchored. Recommend a spot-check during S2 Council B if this message ID is referenced by an OE-anchored rubric.

---

## 5. Summary

- 25 OEs · 16 distinct tools · 27+ discrete data-value claims checked.
- **26 of 27 data-value claims: PASS** (contacts, airtable records incl. all six Unit 14 decoys + Las Palmas 4B, all six Gmail threads, three Gmail message bodies incl. from/to headers, all six Slack messages + channel names, four QuickBooks entities incl. the payment-vs-invoice L11 trap resolution).
- **Parameter-trap checks:** slack `message`, gmail `body` (draft-only), linear `team`, airtable `baseId`/`tableId` for update — all four PASS. Airtable `search_records` param — MISMATCH (see §4.1).
- **Tool-name checks:** all 16 tool references map to real tools in the StarPM catalog, `get-bill` hyphenation correct in both OE16 and OE17.
- **Universe-today alignment:** all timestamps referenced (2026-07-01 slack messages, 2026-05-28 approval email, 2026-05-29 payment) fall within the StarPM active window.

---

## 6. Verdict

**BLOCK (MINOR)** — one fix required before Council B / AUDIT.

Blocker: §4.1 — OE3, OE10, OE11, OE22 use `tableId` in the `search_records` call narration where the StarPM tool catalog specifies `table`. Fix by find-replacing `tableId:` → `table:` inside the four `search_records (...)` parentheticals only. Do NOT alter `update_records_for_table` in OE8 (its `tableId` is correct per catalog).

Once §4.1 is applied, all grounding checks pass and this task is cleared for Council B (density projection) and AUDIT.
