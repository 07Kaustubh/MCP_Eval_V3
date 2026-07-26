# Reads — S1 (Tasks/40_6a614767cd5b60ad96902fb4, universe=starpm/V4)

Reference / spec / eval docs consulted this phase, one line each.

## Runbook + protocol
- Reference/Sessions/S1.md :: the S1 procedure, exit criteria, STOP gate, AUDIT auto-fire conditions.
- Reference/Council_Protocol.md :: Council A (explore) + Council B (oracle) prompt-phase perspectives, prompt-sub-dim scoring scheme map (1/3/5 vs 1/5 binary vs 3/5), StarPM OE-service map.
- Reference/Templates/Verification_phase.md.template :: canonical Verification_<phase>.md sections (Sources consulted / Verification statements / Discrepancies / Verdict) required by check_verification.py.

## Format + hardness cards
- Reference/Prompt_Format.md :: hard rules (500-word cap, no em/en dash, no tool/MCP names, no internal IDs, no pre-solving), voice (mid-thought, asymmetric knowledge), natural surface naming allowed (email/Slack/calendar), 3+ writes across 3+ services.
- Prompt_Guidelines.md :: anti-patterns (QC-sample cliches, command-list, over-signaling investigation, generic urgency); "runny" voice principles.
- Docs_starpm/4_Prompt_Hard_Tips.md :: Opus failure modes (skips structured DBs, latches on first framing, misses replies, data past search-cap invisible); linked-edit-chain difficulty; push tool calls > 40 with multi-write.
- Docs_starpm/6_Prompt_Relative_Time_Updates.md :: StarPM today = July 1, 2026 (Wed); relative-time inference allowed; quarter-boundary (Q3/H2 start) coherence note.

## Universe + design inputs
- Tasks/40_.../_aux/Hardness_Plan.md :: 5 selected levers (S1 possession-hold/L31 Gemini stump; S2 stale-plan latching/L8-L13; S3 HubSpot ESA skip/L10 Opus stump; S4 Unit-14 near-miss/L4; S5 owner-approved authority anchor/L9) + density midpoint 48 + Hardness Brief for the prompt writer.
- Tasks/40_.../PersonaBrief.txt :: Lisa Smith, Onsite PM, Property Operations, warm-professional/thorough/calm, leads fair-housing accommodation, drives make-ready.
- Tasks/40_.../1_Business_Function.txt + 2_Persona.txt :: Property Operations / Lisa Smith Onsite Property Manager.
- Tasks/40_.../_aux/Universe_Index/today_horizon.json :: universe today 2026-07-01 America/Chicago (authoritative; overrides validator's null-fallback 2026-06-12).
- Tasks/40_.../_aux/Fact_Ledger.json :: atom surface (emails/amounts/dates/ids) + lifecycle (today=null -> validator Brookfield-default artifact, surfaced as discrepancy).
- Tasks/40_.../_aux/Universe_Split/ :: 8 services (airtable, contacts, gcalendar, gmail, hubspot, linear, quickbooks, slack); grounding source of truth.
- Validators/universes.py :: registry confirms starpm today=2026-07-01 tz=America/Chicago; density framework v4 (40 design / 15 floor per model).

## Voice references (STRUCTURE ONLY — content is Brookfield-flavored, not StarPM facts)
- QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/5_Prompt.txt :: winning register (mid-thought first person, trigger + believed context + woven investigate-and-write asks, 270-364 words, "don't take it at face value / hold it / leave a paper trail" pattern).

## QC spec + eval (authoritative scoring delegated to Council B)
- Docs_starpm/7_QC_Spec_Doc1.json :: Prompt-dimension sub-dims + 1/3/5 vs binary schemes (applied via Council_Protocol scheme map; full JSON scored by Council B).
- Evals_starpm/1_Prompt_Eval.md :: Prompt eval sub-dims 1.1-1.12 (scored by Council B; verdicts recorded in Verification_s1.md).
