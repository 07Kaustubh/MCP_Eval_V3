# S0 Setup Report — Task 28_6a390e6b331d1ed9022a9f7c

## Persona
- **Name:** Anaya Wallace
- **Role:** Trainee Accountant
- **Authoring categories:** 1, 2, 7
- **Anchor work surface:** AP escalation family (5 of 8), FX month-end JE preparation, recon currency refresh isolation, AR aging buckets. Standing partner with Owen Mercer (AP Specialist). Managed by Harry Marks; pairs with Daniel Jones on AP triage.

## Business Function
- **Name:** Bookkeeping

## Per-task data
- **Input file:** `Tasks/28_6a390e6b331d1ed9022a9f7c/3_UniverseDataForThisTask.json`
- **sha256:** `afecc01fc55fe6bca6e25162d85ffe7190a3e7669831e299bf824980ef73f13c`
- **Total records:** 25,937 across 42 sources

### Record-count highlights (from `service_inventory.md`)
- `blackline.blackline_audit_trail`: 4,414
- `slack.slack_messages`: 2,545
- `sap_subledger.subledger_transactions`: 2,752
- `oracle_gl.ogl_journal_entries`: 2,388
- `records_vault.rv_document_versions`: 2,356
- `records_vault.rv_documents`: 2,007
- `sap_subledger.depreciation_schedule`: 1,499
- `email.emails`: 1,379
- `sap_subledger.ap_invoices`: 987
- `messaging.messages`: 990
- `blackline.blackline_reconciliations`: 683
- `sap_subledger.prepaid_periods`: 498
- `blackline.blackline_close_tasks`: 396
- `oracle_gl.ogl_subledger_feed_runs`: 242
- `oracle_gl.ogl_accounts`: 245
- `sap_subledger.fixed_assets`: 240
- `blackline.blackline_review_notes`: 218
- `records_vault.rv_access_grants`: 184
- `blackline.blackline_archived_reconciliations`: 168
- `contacts.contacts`: 63
- `slack.slack_users`: 57
- `reminder.reminders`: 53
- `calendar.events`: 51
- `linear.linear_users`: 44
- `oracle_gl.ogl_fiscal_periods`: 36
- `linear.linear_issues`: 30
- `linear.linear_comments`: 25
- `blackline.blackline_exceptions`: 24
- `airtable.records`: 21
- `slack.slack_channels`: 11
- `linear.linear_projects`: 8
- `sap_subledger.prepaid_schedules`: 75
- `sap_subledger.lease_schedules`: 6
- `linear.linear_teams`: 6
- `airtable.tables`: 5
- `records_vault.rv_retention_policies`: 4
- `records_vault.rv_classifications`: 3
- `airtable.bases`: 2
- `oracle_gl.ogl_subledger_feeds`: 22
- `linear.linear_team_memberships`: 67
- `messaging.conversations`: 202

## Universe horizon
- **universe_today:** 2026-06-12 (America/New_York)
- **last_event_timestamp_seen:** 2026-06-30
- **records_dated_after_today:** 15 — legitimate per `today_horizon.json` note (future fiscal-period status rows and upcoming AP due-dates).

## Fact Ledger atom counts
- emails: 68 | amounts: 6,461 | dates: 467
- id_je: 2,359 | id_exception: 24 | id_recon: 682 | id_doc: 2,007
- id_vendor: 1,105 | id_apinv: 987
- id_linear_issue: 15 | id_reminder: 53 | id_conversation: 202
- id_airtable_record: 28 | id_calendar_event: 31 | id_slack_channel: 11
- id_contact: 63 | id_persona: 28
- entities: 3 | personas: 63 | fiscal_periods: 36

## Exit-criteria checklist
- [x] `PersonaBrief.txt` written (non-empty, verbatim from `Brookfield_Base_Universe/2_Persona_Briefs.md`).
- [x] `_aux/Universe_Split/` populated (42 per-service JSON files).
- [x] `_aux/Universe_Index/` populated: `service_inventory.md`, `entities_personas.md`, `key_facts.md`, `today_horizon.json`, `accounts_per_entity.md`, `graph_report.md`.
- [x] `_aux/Fact_Ledger.json` written.
- [x] `_aux/S0_Setup_Report.md` written (this file).

## Horizon flag
`records_dated_after_today = 15` against universe today `2026-06-12` — within the expected envelope (future fiscal-period rows + upcoming AP due-dates per `today_horizon.json` note). No anomaly to escalate.
