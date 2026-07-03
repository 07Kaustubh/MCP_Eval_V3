# S0 Setup Report — Task 35_6a4421ec8169e23828bb442d

## Task anchors
- **Universe**: keystone (Keystone Mortgage Partners, residential mortgage brokerage, single entity)
- **Persona**: Robert Calloway — Owner / Licensed Mortgage Broker (final decision-maker on escalations; holds broker license; does not originate loans)
- **Business function**: Executive
- **Per-task data hash (sha256)**: `7c6640c75a38b19b1622d4aca92b8e9978f653d1f26eb282461f51c1fc3a5304`

## Universe temporal window
- **Universe today**: 2026-04-28 (America/New_York)
- **Last event timestamp seen**: 2026-08-04T21:25:33+00:00
- **Records dated after today**: 8940 — legitimate when they represent upcoming due-dates, forward-dated calendar/hold slots, or scheduled closings; treat any prompt-side "as of today" claim against post-today rows as a groundedness risk unless the row's status marks it as future / scheduled.

## Per-task record totals
Total: **31,318 records** across **34 sources** (8 services). See `_aux/Universe_Index/service_inventory.md` for the full table.

Highest-density sources (candidate hardness surfaces):
- `mortgage_los.document_checklist_items` — 8,841
- `email.emails` — 7,287
- `stripe.fc_transactions` — 3,228
- `email.threads` — 2,504
- `stripe.charges` — 1,730
- `stripe.transfers` — 1,183
- `mortgage_los.loans` — 644
- `mortgage_los.borrowers` — 638
- `quickbooks.bills` — 585
- `slack.slack_messages` — 573

## Persona open threads (from PersonaBrief.txt — pre-hardness scan)
Robert Calloway sits on 7 active escalations, all Executive-band:
1. Ransomware incident (scenario_14b3ffde) — 2 BTC ransom vs 72-hour backups, Monday closings at risk, cyber counsel engaged.
2. Marcus Webb departure (scenario_7da8f37a) — 4 borrower file-transfer requests, pre-resignation data exfiltration evidence.
3. Appraisal bias investigation (scenario_2ab2a103, scenario_9639912b) — anonymous tip about systematic bias.
4. Glassdoor toxic-culture reviews (scenario_e2f94849) — 3 reviews describing hostile workplace.
5. Grace pressuring processors on compliance corners (scenario_6232deb5).
6. CFPB fair-lending complaint (scenario_e3be5565) — denied Black borrower discrimination complaint, 15-day response window.
7. Brittany Wallace harassment complaint (scenario_2b42ecf2) — Jordan Blake (Robert's close friend, top BD) is subject.

## KeyStone landmines to flag for HARDNESS
- **TRID timing** — Loan Estimate must be sent within 3 business days of application; Closing Disclosure delivered 3 business days before closing. Query `mortgage_los.disclosures` for actual sent_date vs application_date / closing_date. (No `disclosures.json` in this split — verify at HARDNESS whether disclosures live on the loan record or as document_checklist_items.)
- **Departed employee** — Marcus Webb is the canonical KeyStone departed-employee trap. Do not author tasks that assume he is active.
- **Loan-based, not GL-based** — `mortgage_los.loans` is source of truth for loan-level data; CRM holds marketing / referral funnel only. No account-number cross-entity trap here.

## Atom surface (Fact_Ledger.json)
- emails: 1923 · amounts: 4446 · dates: 808 · slack channels: 8 · personas: 1306
- Non-zero surfaces confirm the ledger has real grounding material for downstream phases.
- Zero-count IDs (JE / exception / recon / doc / vendor / apinv / linear / reminder / conversation / airtable / calendar / contact / persona / entity / fiscal_period) reflect the KeyStone universe schema — the ledger's ID map is Brookfield-flavored; KeyStone IDs are loan_id / borrower_id / lender_id / condition_id / checklist_item_id, which are already captured atomically inside the per-service splits and will be pulled in by phase-specific validators.

## Deliverables written
- `PersonaBrief.txt` — verbatim from `Mortgage_Base_Universe/3_Persona_Briefs.md` lines 13-31
- `_aux/Universe.txt` — `keystone`
- `_aux/Universe_Split/` — 34 per-service JSON files
- `_aux/Universe_Index/` — `service_inventory.md`, `entities_personas.md`, `key_facts.md`, `today_horizon.json`, `accounts_per_entity.md`, `graph_report.md`
- `_aux/Fact_Ledger.json`
- `_aux/Feasible_Surface.json` — 21 tables with enums, 29 enum columns
- `_aux/data_hash.txt`
- `_aux/Todos_s0.md` (this phase's TODO tracker)
- `_aux/Verification_s0.md`
