# Verifier Fails — S4 verdict

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Criteria set:** 60 · **Models verified:** Opus 4.8 (complete), Gemini (BLOCKED)

---

## Phase-readiness

`phase_ready.py --phase s4` returns **exit 1**: `8b_Verifier_Fails_Gemini.txt (empty)`. The file is 0 bytes on disk (last written 2026-07-25 23:56) while `8a_Verifier_Fails_Opus.txt` carries all six Opus run blocks (120,197 bytes, 2026-07-26 10:28). All twelve trajectories are present and parse cleanly.

**Consequence.** The Opus half of the dual-model loop is complete and is reported below. The Gemini half cannot be run: Evals_starpm/4 mandates one classification pass per model, and there is no Gemini verifier output to classify. **S4 is not closed until the Gemini file is saved and the second loop runs.**

---

## Trajectory gates

### Trajectory T3 — Error Rate
Erroneous runs: **0/6 opus**, **0/6 gemini** (12/12 parsed `ok`). Verdict: **PASS (< 3)** for both models.

### Trajectory T2 — Agent Failure Rate (pass@1 <= 40%)
Runs passing all valid criteria, opus: **0/6**. pass@1: **0.0%**. Verdict: **PASS (<= 40%)**.
Per-run opus scores: 25/60 · 30/60 · 44/60 · 42/60 · 26/60 · 46/60. Best run leaves 14 criteria failing.
Gemini pass@1: **not computable** (no verifier output). Verdict: **DEFERRED**.

### Trajectory T1 — Density (V4 target 40+ average per model)
| Model | Runs | Avg total calls | Avg MCP-only calls | Range (total) | Verdict |
|---|---|---|---|---|---|
| opus | 6 | **62.5** | 44.7 | 52 - 79 | **PASS** |
| gemini | 6 | **79.8** | 67.0 | 60 - 91 | **PASS** |

Both models clear 40+ on both the total and the MCP-only measure, and every individual run clears it on totals. Against the Hardness Plan projection of 55.5 midpoint, opus landed at 62.5 and gemini at 79.8, so the projection under-counted rather than over-counted.

---

## Run matrix (opus)

`F` = fail, `.` = pass. Bucket column: `1` rubric invalid, `2` judge error, `3` legitimate model failure, `-` no failures.

