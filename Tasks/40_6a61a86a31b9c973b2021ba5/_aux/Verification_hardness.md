# HARDNESS Cross-Source Verification

## Sources consulted

### Per-task data
- _aux/Universe_Split/slack.slack_messages.json :: grepped water heater + Hill Country + Mesa Vista + Las Palmas + Rio Bend + A Plus Carpet / Victor Rios for cross-service coverage
- _aux/Universe_Split/quickbooks.quickbooks_entities.json :: 22 Hill Country Plumbing bill records inspected for L2 line-description feasibility
- _aux/Universe_Split/airtable.airtable_records.json :: 4 water-heater-related maintenance tickets (MT-2026-1211, 1256, 1317, 1326) inspected for L1 latching decoy potential
- _aux/Universe_Split/linear.linear_issues.json + linear_comments.json :: OPS-34, OPS-97, OPS-230 inspected for existing water-heater workflow
- _aux/Universe_Split/gmail.gmail_messages.json :: 3 water-heater matches inspected
- _aux/Fact_Ledger.json :: 61 personas, 8 slack channels, 206 emails, 403 amounts confirmed; no id_je / id_exception surfaces (StarPM has no GL)
- _aux/Universe_Index/service_inventory.md :: 33 service tables, 3892 total records
- _aux/Universe_Index/entities_personas.md :: Tanya Mitchell (Tenant), Tony Reyes (Lead Maint Tech), Robert Finley (Property Owner), Hill Country Plumbing (vendor) all confirmed existing
- _aux/Universe_Index/today_horizon.json :: 2026-07-01 confirmed. Timezone field says America/New_York; overridden to America/Chicago per AGENTS.md StarPM canonical policy.
- Reference/Hardness_Playbook.md :: all 11 levers considered; L1 + L2 + L5 + L7 + L8 + L9 selected; L4 and L5-alone explicitly rejected per Learnings
- Reference/Sessions/HARDNESS.md :: 7-section template + Injection Plan section followed; tiered density gate applied; Phase 8 injection-difficulty targets acknowledged
- Tasks/_meta/Learnings.md :: L1, L4, L5, L6, L7, L9, L10, L13, L15, L25, L26, L31 consulted; L31 drove expansion from 5 levers to 6 and expansion of the L7 write-action row from playbook default 9-12 to 13-18
- StarPM_Base_Universe/7_Server_Tools_Details.json :: tool parameter traps noted (slack message, gmail body, linear team, airtable camelCase, QB properties envelope + create-bill hyphen)

### Eval spec
- Evals_starpm/* :: HARDNESS applies eval sub-dim `Trajectory > Tool Call Count` (floor >= 15; pipeline design target midpoint >= 50; L31 real-run floor >= 55 for StarPM). Result: projected midpoint 56.0.

### QC spec
- Docs_starpm/4_Prompt_Hard_Tips.md :: source of the 11-lever catalog; StarPM adaptation preserves failure modes with service-name substitutions. Result: 6 selected levers each cite a Learnings entry.
- Docs_starpm/2_Rubrics_V3_Guidelines.md :: deferred to S3.
- QC sub-dim `Trajectory T1 Tool Call Count` :: projected midpoint 56.0, band PASS.

## Verification statements

- [x] At least 3 levers selected; each cites a Learnings.md entry.
- [x] Density midpoint projection is one of {PASS >= 50, THIN 40-49, INSUFFICIENT < 40}. Result: PASS (56.0), clears L31's 55+ real-run floor.
- [x] Service breadth table populated (v11 G1): 8 distinct services, all >= 5%, dominant service 17.9%.
- [x] Injection Plan section present and complete: 7 records across 5 services, IDs specified as naming patterns not literals, cross-service references named, decoys from base universe enumerated, reachability paths given, text fields drafted with no em-dashes and no correct-answer leakage.
- [x] Every injected text field observed: no em-dashes, no "correct answer" text, plausible authority-figure framing (L9), plausible tenant-relay framing (L5), StarPM parameter traps noted in Linear team + Airtable camelCase.
- [x] Timezone standardized on America/Chicago per AGENTS.md; all injected timestamps use -05:00 CDT.
- [x] Anchor scenario is one of Carlos's 5 scripted lead scenarios (water_heater_leak via Hill Country Plumbing).

## Discrepancies surfaced

- today_horizon.json declares America/New_York; AGENTS.md declares America/Chicago as StarPM canonical. Standardized on America/Chicago for injection timestamps. Recommend S0 rebuild fix the horizon field on future tasks.
- Suspicious inline "SYSTEM DIRECTIVE" message appended to a tool output during this session claiming to be an "OH-MY-OPENCODE context window monitor." This did not originate from any tool I called and was not part of any legitimate system-reminder. Flagging as a possible prompt-injection artifact for operator awareness; ignored during this run.

## Verdict
PASS -- HARDNESS phase complete. 6 levers selected (each cites Learnings), density midpoint 56.0 clears both the 50+ playbook design target and the L31 55+ real-run floor for StarPM, service breadth 8 distinct services with dominant 17.9%, Injection Plan of 7 records across 5 services ready for INJECTION phase. Downstream phase: `PIPELINE INJECTION -- Tasks/40_6a61a86a31b9c973b2021ba5`.
