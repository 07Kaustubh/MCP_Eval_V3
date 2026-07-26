# Verifier Fails — S4 verdict (StarPM V4, dual-model: Opus 4.8 + Gemini)

Task: Tasks/39_6a602c8886ebb06f12354d77 · Scenario: Las Palmas 8D make-ready turn closeout · Persona: James Bennett (p_006, Assistant Maintenance Tech) · 15 rubrics, all Outcome.

/ Note: `9_QC_Feedback.txt` / `10_PT_Dispute_To_QC_Feedback.txt` / `11_Final_QC_Validation_On_PT_Dispute.txt` are 0-byte scaffold placeholders — this is a straight verifier-fails S4, NOT a QC-feedback/dispute-stage task, so `qc_verdict.py parse|classify|audit` is N/A (no dispute trio to structurally parse). /

## Rubric legend
- R1 OPS-227 parts-approval follow-up for the full replacement
- R2 update stale make-ready row receb057b02f20052 (no longer "ready")
- R3 change that row's status ready -> in progress (selReady -> selProg)
- R4 that row's notes state disposal seized / awaiting full replacement
- R5 post an update in #make-ready (C004) about 8D
- R6 that C004 post states 8D not ready + should not be marketed/shown
- R7 that C004 post names the seized disposal / replacement as the open item
- R8 draft email to john.smith@starpm.com about where 8D stands
- R9 email states 8D not yet ready to close
- R10 email names seized disposal (full replacement, pending parts approval) as outstanding
- R11 email states path to finish (approve/order replacement, install, final walk/closeout)
- R12 identifies 8D not ready to close despite logged status + channel chatter
- R13 identifies seized disposal as blocker needing full replacement + pending approval
- R14 identifies turn incomplete in Airtable (SoR): MT-2026-1271 open, blank completion date (or equiv. record still selProg)
- R15 reports rest of turn work complete (in-house repairs, carpet, deep clean, punch-list, refrigerator swap)

## Run matrix — OPUS (P=pass F=fail)
```
        R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 | pass
Run1     F  P  P  F  P  P  F  P  P  F   F   P   F   P   F   |  8/15
Run2     P  P  P  P  P  P  P  P  P  P   P   P   P   F   P   | 14/15
Run3     F  P  P  F  P  P  F  P  P  F   F   P   F   P   P   |  9/15
Run4     P  P  P  P  P  P  P  P  P  P   P   P   P   P   F   | 14/15
Run5     P  P  F  P  P  P  P  P  P  P   P   P   P   P   P   | 14/15
Run6     P  F  F  F  P  P  P  P  P  P   P   P   P   F   P   | 11/15
fails/6  2  1  2  3  0  0  2  0  0  2   2   0   2   2   2
```
Opus all-15-pass runs: 0/6. No rubric fails all 6 (max R4 = 3/6).

## Run matrix — GEMINI
```
        R1 R2 R3 R4 R5 R6 R7 R8 R9 R10 R11 R12 R13 R14 R15 | pass
Run1     P  F  F  F  P  F  P  P  P  P   P   P   P   P   P   | 11/15
Run2     P  P  P  P  P  F  P  P  P  P   P   P   P   P   P   | 14/15
Run3     P  F  F  F  P  F  P  P  P  P   F   P   P   F   P   |  9/15
Run4     P  F  F  F  P  F  P  P  P  P   P   P   P   P   P   | 11/15
Run5     P  F  F  F  P  F  P  P  P  P   F   P   P   F   P   |  9/15
Run6     P  F  F  F  P  F  P  P  P  P   P   P   P   F   P   | 10/15
fails/6  0  5  5  5  0  6  0  0  0  0   2   0   0   3   0
```
Gemini all-15-pass runs: 0/6. **R6 fails all 6 (sole all-failing rubric in the task).** R2/R3/R4 fail 5/6 (only Run2 targeted receb057b02f20052).

Rubrics passing all 12 runs both models: R5, R8, R9, R12.

## Trajectory T3 — Error Rate
Erroneous runs: Opus 0/6, Gemini 0/6 (all 12 runs completed to a verifier-evaluable state; every trajectory carries a terminal result item). Verdict: **PASS (< 3)** each model.