| # | 1 2 3 4 5 6 | fails | bucket | criterion |
|---|---|---|---|---|
| 1 | `......` | 0 | - | The Agent creates a new maintenance ticket in the Maintenance Tickets log for the field work that still needs a technician back onsite. |
| 2 | `......` | 0 | - | The Agent's new maintenance ticket describes the two North cluster units Jaime Salinas flagged on May 23, 2026. |
| 3 | `FF.FF.` | 4 | 3 | The Agent raises a tracking item on the Operations board for the West cluster QC coverage gap. |
| 4 | `FF.FF.` | 4 | 3 | West tracking item states the West work was never covered by a QC spot-check record. |
| 5 | `FFFFF.` | 5 | 3 | West tracking item states OPS-186, dated June 17 2026, records West work still underway. |
| 6 | `FF.FF.` | 4 | 3 | West tracking item names the owner (Lisa Smith / John Smith / Brooke Phillips). |
| 7 | `FFFFFF` | 6 | 3 | The Agent raises a tracking item for the portfolio HVAC filter replacement run that was never finished. |
| 8 | `FFFFFF` | 6 | 3 | Filter item states John Smith reported the May 23 2026 20x25 shortage blocking the run. |
| 9 | `FFFFFF` | 6 | 3 | Filter item records Brooke Phillips's outstanding stock-count request to Elias Navarro. |
| 10 | `FFFFFF` | 6 | 3 | Filter item names the owner (John Smith / Elias Navarro / Brooke Phillips). |
| 11 | `FFFFFF` | 6 | **1** | The Agent raises a tracking item covering the push units still waiting on tenant access. |
| 12 | `F..F.F` | 3 | 3 | Tenant-access work covers the single South cluster unit missed on the access window. |
| 13 | `FFFFFF` | 6 | 3 | Tenant-access work covers the two North cluster units OPS-56 records as held up by scheduling conflicts. |
| 14 | `F..F.F` | 3 | 3 | Tenant-access work names the owner (Carlos Mendez / Elias Navarro / Tony Reyes). |
| 15 | `FF..FF` | 4 | **1** | The Agent raises a tracking item for the open plumbing findings from the push. |
| 16 | `......` | 0 | - | Records the two water heaters past serviceable life, in a tracking item or the ticket log. |
| 17 | `......` | 0 | - | Records the hose bibs needing repair, in a tracking item or the ticket log. |
| 18 | `F...F.` | 2 | 3 | Plumbing item states the water heater replacements were escalated to a budget priority. |
| 19 | `F.....` | 1 | 3 | Plumbing item names the owner (Carlos Mendez / Brooke Phillips). |
| 20 | `FFFFFF` | 6 | 3 | Records that OPS-99 and OPS-108 carry the same title in two different workflow states. |
| 21 | `FF.FFF` | 5 | 3 | Records that neither OPS-99 nor OPS-108 is in a completed workflow state. |
| 22 | `......` | 0 | - | Note on OPS-87 that the record does not stand as a close-out of South and North QC. |
| 23 | `FFF.FF` | 5 | 3 | Note on OPS-96 that the filter spot-check does not stand because of the 20x25 restock block. |
| 24 | `FFFFFF` | 6 | 3 | Note on OPS-98 that the record was never moved to a completed state despite its own text. |
| 25 | `......` | 0 | - | Schedules a re-inspection slot on Jaime Salinas's calendar dated on or after July 1 2026. |
| 26 | `......` | 0 | - | Re-inspection slot describes re-inspecting the outstanding follow-up work. |
| 27 | `......` | 0 | - | Posts a status update in the #maintenance channel (C001). |
| 28 | `......` | 0 | - | Channel update states the end-of-June close-out target passed with work still open. |
| 29 | `F.....` | 1 | 3 | Channel update states one South cluster unit was never serviced on a missed access window. |
| 30 | `......` | 0 | - | Channel update states the two units flagged May 23 2026 still need the HVAC work. |
| 31 | `FFF.F.` | 4 | 3 | Channel update states the two North units held up by scheduling conflicts are still open. |
| 32 | `FF..F.` | 3 | 3 | Channel update states the East cluster QC record is not in a completed workflow state. |
| 33 | `.F..F.` | 2 | 3 | Channel update tells the crew West went through the push without QC spot-check coverage. |
| 34 | `FFF.F.` | 4 | 3 | Channel update states the latest dated status statement on West records work still underway. |
| 35 | `FF..F.` | 3 | 3 | Channel update states the filter run was left unfinished after the 20x25 restock block. |
| 36 | `F.....` | 1 | 3 | Channel update states the plumbing findings including two water heaters are still open. |
| 37 | `......` | 0 | - | Drafts an email to brooke.phillips@starpm.com on the close-out position. |
| 38 | `F.....` | 1 | 3 | Draft states the South open item is the unit missed on the access window. |
| 39 | `F.....` | 1 | 3 | Draft states the missed South unit must be re-scheduled for service before close. |
| 40 | `......` | 0 | - | Draft states the two North units flagged May 23 2026 still need a technician onsite. |
| 41 | `FFF.F.` | 4 | 3 | Draft separately identifies the two North units held up by tenant scheduling conflicts. |
| 42 | `.F..F.` | 2 | 3 | Draft states East QC is unconfirmed because the QC record is not in a completed state. |
| 43 | `....F.` | 1 | 3 | Draft states the East cluster QC has to be confirmed before the push can close. |
| 44 | `.F..F.` | 2 | 3 | Draft states no spot-check record of Jaime's covers the West cluster. |
| 45 | `.F..F.` | 2 | 3 | Draft states the West cluster still has to be QC walked before close. |
| 46 | `F.....` | 1 | 3 | Draft names the person holding the outstanding tenant access work. |
| 47 | `.F..F.` | 2 | 3 | Draft names the person holding the West cluster work. |
| 48 | `....F.` | 1 | 3 | Draft names the person holding the East cluster QC confirmation. |
| 49 | `......` | 0 | - | Draft states plainly that Jaime Salinas's earlier QC sign-off does not hold. |
| 50 | `......` | 0 | - | Draft states the push should not be treated as closeable yet. |
| 51 | `FF..F.` | 3 | **1** | Final response reports none of OPS-87, OPS-96, OPS-98 is in a completed workflow state. |
| 52 | `.F..F.` | 2 | 3 | Final response reports Jaime's QC coverage never included the West cluster. |
| 53 | `F..F..` | 2 | 3 | Final response reports the South cluster still has one unit missed on tenant access. |
| 54 | `......` | 0 | - | Final response reports the two North units flagged May 23 2026 still need the HVAC work. |
| 55 | `....F.` | 1 | 3 | Final response reports the East cluster QC is unconfirmed rather than complete. |
| 56 | `F.....` | 1 | 3 | Final response reports the plumbing findings including two water heaters are still open. |
| 57 | `FFF.F.` | 4 | 3 | Final response reports the portfolio filter replacement run was left unfinished. |
| 58 | `FFFFFF` | 6 | **2** | Final response reports the South cluster electrical panel inspections are recorded finished. |
| 59 | `FFFFF.` | 5 | 3 | Final response reports the crew recorded the East cluster HVAC service work as complete. |
| 60 | `......` | 0 | - | Final response reports the push cannot be closed out as of July 1 2026. |

