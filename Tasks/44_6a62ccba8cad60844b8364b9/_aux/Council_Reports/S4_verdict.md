# Verifier Fails: S4 verdict (dual-model, pass 4)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Criteria set:** 60 · **Models verified:** Opus 4.8 (6 runs, complete) + Gemini (6 runs, complete)

> **Supersedes** `_superseded/pass3_2026-07-26_1342/S4_verdict.md`. Prior passes are retained under `_superseded/`.

---

## Input reconciliation (read this first)

Two inputs changed since the pass-3 verdict, and both matter.

**1. The rubric file was edited at 14:42, after the pass-3 verdict was written at 13:42.** Thirteen of the 60
criteria changed: eight titles and eleven evidence fields, with three justifications. Every edit widened an
accept-set. Titles were generalised from "tracking item" to "tracking work" or reworded to drop a required
record identifier; evidence fields were extended to name additional acceptable destinations (a comment on an
existing open record, the maintenance ticket, any deliverable, any correct reason). The set stayed at 60,
inside the 60-criterion ceiling. Criteria affected: the West cluster dated-status statement, all four filter
run criteria, both plumbing criteria, both East duplicate-record criteria, the note on OPS-98, the tenant
access North-units criterion, and the two North access-hold criteria.

**2. Both verifier files were re-exported at 16:18 and 16:19.** The trajectories on disk are **unchanged**;
`parse_trajectories.py` reproduces identical per-run tool-call counts to the unit, and per-model density is
bit-identical to pass 3. What changed is the grading.

| | Opus per-run | Gemini per-run |
|---|---|---|
| Pass 3 grading | 34 · 33 · 44 · 26 · 30 · 46 | 20 · 19 · 22 · 19 · 20 · 21 |
| Pass 4 grading (current) | **28 · 33 · 43 · 31 · 32 · 37** | **20 · 19 · 22 · 17 · 16 · 18** |

All 60 criterion titles in both files match `7_Rubrics.json` exactly across all 12 run blocks (**720 of 720
decisions matched by title, 0 unmatched rows, 0 duplicate titles**), so both files grade the current set.

### Grader variance reproduces, and this time it runs against the agent

**74 of 720 decision cells (10.3%) changed between the two gradings.** Only 12 of those fall on the 13
criteria whose text was edited. The other **62 (8.6% of all cells)** are decision changes on text that did
not change by a character.

- 46 cells moved Pass to Fail, 28 moved Fail to Pass. Pass 3 skewed the other way (42 to Pass, 25 to Fail).
- Opus lost ground on net: 41 of the 74 moved cells are Opus, and the best Opus run fell from 46 to 43.
- Pass 3 measured 9.3% cell movement on unchanged text. Pass 4 measures 8.6%. Two independent regradings of
  byte-identical trajectories now agree that roughly one cell in twelve is not reproducible.

**What this does and does not change.** It does not move the task verdict. Both gradings give pass@1 = 0/6 on
both models, both give 0 error runs, and density is a trajectory property that grading cannot touch. All three
hard gates pass under either export. What it changes is the confidence attachable to any single run-cell, and
it is the reason the contested-cell list is scoped to cells where the artifact text contradicts the judge's
stated reason rather than to every cell that looks harsh.

---

## Trajectory gates

### T3 - Error Rate
Erroneous runs: **0/6 Opus**, **0/6 Gemini** (12/12 parsed `ok`). Verdict: **PASS (< 3)** on both models.

### T2 - Agent Failure Rate (pass@1 <= 40%)

| Model | Per-run criteria passed | Runs passing all criteria | pass@1 | Verdict |
|---|---|---|---|---|
| Opus 4.8 | 28 · 33 · 43 · 31 · 32 · 37 of 60 | 0/6 | **0.0%** | **PASS** |
| Gemini | 20 · 19 · 22 · 17 · 16 · 18 of 60 | 0/6 | **0.0%** | **PASS** |

The best Opus run leaves 17 criteria failing; the best Gemini run leaves 38. Neither model comes close to
sweeping, and the margin is far wider than the grader variance could bridge.

### T1 - Density (V4 target 40+ average per model)

