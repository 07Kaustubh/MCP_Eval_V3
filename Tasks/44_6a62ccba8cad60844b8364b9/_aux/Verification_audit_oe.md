# Verification — AUDIT (phase: oe) · on-demand Mode 2

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** `starpm` (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Artifact:** `6_Oracle_Events.txt` — 38 steps, 0 em-dashes, 0 unknown tool names, 0 meta-tags
**Invocation:** `PIPELINE AUDIT — … --phase all` (fresh chat, on-demand Mode 2), 2026-07-26. Report: `_aux/Council_Reports/AUDIT_all.md`.
**Prior S2 auto-fire pass preserved at** `_aux/Council_Reports/_superseded/audit_ondemand_prev/Verification_audit_oe.md`.

## Strictest interpretation re-applied

- Every "should" in `Evals_starpm/2_OE_Eval.md` read as "must".
- Every NON-FAIL middle band collapsed to REVISE. OE Completeness and OE Accuracy have no FAIL band in the StarPM spec, so the strict bar is the 5/5 Pass text, not the absence of a FAIL.
- Density bar framework-scoped to StarPM V4 (>= 40 per model). The V3-family 50/40 scheme was NOT applied.
- Every soft convention in `Reference/OE_Format.md` and `Reference/OE_Convention_Inventory.json` treated as binding.
- OE ordering treated as unordered for coverage and ordered where lifecycle preconditions apply, per the AGENTS.md deviations table.

## Sources consulted

- **Per-task data** — `3_UniverseDataForThisTask.json` (3,892 rows) and `_aux/Universe_Split/` (linear 230 issues / 48 comments / 5 states, slack 580 messages, airtable, gcalendar, contacts, hubspot, quickbooks), `_aux/Fact_Ledger.json`, `_aux/Feasible_Surface.json`, `_aux/Universe_Index/today_horizon.json`, `_aux/Hardness_Plan.md`.
- **Eval spec** — `Evals_starpm/2_OE_Eval.md` (primary for this phase), plus `Evals_starpm/5_Submission_Gate_Eval.md` and `Evals_starpm/0_Injection_Quality_Eval.md` executed deterministically.
- **QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` Dimension 3 and `Docs_starpm/8_QC_Spec_Doc2.md`. `Docs_starpm/13_QC_Companion.md` deliberately excluded (Brookfield-contaminated).
- **Tool catalog** — `StarPM_Base_Universe/7_Server_Tools_Details.json` (276 names; every OE-named tool and parameter checked).
- **Prior council reports** — re-read to spot pattern misses, not trusted as ground truth: `Council_Reports/{S2_A_grounding,S2_B_adversarial,AUDIT_oe,FINAL_council,QC_Strict_Check,S4_verdict,S4_fixes,verify_universe_atoms}.md`.
- **Cross-task** — `Tasks/_meta/Learnings.md`, `AGENTS.md`, `Reference/OE_Format.md`, `Reference/OE_Convention_Inventory.json`.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)

- `_aux/Universe_Split/linear.linear_issues.json` (230 rows) + `linear.linear_workflow_states.json` (5 rows) :: every `state_id` referenced by an OE re-resolved through the states table. OPS-16/17/18/34/35/40/43/44/51/56/66/71/79/81/87/91/96/97/98/99/108/186 all re-pulled and compared field-by-field against the OE text.
- `_aux/Universe_Split/linear.linear_comments.json` (48 rows) :: comments on OPS-43, OPS-56, OPS-81, OPS-87, OPS-96, OPS-97, OPS-98, OPS-108 re-read verbatim.
- `_aux/Universe_Split/slack.slack_messages.json` (580 rows; C001 = 104) :: full C001 re-read sorted by `created_at`, including the four thread replies the OE cites by `ts`.
- `_aux/Universe_Split/airtable.airtable_records.json` + `airtable_tables.json` + `airtable_fields.json` :: `tblMaintenanceTickets` field set (4 fields, no owner, no status) and the 50-row / 18-HVAC tally re-derived.
- `_aux/Universe_Split/gcalendar.gcalendar_events.json` :: forward sweep from 2026-07-01 re-run.
- `_aux/Universe_Split/contacts.contacts.json` + `hubspot.hubspot_objects.json` :: job titles for all six named owners plus Brooke re-confirmed.
- `_aux/Fact_Ledger.json`, `_aux/Feasible_Surface.json` (15 tables with enum maps) :: re-loaded by the validator during this pass.
- Tool catalog: `StarPM_Base_Universe/7_Server_Tools_Details.json` — every tool named in an OE body checked against the catalog; 0 unknown names, 0 wrong-parameter bindings.

## Eval spec verified for this phase

- `Evals_starpm/2_OE_Eval.md` :: strictest reading applied. Phase 3.2 dependency-chain ordering satisfied (OE 9 `list_issue_statuses` precedes every state-reading step; OE 24 schema read precedes OE 28 write; OE 26 contact resolution precedes OE 38 draft).
- `Evals_starpm/5_Submission_Gate_Eval.md` :: run deterministically, 0 fails.

## QC spec re-verified (`Docs_starpm/`)

- `Docs_starpm/7_QC_Spec_Doc1.json` Dimension 3 (OE), 2 sub-dims, rescored below.
- `Docs_starpm/8_QC_Spec_Doc2.md` :: "OEs describe steps — not what the final response should say" applied when checking whether the ten final-response criteria need their own OE step (they do not).
- `Docs_starpm/13_QC_Companion.md` NOT consulted (Brookfield-contaminated).

## Per-atom evidence table (v18 — required for the OE Accuracy 5/5)

| Atom asserted in an OE | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| OE 9: five states `state_OPS_0..4` = Backlog/Todo/In Progress/In Review/Done on team_001 | `linear_workflow_states` | exactly 5 rows, ids and names match in order | PASS |
| OE 12: OPS-87 state Todo, created 2026-05-24, "moved both from In Review to Done" | `linear_issues WHERE id='OPS-87'` | `state_OPS_1`, created 2026-05-24, description matches verbatim | PASS |
| OE 13: OPS-96 state Todo, comment 2026-05-30 "spot-check across all units" | `linear_issues` + `linear_comments WHERE issue_id='OPS-96'` | `state_OPS_1`; comment 2026-05-30T05:31 "Ran a spot-check across all units this morning" | PASS |
| OE 14: OPS-98 state In Progress, two comments 2026-05-25 09:00 / 14:00 | same | `state_OPS_2`; both comments present, second reads "I'm moving both cluster issues to Done" | PASS |
| OE 15: OPS-40 and OPS-91 in state Done (the overclaim bound) | `linear_issues` | OPS-40 `state_OPS_4` completed 2026-05-18T11:54; OPS-91 `state_OPS_4` | PASS |
| OE 17: OPS-43 In Progress, two 2026-05-14 comments (drain flush, no-access reschedule with Carlos) | `linear_issues` + `linear_comments` | `state_OPS_2`; description carries both flags verbatim | PASS |
| OE 18: OPS-56 In Progress; two North units pending on tenant scheduling; ask to Carlos in both comments; no reply in the 48-comment corpus | `linear_issues` + full `linear_comments` scan | `state_OPS_2`, created 2026-05-18T22:48; comments 2026-05-19T13:13 and 2026-05-20T15:19 both carry the ask; no closing reply exists | PASS |
| OE 19: OPS-97 Todo, "Moving this to In Progress" | `linear_issues WHERE id='OPS-97'` | `state_OPS_1`, description ends "Moving this to In Progress" | PASS |
| OE 20: OPS-35 In Progress (Lisa onsite lead, John execution lead); OPS-186 Todo created 2026-06-17, "West Cluster work still underway" | `linear_issues` | both exact; OPS-186 is the **only** record in all 230 containing "electrical" | PASS |
| OE 21: OPS-99 In Progress / OPS-108 Backlog, byte-identical titles, both assigned Elias | `linear_issues` | `state_OPS_2` / `state_OPS_0`, titles byte-identical, both `assignee_id` = Elias Navarro | PASS |
| OE 21: OPS-16/17/18 are the Summer HVAC scope issues naming only South, East, North | `linear_issues` | all three name South + East + North, none names West | PASS |
| OE 24: `tblMaintenanceTickets` has exactly 4 fields, no owner, no status; description ends "Linear is secondary" | `airtable_fields` + `airtable_tables` | fldTicketNumber / fldDescription / fldPriority / fldCompletionDate; description matches | PASS |
| OE 25: 50 rows, 18 carry HVAC, 0 reference a cluster / the push / 20x25 / hose bib / condensate drain | `airtable_records WHERE table_id='tblMaintenanceTickets'` | 50 rows, 18 HVAC, 0 on all five push tokens | PASS |
| OE 23: Jaime has 0 events on/after 2026-07-01; 9 forward-dated confirmed events universe-wide, none touching the push; Mesa Vista 4C QC inspection 2026-07-15 | `gcalendar_events` | exact; the 2026-07-15 row is the single `verify_universe_atoms` WARN and is reconciled below | PASS |
| OE 5 / OE 6: the four load-bearing thread replies exist at the cited `ts` under the cited parents | `slack_messages` | `…444.000003`, `…445.000004` under parent `8ce45073…`; `…569323.000012` under parent `7b8f1611…` | PASS |

Empty evidence cells: **none**. OE Accuracy scored 5/5 on this table.

## Per-universe landmines (StarPM) re-checked

| Landmine | Status in the OE |
|---|---|
| Near-duplicate decoys | Not engaged, but the OE builds the **same defence pattern** on the universe's own duplicate pairs: OE 21 forces the agent to cross-check OPS-99 vs OPS-108 against the state column rather than the identical title. Correct application of the landmine discipline. |
| Cross-property "Unit 14" | Not engaged. |
| Tanya Mitchell contradiction | Not engaged. |
| Airtable-is-source-of-record vs Linear-secondary | OE 8 and OE 24 both surface the routing rule from the records themselves (`team_001` description and the table description), and OE 28 vs OE 29-33 implement the split. **Correct.** |
| Parameter traps (`slack_send_message(message)`, `create_draft(body)`, `save_issue(team)`, `save_comment(issueId, body)`, camelCase `baseId`/`tableId`) | Every OE write step uses the StarPM parameter names, not the Brookfield/MoveOps ones. OE 37 uses `message`, OE 38 uses `body`, OE 29-33 use `team`, OE 34-35 use `issueId`+`body`, OE 24/25/28 use `baseId`/`tableId`. **0 trap hits**; regression anchors SP-7/SP-8/SP-9 confirm the detector for these is live. |

## All 9 lenses status (OE scope)

- Lens 1 strict QC scoring :: **PASS** — both OE sub-dims at 5
- Lens 2 answer-leakage sweep :: **PASS** (OE is not agent-visible; checked anyway for the aggregate conclusion appearing in a quoted universe string — none)
- Lens 3 hardness end-to-end (OE-side exercise) :: **PASS with note** (Lever 5's two OE steps are correct but the mechanism is inert; see below)
- Lens 4 strict density :: **PASS** (empirical, per model)
- Lens 5 adversarial review :: **PASS**
- Lens 6 :: RETIRED v18 — not executed
- Lens 7 anti-rationalization :: **PASS**
- Lens 8 regression-anchor verification :: **62/62 PASS**
- Lens 9 :: RETIRED v18 — not executed

## Sub-dim scoring (Dimension 3 — OE, 2 sub-dims)

| Sub-dim | Score | Basis under strictest reading |
|---|---|---|
| OE Completeness | 5 | Full critical path present: discovery (OE 1-11, 22-27), dependency chain (OE 12-21), write actions (OE 28-38). Every graded write has an OE. The ten final-response criteria carry no OE step, which `Docs_starpm/8_QC_Spec_Doc2.md` explicitly permits ("OEs describe steps — not what the final response should say"), and every fact they grade is reachable on the OE path. |
| OE Accuracy | 5 | 14/14 atoms in the table above exact. Tools, services, parameters and expected values all match the catalog and the split. Following the OEs literally produces a correct trajectory — confirmed empirically: 12/12 runs parsed `ok`, 0 errors. |

## Notable OE strengths confirmed at source

- **OE 15 scopes the load-bearing determination correctly.** It states the finding as "none of Jaime's three QC spot-check records is in a completed state" and explicitly forbids generalising to "nothing on the push is closed", with OPS-40 and OPS-91 named as the bound. This is Hardness Plan constraint 7a discharged in the artifact, not deferred. Verified against source: OPS-40 and OPS-91 are both `state_OPS_4`.
- **OE 15 grading note two** pre-authorises an agent that also flips one of Jaime's three records to a completed state, which is the correct anti-false-fail posture. Empirically load-bearing: every Gemini run moved the QC records to Done.
- **OE 16 grading note** explicitly de-credits OPS-34 (the record Jaime actually commented on, titled "Exterior signage update"), so identifying it is neither required nor rewarded. Verified: OPS-34 is `state_OPS_4`, 16 comments, title carries no North-cluster signal.
- **OE 28 pre-declares the boundary items** (South unserviced unit, second condensate drain, compressor) as free-routing and unpenalised in either destination. This is the F7/UGT pressure valve and it is stated at the OE, not left to rubric evidence alone.
- **OE 31/32/33 carry explicit `S3 must decompose this into one criterion per content element` directives**, which is F8 discharged at the producing phase.

## OE-side note carried to AUDIT_all.md (not an OE defect)

**OE 5 and OE 6 correctly describe a mechanism that does not discriminate on this server.** Both steps now state that a full `slack_read_channel` returns thread replies inline as flat messages, so neither route is required and no criterion depends on `slack_read_thread`. That text is **accurate** — the 12 live trajectories confirm it (Opus called `slack_read_thread` 0 times across 6 runs, Gemini 9 times across 4 runs, and both had the replies in context either way). The consequence is for the Hardness Plan, not the OE: Lever 5 (thread-reply blindness) is a retrieval-depth lever this server does not support, so the plan's five selected levers are four live ones plus one inert. The facts Lever 5 was planted to hide still carry criteria (8, 9, 12, 29, 35, 38, 39) and still fail, but as **reasoning** misses, not retrieval misses. Logged as `[LOW] A-4` in `AUDIT_all.md`.

## Validator output — every WARN and NOTE adjudicated

| Line | Type | Adjudication |
|---|---|---|
| OE step count: 38 | NOTE | Within band for a six-write task across six services. No action. |
| no closed fiscal periods in `Fact_Ledger.lifecycle.closed_periods` | NOTE | Correct — StarPM is not a GL universe. Lifecycle precondition check correctly skipped. |
| universe: starpm | NOTE | Confirmed against `_aux/Universe.txt`. |
| `verify_universe_atoms`: date 2026-07-15 outside the active window | WARN | **Reconciled, intentional.** The row is the Mesa Vista 4C Make-Ready QC Inspection, a confirmed future event in Jaime's function. F9 discipline is discharged: OE 23 surfaces it explicitly and forbids any deliverable from asserting Jaime's QC queue is otherwise clear or the maintenance budget settled. Re-verified across all 60 criteria — no criterion makes either claim. |

## Verification statements

- [x] Validator re-run during this audit (`validate.py --phase all`); oe phase **0 fails, 0 warns**, exit 0.
- [x] `verify_universe_atoms.py --task …` re-run: 34 atoms, **0 fails**, 1 warn (reconciled above).
- [x] Regression-anchor suite executed: **62/62 PASS**; `check_regression.py` gate PASS.
- [x] Anti-rationalization output check passed.
- [x] Verdict recorded with explicit per-issue trail in `Council_Reports/AUDIT_all.md`.

## Discrepancies surfaced

**None on the OE.** One note (A-4) is carried to `AUDIT_all.md` about the Hardness Plan, not about this artifact: OE 5 and OE 6 accurately describe a retrieval mechanism that does not discriminate on this server, so the plan's Lever 5 is stale, not the OE.

## Verdict

**PASS (STRICT)** — oe phase. Both OE sub-dims at 5/5 under the strictest reading: 14 of 14 atoms exact against source, 0 unknown tool names, 0 parameter-trap hits, 0 fails and 0 warns from `validate.py --phase oe`. The task-level verdict is `REVISE`, driven entirely by two rubric-phase findings; see `_aux/Council_Reports/AUDIT_all.md`.