**Totals.** 16 criteria pass 6/6. **44 criteria fail at least once.** 9 criteria fail 6/6 (7, 8, 9, 10, 11, 13, 20, 24, 58).

---

## Classifications

- **Bucket 1 (rubric invalid): 3 criteria** — 11, 15, 51 → see `S4_fixes.md`
- **Bucket 2 (judge error): 1 criterion** — 58 → see `S4_judge_errors.md`
- **Bucket 3 (legitimate model failure): 40 criteria** → 7 all-failing criteria carry AF justifications in `S4_AF_justifications.md`

Every one of the 44 carries a trajectory citation. All three Bucket 1 entries are the same defect class: a container criterion locks in a destination that the Oracle Events explicitly leave open, or grades a state after an OE-permitted write has changed it. No Bucket 1 entry is a coverage carrier or a Hardness lever carrier, so all three fixes are re-phrasings. **The set stays at 60 criteria; nothing is merged and nothing is cut.**

## All-Failing Rubrics sub-dim

| Basis | Bucket 1 ratio | Score |
|---|---|---|
| Across all 44 failing criteria | 3/44 = **6.8%** | **5/5 PASS** |
| Across the 9 criteria failing 6/6 | 1/9 = **11.1%** | **5/5 PASS** |

Both readings sit well under the 25% threshold. The failing set is dominated by genuine model gaps, not by invalid criterion design.

**Post-fix re-scoring (fixes applied 2026-07-26).** Recomputed against the same six Opus trajectories, the three fixes move 8 run-cells from Fail to Pass and change no criterion's design intent:

| Criterion | Before | After | Runs rescued |
|---|---|---|---|
| 11 (tenant access container) | 6/6 fail | **3/6 fail** | 2, 3, 5 wrote a maintenance ticket naming the South no-access unit and already passed criteria 12 and 14 on it |
| 15 (plumbing container) | 4/6 fail | **0/6 fail** | 1, 2, 5, 6 routed the plumbing findings to the ticket log exactly as OE 32 permits |
| 51 (QC record states) | 3/6 fail | **2/6 fail** | 5 reported the as-found finding and was failed only for flipping OPS-96 |

Per-run scores move 25/30/44/42/26/46 to **26/32/45/42/29/47** of 60. pass@1 is **unchanged at 0/6**: the best run still leaves 13 criteria failing. Criteria 7, 8, 9, 10, 13, 20 and 24 all still fail 6/6, so every all-failing Bucket 3 discriminator is preserved intact. Removing a false-fail did not soften the task, which reproduces the Task 41 post-fix re-grade result.

---

## Hardness calibration

Measured against the four pre-registered predictions in `_aux/Hardness_Plan.md`. Opus only; the Gemini-selective prediction is untested.