| Model | Runs | Avg total calls | Avg MCP-only | Range (total) | Verdict |
|---|---|---|---|---|---|
| Opus 4.8 | 6 | **62.5** | 44.7 | 52 - 79 | **PASS** |
| Gemini | 6 | **79.8** | 67.0 | 60 - 91 | **PASS** |

Both models clear 40+ on both measures, and every individual run clears it on totals. Unchanged from pass 3,
as expected for unchanged trajectories.

---

## Run matrix (both models)

`F` = fail, `.` = pass. `B` = bucket: `1` rubric invalid, `2` judge error, `3` legitimate model failure, `-`
no failures on either model. `AF` = all-failing on `O`pus and/or `G`emini. `ct` = contested cells on that
criterion.

> This matrix records the **16:18 / 16:19 grading against the pre-fix rubric text**, which is the grading of
> record. Rows **6, 33, 58 and 59** were subsequently edited (see `S4_fixes.md`); their patterns here are
> historical and the projected post-fix patterns are tabulated after the classifications.

| # | Opus 1-6 | Gem 1-6 | oF | gF | B | AF | ct | criterion |
|---|---|---|---|---|---|---|---|---|
| 1 | `......` | `......` | 0 | 0 | - | - | | New maintenance ticket for field work needing a tech onsite |
| 2 | `......` | `FFFFFF` | 0 | 6 | 3 | G | | Ticket describes the two North units flagged May 23 |
| 3 | `FF.FF.` | `.F.FFF` | 4 | 4 | 3 | - | | West cluster QC coverage-gap tracking item raised |
| 4 | `FF.FF.` | `FFFFFF` | 4 | 6 | 3 | G | | West item states PM work never covered by a QC spot-check |
| 5 | `FFFFF.` | `FFFFFF` | 5 | 6 | 3 | G | | West item states latest dated status records work underway |
| 6 | `FF.FF.` | `......` | 4 | 0 | **1** | - | | West coverage item names owner (Lisa / John / Brooke) [FIXED: unbound, see B1-3] |
| 7 | `FFF.FF` | `FFFFFF` | 5 | 6 | 3 | G | | Filter run tracking work raised on Operations board |
| 8 | `FFF.FF` | `FFFFFF` | 5 | 6 | 3 | G | | Filter work states John Smith's May 23 20x25 shortage |
| 9 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | O+G | | Filter work records Brooke's outstanding stock-count request |
| 10 | `FFF.FF` | `FFFFFF` | 5 | 6 | 3 | G | | Filter work names owner (John / Elias / Brooke) |
| 11 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | G | | Tracking work or ticket for units awaiting tenant access |
| 12 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | G | | Covers the South unit never serviced (tenant not home) |
| 13 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | O+G | | Covers the two North units OPS-56 holds on scheduling |
| 14 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | G | | Access work names owner (Carlos / Elias / Tony) |
| 15 | `......` | `......` | 0 | 0 | - | - | | Tracking work or ticket for open plumbing findings |
| 16 | `......` | `......` | 0 | 0 | - | - | | Records the two water heaters needing replacement |
| 17 | `......` | `......` | 0 | 0 | - | - | | Records the hose bibs needing repair |
| 18 | `....F.` | `FFFFFF` | 1 | 6 | 3 | G | | Plumbing work states the budget-priority escalation |
| 19 | `F.....` | `......` | 1 | 0 | 3 | - | | Plumbing work names owner (Carlos / Brooke) |
| 20 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | O+G | | Records OPS-99 / OPS-108 same title, two different states |
| 21 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | O+G | | Records neither East QC record is in a completed state |
| 22 | `...F..` | `FFFFFF` | 1 | 6 | 3 | G | 1 | Note on OPS-87: does not stand as a South/North close-out |
| 23 | `FFF.FF` | `FFFFFF` | 5 | 6 | 3 | G | | Note on OPS-96: filter spot-check does not stand (restock) |
| 24 | `.F..F.` | `FFFFFF` | 2 | 6 | 3 | G | | Note on OPS-98: QC did not land where the record claims |
| 25 | `......` | `......` | 0 | 0 | - | - | | Re-inspection slot on Jaime's calendar, on/after July 1 |
| 26 | `......` | `......` | 0 | 0 | - | - | | Slot describes re-inspecting the outstanding follow-up |
| 27 | `......` | `......` | 0 | 0 | - | - | | Status posted in #maintenance (C001) |
| 28 | `......` | `.F.FFF` | 0 | 4 | 3 | - | 1 | Post states end-of-June target passed with work open |
| 29 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | G | | Post states the South unit never serviced (tenant not home) |
| 30 | `......` | `FFFFFF` | 0 | 6 | 3 | G | | Post states the two May 23 North units still need HVAC |
| 31 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | O+G | | Post states the North access follow-up is still open |
| 32 | `..FFFF` | `FFFFFF` | 4 | 6 | 3 | G | 1 | Post states the East QC record is not in a completed state |
| 33 | `.F.FF.` | `FFFFFF` | 3 | 6 | 3 | G | | Post tells the crew West had no QC spot-check coverage [HARDENED, no decision change] |
| 34 | `.F.FF.` | `F.FFFF` | 3 | 5 | 3 | - | | Post states latest dated West status records work underway |
| 35 | `.FF.F.` | `.FFFFF` | 3 | 5 | 3 | - | | Post states the filter run left unfinished after the block |
| 36 | `......` | `...FF.` | 0 | 2 | 3 | - | 2 | Post states plumbing findings incl. water heaters still open |
| 37 | `......` | `......` | 0 | 0 | - | - | | Draft to brooke.phillips@starpm.com on the close-out |
| 38 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | G | | Draft states South open item is the unserviced unit |
| 39 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | G | | Draft states the missed unit must be re-scheduled |
| 40 | `......` | `FFFFFF` | 0 | 6 | 3 | G | | Draft states the two May 23 North units need a tech onsite |
| 41 | `FFFFFF` | `FFFFFF` | 6 | 6 | 3 | O+G | | Draft separately identifies the North access hold |
| 42 | `FF.FFF` | `FFFFFF` | 5 | 6 | 3 | G | | Draft states East QC unconfirmed on the record's state |
| 43 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | G | 2 | Draft states East QC must be confirmed before close |
| 44 | `.F.FF.` | `FF...F` | 3 | 3 | 3 | - | | Draft states no spot-check record covers West |
| 45 | `.F.FF.` | `FF...F` | 3 | 3 | 3 | - | 1 | Draft states West must be QC walked before close |
| 46 | `F....F` | `FFFFFF` | 2 | 6 | 3 | G | 1 | Draft names the tenant access holder (Carlos / Elias / Tony) |
| 47 | `.F..F.` | `......` | 2 | 0 | 3 | - | | Draft names the West holder (Lisa / John / Brooke) |
| 48 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | G | 2 | Draft names the East QC holder (Elias / Jaime / Brooke) |
| 49 | `......` | `......` | 0 | 0 | - | - | | Draft states plainly the earlier QC sign-off does not hold |
| 50 | `......` | `......` | 0 | 0 | - | - | | Draft states the push should not be treated as closeable |
| 51 | `FFF...` | `FFFFFF` | 3 | 6 | 3 | G | | Final: none of the three QC records was complete as found |
| 52 | `.F.FF.` | `FF.FFF` | 3 | 5 | 3 | - | | Final: QC coverage never included the West cluster |
| 53 | `F..F.F` | `FFFFFF` | 3 | 6 | 3 | G | | Final: South still has one unit never serviced |
| 54 | `......` | `FFFFFF` | 0 | 6 | 3 | G | | Final: the two May 23 North units still require HVAC |
| 55 | `F..F..` | `FFFFFF` | 2 | 6 | 3 | G | 1 | Final: East QC unconfirmed rather than complete |
| 56 | `F.....` | `....F.` | 1 | 1 | 3 | - | 2 | Final: plumbing findings incl. water heaters still open |
| 57 | `FFF.FF` | `.FFFFF` | 5 | 5 | 3 | - | | Final: portfolio filter run left unfinished |
| 58 | `FFF.FF` | `F..FF.` | 5 | 3 | **1** | - | 5 | Final: South electrical panel inspections finished [FIXED: attribution demand, see B1-1] |
| 59 | `FFFFFF` | `F..F..` | 6 | 2 | **1** | O | 3 | Final: East HVAC service work recorded as complete [FIXED: attribution demand, see B1-2] |
| 60 | `......` | `..F.F.` | 0 | 2 | 3 | - | | Final: push cannot be closed out as of July 1 |

