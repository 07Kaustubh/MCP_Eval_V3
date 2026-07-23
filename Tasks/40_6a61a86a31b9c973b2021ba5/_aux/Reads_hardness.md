# Reads log — HARDNESS phase

v11 E2 compliance: every QC spec doc / Reference card / Eval spec / Learnings entry consulted.

## Reference cards
- `Reference/Sessions/HARDNESS.md` :: procedure, 6-section Hardness_Plan template, StarPM Injection Plan requirement, tiered density gate (PASS >=50, THIN 40-49, INSUFFICIENT <40), lever gate (>= 3), Phase 8 difficulty targets for StarPM (Cross-Service Spread >= 4 / Tool Call Depth >= 3.5 / Reasoning Chain >= 3.5)
- `Reference/Hardness_Playbook.md` :: 11-lever catalog with per-lever tool-call cost ranges, composition rules, StarPM adaptation section, L12 document cross-reference lever (StarPM-specific)

## Learnings (Tasks/_meta/Learnings.md, L1-L31)
- L1-L7 :: what does NOT reliably fail Opus 4.8 — do not rely on single-hop, near-miss-only, action-incompleteness-only, binary "is it posted?", or correction-emails-that-state-answer
- L6 (HARD) :: correct answer NEVER appears in any email/slack/document body
- L7 (HARD) :: never design "the JE / record is not there" as the answer — plant wrong data instead
- L8 :: three reductions across three services is the target pass@1 ~40% anatomy
- L9 :: authority-figure dismissal is the single most effective mechanism (~100% fail alone)
- L10 :: SAP subledger invisibility — for StarPM this maps to QuickBooks queries and Airtable Make-Ready record queries
- L15 (HARD) :: implicit prompts only — persona believes the wrong number, agent must self-discover
- L18 :: the derived figure IS the rubric — enumerate intermediate wrong answers
- L23 :: dollar-threshold filter blindness (structural stump on AP triage tasks)
- L25 :: existing-output anchor trap — plant a superficially matching artifact missing 1-2 rubric-tested fields
- L26 :: decoy parent thread — plant a competing Slack thread in the same channel on overlapping keywords with a more-recent ts
- L27 :: soft-instruction over-compliance — scope explicit writes or add a second authority endorsement
- L28 :: tool-variant trap — plant similar existing doc to trigger version-bump path over fresh-upload path
- L29 :: escape-valve clauses neutralize L2 on the surface they point at
- L30 :: rubric-persona-attribution cascade — every rubric named-person must be re-checked against prompt recipient
- L31 (StarPM, CRITICAL) :: single-cycle QC closeout scenarios are structurally density-thin; require Hardness_Plan midpoint >= 55 before trusting real-run floor will clear 40. Must include at least one additional service-interaction chain requiring a multi-step lookup before a write (e.g., QuickBooks or HubSpot record tied to closeout, second Airtable table verification, or a second Slack surface with non-trivial prior-thread lookup)

## Eval spec (StarPM V4)
- `Evals_starpm/1_Prompt_Eval.md` (deferred to S1)
- `Evals_starpm/2_OE_Eval.md` (deferred to S2)
- `Evals_starpm/3_Rubrics_Eval.md` (deferred to S3)
- `Evals_starpm/4_Verifier_Fails_Eval.md` (deferred to S4)
- HARDNESS applies eval sub-dim `Trajectory > Tool Call Count` (floor >= 15 per Eval; pipeline design target midpoint >= 50, real-run floor >= 40)

## QC spec (StarPM V4)
- `Docs_starpm/1_Prompt_V3_Guidelines.md` (deferred to S1)
- `Docs_starpm/2_Rubrics_V3_Guidelines.md` (deferred to S3)
- `Docs_starpm/4_Prompt_Hard_Tips.md` :: confirmed the 11-lever catalog is derived from this doc; StarPM adaptation preserves the same failure modes with service-name substitutions
- HARDNESS applies QC sub-dim `Trajectory > T1 Tool Call Count`

## Per-task inputs
- `Tasks/40_6a61a86a31b9c973b2021ba5/PersonaBrief.txt` :: Carlos Mendez, Onsite PM, 33 scripted actions across 11 scenarios; anchors Mesa Vista / Las Palmas / Rio Bend; touches Airtable + Slack #make-ready + #maintenance + Gmail + Linear
- `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/S0_Setup_Report.md` :: universe today 2026-07-01 (canonical zone America/Chicago); no oracle_gl, no filesystem MCP; write surface = Gmail draft (no send) + Slack + Linear + Airtable + QuickBooks + HubSpot + GCalendar + Contacts
- `Tasks/40_6a61a86a31b9c973b2021ba5/_aux/Universe.txt` :: starpm (V4 pipeline path — INJECTION phase required before S1)
