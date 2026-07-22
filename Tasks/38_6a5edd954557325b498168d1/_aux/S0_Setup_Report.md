# S0 Setup Report — Tasks/38_6a5edd954557325b498168d1

## Universe
- **Detected universe:** `starpm` (Star Property Management, LLC — residential property management, V4 framework)
- **Base path:** `StarPM_Base_Universe/` · Tool catalog `7_Server_Tools_Details.json` · Persona briefs `2_StarPM_PERSONA BRIEFS.md`

## Persona
- **Name / role:** Carlos Mendez · Onsite Property Manager
- **Persona id:** `p_009` · email `carlos.mendez@starpm.com`
- **Business function:** 1 · Property Operations (from `1_Business_Function.txt`)
- **Seniority:** Mid · Department: Property Operations
- **Scripted footprint:** 33 actions across 11 scenarios — most-rooted Onsite PM after Brooke (deep tier)
- **Anchors:** Mesa Vista and Las Palmas; leads two make-ready scenarios + two maintenance-response scenarios (carpet, water-heater)

## Per-task data
- **Data hash (sha256 of `3_UniverseDataForThisTask.json`):** `3976fa37728c03476ac804990a4c26973ffdcc3348d722ecd4d26500af7e318f`
- **Total records:** 3892 across 33 sources / 8 services
- **Per-service totals:** airtable 249 · contacts 61 · gcalendar 585 · gmail 640 · hubspot 673 · linear 409 · quickbooks 626 · slack 649
- **Services present:** airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack

## Fact Ledger atom surface
- emails 206 · amounts 403 · dates 192 · personas 61
- id_airtable_record 170 · id_linear_issue 230 · id_linear_comment 48 · id_hubspot_object 183 · id_slack_channel 8 · id_slack_user 61 · id_invoice 504
- entities 0 · fiscal_periods 0 — expected for StarPM (property-management universe, not GL-based; no account-number trap, no fiscal periods)

## Horizon
- **Universe today:** 2026-07-01 (America/Chicago)
- **Last event timestamp seen:** 2026-12-30T12:40:00-05:00
- **Note — records dated after today:** 59 records fall after the universe today (2026-07-01). Legitimate per horizon note (future-status calendar events / upcoming due dates). Flag carried forward for HARDNESS/S1 date-alignment awareness.

## Feasible Surface
- 15 tables with enum-like columns, 19 enum columns total → `_aux/Feasible_Surface.json` (rubric enum cross-reference at S3)