**404 of 720 cells fail. 50 of 60 criteria fail at least one cell. 10 criteria are clean 12/12.**

---

## Classifications (post-fix)

- **Bucket 1 (rubric invalid): 3 criteria, all fixed in place.** See `S4_fixes.md`. Criteria 58 and 59 were Overly Specific: an attribution demand the evidence fields disclaimed, recurring on 5 and 3 cells. Criterion 6 was Overly Broad: unbound from the coverage item its sibling requires, passing 6/6 on Gemini while that sibling passed 2/6. The set stays at 60 criteria, 60 outcome / 0 process.
- **Bucket 2 (judge error): 0 criteria at criterion level, 14 contested run-cells recommended for appeal** (3.5% of 404 fail cells) across 10 criteria. See `S4_judge_errors.md`. The 7 cells originally filed against criteria 58 and 59 are withdrawn from the appeal set and absorbed by the Bucket 1 fixes.
- **Bucket 3 (legitimate model failure): 47 of the 50 failing criteria, 383 of 404 fail cells.** 34 criteria are all-failing on Gemini, 6 of those on both models. See `S4_AF_justifications.md`.

### All-Failing Rubrics sub-dim

| Base | Bucket 1 count | Total | Ratio |
|---|---|---|---|
| Criteria failing at least one cell | 3 | 50 | **6.0%** |
| Criteria all-failing on either model (post-fix) | 0 | 34 | **0.0%** |
| Criteria all-failing on both models | 0 | 6 | **0.0%** |
| Individual fail cells | 3 | 404 | **0.7%** |

