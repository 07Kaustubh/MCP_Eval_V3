# REVIEW — Hardness assessment

**Task:** 29_6a3df3eff98a736992ef76fe
**Universe today:** 2026-06-12 (US/Eastern)
**Source:** **measured** (6 trajectories present in `trajectory-runs/`).

## Measured numbers (from `_aux/Trajectory_Stats.json`)

| Metric | Value | Project gate | Verdict |
|---|---|---|---|
| Avg total tool calls | **55** | ≥ 50 design target / ≥ 40 floor | **PASS** (above design target) |
| Avg MCP tool calls | 40 | — | informational |
| pass@1 (rubric-perfect runs) | **33.3 %** (2 / 6) | ≤ 40 % | **PASS** |
| Error rate | 0 / 6 | < 3 erroneous runs | **PASS** |
| Per-run totals | 55, 51, 81, 47, 52, 44 | — | all individually above 40 floor |

## Per-run rubric pass count

| Run | Rubrics passed | Notes |
|---|---|---|
| 1 | 17 / 17 | clean |
| 2 | 16 / 17 | missed reminder_delete on the moot AML threshold reminder |
| 3 | **6 / 17** | agent misread the universe and reported the review as OPEN / incomplete despite the email chain showing both clearances on record — the prompt's disposition-trust lever (L1 inverse) fired hard |
| 4 | 15 / 17 | missed reminder_delete; final response did not name Farah on counterparty/SOF work |
| 5 | 17 / 17 | clean |
| 6 | 16 / 17 | missed reminder_delete |

## Observed hardness levers (working as designed)

1. **Reminder-delete trap** — `reminder_scen_041_audit_compliance_0000` is still active and instructed completing the review, but both clearances landed by 2026-04-30 so it is moot. Prompt says "deal with it rather than simply flag it." **4 / 6 runs missed the delete call** (runs 2, 3, 4, 6) — the strongest single discriminator on this task. Maps to Learnings L5 inverse (action-incompleteness traps usually fail, but here it works because the delete is OUT of the obvious "ship the close-out" action loop).

2. **Slack-chatter vs structured-calendar contradiction** — the closing Slack message in C008 (msg `ca6b3a86…`, 2026-05-04) asserts "FY26 calibration session is now on the calendar for 2026-06-18." The actual calendar event `event_scen_041_audit_compliance_0011` is dated **2026-06-03** (already passed by today 2026-06-12) and there is NO event on 2026-06-18. The OEs make this the load-bearing lever for the "schedule next-cycle review" rubric (R13), and 6 / 6 runs correctly placed a future event — but they ranged 2026-09-03 → 2027-06-16, showing the structured-calendar check was done by each.

3. **Classification mirroring** — comparable Acme AML docs (`doc_38a8236a0c4546e2`, `doc_fb028c9124e146c5`) are `classification=restricted`; the routine `journal_entry_support` doc on the SAME JE (`doc_770062b1b39b4c41`) is `classification=internal`. The prompt forces mirroring the AML records, not the default. All 6 runs passed — non-discriminating on this task but the rubric still blocks the bad path.

4. **FFIEC_5Y decoy** — email 0008 cites the wire confirmation as "kind: bank_statement; retention: FFIEC_5Y." FFIEC_5Y is NOT a valid retention code in this universe (valid codes: AICPA_SQMS_7Y, IRS_TAX_7Y, FIRM_INTERNAL, INDEFINITE). All 6 runs ignored the decoy and used a valid kind (memo / audit_evidence) — rubric R3 blocks the wrong path even though no rubric explicitly tests retention. Working as designed.

5. **Disposition-trust inverse** — the prompt tells the agent supervisory + partner clearance are both in and disposition is settled, then forces verification of the record. Run #3 over-investigated, concluded the review was open, and cascade-failed 11 of the 17 rubrics. This is a low-rate but high-magnitude lever (1 / 6 runs).

## Verdict

**Measured hardness PASSES both project gates** (density ≥ 40 floor / ≥ 50 design target; pass@1 ≤ 40 %). Task is not a REBUILD candidate on hardness grounds. Proceed to QC scoring.
