# Rubric Fixes (Bucket 1) — Task 26_6a390e724c34487b95645dcc

**Bucket 1 count: 0.**

Every failing rubric was checked against the strictest reading and grounded in a concrete fact the per-task universe carries. None require rewording, splitting, removal, or process-rubric conversion. The shipped `7_Rubrics.json` stays as-is.

Notes on rubrics considered but kept:

- **af1b8d45** (memo content $4,820.30 + 230000/103000 trace) bundles three facts in one rubric. The bundling is consistent with the per-task convention of "atomic on the artifact under test" — the memo body is the one artifact, and the rubric's "or similar" softener is absent because the trace is the audit point. Strict reading keeps the bundle.
- **b02c9e56** (memo refs William's email + posted JE id+entry_number) bundles two identifiers in one rubric. The bundling mirrors the V3 reference voice for audit-anchor rubrics (the two ids are the same lookup pair from the auditor's perspective). Strict reading keeps the bundle.
- **c79d65bd** (Linear comment, with create-then-comment fallback) is strict on the linear_create_comment call. Run 5 created an issue with content baked into the description but did not call linear_create_comment, and OE16 explicitly directs the create-then-comment two-step. Strict reading keeps the comment-call requirement.
- **0a008e90 / 1b119fa1** (C006 SALT cluster and C006 exception cluster) are intentionally bundled at the cluster level with "(or similar)" softeners, matching the V3 reference style. Splitting further would harvest more partial credit on near-misses and dilute the close-out signal. Strict reading keeps the clusters.
