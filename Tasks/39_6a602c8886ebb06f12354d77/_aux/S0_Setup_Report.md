# S0 Setup Report — Tasks/39_6a602c8886ebb06f12354d77

## Universe
- Detected universe: **starpm** (Star Property Management, LLC — V4 framework)
- Universe today: **2026-07-01** (America/Chicago)
- last_event_timestamp_seen: 2026-12-30T12:40:00-05:00
- records_dated_after_today: **59** — legitimate per horizon note (status=future / upcoming due dates); the far-future max (Dec 2026) is ~6 months past today, verify at HARDNESS these are genuine future-dated calendar/AP rows before building any date-window lever on them.

## Persona
- Name / role: **James Bennett · Assistant Maintenance Technician** (`p_006`, email james.bennett@starpm.com)
- Seniority: Junior · Department: Maintenance
- Business Function (from 1_Business_Function.txt): **Maintenance & Repairs** (Cat 4)
- Persona whitelist: CONFIRMED — James Bennett is an authoring persona in `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` (Cat 4 — Maintenance & Repairs).
- **DESIGN-SURFACE PERSONA (load-bearing for HARDNESS):** 0 scripted actions; participant-only cast in `makeready_laspalmas8d_turn`. Tasks are author-from-spec, modeled on the shape of Assistant Maintenance Tech work (executes assigned tickets under John/Elias, follows Lead routing, reports completion). No scripted arc to anchor against — the scripted footprint is thin.
- Systems he touches most: Linear (ticket execution), Slack #maintenance, Google Calendar (dispatch), occasional Gmail.

## Per-task data
- Data hash (sha256 of 3_UniverseDataForThisTask.json): `06f7535a3357ae4900c884fbc76d5e3566f27bf1aef02e47ab6c7ccac8a749a3`
- Record totals: **3892 records across 33 tables / 8 services** (airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack).
- Density highlights: gcalendar_events 565 · slack_messages 580 · quickbooks_entities 625 · gmail_messages 484 · hubspot_associations 388 · linear_issues 230 · airtable_records 170.

## Fact Ledger atom surface
- emails 206 · amounts 403 · dates 192 · personas 61
- ids: airtable_record 170 · linear_issue 230 · linear_comment 48 · hubspot_object 183 · slack_channel 8 · slack_user 61 · invoice 504
- entities 0 · fiscal_periods 0 — EXPECTED-ZERO for StarPM (property-management universe, no GL entities / no fiscal periods; no account-number trap).

## V4 injection gate
- `9_Universe_inject.sql` present with executable statements (73 lines).
- `validate.py --phase injection` → **PASS** (0 fails, 0 warns, 4 notes). Injected scenario data cleared Evals_starpm/0 deterministic gates. Difficulty composite (>=3.5) is judged by council at FINAL, not here.

## Artifacts written
- PersonaBrief.txt (verbatim James Bennett section, lines 269-289 of the briefs)
- _aux/Universe_Split/ (33 per-table JSON files)
- _aux/Universe_Index/ (service_inventory, entities_personas, key_facts, today_horizon, accounts_per_entity, graph_report)
- _aux/Fact_Ledger.json
- _aux/Feasible_Surface.json (15 tables with enums, 19 enum columns)
- _aux/Validator_Reports/injection.md
