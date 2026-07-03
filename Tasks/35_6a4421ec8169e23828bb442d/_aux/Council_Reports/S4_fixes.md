# S4 fixes — Bucket 1 (Rubric Invalid)

Task: `Tasks/35_6a4421ec8169e23828bb442d` (fresh 21:56 re-grade)

## Verdict

**0 new Bucket 1 defects surfaced in the fresh re-grade.** No rubric changes required.

## Prior fixes (already applied, verified against fresh grading)

Round 1 (R11 split — pre-fresh backup: `_aux/Council_Reports/pre-fresh-s4/S4_fixes.md` / `7_Rubrics.json.pre-s4-fix`):
- R11 was bundled (aggregate count + qualifier) — split into R11a + R11b atomic rubrics. Fresh grading shows R11 (index 11 in the current file) at 6/6 pass on the fresh re-grade — fix is stable.

Round 2 (Marcus Webb → Evan Mercer fix — pre-fresh backup: `_aux/Council_Reports/pre-fresh-s4/S4_fixes.md` / `7_Rubrics.json.pre-marcus-fix`):
- R10 / R13 / R18 renamed the post-term workstream owner from "Marcus Webb" to "Evan Mercer" to match universe ground truth (`contacts_contact_387de5925670`, Former Loan Officer, inactive). Fresh grading:
  - R10 (email lists 3 Evan Mercer files): 2/6 pass on fresh (was 1/6 pre-fix). Improved.
  - R13 (leadership DM covers 3 feeder workstreams incl. Evan Mercer): 5/6 pass on fresh (was 5/6 pre-fix). Stable.
  - R18 (CRM NOTE covers 4 reconciled workstreams incl. 4/14 Evan Mercer post-term): 4/6 pass on fresh (was 3/6 pre-fix). Improved.

Round 2 collapsed the prior 3 AF rubrics (R5, R14, R33) into partial fails on the fresh re-grade:
- R5 (email covers Raj LOS-integrity caveat): 2/6 pass fresh (was 0/6). Improved.
- R14 (leadership DM references 7 files): 2/6 pass fresh (was 0/6). Improved.
- R33 (final response reports 7 files): 3/6 pass fresh (was 0/6). Improved.

All three prior-AF rubrics passed the 5-point checklist and were not re-classified as Bucket 1 on either the prior verdict or the fresh — they represent legitimate difficulty (multi-service propagation + aggregate-count omission), and the Round 2 relabeling apparently made the judge grade the underlying substance more accurately.

## Sanity re-check per rubric (fresh grading)

For every 22 rubrics with at least one fail on the fresh re-grade, the 5-point checklist was re-applied:

1. **Self-contained + atomic + grounded** — YES on all 22. Each rubric has one criterion, values exist in `_aux/Universe_Split/`, and the judge does not need external lookup.
2. **Flexible enough** — YES on all 22. Rubric text uses "approximately", "(or similar)", and "including" phrasings where variance is acceptable.
3. **Prompt-required** — YES on all 22. Every rubric traces back to a specific ask in `5_Prompt.txt` (reconcile pay-vs-restore + borrower-notice posture; email counsel; leadership DM; CRM NOTE; decision memo; final response).
4. **Real tool names + valid parameters** — YES on all 22 (rubric text does not name tools; where evidence uses tools, they match `Mortgage_Base_Universe/6_Server_Tools_Details.json`).
5. **Achievable by a capable agent** — YES on all 22. Runs 1, 3, 4, 6 each cleared ≥ 30/36 rubrics; the fail spectrum is per-run (Run 5 polarity, Run 2 minimization + workstream-labeling) not systemic across all runs.

No rubric fails checklist item 1 (self-contained) or item 5 (achievable) on the fresh grading. **0 Bucket 1 reclassifications.**

## Action items

None. Ship the current `7_Rubrics.json` unchanged.

---

## Deep-query addendum — Non-Fail cleanup items (recommended, not blocking)

### Cleanup 1 — OE Marcus Webb → Evan Mercer parity fix (Non-Fail Inaccurate OE)

`6_Oracle_Events.txt` lines 27 / 29 / 37 / 39 / 43 still name "Marcus Webb" as the 4/14 post-termination LO. Universe unambiguously names **Evan Mercer** (`crm_crmcontact_5744dda7fddf`, Former Loan Officer, jobtitle inactive; Raj audit email subject "Evan Mercer LOS access disabled"; Denise escalation subject "post-termination LOS access by Evan Mercer"; Priya offboarding email "Evan Mercer's offboarding checklist"). Round 2 fixed the rubric side but missed the OE side.

