# S0 Setup Report — Tasks/25_6a366bc27d66eaedcae82ab4

## Persona

- **Name:** George McAdam
- **Role:** Accounts Senior *(primary persona — 20 scenarios universe-wide)*
- **Brief:** `PersonaBrief.txt` (copied verbatim from `Brookfield_Base_Universe/2_Persona_Briefs.md`)

## Business function

- **Name:** Accounting Operations (from `1_Business_Function.txt`)

## Per-task data hash

- `sha256: 7f8d87538304f5d18a21de4a1d4580b430afde4570b8203569d91744f29d9446`
- Source: `_aux/data_hash.txt`

## Universe scale

- **Total records:** 25,937 across 42 sources (full per-source breakdown in `_aux/Universe_Index/service_inventory.md`)
- **High-density sources (≥1000):**
  - `blackline.blackline_audit_trail` — 4,414
  - `slack.slack_messages` — 2,545
  - `sap_subledger.subledger_transactions` — 2,752
  - `oracle_gl.ogl_journal_entries` — 2,388
  - `records_vault.rv_document_versions` — 2,356
  - `records_vault.rv_documents` — 2,007
  - `email.emails` — 1,379
  - `sap_subledger.depreciation_schedule` — 1,499
- **Exception / control surfaces:** `blackline.blackline_exceptions` — 24, `blackline.blackline_reconciliations` — 683, `blackline.blackline_close_tasks` — 396
- **AP / vendor surfaces:** `sap_subledger.ap_invoices` — 987, `sap_subledger.prepaid_schedules` — 75, `sap_subledger.prepaid_periods` — 498
- **People / channels:** `contacts.contacts` — 63, `slack.slack_users` — 57, `slack.slack_channels` — 11, `linear.linear_users` — 44

## Fact ledger atom counts (`_aux/Fact_Ledger.json`)

| Atom | Count |
|---|---:|
| emails | 68 |
| amounts | 6,461 |
| dates | 467 |
| id_je | 2,359 |
| id_exception | 24 |
| id_recon | 682 |
| id_doc | 2,007 |
| id_vendor | 1,105 |
| id_apinv | 987 |
| id_linear_issue | 15 |
| id_reminder | 53 |
| id_conversation | 202 |
| id_airtable_record | 28 |
| id_calendar_event | 31 |
| id_slack_channel | 11 |
| id_contact | 63 |
| id_persona | 28 |
| entities | 3 |
| personas | 63 |
| fiscal_periods | 36 |

## Universe horizon

- **Universe today:** `2026-06-12` (`America/New_York`)
- **Last event timestamp seen:** `2026-06-30`
- **Records dated after today:** **15** — universe today is 2026-06-12; the post-today records are legitimate (status=future fiscal periods + upcoming AP due dates per `today_horizon.json` note). No corrective action needed.

## Artifacts produced

- `PersonaBrief.txt`
- `_aux/Universe_Split/` — 42 per-service JSONs + `data_hash.txt`
- `_aux/Universe_Index/` — `service_inventory.md`, `entities_personas.md`, `key_facts.md`, `today_horizon.json`, `accounts_per_entity.md`, `graph_report.md`
- `_aux/Fact_Ledger.json`
- `_aux/S0_Setup_Report.md` (this file)

## Exit criteria — met

- [x] `PersonaBrief.txt` exists, non-empty, verbatim from base persona briefs
- [x] `_aux/Universe_Split/` populated (42 services)
- [x] `_aux/Universe_Index/` contains all 5 summary files + `graph_report.md`
- [x] `_aux/S0_Setup_Report.md` written

## STOP gate

S0 setup complete. Open a fresh chat and invoke:

```
PIPELINE HARDNESS — Tasks/25_6a366bc27d66eaedcae82ab4
```
