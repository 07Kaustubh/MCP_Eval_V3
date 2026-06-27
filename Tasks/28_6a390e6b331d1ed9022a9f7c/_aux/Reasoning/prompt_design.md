# Prompt Design Reasoning — Task 28_6a390e6b331d1ed9022a9f7c

## Levers engineered into 5_Prompt.txt

| # | Lever | Prompt surface |
|---|---|---|
| L1 | Latching (Anaya FX framing vs Hannah's duplicate-classification) | Para 1: "My drill tied the swing cleanly to one Acme Research Ltd UK subscription line that was booked at the March invoice-date spot rate and missed the April closing-day revaluation." Voice anchors FX-catch-up as settled fact; no escape valve hints classification might be wrong. |
| L5 | Thread-reply blindness (Hannah's VEN-441207 reply in C005) | Para 4: "Drop a short summary in the close channel so the team has the same picture going into the rest of the week." Surfaces C005 for the write; agent's thread-reply discipline determines whether they pull Hannah's VEN-441207 / two-identical-invoices reply. |
| L7 | Multi-write diversification (7 writes across 7 services) | Paras 3-6: (1) stage JE; (2) recon variance notes; (3) exception note without resolving; (4) email Ryan cc Daniel+Andrea+Hannah; (5) Slack close channel; (6) fresh Vault memo with retention discipline; (7) reminder reset. |
| L8 | Multi-link chain (messaging → BL → Slack → SAP) | Para 1 (messaging framing) + Para 3 ("the exception that's been sitting on this recon since the 25th" → BL) + Para 4 (close channel → Slack) + Para 5 ("pull the underlying invoice line into it so anyone reviewing can retrace the figure end to end" → SAP). Four hops. |
| L9 | Twin gotcha (FP-2026-06 period trap + phantom Vault doc) | Para 3 ("Stage the entry in the right place against the right period") — agent must verify period; Daniel's `email_scen_040_recon_currency_refresh_0005` names FP-2026-06 (future) as the decoy. Para 1 ("The workings are already up in Vault under the title Brookfield May 2026 AP-external-vendors FX variance workings") — phantom doc title cited as settled fact; agent who cites without verifying via `records_vault_list_documents` fails. |

## Expected stump targets (from Hardness Plan)

| # | Prediction | Confidence | Mechanism |
|---|---|---|---|
| 1 | Agent stages corrective JE on FX framing without consulting the duplicate-classification exception | HIGH | L1 latching + L9 authority dismissal |
| 2 | Agent cites phantom Vault doc verbatim OR tags fresh memo with `FIRM_INTERNAL` instead of `AICPA_SQMS_7Y` | HIGH | L1 confirm-already-done + L28 default-variant trap |
| 3 | Agent posts JE to `brookfield_FP-2026-06` per Daniel's recap email (which has `status=future`) | MED | L9 authority dismissal + L11 structured-source skip |
| 4 | Agent reads Ben's C005 parent without pulling Hannah's thread reply — misses VEN-441207 / consecutive-invoice-numbers signal | MED | L12 thread-reply blindness |

## Council verdicts

| Phase | Round | Verdict |
|---|---|---|
| Validator | r1 | PASS (402 words, 1 advisory warn) |
| Council A (grounding/convention) | r1 | BLOCK (BD3 reminder grounding mismatch) |
| Council B (adversarial QC) | r1 | GO |
| Validator | r2 | PASS (403 words) |
| Council A | r2 | GO (reminder claim now grounds to `reminder_scen_011_orphan_exception_0000`) |
| Council B | r2 | GO (no regression) |
| Similarity gate | r2 | PASS (max composite 29.9 vs Task 14, under 40) |
| AUDIT (strict veteran) | r1 | REVISE (THIN_DENSITY MODERATE — strict mid ~41) |
| Validator | r3 | PASS (419 words) |
| Council A | r3 | GO (para 5 SAP-motivation clause grounds; no escape valve) |
| Council B | r3 | GO (density 47 → 49; L8 Hop D STRONGER) |
| Similarity gate | r3 | PASS (max composite 29.3 vs Task 14, under 40) |
| AUDIT | r2 | **PASS (STRICT, with THIN acceptance)** |

## Final similarity score

Max composite **29.3** vs `QC_Tasks/V3_Tasks/Task14_6a29448b7e4c641c30eb3875/Prompt.txt`. Well under the 40 threshold. Raw lexical 29.3 with `mult=1.000` (no contextual differentiator discount applied — the prompts are genuinely lexically distinct despite both anchoring on Brookfield's stuck May close). Task 14 leads with a senior voice surveying the full close ("our own May books still aren't locked"); Task 28 leads with the trainee's narrow item-level focus ("My one recon item from Brookfield's May FX refresh is still sitting open").

## AUDIT verdict

**PASS (STRICT, with THIN acceptance)** on round 2.

**Density:** strict midpoint 43-46 (Council B 49). Sits in THIN_DENSITY band (40-49). Floor of 40 cleared comfortably. Real-trajectory expectation 47-53 with downstream OE-level coverage.

**Why THIN acceptance:** every plausible round-3 fix to push strict mid >= 50 carries pre-solving or L1 escape-valve risk (e.g., "make sure the support file matches the subledger" → escape valve; "cross-check the vendor master" → L1-killing verification directive). Marginal density gain (+1-2 calls) for material lever-loss risk = bad trade. L1 latching is the highest-confidence lever (Stump Prediction 1 HIGH); must be preserved. AGENTS.md Rule 11 expressly permits THIN_DENSITY operation with explicit per-task justification.

**Locks the THIN acceptance — binding on S2 / S3:**

S2 required OEs:
- SAP query "Acme Research" → ZERO results
- SAP query VEN-441207 → ZERO results
- C005 thread-reply pull at parent ts=1779891480.000000
- Vault search for phantom doc title → ZERO results
- FP-2026-05 (open) + FP-2026-06 (future) status verification
- Reminder anchored on `reminder_scen_011_orphan_exception_0000`

S3 required rubrics:
- JE `period_id = brookfield_FP-2026-05`
- JE business_justification accepts classification-conflict acknowledgment OR disambiguation-routed-to-Ryan
- Memo retention `AICPA_SQMS_7Y`
- Memo content addresses underlying-invoice-line traceability (include reference OR acknowledge broken traceability — hallucinated invoice = fail)
- BL exception add-note only, state preserved
- Email cc enforces all three (Daniel + Andrea + Hannah)

Failure to enforce these in S2 / S3 re-opens the density question and triggers downstream REVISE.

## Exit criteria checklist

- [x] `5_Prompt.txt` exists, 419 words ≤ 500, no em-dashes.
- [x] Validator returns PASS for the prompt phase.
- [x] Council A returns GO with zero ungrounded claims (2 engineered NOT-FOUND items fire as designed per L2 + L9b).
- [x] Council B returns GO with all 12 applicable QC sub-dims at 5/5.
- [x] Council B-B3 returns projected mid 49 (under 50+ design target but above 40 floor; THIN_DENSITY acceptance documented).
- [x] Council B-B4 returns "all five Hardness levers from `_aux/Hardness_Plan.md` still triggered".
- [x] Similarity gate returns composite 29.3 < 40 against the prior-task corpus.
- [x] Strict veteran AUDIT returns `PASS (STRICT, with THIN acceptance)` with binding S2 / S3 enforcement notes.
