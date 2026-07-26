# Verification — S1 (v16 cross-source check)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Deliverable:** `5_Prompt.txt` — 313 words, 14 sentences, zero em/en dashes, zero tool names, zero internal IDs.

## Sources consulted

**Per-task data**

- `_aux/Universe_Split/` :: `linear.linear_issues.json` (230 rows; OPS-16/17/18 Elias scope issues, OPS-35/40/44 cluster issues, OPS-43/56 South holdovers, OPS-51/71 portfolio filter issues, OPS-87/96/98 Jaime's three QC issues, OPS-91 West, OPS-97 Carlos plumbing, OPS-99/108 East near-duplicate pair, OPS-186 West-still-underway), `linear.linear_workflow_states.json` (state_OPS_0 Backlog … state_OPS_4 Done), `linear.linear_comments.json`, `linear.linear_users.json`, `linear.linear_projects.json` (proj_003 = "Preventive Maintenance Push"), `slack.slack_channels.json` (C001 = #maintenance), `slack.slack_messages.json` (104 in C001: Brooke kickoff ts `1778171944.000091`, Elias wrap ts `1779308446.000005` / `1779308447.000006`, Jaime field note ts `1779562423.000092`, John Smith filter-stock ts `1779567943.000011` + Brooke reply ts `1779569323.000012`, Lisa 5/27 ask ts `1779884437.000093`, Carlos plumbing ts `1780256425.000094`, Brooke 6/19 posts ts `1781899601.000096` / `1781902061.000097`), `contacts.contacts.json` (Brooke Phillips = Apartment Property Supervisor; Jaime Salinas = Quality Control Inspector), `gcalendar.gcalendar_events.json` (all 565 rows; 2026-06-02T16:45 mid-initiative check-in; future sweep), `airtable.airtable_tables.json` + `airtable_fields.json` (appPropertyOps / tblMaintenanceTickets, tblMakeReady), `gmail.gmail_messages.json`.
- `_aux/Fact_Ledger.json` :: consulted. **Note the defect below** — `lifecycle.today` is `null`, so no date atom was available from it; date alignment was verified against `_aux/Universe_Index/today_horizon.json` (`universe_today: 2026-07-01`) instead.
- `_aux/Hardness_Plan.md` :: all 5 selected levers engineered into the prompt; all 10 pre-registered S1 constraints checked one by one and honoured (Council B 10/10, AUDIT 10/10 independently).

**Eval spec** — `Evals_starpm/1_Prompt_Eval.md` (12 Prompt sub-dims + the UGT / dimensional-feasibility / phantom-identifier / write-action-divergence / delegation-clarity / minimum-complexity hard gates). **QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` (Prompt dimension fail / non-fail / pass definitions) + `Docs_starpm/8_QC_Spec_Doc2.md` (severity taxonomy). Per-sub-dim results below.

## Eval spec sub-dims (Evals_starpm/1_Prompt_Eval.md) verified

- 1.1 Unique Ground Truth :: **PASS** — end-state divergence gate run; four candidate readings enumerated, all converge on one final universe state; the closing conditional is universe-determinate (only the negative branch fires).
- 1.2 Feasibility :: **PASS** — every ask maps to a real StarPM tool; every required fact is materialized; dimensional gate (T10) passes on the cluster dimension.
- 1.3 Explicit Tool Mention :: **PASS** — zero tool names, parameter names, MCP-server names, or internal IDs (no OPS-nn, no C00n, no tbl*, no ts).
- 1.4 Prompt Clarity and Specificity :: **PASS** — write-action divergence gate clean; delegation-clarity gate clean (zero "I'll [verb]" statements).
- 1.5 Contrived / Unnatural Prompts :: **PASS** — no command list, no numbered steps, no artificial precision, no format constraints.
- 1.6 Truthfulness :: **PASS** — phantom tight-identifier grep clean; AUDIT produced a 17-row per-atom evidence table retrieved from source. Zero major, zero minor errors.
- 1.7 Tool use and Cross-service requirement :: **PASS** — 7 of 8 services; the conclusion is unreachable inside any single service.
- 1.8 Investigation :: **PASS** — not pre-solved; the prompt asserts the opposite of ground truth and the agent must derive the reversal.
- 1.9 Coherence :: **PASS** — validator bolt-on WARN independently re-adjudicated a false positive by both councils and AUDIT (removing sentence 1 strands the "That"/"it"/"this" anaphora chain and leaves the initiative unnamed).
- 1.10 Persona :: **PASS** — sign-off-or-kick-back is the literal centre of Jaime's brief; 313 words, short declaratives, zero emoji, verbosity 0.30 honoured.
- 1.11 Business Function :: **PASS** — assigned 3 (Quality Control & Field Services) = prompt primary 3.
- 1.12 Alignment with Today's Date :: **PASS** — all relative phrases ("End of June … came and went yesterday", "as of today", "in early May", "late May", "around the same time") resolve cleanly against 2026-07-01 with universe data in every resolved window.

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json — Prompt dimension) verified

All 12 Prompt sub-dims plus the 2 Universe sub-dims scored **5/5 by Council B and independently 5/5 by AUDIT under the strictest interpretation**. Zero NON-FAIL band justifications were invoked at either gate.

## Reference docs consulted

- `Reference/Prompt_Format.md` :: voice principles, three-movement structure, anti-pattern list, 500-word cap, dash ban, tool-name ban re-checked against the final text.
- `Prompt_Guidelines.md` :: QC-sample-tonality clone check, over-signaling check, generic-urgency check, formulaic-closing check.
- `Docs_starpm/4_Prompt_Hard_Tips.md` :: structured-DB-skip and first-framing-latch behaviours are the two levers the prompt is built on.
- `Docs_starpm/6_Prompt_Relative_Time_Updates.md` :: date SSOT, today = Wednesday 2026-07-01.
- `QC_Tasks/V4_Tasks/QC_Passed/Task1..Task4/5_Prompt.txt` :: voice and structure baseline.
- Full read log in `_aux/Reads_s1.md`.

## Verification statements

- [x] Validator (`validate.py --phase prompt`) exit 0 — PASS, 0 fails, 1 WARN (adjudicated false positive), 6 notes.
- [x] `verify_universe_atoms.py` exit 0 — 0 fails, 0 warns. Recorded honestly as a **vacuous pass**: the prompt carries no tight identifiers by design, so 0 atoms were checked. Truthfulness rests on AUDIT's hand-retrieved per-atom evidence table, not on this gate.
- [x] Council A grounding + convention clean — GO, 0 BLOCKER, 0 MAJOR, 4 MODERATE (all downstream-binding for S2/S3, none a prompt defect), zero ungrounded claims, zero convention drift.
- [x] Council B QC scoring — GO, every applicable sub-dim 5/5, zero NON-FAIL bands invoked. Density Opus 54 / Gemini 46 / combined 50, band PASS. Levers 5/5 preserved. Constraints 10/10 honoured.
- [x] Similarity gate (`calc_similarity.py`) composite **27.2** < 40 (and < 35, so it did not itself trigger AUDIT). Top match `QC_Tasks/V3_Tasks/Task12` at 27.2; nearest sibling task `Tasks/42` at composite 11.8 (raw lexical 32.6, multiplier 0.360).
- [x] Regression anchors (`test_regression_anchors.py`) — **62/62 PASS**.
- [x] AUDIT verdict = **PASS (STRICT)** — 0 BLOCKER, 0 sub-dim < 5, 5/5 levers trace with cited evidence, density PASS on both models, anti-rationalization scan reported (6 found, 6 promoted, 0 silently cleared).

## Discrepancies surfaced

1. **`Validators/validate.py:464` prints a wrong date for StarPM tasks.** `_aux/Fact_Ledger.json` has `lifecycle.today = null`, and line 464 falls back to a hardcoded Brookfield `"2026-06-12"`. The validator NOTE therefore tells a downstream reader to resolve relative dates against 2026-06-12 when this universe's today is 2026-07-01. Not a prompt defect and not a gate failure (it is a NOTE, not a check), but it is misleading and `Validators/universes.py` already carries the correct value. **Two fixes, both out of scope for a task phase and left for the operator:** backfill `lifecycle.today` in the Fact_Ledger builder, and change line 464 to read the universe registry rather than a hardcoded literal. **Until then S2 and S3 must date-anchor to `_aux/Universe_Index/today_horizon.json`.** AUDIT recommends this land before S2, since `6_Oracle_Events.txt` is still an untouched template.
2. **Atom-verifier vacuity.** `verify_universe_atoms.py` checked 0 atoms on this prompt. Correct behaviour (the prompt deliberately carries no tight identifiers), but it means the deterministic Truthfulness floor did no work here. Recorded so no downstream gate mistakes the PASS for evidence.
3. **Density is tighter than the Hardness Plan claimed.** The plan projected 55.5 midpoint with `linear` at 34% of calls. Council B independently sketched 50 (Opus 54 / Gemini 46) and AUDIT, under the least-generous reading, sketched 44 combined (Opus 47 / Gemini 41) with `linear` at 53% and exactly 4 services at >= 5%. All three are in the StarPM V4 PASS band (>= 40 per model), so this is not a blocker, but Gemini at 41 is close to the line. S2 should prefer OE steps that add non-Linear reads over Linear ones.
4. **Three factual errors in `_aux/Hardness_Plan.md`** found by AUDIT (A-13/14/15): the plan states C001 has 15 distinct thread parents (actual 37), a 5-day gap where the record shows 7, and `linear` at 34% of projected calls (recomputed 53%). None changes the lever selection or the density band. Upstream artifact, not corrected in this phase.
5. **Lever 8 hop B resolved for the first time at AUDIT.** The Linear issue carrying Jaime's coil/plumbing/panel notes is **OPS-34**, whose title is "Exterior signage update - brand-compliant vendor selected" and whose state is Done. Because the title is actively misleading, S3 must never grade the agent on *identifying* that issue; grade the disposition finding instead.

## Verdict

**PASS.** `5_Prompt.txt` clears every S1 exit criterion as drafted, with no edit required at any of the five gates: validator PASS (the single WARN independently re-adjudicated a false positive three times), Council A GO with zero ungrounded claims, Council B GO with every applicable QC sub-dim at 5 and zero NON-FAIL bands invoked, similarity composite 27.2 against a 40 ceiling, and AUDIT `PASS (STRICT)`. Density lands in the StarPM V4 PASS band on both models under all three projections, though AUDIT's least-generous reading puts Gemini at 41 against a 40 floor, which is carried to S2 as a watch item. Five discrepancies are surfaced above; none blocks the phase, and the validator date-fallback defect is flagged for the operator to fix before S2.
