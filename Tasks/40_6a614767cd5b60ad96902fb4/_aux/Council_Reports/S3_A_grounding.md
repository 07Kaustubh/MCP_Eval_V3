# S3 Council A (Grounding) — 7_Rubrics.json

**Task:** Tasks/40_6a614767cd5b60ad96902fb4
**Universe:** StarPM V4
**Deliverable reviewed:** `7_Rubrics.json` (16 Outcome rubrics, read in full)
**Ground truth:** `_aux/Universe_Split/*.json` (primary) + `_aux/Fact_Ledger.json` (cross-check)
**Base-universe dirs consulted as truth:** NONE (per contract)

## Method

Every concrete atom embedded in each of the 16 rubric titles was extracted and located
in the per-task universe split. Line citations are into `_aux/Universe_Split/`. Where the
same row also appears in the merged `Universe_complete_data.json`, the per-service file is
cited as the canonical source. `Fact_Ledger.json` hit counts are noted as a secondary check;
Fact_Ledger is NOT exhaustive, so a `[0]` there is not a grounding failure when the atom is
present in the universe split.

## Per-value grounding table

| Value (rubric atom) | Verdict | Source file : record / line |
|---|---|---|
| Airtable id `recc83c05d889b354` | GROUNDED | `airtable.airtable_records.json:535` — fldUnit `"Unit 14"`, fldTurnStatus `selSched`; notes name Tanya Mitchell, JP coordination, "possession is formally returned". Fact_Ledger [1]. |
| Airtable id `reca8230a8fd9ff51` | GROUNDED | `airtable.airtable_records.json:451` — fldUnit `"Sunset Ridge Unit 14"`, fldTurnStatus `selSched`; notes name Tanya Mitchell + Brooke Phillips. Fact_Ledger [1]. |
| Airtable id `rec94e86a3007dd5e` | GROUNDED | `airtable.airtable_records.json:399` — fldUnit `"Rio Bend - Unit 14"`, fldTurnStatus `selReady`; notes "back to rent-ready condition". Fact_Ledger [1]. |
| email `brooke.phillips@starpm.com` | GROUNDED | `gcalendar.gcalendar_events.json` creator_email (e.g. `Universe_complete_data.json:1363,1479`); also QB bill PrivateNote (`quickbooks.quickbooks_entities.json:275`). Fact_Ledger [5]. |
| email `tanya.mitchell@gmail.com` | GROUNDED | `contacts.contacts.json:211`; `quickbooks.quickbooks_entities.json:1071` (customer proj-2e48c594aab7); ESA request `gmail.gmail_messages.json` (Universe_complete_data.json:3939). Fact_Ledger [5]. |
| amount `$2,132.00` | GROUNDED | `quickbooks.quickbooks_entities.json:275` — bill `QR-2026-0441` `Balance: 2132.0` / `TotalAmt: 2132.0`. Fact_Ledger [1] "2132.00". Confirmed = Balance of bill QR-2026-0441. |
| id `QR-2026-0441` | GROUNDED | `quickbooks.quickbooks_entities.json:275` — DocNumber, entity_type `bill`; lines are "rent arrears - Tanya Mitchell, Unit 14". VendorRef `"Alamo HVAC Services"` is a decoy label (rubric #10 correctly grades on amount+tenant, not vendor). Fact_Ledger [1]. |
| id `EVF-2026-014` | GROUNDED | `airtable.airtable_records.json:395` — fldTicketNumber `"EVF-2026-014"`, "Owner authorization received from Linda Castillo... Owner Approved - Ready to File", fldCompletionDate 2026-06-30. NOTE: Fact_Ledger [0] (absent) — grounded via universe split; Fact_Ledger gap, non-blocking. |
| invoice DocNumber `7214` | GROUNDED | `quickbooks.quickbooks_entities.json:1979` — DocNumber `"7214"`, entity_type `invoice`, CustomerRef Tanya Mitchell, `Balance: 0.0`. Confirms rubric #9 "invoice 7214 showing a zero balance". Fact_Ledger [1]. |
| id `OPS-32` | GROUNDED | `linear.linear_issues.json:127` — id `"OPS-32"`, title "Eviction Hearing - Mitchell, Harris Property", state_id `state_OPS_2` (open). Fact_Ledger [1]. |
| Slack channel `C004` / `#make-ready` | GROUNDED | `slack.slack_channels.json:23` — id `"C004"`, name `"#make-ready"`. Fact_Ledger [1] C004. |
| date `2026-07-06` | GROUNDED (derived) | Computed from `_aux/Universe_Index/today_horizon.json` universe_today `2026-07-01` (Wed). "early next week" → Mon `2026-07-06`. Correct. |
| date `2026-07-07` | GROUNDED (derived) | Same basis; Tue `2026-07-07`. Correct. Rubric #14 offers both Mon/Tue as acceptable. |
| status `Scheduled` / `selSched` | GROUNDED | `airtable.airtable_fields.json:23` — fldTurnStatus singleSelect, choice `{id: selSched, name: Scheduled}`, table `tblMakeReady`. |
| status `selProg` (In Progress) | GROUNDED | `airtable.airtable_fields.json:23` — choice `{id: selProg, name: "In Progress"}`, tblMakeReady. Excluded value exists. |
| status `selReady` (Ready) | GROUNDED | `airtable.airtable_fields.json:23` — choice `{id: selReady, name: Ready}`, tblMakeReady. Excluded value exists. |
| unit `"Sunset Ridge Unit 14"` | GROUNDED | `airtable.airtable_records.json:451` fldUnit (exact); also gcalendar "Sunset Ridge Unit 14" (Universe_complete_data.json:3163). Fact_Ledger [0] string — grounded via split, non-blocking. |
| property `"Rio Bend"` Unit 14 | GROUNDED | `airtable.airtable_records.json:399` fldUnit `"Rio Bend - Unit 14"` (hyphen variant; semantically identical). Fact_Ledger [0] string — grounded via split, non-blocking. |

## Cross-check: the "accept either, bar Rio Bend" rubric (title #1)

- `reca8230a8fd9ff51` — fldUnit **"Sunset Ridge Unit 14"**, selSched, notes explicitly name **Tanya Mitchell** + Brooke/Teresa on account status. → Tanya's Sunset Ridge Unit 14 turn. CONFIRMED.
- `recc83c05d889b354` — fldUnit "Unit 14" (property not embedded in that field), selSched, notes: "Eviction petition for **Tanya Mitchell**... coordinated with the **Justice of the Peace** - make-ready work on this unit cannot begin until the legal process concludes and **possession is formally returned**." Latest record (created + modified 2026-07-01). → same tenant's held Unit 14 turn. CONFIRMED as Tanya's; Sunset Ridge property association derives from sibling `reca8230a8fd9ff51` + the "Sunset Ridge Unit 14" delinquency calendar events, not from its own fldUnit. (Flag for Council B, not a grounding failure.)
- `rec94e86a3007dd5e` — fldUnit **"Rio Bend - Unit 14"**, selReady, notes "back to rent-ready condition. Ticket closed out." → DIFFERENT property (Rio Bend), already rent-ready. CONFIRMED.

Therefore rubric #1 (accept `recc83c05d889b354` OR `reca8230a8fd9ff51`; FAIL on `rec94e86a3007dd5e`/Rio Bend) is **correctly constructed** against the universe. The same Sunset-Ridge-vs-Rio-Bend disambiguation in rubrics #8 is likewise grounded.

## Supporting-atom spot checks (non-listed title atoms)

- "invoice 7214 showing a zero balance" (rubric #9) — `Balance: 0.0` on DocNumber 7214. GROUNDED.
- "eviction filing is owner-approved (EVF-2026-014) but still in coordination with the Justice of the Peace" (rubric #12) — EVF-2026-014 = "Owner Approved - Ready to File"; JP coordination in `recc83c05d889b354` notes + OPS-32 (JP court clerk Patricia Lowe). GROUNDED.
- "approved reasonable-accommodation (emotional support animal)" (rubric #13) — Tanya's ESA request `gmail.gmail_messages.json` (Universe_complete_data.json:3939) + "ESA Lease Addendum Signing" calendar event 2026-05-26 "following approval of Tanya Mitchell's reasonable accommodation request" (Universe_complete_data.json:3347). GROUNDED.

## Notes (non-blocking)

1. `EVF-2026-014`, `"Sunset Ridge"`, `"Rio Bend"`, `"make-ready"` are absent from `Fact_Ledger.json` (hit count [0]) but present in the universe split. This is a Fact_Ledger completeness gap, not a grounding defect. Consider backfilling the ledger.
2. `recc83c05d889b354.fldUnit` is literally `"Unit 14"` (no property token). Its Sunset Ridge property association is inferred from the tenant (Tanya Mitchell) + sibling record + calendar. Grounding holds; flagged for Council B coherence review.
3. Bill `QR-2026-0441` carries a decoy `VendorRef "Alamo HVAC Services"`; the $2,132.00 is genuine Tanya Mitchell Unit 14 rent arrears (line items). Rubric #10 evidence correctly instructs grading on amount+tenant, not vendor label. Landmine handled correctly.

## Verdict

VERDICT: GO — all 17 requested values and every concrete title atom across the 16 rubrics are grounded in the per-task universe split. No UNGROUNDED values. No BLOCK.
