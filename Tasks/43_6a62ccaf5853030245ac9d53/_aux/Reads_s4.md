# Reads — PIPELINE S4 · Task 43_6a62ccaf5853030245ac9d53 (v11 E2 compliance log)

## Eval specs
- `Evals_starpm/4_Verifier_Fails_Eval.md` :: bucket taxonomy (Rubric Invalid / Judge Error / Legit Fail) re-applied per model. Confirmed the eval mandates one run per model, so the classification loop ran twice (Opus 4.8 set, Gemini set) over the same 25-rubric surface.
- `Reference/Sessions/S4.md` :: procedure, T2/T3 hard gates, v15 5-point pre-write checklist, All-Failing Rubrics sub-dim threshold table.

## QC spec
- `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md` (via the FINAL-phase coverage record) :: trajectory sub-dims T1 density / T2 pass@1 / T3 error rate; density fail floor 15, design target 40 average per model.
- `AGENTS.md` hard rule 11 :: V4 density is per-model, 40 design target, 15 fail floor. Confirmed the Brookfield 50/40 scheme does NOT apply here.

## Per-task data (ground truth re-derived from source, not from upstream phase claims)
- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` :: the four AP bills + AR invoice 2026-534 pulled by id and re-read field by field.
- `_aux/Universe_Split/contacts.contacts.json` :: Tony Reyes = `tony.reyes@starpm.com`, Lead Maintenance Technician (internal); Pete Donovan = `pete.donovan@gmail.com`, Exterior Painter (outside); Linda Castillo = Property Owner.
- `_aux/Universe_Split/gmail.gmail_messages.json` :: message `5101c5a41dffa90a` (thread `66132537181ecbe1`), the 2026-06-02 owner summary, body decoded from base64.
- `_aux/Universe_Split/slack.slack_messages.json` (via trajectory results) :: C004 line "Jaime flagged a paint touch-up on the bedroom closet trim. Tony got it done today."
- `_aux/Universe_Split/airtable.airtable_records.json` :: the two 4C make-ready rows `recc8534b3fd13954` (selReady, live) and `recbd087a4abd605b` (selProg, stale).
- `_aux/Fact_Ledger.json` :: amount atoms cross-checked (1622 / 1140 / 95 / 387 / 1340 / 85 present; 1812 absent, confirming derive-only).

## Task artifacts
- `5_Prompt.txt`, `6_Oracle_Events.txt` (OE 3 / 4 / 5 / 7 / 17 / 18 / 19 / 21 / 24 / 25 / 26 / 27), `7_Rubrics.json` (all 25).
- `8a_Verifier_Fails_Opus.txt` + `8b_Verifier_Fails_Gemini.txt` :: 12 run blocks, 25 graded rows each, 300 cells total.
- `Agent_Responses/{Opus,Gemini}/trajectory-run-{1..6}.json` :: all 12 walked call by call.
- `_aux/Hardness_Plan.md` :: 4 stump predictions + the FINAL-council carry-forward re-attribution.
- `_aux/Verification_final.md` :: FINAL discrepancy log, especially the closet-trim adjudication and the Gemini THIN-density watch-item.

## Tool catalog
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: gmail surface is `search_threads` / `get_thread` / `create_draft` / `list_drafts` / label tools only. There is no `get_message` or `read_message`. `get_thread` returns `payload.body.data` base64-encoded. This is what made the base64 finding below decisive.
