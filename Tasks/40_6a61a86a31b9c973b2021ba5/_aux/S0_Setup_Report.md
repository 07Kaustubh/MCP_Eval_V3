# S0 Setup Report — Tasks/40_6a61a86a31b9c973b2021ba5

## Persona
- **Name:** Carlos Mendez
- **Role:** Onsite Property Manager
- **Persona id:** `p_009` · email `carlos.mendez@starpm.com`
- **Business Function:** 1 · Property Operations
- **Systems touched most:** Airtable, Slack `#make-ready` and `#maintenance`, Gmail (tenants + vendors), Linear

## Business Function
- **Name:** Property Operations (Cat 1)

## Universe
- **Detected universe:** starpm (Star Property Management)
- **Base path:** `StarPM_Base_Universe/`
- **Per-task data hash:** `49556fce9808d236f04668faeac79ba84d28b67cdc0a89727f866a12d844545d`

## Record counts (from `_aux/Universe_Split/`)
- **Total records:** 3892 across 33 service tables
- Airtable: 249 (records=170, users=61, others=18)
- Contacts: 61
- Google Calendar: 585 (events=565, calendars=20)
- Gmail: 640 (messages=484, threads=156)
- HubSpot: 673 (associations=388, objects=187, properties=73, others=25)
- Linear: 409 (issues=230, users=61, memberships=61, comments=48, others=9)
- QuickBooks: 626 (entities=625, company_info=1)
- Slack: 649 (messages=580, users=61, channels=8)

## Universe today / horizon
- **Universe today:** 2026-07-01 (America/New_York per today_horizon.json; StarPM canonical zone is America/Chicago per AGENTS.md — timezone field cross-checked at HARDNESS)
- **Last event timestamp seen:** 2026-12-30T12:40:00-05:00
- **Records dated after today:** 59 — legitimate per note (fiscal-period future rows / upcoming AP due_dates). Flag for HARDNESS to verify none are stale scripted-scenario artifacts before selecting a lever anchored in a future window.

## Fact Ledger surface (from `_aux/Fact_Ledger.json`)
- emails: 206 · amounts: 403 · dates: 192
- personas: 61 · slack_channels: 8
- StarPM universe has no oracle_gl GL surface, hence 0 JE/exception/recon/vendor/AP-invoice IDs, and no filesystem service (attachments flow through Gmail / HubSpot / Airtable per V4 spec).

## Feasible Surface
- 15 tables with enum-like columns extracted (19 enum columns total). Written to `_aux/Feasible_Surface.json` for S3 rubric cross-reference.

## Exit note
S0 infrastructure ready. Next: `PIPELINE HARDNESS — Tasks/40_6a61a86a31b9c973b2021ba5` in a fresh chat. (StarPM V4 path: HARDNESS produces an `## Injection Plan`; then `PIPELINE INJECTION` authors + audits `9_Universe_inject.sql` before S1.)
