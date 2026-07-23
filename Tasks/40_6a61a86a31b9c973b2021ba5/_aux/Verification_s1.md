# Verification — S1 prompt (Task 40, StarPM V4)

## Sources consulted

### Per-task data
- `_aux/Universe_Split/` :: grounded Mesa Vista Unit 7B, Tanya, Robert Finley, Hill Country, Tony Reyes against airtable_records, slack_messages, slack_users, quickbooks_entities, gmail_messages, gmail_threads.
- `_aux/Fact_Ledger.json` :: verified Tanya Mitchell (tenant), Robert Finley (owner), Diane Flores (Lonestar Account Rep — the very reason v4 anchored Diane to Hill Country), Tony Reyes (Lead Maintenance Technician). Confirmed no persona field regressed.
- `_aux/Hardness_Plan.md` :: 6 levers (L1/L2/L5/L7/L8/L9) preserved end-to-end in v4 prompt.
- `3_UniverseDataForThisTask.json` :: cross-checked 8 injected records — all LANDED per INJECT_CHECKER PASS; AUDIT round-2 re-verified.

### Eval spec
- `Evals_starpm/1_Prompt_Eval.md` :: all 12 sub-dims re-scored 5/5 at v4 (see block below).

### QC spec
- `Docs_starpm/1_Prompt_V3_Guidelines.md` :: hard rules re-verified (500-word cap, no em-dash, no tool names, no MCP names, no IDs, first-person voice, mid-thought entry).
- `Reference/Prompt_Format.md` :: format-card compliance re-verified.
- `Reference/Hardness_Playbook.md` :: 6 levers cited to StarPM adaptation table; L2 QB structured-DB skip + L7 multi-write + L8 multi-link + L9 authority dismissal + L1 latching + L5 thread-reply blindness all engineered into the prompt without leaking answers.

## Eval spec sub-dims (Evals_starpm/1_Prompt_Eval.md) verified — all 5/5 at v4
- 1.1 Unique Ground Truth :: 5/5 (single valid reading; second-reading attacks by Council B v4 all failed)
- 1.2 Feasibility :: 5/5 (all 8 writes achievable under StarPM 7_Server_Tools_Details.json)
- 1.3 Explicit Tool Mention :: 5/5 (grep -0 tool/MCP-server names)
- 1.4 Prompt Clarity & Specificity :: 5/5 (Diane anchored to Hill Country via `at Hill Country` + AP role + sender-path independence)
- 1.5 Contrived / Unnatural :: 5/5 (natural Carlos voice preserved through 3 trim passes)
- 1.6 Truthfulness :: 5/5 (Diane deadline attribution removed; all timeline anchors match injected timestamps)
- 1.7 Tool Use & Cross-Service :: 5/5 (8 services referenced across the trajectory)
- 1.8 Investigation :: 5/5 (Diane's diagnostic write-up on the bill + tenant-thread expansion)
- 1.9 Coherence :: 5/5 (sentence-removal test — each sentence advances the water-heater scope situation)
- 1.10 Persona :: 5/5 (formality 0.55, structured updates, Mesa Vista anchor honored)
- 1.11 Business Function :: 5/5 (Property Operations Cat 1)
- 1.12 Alignment with Today's Date :: 5/5 (all relative dates resolve against 2026-07-01 CDT + injected timestamps)

## Verification statements
- [x] Validator (`validate.py --phase prompt`) exit 0. v4 = PASS 0 fails, 0 warns, 7 notes (all relative-date cross-check reminders).
- [x] Council A v4 grounding + convention clean. Zero ungrounded claims. Two v3 A3 timeline defects resolved.
- [x] Council B v4 QC scoring — every applicable sub-dim = 5. Truthfulness + Clarity recovered from 4/5 to 5/5 after v4 fixes.
- [x] Similarity gate (`calc_similarity.py`) composite 29.1 << 40.
- [x] AUDIT round-2 verdict = PASS (STRICT). All 4 round-1 findings resolved.
- [x] Regression-anchor suite 48/48 PASS this session.

## Discrepancies surfaced
- None outstanding. All revision-round discrepancies (v1 dual BLOCK → v2 Council A BLOCK on A3 → v3 councils GO but AUDIT REVISE on 4 minor → v4 councils + AUDIT PASS STRICT) resolved in-place. THIN density carry documented in Hardness_Plan.md per AUDIT F3.

## Revision history
- v1: Council A BLOCK (A3 timeline "yesterday" for Tony) + Council B BLOCK (3 Major L9/L5/Clarity + 1 Moderate THIN + 2 Minor).
- v2: L9 fix (skepticism removed), L5 fix (escalation-content leak removed), Slack thread anchor fix, Council B GO with THIN carry; Council A still BLOCK on 2 A3 (Diane email + ticket creation timestamps).
- v3: Prompt aligned to injected timestamps ("that afternoon" for Diane email; "Monday night" for ticket creation). Both councils GO. AUDIT REVISE — 4 minor findings.
- v4: Diane vendor anchor added; false-Diane-attribution deadline removed; word count trimmed; Hardness_Plan.md THIN carry footnote codified. Both councils GO. AUDIT PASS (STRICT).

## Verdict
PASS — S1 v4 cleared validator, Council A, Council B, and AUDIT (STRICT). Ready for S2.
