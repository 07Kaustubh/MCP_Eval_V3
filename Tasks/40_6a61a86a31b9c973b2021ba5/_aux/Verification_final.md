# Verification — FINAL Cross-Artifact Council (Task 40, StarPM V4)

## Sources consulted

**Per-task data:**

- `5_Prompt.txt` + `6_Oracle_Events.txt` + `7_Rubrics.json` :: all 3 deliverables read together for integration-level review.
- `_aux/Universe_Split/` :: 15 tables across 8 services; cross-verified end-to-end dependency chain (Slack C001 messages → Airtable rec92f4a1c8e17bd3 → Linear OPS-231 → QB bill 195836274018 Line[0].Description → Gmail e2f3a4b5c6d789ab).
- `_aux/Fact_Ledger.json` :: 206 emails / 403 amounts / 192 dates atom surface — every tight identifier in artifacts traced back to ledger or Universe_Split.
- `_aux/Hardness_Plan.md` :: 6 selected levers (L1 / L2 / L5 / L7 / L8 / L9) traced end-to-end through Prompt sentences + OE steps + Rubric coverage.
- `_aux/Verification_s1.md` + `Verification_s2.md` + `Verification_s3.md` :: prior-phase verifications cross-referenced; all PASS with common THIN density carry HARD FLAG.
- `_aux/Council_Reports/AUDIT_prompt.md` + `AUDIT_oe.md` + `AUDIT_rubrics.md` :: per-phase STRICT AUDIT PASS confirmed.
- `_aux/Council_Reports/INJECTION_report.md` + `INJECT_CHECKER_report.md` :: pre-solve injection audit + post-inject landing verification confirmed clean.

**Eval spec:** all 4 eval specs re-applied at integration layer.

- `Evals_starpm/1_Prompt_Eval.md` :: prompt sub-dims re-scored via Lens 4 drift sweep + Lens 5 narrative-state check.
- `Evals_starpm/2_Oracle_Events_Eval.md` :: OE sub-dims re-scored via Lens 3 forward/reverse map + Lens 5 tool-parameter binding.
- `Evals_starpm/3_Rubrics_Eval.md` :: rubric sub-dims re-scored via Lens 2 binding + Lens 6 Bucket 1 simulation.
- `Evals_starpm/4_Verifier_Fails_Eval.md` :: Lens 6 bucket-classification simulation for all 16 rubrics.

**QC spec:** `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md` :: full sub-dim tree coverage.

- Prompt sub-dims (12) :: all scored via Lens 1 (Truthfulness on prompt identifiers + no-leakage), Lens 4 (drift sweep + shortcut analysis), Lens 5 (state-implying claims).
- Universe sub-dims (2) :: scored via Fact_Ledger atom grounding (Lens 1) + no phantom IDs.
- OE sub-dims (2) :: scored via Lens 3 forward/reverse map + Lens 5 tool-parameter binding on exact catalog tools.
- Rubric sub-dims (5) :: Atomicity / Self-Containment / Completeness / Flexibility / Accuracy all re-verified via Lens 2 + Lens 6.
- Trajectory sub-dim T1 (density projection) :: scored via Lens 3 integrated-trajectory count; T2 (accuracy) + T3 (efficiency) deferred to S4 per phase scope.

## Verification statements

- [x] Validator (`validate.py --phase all`) exit 0 across all 3 artifacts (Prompt 0/0/7, OE 0/1/3, Rubrics 0/9/5; all WARNs are known-false-positive $1,850 heuristic hits on prose atoms per Verification_s3.md).
- [x] Phase-readiness gate (`phase_ready.py --phase final`) exit 0 after Verification_s3.md header rename + category tags added.
- [x] 6 FINAL lenses returned PASS: Truthfulness / Rubric Binding / Cross-Artifact Holism / Red-team / Narrative-State + Action-Prescription / Verifier-Fails-Spec Pre-Upload.
- [x] Zero answer leakage: grep across prompt body + injected Slack messages + injected Gmail body for `1850` / `full unit` / `Ruud` / `corrosion` / `burner assembly` / `cracked heat exchanger` returned 0 hits. QB Line[0].Description is the sole verbatim scope-truth surface (design-correct L2 load).
- [x] Every 6 Hardness levers still triggers end-to-end per FINAL Lens 3 lever map.
- [x] All 13 hard rules PASS per FINAL Council report Hard Rules Table (Council_Reports/FINAL_council.md).
- [x] Lens 6 Bucket 1 risk = 12.5% LOW-MED (rubric 8 send-vs-draft functional; rubric 16 compound bundle) / 0% HIGH — well under 20% BLOCKER threshold.
- [x] 16 outcome rubrics / 0 process rubrics; multi-recipient atomicity satisfied for 3 Gmail drafts.
- [x] Entity references consistent: Tanya → tanya.mitchell@gmail.com; Robert → robert.finley@gmail.com; Diane → ap@hillcountryplumbing.com (NOT Diane Flores at Lonestar); Tony → Tony Reyes Lead Maintenance Tech (NOT Tommy Reyes the resolved Unit 14 tenant).
- [x] Implicit-prompt framing preserved end-to-end: no rubric demands an explicit "flag the discrepancy first" step.

