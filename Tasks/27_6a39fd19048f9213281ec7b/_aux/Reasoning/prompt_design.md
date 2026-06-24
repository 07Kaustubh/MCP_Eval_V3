# Prompt Design — Task 27 (6a39fd19048f9213281ec7b)

**Date:** 2026-06-23
**Persona:** Ben Arinzo (Bookkeeper, Brookfield CPAs & Advisors)
**Business Function:** Bookkeeping
**Word count:** 345 (within ≤350 Hardness Brief target, well under 500 cap)

## Context

This is a CB REBUILD (`PIPELINE REDO`) from a candidate submission that REVIEW called REBUILD on. The candidate's failure mode was blueprint-first construction: OE5b / OE5c / OE10 named a SAP subledger transaction `brookfield_6000001115` carrying a $28.59 payroll-funding adjustment, but that record does not exist in the per-task universe. Rubrics 6 and 7 were unearnable; 0 of 6 candidate runs cleared all 13 rubrics.

The rebuild swings to data-first: pick a real reconciling-item record that exists in `_aux/Universe_Split/`, then engineer the scenario around it. The load-bearing real-record discriminator the agent must find is `exc_d8fc13aa2cc742` (brookfield_FP-2025-12, type=`unrecorded_invoice`, financial_impact=-$617.63, resolution_summary="Corrective JE posted; variance cleared in subsequent recon refresh"). The candidate's prompt body, voice, and multi-thread setup were on-pattern; the discriminator was the structural break.

## Levers engineered into the prompt