Ratio is below 25% on every base. **All-Failing Rubrics sub-dim: 5/5 (PASS).** After the fixes, no criterion is
all-failing because of its own design: every one of the 34 remaining all-failing criteria traces to a genuine
reasoning failure, and the failures concentrate on the four open items the task was built around rather than
scattering across the set.

### Effect of the fixes on all-failing status

One criterion leaves the all-failing set. The East service-recorded criterion was graded 0/6 on Opus with 2 of 6
cells contested; under the corrected text it passes 2 of 6 on Opus and is no longer all-failing on either model.
**AF union falls from 35 to 34, and every remaining entry is a clean model failure with a justification.** No
Gemini all-failing criterion contained a contested cell, so all 34 stand unchanged.

### Projected re-grade of the edited criteria

Derived by hand from the trajectories, to be re-derived from the next platform export rather than carried
forward as fact.

| Criterion | Before | After | Fails that correctly remain |
|---|---|---|---|
| 58 South electrical finished | 8 fail cells | 3 | Opus 2 (no mention), Opus 3 ("only partially complete, stays open"), Opus 5 (North panel notes only) |
| 59 East service recorded complete | 8 fail cells | 5 | Opus 2 (carries East as unconfirmed), Opus 3 (no affirmative completion), Opus 4 and Gemini 4 (East omitted), Opus 5 ("Never completed") |
| 6 West coverage owner | 4 fail cells | 8 | Opus unchanged at 4; Gemini 2, 5, 6 (item concerns completion not QC coverage), Gemini 4 (no West item created) |
| 33 West coverage in channel post | 6 fail cells | 6 | unchanged, hardening only |

Net fail cells 404 to 400. Every legitimate fail was checked and none was flipped by a widening.

---

## Hardness calibration

Four predictions were pre-registered. The pass-4 grading reproduces the pass-3 calibration exactly, which is
expected because the trajectories are unchanged and the calibration is a property of agent behaviour rather
than of grading.

