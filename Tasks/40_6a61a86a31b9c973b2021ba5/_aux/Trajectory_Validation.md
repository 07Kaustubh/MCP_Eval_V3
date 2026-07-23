# Trajectory Validation — Task 40 (StarPM V4)

Full 6-run × 49-rubric matrix per model, derived from independent trajectory reads cross-checked against the verifier output.

## Opus (Agent_Responses/Opus/Run{1..6}_Trajectory.json)

Only rubrics with at least one Fail shown; all other rubrics = Pass across all 6 runs.

| # | Rubric (short) | R1 | R2 | R3 | R4 | R5 | R6 | Fail rate | AF? |
|---|---|---|---|---|---|---|---|---|---|
| 4 | Airtable desc: tenant without hot water | F | P | P | P | P | P | 1/6 | No |
| 5 | Airtable desc: active leak w/ occupants at home | F | P | P | P | P | P | 1/6 | No |
| 9 | Linear OPS-231 update called | P | P | F | P | P | P | 1/6 | No |
| 10 | Linear desc: full unit replacement scope | P | P | F | F | P | P | 2/6 | No |
| 11 | Linear desc: ~$1,850 | P | P | F | F | P | P | 2/6 | No |
| 12 | Linear desc: Thursday install retained | P | P | F | F | P | P | 2/6 | No |
| 20 | Linear comment: tenant without hot water | F | P | P | P | P | P | 1/6 | No |
| 21 | Linear comment: active pooling w/ occupants at home | F | P | P | P | P | P | 1/6 | No |
| 23 | Slack post send (thread_ts 1782824160.000302) | F | F | F | F | F | F | **6/6** | **YES** |
| 24 | Slack: corrected scope | F | F | F | F | F | F | **6/6** | **YES** |
| 25 | Slack: escalation to High | F | F | F | F | F | F | **6/6** | **YES** |
| 26 | Slack: Thursday slot kept | F | F | F | F | F | F | **6/6** | **YES** |
| 47 | Robert draft: Ruud RS75 | F | P | P | P | P | F | 2/6 | No |

**Opus per-run pass totals:** R1 40/49 · R2 45/49 · R3 41/49 · R4 42/49 · R5 45/49 · R6 44/49

## Gemini (Agent_Responses/Gemini/Run{1..6}_Trajectory.json)

| # | Rubric (short) | R1 | R2 | R3 | R4 | R5 | R6 | Fail rate | AF? |
|---|---|---|---|---|---|---|---|---|---|
| 2 | Airtable fldPriority = selHigh | P | P | P | F | P | P | 1/6 | No |
| 5 | Airtable desc: active leak w/ occupants at home | F | F | F | F | F | F | **6/6** | **YES** |
| 9 | Linear OPS-231 update called | P | P | P | F | P | F | 2/6 | No |
| 10 | Linear desc: full unit replacement scope | P | P | P | F | P | F | 2/6 | No |
| 11 | Linear desc: ~$1,850 | P | P | P | F | P | F | 2/6 | No |
| 12 | Linear desc: Thursday install retained | P | P | P | F | P | F | 2/6 | No |
| 21 | Linear comment: active pooling w/ occupants at home | F | F | F | P | F | P | 3/6? / 4/6? | No (partial only) |
| 39 | Robert draft: initial ~$310 quote | P | P | P | F | P | P | 1/6 | No |

**Gemini per-run pass totals:** R1 47/49 · R2 46/49 · R3 48/49 · R4 42/49 · R5 48/49 · R6 44/49

## Model Divergence Summary

| # | Rubric | Opus fail rate | Gemini fail rate | Divergence? | Note |
|---|---|---|---|---|---|
| 5 | Airtable desc: active leak w/ occupants | 1/6 (17%) | 6/6 (100%) | **MAJOR** | Gemini systematically omits "occupants at home" atom; Opus consistently includes it (except thin Run 1 desc) |
| 21 | Linear comment: active pooling w/ occupants | 1/6 (17%) | 3–4/6 (~50–67%) | **MODEL_DIVERGENCE** | Same atom-drop pattern as R5; Gemini generation style deprioritizes secondary safety atoms |
| 23-26 | Slack #maintenance post cluster | 6/6 (100%) | 0/6 (0%) | **MAJOR** | Opus fully misses; Gemini fully lands. Reverse of the R5/R21 pattern. Points to Opus getting stuck on thread-anchor selection: Run 4 posts top-level (no thread_ts), Run 6 posts to WRONG thread ts (evening-reply ts 1782863220.000303 instead of parent-tenant-relay ts 1782824160.000302). Other 4 runs skip the post entirely — Run 1 verbatim: "One thing I did not do: post in #maintenance to Tony." |
| 9–12 | Linear OPS-231 update + desc content | 1–2/6 | 2/6 | MINOR | Both models occasionally skip the Linear write; failure cascades to desc-content rubrics R10/R11/R12 |
| 47 | Robert draft: Ruud RS75 | 2/6 | 0/6 | MINOR | Opus occasionally drops the "RS75" model suffix from the owner draft, writing "12-year-old Ruud heater" instead. Gemini consistently includes RS75. |
| 2 | Airtable fldPriority = selHigh | 0/6 | 1/6 | MINOR | Gemini Run 4 miss (also skipped save_issue in R4); single-outlier |
| 39 | Robert draft: initial $310 | 0/6 | 1/6 | MINOR | Gemini Run 4 miss (same Run 4 pattern of thinner outputs) |

## Combined AF list (rubrics failing 6/6 on either model)

| # | Rubric | Model(s) | Classification |
|---|---|---|---|
| 5 | Airtable desc: active leak w/ occupants at home | Gemini AF | Bucket 3 (Gemini systematically drops occupants atom) |
| 23 | Slack post send to #maintenance thread | Opus AF | Bucket 3 (L9+L8 authority-dismissal + wrong-thread-anchor stump) |
| 24 | Slack: corrected scope | Opus AF | Bucket 3 (cascade from R23 — no valid post) |
| 25 | Slack: escalation to High | Opus AF | Bucket 3 (cascade from R23) |
| 26 | Slack: Thursday slot kept | Opus AF | Bucket 3 (cascade from R23) |

**No rubric is AF for BOTH models.** The cross-model divergence is itself informative: the two models have different failure modes, both real, on this scenario. That's a good sign for the task — it's discriminating on multiple axes rather than a single narrow one.

## Interpretation rules applied
- **AF Opus only (R23–R26):** legitimate Opus-specific stump. Trajectory walked — Runs 1/2/3/5 skip the post entirely; Runs 4/6 attempt but with wrong thread anchor. Both mechanisms are real reasoning failures, not judge errors.
- **AF Gemini only (R5):** Gemini genuinely omits the safety atom. Rubric bundling is a mild refinement suggestion but the atom itself is prompt-derived and required.
- **Partial fails both models (R9–R12):** consistent partial pattern from runs that skip the Linear write. Bucket 3 for the runs that fail.
- **No rubric fails 6/6 on both models.** No cross-model AF cluster; nothing suggests a task-wide rubric defect.

This table is the foundation for all bucket classifications in `S4_AF_justifications.md` / `S4_fixes.md` / `S4_judge_errors.md`.
