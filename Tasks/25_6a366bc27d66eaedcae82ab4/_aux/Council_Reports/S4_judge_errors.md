# Bucket 2 — Judge Errors

## Confirmed judge errors

None confirmed against the trajectories with confidence.

## Soft-confidence candidate (advisory only, do not appeal)

### Run 2 — "Adds an accept-timing variance explanation entry to BL-75810CD0FEE4, leaving the existing partial-feed variance explanation in place" — judge marked Fail

The judge's own justification reads: "it's unclear from the trajectory whether the existing partial-feed explanation was left in place or overwritten ... Given the ambiguity, I score this 0.0." The same rubric was marked Pass in Run 1, Run 3, and Run 5, all of which also called `blackline_update_reconciliation_variances` on BL-75810CD0FEE4 without submitting / approving / certifying. The Run 2 trajectory likely satisfies the rubric on the same evidence basis as Runs 1 / 3 / 5, but the judge defaulted to Fail under uncertainty rather than walking the parameter payload.

Action: do NOT appeal this single judge call. The 5/6 fail majority on this rubric is dominated by Run 4 (recon was submitted) and Run 6 (single-element array likely replacing the existing entry) — both legitimate failures — so even a flipped Run 2 would only move the rubric to 4/6 pass, not 5/6.

## All other failing rubrics

Every other failing rubric across the six runs was a legitimate model failure (Bucket 3). The judges read the trajectories correctly: missing tool calls, wrong thread_ts, missing CC, wrong tool variant (add_document_version vs upload_document), wrong claim ("posted" vs "staged"), and missing analytical content (the doppelganger record, the exception update).
