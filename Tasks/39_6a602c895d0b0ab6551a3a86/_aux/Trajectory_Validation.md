# Trajectory Validation — 39_6a602c895d0b0ab6551a3a86

Universe: StarPM V4 | Date: 2026-07-23 (re-review)

> Full trajectory matrix for the current batch. See `_aux/Council_Reports/S4_verdict.md` for bucket assignments and `_aux/Council_Reports/S4_AF_justifications.md` for the AF batch.

## Rubric numbering

Full rubric text lives in `7_Rubrics.json`; 32 rubrics total. Only failing rubrics itemized below; R1-R19, R21-R23, R25-R27 pass 12/12 across both models.

## Opus (`Agent_Responses/Opus/Run{1..6}_Trajectory.json`)

| # | Rubric (truncated) | R1 | R2 | R3 | R4 | R5 | R6 | AF? |
|---|---|---|---|---|---|---|---|---|
| 20 | Gmail draft threads under Brooke 6/18 (replyToMessageId d0e6f2c5b4a70b19) | F | F | F | F | F | F | YES |
| 24 | Slack post threaded under Brooke 6/18 (thread_ts 1781788320.000202) | F | F | F | F | F | F | YES |
| 28 | Calendar event on jaime.salinas@starpm.com's calendar | F | F | F | F | F | F | YES |
| 29 | Calendar reminder Friday 2026-07-03 07:00-11:00 CT | P | F | F | P | F | F | No |
| 30 | Calendar summary references Las Vistas 3C | P | F | F | P | F | F | No |
| 31 | Calendar summary references refrigerator interior | P | F | F | P | F | F | No |
| 32 | Calendar summary references oven interior | P | F | F | P | F | F | No |

**Opus per-run outcome:** R1 = 29/32, R2 = 25/32, R3 = 25/32, R4 = 29/32, R5 = 25/32, R6 = 25/32. **pass@1 = 0/6 = 0.0%**.

## Gemini (`Agent_Responses/Gemini/Run{1..6}_Trajectory.json`)

| # | Rubric (truncated) | R1 | R2 | R3 | R4 | R5 | R6 | AF? |
|---|---|---|---|---|---|---|---|---|
| 20 | Gmail draft threads under Brooke 6/18 | F | P | F | P | P | P | No |
| 24 | Slack post threaded under Brooke 6/18 | F | F | F | F | F | F | YES |

**Gemini per-run outcome:** R1 = 30/32, R2 = 31/32, R3 = 30/32, R4 = 31/32, R5 = 31/32, R6 = 31/32. **pass@1 = 0/6 = 0.0%** [informational only per July 2026 Gemini-not-gated rule].

## Model Divergence Summary

| # | Rubric | Opus pass rate | Gemini pass rate | Divergence | Note |
|---|---|---|---|---|---|
| 20 | Gmail thread | 0/6 (0%) | 4/6 (67%) | MODEL_DIVERGENCE (67pp) | Gemini locates Brooke's canonical closeout message (d0e6f2c5b4a70b19) via gmail_search_threads and passes it as replyToMessageId on 4/6 runs. Opus never does. Rubric proven achievable by Gemini → Bucket 3 for Opus. |
| 24 | Slack thread | 0/6 (0%) | 0/6 (0%) | NONE | AF both models 12/12. Both frontier models see Brooke's ts 1781788320.000202 in slack_search output but do not propagate it as thread_ts on the send call. Interpretation of "drop the closeout note here" as channel-post-not-thread-reply is a systematic Opus 4.8 + Gemini failure mode. Designed hardness lever L26 landed at 100% failure. |
| 28 | Calendar (calendarId) | 0/6 (0%) | 6/6 (100%) | MODEL_DIVERGENCE (100pp) | On Opus R1/R4 and Gemini R1/R4, both models called create_event without an explicit calendarId parameter — identical tool-call shape. Gemini judge PASSED (correct: session operating as Jaime → primary calendar defaults to jaime.salinas@starpm.com). Opus judge FAILED for missing calendarId. Judge inconsistency = Bucket 2 for Opus R1/R4. Opus R2/R3/R5/R6 used CronCreate (wrong tool family) = Bucket 3. |
| 29-32 | Calendar details | 2/6 (33%) | 6/6 (100%) | MODEL_DIVERGENCE (67pp) | Opus R2/R3/R5/R6 cascade-fail 29-32 because CronCreate produced no calendar event to inspect. Not intrinsic rubric issues → Bucket 3 cascade. |

## Combined AF List

- **Rubric 20** (Gmail thread — AF Opus 0/6): Bucket 3 for Opus (Gemini's 4/6 pass rate proves rubric achievable).
- **Rubric 24** (Slack thread — AF both models 0/12): Bucket 3 both models (designed hardness lever L26, thread_ts extraction failure is a genuine capability gap in both frontier models).
- **Rubric 28** (Calendar on Jaime's calendar — AF Opus 0/6): Mixed — Bucket 2 for Opus R1/R4 (judge inconsistency with Gemini) + Bucket 3 for Opus R2/R3/R5/R6 (CronCreate wrong-tool-family selection).

**Bucket 1 count = 0. Bucket 2 count = 2 (Opus R28 R1+R4). Bucket 3 count = 41.**
**All-Failing Rubrics sub-dim: 0/3 = 0% Bucket 1 → 5/5 PASS.**
