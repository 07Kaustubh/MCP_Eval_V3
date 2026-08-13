# FINAL Phase Reads Log — HarmonyGames Task 3_6a797ca9aaeb231749d71fc3

v11 E2 compliance gate. Every spec / reference / eval doc consulted during FINAL is logged with a one-line summary.

## Root bootstrap
- `AGENTS.md` :: read hard rules 1-34 + HG-U pinned deviations; universe `harmonygames` framework `hg`, model under test Opus 4.7, universe today 2026-02-28 (America/Chicago, Saturday), Generated_Tasks/ routing, dual-artifact pipeline (single-model verification + V4 injection/submission_gate)
- `Reference/AGENTS.md` :: card + runbook index; confirmed FINAL.md is the correct runbook to bootstrap from
- `Reference/Sessions/FINAL.md` :: read entire 286 lines; procedure confirmed - 6 lenses (Truthfulness / Rubric-Binding / Cross-Artifact Holism / Red-team / Narrative-State + Action-Prescription / Verifier-Fails-Spec Pre-Upload); STOP after PASS

## Artifacts in scope
- `5_Prompt.txt` :: Victor Barnes, art-import status brief for Leonard by Monday; anchors on Leonard's Friday-evening "Marcus told me the import PR is already covered by the merged VFX branch, treat that draft as parked" dismissal
- `6_Oracle_Events.txt` :: 30 OEs covering GitHub Combo-Fighters PR walk, Trello ZM ROADMAP checklist descent, Marcus disambiguation across Contacts + Linear + GitHub, Linear ART tracker resolution + comment, Trello card update + comment, GDocs status brief, GSheets vendor tracker, reply framing
- `7_Rubrics.json` :: 29 rubrics; category distribution TBD after read
- `_aux/Hardness_Plan.md` :: 5 levers selected (L1 Latching, L2 Structured-DB skip, L6 Near-miss entity, L9 Authority dismissal, L10 Reversal/supersession); post-ACL revised anchors (all levers on unscoped surfaces; density midpoint 56 across 7 services)
- `_aux/Fact_Ledger.json` :: atom surface for grep-truthfulness
- `_aux/Universe_Split/` + `_aux/Universe_Index/` :: HG per-task split source of truth
- `_aux/Verification_s1.md` / `Verification_s2.md` / `Verification_s3.md` :: prior-phase verifications

## Eval specs re-applied at integration layer
- `Evals_harmonygames/1_Prompt_Eval.md` :: Prompt phase eval; F0 injection ready + F1 density gate (>15 necessary calls AND 2+ services) + F2 tool feasibility (V5 A1 retired-servers)
- `Evals_harmonygames/2_Oracle_Events_Eval.md` :: OE eval; forward/reverse coverage, tool-parameter binding
- `Evals_harmonygames/3_Rubrics_Eval.md` :: rubric eval; HG 40% Process cap (binary); negative criteria dimension 23; vague exemplar
- `Evals_harmonygames/4_Verifier_Fails_Eval.md` :: bucket classification (1 Rubric Invalid / 2 Judge Error / 3 Legit AF) - drives Lens 6
- `Evals_harmonygames/5_Submission_Gate.md` :: HG hg_f1_f6 defect families (F1-F6 with HG-authored triggers per HG-U10)

## QC spec (HG-scoped - NEVER cross-load another universe's spec)
- `Docs_harmonygames/7_QC_Spec_Doc1.json` :: 7 dims / 38 sub-dims, 18 BINARY; density is three normatively separated thresholds; rubric balance is 40% Process cap flat binary; Alignment-with-Today's-Date NOT binary here
- `Docs_harmonygames/8_QC_Spec_Doc2.md` :: severity reversed vs StarPM (Overly Broad = Moderate, Overly Specific = Minor); negative-criteria dim 23 pre-scan + prompt-mandate adjudication; vague exemplar dim = Moderate per instance
- `Docs_harmonygames/14_Persona_ACL.md` :: 7 scoped services (gmail, gcal, gdrive, gdocs, gsheets, gslides, slack); 4 unscoped (contacts, github, trello, linear); ACL does NOT govern writes; :132 forbids making an ACL write denial necessary to prompt/OE/rubric

## Reference cards consulted
- `Reference/Council_Protocol.md` :: council structure + B3 density SSOT (HG uses framework `hg` thresholds not V3-family 50/40 scheme)
- `Reference/Hardness_Playbook.md` :: lever catalog reference for cross-verification
- `Reference/OE_Format.md` :: OE structural convention grounding
- `Reference/Rubric_Format.md` :: rubric convention grounding

## Cross-task learnings
- `Tasks/_meta/Learnings.md` :: empirical Opus failure modes (L1-L28 refs used in Hardness_Plan)

## Verification statements
- All 3 deliverables + Hardness_Plan + Fact_Ledger + Universe_Split + Universe_Index read together as the FINAL integration layer
- 4 eval specs re-applied
- HG QC spec dims mentally walked
- Slack/gmail service constraints (HG-specific: gmail read-only, Slack persona-ACL blocked for Victor) verified against ACL doc
- FINAL runbook procedure Steps 0-5 walked; all 6 lenses to be applied by council
