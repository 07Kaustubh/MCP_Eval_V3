# Verification — AUDIT (phase: rubrics) · on-demand Mode 2

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** `starpm` (V4) · **Universe today:** 2026-07-01 (America/Chicago)
**Artifact:** `7_Rubrics.json` — **60 criteria**, 60 `outcome` / 0 `process`, flat schema, re-read from disk this pass
**Invocation:** `PIPELINE AUDIT — … --phase all` (fresh chat, on-demand Mode 2), 2026-07-26. Report: `_aux/Council_Reports/AUDIT_all.md`.
**Prior S3 auto-fire pass (against the 64-criterion set) preserved at** `_aux/Council_Reports/_superseded/audit_ondemand_prev/Verification_audit_rubrics.md`.

> **Index note.** Earlier council reports index against the 64-criterion set. This pass indexes against the shipped 60. Tail mapping: current 51 = old idx 54, current 58 = old idx 61, current 59 = old idx 62, current 60 = old idx 63. Early indices align 1:1.

## Strictest interpretation re-applied

- Every "should" in `Evals_starpm/3_Rubrics_Eval.md` read as "must".
- Every NON-FAIL middle band collapsed to REVISE. This is what separates this pass's verdict from FINAL's: Overall Rubric Quality and All-Failing Rubrics both sit comfortably inside the spec's NON-FAIL bands and would score 3/4 or better at the platform, but neither reaches the 5/5 Pass text, and under AUDIT's rule 4 is a soft fail.
- **Density bar is FRAMEWORK-SCOPED (StarPM V4):** >= 40 midpoint PASS / 15-39 THIN / < 15 INSUFFICIENT, applied **per model**. The V3-family 50/40 scheme was explicitly NOT applied.
- Every soft convention in `Reference/Rubric_Format.md` treated as binding: flat schema, agent-centric titles, self-containment, atomicity, no tool names in titles, no "at least N" without prompt mandate, `(or similar)` permitted on free text and forbidden near ids/dates/emails, grounded literals.
- AGENTS.md hard rule 14 (60-criterion cap) applied as binding. Set is **exactly at 60** — compliant, with zero headroom.

## Sources consulted

