# Prompt Design Reasoning — S1

## Anchor

Anchor A from `_aux/Hardness_Plan.md`: NorthWind / Emilia Cruz piano damage operational docket. Blessing Okafor (Relocation Coordinator) must close out the operational damage docket on/around 2026-04-26 (universe today) while the $1,200 KeyMove insurance rider (`BILL-KEYMOVE-2026-0417`, DueDate 2026-04-24) sits on the QB books with Marcus Thorne's Apr 17 email (`email_99e10a978b48`) framing it as a finance-clean disposition.

## Levers engineered into the prompt

| # | Lever | Prompt sentence that surfaces it |
|---|---|---|
| L1 | Latching | "The KeyMove insurance rider for the Steinway scratch came through our books last week. Marcus already weighed in on the finance side. His read is we process it as submitted because the vendor paperwork lines up with the field report, and there is no clean argument to dispute it on the vendor line. Fine. I am not going to relitigate the rider with him. That part is in his lane." |
| L2 | Structured-DB skip | "I keep thinking about how we structured the Mosaic case last quarter, where the carrier exposure was one piece and the client facing piece was a separate disposition with its own treatment, and we attached a process improvement section to the file afterward." + "Update Emilia's relocation record so it reflects both sides of the disposition." |
| L7 | Multi-write diversification | 6 writes / 5 services: email Craig, email David+Catalina, airtable update, Slack post, Linear comment, reminder for Monday. |
| L8 | Multi-link chain | Craig Apr 11 → Marcus Apr 17 → Catalina Apr 14 commitment ("Catalina is pulling something together on the NorthWind side") → Linear retention issue ("There is already a Linear item open for the wider NorthWind situation") → Pam Apr 24 (derive-required, not echoed in prompt per L15 anti-leak). |
| L11 | Net-vs-gross framing | "The rider closes one ledger line. It does not close out the rest of this." + "I do not have authority on the client facing piece." |

## Stump targets (per Hardness_Plan, confirmed preserved by Council B-B2 and AUDIT LENS 5)

1. **[HIGH]** Agent stops at "approve the $1,200 rider" and never files the customer-side docket — Lever 1 + Lever 11.
2. **[HIGH]** Agent never queries Airtable for Emilia row AND never queries `bill_mosaic_damage_accrual_001` for precedent — Lever 2.
3. **[MED]** Agent posts ops lesson to wrong Slack channel (#customer-engagement C002 or #finance C005) instead of #operations C006 — channel-lockin minor risk softened via "Chloe and the ops team" phrasing.
4. **[MED]** Agent emails Craig but does not answer his Apr 11 formal-claim-or-hold question — Lever 3 (adjacent missing-reply mechanism).

## Council verdicts

- **Validator** `validate.py --phase prompt` :: PASS (0 fails, 0 warns, 6 notes).
- **Council A** (explore sub-agent, 8 active perspectives) :: GO. 2 MINOR A3 non-blocking notes (Chloe verbal ask grounded by manager-to-direct-report relationship; "overnight" → "last week" fix applied pre-emptively to defuse temporal-stretch flag).
- **Council B** (oracle sub-agent, 5 active perspectives for prompt phase) :: GO. All 12 QC sub-dims 5/5. Three alt-paths classified INTENDED_HARDNESS_NOT_CLARITY_FAIL. THIN_DENSITY 47-midpoint accepted per Hardness_Plan operator continuation justification. All 5 levers preserved. Zero upstream propagation flags.

## Similarity

`calc_similarity.py` :: max composite **27.4** vs prior-task corpus (35 prompts). Top match: QC_Tasks/V3_Tasks/Task14 at 27.4 (raw lex 27.4, multiplicative weighting 1.000). Well under the 40 ceiling — no PIVOT required.

## AUDIT (STRICT, auto-fired per Track F v21 trigger (e): prompt revised in this S1 pass)

Verdict: **PASS (STRICT)**. All 7 active lenses pass (LENS 6/9 retired per v18). Per-atom evidence table 11/11. Leakage sweep clean. All 5 levers trace end-to-end with cited prompt-sentence evidence. 48/48 regression anchors PASS. Two non-blocking forwards recorded (validator stale-date code bug for separate ticket; density monitor for first platform trajectory cycle).

## Final prompt stats

- Word count: 380
- Distinct services referenced: 3 explicit (Slack, Linear, email) + 2 implicit (Airtable via "relocation record"; reminders via "Remind me Monday")
- Em-dashes / en-dashes: 0
- Tool names: 0
- Internal IDs: 0
- Top similarity composite: 27.4

## Operator notes for downstream phases

- S2 OE drafting must preserve the 6 writes / 5 services mapping. The L8 chain Craig→Marcus→Catalina commitment→Linear retention issue→Pam-derive-required must be encoded as a 5-link OE traversal.
- S3 Rubrics must include atomic Outcome rubrics per Hardness_Plan stump targets 1-4. Stump 3 (channel choice) is a candidate Outcome 1.1 rubric — Slack post landing on #operations C006 specifically, NOT C002 / C005.
- FINAL must re-verify L29 escape-valve mitigation (prompt does not echo Marcus's customer-side flag).
