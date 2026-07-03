# S0 Setup Report — Task 36

## Task identity
- **Task dir:** `Tasks/36_6a44224ed5d3b47d6d727cf5`
- **Universe:** `moveops` (auto-detected, cached to `_aux/Universe.txt`)
- **Business function:** Customer Engagement
- **Persona:** Julian Brooks — Lead Customer Support Specialist

## Per-task data
- **Source file:** `3_UniverseDataForThisTask.json`
- **SHA-256:** `5ec3cf27faf9e0e0c2991b57247f70aa63291d1f55e5e7a40a2fcbfb9094805b`
- **Total records:** 1705 across 25 sources / 9 services

## Record totals (from `service_inventory.md`)

| Service | Rows |
|---|---:|
| airtable (bases + records + tables) | 172 |
| contacts | 119 |
| crm (companies + contacts + deals + engagements + leads) | 242 |
| email | 494 |
| linear (comments + issues + projects + team_memberships + teams + users) | 182 |
| quickbooks (accounts + bills + customers + invoices + items + vendors) | 112 |
| slack (channels + messages + users) | 384 |
| **Total** | **1705** |

## Time horizon
- **Universe today:** `2026-04-26` (America/New_York per `today_horizon.json`; AGENTS.md notes MoveOps universe as US/Pacific — timezone label mismatch is source-of-truth-level and should be flagged if HARDNESS proposes any timezone-sensitive lever)
- **Last event timestamp seen:** `2026-07-02T06:42:37Z` (this is a data-load stamp, well past universe_today — do NOT use as an event anchor)
- **Records dated after universe_today:** 5 (legitimate per builder note — future fiscal periods / upcoming AP due dates)

## Fact Ledger atom summary
- emails: 216 · amounts: 64 · dates: 155
- personas: 132 · aliases: 3
- ids: 14 categories · lifecycle: 4 domains
- entities / accounts_by_entity / fiscal_periods: 0 (expected — MoveOps is operational, not GL-based; no account-number trap)

## Feasible surface
- 11 tables with enums, 15 enum columns total (cached at `_aux/Feasible_Surface.json`)

## Persona brief context (from `PersonaBrief.txt`)
Julian Brooks is Lead Customer Support Specialist. Active thread nexus:
- Terraform Digital / Vantage Distributed enterprise contract onboarding (1,047 employees, 3-relocation batch May 5–12)
- Root-cause contributor to AWS cost spike (identified in `#root-cause-aws-spike`)
- Owns BrightLoop service recovery (Simone Richter apartment mismatch; Marcus Webb car — note: **MoveOps Marcus Webb ≠ KeyStone departed-employee Marcus Webb**; MoveOps Marcus is BrightLoop Analytics client)
- NorthWind piano-damage callback (April 12 Emilia Cruz complaint, no follow-up)
- StormCloud flight-complaint context reconstruction
- Direct reports: Zara Kovačević, Omar Ibrahim (Omar mis-prioritized Jae-won Kim StormCloud lease request — cross-persona landmine)

## Flags for HARDNESS
- **Persona attribution landmine (see auto-memory):** multi-person recovery threads (BrightLoop: Simone + Marcus Webb) sit alongside Slack thread mentions of both. If HARDNESS proposes a levered lookup asking who owns which recovery, grep for BOTH names before signing off — Task 35 pattern.
- **MoveOps Marcus Webb ≠ KeyStone Marcus Webb.** Same name, different person, different universe. Any lever touching Marcus Webb must be grounded in `crm_contacts` / `email` here, not carried over from KeyStone departed-employee logic.
- **PHMSA hazmat + Airtable-vs-CRM source-of-truth landmines** apply for MoveOps generally; verify against per-task universe if HARDNESS proposes touching hazmat / relocation-state levers.
- **Timezone label:** `today_horizon.json` reports `America/New_York` while AGENTS.md says US/Pacific for MoveOps universe. Do NOT ship any timezone-sensitive lever without HARDNESS resolving which is authoritative for THIS task.

## Data-load timestamp
`last_event_timestamp_seen = 2026-07-02T06:42:37Z` is later than `universe_today = 2026-04-26`. Confirmed as builder metadata (data hash / load stamp), not an in-universe event. Downstream phases must anchor to `universe_today`, not to `last_event_timestamp_seen`.
