# S4 — Bucket 1 (Rubric Invalid) fixes

## Fix 1 — Rubric #25 (precedent retrieval) — platform data-state contradiction

**Affected file:** `Tasks/30_6a3de5194c34125ef86fb36f/15_Updated_Rubrics.json`, rubric titled "The Agent retrieves the content of an existing Acme Cloud AML precedent memo (either the Beneficial Owner Refresh or the AML Risk Assessment) from the Records Vault."

**Trajectory citation:**
- Run 1, tool call 1 of 2 (`Run1_Trajectory.json` ~line 2594): `records_vault_download_document_content {document_id: "doc_38a8236a0c4546e2", actor_role: "compliance_officer"}` -> `{"success": false, "error": "version 1 not found for doc_38a8236a0c4546e2", "code": "IMG.VERSION_NOT_FOUND"}`.
- Run 1, tool call 2 of 2 (`Run1_Trajectory.json` ~line 2659): same call on `doc_fb028c9124e146c5` -> identical failure.
- Same exact failure reproduced in Run 2, Run 3, and Run 6 with `actor` parameter variations that do not change the outcome.
- Preceding evidence (Run 1 `records_vault_get_document` on the same doc, ~line 2960): `{"id": "doc_38a8236a0c4546e2", "kind": "memo", "title": "Acme Cloud FY2026 AML Risk Assessment Memo", "current_version": 1, "version_count": 1, "status": "active"}`. The metadata layer reports the version exists; the content layer denies it.

**Reasoning:** The rubric as currently written cannot be satisfied by any agent under strict reading. The platform's metadata subsystem and content subsystem disagree on whether version 1 of these two seeded AML memos exists. R1 and R2 judges enforced the strict reading and marked the rubric FAIL. R3/R4/R5/R6 judges accepted the well-formed call attempt as satisfying the rubric and marked PASS. The verifier output is therefore noise rather than signal for this rubric.

The two paths forward are (a) remove the rubric, or (b) rewrite it to score on the discovery attempt (which is the substantive behavior the rubric was meant to test). Option (b) preserves the lever and matches the lenient judge interpretation that 4 of 6 graders already applied.

**Before** (verbatim from `15_Updated_Rubrics.json`):

> title: "The Agent retrieves the content of an existing Acme Cloud AML precedent memo (either the Beneficial Owner Refresh or the AML Risk Assessment) from the Records Vault."
>
> evidence: "A records_vault_download_document_content tool call in the trajectory targeting the FY2026 BO Refresh memo OR the FY2026 AML Risk Assessment memo, returning a successful response."

**After:**

> title: "The Agent attempts to retrieve the content of an existing Acme Cloud AML precedent memo (either the Beneficial Owner Refresh or the AML Risk Assessment) from the Records Vault."
>
> evidence: "A records_vault_download_document_content tool call in the trajectory with document_id set to doc_38a8236a0c4546e2 (FY2026 AML Risk Assessment Memo) or doc_fb028c9124e146c5 (FY2026 Beneficial Owner Refresh). The platform's content layer may return either a successful payload or an IMG.VERSION_NOT_FOUND error for these seeded documents; both responses satisfy the rubric provided the agent's call is well-formed (correct tool, correct document_id, role authorised to read restricted AML memos)."

**What this does:**

- Removes the platform-bug dependence: the rubric now scores on agent behavior (attempting precedent discovery) rather than on a content-payload the platform will not serve.
- Matches what R3/R4/R5/R6 graders already did, so re-running the verifier should produce uniform PASS across all runs that made the call.
- Preserves the underlying hardness intent: the agent must still know to look up the precedent memos before drafting the disposition memo. Rubric #26 (memo references the precedent) still gates whether the agent did substantive work with what it discovered.

**No information loss for the grader.** The two document IDs are still named verbatim in evidence. Pass/fail behavior changes only for the platform-bug case that the rubric should not be testing.

## Out-of-scope

No other rubrics require Bucket 1 fixes. Rubric #13 (Marina coordination) and rubric #26 (memo references precedent) are correctly written — see `S4_AF_justifications.md`.
