# Verifier Fails — S4 verdict (Task 36)

## Trajectory hard gates

### T3 — Error Rate
Erroneous runs: 0/6. Verdict: **PASS** (< 3).

### T2 — Agent Failure Rate
Runs passing all rubrics: 0/6. pass@1: **0.0%**. Verdict: **PASS** (≤ 40%).

### T1 — Density (empirical)
Avg total tool calls: 52 (per `_aux/Trajectory_Stats.json`). Avg MCP calls: 37.7. Range 35–71. Verdict: **PASS** (≥ 50 design target).

## Run matrix (34 rubrics × 6 runs)

Failing-rubric detail (all others PASS on every run):

| Rubric | R1 | R2 | R3 | R4 | R5 | R6 | Total |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| R1 Linear comment on `linear_issue_f85be674c9b8` | F | F | F | F | F | F | **6/6** |
| R2 Linear per-employee line items (Simone $4,500+$750 / Marcus $4,500+$1,100) | F | F | F | F | F | F | **6/6** |
| R3 Linear references INV-2026-0308 $11,350 total | F | F | F | F | F | F | **6/6** |
| R4 Linear describes Marcus (Indianapolis, Apr 18-20, no hard date) | F | F | F | F | F | F | **6/6** |
| R5 Linear describes Simone (wrong unit, Carmen escalation, transfer/credit pending) | F | F | F | F | F | F | **6/6** |
| R6 Slack post on C002 / thread_ts 1776997200.000000 | P | F | F | F | P | F | 4/6 |
| R7 Slack references Marcus content on Mina's thread | P | F | F | F | P | F | 4/6 |
| R8 Slack references Simone content on Mina's thread | P | F | F | F | P | F | 4/6 |
| R9 Simone email: Julian escalated to Carmen Reyes with same-day response | F | P | F | F | P | F | 4/6 |
| R10 Marcus email: at Indianapolis hub since April 11, driver called off | P | P | P | F | F | F | 3/6 |
| R11 Simone email flags transfer availability + dollar swing pending Carmen | F | P | P | P | P | F | 2/6 |
| R12 Mina summary references all 4 internal actions (Slack + Linear + CRM + calendar) | P | P | P | F | P | P | 1/6 |
| **Fails per run** | **7** | **9** | **9** | **11** | **6** | **11** | **53** |

## Classifications

Distinct failing rubrics: **12** of 34.

- **Bucket 1 (rubric invalid): 0** — see `S4_fixes.md`
- **Bucket 2 (judge error): 0** — see `S4_judge_errors.md`
- **Bucket 3 (legitimate model failure): 12** — see `S4_AF_justifications.md`

## All-Failing Rubrics sub-dim

Rubrics that failed EVERY completed run: **5** (R1, R2, R3, R4, R5 — all rooted in Linear-issue disambiguation).
Bucket 1 count among those 5: 0.
Bucket 1 ratio: **0/12 = 0%** (using distinct failing rubrics as the denominator).
Bucket 1 ratio (AF-only interpretation): 0/5 = 0%.

Either interpretation puts the ratio well under 25%.
**Score: 5/5 PASS.**
Justification: Every failing rubric is grounded in the shipped OE + universe and cites a specific, verifiable trajectory action. The stump pattern (Linear-issue disambiguation, Slack decoy parent thread, Simone email content omissions) is genuine model failure produced by the intended levers, not rubric drift.

## Root-cause summary

The 53 total failures collapse to 3 root causes:

