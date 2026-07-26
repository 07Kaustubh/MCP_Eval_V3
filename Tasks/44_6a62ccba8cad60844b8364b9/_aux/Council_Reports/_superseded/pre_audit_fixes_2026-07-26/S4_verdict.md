# Verifier Fails: S4 verdict (dual-model, pass 3)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Criteria set:** 60 · **Models verified:** Opus 4.8 (6 runs, complete) + Gemini (6 runs, complete)

> **Supersedes** `_superseded/pass2_2026-07-26_1245/S4_verdict.md`. Prior passes are retained under `_superseded/`.

---

## Input reconciliation (read this first)

Both verifier files were re-exported after the pass-2 verdict: `8a_Verifier_Fails_Opus.txt` at 13:24 and `8b_Verifier_Fails_Gemini.txt` at 13:28. The trajectories on disk are **unchanged** (`Agent_Responses/{Opus,Gemini}/`, all twelve files still stamped 10:50; `parse_trajectories.py` reproduces the identical per-run tool-call counts to the unit). What changed is the grading.

Between pass 2 and pass 3 the rubric file was edited once, at 12:58: **six evidence fields** on criteria 11, 22, 23, 24, 34 and 48. No title, category or justification changed, and the set stayed at 60. The three 12:35 edits from the pass-2 action list plus three further clarifications from `QC_Strict_Check.md` are all present.

| | Opus per-run | Gemini per-run |
|---|---|---|
| Pass 2 grading | 31 · 36 · 45 · 27 · 30 · 47 | 17 · 10 · 25 · 16 · 15 · 18 |
| Pass 3 grading (current) | **34 · 33 · 44 · 26 · 30 · 46** | **20 · 19 · 22 · 19 · 20 · 21** |

All 60 criterion titles in both files match `7_Rubrics.json` exactly across all 12 run blocks (720 of 720 decisions matched by title, 0 unmatched), so both files grade the current set.

### The finding that dominates this pass: grader variance on identical trajectories

**67 of 720 decision cells (9.3%) changed between the two gradings**, against byte-identical trajectories. Only **6** of those 67 fall on the six criteria whose evidence text was edited. The other **61 (8.5% of all cells)** are on criteria whose text did not change by a character.

- 42 cells moved Fail to Pass, 25 moved Pass to Fail.
- Net effect is model-asymmetric: Gemini gained 20 criteria-passed across its six runs, Opus lost 3.
- Largest single-run swings: Gemini run 2 moved 10 to 19, Gemini run 5 moved 15 to 20, Opus run 2 moved 36 to 33.
- Verified by hand: several of the newly-failing cells contradict text present verbatim in the trajectory. `Opus run 6` on criterion 6 is the clearest, and is documented in `S4_judge_errors.md`.

**What this does and does not change.** It does not move the task verdict: both gradings give pass@1 = 0/6 on both models, both give 0 error runs, and density is a trajectory property that grading cannot touch. All three hard gates pass under either export. What it does change is the confidence attachable to any **single** run-cell. Per-cell appeals on this task are worth filing only where the trajectory text is unambiguous, and the ten cells in `S4_judge_errors.md` are scoped to exactly that standard.

---

## Trajectory gates

### T3 - Error Rate
Erroneous runs: **0/6 Opus**, **0/6 Gemini** (12/12 parsed `ok`). Verdict: **PASS (< 3)** on both models.

### T2 - Agent Failure Rate (pass@1 <= 40%)

| Model | Per-run criteria passed | Runs passing all criteria | pass@1 | Verdict |
|---|---|---|---|---|
| Opus 4.8 | 34 · 33 · 44 · 26 · 30 · 46 of 60 | 0/6 | **0.0%** | **PASS** |
| Gemini | 20 · 19 · 22 · 19 · 20 · 21 of 60 | 0/6 | **0.0%** | **PASS** |

The best Opus run leaves 14 criteria failing; the best Gemini run leaves 38. Neither model comes close to sweeping, and the margin is wide enough that the grader variance above cannot threaten the gate.

### T1 - Density (V4 target 40+ average per model)

| Model | Runs | Avg total calls | Avg MCP-only | Range (total) | Verdict |
|---|---|---|---|---|---|
| Opus 4.8 | 6 | **62.5** | 44.7 | 52 - 79 | **PASS** |
| Gemini | 6 | **79.8** | 67.0 | 60 - 91 | **PASS** |

Both models clear 40+ on both measures and every individual run clears it on totals.

---

## Run matrix (both models)

