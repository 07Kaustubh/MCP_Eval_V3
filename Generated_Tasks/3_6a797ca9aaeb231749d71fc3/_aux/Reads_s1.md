# Reads - S1 (Generated_Tasks/3_6a797ca9aaeb231749d71fc3)

## Reference cards
- `Reference/Sessions/S1.md` :: full runbook internalized (steps 0-9, AUDIT auto-fire Track F v21 conditions).
- `Reference/Prompt_Format.md` :: hard rules (500-word cap, no em-dash, no tool names, no MCP-server names, no internal IDs, no pre-solving), voice principles (mid-thought entry, asymmetric knowledge, emotional texture, persona register), structure (trigger / context / asks), name-swap test, HG deltas (weekend rule, Q1 incoherence risk, persona-email resolution rule, triple density thresholds).
- `Reference/Hardness_Playbook.md` :: 11-lever catalog, composition rules (4-5 levers default), HG framework-scoped density scheme (40+ calls AND 3+ services, not V3-family 50/40).
- `Reference/Council_Protocol.md` :: Council A perspectives A1-A13 (post-v18 trim to 9 active) and Council B perspectives B1-B11 (post-v18 trim to 8 active). Bar = 5/5 on every applicable QC sub-dim. Prompt templates for both councils.

## Framework specs (HarmonyGames)
- `Docs_harmonygames/4_Prompt_Hard_Tips.md` :: agent-behavior anchors (broad-search / structured-DB-skip / thread-reply blindness / latching-first-framing / dispute-without-reply). Persona ACL derivation rule. Difficulty calibration (authoring target vs prompt-eval hard gate vs trajectory floor).
- `Docs_harmonygames/9_Common_Error.md` :: prompt errors (giving away discoveries, tool-scripting, MCP-function naming, pre-solving, bolt-on asks, unavailable actions, action ambiguity, broken relative time, threshold confusion). Persona ACL errors. Confirmed writes-are-outside-ACL and gmail-is-read-only-no-draft.
- `Reference/AGENTS.md` :: HG hybrid framework `hg`, working directory `Generated_Tasks/`, four unscoped services (contacts, github, trello, linear), seven scoped services (gmail, gcal, gdrive, gdocs, gsheets, gslides, slack).

## QC spec (HarmonyGames)
- `Docs_harmonygames/7_QC_Spec_Doc1.json` (per hardness verification): Trajectory Tool Call Count floor 15 average; authoring target 40+ AND 3+ services; Universe Feasibility binary; Cross-service Coherence binary; Prompt Category Balance is 40% Process CAP (binary), zero Process is valid.
- `Docs_harmonygames/8_QC_Spec_Doc2.md` (per hardness verification): severity taxonomy pre-swap (Overly Broad = Moderate; Overly Specific = Minor here — REVERSED from StarPM). Percentage bands identical.

## Cross-task learnings
- `Tasks/_meta/Learnings.md` (L1-L35): consulted for lever design (L6 hard rule "never put correct answer in body"; L7 hard rule "never design task where answer is `it is not there`"; L9 authority dismissal as most effective single mechanism; L10 SAP-subledger-style skip mapped to HG structured-DB skips on `github.review_comments` + `trello.check_items`; L13 first-framing anchor; L15 hard rule "never hint the answer is wrong"; L24 soft-verb convention on prompt-side L9; L25 existing-artifact-anchor supersession trap; L33 design for margin not for a number).

## Reference V5 HarmonyGames QC_Passed samples
- `QC_Tasks/V5_HG_Buckets/QC_Passed/Task2_6a62909d918832d268962da6_HG/5_Prompt.txt` :: voice-calibration reference for a review-control audit shape (Sequencer 2.0 huddle-bookends prompt). Confirmed: three-paragraph shape, situation-first opening, deliverable named at end, no em-dashes, no tool names, natural product references (`GameOfDominoes`, `#executives`, spreadsheet, ticket).
- `QC_Tasks/V5_HG_Buckets/QC_Passed/Task3_6a63e91c02df598d950da85f_HG/5_Prompt.txt` :: voice-calibration reference for casual mid-thought entry ("can you get the source handoff pack Arthur and I talked about over the line?") pointing to a Slack channel for environmental steering.

## Per-task setup (S0 + HARDNESS outputs consumed)
- `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/_aux/Universe_Split/*` :: 39 service files; grounded every named entity in the prompt (Combo-Fighters repo, Zombie Match 3D roadmap board, ART tracking ticket lineage, four Marcus identities, Leonard as authority speaker, Leapblock + Martin Walsh as vendor followups).
- `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/_aux/Universe_Index/today_horizon.json` :: universe today 2026-02-28 America/Chicago. Confirmed today is Saturday; framed dismissal as Friday-evening quote to clear weekend-comms rule.
- `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/_aux/Universe_Index/entities_personas.md` :: confirmed persona/npc split (Leonard Hayes persona, Martin Walsh persona, Leapblock as contact, four Marcus identities present as distinct rows).
- `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/_aux/Hardness_Plan.md` :: 5 levers (L1 latching, L2 dual carrier structured-DB skip, L6 Marcus disambiguation, L9 Friday-evening authority dismissal, L10 supersession); density midpoint 56 across 7 services; post-ACL revision confirmed Slack fully excised.
- `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/PersonaBrief.txt` :: Victor Barnes, Game Engineer, actual scope art/animation lead; confirmed voice register (technical engineer with vendor-management responsibilities).
- `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/1_Business_Function.txt` :: Engineering (matches HG Engineering & Live-Ops 25% slice).
- `Generated_Tasks/3_6a797ca9aaeb231749d71fc3/2_Persona.txt` :: Victor Barnes, Game Engineer.
