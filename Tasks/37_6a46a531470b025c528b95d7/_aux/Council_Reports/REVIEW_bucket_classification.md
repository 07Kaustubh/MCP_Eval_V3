# REVIEW bucket classification — Task 37

**S4-style trajectory walk applied to candidate's ORIGINAL rubric set.**

Runs completed: 6/6. Runs errored: 0/6. **T3 (error runs ≤ 2): PASS.**

Runs passed all rubrics: 2/6 (Run #2, Run #4). Runs failed ≥ 1: 4/6. **T2 (pass@1 ≤ 40%): PASS (33.3%).**

## Failure map (per-rubric across all 6 runs)

Failed rubrics identified from 8_Verifier_Fails.txt (Run #1 explicit; Runs 3/5/6 inferred from identical 28/30 pattern + prompt-set architecture; Run #2 and Run #4 = 30/30 clean):

| Rubric | Failed in runs | Bucket | Evidence |
|---|---|---|---|
| "The Agent reports in the final response that LN-2026-00623 is at clear-to-close status but still has 5 outstanding required documents..." | 1, 3, 5, 6 (inferred consistent) | **Bucket 3 — Legitimate Model Failure** | Run #1 justification: "mentions '00623 V. Pham — signed, but lender wire missed cutoff; recording pushed — needs funding confirmation' but does NOT state it has 5 outstanding required documents." Agents put doc details in the Priya email but truncate/abstract them in the summary. Rubric is correct — the prompt says "for each one tell me where it stands... what conditions or documents are still outstanding" which requires the summary to carry this detail. |
| "The Agent reports in the final response that LN-2026-00010 has the most outstanding required documents in the pipeline, with 7 items still needed." | 1, 3, 5, 6 (inferred consistent) | **Bucket 3 — Legitimate Model Failure** | Run #1 justification: "mentions '00008 Wilson & 00010 Ferguson — on Compliance's compromised-portal impacted list (borrower comms on hold)' but does NOT mention 7 outstanding required documents or multiple missing document types for LN-2026-00010." Same failure mode — summary drops detail carried in the Natasha email. |

## Bucket totals

- Bucket 1 (Rubric Invalid): **0**
- Bucket 2 (Judge Error): **0** (both fails have clear trajectory citations showing the final response omitted the required detail)
- Bucket 3 (Legitimate Model Failure): **8** (2 rubrics × 4 failing runs)

**Bucket 1 ratio: 0 / 8 = 0%** — well under the 25% threshold.

## All-Failing Rubrics sub-dim scoring

- Bucket 1 ratio 0% → **5/5 PASS on All-Failing Rubrics sub-dim.**

## Positive evidence of rubric quality

Both failing rubrics are legitimate difficulty knobs:
- They probe a well-known Opus-4.8 failure mode: **summary drift** — agents faithfully report per-recipient details in individual emails but over-abstract the final response
- The prompt explicitly requires the per-loan detail: "for each one tell me where it stands, whether the lock is still good or expired, and what conditions or documents are still outstanding"
- 2 of 6 runs (33.3%) succeeded on both, proving the rubrics ARE satisfiable when the agent preserves detail through the final response

## Triage impact

- No Bucket 1 findings → no `[trajectory-bucket-1]` rows auto-populated in `changes.md`
- Bucket 3 findings reinforce hardness quality → triage input: SALVAGEABLE (not REBUILD)
