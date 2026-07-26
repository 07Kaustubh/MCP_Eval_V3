# Verifier Fails: S4 verdict (dual-model)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Criteria set:** 60 · **Models verified:** Opus 4.8 (6 runs, complete) + Gemini (6 runs, complete)

> **Supersedes** `_superseded/S4_verdict.md`. Both halves of the dual-model loop are now closed.

---

## Input reconciliation (read this first)

`8a_Verifier_Fails_Opus.txt` **changed** between the superseded pass and this one. Both verifier files were re-exported at 2026-07-26 12:04 and both are graded against the **current** 60-criterion set, including the three criterion edits applied at 11:10. Three facts establish this:

1. All 60 criterion titles in both files match `7_Rubrics.json` exactly, for all 12 run blocks, including the three edited titles (tenant-access container, plumbing container, QC-record states).
2. The per-run Opus scores changed from 25/30/44/42/26/46 to **31/36/45/27/30/47**. The three applied edits alone cannot produce that delta.
3. The new `8a` matches the Opus trajectories on disk; the old one did not. Example: the superseded matrix recorded a fail on the plumbing budget-priority criterion for Opus run 1, but `Opus Run 1, tool call 9 (create_records_for_table)` writes `MT-2026-1328` with "the water heater replacements were also flagged as a budget priority (Brooke Phillips, 2026-06-03)", which the new `8a` correctly passes.

**Consequence.** The superseded Opus classification was built on a verifier export that did not correspond to the downloaded trajectories, so the entire Opus loop was re-run here alongside the Gemini loop. The three rubric edits already applied to `7_Rubrics.json` were re-checked against the new grading and all three stand.

---

## Trajectory gates

### T3 - Error Rate
Erroneous runs: **0/6 Opus**, **0/6 Gemini** (12/12 parsed `ok`). Verdict: **PASS (< 3)** on both models.

### T2 - Agent Failure Rate (pass@1 <= 40%)

| Model | Per-run criteria passed | Runs passing all criteria | pass@1 | Verdict |
|---|---|---|---|---|
| Opus 4.8 | 31 · 36 · 45 · 27 · 30 · 47 of 60 | 0/6 | **0.0%** | **PASS** |
| Gemini | 17 · 10 · 25 · 16 · 15 · 18 of 60 | 0/6 | **0.0%** | **PASS** |

The best Opus run leaves 13 criteria failing; the best Gemini run leaves 35. Neither model comes close to sweeping.

### T1 - Density (V4 target 40+ average per model)

| Model | Runs | Avg total calls | Avg MCP-only | Range (total) | Verdict |
|---|---|---|---|---|---|
| Opus 4.8 | 6 | **62.5** | 44.7 | 52 - 79 | **PASS** |
| Gemini | 6 | **79.8** | 67.0 | 60 - 91 | **PASS** |

Both models clear 40+ on both measures and every individual run clears it on totals. Against the projected 55.5 midpoint, Opus landed at 62.5 and Gemini at 79.8, so the projection under-counted.

---

## Run matrix (both models)

`F` = fail, `.` = pass. `B` = bucket: `1` rubric invalid, `2` judge error, `3` legitimate model failure, `-` no failures on either model.