| # | Prediction | Outcome |
|---|---|---|
| 1 | **[HIGH]** Both models report the QC side complete-and-clean, never reading the Linear `state` column | **CONFIRMED at the criterion level, OVER-PREDICTED at the conclusion level.** The state column was skipped as designed: criteria 20 (6/6 fail), 24 (6/6), 21 (5/6), 32 (3/6). But no run concluded the push was closeable. Criteria 49, 50, 54 and 60 passed 6/6. The agents reached the correct headline verdict through Jaime's own May 23 field note rather than through the state column. |
| 2 | **[HIGH]** Gemini names the open items but never issues the retraction | **UNTESTED** (no Gemini verifier output). The Opus side of the prediction held exactly: criteria 49 and 50 passed 6/6, matching the predicted near-0% Opus failure. |
| 3 | **[MED]** Runs miss the South no-access unit and the unfinished filter run, both living in thread replies | **SPLIT, and the stated mechanism is wrong.** South no-access: OVER-predicted, found by 5/6 runs (criteria 29, 38, 39 all 5/6 pass). Filter run: CONFIRMED and stronger than predicted, 6/6 fail on criteria 7 to 10. See the mechanism correction below. |
| 4 | **[MED]** Runs overlook that Jaime's QC coverage never included West | **PARTIALLY CONFIRMED, weaker than predicted.** Four of six runs surfaced the West gap in narrative (criteria 33, 44, 52 each 4/6 pass); only two raised the tracking item (criteria 3, 4, 6 each 2/6 pass). The gap is discoverable; acting on it is what discriminates. |

**Stump hypothesis hit rate: 2 confirmed / 1 split / 1 untested out of 4.**

### Mechanism correction — Lever 5 (thread-reply blindness) is inert on StarPM

**Zero of 12 runs across both models called `slack_read_thread`.** Yet the reply content the lever depends on was in every run's context: `slack_read_channel(channel_id="C001", limit=100)` returns thread replies inline as flat messages. Brooke Phillips's stock-count ask at ts `1779569323.000012` and John Smith's parent post at ts `1779567943.000011` both appear in the first channel-read result of all 12 runs, as do the South-cluster reschedule replies at ts `1779308444.000003`.

The filter-run miss is therefore a **reasoning** failure, not a **retrieval** failure. The agents read "the supply closet is almost out of 20x25 filters so we'll need a restock before I can finish the run" and then, in five of six runs, closed the portfolio filter spot-check as a clean pass anyway. That is a stronger and more defensible stump than the one the plan designed, but it is not the mechanism the plan credited.

**Consequence for future StarPM builds:** do not budget tool calls for `slack_read_thread` and do not select Lever 5 as an independent lever on this universe. The two-to-four calls the density projection assigned to it never happen.

### Under-predicted lever — near-miss entity pairs are a difficulty lever, not flavor

The Hardness Plan demoted Lever 6 (near-miss entity confusion) to *"flavor, not a difficulty lever, carried but not counted"*. It produced two of the three strongest discriminators in the set:

- **The two North pairs.** Jaime's two units flagged May 23 as deficient versus OPS-56's two units pending tenant access. Every run collapsed them into one pair. Criterion 13 failed 6/6, criterion 31 failed 4/6, criterion 41 failed 4/6.
- **OPS-99 versus OPS-108.** Identical title, opposing states. Criterion 20 failed 6/6; three runs retrieved both, called them duplicates, and never compared the states.

The shape that works is a same-cluster, same-count, same-noun pair whose members differ only in *why* they are open. That is worth promoting to a first-class lever.

### Lever re-attribution against the pre-registered rule

The plan pre-registered: *"if runs surface the West-coverage gap but not the state contradiction, Lever 1 fired and Lever 2 did not."* Four of six runs surfaced the West gap and none fully surfaced the state contradiction, so **Lever 1 (latching) fired and Lever 2 (structured-DB skip) fired only on the granular records, not on the headline.** Lever 8 (multi-link chain off Jaime's field note) carried the conclusion and was stronger than its 7.5 projected cost implied.

---

## Action items

1. **Save `8b_Verifier_Fails_Gemini.txt` and re-invoke S4** in a fresh chat. The Gemini classification loop, the Gemini pass@1 gate and stump prediction 2 all depend on it. This is the only thing blocking phase closure.
2. **Apply the three Bucket 1 fixes** to `7_Rubrics.json` (criteria 11, 15, 51) per `S4_fixes.md`, and append the one mirroring sentence to OE 31 in `6_Oracle_Events.txt` so OE 28 and OE 31 stop disagreeing on the South-unit routing. Set stays at 60.
3. **Ship the seven AF justifications** in `S4_AF_justifications.md` to the platform. Voice gate clean (`check_justification.py` exit 0).
4. **Appeal criterion 58** on runs 1, 4 and 6 if the platform supports per-run appeals. Optional hardening: append `(or similar)` to its title.
5. **No REDO.** Both trajectory gates pass on both models. pass@1 0.0% against a 40% ceiling and density 62.5 / 79.8 against a 40 floor. The task is neither too easy nor too thin.
