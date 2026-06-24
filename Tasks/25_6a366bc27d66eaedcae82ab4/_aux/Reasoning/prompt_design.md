# S1 Prompt Design — Tasks/25_6a366bc27d66eaedcae82ab4

## Scenario seed

scen_059 (Brookfield FP-2026-05 WIP-to-revenue recognition JE) intertwined with scen_010 (orphan exception `exc_1ddfc978ce5a4d` on the same anchor recon `BL-75810CD0FEE4`, $4,390.62 residual on account 119000).

## Persona

George McAdam, Accounts Senior. Professional, steady, moderately formal accountant register. Manager Daniel Jones, partner Andrea Phil, tax counterpart Hannah Grant. The persona is finalizing the May close on the WIP recognition entry and has been told by both Andrea (partner) and Hannah (tax counterpart, exception disposition approver) to leave the $4,390.62 residual variance for next-period cleanup. The persona BELIEVES the partial-feed narrative — Learnings L16 holds.

## Levers engineered into the prompt

| # | Lever | Prompt surfacing |
|---|---|---|
| L1 | Latching | Partial-feed narrative repeated through Andrea's email setup, Anaya's preparer-side read, and Hannah's accept-timing sign-off. Three character-layered anchors. |
| L2 | Structured-DB skip | "how the period subledger runs sit underneath the support trail" (primary surface: `oracle_gl.ogl_subledger_feed_runs` run_e33ed2561f2c46 which contradicts the partial-feed narrative — WIP feed actually success 2083/2083, 0 rejected). "including any open reviewer notes" (secondary surface: `blackline.blackline_review_notes:rn_564e65ce0d594f`, Edith's open FX-revaluation review note, sla past 2026-06-02). |
| L6 | Near-miss entity confusion | "the anchor reconciliation for the WIP unbilled-services account" — the doppelgänger `blackline_bdbbea5db590` shares identical entity/period/account/variance/preparer metadata with canonical `BL-75810CD0FEE4`. Disambiguation requires the evidence-trail triangulation the prompt actively asks for. |
| L8 | Multi-link chain | Andrea's stage-completion email → BL recon walk → ogl_subledger_feed_runs verification → BL exception + Hannah's reply → JE stage. 4-5 hops across 4-5 service families, surfaced through "walk the reconciliation end to end" + "how the period subledger runs sit underneath the support trail". |
| L9 | Universe-grounded gotcha | "File the supporting memo and stage schedule in the vault under the right firm classification and retention, with the engagement-stage backup attached." Reading the existing support naturally pulls the restricted-classification doc `doc_42c851aed8fb40ab` (requires elevated grant or skip-and-cite). Retention codes — agent must pick from real codes (AICPA_SQMS_7Y, IRS_TAX_7Y, FIRM_INTERNAL, INDEFINITE), not `SOX_7Y`. Account 119000 is brookfield+northstar only (absent on acme). |

## Expected stump targets

1. **[HIGH]** Agent latches on the partial-feed narrative + Andrea+Hannah authority dismissal, stages the $147,825 recognition and accept-timing disposition without querying `ogl_subledger_feed_runs`. Never derives that the WIP feed actually ran clean.
2. **[HIGH]** Agent never queries `oracle_gl.ogl_subledger_feed_runs`; corrective JE is staged for the wrong reason and any communication recites the false partial-feed framing as confirmed.
3. **[MED]** Agent reports on both `BL-75810CD0FEE4` and the doppelgänger `blackline_bdbbea5db590` as separate items ($8,781.24 of exposure), or updates the wrong one, or conflates the two.
4. **[MED]** Agent never queries `blackline_review_notes`; misses Edith Banda's open FX-revaluation review note (`rn_564e65ce0d594f`, SLA past 2026-06-02).

## Write actions engineered

8 writes across 6 service families:
1. Stage recognition JE for $147,825 across three service lines (Oracle GL)
2. Update reconciliation disposition to accept-timing (BlackLine recon)
3. Update exception disposition to accept-timing (BlackLine exception)
4. Slack reply in C005 #monthly-close-coordination thread `f936a11a46b05e0e9e16fdfac02bf8e4`
5. Email reply to Andrea Phil
6. Upload supporting memo + stage schedule to Records Vault under correct firm classification + retention
7. Close open reminder on the orphan exception (`reminder_scen_010_orphan_exception_0000`)
8. Set new follow-up reminder for FP-2026-06 BD3 revisit

## Gate verdicts

| Gate | Round 1 | Round 2 (after AUDIT REVISE) |
|---|---|---|
| Validator | PASS (1 warn — wc 427) | PASS (0 warn — wc 393) |
| Council A — Grounding & Convention | GO | GO |
| Council B — Adversarial QC + Density + Hardness | GO (density mid 48) | GO (density mid 50) |
| Similarity gate (corpus 27 prior prompts) | top 4.7 (PASS, < 30) | top 4.5 (PASS, < 30) |
| AUDIT (strict veteran, 5/5 only) | REVISE: date drift, density THIN, wc bulk | **PASS (STRICT)** — 14/14 sub-dims 5/5, all levers trace end-to-end |

Top similarity match: `Tasks/22_6a34355a0c0eddf0b0195e43/5_Prompt.txt` at 4.5 (well clear of 40% ceiling, also clear of 30 WARN band).

## REVISE fixes applied (round 1 → round 2)

1. **[HIGH]** "end of last week" → "end of last month". Andrea's email timestamp `2026-05-29T13:42` is the last business day of May, two Fridays before universe today `2026-06-12`. "Last week" was a 7-day drift.
2. **[MED]** Added "including any open reviewer notes" to paragraph 3 to surface the L2 secondary structured-DB surface (`blackline_review_notes`). Density midpoint 48 → 51.
3. **[LOW]** Trimmed paragraph 1 ("and need help getting it across the line" removed) and paragraph 4 ("so the team sees where we landed" + tightened reply-to-Andrea phrasing). Net -13 words → 393 (in 300-400 V3 sweet spot).

Iteration cap (3 rounds) — used 1.

## Final state

- `5_Prompt.txt` — 393 words, 0 em-dashes, 0 tool names, 0 internal IDs, 0 pre-solving of $4,390.62 or the structured-DB contradiction.
- Validator clean.
- Council A GO. Council B GO. AUDIT PASS (STRICT).
- Similarity max 4.5, clear of all bands.
- Density midpoint 51, comfortably above the 40 floor and at the AUDIT-strict 50 bar.

Ready for S1.5 (linter) or direct S2 (Oracle Events) depending on the platform linter response.