| # | Opus 1-6 | Gem 1-6 | oF | gF | B | criterion |
|---|---|---|---|---|---|---|
| 1 | `......` | `......` | 0 | 0 | - | The Agent creates a new maintenance ticket in the Maintenance Tickets log for the field w... |
| 2 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent's new maintenance ticket describes the two North cluster units Jaime Salinas fl... |
| 3 | `FF.FF.` | `.F.FFF` | 4 | 4 | 3 | The Agent raises a tracking item on the Operations board for the West cluster preventive ... |
| 4 | `FF.FF.` | `FF.FFF` | 4 | 5 | 3 | The Agent's West cluster tracking item states that the West cluster's preventive maintena... |
| 5 | `FFFFF.` | `FFFFFF` | 5 | 6 | 3 | The Agent's West cluster tracking item states that OPS-186, dated June 17, 2026, records ... |
| 6 | `FF.FF.` | `......` | 4 | 0 | 3 | The Agent's West cluster tracking item names the owner of that work, which must be one of... |
| 7 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent raises a tracking item for the portfolio HVAC filter replacement run that was n... |
| 8 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's filter run tracking item states that John Smith reported on May 23, 2026 that... |
| 9 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's filter run tracking item records Brooke Phillips's outstanding request to Eli... |
| 10 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's filter run tracking item names the owner of that work, which must be one of: ... |
| 11 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | The Agent raises tracking work or a maintenance ticket covering the push units still wait... |
| 12 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | The Agent's tracking work or maintenance ticket for outstanding tenant access covers the ... |
| 13 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent's tracking work for outstanding tenant access covers the two North cluster unit... |
| 14 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | The Agent's tracking work for outstanding tenant access names the owner, which must be on... |
| 15 | `......` | `......` | 0 | 0 | - | The Agent raises tracking work or a maintenance ticket for the open plumbing findings fro... |
| 16 | `......` | `......` | 0 | 0 | - | The Agent records the two water heaters that are past serviceable life and need replaceme... |
| 17 | `......` | `......` | 0 | 0 | - | The Agent records the hose bibs at several units that need repair, either in a tracking i... |
| 18 | `....F.` | `FFFFFF` | 1 | 6 | 3 | The Agent's plumbing tracking item states that the water heater replacements were escalat... |
| 19 | `F.....` | `......` | 1 | 0 | 3 | The Agent's plumbing tracking item names the owner of that work, which must be one of: Ca... |
| 20 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent records that OPS-99 and OPS-108 carry the same East cluster HVAC QC title while... |
| 21 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent records that neither East cluster QC record, OPS-99 nor OPS-108, is in a comple... |
| 22 | `.....F` | `FFFFFF` | 1 | 6 | 3 | The Agent leaves a note on OPS-87 stating that the record does not stand as a close-out o... |
| 23 | `FFF.FF` | `FFFFFF` | 5 | 6 | 3 | The Agent leaves a note on OPS-96 stating that the portfolio filter spot-check does not s... |
| 24 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | The Agent leaves a note on OPS-98 stating that the record was never moved to a completed ... |
| 25 | `......` | `......` | 0 | 0 | - | The Agent schedules a re-inspection slot on Jaime Salinas's calendar (jaime.salinas@starp... |
| 26 | `......` | `......` | 0 | 0 | - | The Agent's re-inspection slot describes going back out to re-inspect the outstanding pre... |
| 27 | `......` | `......` | 0 | 0 | - | The Agent posts a status update for the crew in the #maintenance channel (C001), the chan... |
| 28 | `......` | `.F....` | 0 | 1 | 3 | The Agent's channel status update states that the end-of-June close-out target for the Pr... |
| 29 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent's channel status update states that one South cluster unit was never serviced b... |
| 30 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent's channel status update states that the two units Jaime Salinas flagged in the ... |
| 31 | `FFFFF.` | `FFFFFF` | 5 | 6 | 3 | The Agent's channel status update states that the access follow-up on two North cluster u... |
| 32 | `...FF.` | `FFFFFF` | 2 | 6 | 3 | The Agent's channel status update states that the East cluster QC record is not in a comp... |
| 33 | `...FF.` | `FF.FFF` | 2 | 5 | 3 | The Agent's channel status update tells the crew that the West cluster went through the p... |
| 34 | `FFFFF.` | `FFFFFF` | 5 | 6 | 3 | The Agent's channel status update states that the latest dated status statement on the We... |
| 35 | `FF..F.` | `.FFFFF` | 3 | 5 | 3 | The Agent's channel status update states that the portfolio HVAC filter replacement run w... |
| 36 | `......` | `.F.FF.` | 0 | 3 | **2** | The Agent's channel status update states that the plumbing findings, including the two wa... |
| 37 | `......` | `......` | 0 | 0 | - | The Agent drafts an email to brooke.phillips@starpm.com on the Preventive Maintenance Pus... |
| 38 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent's draft to Brooke Phillips states that the South cluster's open item is the uni... |
| 39 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent's draft to Brooke Phillips states that the missed South cluster unit still has ... |
| 40 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent's draft to Brooke Phillips states that the two North cluster units flagged on M... |
| 41 | `FFFFF.` | `FFFFFF` | 5 | 6 | 3 | The Agent's draft to Brooke Phillips separately identifies two North cluster units held u... |
| 42 | `.F.FF.` | `FFFFFF` | 3 | 6 | 3 | The Agent's draft to Brooke Phillips states that the East cluster QC is unconfirmed becau... |
| 43 | `...F..` | `FFFFFF` | 1 | 6 | 3 | The Agent's draft to Brooke Phillips states that the East cluster QC has to be confirmed ... |
| 44 | `...FF.` | `FF.FFF` | 2 | 5 | 3 | The Agent's draft to Brooke Phillips states that no spot-check record of Jaime Salinas's ... |
| 45 | `....F.` | `FF.FFF` | 1 | 5 | 3 | The Agent's draft to Brooke Phillips states that the West cluster still has to be QC walk... |
| 46 | `F..F..` | `FFFFF.` | 2 | 5 | 3 | The Agent's draft to Brooke Phillips names the person holding the outstanding tenant acce... |
| 47 | `.F..F.` | `.F..FF` | 2 | 3 | **2** | The Agent's draft to Brooke Phillips names the person holding the West cluster work, whic... |
| 48 | `.F.FF.` | `FFFFFF` | 3 | 6 | **1** | The Agent's draft to Brooke Phillips names the person holding the East cluster QC confirm... |
| 49 | `......` | `FF....` | 0 | 2 | **2** | The Agent's draft to Brooke Phillips states plainly that Jaime Salinas's earlier QC sign-... |
| 50 | `......` | `FF....` | 0 | 2 | **2** | The Agent's draft to Brooke Phillips states that the Preventive Maintenance Push should n... |
| 51 | `FF.FF.` | `FFFFFF` | 4 | 6 | 3 | The Agent reports in its final response that none of Jaime Salinas's three QC spot-check ... |
| 52 | `...F..` | `FF.FFF` | 1 | 5 | 3 | The Agent reports in its final response that Jaime Salinas's QC spot-check coverage never... |
| 53 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | The Agent reports in its final response that the South cluster still has one unit that wa... |
| 54 | `......` | `FFFFFF` | 0 | 6 | 3 | The Agent reports in its final response that the two North cluster units Jaime Salinas fl... |
| 55 | `...FF.` | `FFFFFF` | 2 | 6 | 3 | The Agent reports in its final response that the East cluster QC is unconfirmed rather th... |
| 56 | `......` | `.F..F.` | 0 | 2 | **2** | The Agent reports in its final response that the plumbing findings from the push, includi... |
| 57 | `FF..F.` | `.FFFFF` | 3 | 5 | 3 | The Agent reports in its final response that the portfolio HVAC filter replacement run wa... |
| 58 | `FFF.F.` | `FF.FF.` | 4 | 4 | **2** | The Agent reports in its final response that the electrical panel inspections across the ... |
| 59 | `.FFFF.` | `FF.F.F` | 4 | 4 | 3 | The Agent reports in its final response that the crew recorded the East cluster HVAC serv... |
| 60 | `......` | `FF....` | 0 | 2 | 3 | The Agent reports in its final response that the Preventive Maintenance Push cannot be cl... |