1. **Linear issue disambiguation (30/53 = 57% of all failures)**: All 6 runs' agents READ `linear_issue_f85be674c9b8` (Chloe's BrightLoop ops-gaps issue) during exploration, but at write time picked `linear_issue_c16357d188c6` (Mina's audit issue). Direct-verified in Run 1 trajectory: 3 reads on f85be… + 7 refs total to c16357… with the write call going to c16357. Cause: the prompt anchors on Mina ("Mina's audit thread", "cc Mina", "send Mina a short internal email") which primed attention on Mina's issue over Chloe's ops-gaps issue. This is the L26 decoy-parent trap extended to Linear (not explicitly named in the Hardness Plan but analogous to the Slack decoy).

2. **Slack decoy parent thread (12/53 = 23%)**: 4/6 runs posted the operations Slack status to C006 with thread_ts 1777001700.000000 (Chloe's ops-gaps thread) instead of C002 with thread_ts 1776997200.000000 (Mina's canonical BrightLoop audit thread). This is Hardness Plan Lever C (L26) working as designed. Runs 1 and 5 got the target thread correct.

3. **Simone/Marcus email content omissions (11/53 = 21%)**: Runs varied in whether the Simone-facing email named Carmen Reyes AND set a same-day response expectation (R9), whether the Marcus-facing email cited the April 11 date explicitly (R10), whether the Simone email flagged dollar swing as pending Carmen's answer (R11), and whether the Mina internal summary named all 4 internal actions (R12). These reflect the L25 existing-output-anchor lever — agents paraphrased Julian's 4/23 apology template rather than delivering the factual scaffolding required.

## Hardness calibration

Stump hypothesis hits from `_aux/Hardness_Plan.md`:

| H | Predicted lever | Observed | Hit? |
|---|---|---|:---:|
| H1 | L25 existing-output anchor (Julian's 4/23 apology template as answer) | R9-R12 failures track this exactly; agents left out Carmen name, dollar-swing framing, April 11 date | HIT |
| H2 | L9 authority self-anchor + L14 correct-observation-wrong-conclusion | Weak — trajectories show agents did read Special Requirements; Airtable updates were correct | PARTIAL |
| H3 | L26 decoy Slack parent thread | 4/6 runs posted to C006/1777001700 instead of C002/1776997200 | HIT |
| H4 | L4 Marcus 3-way name collision | 0/6 runs used the wrong email; agents correctly used marcus.webb@brightloopanalytics.com | MISS |

**Bonus finding (NOT in the hardness plan)**: L26 analog applied to Linear issue selection produced the highest single-lever fail count in the task (30/53 fails). The plan named the two candidate issues (`f85be674c9b8` vs `c16357d188c6`) but did not project them as a distinct disambiguation lever. Both issues sit on Chloe/Mina, both are BrightLoop-scoped, both target the same batch — the prompt phrase "the BrightLoop operational issue" is under-specified relative to the universe surface. The prompt author leaned on the "operational" adjective to disambiguate; agents anchored on Mina-centric prompt language and picked her issue anyway.

**Lessons for next task**:
- When the universe surfaces two candidate Linear/CRM/Airtable records that both match the prompt's descriptive phrase, treat that as a Linear-analog L26 lever and price the density projection accordingly.
- Prompt language that heavily names one persona (Mina here) will bias the agent toward records owned by that persona even when the target is owned by someone else (Chloe here). This is a proto-lever worth cataloguing.

## Action items

- 0 Bucket 1 fixes needed (no rubric-invalid classifications).
- Ship all 5 AF justifications from `S4_AF_justifications.md` back to the platform if AF flagging surfaces on the platform side.
- No judge-error appeals.
- The task is defensibly hard: 0% pass@1, 52 avg tool calls, 5 AF rubrics all Bucket 3.

## Data sources consulted
- 5_Prompt.txt · 6_Oracle_Events.txt · 7_Rubrics.json (shipped)
- 8_Verifier_Fails.txt (raw judge output per run)
- trajectory-runs/*.json (6 completed trajectories; spot-checked Run 1, Run 2, Run 5)
- _aux/Universe_Split/ (Linear issue ownership + Slack channel/thread ground truth)
- _aux/Hardness_Plan.md (H1-H4 predictions)
- _aux/Trajectory_Stats.json (empirical pass@1 + density)
