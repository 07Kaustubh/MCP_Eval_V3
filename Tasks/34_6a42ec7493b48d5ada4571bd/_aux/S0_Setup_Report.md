# S0 Setup Report — Task 34_6a42ec7493b48d5ada4571bd

## Identity
- **Universe**: moveops (MoveOps Inc., B2B remote-work relocation services, V2.1 framework)
- **Persona**: Blessing Okafor — Relocation Coordinator
- **Reports to**: Chloe Vance (Operations Manager)
- **Business Function**: Operations
- **Universe today**: 2026-04-26
- **Universe timezone (registry)**: America/Los_Angeles (MoveOps registry); `today_horizon.json` reports America/New_York (detector default; non-blocking — universe today date itself is authoritative).
- **Last event timestamp seen**: 2026-06-30T12:08:07Z (note: this is build-time clock, not universe data)
- **Records dated after universe today**: 5 (legitimate per detector note — future fiscal periods or upcoming AP due_dates; flag forwarded to HARDNESS for confirmation)

## Per-task data hash
`011c1f02ef6741e292ff7230a4c06304395d6ba2d5f6d9117309e41dfa2e5140`

## Record counts (from `_aux/Universe_Split/`)
- Total: 1705 records across 25 source files / 9 services
- airtable: bases 2, records 167, tables 3
- contacts: 119
- crm: companies 71, contacts 88, deals 44, engagements 16, leads 23
- email: 494
- linear: comments 79, issues 69, projects 8, team_memberships 4, teams 3, users 19
- quickbooks: accounts 7, bills 17, customers 15, invoices 35, items 31, vendors 7
- slack: channels 9, messages 354, users 21

## Fact_Ledger atom counts (from `_aux/Fact_Ledger.json`)
- emails: 216
- amounts: 64
- dates: 154
- personas: 132
- slack_channels: 9
- GL/JE/exception/recon/doc/vendor/AP/Linear-issue/Airtable-record/calendar/contact IDs: 0 each
  (MoveOps universe has no GL accounts, no JE lifecycle, no Records Vault retention codes — distinct from Brookfield)

## Persona open threads (high-level — see PersonaBrief.txt for verbatim)
- Marcus Webb Detroit→Chicago split-vendor coordination (Heartland household + Swift cold-chain lab equipment)
- Canopy Q2 wave coordination
- DOT hazmat training certification in progress
- NorthWind piano damage acknowledged (Emilia Cruz stairwell turn radius)
- Missed Road Runner Auto Transport April 11 delay email for Marcus Webb's Honda Civic (BrightLoop)
- Swift driver pushback on new paperwork requirements

## MoveOps universe landmines applicable to this persona
- **PHMSA DOT hazmat compliance**: Hazmat shipments (Class 3B lasers, cryogenic equipment, Class 9 lithium) require SIGNED DOT certificate from freight carrier — verbal driver confirmation does NOT count.
- **Marcus Webb identity trap**: Two distinct "Marcus Webb"s exist across pipeline universes — MoveOps's Marcus Webb is a Canopy/BrightLoop CLIENT employee (not the KeyStone departed-employee). Do NOT pollute logic across universes.
- **Airtable-vs-CRM source-of-truth trap**: Relocation/vendor/coordinator state lives in Airtable (`tblRelocations01`); CRM is deal/engagement funnel only. Never trust CRM as source for relocation state.
- **Parameter trap relevant to Relocation Coordinator**: email + messaging use `content` (not `body`). Slack uses `payload` (not `text`).

## Exit status
All required S0 artifacts written. Ready for `PIPELINE HARDNESS — Tasks/34_6a42ec7493b48d5ada4571bd` in a fresh chat.
