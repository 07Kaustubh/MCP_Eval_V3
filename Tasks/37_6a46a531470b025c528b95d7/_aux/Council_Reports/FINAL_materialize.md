# FINAL Council (6 lenses) — Task 37 CORRECTED MATERIALIZATION

**Scope:** Cross-artifact holistic check on `5_Prompt.txt` (unchanged) + `6_Oracle_Events.txt` (unchanged) + `15_Updated_Rubrics.json` (produced by MATERIALIZE with 2 Applied rubric-phase rows).
**Baseline:** `REVIEW_FINAL.md` = PASS on Lens 1/2/5, PASS-with-1-Minor on Lens 3, FAIL Moderate on Lens 4. The two Applied rows target exactly Lens 3 + Lens 4 findings.

## Lens 1 — Truthfulness (cross-artifact)

- Prompt + OE unchanged; their programmatic groundedness was PASS at REVIEW (39/39 universe atoms, hand-audited for entities/loans/dates/amounts/emails).
- Corrected `15_Updated_Rubrics.json`: the two edited rubrics ([3] AFTER + [24] justification AFTER) re-verified atom-by-atom against `_aux/Universe_Split/` in `AUDIT_rubrics.md` (Row #1 + Row #2 sections). Every claim traces to `mortgage_los.loans`, `mortgage_los.document_checklist_items`, `mortgage_los.staff`, or Slack C002/C004 verbatim text.
- No other rubric text changed — the other 28 rubrics inherit the original groundedness verdict from `AUDIT_rubrics_original.md`.
- Em-dash sweep: 0 em-dashes / 0 en-dashes in the corrected file (project-wide AGENTS.md rule 5).
- Programmatic `verify_universe_atoms.py`: original run = 0 fails / 0 warns / 39 atoms across the CB set. The two Applied rows only tighten atoms that were ALREADY in the verified atom surface.
- **Verdict: PASS.**

## Lens 2 — Answer leakage (prompt hardness preservation)

- Prompt file is BYTE-UNCHANGED (`sha256[:16]=d219fff2a319dd5f` — recorded at materialize time; git diff clean on `5_Prompt.txt`). No leakage vector introduced.
- The corrected rubrics land in `15_Updated_Rubrics.json` (a new file), NOT back into `7_Rubrics.json` — so nothing the model would see at solve time changes. Hardness of the pre-solve surface is preserved end-to-end.
- Density projection unchanged (216.8 avg total / 194.7 avg MCP tool calls — well above the 50 design target and 40 floor).
- **Verdict: PASS — no leakage introduced by materialization.**

## Lens 3 — Entity drift

Baseline finding: rubric[24] justification implicitly framed Elena Marchetti as universe-level compliance authority (drift — Elena's LOS role is `processor` with specialization `Doc collection, lender coordination`; Denise Holloway is the actual compliance authority per Slack C004 breach-response initiation and 4-file phishing scope naming).

Fix (Row #2, Applied): rubric[24] title unchanged (prompt names both by name — the rubric correctly follows the prompt). Justification rewritten to:
- Name Denise Holloway as "the confirmed compliance authority per Slack C004 messages (formal breach response initiation for the compromised UWM portal, portal-access audit tied to Keisha's account)" — verbatim quotes present in Denise's C004 posts at ts=1775570820 and ts=1775572140.
- Name Elena Marchetti as "a senior processor whose specialization includes lender coordination — her inclusion in Sofia's escalation chain reflects the prompt's explicit direction." — matches `mortgage_los.staff` role/spec exactly.

No other rubric contains persona-attribution drift. Grace Yamamoto, Camille Foster, Robert Calloway, Sofia Reyes, and the 8 LOs (Amy/Carlos/Derek/James/Keisha/Marcus/Natasha/Priya) all cross-check clean against `mortgage_los.staff`.

**Verdict: PASS. Baseline Minor closed.**

## Lens 4 — Coverage consistency (rubric symmetry across LOs)

Baseline finding: rubric[3] Derek Moss content check covered only LN-2026-00008 (1 of 3 active loans); every other LO in the pipeline received full-loan-set coverage in one bundled per-LO content rubric.

Cohort verification (per-LO content rubric):

| LO | Rubric idx | Loans covered in AFTER title | Loans in Sofia's pipeline for this LO | Symmetric? |
|---|---|---|---|---|
| Carlos Rivera | [1] | LN-2026-00184, LN-2026-00611 (2/2) | 2 | ✅ |
| Derek Moss | [3] AFTER | LN-2026-00008, LN-2026-00196, LN-2026-00632 (3/3) | 3 | ✅ (was 1/3) |
| Keisha Williams | [5] | LN-2024-00103, LN-2025-00330, LN-2025-00380, LN-2026-00376 (4/4) | 4 | ✅ |
| Amy Chen | [7] | LN-2024-00123, LN-2026-00532 (2/2) | 2 | ✅ |
| Natasha Okafor | [9] | LN-2025-00286, LN-2026-00010 (2/2) | 2 | ✅ |
| James Thornton | [11] | LN-2025-00344, LN-2025-00363, LN-2026-00541 (3/3) | 3 | ✅ |
| Priya Desai | [13] | LN-2025-00244, LN-2026-00613, LN-2026-00623 (3/3) | 3 | ✅ |
| Marcus Webb | [15] | LN-2024-00125, LN-2026-00539 (2/2) | 2 | ✅ |

Cross-check: Derek's 3-loan set matches EXACTLY `mortgage_los.loans` filtered on `assigned_lo=los_staff_f9aa4c3c2fcb AND assigned_processor=los_staff_afc9caafae9d AND status not in closed/denied/withdrawn`. All AFTER atoms (status / amount / lock expiration / outstanding required docs) match the raw records.

**Verdict: PASS. Baseline Moderate closed. Cohort symmetry is now uniform across all 8 LOs.**

## Lens 5 — Lever preservation (end-to-end)

Traced 8 hardness levers from prompt → OE → rubric on the corrected set:

| Lever | Prompt anchor | OE anchor | Rubric anchor (corrected) | Preserved? |
|---|---|---|---|---|
| 26 active loans | "every active loan assigned to me" | OE 2 | Rubric [25] | ✅ (unchanged) |
| All 26 locks expired | "whether the lock is still good or expired" | OE 3, 4 | Rubric [17], [26] | ✅ (unchanged) |
| 5 terminated-LO loans | "if any file is assigned to someone who's no longer with the company" | OE 7 | Rubric [20], [27] | ✅ (unchanged) |
| Outstanding docs (26 across 8 loans) | "what conditions or documents are still outstanding" | OE 5, 6 | Rubric [3] AFTER now surfaces Derek's LN-00196 w2_current requirement, Rubric [5], per-LO content | ✅ (STRENGTHENED — new w2_current atom now gated) |
| Phishing scope (UWM/Keisha) | "if anything you find looks like it could be a compliance concern" | OE 8, 9, 26 | Rubric [24] AFTER justification now cites the exact 4-loan scope (LN-2026-00522, LN-2026-00008, LN-2026-00010, LN-2026-00009) | ✅ (STRENGTHENED — verbatim atom set now grounded) |
| TRID/30yr→15yr LN-00613 | (implicit via investigation) | OE 8, 9 | Rubric [24] AFTER justification cites Slack C002 verbatim scope | ✅ (STRENGTHENED) |
| CTC anomaly LN-00623 (5 docs) | "figure out exactly what's blocking progress" | OE 6 | Rubric [13], [28] | ✅ (unchanged) |
| Max-docs LN-00010 (7 docs) | same | OE 6 | Rubric [9], [29] | ✅ (unchanged) |

**Verdict: PASS — no lever loss, 3 levers strengthened by the two Applied rows.**

## Lens 6 — Convention & format hygiene

- 500-word cap: prompt unchanged (343 words per baseline REVIEW score).
- No em-dashes / no en-dashes: 0 in prompt (unchanged), 0 in OE (unchanged), 0 in corrected rubrics (verified after em-dash replacement in rubric[24].justification).
- No "at least N" in rubric titles unless prompt-mandated: 3 uses on the original (activity note / CRM engagement / compliance concern) — all defensible per baseline AUDIT; corrected version unchanged (Row #1 and Row #2 did not touch these rubrics).
- No tool names in rubric titles: 0 tool names in any of the 30 corrected rubric titles.
- Method-lock hygiene: 2 method-locks (Slack C002 in rubric [21], Elena+Denise emails in rubric [24]) — both prompt-inherent; unchanged by Row #2 (title untouched).
- Flat rubric schema per v9 mandate: preserved (title / category / justification / evidence, no nested keys).
- **Verdict: PASS.**

## Final verdict

**FINAL: PASS (STRICT)**

- Lens 1 Truthfulness: PASS (all atoms grounded, universe re-queried for the two edits)
- Lens 2 Answer leakage: PASS (prompt untouched, corrected rubrics live in `15_Updated_Rubrics.json`, hardness preserved)
- Lens 3 Entity drift: PASS (Elena attribution grounding closed; baseline Minor resolved)
- Lens 4 Coverage consistency: PASS (Derek cohort symmetry restored; baseline Moderate resolved)
- Lens 5 Lever preservation: PASS (0 losses, 3 levers strengthened)
- Lens 6 Convention hygiene: PASS (word count, dashes, "at least N", tool names, method-lock, schema all clean)

Corrected materialization is ready. Originals `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` remain untouched — they are the artifact FEEDBACK will rate against QC spec baseline.