| # | Prediction | Outcome |
|---|---|---|
| 1 | **[HIGH]** Both models report the QC side as complete-and-clean because they never read the Linear state column | **CONFIRMED.** The two East duplicate-record criteria fail 0/12. The as-found-states criterion fails 0/6 on Gemini. The state column is the single highest-discrimination surface in the set. |
| 2 | **[HIGH]** Gemini names the open items but never issues the retraction | **FALSIFIED.** The two retraction criteria pass 12/12 again. Already corrected in the plan; the root cause is that the prompt's closing paragraph supplies both branches of the verdict in the persona's own words, which a 5/5 Unique Ground Truth score requires. |
| 3 | **[MED]** Runs miss the South no-access unit and the unfinished filter run, both resolving only in Slack thread replies | **CONFIRMED, asymmetric.** All four filter run criteria fail 0/6 on Gemini and 5 or 6 of 6 on Opus. The South no-access criteria fail 0/6 on Gemini and 3 of 6 on Opus. Thread-reply blindness is stronger than the 40% estimate on this surface. |
| 4 | **[MED]** Runs overlook that the QC coverage never included the West cluster | **CONFIRMED.** The West coverage criteria fail 0/6 on Gemini and 3 or 4 of 6 on Opus. Every Gemini run and three Opus runs raised a West item about unfinished field work rather than about the absent QC record. |

Hit rate: **3 of 4 confirmed, 1 falsified.** Unchanged from pass 3.

**Lever re-attribution, applied as pre-registered.** No run read the state column and still concluded the push
was closeable, so Lever 9 is not separately observable and Lever 2 carries the discrimination. Runs that
surfaced the West coverage gap without the state contradiction confirm Lever 1 fired independently of Lever 2.
Two Opus runs reached the open items with substantial Slack grounding and thin Linear resolution, which is
Lever 2 at close to maximum strength.

**New calibration note from this pass.** The 14:42 evidence widening is measurable and favourable. The note on
OPS-98 moved from 0/6 to 4/6 on Opus once the criterion accepted any correct reason, and the three filter run
criteria each gained their first Opus pass once a comment on an existing open record was accepted. Widening an
accept-set recovered real agent work without touching a single lever, which is the cheapest available fix when
a criterion is failing for the wrong reason.

---

## Action items

1. **Three rubric fixes applied in place** (criteria 6, 58, 59) plus a hardening on criterion 33 and the mandatory OE 29 mirror. Set stays at 60 criteria, 60 outcome / 0 process. Snapshots at `_aux/7_Rubrics.pre_qc5_fixes.json` and `_aux/6_Oracle_Events.pre_qc5_fixes.txt`. Validator PASS on prompt, oe, rubrics, all, submission_gate and injection.
2. **Submit the 34 AF justifications** in `S4_AF_justifications.md`. Voice gate clean, zero em-dashes.
3. **File 14 contested cells** from `S4_judge_errors.md` if the platform accepts per-cell appeals. Strongest: the OPS-87 comment the judge could not resolve from its internal id, the two Gemini run 5 draft cells where the East QC owner and close condition are stated verbatim, and the Gemini run 6 channel post whose first line is the criterion. Do not file the 7 cells on criteria 58 and 59; those are fixed at source.
4. **No REDO.** All three hard gates pass on both models with wide margins, and none of the edits touches a trajectory property.
5. **Re-derive per-cell counts from the next export.** These edits change rubric text after the 16:18 / 16:19 grading, so the current exports no longer grade the current set on criteria 6, 33, 58 and 59.
6. **Carry the grader-variance finding forward.** Two independent regradings of identical trajectories moved 9.3% and 8.6% of cells, in opposite net directions. Per-cell appeals on this task family are worth filing only where the artifact text is unambiguous.

## Verdict

**S4 pass 4 COMPLETE, fixes applied.** T1, T2 and T3 PASS on both models. Three Bucket 1 defects were found
and fixed in place, holding the set at 60 criteria. All-Failing Rubrics sub-dim **5/5** (Bucket 1 ratio 6.0%,
well inside the 25% band). AF union falls from 35 to 34 with the false all-fail removed, and every remaining
entry carries a justification. AF batch clean on the voice gate. No REDO.
