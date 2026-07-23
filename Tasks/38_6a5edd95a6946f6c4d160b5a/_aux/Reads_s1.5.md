# S1.5 Reads — Tasks/38_6a5edd95a6946f6c4d160b5a

## Runbook + specs
- Reference/Sessions/S1.5.md :: CB-mode + Class A skeptical-first decision flow; unconditional AUDIT on revise path per step 8.
- Reference/Linter_Playbook.md :: Class A pushback template (not used — REVISE path); voice-gate rules; forbidden-terms table.
- Reference/Sessions/AUDIT.md :: 9-lens strict veteran template used for the AUDIT sub-agent inline in S1.5.

## Per-task inputs
- Tasks/38_6a5edd95a6946f6c4d160b5a/5_Prompt.txt :: revised prompt (persona-neutral cleanup — drop "on my portfolio" possessive).
- Tasks/38_6a5edd95a6946f6c4d160b5a/2_Persona.txt :: rewritten to Brooke Phillips / Apartment Property Supervisor.
- Tasks/38_6a5edd95a6946f6c4d160b5a/PersonaBrief.txt :: rewritten to Brooke's canonical StarPM brief.
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Hardness_Plan.md :: 5 selected levers (L9, L11, L2, L8, L6) — verified all survive Brooke persona swap. Tony's L9 Slack post is C001 #maintenance public, not a DM.
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Universe.txt :: starpm.

## Universe ground truth checked
- StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md :: Denise (p_013) authoring guidance = "property-level operations, model after Lisa/Carlos rooted patterns but shift property and unit numbers"; Brooke (p_000) canonical scope = "cross-portfolio operations sync, vendor invoice approval, budget oversight, owner reporting, and the CapEx approval flow with owners" + signature scenarios `owner_capex_approval_roof` (leads, 8 actions) and `owner_portfolio_review_midyear` (leads, 4 actions, coordinates with Aurora Winona directly).
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Universe_Split/slack.slack_messages.json :: Tony's Sunset Ridge 208B AC Slack post at ts 1782914700 in channel C001 (#maintenance) is a public channel post ("Swung by 208B on Sunset Ridge this morning. Dirty filter tripped the unit... Got her penciled in for Thursday when I do the rest of the PM rounds. -Tony"). Brooke reads C001 same as any onsite PM.
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Universe_Split/slack.slack_users.json :: Brooke's Slack user id U9741B657FE with email brooke.phillips@starpm.com.

## Reports produced
- Tasks/38_6a5edd95a6946f6c4d160b5a/_aux/Validator_Reports/prompt.md :: PASS (0 fails, 3 warns). Warns are the coherence heuristic firing on a portfolio-brief structure where each item has its own entities and the coherence spine is the Aurora-brief framing — known false-positive class for portfolio-brief prompts.

## Platform linter output (input to this phase)
- Persona-scope complaint (Class A). Cited: (a) role stretch — Denise Onsite PM at own property, prompt covers 3 properties; (b) reporting to Aurora directly bypasses Brooke; (c) Tony Reyes cross-property reference elevated; (d) Ridgeview roof CapEx billing reconciliation + Linear issue update sits with Brooke.