`F` = fail, `.` = pass. `B` = bucket: `1` rubric invalid, `2` judge error, `3` legitimate model failure, `-` no failures on either model.

| # | Opus 1-6 | Gem 1-6 | oF | gF | B | criterion |
|---|---|---|---|---|---|---|
| 1 | `......` | `......` | 0 | 0 | - | The Agent creates a new maintenance ticket in the Maintenance Tickets log for the f... |
| 2 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent's new maintenance ticket describes the two North cluster units Jaime Sali... |
| 3 | `FF.FF.` | `...F..` | 4 | 1 | 3 | The Agent raises a tracking item on the Operations board for the West cluster preve... |
| 4 | `FF.FF.` | `FFFFFF` | 4 | 6 | 3 | The Agent's West cluster tracking item states that the West cluster's preventive ma... |
| 5 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's West cluster tracking item states that OPS-186, dated June 17, 2026, re... |
| 6 | `FF.FFF` | `...F..` | 5 | 1 | 3 | The Agent's West cluster tracking item names the owner of that work, which must be ... |
| 7 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent raises a tracking item for the portfolio HVAC filter replacement run that... |
| 8 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's filter run tracking item states that John Smith reported on May 23, 202... |
| 9 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's filter run tracking item records Brooke Phillips's outstanding request ... |
| 10 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's filter run tracking item names the owner of that work, which must be on... |
| 11 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | The Agent raises tracking work or a maintenance ticket covering the push units stil... |
| 12 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | The Agent's tracking work or maintenance ticket for outstanding tenant access cover... |
| 13 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's tracking work for outstanding tenant access covers the two North cluste... |
| 14 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | The Agent's tracking work for outstanding tenant access names the owner, which must... |
| 15 | `......` | `......` | 0 | 0 | - | The Agent raises tracking work or a maintenance ticket for the open plumbing findin... |
| 16 | `......` | `......` | 0 | 0 | - | The Agent records the two water heaters that are past serviceable life and need rep... |
| 17 | `......` | `......` | 0 | 0 | - | The Agent records the hose bibs at several units that need repair, either in a trac... |
| 18 | `.F..F.` | `FFFFFF` | 2 | 6 | 3 | The Agent's plumbing tracking item states that the water heater replacements were e... |
| 19 | `F.....` | `......` | 1 | 0 | 3 | The Agent's plumbing tracking item names the owner of that work, which must be one ... |
| 20 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent records that OPS-99 and OPS-108 carry the same East cluster HVAC QC title... |
| 21 | `FF.FFF` | `FFFFFF` | 5 | 6 | 3 | The Agent records that neither East cluster QC record, OPS-99 nor OPS-108, is in a ... |
| 22 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent leaves a note on OPS-87 stating that the record does not stand as a close... |
| 23 | `FFF.FF` | `FFFFFF` | 5 | 6 | 3 | The Agent leaves a note on OPS-96 stating that the portfolio filter spot-check does... |
| 24 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent leaves a note on OPS-98 stating that the record was never moved to a comp... |
| 25 | `......` | `......` | 0 | 0 | - | The Agent schedules a re-inspection slot on Jaime Salinas's calendar (jaime.salinas... |
| 26 | `......` | `......` | 0 | 0 | - | The Agent's re-inspection slot describes going back out to re-inspect the outstandi... |
| 27 | `......` | `......` | 0 | 0 | - | The Agent posts a status update for the crew in the #maintenance channel (C001), th... |
| 28 | `......` | `.F..F.` | 0 | 2 | 3 | The Agent's channel status update states that the end-of-June close-out target for ... |
| 29 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent's channel status update states that one South cluster unit was never serv... |
| 30 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent's channel status update states that the two units Jaime Salinas flagged i... |
| 31 | `FFFFF.` | `FFFFFF` | 5 | 6 | 3 | The Agent's channel status update states that the access follow-up on two North clu... |
| 32 | `...FF.` | `FFFFFF` | 2 | 6 | 3 | The Agent's channel status update states that the East cluster QC record is not in ... |
| 33 | `.F.FF.` | `FF.FFF` | 3 | 5 | 3 | The Agent's channel status update tells the crew that the West cluster went through... |
| 34 | `.F.FF.` | `FFF.FF` | 3 | 5 | 3 | The Agent's channel status update states that the latest dated status statement on ... |
| 35 | `.FF.F.` | `FF.FFF` | 3 | 5 | 3 | The Agent's channel status update states that the portfolio HVAC filter replacement... |
| 36 | `......` | `......` | 0 | 0 | - | The Agent's channel status update states that the plumbing findings, including the ... |
| 37 | `......` | `......` | 0 | 0 | - | The Agent drafts an email to brooke.phillips@starpm.com on the Preventive Maintenan... |
| 38 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent's draft to Brooke Phillips states that the South cluster's open item is t... |
| 39 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent's draft to Brooke Phillips states that the missed South cluster unit stil... |
| 40 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent's draft to Brooke Phillips states that the two North cluster units flagge... |
| 41 | `FFFFF.` | `FFFFFF` | 5 | 6 | 3 | The Agent's draft to Brooke Phillips separately identifies two North cluster units ... |
| 42 | `...FF.` | `FFFFFF` | 2 | 6 | 3 | The Agent's draft to Brooke Phillips states that the East cluster QC is unconfirmed... |
| 43 | `...FF.` | `FFFF.F` | 2 | 5 | 3 | The Agent's draft to Brooke Phillips states that the East cluster QC has to be conf... |
| 44 | `.F.FF.` | `FF.FFF` | 3 | 5 | 3 | The Agent's draft to Brooke Phillips states that no spot-check record of Jaime Sali... |
| 45 | `.F.FF.` | `F.....` | 3 | 1 | 3 | The Agent's draft to Brooke Phillips states that the West cluster still has to be Q... |
| 46 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent's draft to Brooke Phillips names the person holding the outstanding tenan... |
| 47 | `.FF.F.` | `......` | 3 | 0 | 3 | The Agent's draft to Brooke Phillips names the person holding the West cluster work... |
| 48 | `...FF.` | `FFFF.F` | 2 | 5 | 3 | The Agent's draft to Brooke Phillips names the person holding the East cluster QC c... |
| 49 | `......` | `......` | 0 | 0 | - | The Agent's draft to Brooke Phillips states plainly that Jaime Salinas's earlier QC... |
| 50 | `......` | `......` | 0 | 0 | - | The Agent's draft to Brooke Phillips states that the Preventive Maintenance Push sh... |
| 51 | `.FFF..` | `FFFFFF` | 3 | 6 | 3 | The Agent reports in its final response that none of Jaime Salinas's three QC spot-... |
| 52 | `.F.F..` | `FFFFFF` | 2 | 6 | 3 | The Agent reports in its final response that Jaime Salinas's QC spot-check coverage... |
| 53 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent reports in its final response that the South cluster still has one unit t... |
| 54 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent reports in its final response that the two North cluster units Jaime Sali... |
| 55 | `...FF.` | `FFFFFF` | 2 | 6 | 3 | The Agent reports in its final response that the East cluster QC is unconfirmed rat... |
| 56 | `......` | `......` | 0 | 0 | - | The Agent reports in its final response that the plumbing findings from the push, i... |
| 57 | `.FF.F.` | `FFFFFF` | 3 | 6 | 3 | The Agent reports in its final response that the portfolio HVAC filter replacement ... |
| 58 | `FFF.F.` | `.FF.F.` | 4 | 3 | 3 | The Agent reports in its final response that the electrical panel inspections acros... |
| 59 | `FF.FF.` | `..F.F.` | 4 | 2 | 3 | The Agent reports in its final response that the crew recorded the East cluster HVA... |
| 60 | `......` | `...F..` | 0 | 1 | 3 | The Agent reports in its final response that the Preventive Maintenance Push cannot... |

