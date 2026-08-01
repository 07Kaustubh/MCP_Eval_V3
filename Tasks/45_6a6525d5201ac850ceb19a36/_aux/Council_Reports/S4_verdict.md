# Verifier Fails — S4 verdict (Task 45, StarPM V4 dual-model)

**Date:** 2026-07-27 · **Universe:** starpm · **Framework:** V4 (Opus 4.8 + Gemini)
**Machine verdict (`parse_trajectories.py`):** `REBUILD_CANDIDATE_DIFFICULTY`
**S4 outcome: STOP at the T2 gate. This task is TOO EASY. Route to `PIPELINE REDO`.**

Inputs pinned (rule 15) before any reasoning; pin re-verified at exit.
- `8a_Verifier_Fails_Opus.txt`  sha `1526b9dbae6095e3…`  per-run passed [20,20,20,20,20,20]
- `8b_Verifier_Fails_Gemini.txt` sha `4bb5dc1d09b83fc7…`  per-run passed [18,14,20,15,20,20]
- `7_Rubrics.json`  sha `fa2912c664d0e2db…`  (20 criteria)

---

## Trajectory hard gates (Procedure 0.5 — run BEFORE classification)

### Trajectory T3 — Error Rate
Erroneous runs: 0/12 (6 Opus + 6 Gemini all parsed to a verifier-evaluable state). **Verdict: PASS (< 3).**

### Trajectory T2 — Agent Failure Rate (pass@1 <= 40%, PER MODEL for V4)
| Model | Runs passing ALL 20 rubrics | pass@1 | Verdict |
|---|---|---|---|
| **Opus 4.8** | **6/6** | **100%** | **FAIL** (the model under test solved every rubric on every run) |
| Gemini | 3/6 | 50% | FAIL (> 40%) |
| Overall | 9/12 | 75% | FAIL (> 40%) |

**Verdict: FAIL on both models.** Opus 4.8 is the model the entire hardness stack targets, and it passed 20/20 on all six runs. Per S4 Procedure 0.5 T2 and AGENTS.md rule 11, a difficulty FAIL is a hard STOP to `PIPELINE REDO`; S4 classification cannot rescue a too-easy task.

### Density (secondary, informational)
| Model | avg total tool calls | Band |
|---|---|---|
| Opus | 37.0 (min 28, max 49) | THIN — below the 40 design target, above the 15 QC floor |
| Gemini | 43.3 (min 34, max 51) | PASS — >= 40 design target |

Opus also lands sub-40 on the Hardness_Plan's own mandatory downstream mitigation #2 ("per-model average tool calls < 40 -> PIPELINE REDO"). Difficulty is the decisive failure; density THIN on Opus is a corroborating signal, not the trigger.

---

## Run matrix (per model)

| Rubric | Subject | Opus 1-6 | Gemini 1-6 |
|---|---|---|---|
| 1 | Airtable QC determination WRITE on recbd087 | PPPPPP | **F**·**F**·P·P·P·P |
| 2 | did not advance to Ready (anti-pattern absent) | PPPPPP | PPPPPP |
| 3 | determination on recbd087 states HOLD | PPPPPP | **F**·**F**·P·P·P·P |
| 4 | opens OPS tracking issue | PPPPPP | PPPPPP |
| 5 | issue: deep-clean $387 unpaid | PPPPPP | P·P·P·**F**·P·P |
| 6 | issue: interior-repaint $1,340 unpaid | PPPPPP | P·**F**·P·**F**·P·P |
| 7 | issue: In Progress + 6/30 past due | PPPPPP | P·**F**·P·P·P·P |
| 8 | issue: 7/15 re-inspection not occurred | PPPPPP | PPPPPP |
| 9 | posts in #make-ready C004 | PPPPPP | PPPPPP |
| 10 | #make-ready post states HOLD | PPPPPP | PPPPPP |
| 11 | drafts email to Carlos | PPPPPP | PPPPPP |
| 12 | email states HOLD / not signed off | PPPPPP | PPPPPP |
| 13 | email: deep-clean unpaid | PPPPPP | PPPPPP |
| 14 | email: interior-repaint unpaid | PPPPPP | PPPPPP |
| 15 | notifies Brooke | PPPPPP | PPPPPP |
| 16 | final: not marketing-ready / held | PPPPPP | PPPPPP |
| 17 | final: deep-clean $387 unpaid | PPPPPP | P·P·P·**F**·P·P |
| 18 | final: interior-repaint $1,340 unpaid | PPPPPP | P·**F**·P·**F**·P·P |
| 19 | final: In Progress + 6/30 past due | PPPPPP | P·**F**·P·**F**·P·P |
| 20 | final: 7/15 re-inspection not occurred | PPPPPP | PPPPPP |

**Opus: 0 fails anywhere. Gemini: 8 distinct criteria fail, none all-failing (max 2/6).**