## Discrepancies surfaced

- **HARD FLAG (inherited from HARDNESS + S1 + S2 + S3, not FINAL-attributable):** Density THIN under strictest lens. FINAL Lens 3 strictest per-service accounting projects ~28-30 midpoint; Council B v3 optimistic ~38-40; Hardness_Plan generous 56. Root cause is prompt-level scope of ask, not FINAL-fixable. Accepted per AGENTS.md Rule 11 via documented 6-lever buffer over default 4-5 (Hardness_Plan §THIN carry). Escalation trigger: platform 6-run average <40 tool calls → `PIPELINE REDO` mandated with 7th lever (L3 missing-reply or L12 document-cross-reference StarPM adaptation).
- **Two-Dianes universe ambiguity:** Diane Flores (Lonestar Maintenance Supply) vs unnamed Diane (Hill Country Plumbing AP). Resolved at rubric level via exact-email routing on `ap@hillcountryplumbing.com`. Cannot resolve to Diane Flores. Confirmed no artifact accidentally names "Diane Flores" where Hill Country is meant.
- **Rubric 8 "send-message action rather than the draft action" language:** Under strictest reading, closest to the no-tool-name-in-rubric-title rule. Verified as FUNCTIONAL description (natural language) not tool-identifier (underscore-separated code identifier `slack_send_message` / `slack_send_message_draft`). Explicit Verification_s3.md finding upheld by FINAL Lens 6 as non-defect.
- **Validator $1,850 WARNs:** amount is in QB Line[0].Description prose but not tagged as canonical amount atom in Fact_Ledger (heuristic gap). Confirmed groundedness via direct Universe_Split read; non-defect.

## Verdict

**PASS** — Cross-artifact holistic council cleared all 6 lenses + all 13 hard rules under strict interpretation. One HARD FLAG inherited from prior phases for platform-run monitoring. Task 40 is cleared for the StarPM V4 pre-upload SUBMISSION_GATE.

---

## RE-RUN v2 (2026-07-23)

**Trigger:** `7_Rubrics.json` mtime 19:30:57 > prior `FINAL_council.md` mtime 18:59:27 → prior verdict stale, rubric count expanded 16 → 28 by atomizing bundled body rubrics into single-fact rubrics.

**Re-verified sources:** all v1 sources re-consulted; additionally `_aux/Council_Reports/FINAL_council.md` v1 read for regression comparison only (no conclusions copied — full re-verify from artifacts).

**v2 verdict: PASS** (0 BLOCKER / 0 MAJOR / 1 MINOR observation).

**What changed vs v1:**
- Rubric count 16 → 28 (+12 via atomization; +75%).
- Outcome / Process split now 28/0 (v1 was 16/0). Discipline preserved.
- Lens 6 Bucket 1 risk 14.3% LOW-MED / 0% HIGH (v1 was 12.5% LOW-MED / 0% HIGH). Still under 20% threshold; slight uptick reflects greater surface area for LOW-MED classification, not a defect regression.
- Multi-recipient atomicity now MORE compliant: 3 separate 1.1 Gmail-draft existence rubrics (16 / 19 / 24) satisfy V4 rule cleanly.
- All 6 hardness levers (L1 / L2 / L5 / L7 / L8 / L9) preserved with STRONGER enforcement — atomization reduces shortcut-satisfaction risk since each body fact must land independently.
- Answer-leakage sweep re-run: grep on "1850" / "full unit replacement" / "Ruud" / "corrosion" / "burner assembly" / "cracked heat exchanger" in Universe_Split confirms zero leakage in prompt + injected Slack + injected Gmail. Corpus "1850" substring hit in a Slack message ID (coincidental) + "full unit replacement" hit in unrelated 2026-05-23 Wesley→Tony Unit-14 $4,200 decoy thread (L1-strengthening, non-defect).
- Density projection unchanged (write count identical between v1 and v2 — rubric atomization does not change tool-call surface). THIN HARD FLAG inherited.

**New MINOR observation (non-defect, non-blocking):** rubric 7 (Linear description) still bundles 2 facts (full-unit-replacement scope + Thursday-retained) while every other body was fully atomized in the v2 expansion. Under strictest atomicity-consistency reading this is asymmetric with rubrics 4+5 (Airtable), 13+14+15 (Slack), 17+18 (Diane), 20+21+22+23 (Tanya), 25+26+27 (Robert). V3 Rubric_Format.md explicitly permits the single-artifact narrative-bundle pattern, so this is not a defect. Logged for potential future normalization pass; does not block platform submission.

**Hardness_Patterns_Log.md:** no update — same 6 levers preserved end-to-end; v2 rubric expansion strengthens enforcement of the same lever set, no new lever selection.

**Task 40 cleared for `PIPELINE SUBMISSION_GATE` (v2 verdict supersedes v1).**