**Totals.** 12 criteria pass 6/6 on **both** models (1, 15, 16, 17, 25, 26, 27, 36, 37, 49, 50, 56). **48 criteria fail at least once.** Opus: 41 failing, 8 all-failing. Gemini: 46 failing, 33 all-failing. 8 criteria fail 12/12 across both models (5, 7, 8, 9, 10, 13, 20, 24). Fail cells: 147 Opus + 239 Gemini = **386 of 720**.

Four criteria that pass-2 recorded as failing are now clean 12/12: **36, 49, 50 and 56**. All four were pass-2 Bucket 2 entries, and the new grading independently vacated every disputed cell on them. Criterion 47's three Gemini disputes were vacated as well. That is 11 of the 22 pass-2 contested cells corrected without any rubric change, which is the strongest available confirmation that the pass-2 Bucket 2 calls were right.

---

## Classifications

Every one of the 48 failing criteria carries a trajectory citation. Buckets are assigned at the criterion level across the union of both models; contested individual cells are recorded separately.

- **Bucket 1 (rubric invalid): 0 criteria.** The single pass-2 Bucket 1 entry (criterion 48, East QC holder accept-set) was fixed at 12:35, and the fix landed: `Opus run 2` flipped to Pass on the amended evidence, which is exactly the cell the fix targeted. Every remaining fail on criterion 48 is a draft that treats the East cluster as closed. No new Bucket 1 entry survived the 5-point checklist. See `S4_fixes.md`.
- **Bucket 2 (judge error): 0 criteria at the criterion level.** No criterion has a majority of its fail cells contested. **10 individual run-cells** are contested and are itemised in `S4_judge_errors.md`.
- **Bucket 3 (legitimate model failure): 48 criteria.** 33 of them fail all six runs on at least one model and carry justifications in `S4_AF_justifications.md`.