**Fix**: sed-replace 5 occurrences of "Marcus Webb" → "Evan Mercer" in `6_Oracle_Events.txt`:

- Line 27 (OE 14): "the 4/14 Marcus Webb post-termination LOS access CRM stream" → "the 4/14 Evan Mercer post-termination LOS access CRM stream"
- Line 29 (OE 15): "3 files from the 4/14 Marcus Webb post-termination LOS access" → "3 files from the 4/14 Evan Mercer post-termination LOS access"
- Line 37 (OE 19): "the Marcus Webb post-termination access" → "the Evan Mercer post-termination access"
- Line 39 (OE 20): "the 4/14 Marcus Webb post-termination access" → "the 4/14 Evan Mercer post-termination access"
- Line 43 (OE 22): "Marcus Webb post-term access feeder streams" → "Evan Mercer post-term access feeder streams"

**Severity**: `[Non-Fail - Inaccurate Oracle Events]` per Keystone `Docs_keystone/7_QC_Spec_Doc1.json` Oracle Event dimension. Sub-dim scoring 3/4. **NOT** a shipping blocker (OE Accuracy has no Fail tier under Keystone spec). Editorial cleanup for QC auditor cleanliness.

**Impact if not applied**: OE Accuracy sub-dim scored at 3/4 Non-Fail. Rubric grading unaffected (verifier uses rubric text, not OE text). No agent-run impact.

### Cleanup 2 — Rubric R10 flexibility on 3rd Mercer file (Non-Fail Minor)

R10 (email lists 3 Evan Mercer post-term files) specifies exactly LN-2025-00002, LN-2025-00007, LN-2025-00229. Chain A (Raj's authoritative audit email) names LN-2026-00009 as the 3rd file. Chain B (Denise's notice-queue reconciliation Slack + DRAFT notice email) names LN-2025-00229. Both are universe-grounded. Rubric grades only Chain B agents as passing.

**Fix (optional)**: rephrase R10 title from ...
> "...LN-2025-00002, LN-2025-00007, and LN-2025-00229"

to ...
> "...LN-2025-00002 and LN-2025-00007, plus a third file identified either as LN-2026-00009 (per Raj Anand audit email) or LN-2025-00229 (per Denise Holloway notice-queue reconciliation)"

Same fix for R19 + R24 3rd-file references.

**Severity**: `[Non-Fail Minor Clarity / Specificity Issues]` per Keystone QC Spec Doc1 Rubrics dimension. Sub-dim scoring 3/4. Universe-defensible design trade-off documented in Round 2 meta log — the CB deliberately picked Chain B to preserve 4+3=7 aggregate math (Chain A would collapse to 4+3-1=6 due to LN-2026-00009's collision with the portal-breach set).

**Impact if not applied**: R10 grades stricter than universe supports. Agents citing Chain A (Raj audit) fail R10 — this affected Run 2 + Run 5 on R10 in the fresh grading, but those runs also fail other rubrics for independent reasons. NOT a shipping blocker. R14 / R33 aggregate-of-7 claim is defensible under Chain B.

### Cleanup 3 — Rubric R33 flexibility (Non-Fail Minor)

R33 (final response reports 7 files) inherits the same aggregate-math trade-off. Under Chain A the unique count is 6; under Chain B it's 7. Fresh grading shows Run 5 ("lists more than seven files") failed R33 partly because the agent enumerated across multiple chains and hit >7. This is a Non-Fail-Minor rubric-strictness artifact.

**Fix (optional)**: rephrase R33 title to accept "6 or 7 files" or "the reconciled files count identified across the three feeder workstreams." Not required for shipping.

## Summary of fix scope

- **Rubric fixes required to ship**: 0 (rubric-side clean).
- **Rubric fixes optional (Non-Fail cleanup)**: R10 / R19 / R24 rephrase to accept either LN-2025-00229 or LN-2026-00009. R33 rephrase to accept 6-or-7 file count.
- **OE fixes optional (Non-Fail cleanup)**: 5 line-level Marcus Webb → Evan Mercer swaps.
- **Ship-status**: task ships as-is; optional cleanups improve QC auditor score bands from 3/4 Non-Fail to 5/5 Pass on the OE + Rubric-Flexibility sub-dims.