- **Per-task data** — `3_UniverseDataForThisTask.json` (3,892 rows) and `_aux/Universe_Split/` (linear 230 issues / 48 comments / 5 workflow states, slack 580 messages incl. C001's 104, airtable records + tables + fields, gcalendar, contacts, hubspot, quickbooks), `_aux/Fact_Ledger.json` (403 amounts / 206 emails), `_aux/Feasible_Surface.json` (15 tables with enum maps), `_aux/Hardness_Plan.md`, `_aux/Trajectory_Stats.json`, `_aux/Similarity_Report.json`.
- **Post-verifier data** — `8a_Verifier_Fails_Opus.txt`, `8b_Verifier_Fails_Gemini.txt` (720 decisions), `Agent_Responses/{Opus,Gemini}/Run1-6_Trajectory.json` (12 runs).
- **Eval spec** — `Evals_starpm/3_Rubrics_Eval.md` (primary for this phase) and `Evals_starpm/5_Submission_Gate_Eval.md` (F1-F9, run deterministically), plus `Evals_starpm/0_Injection_Quality_Eval.md`.
- **QC spec** — `Docs_starpm/7_QC_Spec_Doc1.json` Dimension 4 (5 sub-dims, scored against the literal Pass(5) text) and `Docs_starpm/8_QC_Spec_Doc2.md`. `Docs_starpm/13_QC_Companion.md` deliberately excluded (Brookfield-contaminated).
- **Tool catalog** — `StarPM_Base_Universe/7_Server_Tools_Details.json` (276 names swept against all 60 titles).
- **Prior council reports** — re-read to spot pattern misses, not trusted as ground truth: `Council_Reports/{S3_A_grounding,S3_B_adversarial,AUDIT_rubrics,FINAL_council,QC_Strict_Check,S4_verdict,S4_fixes,S4_AF_justifications,S4_judge_errors}.md`.
- **Cross-task** — `Tasks/_meta/Learnings.md`, `AGENTS.md` (hard rules 6, 7, 8, 11, 13, 14 + the deviations table), `Reference/Rubric_Format.md`, `Reference/Strict_Convention_Inventory.json`.

## Data sources consulted (re-verified from source — NOT trusting prior phase outputs)

- `_aux/Universe_Split/linear.linear_issues.json` + `linear_workflow_states.json` + `linear_comments.json` :: every record id named in a rubric title re-pulled and its state re-resolved. OPS-56, OPS-66, OPS-81, OPS-87, OPS-96, OPS-97, OPS-98, OPS-99, OPS-108, OPS-186, OPS-35, OPS-40, OPS-43, OPS-44, OPS-91, OPS-16/17/18, OPS-34, OPS-51, OPS-71, OPS-79.
- `_aux/Universe_Split/slack.slack_messages.json` :: C001 re-read in full; every `ts` cited in a rubric justification confirmed at source.
- `_aux/Universe_Split/airtable.*`, `gcalendar.*`, `contacts.*`, `hubspot.*`, `quickbooks.*` :: swept for the ticket-table schema, the forward-event set, and every owner accept-set name.
- `_aux/Fact_Ledger.json` (403 amounts / 206 emails) and `_aux/Feasible_Surface.json` (15 tables with enum maps) :: loaded by the validator during this pass.
- `_aux/Trajectory_Stats.json` + `8a_Verifier_Fails_Opus.txt` + `8b_Verifier_Fails_Gemini.txt` + all 12 trajectories :: used for the All-Failing Rubrics sub-dim, which is only scorable post-verifier.
- Tool catalog: `StarPM_Base_Universe/7_Server_Tools_Details.json`, 276 names swept against all 60 titles — **0 hits**.

## Eval spec verified for this phase

- `Evals_starpm/3_Rubrics_Eval.md` :: strictest reading. Phase 2.7 channel/method lock-in escalation applied as Major-by-default per the AGENTS.md deviations table; Phase 4.2 threshold math supplemented with the absolute-count gate from `Reference/Rubric_Format.md` (Major >= 3 = FAIL).
- `Evals_starpm/5_Submission_Gate_Eval.md` :: run deterministically. F1-F9 families, 0 fails, 2 NOT_ATOMIC soft warns adjudicated below.

## QC spec re-verified (`Docs_starpm/`)

- `Docs_starpm/7_QC_Spec_Doc1.json` Dimension 4 (Rubric), 5 sub-dims, rescored below against the literal Pass(5) text, not against the absence of a Fail.
- `Docs_starpm/8_QC_Spec_Doc2.md` :: appendix taxonomy re-applied, including "one rubric item can be used as context for another" (relied on for cross-criterion self-containment) and "OEs describe steps — not what the final response should say".
- `Docs_starpm/13_QC_Companion.md` NOT consulted (Brookfield-contaminated).

## Per-atom evidence table (v18 — required for the Rubric-set Accuracy 5/5)

Every concrete literal in a rubric title, re-grounded independently:

| Atom in a rubric title | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| #2/#30/#40/#54 "two North cluster units … flagged on May 23, 2026" | `slack_messages WHERE ts='1779562423.000092'` | 2026-05-23T18:53Z (13:53 CDT), jaime.salinas, "Two units need HVAC looked at right away" | PASS |
| #5 "OPS-186, dated June 17, 2026 … West Cluster work as still underway" | `linear_issues WHERE id='OPS-186'` | created 2026-06-17, `state_OPS_1`, "with the West Cluster work still underway" | PASS on the fact (over-specification issue logged separately as A-1) |
| #8/#23/#35 "20x25 filter" shortage, May 23 2026, John Smith | `slack_messages WHERE ts='1779567943.000011'` | 2026-05-23T20:25, john.smith, "almost out of 20x25 filters so we'll need a restock before I can finish the run" | PASS |
| #9 Brooke → Elias stock count ahead of a bulk order | `slack_messages WHERE ts='1779569323.000012'` | "Elias, can you do a quick count on our filter stock? … bulk order with Lone Star Maintenance Supply" | PASS |
| #12/#29/#38/#39/#53 South unit, tenant not home during the window | `linear_issues WHERE id='OPS-43'` | "another unit was a no-access - tenant was out during the scheduled window" | PASS |
| #13/#31/#41 "two North cluster units that OPS-56 records as still held up by tenant scheduling conflicts" | `linear_issues WHERE id='OPS-56'` + its 2 comments | `state_OPS_2`, "two units are still pending because of tenant scheduling conflicts", ask to Carlos in both comments, no closing reply in the 48-comment corpus | PASS on the fact (evidence-field gap logged as A-2) |
| #16/#17/#18/#36/#56 two water heaters past serviceable life + hose bibs + budget escalation | `linear_issues WHERE id='OPS-97'` + `slack ts='1780494075.000095'` + `gcalendar` 2026-06-02T16:45 | all three present verbatim | PASS |
| #20/#21/#32/#42/#55 OPS-99 In Progress / OPS-108 Backlog, byte-identical title | `linear_issues` | `state_OPS_2` / `state_OPS_0`, titles byte-identical | PASS (atomicity warn adjudicated below) |
| #22/#23/#24 comment targets OPS-87 / OPS-96 / OPS-98 | `linear_issues WHERE assignee_id=Jaime Salinas` | exactly 3 rows of 230, all carry "spot-check" | PASS — F7 clean, the pin is unique |
| #25 Jaime's calendar, on/after 2026-07-01 | `gcalendar_events` | 0 existing events for her on/after 2026-07-01 → the slot is a create, not an update | PASS |
| #27 `#maintenance` (C001) | `slack_channels` + traffic | C001 = `#maintenance`, sole channel with push traffic | PASS |
| #37/#46/#47/#48 recipient + owner accept-sets | `contacts` + `hubspot_objects` | brooke.phillips (Apartment Property Supervisor); lisa.smith / carlos.mendez (Onsite Property Manager); john.smith / elias.navarro / tony.reyes (Lead Maintenance Technician) | PASS |
| #51 "none of … OPS-87, OPS-96, and OPS-98 … in a completed workflow state" | `linear_issues` | Todo / Todo / In Progress — none is `state_OPS_4` | PASS (atomicity warn adjudicated below) |
| #58 "electrical panel inspections across the South cluster are recorded as finished" | `linear_issues WHERE description LIKE '%electrical%'` | OPS-186 is the **only** electrical record in all 230; title says "South Cluster wrap-up", body says "across **her cluster**" (Patricia's) | PASS via the title, with the attribution accommodation in the evidence field (see A-3) |
| #59 "the crew recorded the East cluster HVAC service work as complete" | `linear_issues WHERE id IN ('OPS-99','OPS-108')` | both descriptions record Elias finishing East coil cleaning | PASS on the fact (see A-3) |
| #4/#33/#44/#52 "no QC spot-check record covers the West cluster" | `linear_issues WHERE assignee_id=Jaime Salinas` | OPS-87 = South+North, OPS-98 = South+North, OPS-96 = portfolio filters; no West-scoped QC record exists | PASS |

Empty evidence cells: **none**. No universe-grounded sub-dim was scored without proof.

## Per-universe landmines (StarPM) re-checked against the rubric set

| Landmine | Status |
|---|---|
| Near-duplicate decoy files | Not engaged (no document surface). |
| Cross-property "Unit 14" | Not engaged; no unit identifier is graded. |
| Tanya Mitchell contradiction | Not engaged. |
| Airtable-is-source-of-record vs Linear-secondary | Honoured: #1/#2 grade the Airtable ticket for technician-onsite work; #3-#21 grade Linear tracking items. #11/#12/#15/#16/#17 accept **either** destination for the genuine boundary items, matching OE 28/31/32. |
| Parameter traps | No rubric grades a parameter name. Evidence fields describe outcomes ("a record-creation call … that returns success"), never bindings. |
| Duplicate-record pairs (the universe's own near-miss trap) | Turned into a lever rather than tripped over: #20/#21 grade the OPS-99/OPS-108 pair by state, not by title. |

## Atomicity — full decomposition run on all 60

Two criteria carry the deterministic F6.1 NOT_ATOMIC soft warn. Both re-adjudicated from source this pass, independently of `FINAL_council.md`:

- **#20** — "OPS-99 and OPS-108 carry the same East cluster HVAC QC title while sitting in two different workflow states." This is **one relational claim** whose operands happen to be two ids. Splitting it yields "OPS-99 and OPS-108 have the same title" and "OPS-99 and OPS-108 are in different states", neither of which states the contradiction the criterion exists to grade, and both of which would co-fail on the same read. Not an F8 defect. **Residual risk flagged for the platform reviewer** — it is AF 12/12 and reads like the F8 shape on a fast pass.
- **#51** — "none of Jaime Salinas's three QC spot-check records, OPS-87, OPS-96, and OPS-98, was in a completed workflow state as the Agent found them." This is the one that textually matches the F8 shape AGENTS.md rule 13 / Hardness Plan constraint 2 warn about, so it gets the explicit reasoning: the three ids come from **one** `list_issues` output (assignee = Jaime Salinas returns exactly these three across 230 issues), the criterion grades **one** determination rather than three verifiable values, and the contrast case proves the rule was applied correctly elsewhere — OE 35 requires the three *comments* to be three atomic criteria "so a two-of-three agent fails exactly one", and #22/#23/#24 do exactly that. Three separate **write actions** are split; one **determination** over a closed single-query set is not. Not an F8 defect. **Residual risk flagged for the platform reviewer.**

Both adjudications are recorded as residual risk rather than silently accepted, per the anti-rationalization rule.

## Other convention sweeps

| Convention | Result |
|---|---|
| Em-dashes across all 3 fields × 60 | **0** |
| Tool names in titles (276-name sweep) | **0** |
| "at least N" in titles | **0** |
| `(or similar)` placement | 1 hit, #26, on a **free-text description** — explicitly sanctioned by `Reference/Rubric_Format.md` (line 69 and the worked example at line 106). Not near an id, date, email or amount. **Compliant.** |
| Agent-centric phrasing | 60/60 titles open with "The Agent". 0 passive. |
| Category balance | 60 outcome / 0 process. Outcome > Process. |
| Process three-condition test | No behaviour in this task qualifies: every required action produces an inspectable artifact (ticket, issue, comment, event, post, draft, final response), so no verification-not-execution behaviour is unprovable from outcomes. 0 process is correct, matching all four V3 reference tasks. |
| Channel lock-in (Phase 2.7 Major-by-default) | #27 names `#maintenance` **and** accepts the id or the name, and its FAIL clause is descriptive ("a channel that carries no push traffic"). Exactly one channel carries push traffic, so no valid alternative path is rejected — the Major escalation does not trigger and the taxonomy's Minor fallback does not either. **Clean.** |
| Grounded literals | Every concrete value in every title appears verbatim in `_aux/Universe_Split/`. Validator substring sweep clean; independently spot-checked on 16 atoms above. |
| 60-criterion cap (AGENTS.md rule 14) | **Exactly 60. Compliant, zero headroom.** |

## All 9 lenses status (rubrics scope)

- Lens 1 strict QC scoring :: **REVISE** — 3/5 Rubric sub-dims at 5, 2 at 4
- Lens 2 answer-leakage sweep :: **PASS**
- Lens 3 hardness end-to-end (rubric carriers) :: **PASS with note**
- Lens 4 strict density :: **PASS** (empirical, per model)
- Lens 5 adversarial review :: **PASS with 2 findings** (A-1, A-2)
- Lens 6 :: RETIRED v18 — not executed
- Lens 7 anti-rationalization :: **2 findings promoted** (A-1 from S4's "watch item, not a fix"; A-2 from FINAL's Bucket-3 disposition)
- Lens 8 regression-anchor verification :: **62/62 PASS**
- Lens 9 :: RETIRED v18 — not executed

## Sub-dim scoring (Dimension 4 — Rubric, 5 sub-dims)

| Sub-dim | Score | Basis under strictest reading |
|---|---|---|
| Overall Rubric Quality | **4** | Pass(5) requires "less than 5% of the rubrics have minor issues; no major or moderate issues". Two moderate issue classes survive verification: **A-1** (#5 over-specification, unrebutted asymmetry with #34) and **A-2** (#13/#31/#41 missing the anti-overclaim bound every sibling family carries). 2 of 60 = 3.3% moderate, well inside the spec's NON-FAIL band (<= 15%) — the platform would score this 3/4 at worst — but the Pass text says *no* moderate issues, so under AUDIT's rule this is 4. |
| All-Failing Rubrics | **4** | Pass(5) requires "**all** rubrics that failed all completed runs are valid". Eight criteria failed 12/12: #5, #7, #8, #9, #10, #13, #20, #24. Seven are clean Bucket 3. **#5 carries an over-specification issue that contributed to the failure** — `S4_fixes.md` records Opus run 6 reaching "electrical was reported 'still underway' … (OPS-186)" and failing on the literal June-17 dating. One invalid AF is below the spec's 2+ FAIL threshold, so the platform band is NON-FAIL, but "all are valid" is not met. |
| Rubric Category Balance | 5 | 60 outcome / 0 process. Outcome strictly greater than Process. |
| Process Rubrics | 5 | Three-condition test run against every candidate behaviour; none qualifies. Zero process is the correct answer here, not an omission. |
| Agent Centric Phrasing | 5 | 60/60 agent-centric, 0 tool names in titles, 0 passive constructions. |

## Findings (full detail, fixes and severity in `Council_Reports/AUDIT_all.md`)

- **[MODERATE] A-1** — #5 requires the literal "June 17, 2026" dating inside a write body, while its sibling #34 (same underlying fact, same record) was explicitly relaxed at 12:58 to state that naming the record or its date is not required. The asymmetry is unrebutted anywhere in the report chain. `S4_fixes.md` already pre-registers the exact fix (evidence-field accept-set: "June 17, 2026" **or** "the mid-initiative check-in" — OPS-186's own wording) and declined it only because Bucket 1 was empty. Under AUDIT's bar, a known cost-free fix on an AF criterion is a REVISE item.
- **[MINOR] A-2** — #13/#31/#41 waive only the Carlos 2026-05-26 "notice letters are out" reading. The likelier competing reading is left unwaived: OPS-81's 2026-05-23T14:00 comment ("Wesley and I finished out the remaining North cluster units … we got everything covered") and OPS-66 ("North cluster confirmed complete"), both of which OE 16 puts directly in the agent's result set. Separately, `FINAL_council.md` line 381 justifies this family with "nothing in the North chain is in a completed state" — that is **factually wrong**: OPS-40 "Preventive Maintenance Push - North Cluster Properties" is `state_OPS_4`, completed 2026-05-18T11:54. The criteria remain substantively defensible (OPS-40 closed ~11 hours *before* OPS-56 raised the flag, and OPS-81/OPS-66 are themselves In Progress / In Review prose), but the stated basis is wrong and the evidence fields do not carry the bound.
- **[LOW] A-3** — #58 and #59 generate 6 of the 10 contested run-cells. Both grade the agent's characterisation of a pre-existing record's claim rather than an artifact it produced. Both were adjudicated at S3/AUDIT_rubrics/FINAL and AUDIT_rubrics watch item N4 ("if both return all-fail, the remedy is a prompt-side nudge, not deletion") is satisfied — neither is AF (#58 7/12, #59 6/12). #59 additionally has no OE step designating its graded fact, which `Docs_starpm/8_QC_Spec_Doc2.md` permits for final-response criteria. Accepted; recorded so a reviewer sees it was examined.
- **[LOW] A-5** — #60 grades close to a restatement of the prompt's own premise ("it is still sitting open"), passing 11/12. Low-discrimination rather than defective; first cut candidate if the set ever needs a slot.

## Verification statements

- [x] Validator re-run during this audit (`validate.py --phase all`); rubrics phase **0 fails, 0 warns**, exit 0. `--phase submission_gate` 0 fails, 2 NOT_ATOMIC warns (both adjudicated above).
- [x] Regression-anchor suite executed: **62/62 PASS**; `check_regression.py` gate PASS (anchors 62/62, reports 21/21 identical, verdicts 7/7 unchanged).
- [x] `calc_similarity.py` re-run: top composite **27.2**, all under the 40 ceiling.
- [x] `verify_universe_atoms.py` re-run: 34 atoms, 0 fails, 1 reconciled warn.
- [x] Anti-rationalization output check passed. Two findings were **promoted** by it: A-1 (S4 had filed it as "watch item, not a fix") and A-2 (FINAL had closed it Bucket 3 on a basis that does not hold).
- [x] Verdict recorded with explicit per-issue trail in `Council_Reports/AUDIT_all.md`.

## Discrepancies surfaced

Two, both fix-in-place, both evidence-field-only, neither touching a title, a category, the prompt, the OE path, the write set, or the difficulty of the task: **A-1** (#5) and **A-2** (#13/#31/#41). Three further candidates were examined and recorded as residual risk rather than dropped in silence: criterion 20 atomicity, criterion 51 atomicity, and the criterion 58 / 59 characterisation family.

## Post-fix status (2026-07-26, operator-directed, same chat)

Findings **A-1 and A-2 are CLOSED**, alongside six further operator-directed changes (R5, R7, R19, R20, R21, R24). Full trail, including two self-inflicted validator regressions caught and repaired mid-pass, in `Council_Reports/AUDIT_all.md`. Pre-fix file at `_aux/7_Rubrics.pre_audit_fixes.json`.

Post-fix sub-dim movement, re-graded against the 12 trajectories:

| Sub-dim | Was | Now | Basis |
|---|---|---|---|
| Overall Rubric Quality | 4 | **5** | A-1 closed by R5, A-2 closed by the bound. One minor residual at 1.7% (criterion 9's absence clause), inside the <5% Pass band. |
| All-Failing Rubrics | 4 | **5** | All-failing-on-both drops 8 → 3 (criteria 9, 13, 20); all three justified with cited trajectory evidence in `S4_AF_justifications.md`. |
| Rubric Category Balance | 5 | 5 | 60 outcome / 0 process, unchanged. |
| Process Rubrics | 5 | 5 | unchanged. |
| Agent Centric Phrasing | 5 | 5 | 8 titles edited; all 60 still open with "The Agent", 0 tool names. |

Gates after the fixes: rubrics **0F/0W**, submission_gate 0F/2W (pre-existing), regression 62/62, set at 60. pass@1 unchanged at 0/6 on both models.

**Residual risks introduced by the fixes, recorded rather than buried:** no rubric title now names OPS-186 (both criterion 5 and criterion 34 resolve the record via their evidence fields — a real trade against the self-containment convention, not a costless win); R21 makes criterion 21 partly redundant with criteria 32 and 42; criterion 9's *"carried as still outstanding"* clause leans on an absence, with a pre-written one-line relaxation held in reserve.

## Verdict

**REVISE as raised; all findings CLOSED after the operator-directed fix pass.** All 24 sub-dims now score 5 on re-grade — but that re-grade was performed in the same chat that raised the findings, so it is a self-regrade and not an independent confirmation. `PASS (STRICT)` is deliberately **not** self-certified and `Tasks/_meta/Audit_Log.md` is deliberately **not** appended. Run `PIPELINE AUDIT — Tasks/44_6a62ccba8cad60844b8364b9 --phase rubrics` in a fresh chat for the confirmation pass before upload.

### Verdict as originally raised (pre-fix)

**REVISE** — rubrics phase, and therefore the task. 3 of 5 Rubric sub-dims at 5/5; Overall Rubric Quality and All-Failing Rubrics both at 4 under the strictest reading of their Pass(5) text. 0 BLOCKERs, 0 REBUILD conditions, 0 Major issues. Both fixes are single evidence-field appends and one of them (**A-1**) is already written out verbatim in `S4_fixes.md`. Both sub-dims sit inside the platform spec's NON-FAIL bands, so this is an internal-bar REVISE rather than a predicted platform rejection. Full per-issue trail and exact fix text: `_aux/Council_Reports/AUDIT_all.md`.