Per model: Opus B3 = 41 of 41 failing; Gemini B3 = 46 of 46 failing.

**Contested run-cells:** 10 of 386 fail cells (2.6%), spread over six criteria (6, 18, 34, 52, 58, 59). Down from 22 of 403 in pass 2, and the composition changed: pass 2's contested cells were 20-of-22 on Gemini and clustered on the retraction beat, which the new grading fixed outright. Pass 3's contested cells split 4 Opus / 6 Gemini and cluster instead on two "recorded as finished" criteria (58 and 59) where the judge repeatedly demands a meta-framing that separates the record's claim from the work, which neither criterion asks for.

## All-Failing Rubrics sub-dim

| Basis | Bucket 1 ratio | Score |
|---|---|---|
| Union of both models, all 48 failing criteria | 0/48 = **0.0%** | **5/5 PASS** |
| Opus only, 41 failing criteria | 0/41 = **0.0%** | **5/5 PASS** |
| Gemini only, 46 failing criteria | 0/46 = **0.0%** | **5/5 PASS** |
| Criteria failing 6/6 on at least one model (33) | 0/33 = **0.0%** | **5/5 PASS** |

Every reading is 0% against a 25% threshold. The failing set is entirely legitimate model failures, with ten contested cells that do not reach criterion level anywhere.

### One criterion to watch (recorded, not a Bucket 1 entry)

**Criterion 5** ("the West cluster tracking item states that OPS-186, dated June 17, 2026, records the West Cluster work as still underway") fails 12/12 and is the tightest criterion in the set. `Opus run 6, tool call 49 (save_issue)` created OPS-1002 with the description "electrical was reported \"still underway\" at the mid-initiative check-in (OPS-186)". That names the record and the still-underway status and misses only the June 17 dating and the West-versus-electrical scoping. The criterion survives all five checklist questions: it is grounded, atomic in the sense of describing one record's one statement, required by the prompt's "get our tracking to match" instruction, uses no tool names, and Opus run 6 shows it is nearly reachable. It stays Bucket 3. It is flagged here because it is the criterion most likely to be read as over-specific by a downstream reviewer, and because the run-6 judge text on it ("does not contain any reference to OPS-186") is factually wrong even though the decision is defensible.

---

## Hardness calibration

Measured against the four pre-registered predictions in `_aux/Hardness_Plan.md`, re-scored against the pass-3 grading. The trajectories did not change, so the mechanism findings from pass 2 stand; the counts below are updated.

| # | Prediction | Outcome |
|---|---|---|
| 1 | **[HIGH]** Both models report the QC side complete-and-clean, never reading the Linear `state` column | **CONFIRMED at the criterion level on both models. OVER-PREDICTED at the conclusion level on Opus.** The state column was skipped as designed: criterion 20 fails 12/12, criterion 24 fails 12/12, criterion 21 fails 11/12. On Opus the headline verdict was still reached without it (criteria 49, 50 and 60 pass 6/6). On Gemini the prediction held on the records and failed on the headline: every Gemini run moved the QC records to Done, yet all six drafts still issued the retraction. |
| 2 | **[HIGH]** Gemini names the open items but never issues the retraction | **FALSIFIED, and now unambiguously so.** Criteria 49 and 50 pass 12/12 in the new grading, up from 4/6 on Gemini in pass 2. The retraction beat is fully reachable on both models. Gemini fails instead on **what** it names: the May 23 North pair, the tenant-access holdovers and the West coverage gap are absent, so the retraction attaches to the wrong open-item list. |
| 3 | **[MED]** Runs miss the South no-access unit and the unfinished filter run, both living in thread replies | **SPLIT, mechanism partly wrong.** Filter run: **CONFIRMED and stronger than predicted**, criteria 7, 8, 9 and 10 fail 12/12, and criterion 57 fails 6/6 on Gemini. South no-access: **model-split**, criterion 29 fails 2/6 on Opus and 6/6 on Gemini. |
| 4 | **[MED]** Runs overlook that Jaime's QC coverage never included West | **CONFIRMED on the framing, not on the artifact.** Under the new grading Gemini raises a West tracking item in 5 of 6 runs (criterion 3 fails only run 4) but **never once frames it as a QC coverage gap** (criterion 4 fails 6/6, criterion 52 fails 6/6). Opus raises the item in 2 of 6 and frames it correctly in 3 of 6. The lever fires on the framing, not on whether an item gets created. |

