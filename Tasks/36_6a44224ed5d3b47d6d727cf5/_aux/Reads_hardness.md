# Reads Log — HARDNESS (Task 36 · MoveOps · Julian Brooks · Customer Engagement)

v11 E2 compliance gate. Every reference doc / QC spec / Eval spec consulted this phase, one line each.

## Cross-cutting pipeline docs
- `AGENTS.md` :: PIPELINE HARD RULES + MoveOps universe constants (universe today 2026-04-26, PHMSA hazmat landmine, Marcus Webb identity distinct from KeyStone, Airtable-vs-CRM SSOT, V2.1 framework).
- `Reference/Sessions/HARDNESS.md` :: Phase runbook (11-lever scan → 3-5 selected → density projection with tiered gate 50+/40-49/<40 → service-breadth check → stump hypothesis → Hardness_Plan.md 6 sections).
- `Reference/Hardness_Playbook.md` :: 11-lever catalog with per-lever tool-call cost ranges; PASS ≥ 50 midpoint / THIN 40-49 / STOP < 40; anti-patterns (contrived precision, over-stacking, pre-solving, tool naming).
- `Reference/Knowledge_Flow.md` :: not re-read (used implicitly through S0 outputs).

## Learnings (empirical Opus 4.8 failure modes) — MANDATORY FIRST READ
- `Tasks/_meta/Learnings.md` :: L1-L30 loaded end-to-end.
  - L1 confirm-already-done / L4 near-miss-entity-alone / L5 action-incompleteness / L6 correction-email-stating-answer / L7 binary-is-it-posted — all ineffective alone, must avoid.
  - L8 three reductions across three services — target failure anatomy, but Brookfield-anchored (GL + SAP subledger). Need MoveOps translation.
  - L9 authority-figure dismissal — most effective single mechanism (~100% fail).
  - L10 SAP subledger invisibility — Brookfield-only; MoveOps analog = Airtable relocation records / QuickBooks bills / CRM engagements.
  - L11 structured-vs-conversation skip — MoveOps analog = Airtable / Linear / QuickBooks skipped when Slack/email chatter is rich.
  - L12 thread-reply invisibility (~40% miss) / L13 first-framing anchor / L14 correct-observation-wrong-conclusion — all applicable.
  - L15 implicit prompts only / L16 persona believes wrong number / L17 wrong-answer catalog — prompt design gates.
  - L23 dollar-threshold filter blindness on email surface (Task 24 pattern).
  - L24 verb-tense sensitivity in L9 anchors — soft verbs default.
  - L25 existing-output anchor trap — plant a superficially matching artifact that fails on rubric-tested fields (per-line schedule, business justification, routing). HIGHEST-yield novel stump.
  - L26 decoy parent thread on Slack — same channel, overlapping topic, more recent ts → 80%+ failure on canonical thread_ts.
  - L27 soft-instruction over-compliance — "leave X as-is" reads as blanket no-op unless scoped.
  - L28 tool-variant trap (Records Vault add_version vs upload_document) — Brookfield-only, MoveOps analog = Airtable update-record vs create-record.
  - L29 escape-valve prompt clauses neutralize L2 structured-DB skip — do not include when structured DB is load-bearing.
  - L30 REVIEW REBUILD triage from rubric-binding cascade — not directly applicable at HARDNESS, but reinforces the "wrong-recipient rubric binding" landmine.

