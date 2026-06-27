# REVIEW2 summary — Task 30_6a3de5194c34125ef86fb36f

**Trigger:** `PIPELINE REVIEW — Tasks/30_6a3de5194c34125ef86fb36f/_aux/Scratch_Corrected COUNCIL_MODE=multi`

**Mode:** Multi-mode second-opinion gate on the CORRECTED MATERIALIZATION of a SALVAGEABLE task. Five independent Council B lens reviewers + Council A grounding + FINAL cross-artifact + Council B consensus. Council Protocol §"True multi-model Council B" point 4 invoked for veto propagation.

**Final verdict:** **REVISE — corrected materialization cannot ship as-is.**

## Wave-1 outputs (read in parallel)

| Seat | Verdict | Findings | Report path |
|---|---|---|---|
| Council A — Grounding + Convention | GO | 0 BLOCKER / 0 MAJOR / 0 MINOR / 1 INFO | `REVIEW2_A_grounding.md` |
| Lens 1 — Architect (B1+B4) | PASS | 0 BLOCKER / 0 MAJOR / 1 MINOR (Lever 2 implicit prompt hook flagged informational) | `REVIEW2_B_architect.md` |
| Lens 2 — Implementer (B5) | REVISE | **1 BLOCKER** — rubric #21 evidence references non-existent `body` parameter on email_send_email | `REVIEW2_B_implementer.md` |
| Lens 3 — Red-team (B2) | REVISE | **3 BLOCKERs** — rubric #5 hidden trap; rubric #13 prompt fragility (re-classed to MAJOR by consensus); effective lever count = 1 (subsumed) | `REVIEW2_B_redteam.md` |
| Lens 4 — Ground-truth (B1+B5) | PASS | 0 BLOCKER / 0 MAJOR / 0 MINOR — every concrete atom verified in `_aux/Universe_Split/`; prompt clean of derived-answer leakage | `REVIEW2_B_groundtruth.md` |
| Lens 5 — Integration (B3+B4+B6) | REVISE | **1 BLOCKER** PROPAGATE TO S1 (rubric #5 hidden trap), 1 MAJOR (THIN_DENSITY), 1 MINOR | `REVIEW2_B_integration.md` |
| FINAL — Cross-artifact holistic | PASS | 1 MAJOR (rubric #5 title verbatim JE id — re-classed to BLOCKER by consensus on FINAL.md hard rule), 3 MINOR | `REVIEW2_FINAL.md` |

## Wave-2 consensus

Spawned 6th consensus sub-agent per Council_Protocol multi-mode point 4. Resolved 5 disagreements with cited rule evidence. ROUND VALID: yes. VERDICT: REVISE.

**3 BLOCKERs survive consensus:**

1. **Rubric #5 hidden trap (PROPAGATE TO S1)** — prompt does not surface the JE-id-in-subject requirement that rubric #5 demands. Two seats raised BLOCKER on independent paths (Red-team + Integration); FINAL/Architect counter-arguments were uncited assertions. Per Council_Protocol B6 example, "silently keep both" is forbidden. Fix: prompt re-frame on `_aux/REVIEW_prompt_draft.txt` line 6 to surface filterability/correlation requirement.

2. **Rubric #5 title contains derived JE id verbatim** — `JE-acme_cloud-FP-2026-04-0052` literally in title. Per `Reference/Sessions/FINAL.md` hard-rules table: "Correct derived figure is NEVER stated verbatim in... rubric title..." → BLOCKER. FINAL flagged but downgraded to MAJOR on uncited reasoning; consensus applies the rule as written. Fix: rewrite title (one line); keep verbatim JE id in evidence.

3. **Rubric #21 evidence "body parameter"** — non-existent API parameter; correct is `content` per AGENTS.md trap. Intra-file inconsistency (rubrics #4 / #5 / #6 / #7 all name correct parameters). Fix: replace "body" → "content" in rubric #21 evidence (three occurrences).

**2 MAJORs accepted with monitoring:**
- THIN_DENSITY (projected midpoint 45-50 vs design target 50+; acceptable per AGENTS.md Rule #11 with `REVIEW_hardness.md` per-task justification)
- Single-rubric-monopoly fragility on rubric #13 (auto-mitigated if BLOCKER #1 takes preferred prompt-re-frame fix)

**3 MINORs / 1 INFORMATIONAL:** rubric #4 atomicity borderline (acceptable per Row 5 intent), rubrics #6/#7/#14 parameter keys in titles (compliant per hard rule #7), validator action-verb whitelist gap (project-wide).

## Overturned verdicts

- `AUDIT_prompt.md` PASS (STRICT) — **OVERTURNED** by BLOCKER #1 (Council_Protocol B6 PROPAGATE TO S1)
- `AUDIT_rubrics.md` PASS (STRICT) — **OVERTURNED** by BLOCKER #2 (FINAL.md hard rule) and BLOCKER #3 (AGENTS.md parameter trap)
- `AUDIT_oe.md` PASS (STRICT) — NOT overturned (no finding traces to OE root cause)

The overturns reflect the consensus protocol's mandate to apply rules under their plainest cited reading and to honor the BLOCKER veto when a single seat raises a finding backed by cited rule evidence with no cited counter-disproof.

## Changes pushed to `changes.md`

Three new rows (#8, #9, #10) added as BLOCKERs with status Pending; one row (#11) added as conditional-escalation MINOR.

## Recommendation + next-trigger paths

**Do NOT ship the current `_aux/Scratch_Corrected/` bundle to platform.** It still mirrors the as-shipped `14_Updated_Oracle_Events.txt` / `15_Updated_Rubrics.json` / `_aux/REVIEW_prompt_draft.txt` in the parent task directory; those carry the same BLOCKERs.

| Scenario | Next trigger (in a fresh chat) |
|---|---|
| Operator marks Rows 8 + 9 + 10 Applied (preferred path) | `PIPELINE REVIEW — Tasks/30_6a3de5194c34125ef86fb36f` to materialize the fixes into a new corrected version (`14_*` / `15_*` / `_aux/REVIEW_prompt_draft.txt` get rewritten) and re-run all gates. Operator may also re-invoke with `COUNCIL_MODE=multi` for max-rigor re-audit. |
| Operator marks Row 8 Applied via the **alt path** (drop rubric #5 instead of prompt re-frame) | Row 11 (single-rubric monopoly) escalates to BLOCKER per Hardness_Playbook composition rule. Recommend `PIPELINE REDO — Tasks/30_6a3de5194c34125ef86fb36f` to rebuild from scratch with a fresh lever combination. |
| Operator marks any Row Dismissed-with-proof | Cite the per-task universe evidence in the changes.md Status column. Re-run REVIEW after the dismissal is recorded. |
| Operator decides to ship as-is despite REVIEW2 verdict | Override path — not recommended. Recall that prior `AUDIT_prompt.md` and `AUDIT_rubrics.md` STRICT PASS verdicts are now overturned with cited rule evidence; shipping accepts the documented risks. |

## Files produced this REVIEW2 pass

- `_aux/Council_Reports/REVIEW2_A_grounding.md` (Council A)
- `_aux/Council_Reports/REVIEW2_B_architect.md` (Lens 1)
- `_aux/Council_Reports/REVIEW2_B_implementer.md` (Lens 2)
- `_aux/Council_Reports/REVIEW2_B_redteam.md` (Lens 3)
- `_aux/Council_Reports/REVIEW2_B_groundtruth.md` (Lens 4)
- `_aux/Council_Reports/REVIEW2_B_integration.md` (Lens 5)
- `_aux/Council_Reports/REVIEW2_FINAL.md` (FINAL cross-artifact)
- `_aux/Council_Reports/REVIEW2_B_consensus.md` (Wave-2 consensus)
- `_aux/Council_Reports/REVIEW2_score.md` (per-phase QC scoresheet, this pass)
- `_aux/Council_Reports/REVIEW2_summary.md` (this file)
- `changes.md` (Rows 8-11 appended; summary updated)

Originals (`5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`, `2_Persona.txt`) and the prior corrected materialization (`14_Updated_Oracle_Events.txt`, `15_Updated_Rubrics.json`, `_aux/REVIEW_prompt_draft.txt`, `_aux/REVIEW_persona_draft.txt`) **UNTOUCHED** — REVIEW2 is read-only per runbook step 9.

## Process learning to append to `Tasks/_meta/Learnings.md` on close

When a REVIEW pass adds a NEW rubric to diversify levers (e.g., Row 5's email-subject-JE-id rubric), the changes.md row must include a step-5-equivalent verification check: **does the prompt actually surface the requirement the new rubric demands?** If the answer is "the prompt's general framing implies it" (an inferential bridge), that is a hidden trap per Council_Protocol B6 and the prompt must be re-framed in the SAME row (not silently kept implicit). The corrected materialization on Task 30 added rubric #5 in REVIEW1 Row 5 without this verification step, which the multi-mode second-opinion REVIEW2 caught as a BLOCKER. Future REVIEW Row proposals that add rubrics must include the prompt-surface check as a verification predicate.
