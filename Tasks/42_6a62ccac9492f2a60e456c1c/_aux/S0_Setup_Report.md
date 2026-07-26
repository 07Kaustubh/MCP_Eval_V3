# S0 Setup Report — Tasks/42_6a62ccac9492f2a60e456c1c

## Universe
- **Detected universe:** `starpm` (Star Property Management, LLC — V4 framework)
- **Base path:** `StarPM_Base_Universe/` · Tool catalog: `7_Server_Tools_Details.json`
- Detection cached to `_aux/Universe.txt`.

## Persona
- **Name:** Brooke Phillips
- **Role:** Apartment Property Supervisor (persona id `p_000`, `brooke.phillips@starpm.com`)
- **Seniority:** Senior · Department: Portfolio Operations
- Deepest scripted footprint in the universe (69 actions across 23 scenarios); present in 26 of 27 scenarios.

## Business Function
- **Portfolio Coordination & Owner Relations** (StarPM BF #2, 20% weight)

## Per-task data
- **Data hash (sha256):** `06f7535a3357ae4900c884fbc76d5e3566f27bf1aef02e47ab6c7ccac8a749a3`
- **Record totals:** 3892 records across 33 service tables (8 services: airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack).
- Heaviest tables: quickbooks_entities (625), slack_messages (580), gcalendar_events (565), gmail_messages (484), hubspot_associations (388), linear_issues (230), airtable_records (170).

## Fact Ledger atom surface
- emails 206 · amounts 403 · dates 192 · airtable_record ids 170 · linear_issue ids 230 · linear_comment ids 48 · hubspot_object ids 183 · slack_channel ids 8 · slack_user ids 61 · invoice ids 504 · personas 61.
- `entities` (0) and `fiscal_periods` (0) are Brookfield-GL concepts — legitimately absent in the property-management (StarPM) universe.

## Horizon
- **Universe today:** 2026-07-01 (America/Chicago)
- **last_event_timestamp_seen:** 2026-12-30T12:40:00-05:00
- **records_dated_after_today: 59** — with universe today = 2026-07-01, 59 records carry dates after today (latest 2026-12-30). Expected for a property-management universe: forward-scheduled Google Calendar events (owner meetings, ops sync, preventive-maintenance pushes) and upcoming invoice/AP due dates. Not a defect at S0; HARDNESS must still resolve any relative-date windows against real in-window data.

## V4 injection gate
- `9_Universe_inject.sql` is the **comment-only template header** (no executable INSERT/UPDATE statements). `validate.py --phase injection` → **PASS** (0 fails, 0 warns; 4 council-deferred semantic notes). No injected scenario at S0 — this task is built from levers already present in the per-task universe (hard rule 4). If injection SQL is added later, re-run the injection gate; the difficulty composite (>= 3.5) is council-judged at FINAL.

## Exit status
- PersonaBrief.txt written · Universe_Split (33 files) written · Universe_Index (5 files + graph_report.md) written · Fact_Ledger.json written · Feasible_Surface.json (15 tables / 19 enum cols) written · S0_Setup_Report.md written · Verification_s0.md written.
- **Next:** `PIPELINE HARDNESS — Tasks/42_6a62ccac9492f2a60e456c1c` in a fresh chat.
