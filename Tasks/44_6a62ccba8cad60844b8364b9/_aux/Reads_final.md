# Reads log — PIPELINE FINAL · Task 44 (`44_6a62ccba8cad60844b8364b9`)

v11 E2 compliance gate. Every spec doc / Reference card / Eval spec / universe source read during this phase, one line each.

## Bootstrap + runbook

- `AGENTS.md` :: confirmed hard rules 1-13; confirmed StarPM V4 routing (rule 11 density is framework-scoped: V4 = 40+ average per model, 15 = QC-spec fail floor; the V3-family 50/40 bands do NOT apply); confirmed rule 4 injection is first-class for V4 and rule 13 F7/F8/F9 design-time enforcement.
- `Reference/Sessions/FINAL.md` :: confirmed 6-lens roster, the 11 binding hard-rule gates, the V4 extra-gate block (injection + submission_gate run BEFORE the council), and the STOP-gate contract (single-shot chat, no chaining to S4).

## Universe routing

- `Tasks/44_6a62ccba8cad60844b8364b9/_aux/Universe.txt` :: `starpm` — all spec routing goes to `Docs_starpm/` + `Evals_starpm/`; Brookfield `Docs/` and `Evals/` were NOT loaded.
- `_aux/Universe_Index/today_horizon.json` (via Hardness_Plan + validator reports) :: universe today `2026-07-01`, America/Chicago, active window 2026-05-01..2026-07-01.

## QC spec docs (StarPM)

