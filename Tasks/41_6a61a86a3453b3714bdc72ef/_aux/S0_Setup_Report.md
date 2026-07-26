# S0 Setup Report — Tasks/41_6a61a86a3453b3714bdc72ef

## Universe
- **Detected universe:** `starpm` (Star Property Management, LLC — San Antonio TX multifamily property manager, V4 framework)
- **Base path:** `StarPM_Base_Universe/` · Tool catalog `7_Server_Tools_Details.json`

## Persona
- **Name / role:** Patricia Nguyen · Onsite Property Manager *(reassigned from Lisa Smith p_002 at S1.5 — persona-scope correction, see `_aux/Linter_Decision.md`)*
- **Persona id / email:** `p_010` · `patricia.nguyen@starpm.com`
- **Seniority / dept:** Mid · Property Operations (BF1 unchanged)
- **Scripted footprint:** 26 actions across 7 scenarios (deeply rooted; the rent/eviction anchor); leads `rent_late_first_notice`, `rent_delinquency_payment_plan`, `rent_3day_notice_pay_or_quit`, `eviction_filing_prep`, `eviction_court_coordination`.
- Confirmed against `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` (positive whitelist match).

## Business function
- **Property Operations** (from `1_Business_Function.txt`) — BF1 in the StarPM registry (32% weight).

## Per-task data
- **data hash (sha256):** `06f7535a3357ae4900c884fbc76d5e3566f27bf1aef02e47ab6c7ccac8a749a3`
- **Record totals:** 3892 records across 33 service-tables (8 services: airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack).
- Densest sources: `quickbooks.quickbooks_entities` 625 · `gcalendar.gcalendar_events` 565 · `slack.slack_messages` 580 · `gmail.gmail_messages` 484 · `hubspot.hubspot_associations` 388 · `linear.linear_issues` 230 · `airtable.airtable_records` 170.

## Time horizon
- **Universe today:** 2026-07-01 (America/Chicago).
- **last_event_timestamp_seen:** 2026-12-30T12:40:00-05:00.
- **records_dated_after_today:** 59 — legitimate per `today_horizon.json` note (future-status fiscal periods / upcoming calendar events & due-dates). Non-blocking at S0; HARDNESS should still confirm any lever built on a post-today record reflects an intended future event, not stale drift.

## Injection gate
- `9_Universe_inject.sql` present but **comment-only** (template header, no executable statements) → `validate.py --phase injection` SKIPs (per AGENTS.md hard rule 4). `4_Changelog.json` is empty `[]`. No injected scenario data for this task.

## Artifacts produced
- `PersonaBrief.txt` (verbatim from persona-briefs source)
- `_aux/Universe_Split/` (33 per-table JSON + combined) · `_aux/data_hash.txt`
- `_aux/Universe_Index/` (service_inventory, entities_personas, key_facts, today_horizon, accounts_per_entity, graph_report)
- `_aux/Fact_Ledger.json` (emails 206, amounts 403, dates 192, linear_issues 230, airtable_records 170, hubspot_objects 183, invoices 504, slack_channels 8, slack_users 61, personas 61)
- `_aux/Feasible_Surface.json` (15 tables with enums, 19 enum columns)
