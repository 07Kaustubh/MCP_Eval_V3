# S4 — Bucket 2 (Judge Error) log

## Judge error 1 — Rubric #25 (precedent retrieval) — inconsistent grading across runs

**Affected rubric:** "The Agent retrieves the content of an existing Acme Cloud AML precedent memo (either the Beneficial Owner Refresh or the AML Risk Assessment) from the Records Vault."

**Inconsistency:** The same trajectory pattern (a `records_vault_download_document_content` call returning `IMG.VERSION_NOT_FOUND`) was graded FAIL in some runs and PASS in others.

**Per-run trajectory citations and judge verdicts:**

- **Run 1 FAIL** (judge applied strict reading) — `Run1_Trajectory.json` ~line 2594-2659: two `records_vault_download_document_content` calls on `doc_38a8236a0c4546e2` and `doc_fb028c9124e146c5`, both returned `{"success": false, "error": "version 1 not found", "code": "IMG.VERSION_NOT_FOUND"}`. Judge justification: "Both records_vault_download_document_content calls for doc_38a8236a0c4546e2 and doc_fb028c9124e146c5 returned 'success: false' with error 'IMG.VERSION_NOT_FOUND'."

- **Run 2 FAIL** (judge applied strict reading) — `Run2_Trajectory.json` ~line 2923-2989: identical call shape, identical failure. Judge justification: "both calls FAILED ('version 1 not found'). The criterion requires a successful response, which was not achieved."

- **Run 3 PASS** (judge applied lenient reading) — `Run3_Trajectory.json` ~line 2975: one `records_vault_download_document_content` call on `doc_38a8236a0c4546e2`, same `IMG.VERSION_NOT_FOUND` failure. Judge justification: "The trajectory shows a records_vault_download_document_content tool call targeting document_id doc_38a8236a0c4546e2 (FY2026 AML Risk Assessment Memo), not merely listing documents." — judge did not check `success`.

- **Run 4 PASS** (judge applied lenient reading) — same call pattern. Judge justification: "satisfying the requirement" — judge did not check `success`.

- **Run 5 PASS** (judge applied lenient reading) — same call pattern. Judge justification: "both precedent memos retrieved" — judge did not check `success`.

- **Run 6 PASS** (judge hallucinated success) — `Run6_Trajectory.json` line 3761 and 3827 contain the calls; line 3801 contains the response `{"success": false, "error": "version 1 not found for doc_38a8236a0c4546e2", "code": "IMG.VERSION_NOT_FOUND"}`. Judge justification claims: "both returning successful responses." The trajectory contradicts the judge's claim — Run 6 did NOT have successful responses on these calls.

**Impact:** Pass@1 was reported as 0.333 (2/6). If the lenient reading had been applied uniformly, Run 1 and Run 2 would also have scored PASS on rubric #25, raising pass@1 to ~0.667 — well over the 40% threshold and the task would have failed difficulty. If the strict reading had been applied uniformly, pass@1 would drop to ~0.0 on this rubric across all 6 runs, but in fact the only blocker per run would have been rubric #13 (Marina). Either way, the inconsistency means the per-run scores cannot be compared to each other.

**Recommended platform-side action:** flag rubric #25 graders for inconsistency review; either harmonise on "call attempt is sufficient" or harmonise on "call must succeed" — but apply the same rule across all six runs.

**Client-side action:** apply the Bucket 1 fix in `S4_fixes.md` to rewrite the rubric so the strict-vs-lenient ambiguity disappears. After the fix is shipped, this judge inconsistency will be moot.

## No other judge errors detected

The Marina coordination judge verdicts (rubric #13) are consistent across all six runs against the trajectory evidence:
- R1, R2, R4, R5 FAIL — verified that the memo content in each of these runs lists Marina only as "Prepared by:" / `uploaded_by`, matching the rubric's explicit fail example.
- R3, R6 PASS — verified that the memo content includes "Compliance coordination: Marina Soko" in the approval chain, matching the rubric's explicit pass example.

The precedent-references judge verdict (rubric #26) is consistent for the one fail (R2 — memo had no precedent references in body, confirmed; the agent could not include them because the precedent downloads failed).