**Totals.** 8 criteria pass 6/6 on **both** models (1, 15, 16, 17, 25, 26, 27, 37). **52 criteria fail at least once.** Opus: 42 failing, 8 all-failing. Gemini: 50 failing, 32 all-failing. 8 criteria fail 12/12 across both models (7, 8, 9, 10, 13, 20, 21, 24). Fail cells: 144 Opus + 259 Gemini = 403 of 720.

---

## Classifications

Every one of the 52 failing criteria carries a trajectory citation. Buckets are assigned at the criterion level across the union of both models; per-run dissent is recorded in the sub-reports.

- **Bucket 1 (rubric invalid): 1 criterion** (idx 48, East QC holder accept-set) -> `S4_fixes.md`
- **Bucket 2 (judge error): 6 criteria** (idx 36, 47, 49, 50, 56, 58) -> `S4_judge_errors.md`
- **Bucket 3 (legitimate model failure): 45 criteria** -> 31 all-failing criteria carry justifications in `S4_AF_justifications.md`

Per model: Opus B1 = 1, B2 = 1, B3 = 40 of 42 failing. Gemini B1 = 0, B2 = 6, B3 = 44 of 50 failing.

**Disputed run-cells:** 22 of 403 fail cells (5.5%) are contested. 21 are judge errors (16 under the six Bucket 2 criteria, 5 under Bucket 3 criteria) and 1 is the rubric-phrasing false fail that produced the Bucket 1 entry. 20 of the 22 are on Gemini. The dominant judge-error shape is grading the agent's Linear writes when the criterion scopes itself to the draft body or the channel post, and one Gemini justification applies the wrong criterion's accept-set outright.