**Stump hypothesis hit rate: 2 confirmed / 1 split / 1 falsified out of 4** (unchanged from pass 2; prediction 4's mechanism is sharpened).

### The cross-model differentiator holds exactly

The **May 23 field note** (the two North units Jaime Salinas flagged as needing HVAC right away) carries four criteria: the ticket description (2), the channel statement (30), the draft statement (40) and the final-response statement (54). All four are **6/6 pass on Opus and 6/6 fail on Gemini** under both gradings. Across 67 cells of grader movement, not one of those 24 cells moved. That is the most stable signal in the entire matrix and it is the cleanest asymmetric split this pipeline has produced. The Opus sweep is the achievability proof; the Gemini sweep is the difficulty.

### Carried forward from pass 2 (mechanisms, unaffected by regrading)

- **Thread-reply blindness is Opus-inert.** Opus called `slack_read_thread` 0 times across all 6 runs; Gemini called it 9 times across 4 runs. It does not matter either way, because `slack_read_channel(channel_id="C001", limit=100)` returns thread replies inline, so John Smith's 20x25 post and Brooke Phillips's stock-count reply were in every run's context. The filter-run miss is a **reasoning** failure on both models, not a retrieval one. Do not budget calls for it and do not select it as an independent lever on this universe.
- **Near-miss entity pairs are a first-class lever, not flavor.** The two North pairs (May 23 deficiency pair versus the OPS-56 tenant-access pair) and OPS-99 versus OPS-108 (identical title, opposing states) produced the two strongest discriminators. Criterion 13 fails 12/12, criterion 20 fails 12/12. Every run on both models collapsed the North pairs into one.

### New calibration finding: grader variance is a first-class risk on 60-criterion sets

Two gradings of the same twelve trajectories disagreed on 61 cells that no rubric edit touched. The disagreement is concentrated on criteria whose subject is a **statement about a record's own claim** rather than an artifact the agent either did or did not create. Criteria 58 and 59 account for 6 of the 10 contested cells in this pass and both are of that shape. Criteria that grade a **created artifact and its contents** (1, 15, 16, 17, 25, 26, 27, 37) moved zero cells across both gradings.

**Consequence for future builds:** prefer criteria that grade an artifact's existence and content over criteria that grade the agent's characterisation of a pre-existing record's claim. Where the latter is needed for a lever, spend the evidence field on an explicit accept-set of phrasings, as was done for criterion 58, and expect it to still absorb variance.

---

## Action items

1. **No rubric fixes required.** Bucket 1 is empty. The pass-2 Bucket 1 fix on criterion 48 is verified landed (`Opus run 2` flipped to Pass). `7_Rubrics.json` stays at 60 criteria and needs no further edit for S4 purposes. `S4_fixes.md` records the closed fix and the criterion-5 watch item.
2. **Ship the 33 all-failing justifications** in `S4_AF_justifications.md`. Voice gate clean (`check_justification.py` exit 0), 0 em-dashes.
3. **Appeal the 10 contested run-cells** in `S4_judge_errors.md` if the platform supports per-run appeals. The three highest-value appeals are `Opus run 6 / criterion 6` (the description says "Owner: Lisa Smith (cluster lead)" and the judge wrote that it does not), `Gemini run 3 / criterion 58` (the response says "Electrical panel inspections complete (Patricia Nguyen)" under a South Cluster heading) and `Gemini run 5 / criterion 59` (the response names the coil cleaning, which the evidence states is sufficient on its own).
4. **Report the grader-variance measurement to the platform** alongside the appeals. 61 of 720 cells moved between two gradings of identical trajectories with no rubric change on those criteria. This is more actionable as a single measurement than as ten separate appeals.
5. **No REDO.** Both trajectory gates pass on both models under both exports: pass@1 0.0% against a 40% ceiling, density 62.5 and 79.8 against a 40 floor, 0 error runs. The task is neither too easy nor too thin and it discriminates cleanly across model families.
6. **Carry the calibration findings forward** into `Tasks/_meta/Hardness_Patterns_Log.md` and `Tasks/_meta/Stump_Hypotheses.md`. Both are appended.