## S0 outputs consulted (per-task ground truth)
- `Tasks/36_6a44224ed5d3b47d6d727cf5/PersonaBrief.txt` :: Julian Brooks - Lead Customer Support Specialist; 5 active threads (Terraform/Vantage 1047-employee onboarding, BrightLoop recovery Simone+Marcus, NorthWind Emilia Cruz piano callback, StormCloud flight-complaint context, AWS cost spike root cause); direct reports Zara Kovacevic + Omar Ibrahim; Omar-mis-prioritized-Jae-won-Kim landmine.
- `Tasks/36_6a44224ed5d3b47d6d727cf5/2_Persona.txt` + `1_Business_Function.txt` :: persona + function confirmed.
- `_aux/S0_Setup_Report.md` :: universe = moveops, 1705 records / 25 sources / 9 services; timezone discrepancy (today_horizon says America/New_York, AGENTS.md says US/Pacific) — non-blocking if HARDNESS does not pick a timezone-sensitive lever.
- `_aux/Universe_Index/service_inventory.md` :: 7 services active (airtable 172, contacts 119, crm 242, email 494, linear 182, quickbooks 112, slack 384). No Oracle GL, no SAP, no BlackLine, no Records Vault. Structured surfaces available: airtable.records (167 rows), quickbooks.bills+invoices+customers+vendors, linear.issues+comments, crm.engagements+deals+leads.
- `_aux/Universe_Index/graph_report.md` :: Julian in top-30 by mentions (17 direct + 24 email + 19 Slack). Densest persona clusters: Mina Hashimoto (73), Catalina Dubois (69), Emeka Diallo (68), Chloe Vance (60), Marcus Thorne (44). No JEs / no BlackLine exceptions / no reconciliations / no AP invoice pending (MoveOps is operational).
- `_aux/Universe_Index/key_facts.md` :: 494 emails, 354 Slack (top channels C002 water-cooler 94, C006 sales-pipeline 91, C003 engineering 68, C005 finance 49, C004 executive 26, C009 root-cause-aws-spike 14), 69 Linear issues.
- `_aux/Universe_Index/entities_personas.md` :: 114 unique emails. MoveOps personas (all Julian's peer / adjacent): Julian, Zara Kovacevic, Omar Ibrahim (Customer Support), Catalina Dubois (Account Mgr), David Chen (Customer Engagement Lead), Mina Hashimoto (Account Mgr), Emeka Diallo (Account Mgr), Suki Patel + Blessing Okafor + Fatimah Al-Rashidi + Javier Morales (Relocation Coordinators), Marcus Thorne (Head of Finance), Elena Rostova (CEO), Chloe Vance (Ops Mgr), Samira Tariq (Eng Mgr), Priya Chakrabarti (EA), Dmitri Volkov + Lena Bjorkstrom + Anh Nguyen (SWEs), Hana Kim (Accountant), Alejandro Fuentes (Financial Analyst). NPC clusters: BrightLoop (Marcus Webb + Simone Richter + Jordan Ekwueme + Tessa Moreno), Vantage/Terraform (Rachel Nguyen), NorthWind (Emilia Cruz + Victor Huang), StormCloud (Jae-won Kim + Anya Petrova + Liam Park + Simone Richter — SAME NAME as BrightLoop Simone), UrbanNest (Carmen Reyes), Heartland Movers (Jake Loomis + Lisa Kwan), Swift Relocations (Greg Pallone), DOT hazmat (Linda Castellano + hazmat.compliance@dot.gov). Persona-attribution landmines: (a) three distinct Marcus Webbs — brightloopanalytics.com + m.webb@ironcladsec.com + marcus.webb.lab@gmail.com; (b) two distinct Simone (BrightLoop apartment recovery + StormCloud PMM).
- `_aux/Universe_Index/accounts_per_entity.md` :: empty (no Oracle GL — MoveOps operational). Account-number trap DOES NOT apply.
- `_aux/Universe_Index/today_horizon.json` :: universe_today 2026-04-26 (America/New_York per file; AGENTS.md says US/Pacific — flagged).
- `_aux/Fact_Ledger.json` :: 216 emails, 64 amounts, 155 dates, 132 personas, 9 slack channel IDs. Empty entities/fiscal_periods/JE-IDs (expected for MoveOps).

## Universe grep (grounding pointers for the sub-agent)
- Terraform / Vantage / 1047-employee onboarding: 32 emails, 39 Slack, 2 CRM deals, 1 CRM engagement, 1 CRM lead, 1 QuickBooks customer, 2 QuickBooks invoices, 9 Linear comments, 1 Linear issue, 2 Airtable records. Rachel Nguyen 8 emails + 5 Slack (primary); Derek Liu + Sarah Chen barely mentioned (potential admin-account trap).
- BrightLoop / Simone / Marcus Webb: 67 emails, 36 Slack, 22 Linear comments, 7 Linear issues, 1 Linear project, 11 Airtable records, 7 CRM engagements, 5 CRM contacts, 5 CRM deals, 4 QuickBooks bills, 3 QuickBooks invoices. Deepest surface — multi-service structural.
- NorthWind / Emilia Cruz / piano: 34 emails, 36 Slack, 7 Linear comments, 2 Linear issues, 2 CRM engagements, 4 CRM deals, 6 CRM contacts, 9 Airtable records.
- StormCloud / Jae-won Kim: 27 emails, 19 Slack, 8 Linear comments, 3 Linear issues, 5 Airtable records, 3 CRM deals, 2 CRM leads.
- UrbanNest / Carmen Reyes (Simone apartment mismatch): 36 emails, 9 Slack, 9 Linear comments, 6 Linear issues, 2 CRM engagements, 1 CRM deal, 1 QuickBooks vendor, 1 QuickBooks invoice, 1 Airtable record.
- AWS cost spike: 4 emails, 16 Slack (channel C009 root-cause-aws-spike, 14 messages), 1 QuickBooks vendor.
- Hazmat / PHMSA / DOT: 28 emails, 18 Slack, 5 Linear issues, 1 Linear comment, 1 Linear project, 3 Airtable records, 4 CRM deals, 3 CRM engagements, 3 QuickBooks invoices, 1 QuickBooks bill, 1 QuickBooks vendor, 2 QuickBooks accounts, 2 QuickBooks items.
- Marcus Webb variant emails: 6 in email.emails.json across three distinct addresses (brightloopanalytics.com, ironcladsec.com, gmail.com). Persona-attribution landmine ACTIVE.
- Julian Brooks direct involvement: 24 emails, 19 Slack, 3 Linear comments.

## Eval spec sub-dims relevant to this phase
- N/A. HARDNESS phase produces the Hardness_Plan; phase-eval sub-dims (Prompt 1.3/2.8, OE 3.2, Rubrics 4.1) are checked at downstream phases. Density projection ties to Trajectory T1 Tool Call Count (floor 15, pipeline target 50+ midpoint).

## QC spec sub-dims relevant to this phase
- N/A directly. `Docs_moveops/1_Prompt_V3_Guidelines.md` / `2_Rubrics_V3_Guidelines.md` / `3_Oracle_Events_V3_Guidelines.md` will govern S1/S2/S3; HARDNESS output feeds S1 via `## Hardness Brief for the Prompt Writer`.
