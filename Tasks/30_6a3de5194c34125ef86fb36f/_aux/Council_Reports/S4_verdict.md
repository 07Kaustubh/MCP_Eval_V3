# Verifier Fails — S4 verdict (Task 30_6a3de5194c34125ef86fb36f)

Empirical input: 6 of 6 runs evaluated. pass@1 = 0.333 (2/6 PASS clean). Avg total tool calls = 47.2 (density OK, >= 40 floor). Parse verdict from `Validators/parse_trajectories.py`: OK.

## Run x failing-rubric matrix

| Failing rubric (short) | R1 | R2 | R3 | R4 | R5 | R6 | Total fail |
|---|---|---|---|---|---|---|---|
| Retrieves precedent memo content from Records Vault (rubric #25 in `15_Updated_Rubrics.json`) | FAIL | FAIL | pass | pass | pass | pass | 2/6 |
| Identifies Marina Soko CDD coordination stage in memo body (rubric #13) | FAIL | FAIL | pass | FAIL | FAIL | pass | 4/6 |
| Memo references firm's existing AML precedent for Acme Cloud (rubric #26) | pass | FAIL | pass | pass | pass | pass | 1/6 |

All other 23 rubrics passed in every completed run.

Per-run totals match the platform verifier output: R1 24/26, R2 23/26, R3 26/26, R4 25/26, R5 25/26, R6 26/26.

## Classifications

- **Bucket 1 (rubric invalid):** 1 rubric -> see `S4_fixes.md`.
  - **Rubric #25 (precedent retrieval)** — platform data-state contradiction (metadata reports `current_version: 1, version_count: 1, status: "active"` but content layer returns `version 1 not found` for both seeded AML memos). No well-formed call signature can satisfy the rubric under strict reading. Confirmed across R1, R2, R3, and R6 trajectories — all download attempts on `doc_38a8236a0c4546e2` and `doc_fb028c9124e146c5` returned identical `IMG.VERSION_NOT_FOUND`.

- **Bucket 2 (judge error):** 1 rubric x 4 runs of inconsistent grading -> see `S4_judge_errors.md`.
  - Same rubric #25. R3, R4, R5 judges accepted the failed-call attempt as satisfying "retrieves the content". R6 judge explicitly hallucinated "both returning successful responses" when the trajectory shows the same `IMG.VERSION_NOT_FOUND` failure (verified at `Run6_Trajectory.json` line 3801). R1 and R2 judges read the rubric strictly (call must succeed) and marked FAIL. Grader inconsistency on identical evidence.

- **Bucket 3 (legitimate AF):** 2 rubrics -> see `S4_AF_justifications.md`.
  - **Rubric #13 (Marina coordination)** — 4 of 6 runs put Marina only as "Prepared by:" or `uploaded_by` (authorship), which the rubric explicitly disqualifies as a fail example. The Hardness_Playbook lever (Row 6 in `changes.md`) is working as designed.
  - **Rubric #26 (memo references precedent)** — R2 produced a disposition memo with no reference to the BO Refresh or AML Risk Assessment memo. Direct consequence of the failed precedent download (Bucket 1) plus the agent not falling back on the catalog metadata it had already retrieved.

## Hardness calibration

`Hardness_Plan.md` does not exist for this task (REVIEW-flow, not CB-flow — no S0/HARDNESS phase ran). Calibration is therefore against the levers documented in `changes.md` Row 6, Row 8/9, and Row 12:

| Lever (from changes.md) | Predicted to fail | Actually failed | Calibration |
|---|---|---|---|
| Marina coordinator-role inference (Row 6) | yes (single load-bearing hardness lever, 5/6 expected) | yes (4/6) | hit — slight under-prediction |
| Email subject contains JE id (Row 8/9 added via REVIEW2) | yes (lever 2, expected partial fail) | no (0/6 — all runs nailed it) | over-predicted — lever weaker than hoped |
| Precedent linkage (Row 12 added via AUDIT_all composite fix) | yes (lever 3, expected partial fail) | partial (rubric #25 platform bug + rubric #26 1/6) | under-predicted on rubric #25 (platform issue, not model), correct on rubric #26 |

Lessons for next task: when a hardness lever depends on the platform actually serving Records Vault content for an existing seeded document, smoke-test the `records_vault_download_document_content` call against that exact document during S0/Universe verification before promoting the lever into a rubric. The metadata layer reporting `current_version: 1` is not sufficient evidence that the content endpoint will serve it.

## Action items

- **Bucket 1 fixes** — apply rubric #25 rewrite from `S4_fixes.md` to `15_Updated_Rubrics.json` so the rubric scores on the attempt rather than on a content-payload success the platform won't deliver. Rerun the platform verifier.
- **Bucket 2 — judge errors** — log inconsistency for platform team; no client-side fix (graders are out of scope for this pipeline).
- **Bucket 3 — ship AF justifications** — submit `S4_AF_justifications.md` to the platform reviewer as documented hardness for rubrics #13 and #26. Both are legitimate model failures, not rubric defects.
