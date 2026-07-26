# Reads — S1 (reference-doc reading log, v11 E2 gate)

## Runbook + validators
- `Reference/Sessions/S1.md` :: S1 procedure, exit criteria, STOP gate, conditional AUDIT auto-fire (MANDATORY here: prompt drafted this pass).
- `Reference/AGENTS.md` :: which reference card for which phase.
- `Validators/phase_ready.py` :: gate mechanics; VERIFICATION_DEPS[s1]=[hardness] runs check_verification on the upstream verification doc.
- `Validators/check_verification.py` :: verification-doc validator. Diagnosed the false-positive (naive re.search matched the strings `## Sources consulted` / `## Verdict` quoted in the Discrepancies prose) + real-header mismatch (`## Data sources consulted`). Repaired the HARDNESS doc to conform; substance untouched.

## Upstream task artifacts
- `_aux/Verification_hardness.md` :: HARDNESS cross-source verification (PASS, 5 levers, 48.5/model).
- `_aux/Hardness_Plan.md` :: levers L10/L2/L1/L4/L3, stump hypothesis, density 48.5/model, load-bearing base rows, feasibility-signature TODO (discrepancy #3).
- `PersonaBrief.txt` + `1_Business_Function.txt` + `2_Persona.txt` :: James Bennett, Assistant Maintenance Tech, junior voice (formality 0.35, verbosity 0.30), design-surface / author-from-spec, Maintenance & Repairs.
- `_aux/Universe_Index/today_horizon.json` :: universe today 2026-07-01 America/Chicago (AUTHORITATIVE). NOTE bug: Fact_Ledger.lifecycle.today mis-set to 2026-06-12 (Brookfield default).
- `_aux/Universe_Index/service_inventory.md` :: airtable 170 records, slack 580 msgs, linear 230 issues, gmail 484, gcalendar 565 events, quickbooks 625, hubspot 187, contacts 61.
- `_aux/Universe_Index/entities_personas.md` :: Leads John Smith / Elias Navarro / Tony Reyes (all @starpm.com). Confirmed john.smith@starpm.com = Lead (the prompt's rundown recipient).

## Format / voice / hardness cards
- `Reference/Prompt_Format.md` :: 500-word cap, no em-dash, no tool/MCP/ID names, no pre-solving, Trigger/Context/Asks, 3+ writes across 3+ services, sentence-removal coherence test.
- `Docs_starpm/6_Prompt_Relative_Time_Updates.md` :: date SSOT, today July 1 2026 (Wed), relative time enabled, Q3/H2 boundary.
- `Docs_starpm/4_Prompt_Hard_Tips.md` :: Opus search behavior (broad-first, skips structured DBs, misses replies, latches first framing, search-cap invisibility) -> maps to L2/L3/L1/L4; go-broad-not-specific; hint without telegraphing.
- `Prompt_Guidelines.md` :: anti-patterns (QC-sample clichés, command-lists, over-signaling, generic urgency, formulaic closes).
- `QC_Tasks/V4_Tasks/QC_Passed/Task1..4/5_Prompt.txt` :: passing V4 prompt voice/structure (senior-register refs; James is junior so plainer/shorter, same Trigger/Context/Asks arc).
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: feasibility of the 4 target writes confirmed — create_draft (Gmail draft-only, no send tool), slack_send_message, save_comment (Linear), create_records_for_table (Airtable), manage_crm_objects. Closes HARDNESS discrepancy #3.
- `Reference/Council_Protocol.md` :: Council A (A1-A13) + Council B (B1-B11) templates, per-sub-dim scoring scheme, StarPM per-model density bands (40 design / 15 floor, NOT V3 50/40), unified verdict JSON schema.

## Delegated to councils (read by sub-agents, not directly)
- `Docs_starpm/7_QC_Spec_Doc1.json` :: Prompt QC sub-dim scoring (Council B-B1).
- `Evals_starpm/1_Prompt_Eval.md` :: prompt eval sub-dims (Council B).
- `_aux/Universe_Split/*` :: per-row grounding (Council A-A1/A3/A11).
