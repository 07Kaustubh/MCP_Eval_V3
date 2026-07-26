# S0 Setup Report — Task 43_6a62ccaf5853030245ac9d53

## Universe
- **Universe:** `starpm` (Star Property Management, LLC — San Antonio TX multifamily property manager, domain `starpm.com`) — auto-detected, written to `_aux/Universe.txt`.
- **Framework:** V4.

## Persona
- **Name:** Carlos Mendez
- **Role:** Onsite Property Manager (`p_009` · `carlos.mendez@starpm.com`)
- **Seniority:** Mid · Department: Property Operations
- **Scripted footprint:** 33 actions across 11 scenarios — most-rooted Onsite PM after Brooke. Anchors Mesa Vista and Las Palmas; leads two Cat 1 make-ready scenarios + two Cat 1 maintenance-response scenarios (carpet, water-heater).
- Grounded in per-task data across contacts, airtable_users, slack_users, linear_users, hubspot_owners/objects, plus 341 gcalendar-event and 417 gmail-message hits.

## Business Function
- **Property Operations** (from `1_Business_Function.txt`) — StarPM BF 1 (32% portfolio weight). Matches Carlos's persona-brief business function (`1 · Property Operations`).

## Per-task data
- **Data hash (sha256 of `3_UniverseDataForThisTask.json`):** `06f7535a3357ae4900c884fbc76d5e3566f27bf1aef02e47ab6c7ccac8a749a3`
- **Record totals:** 3892 records across 33 per-service files spanning 8 services (airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack). See `_aux/Universe_Index/service_inventory.md` for the full breakdown. Heaviest surfaces: quickbooks_entities 625, slack_messages 580, gcalendar_events 565, gmail_messages 484, hubspot_associations 388, linear_issues 230, airtable_records 170.
- **Fact Ledger atoms:** emails 206 · amounts 403 · dates 192 · airtable-record ids 170 · linear-issue ids 230 · linear-comment ids 48 · hubspot-object ids 183 · slack-channel ids 8 · slack-user ids 61 · invoice ids 504 · personas 61.

## Universe horizon
- **Universe today:** 2026-07-01 (America/Chicago).
- **last_event_timestamp_seen:** 2026-12-30T12:40:00-05:00.
- **NOTE (records after today):** `records_dated_after_today = 59` against the 2026-07-01 universe today. These are legitimate forward-dated records (future fiscal periods / upcoming due dates / scheduled calendar events) per `today_horizon.json`; not a data defect. HARDNESS/S1 must resolve any relative-date phrasing against 2026-07-01 and confirm the resolved window has data before relying on future-dated rows.

## V4 injection
- `9_Universe_inject.sql` is the comment-only template header (0 executable statements); `4_Changelog.json` is empty `[]`. This is a **no-injection** task — hardness will be built on levers already present in the per-task universe (Hard rule 4).
- `validate.py --phase injection` → **PASS** (SKIP; deterministic layer has no injected atoms to check). Report: `_aux/Validator_Reports/injection.md`.

## Exit status
- `PersonaBrief.txt` written (non-empty). ✅
- `_aux/Universe_Split/` populated (33 per-service JSON files + `data_hash.txt`). ✅
- `_aux/Universe_Index/` has all 5 summary files + `graph_report.md`. ✅
- `_aux/Fact_Ledger.json`, `_aux/Feasible_Surface.json` written. ✅
- `_aux/S0_Setup_Report.md`, `_aux/Verification_s0.md` written. ✅

Next: `PIPELINE HARDNESS — Tasks/43_6a62ccaf5853030245ac9d53` (fresh chat).
