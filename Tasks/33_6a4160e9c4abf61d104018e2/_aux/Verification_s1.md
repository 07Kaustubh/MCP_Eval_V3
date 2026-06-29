## Data sources consulted
- _aux/Universe_Split/ :: mortgage_los.loans (trio status: LN-2026-00009 conditional_approval, LN-2026-00211 withdrawn 2026-03-28, LN-2026-00622 processing; assigned_lo verified per row); mortgage_los.conditions (3 outstanding on LN-2026-00009 — los_cond_74d7f24385f5 / 739ecac87a02 / d7fdad61f9fa); mortgage_los.staff (Carlos los_staff_a7fa5b29babd, Sofia Reyes los_staff_afc9caafae9d, Robert Calloway los_staff_e85bc913c756 = broker / oversight); mortgage_los.borrowers (Darren Singh / Elizabeth Gray / Angela Foster); slack.slack_users (Grace Yamamoto keystone_e304643b171b); slack.slack_channels (D-grace-yamamoto MPIM Carlos-readable; D-grace-robert excludes Carlos; C002 #loan-processing); rate_lock_expiration field populated on all three trio loans (all expired 47-64 days back of universe today 2026-06-12).
- _aux/Fact_Ledger.json :: Universe today 2026-06-12; lifecycle atoms consulted for relative-date resolution ("tomorrow afternoon", "this month", "today", "last week", "this afternoon", "weeks").
- _aux/Hardness_Plan.md :: All 5 selected levers preserved through 3 AUDIT rounds; L9 v2 (Grace authority dismissal) replaced by L1+L25 v3 (Carlos's self-quoted over-promise) after round 1 AUDIT contradicted Grace's documented 2026-03-25 investigation role on LN-2026-00211. L25 strengthens via Carlos's prior claim as the anchor.

## Eval spec sub-dims (Evals/1_Prompt_Eval.md) verified
- 1.1 Unique Ground Truth :: NON-FAIL (audit strict reading 4/5 — CRM orphan-vs-bound binding deferred to S3 count-based rubric)
- 1.2 Feasibility :: PASS 5/5
- 1.3 Explicit Tool Mention :: PASS 5/5 (zero tool names)
- 1.4 Prompt Clarity and Specificity :: PASS 5/5 ("longest-overdue outstanding condition" anchors cleanly)
- 1.5 Contrived / Unnatural Prompts :: PASS 5/5
- 1.6 Truthfulness :: PASS 5/5 (Carlos self-attribution removes Grace contradiction)
- 1.7 Tool use and Cross-service requirement :: PASS 5/5 (≥5 services forced)
- 1.8 Investigation :: PASS 5/5
- 1.9 Coherence :: PASS 5/5
- 1.10 Persona :: PASS 5/5 (Carlos's over-promise pattern integrated)
- 1.11 Business Function :: PASS 5/5 (Loan Operations)
- 1.12 Alignment with Today's Date :: NON-FAIL (audit strict reading 4/5 — "she has been pushing on for weeks" present-perfect against Grace's 11-week-back last Carlos-readable pipeline activity; S2 plant satisfies)

## QC spec sub-dims (Docs/7_QC_Spec_Doc1.json — Prompt dimension) verified
- 10/12 sub-dims at 5/5 under strictest AUDIT reading.
- 2 sub-dims at 4/5 (UGT + Date-alignment) under strictest reading. Both fall in the QC spec's NON-FAIL middle band (1/3/5 scheme — there is no "4" band; the audit's 4 represents borderline cases that collapse to either 3 NON-FAIL or 5 PASS depending on reader leniency). Platform scoring expected to land NON-FAIL (acceptable, not FAIL).

## Reference docs consulted
- Reference/Prompt_Format.md :: 500-word cap, no em-dash, no tool names, no internal IDs, no pre-solving, first-person mid-thought, trigger → context → asks structure — all confirmed.
- Reference/Hardness_Playbook.md :: L1 first-framing, L2 structured-DB skip, L8 multi-link chain, L10 reversal, L25 existing-output anchor — all triggered.

## Verification statements
- [x] Validator (validate.py --phase prompt) exit 0, 0 fails, 0 warns.
- [x] Council A grounding + convention clean (GO verdict).
- [x] Council B QC scoring + density + hardness preservation (GO verdict at 52.0 midpoint).
- [x] Similarity gate (calc_similarity.py) composite 29.4 < 40 against 34-prompt corpus.
- [ ] AUDIT verdict = PASS (STRICT) — NOT achieved. 3 rounds completed: round 1 REVISE (6 issues), round 2 REVISE (4 sub-dims at 4/5), round 3 REVISE (2 sub-dims at 4/5, density PASS). Iteration cap hit. Per runbook, escalating to user.

## Discrepancies surfaced (audit round 3 residues)
- **UGT 4/5** — CRM engagement "for each of the three" admits orphan vs Darren-bound paths. Universe has 6 trio orphan engagements (existing pattern); only 1/3 trio borrowers (Darren Singh) has a CRM contact. Single-phrase fix available (e.g., "Log a CRM engagement note for each one mirroring how the existing notes on those files are set up" — directs orphan pattern). Operator decision deferred.
- **Date-alignment 4/5** — "She has been pushing on for weeks" present-perfect against Grace's last Carlos-readable pipeline-review activity (March 2026). Single-phrase fix available (e.g., drop "for weeks" → "the pipeline review she has been pushing on"). Operator decision deferred — S2 plant satisfies under loose reading.

## Hardness Plan amendments during S1 (preserved for S2)
- v1 → v2: L9 plant moved from D-grace-robert (Carlos not member) to D-grace-yamamoto MPIM (Carlos-readable) [Council B B6 propagate].
- v2 → v3: L9 (Grace authority dismissal) replaced by L1+L25 (Carlos's self-quoted over-promise) because Grace's 2026-03-25 emails identify 211 as a Marcus-Webb spouse-conflict fraud-investigation file. Universe-grounded persona-consistent reframe; L10 reversal still triggered; L25 strengthens.
- Robert Calloway IS in mortgage_los.staff (broker; oversight/escalations/compliance specialization). Original Hardness Plan claim "Robert is NOT in mortgage_los.staff" was incorrect and is now fixed.