- `Docs_starpm/7_QC_Spec_Doc1.json` :: enumerated the full scoring surface — Prompt 12 sub-dims (Unique Ground Truth, Feasibility, Explicit Tool Mention, Clarity/Specificity, Contrived/Unnatural, Truthfulness, Tool use and Cross-service requirement, Investigation, Coherence, Persona, Business Function, Alignment with Today's Date), Universe 2 (Universe Feasibility, Cross-service Coherence), OE 2 (OE Completeness, OE Accuracy), Rubric 5 (Overall Rubric Quality, All-Failing Rubrics, Rubric Category Balance, Process Rubrics, Agent Centric Phrasing), Trajectory 3 (Tool Call Count, Agent Failure Rate, Error Rate). Confirmed the 06/09 amendment removing the Unique Ground Truth middle band — two reasonable readings producing two different final universe states is now a hard FAIL even with a leading interpretation.
- `Docs_starpm/8_QC_Spec_Doc2.md` :: read via the Rubric self-containment rule the AUDIT relied on — the judge sees all rubric criteria and one rubric item may be used as context for another (this is what permits idx 36 not to re-name OPS-186 when idx 4 already does).

## Eval specs (StarPM)

- `Evals_starpm/5_Submission_Gate_Eval.md` + `Validators/v4_gates.py:511-514, 596-602` :: separated the two atomicity checks. **F6.1 NOT_ATOMIC** is a soft WARN heuristic (>=2 ID/money/email atoms in a title plus the token "and"), explicitly tagged "COUNCIL confirms". **F8 NON_ATOMIC_ENUM** is the hard FAIL gate (>=2 commas plus a trailing ", and X" plus a completeness/step predicate). The hard F8 gate did NOT fire on any of the 64 criteria; the three reported items are soft warns requiring council adjudication, not deterministic defects.
- `Evals_starpm/0_Injection_Quality_Eval.md` :: routed via `validate.py --phase injection` — 7 hard gates PASS, 4 COUNCIL notes (P4 contradiction review, P5 register match, P6 chain depth, P8 difficulty >= 3.5) fed to the Final Council.
- `Evals_starpm/4_Verifier_Fails_Eval.md` :: routed to the council for the Lens 6 bucket-classification simulation.
- `Evals_starpm/1_Prompt_Eval.md` / `2_OE_Eval.md` / `3_Rubrics_Eval.md` :: re-applied at the integration layer through the council's Lens 1-3.

## Reference cards

- `Reference/Council_Protocol.md` :: routed to the council as its instruction card (B3 density projection is the SSOT, framework-scoped).

## Prior-phase artifacts re-verified (NOT inherited)

- `_aux/Council_Reports/AUDIT_prompt.md` :: PASS (STRICT); 15 findings, 6 binding downstream; the validator's "bolt-on candidate" WARN on the opening sentence adjudicated a FALSE POSITIVE (anaphora chain the entity extractor cannot see); the "distinct services referenced: 2" NOTE adjudicated an inverted-signal regex artifact (the prompt names zero services).
- `_aux/Council_Reports/AUDIT_oe.md` :: PASS (STRICT) after two REVISE rounds; carries an explicit instruction that FINAL must **re-verify rather than inherit** council GO/NO-GO reasoning, and a THIN_BREADTH acceptance note (Linear share 56-64% vs the Hardness Plan's own <35% target).
- `_aux/Council_Reports/AUDIT_rubrics.md` :: PASS (STRICT) round 2; four round-1 findings closed; **N6 tagged `PROPAGATE TO S2` with an exact fix for FINAL to apply** (OE 36 `dated after 2026-07-01` -> `dated on or after 2026-07-01`). Applied this phase.
- `_aux/Hardness_Plan.md` :: 5 selected levers, 10 pre-registered constraints, and the S2-appended correction block (37 thread parents not 15; 18 HVAC ticket rows not "20+"; "Oakdale" absent; Lisa's ask 7 days after the wrap not 5).

## Universe sources independently queried this phase (`_aux/Universe_Split/`)

- `linear.linear_issues.json` (230 rows) :: verified every load-bearing state — OPS-87 `state_OPS_1`, OPS-96 `state_OPS_1`, OPS-98 `state_OPS_2`, OPS-97 `state_OPS_1`, OPS-99 `state_OPS_2`, OPS-108 `state_OPS_0`, OPS-40 `state_OPS_4`, OPS-91 `state_OPS_4`, OPS-186 `state_OPS_1` created 2026-06-17, OPS-35 `state_OPS_2`, OPS-43 `state_OPS_2`, OPS-56 `state_OPS_2`. Confirmed exactly **3 of 230** issues carry Jaime Salinas as assignee (OPS-87 / OPS-96 / OPS-98) and confirmed OPS-99 and OPS-108 carry byte-identical titles in opposing states.
- `slack.slack_messages.json` (580 rows, C001 = 104) :: verified all 15 cited `ts` values resolve to the exact quoted messages and authors; verified thread parentage by internal id (`8ce45073...` -> ts `1779308442.000001`; `7b8f1611...` -> ts `1779567943.000011`), so both load-bearing replies genuinely sit behind `slack_read_thread`. C001 census: 48 top-level / 56 replies / **37 distinct parents**, confirming the S2 correction block.
- `airtable.airtable_records.json` + `airtable_fields.json` + `airtable_tables.json` + `airtable_bases.json` :: one base `appPropertyOps`, two tables, `tblMaintenanceTickets` = 50 rows with exactly 4 fields (`fldTicketNumber` singleLineText / `fldDescription` multilineText / `fldPriority` singleSelect / `fldCompletionDate` date — no owner field, no status field). 18 of 50 rows carry the token HVAC; **0 rows** contain "cluster", "Preventive Maintenance Push", "condensate", "20x25" or "hose bib"; "Oakdale" absent.
- `gcalendar.gcalendar_events.json` (565 rows) :: Jaime has exactly 10 events, latest 2026-06-02; **0 events on or after 2026-07-01**. Nine confirmed universe-wide future events exist and **none references Jaime or the push** — F9 clean, with the 2026-07-15 Mesa Vista 4C QC inspection and the 2026-07-23 Q3 budget review carried as the two watch items no deliverable may contradict.
- `contacts.contacts.json` (61 rows) :: verified all seven persona emails and job titles named across the OEs and rubrics (Brooke Phillips Apartment Property Supervisor; Lisa Smith and Carlos Mendez Onsite Property Manager; John Smith, Elias Navarro, Tony Reyes Lead Maintenance Technician; Jaime Salinas Quality Control Inspector) — all `@starpm.com`.
- `Universe_complete_data.json` (4.44 MB) :: answer-leakage sweep on 27 conclusion phrasings, **0 hits**. The single "coverage gap" hit is OPS-121's unrelated "after-hours maintenance coverage gap" (staffing, not QC).

## Tool catalog

- `StarPM_Base_Universe/7_Server_Tools_Details.json` (268 tools) :: every one of the 25 tools named across the 38 OE steps exists under that exact name, and every parameter each OE binds exists on **that** tool. Spot-confirmed the StarPM-specific traps: `slack_send_message(channel_id, message)`, `create_draft(to, subject, body)` with no send tool, `save_issue(..., team, ...)`, `save_comment(issueId, body)`, `search_records(baseId, table, query)` vs `list_records_for_table(baseId, tableId)`, `create_records_for_table(baseId, tableId, records, typecast)`. Independently confirmed OE 29-33's claim that `save_issue.assignee` cannot carry a value: the catalog types it `{"required": "optional", "type": "null"}`, which validates the rubric design that requires the owner in the description text rather than as an assignment.