## All-Failing Rubrics sub-dim

| Basis | Bucket 1 ratio | Score |
|---|---|---|
| Union of both models, all 52 failing criteria | 1/52 = **1.9%** | **5/5 PASS** |
| Opus only, 42 failing criteria | 1/42 = **2.4%** | **5/5 PASS** |
| Gemini only, 50 failing criteria | 0/50 = **0.0%** | **5/5 PASS** |
| Criteria failing 6/6 on at least one model (32) | 1/32 = **3.1%** | **5/5 PASS** |

Every reading sits well under the 25% threshold. The failing set is dominated by genuine model gaps.

**Impact of the single Bucket 1 fix,** recomputed against the same 12 trajectories: one cell flips (Opus run 2), Opus per-run scores become 31/37/45/27/30/47, Gemini is unchanged, and pass@1 stays 0/6 on both models. All 8 criteria failing 12/12 are preserved intact.

---

## Hardness calibration

Measured against the four pre-registered predictions in `_aux/Hardness_Plan.md`. Both models now testable.

| # | Prediction | Outcome |
|---|---|---|
| 1 | **[HIGH]** Both models report the QC side complete-and-clean, never reading the Linear `state` column | **CONFIRMED at the criterion level on both models. OVER-PREDICTED at the conclusion level on Opus only.** The state column was skipped as designed: the two East-state criteria fail 12/12 and the OPS-98 state note fails 12/12. On Opus the headline verdict was still reached without it (the closeability and retraction criteria pass 6/6). On Gemini the prediction held in full: all six runs moved the QC records to Done and reported the push substantially complete. |
| 2 | **[HIGH]** Gemini names the open items but never issues the retraction | **FALSIFIED as stated, and the differentiator relocated.** Four of six Gemini drafts issue the retraction cleanly and the other two do as well and were mis-graded, so the retraction beat is 6/6 achievable on Gemini rather than near-0%. Gemini fails instead on **what** it names: the two North units flagged on May 23, the tenant-access holdovers and the West coverage gap are all absent, so the retraction is attached to the wrong open-item list. |
| 3 | **[MED]** Runs miss the South no-access unit and the unfinished filter run, both living in thread replies | **SPLIT, mechanism partly wrong.** Filter run: **CONFIRMED and stronger than predicted**, 12/12 fail across four criteria on both models. South no-access: **model-split**, Opus found it in 4 of 6 runs, Gemini in 0 of 6. |
| 4 | **[MED]** Runs overlook that Jaime's QC coverage never included West | **CONFIRMED, stronger on Gemini.** Opus surfaced the gap in narrative in 4 of 6 runs and raised the tracking item in 2. Gemini raised a West item in 2 of 6 but never framed it as a QC coverage gap, and named the coverage gap in narrative 1 of 6. |

**Stump hypothesis hit rate: 2 confirmed / 1 split / 1 falsified out of 4.**

### Mechanism correction - Lever 5 (thread-reply blindness) is Opus-inert, not universally inert

The superseded pass concluded that zero of 12 runs called `slack_read_thread`. That was measured against the mismatched export. Re-measured against the trajectories on disk: **Opus called it 0 times across all 6 runs; Gemini called it 9 times across 4 of 6 runs** (runs 1, 2, 3, 5). The lever fires as a retrieval barrier on Opus only.

