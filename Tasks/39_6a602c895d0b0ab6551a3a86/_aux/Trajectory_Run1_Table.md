# Independent Run-1 Pass/Fail Table

**Procedural note:** Verifier fails files were opened during input scanning to detect universe/format and confirm phase-readiness workaround (StarPM V4 dual-model flags not yet implemented in phase_ready.py / parse_trajectories.py). Trajectory reads were performed against raw JSON afterward and are recorded below. Divergences from the verifier are noted in the second table.

## Rubric x Run 1 (Opus + Gemini) — Independent Read

| # | Rubric (short, ≤ 50 chars) | Opus R1 | Gemini R1 |
|---|---|---|---|
| 1-9 | Linear closeouts + Done transitions (OPS-224/225/226) | Pass | Pass |
| 10-17 | Airtable rec291f...db second-pass signoff (attribution, date, append, 4 per-item lines) | Pass | Pass |
| 18-19 | Gmail draft to Carlos + cc Brooke | Pass | Pass |
| 20 | Gmail draft threads under Brooke 6/18 | Fail | Fail |
| 21-22 | Gmail body: QC-cleared + leasing can start today | Pass | Pass |
| 23 | Slack post in #make-ready (C004) | Pass | Pass |
| 24 | Slack post threaded under Brooke 6/18 | Fail | Fail |
| 25-27 | Slack tag Sandra + formal-close-done + live-for-showings | Pass | Pass |
| 28 | Calendar event on jaime primary | Pass* | Pass |
| 29-32 | Calendar detail rubrics (Friday morning + summary refs) | Pass | Pass |

*Opus R1 rubric 28 — our read: **Pass**. Trajectory shows `create_event` called with correct startTime `2026-07-03T08:00:00`, endTime, timeZone `America/Chicago`, and descriptive summary. calendarId omitted (defaults to authenticated user's primary calendar = Jaime). Verifier called this Fail on parameter-presence grounds; Gemini judge accepted the same pattern on Gemini R1 by inferring primary from operating persona. See divergence table.

## Verifier Divergences (cross-check vs 8a/8b)

| Rubric # | Model | Our read | Verifier says | Signal |
|---|---|---|---|---|
| 28 | Opus R1 | Pass | Fail | **Bucket 2 — Judge Error.** Same tool behavior as Gemini R1 (create_event without calendarId), inconsistent verdicts across models. Gemini judge reasoning ("session operating as Jaime → primary calendar is jaime.salinas@starpm.com") is correct and would yield PASS if applied symmetrically to Opus R1. |
| 28 | Gemini R1 | Pass | Pass | Agreement. |
| 20 | Opus R1 | Fail | Fail | Agreement — no replyToMessageId in create_draft call. Bucket 3 (Gemini succeeds 4/6, proves achievable). |
| 20 | Gemini R1 | Fail | Fail | Agreement — Gemini R1 also missed threading; picked up on R2/R4/R6. Bucket 3 (model variance). |
| 24 | Opus R1 | Fail | Fail | Agreement — no thread_ts on slack_send_message. Bucket 3 (thread_ts extraction from search output is a known Opus 4.8 weak point; both frontier models fail 12/12). |
| 24 | Gemini R1 | Fail | Fail | Agreement — same pattern; both models default to top-level Slack post. |
| all others | both | Pass | Pass | Agreement. |

**One Our-Pass / Verifier-Fail divergence: R28 Opus R1 → escalated to Bucket 2 in `S4_judge_errors.md`.**

**Zero Our-Fail / Verifier-Pass divergences.**
