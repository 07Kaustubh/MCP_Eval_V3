# S0 Setup Report — 39_6a602c895d0b0ab6551a3a86

## Task metadata
- **Universe:** starpm (Star Property Management, SW Texas residential PM)
- **Business function:** Quality Control & Field Services
- **Persona:** Jaime Salinas · Quality Control Inspector (`p_007`, `jaime.salinas@starpm.com`)
- **Seniority / Department:** Mid · Portfolio Operations
- **Communication profile:** Formality 0.55 · verbosity 0.30 · medium response · active 8 AM–4 PM
- **Scripted footprint:** 7 actions across 7 scenarios (always QC anchor, never lead)

## Data provenance
- **Per-task data sha256:** `49556fce9808d236f04668faeac79ba84d28b67cdc0a89727f866a12d844545d`
- **Universe today:** `2026-07-01` (tz reported by builder: America/New_York; canonical StarPM tz is America/Chicago per AGENTS.md)
- **Last event timestamp seen:** `2026-12-30T12:40:00-05:00`
- **Records dated after today:** 59 (legitimate for future fiscal periods / upcoming AP due dates)

## Record count totals (33 tables across 8 services)

| Service | Records |
|---|---|
| airtable | 249 (bases 1, fields 9, interfaces 1, pages 2, records 170, tables 2, users 61, views 2, workspaces 1) |
| contacts | 61 |
| gcalendar | 585 (calendars 20, events 565) |
| gmail | 640 (messages 484, threads 156) |
| hubspot | 673 (associations 388, job_titles 1, objects 187, owners 21, properties 73, seats 2, teams 1) |
| linear | 409 (comments 48, issues 230, projects 3, team_memberships 61, teams 1, users 61, workflow_states 5) |
| quickbooks | 626 (company_info 1, entities 625) |
| slack | 649 (channels 8, messages 580, users 61) |
| **Total** | **3892** |

## Fact ledger atom coverage
- Emails: 206 · Amounts: 403 · Dates: 192
- Personas: 61 · Slack channels: 8
- V3-legacy id categories (JE / exception / recon / doc / vendor / AP invoice / etc.) are 0 as expected — StarPM is an operational (Airtable + HubSpot + Linear + QuickBooks) universe, not GL-heavy.

## Feasible surface
- 15 tables with enum-like columns, 19 enum columns total → `_aux/Feasible_Surface.json`
- Used by S3 rubric validator to catch universe-contradicting enum values.

## Notes / flags
- `records_dated_after_today = 59` is expected for StarPM's late-2026 tail (recurring calendar events, QuickBooks scheduled bills, forward Airtable make-ready records). Not a data-integrity concern for S0.
- StarPM V4 note (from S0 runbook): universe injection is expected AFTER S0 via `PIPELINE INJECTION` → `9_Universe_inject.sql`. Current split reflects the seed universe the CB pasted; if hardness levers require injection, that flows through the INJECTION phase before S1.
