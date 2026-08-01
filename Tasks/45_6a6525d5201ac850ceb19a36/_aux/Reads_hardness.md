# Reads log — HARDNESS (Task 45, StarPM V4)

## Reference cards / eval / QC spec consulted
- Reference/Sessions/HARDNESS.md :: phase runbook; confirmed StarPM per-model density scheme (40 design / 15 floor), 6-section Hardness_Plan, single-target uniqueness mandate.
- Reference/Hardness_Playbook.md :: the 11-lever catalog + tool-call costs; StarPM-scoped density note (never apply 50/40 to StarPM).
- Tasks/_meta/Learnings.md :: read end-to-end. Cited L1/L13 (latching/first-framing), L2/L10/L11 (structured-DB skip = reliable service-skip), L4/L5 (near-miss/action-incompleteness ineffective alone), L6 (answer never verbatim), L7 (multi-write density), L9 (universe gotcha), L15/L16 (implicit prompt), L31 (Gemini omits negative directives), items 9-12 (dual-model recipe: symmetric + 2 asymmetric; displaced-lever warning), item 13-16 (Task 39 Las Palmas 8D QC-fail: F7/F8/F9), item 17 (StarPM base64 email body), item 20 (prose volume ≠ rigour).
- Tasks/_meta/AGENTS.md :: cross-task log protocol.

## Per-task data sources consulted
- _aux/Universe.txt :: universe = starpm.
- _aux/Universe_Index/today_horizon.json :: today 2026-07-01 America/Chicago; 59 records after today (legit if future/upcoming).
- _aux/Universe_Index/service_inventory.md + graph_report.md + key_facts.md + entities_personas.md + accounts_per_entity.md :: 8 services; Airtable SoR (tblMakeReady 120 / tblMaintenanceTickets 50); no GL accounts; 61 emails; Jaime = 48 mentions.
- _aux/Fact_Ledger.json :: 206 emails / 403 amounts / 192 dates / 170 airtable ids / 230 linear ids; source_hash 06f7535a…; confirmed `recbd087a4abd605b` present in airtable id list.
- PersonaBrief.txt + 1_Business_Function.txt + 2_Persona.txt :: Jaime Salinas, QC Inspector, BF3 QC & Field Services.
- _aux/Universe_Split/airtable.airtable_records.json :: GREPPED — verified Mesa Vista 4C = 3 records (recbd087 selProg / recc8534 selReady / reca424 maint-ticket); Las Palmas 8D = 4 rows; Las Vistas 9D = 7; Las Palmas 212D = 1; Las Vistas 3C = 1.
- _aux/Universe_Split/gcalendar.gcalendar_events.json :: GREPPED — only future Mesa Vista 4C event = QC inspection 2026-07-15 (confirmed, 3 calendar copies).

## Eval / QC sub-dims relevant to this phase
- Trajectory · Tool Call Count (StarPM floor 15; design 40+ per model) :: projected Opus ~45 / Gemini ~43 → PASS.
- Trajectory · cross-service breadth :: 7 of 8 services → PASS.
- Universe · Feasibility + Cross-service Coherence :: levers grounded in real records; reachable via Airtable; no universe edits.
- (Pre-empting submission-gate) F7 AMBIGUOUS_TARGET :: flagged — 4C is multi-row; disambiguation contract issued to S1/S3. F9 UNRECONCILED_FUTURE_EVT :: only future 4C event is the task's own 7/15 QC inspection.

## Delegation
- ultrabrain sub-agent (ses_0600ab97bffeUkhXl0mdFxF2Ts) performed the grounded lever scan. Its row-count claim (2 rows for 4C) was VERIFIED and CORRECTED to 3 records; all other findings independently re-verified against the universe before transcription.