## Trajectory T2 — Agent Failure Rate (pass@1 <= 40%)
Runs passing all 15 rubrics: Opus 0/6, Gemini 0/6. pass@1 = **0.0%** each model. Verdict: **PASS (<= 40%)**. The 15-rubric conjunction is unwinnable in a single pass on either model while every individual rubric is achievable (distributed difficulty).

## Density (StarPM V4 per-model: 40 design target / 15 fail floor)
| Model | Avg total tool calls | vs 40 target | vs 15 floor | Verdict |
|---|---:|---|---|---|
| Opus 4.8 | 43.5 (46,52,46,46,45,26) | >= 40 | >= 15 | **PASS** |
| Gemini | 33.0 (33,37,28,31,36,33) | THIN (< 40) | >= 15 | **PASS (floor); THIN vs target** |

Neither model is below the 15 floor, so **no REDO trigger**. Gemini runs fewer tool calls per run than Opus (33 vs 43.5); the projection (48.5/model) held for Opus and over-predicted Gemini by ~15.

> **PARSER DEFECT (surfaced, non-blocking for this task).** `Validators/parse_trajectories.py` reports Gemini avg=0 because it does not recognize the Gemini flat-list schema (`type: "tool_use"` items with `tool_name`/`parameters`; MCP calls prefixed `mcp_mcp<hash>_`). It only counts the Opus nested-content schema. The Gemini numbers above (avg 33.0) were recomputed by hand by counting `type=="tool_use"` items per run. `_aux/Trajectory_Stats.json` currently stores the wrong Gemini figure (0). This did not change this task's verdict (Opus 43.5 drives PASS; Gemini's true 33.0 is above the floor), but on a future V4 task where Gemini is the only model clearing the floor it could emit a FALSE `REBUILD_CANDIDATE_DENSITY`. Recommend patching the parser to handle the Gemini schema. NOT fixed here (shared, regression-pinned validator; out of S4 scope).

## Classifications
- **Bucket 1 (rubric invalid): 0** rubrics. See S4_fixes.md (documents why none, incl. the R14 / R2-R4 specificity analysis against ground truth).
- **Bucket 2 (judge error): 0** rubrics. See S4_judge_errors.md (documents the R6 all-fail and Opus-Run5-R3 spot-checks that ruled out judge error).
- **Bucket 3 (legitimate model failure): every failing rubric instance.** Per-model trajectory walk in `_aux/S4_bucket3.md`; AF justifications in S4_AF_justifications.md (voice gate exit 0).

Distinct failing rubrics: Opus 10 (R1,R2,R3,R4,R7,R10,R11,R13,R14,R15); Gemini 6 (R2,R3,R4,R6,R11,R14).

### Ground-truth confirmations (re-grep of _aux/Universe_Split/)
- Three 8D make-ready rows: `receb057b02f20052` (2026-05-01, **selReady**, "cleared for leasing - available to show immediately" = the stale row R2/R3/R4 target); `recf7aecc318b2252` (2026-05-14, selProg); `rec651427ec0d84dd5a` (2026-06-25, selProg, fridge "delivered and installed"). R3's justification ("two later 8D rows are in progress") matches exactly. Requiring the specific stale selReady row is grounded, not over-strict.
- `rec651427ec0d84dd5a` **exists** in the universe. Gemini Run6's verifier claim that it is "a hallucinated record ID" is factually wrong (does not change the fail verdict; the agent still failed to target receb057b02f20052).
- `MT-2026-1271` = `recac236210094352` in tblMaintenanceTickets, **blank fldCompletionDate** = OPEN. It is the master maintenance ticket that opened the 8D turn; "make-ready ticket" is loose labeling but factually correct as the turn's master ticket. R14 grounded.
- OPS-227: issue title "Clear garbage disposal **jam**" + description "reset and clear the jam" is **overridden** by the 2026-06-22 comment "the 8D disposal is **seized, not just jammed** ... needs a **full unit replacement** ... Routing back to you for **parts approval**." completed_at null (open). This comment-overrides-title structure is the central lever; Opus runs 1 & 3 stopped at the title (jam) and failed the whole disposal cluster.
- rec651427 (June fridge row) documents the swap complete — the same row is the R15 evidence AND the R2/R3/R4 decoy (must be read but must NOT be the record updated for the ready-status fix).