It does not matter for outcomes either way, because `slack_read_channel(channel_id="C001", limit=100)` returns thread replies inline as flat messages, so the reply content was in every run's context regardless. John Smith's 20x25 post, Brooke Phillips's stock-count reply and the South reschedule replies all appear in the first channel read of all 12 runs. **The filter-run miss is a reasoning failure, not a retrieval failure**, on both models: the agents read "we'll need a restock before I can finish the run" and then closed the filter spot-check as a clean pass anyway.

**Consequence for future StarPM builds:** do not budget tool calls for `slack_read_thread` on Opus and do not select thread-reply blindness as an independent lever on this universe. Its two-to-four projected calls do not happen on Opus and buy nothing on Gemini.

### Under-predicted lever - near-miss entity pairs are a difficulty lever, not flavor

The Hardness Plan demoted near-miss entity confusion to "flavor, not a difficulty lever, carried but not counted". It produced the two strongest discriminators in the set:

- **The two North pairs.** The units flagged May 23 as deficient versus the OPS-56 units pending tenant access. Every run on both models collapsed them into one pair. The OPS-56-pair criterion fails 12/12; the deficiency-pair criteria fail 6/6 on Gemini while passing 6/6 on Opus.
- **OPS-99 versus OPS-108.** Identical title, opposing states. Fails 12/12. Three Opus runs retrieved both, called them duplicates, and never compared the states; all six Gemini runs moved both to Done.

The shape that works is a same-cluster, same-count, same-noun pair whose members differ only in *why* they are open. Promote to a first-class lever.

### The real cross-model differentiator on this task

The pre-registered Gemini-selective lever was the retraction beat. The measured one is **the May 23 field note**: the two North units Jaime Salinas flagged as needing HVAC right away. Four criteria carry it (the ticket description, the channel statement, the draft statement and the final-response statement) and every one of them is **6/6 pass on Opus and 6/6 fail on Gemini**. That is a cleaner asymmetric split than the retraction beat has ever produced, with the Opus sweep serving as the achievability proof. The mechanism is the multi-link chain: Gemini read the note and did not carry it past the read, while Opus traced it to the absence of any follow-up record.

### Lever re-attribution against the pre-registered rule

The plan pre-registered: "if runs surface the West-coverage gap but not the state contradiction, Lever 1 fired and Lever 2 did not." On Opus, 4 of 6 runs surfaced the West gap and none fully surfaced the state contradiction, so **latching fired and structured-DB skip fired on the granular records but not on the headline**. On Gemini, neither surfaced, so **both fired at full strength**. The multi-link chain off the field note carried the entire cross-model split and was worth more than its 7.5 projected cost implied.

---

## Action items

1. ~~Apply the single Bucket 1 evidence fix~~ **DONE 2026-07-26.** Applied to `7_Rubrics.json` idx 48, evidence field only, title unchanged. Set stays at 60. A subsequent strict QC pass (`QC_Strict_Check.md`) applied three further hardening fixes: OE 5 / OE 6 retrieval-mechanism correction, idx 34 evidence self-containment, idx 22/23/24 identifier-form latitude. Post-fix Opus per-run 31/**37**/45/27/30/47; pass@1 unchanged at 0/6 on both models. All gates re-run clean.
2. **Ship the 31 all-failing justifications** in `S4_AF_justifications.md`. Voice gate clean (`check_justification.py` exit 0), 0 em-dashes.
3. **Appeal the 21 judge-error run-cells** in `S4_judge_errors.md` if the platform supports per-run appeals. The highest-value appeals are the two retraction criteria on Gemini runs 1 and 2, which are graded against text that is capitalised in both drafts, and the West-holder criterion on Gemini run 6, whose justification applies the tenant-access accept-set.
4. **No REDO.** Both trajectory gates pass on both models: pass@1 0.0% against a 40% ceiling, density 62.5 and 79.8 against a 40 floor, 0 error runs. The task is neither too easy nor too thin, and it discriminates on both model families.
5. **Carry the two calibration corrections forward** (thread-reply blindness is Opus-inert; near-miss entity pairs are a first-class lever) into `Tasks/_meta/Hardness_Patterns_Log.md` and `Tasks/_meta/Stump_Hypotheses.md`. Both are appended.
