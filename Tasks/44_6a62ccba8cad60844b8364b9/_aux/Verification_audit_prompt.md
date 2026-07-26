# Verification — AUDIT (phase: prompt) · on-demand Mode 2

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** `starpm` (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Artifact:** `5_Prompt.txt` — 313 words, 0 em-dashes, 0 tool names, 0 internal ids
**Invocation:** `PIPELINE AUDIT — Tasks/44_6a62ccba8cad60844b8364b9 --phase all` (fresh chat, on-demand Mode 2), 2026-07-26. Report: `_aux/Council_Reports/AUDIT_all.md`.
**Prior S1 auto-fire pass preserved at** `_aux/Council_Reports/_superseded/audit_ondemand_prev/Verification_audit_prompt.md`.

## Strictest interpretation re-applied

- Every "should" in `Evals_starpm/1_Prompt_Eval.md` and `Docs_starpm/7_QC_Spec_Doc1.json` read as "must".
- Every NON-FAIL middle band collapsed to REVISE.
- **Density bar is FRAMEWORK-SCOPED.** `_aux/Universe.txt` = `starpm`, so the StarPM V4 scheme applies: midpoint >= 40 PASS / 15-39 THIN / < 15 INSUFFICIENT, **per model**. The V3-family 50/40 scheme was explicitly NOT applied.
- Every soft convention in `Reference/Prompt_Format.md` treated as binding.
- Every validator WARN and NOTE listed and individually adjudicated, none waived silently.

## Sources consulted

- **Per-task data** — `3_UniverseDataForThisTask.json` (3,892 rows, queried directly) and `_aux/Universe_Split/` (slack, linear, airtable, gcalendar, contacts, hubspot, quickbooks), `_aux/Fact_Ledger.json`, `_aux/Universe_Index/today_horizon.json`, `_aux/Feasible_Surface.json`, `_aux/Hardness_Plan.md`, `_aux/Trajectory_Stats.json`.
- **Eval spec** — `Evals_starpm/1_Prompt_Eval.md` (primary for this phase), plus `Evals_starpm/0_Injection_Quality_Eval.md` and `Evals_starpm/5_Submission_Gate_Eval.md` executed deterministically.
- **QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` (5 dims / 24 sub-dims) and `Docs_starpm/8_QC_Spec_Doc2.md`. `Docs_starpm/13_QC_Companion.md` deliberately excluded (Brookfield-contaminated).
- **Tool catalog** — `StarPM_Base_Universe/7_Server_Tools_Details.json` (276 names).
- **Prior council reports** — re-read to spot pattern misses, not trusted as ground truth: `Council_Reports/{S1_A_grounding,S1_B_adversarial,AUDIT_prompt,FINAL_council,QC_Strict_Check,S4_verdict,S4_fixes,S4_AF_justifications,S4_judge_errors}.md`.
- **Cross-task** — `Tasks/_meta/Learnings.md`, `AGENTS.md`, `Reference/Prompt_Format.md`.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)

- `_aux/Universe_Split/slack.slack_messages.json` :: C001 re-read in full (104 messages, sorted by `created_at`). Kick-off `1778171944.000091` (2026-05-07T16:39), Elias wrap pair `…446.000005` / `…447.000006` (2026-05-20T20:20), Jaime field note `1779562423.000092` (2026-05-23T18:53Z = 13:53 CDT), John Smith restock `1779567943.000011`, Brooke reply `1779569323.000012`, Lisa 5/27 `1779884437.000093`, Carlos plumbing `1780256425.000094`, Brooke budget `1780494075.000095`, Brooke 6/19 pair `…601.000096` / `…061.000097` — all re-read at source, none via a prior report.
- `_aux/Universe_Split/linear.linear_issues.json` + `linear.linear_workflow_states.json` :: 22 push-adjacent issues re-pulled with `state_id` resolved through the states table, not through prose.
- `_aux/Fact_Ledger.json` :: 403 amounts / 206 emails indexed; lifecycle `today` = 2026-07-01 confirmed as the single date-alignment source for prompt + OE + rubrics.
- Tool catalog (universe-aware per `_aux/Universe.txt` = starpm): `StarPM_Base_Universe/7_Server_Tools_Details.json` — 276 tool names swept against the prompt body, **0 hits**.

## Eval spec verified for this phase

- Universe-correct eval set: `Evals_starpm/` (6 evals). `0_Injection_Quality_Eval.md` and `5_Submission_Gate_Eval.md` executed via `validate.py --phase injection` / `--phase submission_gate`.
- `Evals_starpm/1_Prompt_Eval.md` :: strictest reading applied — anti-pattern checks mapped to hard 1/5 on their sub-dims per the AGENTS.md deviations table; 2.8 relative-date rule scored NON-FAIL-as-5 because both resolved windows carry universe data.

## QC spec re-verified (universe-correct doc set: `Docs_starpm/`)

- `Docs_starpm/7_QC_Spec_Doc1.json` :: 5 dimensions / 24 sub-dims parsed from source. The 12 Prompt sub-dims rescored below. The stale "Jun 12 2026 US/Eastern" string inside the JSON was **not** used; today resolves to 2026-07-01 America/Chicago per `Docs_starpm/6_Prompt_Relative_Time_Updates.md` and `_aux/Universe_Index/today_horizon.json`.
- `Docs_starpm/8_QC_Spec_Doc2.md` :: appendix issue taxonomy re-applied.
- StarPM caveat honoured: `Docs_starpm/13_QC_Companion.md` is Brookfield-contaminated and was NOT consulted as SSOT (`Validators/regression_baseline/ROUTING_DECISIONS.md`).

## Per-atom evidence table (v18 — required for the Truthfulness 5/5)

| Atom asserted in the prompt | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| "End of June was the target to have the Preventive Maintenance Push closed out" | `linear_issues WHERE id='OPS-186'` + `slack_messages WHERE ts='1781902061.000097'` | "The goal is to have every open issue resolved and closed out before the end of June" / "Goal is to have everything vlosed out before end of June" | PASS |
| "That came and went yesterday" | `today_horizon.json` today = 2026-07-01 | yesterday = 2026-06-30 = end of June | PASS |
| "Brooke started this in early May" | `slack_messages WHERE ts='1778171944.000091'` | 2026-05-07T16:39, brooke.phillips, "the Preventive Maintenance Push is officially moving into active execution" | PASS |
| "HVAC, plumbing and electrical across the whole portfolio" | same row | "kicking off the portfolio-wide HVAC, plumbing, and electrical audit" | PASS |
| "I logged both cluster spot-checks as passing in late May" | `linear_issues WHERE assignee_id=Jaime Salinas` | OPS-87 created 2026-05-24 "both passed"; OPS-98 created 2026-05-25 "spot-checks complete" | PASS |
| "my read is that my part of it is finished" (soft verb, L24) | OPS-87 / OPS-96 / OPS-98 descriptions | "moved both from In Review to Done" / "Moving this to In Review" / "I'm moving both cluster issues to Done" | PASS — belief-framed, literally true of what she logged |
| "The crew called the HVAC run wrapped around the same time" | `slack_messages WHERE ts='1779308446.000005'` | 2026-05-20, elias.navarro, "all three clusters are done. Every unit serviced" | PASS |
| "the channel the push has been running in" | `slack_channels` + C001 traffic count | C001 `#maintenance`, 104 messages, sole channel carrying push traffic; Jaime's own habitual C004 carries none | PASS — descriptive, exactly one referent |

Empty evidence cells: **none**. Truthfulness scored 5/5 on this table, not on narration.

## Per-universe landmines (StarPM) re-checked

| Landmine | Status |
|---|---|
| Near-duplicate decoy files (invoice-2026-419 / -287, BILL-0392 / -920, tanya-mitchell agreement / -2, laspalmas-8d-qc / -2) | Not touched. Surface is Linear + Slack + Airtable + Calendar; no document dependency. |
| Cross-property "Unit 14" ambiguity | Not touched. No unit-level identifier appears in the prompt. |
| Tanya Mitchell accommodation-vs-eviction contradiction | Not touched; that chain lives in C003, outside the push. |
| Airtable-is-source-of-record vs Linear-secondary | **Load-bearing and correctly honoured.** The prompt routes technician-onsite field work to "our maintenance ticket log" (Airtable `tblMaintenanceTickets`, description ends "System of record for maintenance work orders; Linear is secondary") and everything else to tracking items. `linear_teams.team_001` carries the same routing rule. |

## All 9 lenses status (prompt scope)

- Lens 1 strict QC scoring :: **PASS** — 12/12 Prompt sub-dims at 5
- Lens 2 answer-leakage sweep :: **PASS**
- Lens 3 hardness end-to-end (prompt-side surfacing) :: **PASS with note** (Lever 5 mechanism inert on this server; see AUDIT_all.md Lens 3)
- Lens 4 strict density :: **PASS** (empirical, per model)
- Lens 5 adversarial review :: **PASS**
- Lens 6 :: RETIRED v18 — not executed
- Lens 7 anti-rationalization :: **PASS**
- Lens 8 regression-anchor verification :: **62/62 PASS**
- Lens 9 :: RETIRED v18 — not executed

## Sub-dim scoring (Dimension 1 — Prompt, 12 sub-dims)

| Sub-dim | Score | Basis under strictest reading |
|---|---|---|
| Unique Ground Truth | 5 | Every write is unique by construction (new ticket, new issues, 3 comments on the only 3 issues assigned to Jaime across 230, new event, 1 channel post, 1 draft to one named recipient). F7 clean. |
| Feasibility | 5 | Every ask has a tool and data. Gmail draft-only constraint honoured — the prompt asks for a draft, never a send. |
| Explicit Tool Mention | 5 | 276 catalog tool names swept: 0 hits. No parameter names, no MCP-server references, no internal ids. |
| Prompt Clarity and Specificity | 5 | Every imperative is directed at the agent; no "I'll [verb]" delegation seam; the ticket-vs-tracking-item routing rule is stated rather than left to inference. |
| Contrived / Unnatural | 5 | No timestamp demands, no format constraints. Difficulty is entirely record complexity. |
| Truthfulness | 5 | Per-atom table above, 8/8 PASS, 0 empty cells. |
| Tool use and Cross-service | 5 | Requires linear + slack + airtable + gcalendar + gmail + contacts; no single service resolves it. |
| Investigation | 5 | Root cause is not stated. Both branches of the QC question are offered symmetrically, so the agent must derive which holds. |
| Coherence | 5 | See WARN adjudication below. |
| Persona | 5 | Jaime Salinas, `p_007`, Quality Control Inspector. Voice, verbosity and scope match the persona brief; the ask sits inside her own sign-off authority. |
| Business Function | 5 | Quality Control & Field Services — a QC inspector closing out her own spot-check position. |
| Alignment with Today's Date | 5 | "yesterday" = 2026-06-30 = the stated end-of-June target; "as of today" = 2026-07-01. Both resolved windows carry universe data. |

## Validator output — every WARN and NOTE adjudicated

| Line | Type | Adjudication |
|---|---|---|
| bolt-on candidate: sentence 1 shares no named entities with the rest | WARN | **NOT a defect.** Remove-sentence test executed: deleting "End of June was the target… still sitting open." leaves "Brooke started this in early May" with a dangling "this" and removes the deadline the whole ask hangs on. That test is the spec's own criterion and it fails, so Coherence holds at 5. The detector keys on entity overlap and cannot see the anaphor. |
| word count 313 over 300 | NOTE | Inside the 500-word hard cap and inside the sweet-spot band. No action. |
| relative date `yesterday` / `today` | NOTE ×2 | Both resolved against `Fact_Ledger.lifecycle` today = 2026-07-01; both windows carry data. No action. |
| distinct services referenced: 2 | NOTE | Detector counts explicit service nouns; destinations are named descriptively by design (channel-lock-in avoidance). Actual cross-service requirement is 6, evidenced on 12 live trajectories. No action. |

## Verification statements

- [x] Validator re-run during this audit (`validate.py --phase all` / `--phase injection` / `--phase submission_gate`); prompt phase exit 0, 0 fails.
- [x] Regression-anchor suite executed: **62/62 PASS**; `check_regression.py` gate PASS (anchors 62/62, reports 21/21 identical, verdicts 7/7 unchanged).
- [x] Anti-rationalization output check passed; no "I considered flagging X but decided it's fine because…" line survives.
- [x] Verdict recorded with explicit per-issue trail in `Council_Reports/AUDIT_all.md`.

## Discrepancies surfaced

**None on the prompt.** Prompt phase verdict: **PASS (STRICT)**.

One calibration note carried to AUDIT_all.md (not a prompt defect): the closing paragraph supplies both branches of the QC verdict in the persona's own words. That is required for Unique Ground Truth, and it also removes the L31 Gemini-selective retraction stump the Hardness Plan pre-registered — criteria 49 and 50 pass 12/12 on both models. It threatens no gate (pass@1 is 0/6 on both models) and the prompt sentence is the correct trade.

## Verdict

**PASS (STRICT)** — prompt phase. 12 of 12 Prompt sub-dims at 5/5 under the strictest reading. 0 BLOCKERs, 0 findings, 1 validator WARN adjudicated as a detector limitation rather than a defect. The task-level verdict is `REVISE`, driven entirely by two rubric-phase findings; see `_aux/Council_Reports/AUDIT_all.md`.