## All-Failing Rubrics sub-dim
Bucket 1 count / total failing rubrics = **0 / 11 (union) = 0%**.

| Bucket 1 ratio | Score |
|---|---|
| < 25% | **5/5 (PASS)** |

Score: **5/5 (PASS).** The one all-failing rubric (Gemini R6) is Bucket 3, not Bucket 1: Opus satisfies R6 in all 6 runs (e.g. Run2 C004 "status correction, please don't treat as fully ready yet"), and all 6 Gemini C004 posts verified to contain no "not ready / don't show / don't market" language (positive framing only). The rubric set is sound.

## Hardness calibration (vs _aux/Hardness_Plan.md stump hypothesis)
| # | Predicted | Mechanism | Actual | Verdict |
|---|---|---|---|---|
| 1 | Both models report 8D ready, omit disposal replacement | L10 + L1 | Over-predicted at the global level (both models caught the blocker in most runs). Fired as the jam-vs-seized misread on Opus runs 1,3 (disposal cluster) + emerged as Gemini R6 don't-show gap (6/6) | Partial hit; mechanism confirmed |
| 2 | Trust Linear mirror, skip Airtable SoR, miss MT-2026-1271 OPEN | L2 | Confirmed. R14 fails Opus 2/6 + Gemini 3/6 (chatter shortcut / backfilled completion date) | Direct hit (partial-fail, not all-fail) |
| 3 | Conflate 8D with Rio Bend 214 / lose 8D under 204B swarm | L4 + L6 | No cross-unit confusion observed. Manifested instead as INTRA-unit record disambiguation (R2/R3/R4 wrong-record, Gemini 5/6, Opus 1-2/6) | Partial hit; mechanism confirmed, different surface |
| 4 | Collapse to single write, or update stale row | L7 + variant | Multi-write breadth held (no single-write collapse). Failure was record SELECTION: updated the wrong (non-stale) row, or updated notes without flipping status | Partial hit; inverted (wrong row, not stale row) |

**Stump-hypothesis hit rate: 4/4 mechanisms fired**, though 3/4 manifested on a different surface than predicted, and difficulty was distributed (0% pass@1, every rubric individually achievable) rather than the predicted global "reports ready."

**Under-predicted lever (new):** Gemini's systematic refusal to state "not ready / do not show or market" (R6, 6/6 fail) was the single most reliable stump and was NOT explicitly named in the plan. It emerged from the "correct the stale ready signal" requirement. Logged to Stump_Hypotheses.md.

**Density lesson:** projection 48.5/model held for Opus (43.5) but over-predicted Gemini (33.0) by ~15. Gemini consistently uses fewer tool calls per run on the same task; future V4 projections should carry a per-model spread, not a single midpoint.

## Action items
- Bucket 1: none. No rubric fixes required.
- Bucket 2: none. No judge-error appeals.
- Bucket 3: ship the AF justifications (S4_AF_justifications.md, voice gate clean) to the platform to defend the intended difficulty, per model.
- Optional (non-blocking) wording nits, ship-as-is: R14 could name MT-2026-1271 as the master maintenance/turn ticket rather than "make-ready ticket" for precision; the "or equivalently ... selProg" alternative could be stated a touch more explicitly. Neither caused a fail or judge error; do NOT gate on these.
- Follow-up (separate from this task): patch `parse_trajectories.py` for the Gemini flat-list schema so `_aux/Trajectory_Stats.json` stops recording Gemini density as 0.

## Verdict: STRONG PASS
pass@1 0% both models · 0 errored runs both models · density above floor both models (Opus PASS target, Gemini PASS floor/THIN target) · 0 Bucket 1 · 0 Bucket 2 · All-Failing sub-dim 5/5. Difficulty is genuine and the rubric set is sound. No REDO.
