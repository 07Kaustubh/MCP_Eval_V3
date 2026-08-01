# S0 Setup Report — Task 45_6a6525d5201ac850ceb19a36

## Universe
- **Universe:** `starpm` (Star Property Management, LLC — V4 framework) — auto-detected, written to `_aux/Universe.txt`.
- **Universe today:** 2026-07-01 (America/Chicago).
- **last_event_timestamp_seen:** 2026-12-30T12:40:00-05:00.

## Persona
- **Name:** Jaime Salinas
- **Role:** Quality Control Inspector
- **Persona id:** `p_007` · email `jaime.salinas@starpm.com`
- **Seniority:** Mid · Dept: Portfolio Operations
- **Scripted footprint:** 7 actions across 7 scenarios (participates broadly, leads none — QC sign-off anchor).
- Extracted verbatim from `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` (lines 172-190) → `PersonaBrief.txt`.

## Business function
- **Quality Control & Field Services** (StarPM function 3 · 10% of business mix).

## Per-task data
- **Source:** `3_UniverseDataForThisTask.json` (4.4 MB)
- **data_hash (sha256):** `06f7535a3357ae4900c884fbc76d5e3566f27bf1aef02e47ab6c7ccac8a749a3`
- **Record totals:** 3892 records across 33 sources (8 services: airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack).
- Densest tables: quickbooks_entities 625 · gcalendar_events 565 · slack_messages 580 · gmail_messages 484 · linear_issues 230 · hubspot_objects 187 · airtable_records 170.

## Horizon note
- **records_dated_after_today = 59.** Legitimate per universe convention when `status=future` (fiscal periods) or upcoming `due_dates` (AP). Active window 2026-05-01 → 2026-07-01; the 2026-12-30 last-event tail is future-scheduled events/due-dates, not stale data. Downstream phases (HARDNESS, S1) must resolve any relative-date prompt phrase against 2026-07-01, not against the trailing event.

## Fact Ledger atom surface
- emails 206 · amounts 403 · dates 192 · airtable_record ids 170 · linear_issue ids 230 · linear_comment ids 48 · hubspot_object ids 183 · slack_channel ids 8 · slack_user ids 61 · invoice ids 504 · personas 61.
- `entities 0` / `fiscal_periods 0` expected — StarPM is a property-management universe, not GL-based (no account-number trap, no fiscal-period ledger).

## Feasible surface
- 15 tables with enum-like columns, 19 enum columns total → `_aux/Feasible_Surface.json` (S3 rubric enum-value cross-reference).

## V4 injection gate
- `9_Universe_inject.sql` present (4065 bytes, non-empty) → `validate.py --phase injection` ran.
- **Result: PASS** — 0 fails, 0 warns, 4 notes. The 4 notes are council-deferred semantic checks (injection difficulty composite ≥ 3.5 is judged at FINAL, not deterministically here).

## Artifacts produced
- `_aux/Universe.txt`, `PersonaBrief.txt`, `_aux/data_hash.txt`
- `_aux/Universe_Split/` (33 source JSONs)
- `_aux/Universe_Index/` (service_inventory, entities_personas, key_facts, today_horizon, accounts_per_entity, graph_report)
- `_aux/Fact_Ledger.json`, `_aux/Feasible_Surface.json`
- `_aux/Validator_Reports/injection.md`
