# Verification — PIPELINE FINAL · Task 44 (`44_6a62ccba8cad60844b8364b9`)

**Universe:** starpm (V4, Star Property Management, LLC) · **Universe today:** 2026-07-01 (America/Chicago)
**Density scheme:** StarPM V4 — midpoint >= 40 PASS, applied PER MODEL. The V3-family 50/40 bands do NOT apply.
**Date:** 2026-07-26

## Sources consulted

**Per-task data**

- All 3 artifacts (`5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`) read together, not in isolation.
- `_aux/Universe_Split/` :: cross-verified the end-to-end dependency chain directly against the per-service rows — `linear.linear_issues.json` (230), `linear.linear_comments.json` (48), `slack.slack_messages.json` (580, C001 = 104), `airtable.airtable_records.json` / `_fields` / `_tables` / `_bases`, `gcalendar.gcalendar_events.json` (565), `contacts.contacts.json` (61), `Universe_complete_data.json` (4.44 MB).
- `_aux/Fact_Ledger.json` :: 403 amounts / 206 emails indexed; every artifact atom traced.
- `_aux/Hardness_Plan.md` :: 5 selected levers traced through the final artifact set; the S2 corrections block extended with a fourth row this phase.
- `_aux/Verification_s1.md` / `Verification_s2.md` / `Verification_s3.md` + `_aux/Council_Reports/AUDIT_prompt.md` / `AUDIT_oe.md` / `AUDIT_rubrics.md` :: cross-referenced for carried-forward items. Per AUDIT_oe's explicit instruction, prior council GO/NO-GO reasoning was **re-verified rather than inherited**.
- `StarPM_Base_Universe/7_Server_Tools_Details.json` :: 268 tools, used for the per-tool parameter-binding check.

**Eval spec** — `Evals_starpm/0` through `Evals_starpm/5`, StarPM-routed; no Brookfield spec was loaded. Itemised in the next section.

**QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md`, full sub-dim sweep. Itemised two sections below.

## All eval specs verified

- `Evals_starpm/1_Prompt_Eval.md` :: re-applied at the integration layer via Lens 1 and Lens 5.
- `Evals_starpm/2_OE_Eval.md` :: re-applied via Lens 3 forward/reverse map and Lens 5 tool-binding strictness.
- `Evals_starpm/3_Rubrics_Eval.md` :: re-applied via Lens 2 across all 64 criteria.
- `Evals_starpm/4_Verifier_Fails_Eval.md` :: Lens 6 simulated bucket classification for every one of the 64.
- `Evals_starpm/0_Injection_Quality_Eval.md` :: `validate.py --phase injection` — 7 hard gates PASS; 4 COUNCIL notes (P4/P5/P6/P8 difficulty >= 3.5) fed to the council.
- `Evals_starpm/5_Submission_Gate_Eval.md` :: `validate.py --phase submission_gate` — defect families F1-F9, 0 deterministic defects.

## QC spec full coverage check (`Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md`)

- All Prompt sub-dims (12) :: scored — Unique Ground Truth, Feasibility, Explicit Tool Mention, Clarity and Specificity, Contrived/Unnatural, Truthfulness, Tool use and Cross-service requirement, Investigation, Coherence, Persona, Business Function, Alignment with Today's Date.
- All Universe sub-dims (2) :: scored — Universe Feasibility, Cross-service Coherence.
- All OE sub-dims (2) :: scored — OE Completeness, OE Accuracy.
- All Rubric sub-dims (5) :: scored — Overall Rubric Quality, All-Failing Rubrics, Rubric Category Balance, Process Rubrics, Agent Centric Phrasing.
- Trajectory sub-dims :: T1 (Tool Call Count) projected only at this phase; T2 (Agent Failure Rate) and T3 (Error Rate) deferred to S4, dual-model.

## Verification statements

- [x] **Validator (`validate.py --phase all`) exit 0 across all 3 artifacts.** prompt 0 fails / 1 warn (adjudicated false positive), oe 0 fails / 0 warns, rubrics 0 fails / 0 warns.
- [x] **V4 gate `--phase injection` PASS** (0 fails, 0 warns, 4 COUNCIL notes).
- [x] **V4 gate `--phase submission_gate` PASS** (0 fails, 3 soft F6.1 warns, all three adjudicated non-defects; the hard F8 NON_ATOMIC_ENUM gate did not fire on any criterion).
- [x] **6 FINAL lenses returned PASS** — Truthfulness / Rubric Binding / Cross-Artifact Holism / Red-team / Narrative-State + Action-Prescription / Verifier-Fails-Spec Pre-Upload.
- [x] **Zero answer leakage.** Two independent sweeps of the 4.44 MB `Universe_complete_data.json` (27 phrasings by the coordinator, 35 by the council) returned 0 hits on every conclusion phrasing. The only near-matches are unrelated: OPS-121's "after-hours maintenance **coverage gap**" (staffing) and a QuickBooks "overstated late fee" memo. No OE step or rubric title states the aggregate conclusion in copyable form.
- [x] **Every Hardness lever still triggers end-to-end.** Lever 2 (Linear `state_id` skip) prompt "work out what is actually finished... get our tracking to match" -> OE 9/12/13/14/15 -> idx 54. Lever 9 (authority dismissal, persona-self) prompt "I logged both cluster spot-checks as passing... my read is that my part of it is finished" -> OE 12/13/14 -> idx 52/53 + notes at idx 24/25/26. Lever 1 (latching on the crew's wrap) prompt "The crew called the HVAC run wrapped around the same time" -> OE 3 -> idx 55/56. Lever 8 (multi-link chain) prompt "Anything flagged in the field that still needs a tech back onsite" -> OE 4/16 -> idx 1. Lever 5 (thread-reply blindness) -> OE 5/6 -> idx 8/11. **No lever carrier was edited this phase.**
- [x] **Every tight identifier verified on the row, not just in the ledger.** OPS-87 `state_OPS_1`, OPS-96 `state_OPS_1`, OPS-98 `state_OPS_2`, OPS-97 `state_OPS_1`, OPS-99 `state_OPS_2`, OPS-108 `state_OPS_0` (byte-identical titles in opposing states), OPS-40 `state_OPS_4`, OPS-91 `state_OPS_4`, OPS-186 `state_OPS_1` created 2026-06-17, OPS-35 `state_OPS_2`, OPS-43 `state_OPS_2`, OPS-56 `state_OPS_2`. Exactly **3 of 230** issues carry Jaime Salinas as assignee. All 15 cited Slack `ts` values resolve to the exact quoted text and author, and both load-bearing thread replies were confirmed to sit behind `slack_read_thread` by internal parent-id linkage (`8ce45073…` -> ts `1779308442.000001`; `7b8f1611…` -> ts `1779567943.000011`). All 7 contact emails and job titles exact.
- [x] **Every OE tool-parameter binding on the EXACT named tool.** All 25 tools across the 38 OE steps exist in the 268-tool catalog and every bound parameter is on that tool, including the per-tool trap `search_records(baseId, table, query)` versus `list_records_for_table(baseId, tableId)`. Independently confirmed OE 29-33's claim that `save_issue.assignee` cannot carry a value: the catalog declares it `{"required": "optional", "type": "null"}`. Confirmed the gmail server exposes no send tool, so OE 38's draft-only deliverable is correct.
- [x] **F7 / F8 / F9 clean.** F7: every write is unique by construction (new Airtable ticket, new Linear issues, new calendar event, draft to a named recipient, post to the uniquely determined push channel); the three note targets are the complete enumeration of Jaime's assigned records. F8: hard gate did not fire; the three soft warns adjudicated as permitted single-comparison and single-output groupings. F9: Jaime has **0** calendar events on or after 2026-07-01, and none of the 9 confirmed universe-wide future events references her or the push.
- [x] **Hardness constraints 6 / 7 / 7a hold.** `OPS-91` and `OPS-40` each appear **0 times** in `7_Rubrics.json`. idx 54 is id-scoped to Jaime's three records with an explicit FAIL guard against generalising to "no push work is complete", and idx 61 / idx 62 carry the affirmative completion counterweight.
- [x] **Density PASS on both models** under the StarPM V4 band: Opus 4.8 range 46-63, **midpoint 54**; Gemini range 40-58, **midpoint 49**. Floor protected by 11-12 mandatory write calls plus an unavoidable Airtable schema walk and Linear team/status/project enumeration. Verification is dual-model: `8a_Verifier_Fails_Opus.txt` + `8b_Verifier_Fails_Gemini.txt` and `Agent_Responses/{Opus,Gemini}/` are expected downstream.
- [x] **Outcome > Process** (64 / 0), 0 tool names in any rubric title, 0 em-dashes in any of the three artifacts, prompt 313 words against the 500 cap, platform similarity top match 27.2% (< 40).
- [x] **Council report exists with `VERDICT: PASS`** at `_aux/Council_Reports/FINAL_council.md`, with a coordinator adjudication section recording every fix applied and every finding declined.

## Discrepancies surfaced

**Four found, four resolved in place; two findings declined with reasoning.**

1. **[MAJOR-1, FIXED] Rubric idx 17 locked the hose-bib repairs to a Linear tracking item** while the prompt routes tech-onsite field items to the maintenance ticket log "rather than sitting as a tracking item", and idx 16 already granted either-destination latitude to the water heaters from the same OPS-97 comment. Confirmed on the source row before acting. idx 17 retitled and its evidence mirrored to idx 16; OE 32's accommodation clause extended to cover the hose bibs so the two artifacts agree.
2. **[MAJOR-2, FIXED] Rubric idx 61 required crediting a completion claim in a Todo-state record** with a justification asserting it as settled, in a set that otherwise trains distrust of exactly that pattern, and with **no OE anchor at all** — independently confirmed that OE 20 quoted OPS-186's description starting at the second sentence, truncating the very sentence idx 61 grades. Fixed on three fronts: the justification now carries idx 62's grades-what-the-record-states hedge, the evidence now accepts a state-aware phrasing, and OE 20 now carries the electrical-completion sentence as a designated expected discovery.
3. **[MINOR-4, FIXED] Rubric idx 12 withheld ticket-log latitude** that the structurally identical idx 11 granted. Evidence extended to match.
4. **[MINOR-5, FIXED] Rubric idx 62 AND-bundled "coil cleaning and A/C checks"** where "A/C checks" is sourced from exactly one comment row whose near-duplicate says "filter checks" instead. Verified the sourcing directly, then retitled to "HVAC service work" with an explicit note that coil cleaning alone suffices.
5. **[MINOR-2, FIXED] Hardness Plan Service Breadth table understated Linear's share** (34% stated, ~49% measured by trajectory sketch). Corrected in the plan's S2 corrections block. Not a breadth defect: still under the 60% single-service ceiling with five services at >= 5%, and the concentration is intrinsic to a Linear-state-resolved answer.
6. **[MINOR-1, DECLINED] The prompt's closing conditional supplies the phrasing of the conclusion.** Declined: it supplies the format and never points at a load-bearing surface, editing the prompt at FINAL re-opens the whole S1 gate chain, and the branch asymmetry is the pre-registered Learnings L31 Gemini-selective differentiator.
7. **[MINOR-3, DECLINED] Brooke Phillips is an accepted owner in five of six owner accept-sets.** Declined: narrowing accept-sets to raise discrimination is the move that manufactures Bucket-1 false-fails, AUDIT_rubrics Q1 already ruled against exactly this on idx 23, and Brooke is record-backed in both flagged sets.

**Self-inflicted regression caught and corrected within the phase:** the first form of the idx 61 evidence accommodation named `OPS-186`, which raised a new validator WARN (evidence carrying an identifier the criterion does not) where the rubric phase previously had zero. Rephrased to "the record carrying that statement"; rubric phase back to 0 fails / 0 warns.

**Two Lens 6 Bucket-1 risks remain as noted, not fixed** (idx 15 state-mismatch observation locked to one location; idx 22 assignee audit is arguably beyond-prompt). Post-fix Bucket_1_Risk is **3.1% (2/64)** against a 20% threshold.

## Post-fix gate re-run (every gate re-executed after the final edit)

```
validate.py --phase all              prompt PASS 0F/1W · oe PASS 0F/0W · rubrics PASS 0F/0W
validate.py --phase injection        PASS  0 fails, 0 warns, 4 notes
validate.py --phase submission_gate  PASS  0 fails, 3 warns, 2 notes
test_regression_anchors.py           62 passed, 0 failed out of 62
verify_universe_atoms.py             0 fails, 1 warn (reconciled 2026-07-15 event), 34 atoms
```

## Rubric count cap applied (operator constraint, post-council)

The operator set a hard ceiling of **60 rubrics**. The set was at 64. This cap appears nowhere in `AGENTS.md`, `Docs_starpm/`, `Evals_starpm/`, `Reference/Rubric_Format.md` or any validator, which is why 64 cleared S3, AUDIT and the Final Council unchallenged; it is now recorded in `AGENTS.md` hard rule 14 and `Tasks/_meta/Learnings.md` so it binds from the next task.

Four criteria removed, chosen to retire risk rather than trim coverage: former **idx 15** (OPS-97 state-versus-prose, a location-pinned second copy of the portfolio-scope determination — council Bucket-1 risk), **idx 22** (assignee audit, beyond-prompt — council Bucket-1 risk and the third soft NOT_ATOMIC warn), **idx 23** (East owner, the weakest accept-set per council MINOR-3, and the subject of the fragile idx 23/51 disjointness adjudication — East ownership still graded on the draft), and **idx 39** (channel recap of the agent's own writes, which the council recorded as borderline beyond-prompt and did not count).

- [x] **All 5 lever carriers survive the cut** and none was edited. Verified by string-matching each carrier criterion in the reduced set.
- [x] **All 8 prompt asks still covered** — Airtable ticket, 4 tracking items each with a named owner, 3 notes on Jaime's records, calendar slot, channel post, draft to Brooke, retraction beat.
- [x] **No bundling introduced** — every cut is a whole-criterion removal, never a merge. Hard F8 gate still unfired; soft F6.1 warns dropped 3 -> 2.
- [x] **Density unchanged** — none of the four forced a unique tool call. Opus midpoint 54 · Gemini midpoint 49, both PASS.
- [x] **OE realignment applied** — OE 32, OE 33 and OE 37 each carried an `S3 must decompose…` directive naming an element that no longer has a criterion. All three narrowed to the surviving elements, with the dropped element re-stated as description content carrying no criterion and the reason given. Agent-facing expected-discovery content untouched, so the oracle path is unchanged.
- [x] **Post-cut census:** 60 outcome / 0 process · 0 duplicate titles · 0 em/en dashes · 0 "at least" · 0 "approximately" · 0 occurrences of OPS-91 or OPS-40 · 7 owner criteria.
- [x] **Lens 6 Bucket_1_Risk now 0 / 60 = 0%.** All four council-itemised risks closed: idx 17 and idx 62 by fix, idx 15 and idx 22 by removal.
- [x] **Every gate re-run after the cut:** `validate.py --phase all` exit 0 (rubrics 0F/0W) · `--phase injection` PASS · `--phase submission_gate` PASS 0 fails / 2 warns / census 60 · `test_regression_anchors.py` 62/62 · `verify_universe_atoms.py` 0 fails.

## Verdict

**PASS — 60 criteria, cleared for platform upload.**