## Classifications
- **Bucket 1 (rubric invalid): 0.** No rubric mis-graded; criterion-dependency audit exit 0; anti-pattern scan exit 0.
- **Bucket 2 (judge error): 0.** Every grading is defensible on the cited trajectory.
- **Bucket 3 (legitimate AF): 0.** There are NO all-failing rubrics. The Gemini fails are inconsistent (1-2 of 6) and model-specific, not engineered difficulty.
- **All-Failing Rubrics sub-dim:** trivially 5/5 (empty AF set) — but this is not a pass signal; the task fails the upstream T2 difficulty gate, which is dispositive.

No AF justifications authored (Bucket 3 empty) — justification voice gate correctly skipped.

---

## Root cause — the prompt hands the agent the answer

The task is too easy because `5_Prompt.txt` explicitly names every discriminator the rubric set tests, so there is near-zero inference load and every engineered stump lever is pre-solved in the prompt text:

| Engineered lever (Hardness_Plan) | How the prompt neutralizes it |
|---|---|
| **L2 structured-DB skip (SYMMETRIC primary)** | Prompt states "A scope that is billed but not finished, or finished with the bill still sitting unpaid, does not count as closed to me." This hands the agent the exact billed-but-unpaid trap. No structured-store reconciliation is left to skip. |
| **L1 latching + L10 supersession (OPUS-selective)** | Prompt pins the current turn by content: "moved out in the middle of June with a target-ready date at the end of the month, which has already come and gone." That IS recbd087's distinguishing content, so no disambiguation between the two make-ready rows remains. |
| **L31 explicit negative directive (GEMINI-selective)** | Prompt already frames the hold path: "if it is not, say so plainly and hold it ... it does not go to listing until every outstanding scope is closed and signed off." The negative is scaffolded, not withheld. |
| **L9 future-event gotcha** | Prompt states "There is also a re-inspection on the calendar for the middle of this month, and it factors into whether I can call this one done." The 7/15 discriminator is named outright. |

Every rubric criterion traces to an explicit prompt sentence. This is the "escape-valve clause neutralizes the lever" pattern (Stump_Hypotheses Task 25) taken to its limit — the whole prompt is one escape valve that pre-solves the scenario. The universe is genuinely hard (the recbd087/recc8534 supersession trap, the two "done"-flavored maintenance tickets, unpaid bills, the future QC event are all real and well-built), but the prompt gives all of it away.

The only residual difficulty signal is Gemini-only and noise-level: Gemini occasionally (a) skips the Airtable write on recbd087 and only communicates the hold via Linear/Slack/email (crit 1+3, Runs 1-2), or (b) drops a specific dollar figure / the In-Progress+past-due framing from the issue or final response (crit 5-7, 17-19, Runs 2 and 4). Opus never misses any of these. None recur across all runs, so there is no durable stump for either model.

---

## Hardness calibration (Hardness_Plan vs actuals)

- Stump hypothesis hit rate: **0 / 4** predictions fired as engineered.
  - H1 SYMMETRIC (L1+L2 latch on "done"): MISS — Opus 6/6, Gemini 4/6 correctly recorded the hold. The prompt's billed-but-unpaid definition neutralized it.
  - H2 OPUS-selective (L10 supersession / latest-row): MISS — Opus picked recbd087 every run; the prompt's mid-June/6-30 content pin removed the disambiguation.
  - H3 GEMINI-selective (L31 negative omission): MISS — Gemini issued the HOLD/"do not list" negative in all 6 runs; the prompt pre-scaffolded it.
  - H4 MED (L9 past-due / future-event): MISS — both models handled the 7/15 event and 6/30 past-due cleanly.
- Lesson for next task (one paragraph): the difficulty of a StarPM QC-hold scenario lives entirely in the INFERENCE the prompt withholds, not in how well the universe is booby-trapped. This universe was strong; the prompt spent every trap by naming it. To rebuild, the prompt must ask for the QC determination WITHOUT pre-defining "billed-but-unpaid = not closed", WITHOUT naming the two scopes, WITHOUT pinning the turn by its move-out/target dates, and WITHOUT naming the re-inspection as a gating factor. Let the agent discover which of the two make-ready rows is live, that the bills are unpaid, and that a future re-inspection blocks sign-off. See the REDO brief below.

---

## Action items
1. **`PIPELINE REDO — Tasks/45_6a6525d5201ac850ceb19a36`** (mandatory — difficulty FAIL on both models, Opus 100%). Archive the current 5/6/7 and rebuild from scratch as a CB build.
2. REDO prompt brief: keep the Mesa Vista 4C anchor and universe (traps are real and well-grounded), but STRIP the giveaways from the prompt — do not define billed-but-unpaid, do not enumerate the deep-clean + interior-repaint scopes, do not pin the turn by its dates, do not name the 7/15 re-inspection. Force the agent to (a) discover recbd087 is the live turn vs the recc8534 selReady decoy and the two "done" maintenance tickets, (b) reconcile QuickBooks to find the unpaid bills itself, (c) surface the 7/15 future event on its own. Target Opus pass@1 <= 40% and per-model density >= 40.
3. No rubric fixes to apply and no AF justifications to ship — the rubric set graded cleanly; it is the prompt's information content, not the rubrics, that must change. (When the prompt is rebuilt, the rubric discriminators will need to be re-derived against the harder prompt.)
