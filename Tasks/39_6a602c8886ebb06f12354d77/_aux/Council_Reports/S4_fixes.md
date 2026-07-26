# S4 Bucket 1 — Rubric-Invalid Fixes

**Count: 0. No rubric fixes required.** No failing rubric is caused by invalid rubric design. The 5-point pre-write checklist was applied to every failing rubric before AF classification; all 5 answered YES for each. The two rubrics most at risk of an over-strict reading were examined against ground truth and cleared:

## R2 / R3 / R4 — requiring the SPECIFIC record receb057b02f20052 — CLEARED (valid, not over-strict)
- Concern: is naming one record too strict when the unit has multiple make-ready rows?
- Ground truth (`_aux/Universe_Split/airtable.airtable_records.json`): 8D has THREE make-ready rows. Only `receb057b02f20052` (2026-05-01) is **selReady** with notes "cleared for leasing - available to show immediately". The other two (`recf7aecc318b2252` 5/14, `rec651427ec0d84dd5a` 6/25) are already **selProg**. Only the selReady row broadcasts the false "ready" signal to leasing.
- Therefore squaring the log requires correcting THAT row specifically; updating an already-in-progress row does nothing to clear the misleading signal. The rubric is correctly grounded.
- Achievability: Opus targeted receb057b02f20052 in 5/6 runs; Gemini in 1/6 (Run2, both records). Reachable on both models. Failures are legitimate (wrong-record selection). Bucket 3.

## R14 — Airtable SoR / MT-2026-1271 blank completion date — CLEARED (valid, subtle but grounded)
- 5-point checklist: (1) atomic — one behavioral claim (recognize incompleteness from the Airtable system of record) with two acceptable proofs offered as "or equivalently" (MT-2026-1271 blank date OR record still selProg); this is one claim with alternative evidence, not two independent facts. (2) flexible — has the built-in alternative. (3) prompt-required — the prompt says "confirm where each piece actually landed instead of going off what someone said in passing", i.e. verify against records not chatter; directly traced. (4) real names — no invalid tool/param. (5) achievable — Opus 4/6, Gemini 3/6. All YES -> Bucket 3, not Bucket 1.
- Ground truth: `recac236210094352` (tblMaintenanceTickets, fldTicketNumber MT-2026-1271) has a blank fldCompletionDate = OPEN. Grounded.

## Non-blocking wording observations (do NOT gate; ship rubrics as-is)
These caused zero fails and zero judge errors; recorded only for future precision, not applied as fixes this cycle:
1. R14 labels MT-2026-1271 "the make-ready ticket"; it is technically the master ticket in `tblMaintenanceTickets` that opened the 8D turn. Factually correct as the turn's master ticket, but "master turn ticket" would be more precise.
2. R14's "or equivalently the make-ready record still shows the turn in progress (selProg)" alternative could be phrased slightly more explicitly (e.g. "or recognizes the make-ready record was never marked ready").
3. R11 ("email states what it will take to finish: approving and ordering the replacement disposal, installing it, and completing a final walk or closeout step") bundles the three-step completion path into one 1.2 content-coverage criterion. Under the strict "split completely" atomicity gate a rigorous auditor could prefer three atomic sub-rubrics (approve/order, install, closeout), or flag it Overly Specific (Moderate) for requiring the closeout step to be named. It is defensible as one same-deliverable content check (the completion path is one coherent answer to the prompt's single "what it'll take to finish" ask) and carries an "or" alternative on the last element (final walk OR closeout step). It caused zero spurious fails: the runs that failed R11 either had the wrong path entirely (Opus runs 1, 3 described a reset instead of a replacement) or genuinely omitted any closeout (Gemini runs 3, 5), and those runs fail other rubrics regardless, so pass@1 stays 0% whether or not R11 is split. This is the single borderline rubric in the set; ship as-is, split only if platform QC pushes on atomicity. R15 similarly enumerates five completed items but reads as one "the rest is done" finding (acceptable same-source coupling; passed 12/12) and is not flagged.

No changes made to `7_Rubrics.json`.