| # | Lever | How the prompt surfaces it |
|---|---|---|
| P1 | Latching (consistent feed-drop / accept-timing / June-retry story across Slack + email + messaging) | "It's bounced around a few places this week, so don't go off one message. Track down every place this variance has been discussed and pin down what each person is claiming the cause is, because the read isn't consistent." |
| P2 | Structured-DB skip (blackline_evidence → RV docs, where the recon's `attachments=[]` is misleading) | "Look at what's attached to the reconciliation as support, because that and the thread's read aren't lining up." |
| P7 | Multi-write diversification (4 writes across 3+ services: Slack close thread + Blue + manager + reminder) | "Reach each where they raised it: the close thread, Blue, and the manager approving the disposition. … Set me a follow-up to chase this before the period certifies on the old read." |
| P8 | Multi-link chain (precedent dig: George's FP-2025-11 / $42 / feed-drop claim → falsified against actual FP-2025-11 recon BL-8DCA6908E272 → broader search → real `exc_d8fc13aa2cc742` on FP-2025-12 → resolution_summary → corrective-JE lesson) | "There's also a prior-period precedent the recommendation leans on. Check the number, the period, the cause, and how it was cleared all match the record before that precedent counts." |
| P9 | Universe-grounded gotcha (USD Cash-Payroll → FX revaluation cannot apply → Ben's own variance_explanation is anti-grounded) | "I post the payroll-cash entries on that account, and the read going round (…) doesn't sit right against what that account actually does. … Tie it against the period's own activity on the account." |
| L9 | Authority-dismissal overlay (Ryan/George/Hannah/Daniel/Blue all aligned on the wrong call) | "They want the activity confirmed from the systems before anyone signs off on that story. … And check whose sign-off the disposition has and on what basis, since the recommendation's leaning on that approval." |

L24 soft verbs preserved (no "Daniel was wrong"). L29 escape-valve avoided (verification-of-basis, not contradiction-hunting). L6 verbatim leakage zero (no naming of FX, USD, $617.63, FP-2025-12, exc_d8fc13aa2cc742, corrective JE, $28.59). L25 reminder framed distinctly from existing reminders (`reminder_scen_009_orphan_exception_0000`/`_0008`).

## Expected stump targets

Per `_aux/Hardness_Plan.md`:
1. Agent fails to find `exc_d8fc13aa2cc742` and applies the wrong precedent or stops at "precedent number doesn't match" — HIGH confidence.
2. Agent fails to introspect `blackline_evidence` and misses the mislabeled fx_rate_workbook / subledger_export evidence pointing to Marketing / AICPA JE docs — HIGH confidence.
3. Agent skips the reminder due to two existing reminders on the exception (L25 anchor trap) — MED-HIGH confidence.
4. Agent recommends "do not accept-timing" but does not prescribe the corrective JE remediation derived from the FP-2025-12 precedent — MED confidence.

## Council verdicts

| Phase | Verdict | Notes |
|---|---|---|
| Validator | PASS | 0 fails, 0 warns, 3 notes (word count 345, "this week" relative date — both informational) |
| Council A (round 1) | GO | All 9 load-bearing claims grounded; convention sweep clean |
| Council B (round 1) | GO | 12/12 QC sub-dims at 5/5; projected density 44; all 6 levers preserved; zero phrasing hits |
| Similarity gate | PASS | Max similarity 3.8 vs prior corpus (Task14 V3); well under 30-band PASS ceiling |
| AUDIT (round 1, STRICT) | REVISE | P9 surfacing only indirect (4/5); strict density midpoint 40 below 50+ bar |
| Fixes applied | — | (1) "from where I sit" → "doesn't sit right against what that account actually does" for explicit P9 surfacing. (2) Appended sign-off-basis check after precedent-attribute check for density bump + L9 reinforcement. |
| Council A (round 2) | GO | Both deltas ground; conventions clean; 345 words |
| Council B (round 2) | GO | 28/28 sub-dims at 5/5; strict density 49 (+9 above 40 floor); P9 explicit; L9 reinforced |
| AUDIT (round 2, STRICT) | **PASS (STRICT)** | 33/33 sub-dims at 5/5; strict density midpoint 52 (≥50 bar); 6/6 levers explicit; zero leakage |

## Final similarity score

Max 3.8 against the 29-prompt prior-task corpus + V3 reference set. Top match: `QC_Tasks/V3_Tasks/Task14_6a29448b7e4c641c30eb3875/Prompt.txt`. Well under 30-band PASS ceiling; no pivot required.

## AUDIT verdict

**PASS (STRICT)** on round 2 after one REVISE round and two fix-in-place edits. Both fixes landed verbatim; no further iteration required.

## Ready for next phase

`PIPELINE S2 — Tasks/27_6a39fd19048f9213281ec7b`

---

# Addendum — S1 redraft (post-S2 B6 PROPAGATE broadening)

**Date:** 2026-06-23
**Trigger:** S2 Council B `S2_B_adversarial.md` B6 PROPAGATE TO S1. The prior prompt's four-pillar comparison directive scoped narrowly to "same period" (FP-2025-11) and singular "the record", which allowed a competent narrow-reading agent to satisfy the prompt without discovering `exc_d8fc13aa2cc742` (FP-2025-12 unrecorded_invoice). Two valid readings produced different write-action contents -- a Prompt > Unique Ground Truth fail under the 06/09 QC spec.

## What changed in the prompt

Surgical edit in paragraph 2 only. The narrow directive:

> "Then open the prior-period record and compare it back. Same account, same period, same cause label, same close-out path. If anything is off, tell me what is off and what the record actually shows so I can take it to George."

becomes the forced-broad directive:

> "Then take it apart on all four: same account, same period, same cause label, same close-out path. Pull the record for the period that was named and lay it next to the claim. If that period is not the closest fit for what we are actually seeing on this account, tell me which recent prior-period record on this account is the closer fit, and what that one shows on the same four. I want the real prior-period shape on this account, not the framing in the thread."

The four-pillar test is preserved. The conditional "If that period is not the closest fit" + the capping "I want the real prior-period shape on this account, not the framing in the thread" forces the closer-fit identification under any reading. Em-dash-clean, ID-clean (no "102000"), answer-leakage clean.

## Council verdicts (fresh round)

| Phase | Verdict | Notes |
|---|---|---|
| Validator | PASS | 0 fails, 0 warns, 2 notes (word count 335) |
| Council A grounding | GO | 14 concrete claims all ground; convention sweep clean (zero ungrounded, zero drift) |
| Council B adversarial | GO | 12/12 Prompt sub-dims at 5/5; alt-path closed (both narrow and broad readings converge on same write-action contents); strict density ~42, realistic ~55; 6/6 levers triggered; phrasing scan clean; no upstream propagation |
| Similarity gate | PASS | max 6.2 vs Tasks/25_6a366bc27d66eaedcae82ab4 (well under 30-band PASS ceiling) |
| Strict veteran AUDIT | **PASS (STRICT)** | 28/28 sub-dims at 5/5; LENS 2 leakage clean; LENS 3 all 6 levers trace (P8 now under BOTH readings); LENS 4 strict 42-46 above 40 floor / realistic 55+ above 50 bar; LENS 5 no new defects; S2 propagate structurally resolved |

## Final similarity score

Max 6.2 against the 29-prompt prior-task corpus + V3 reference set. Top match: `Tasks/25_6a366bc27d66eaedcae82ab4/5_Prompt.txt`. Comfortably under the 30-band PASS ceiling. No pivot required.

## Carry-forward observations (S2 / S3 design hooks)

OBS A (archetype residual with Tasks/10 family -- hedge plan if platform reviewer flags) ; OBS B (P9 USD-cash -> no FX surfaces indirectly via evidence-content check -- S3 must rubric explicitly) ; OBS C (four-pillar test + closer-fit identification risk process-style rubrics at S3 -- phrase as OUTCOMEs) ; OBS D (Records Vault retention `FIRM_INTERNAL` + classification `internal` -- S3 must grade) ; OBS E (vault file organization under FP-2026-05 close cycle -- S3 must grade metadata) ; OBS F (strict density THIN at 50+ / realistic 55+ -- S2 has natural opportunities to add density-supporting OE steps).

## Ready for next phase

`PIPELINE S2 — Tasks/27_6a39fd19048f9213281ec7b`
