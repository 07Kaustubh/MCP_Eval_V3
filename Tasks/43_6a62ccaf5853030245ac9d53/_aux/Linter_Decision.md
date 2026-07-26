# Linter Decision — S1.5 — Task 43_6a62ccaf5853030245ac9d53

**Mode:** CB. **Class:** A only (no similarity finding). **Resolution: INVALIDATE all four findings, `5_Prompt.txt` unchanged, one justification on file (voice gate 0 hits).**

## What the linter blocked

A single Business alignment check returning FALSE on four grounds: (1) owner misattribution, Linda Castillo assigned to Mesa Vista when she "owns Rio Bend" and Robert Finley "owns Mesa Vista"; (2) QuickBooks bill lookups and owner-invoice correction are outside the Property Operations tool and write-action matrix and belong to Portfolio Coordination 2.2/2.3; (3) "final owner cost" is an invented Airtable field absent from the tblMakeReady schema; (4) an Onsite PM lacks authority to issue or correct an owner-facing invoice. Its suggested revision reassigns the owner to Robert Finley and recommends re-labelling the task as Portfolio Coordination.

## Skeptical-first reasoning

Each finding was re-grepped against the per-task data and the base-universe docs before deciding. All four are contradicted by evidence, so this is the clearly-wrong branch on every leg, not the ambiguous branch.

**F1 owner identity, clearly wrong and load-bearing.** The AR invoice `445653930748` (Doc 2026-534) carries CustomerRef **Linda Castillo** against "Mesa Vista Unit 4C", lines $387 / $1,140 / $95, total $1,622. The belief email `5101c5a41dffa90a`, "Mesa Vista 4C Make-Ready Complete. Cost Summary for Your Records", opens "Hi Linda." Maintenance ticket `rec12969a3fdb0852` flags Linda Castillo on the 4C turn. The `makeready_turn_carlos` storyline, Carlos's signature scenario, states outright that "an owner invoice gets issued to Linda Castillo." The linter's source is the owner table in the universe summary, whose column is headed "Owns / touches" and which is prefaced with "Each owns one or more properties"; Robert Finley's "Mesa Vista (monthly reports)" entry traces to `owner_monthly_report_review`, a Brooke and Lisa reporting scenario, not to unit-level 4C billing. The table is a scenario-appearance shorthand, and the authoring guidance is explicit that live data is the anchor of record. Acting on this finding would also break the task: there is no 4C invoice under any other owner name, so "correct the invoice she is holding" would have no target and the reconciliation spine collapses.

**F2 QuickBooks scope, clearly wrong.** The Category 1 authoring checklist lists QuickBooks among the Onsite PM primary systems, and subcategory 1.4 lists `quickbooks_mock_update_invoice` as a Cat 1 write with `quickbooks_mock_list_invoices` as a Cat 1 read. The Cat 2.2 write the linter is actually describing is `quickbooks_mock_update_bill`, approve / hold / dispute on a vendor payable, which this prompt never asks for. The prompt's bill touches are reads used to derive a figure; the only QuickBooks write is the correction of an AR invoice the persona's own scenario issued. Both bill notes on the 4C payables name Carlos directly: `195089456477` records "entered into QB by Carlos" and `546359391323` records "Routed and logged by Carlos Mendez." He is already in this ledger in the data.

**F3 invented Airtable field, clearly wrong.** The prompt names no field. `tblMakeReady` carries fldNotes2 as multilineText, and both live 4C rows already hold narrative cost and scope detail there. The linter's own suggested revision resolves to the same place ("note the confirmed vendor costs in the notes field"), so it concedes the mechanism exists and objects only to the prompt not pre-solving where it goes, which is the required prompt style. Already logged at S1 as an S2 carry-forward, not a new defect.

**F4 billing authority, clearly wrong.** Pass-through owner invoicing is a defined universe motion, and Carlos's own make-ready scenario is where the 4C owner invoice originates. Correcting a figure on an invoice his own turn produced is not a spend approval and crosses no threshold.

## Prompt state

`5_Prompt.txt` unchanged, byte-identical to the S1-cleared version. No AUDIT re-fire, correctly: S1.5 step 8 is unconditional only on a revise or pivot path, and there is no new artifact here.

## If the platform rejects the pushback

The strongest ground is F1 and it is documentary, so lead with the invoice and the sent email on any re-submission. Do **not** concede the owner swap: it is factually wrong and it destroys the task. The only cheap surgical concession available, if one is ever demanded, is softening the self-attribution of the original owner bill ("I billed her" to "the bill went out on my turn"), which costs nothing in the levers. Do not concede the QuickBooks reconciliation, which is the entire spine (L2, L10, L6, L11).

## Cross-task pattern

Third recorded StarPM within-universe false positive, after Task 39 (persona seat) and Task 42 (vendor list). Same shape all three times: the linter applies a summary-doc roster or category shorthand as if it were an exclusive rule and does not cross-check the live records that the authoring guidance names as the anchor of record. Does not increment the wrong-universe counter, which stays at 2 (Tasks 35 and 36).
