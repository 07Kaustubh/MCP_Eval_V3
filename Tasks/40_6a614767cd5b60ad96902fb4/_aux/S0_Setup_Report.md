# S0 Setup Report — Tasks/40_6a614767cd5b60ad96902fb4

## Universe
- **Detected:** `starpm` (Star Property Management, LLC — San Antonio TX multifamily property manager)
- **Framework:** V4 (dual-model verification: Opus 4.8 + Gemini)
- **Base path:** `StarPM_Base_Universe/` · Tool catalog `7_Server_Tools_Details.json` · Persona briefs `2_StarPM_PERSONA BRIEFS.md`

## Persona
- **Name:** Lisa Smith
- **Role:** Onsite Property Manager
- **Persona id:** `p_002` · email `lisa.smith@starpm.com`
- **Seniority:** Mid · Department: Property Operations
- **Scripted footprint:** 20 actions across 11 scenarios (deeply rooted)
- **Leads:** `fair_housing_reasonable_accommodation` (6 actions); drives one make-ready end-to-end
- Whitelist check: Lisa Smith is one of the 13 StarPM authoring personas (p_002). CONFIRMED.

## Business function
- **Name:** Property Operations (Business Function 1)
- Matches the persona's declared business function (Cat 1 · Property Operations).

## Per-task data
- **Data hash:** `06f7535a3357ae4900c884fbc76d5e3566f27bf1aef02e47ab6c7ccac8a749a3`
- **Total records:** 3892 across 33 service tables
- **Services present:** airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack
- Notable volumes: quickbooks_entities 625 · slack_messages 580 · gcalendar_events 565 · gmail_messages 484 · linear_issues 230 · hubspot_objects 187 · airtable_records 170

## Today horizon
- **Universe today:** 2026-07-01 (America/Chicago) — matches registry constant.
- **last_event_timestamp_seen:** 2026-12-30T12:40:00-05:00
- **records_dated_after_today:** 59 — legitimate when status=future (fiscal periods) or upcoming due_dates / future calendar events. NOTE for HARDNESS/S1: date ceiling is 2026-07-01; relative-date windows must resolve to <= that date with universe data present. The 59 forward-dated records extend to Dec 2026 (mostly gcalendar events).

## Fact Ledger atom surface
- emails 206 · amounts 403 · dates 192 · personas 61
- id_airtable_record 170 · id_linear_issue 230 · id_linear_comment 48 · id_hubspot_object 183 · id_slack_channel 8 · id_slack_user 61 · id_invoice 504
- entities 0 · fiscal_periods 0 (StarPM is property-management, not GL-based — no account-number trap / fiscal-period ledger; expected)

## Feasible surface
- 15 tables with enum-like columns · 19 enum columns total → `_aux/Feasible_Surface.json`

## V4 injection gate
- `9_Universe_inject.sql` present (4065 bytes) but **comment-only template header** — 0 executable statements.
- `validate.py --phase injection` → **PASS** (0 fails, 0 warns, 4 notes). Comment-only header self-skips per pipeline rule. No injected scenario data; task runs on base universe as-is.

## Artifacts produced
- `PersonaBrief.txt` (verbatim Lisa Smith section)
- `_aux/Universe.txt` = `starpm`
- `_aux/Universe_Split/` (33 per-service JSON files)
- `_aux/Universe_Index/` (service_inventory, entities_personas, key_facts, today_horizon, accounts_per_entity, graph_report)
- `_aux/Fact_Ledger.json`
- `_aux/Feasible_Surface.json`
- `_aux/Validator_Reports/injection.md`
