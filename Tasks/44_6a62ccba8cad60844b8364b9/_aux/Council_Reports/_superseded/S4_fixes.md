# S4 Bucket 1 — Rubric Invalid: fixes

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4) · **Model set:** Opus 4.8 (6 runs)
**Gemini half not classified** — `8b_Verifier_Fails_Gemini.txt` is 0 bytes on disk.

Three criteria out of 44 failing criteria are Bucket 1. All three are the same defect class: the criterion penalises an action the Oracle Events explicitly bless. None of them is a coverage carrier and none is a Hardness lever carrier, so all three fixes are re-phrasings, not deletions. **No criterion is merged and none is removed, so the set stays at 60.**

---

## Fix 1 — criterion 15 (plumbing container): channel lock-in against an explicit OE latitude clause

**Before (title unchanged in substance, evidence is the defect):**

> title: `The Agent raises a tracking item for the open plumbing findings from the push.`
> evidence: `Look for an issue-creation call on the Operations team that returns success, whose title or description concerns the open plumbing findings from the push.`

**After:**

> title: `The Agent raises tracking work or a maintenance ticket for the open plumbing findings from the push.`
> evidence: `Look for an issue-creation call on the Operations team that returns success, or a new row in the Maintenance Tickets table, whose title or description concerns the open plumbing findings from the push. Either destination satisfies this criterion, because the water heater replacements and the hose bib repairs are field items that may be routed to either the tracking board or the ticket log.`

**Trajectory citation.** Run 1, tool call 47 `create_records_for_table`: `MT-2026-1328` = "two water heaters for replacement and several hose bibs needing repair ... Owner: John Smith (execution); flagged by Carlos Mendez". Run 6, tool call 45: `PMP-2026-02` = "Two water heaters are past serviceable life and require replacement ... Hose bibs at several units require repair ... OWNER: Carlos Mendez." Both runs routed the plumbing findings to the ticket log and were failed on the container criterion for not using Linear. Runs 2 and 5 did the same.

**Reasoning.** OE 32 states verbatim: *"Because routing the water heater replacements to the Airtable ticket log is equally acceptable, the criterion covering them must accept either location, and the same latitude applies to the hose bib repairs ... both are boundary items and no criterion may require or penalise a particular routing for either."* The two content criteria under this container (criteria 16 and 17, water heaters and hose bibs) were written with that latitude and passed 6/6. The container criterion was not, and it false-failed four runs that satisfied its content. Channel / method lock-in with a valid alternative path available is **Major by default** under the pipeline's Rubrics-Eval Phase 2.7 reading.

**Cross-artifact check.** No OE edit needed. OE 32's decomposition directive names the water heaters, the hose bibs and the budget escalation as the content elements plus a separate owner criterion; all four survive this fix unchanged.

---

## Fix 2 — criterion 11 (tenant-access container): same defect, boundary item named in OE 28

**Before:**

> title: `The Agent raises a tracking item covering the push units still waiting on tenant access.`
> evidence: `Look for an issue-creation call on the Operations team that returns success, whose title or description concerns units still awaiting tenant access. Splitting this into two separate tracking items, one per cluster, satisfies this criterion equally.`

**After:**

> title: `The Agent raises tracking work or a maintenance ticket covering the push units still waiting on tenant access.`
> evidence: `Look for an issue-creation call on the Operations team that returns success, or a new row in the Maintenance Tickets table, whose title or description concerns units still awaiting tenant access. Splitting this into two separate items, one per cluster, satisfies this criterion equally, and either destination satisfies it, because the South cluster unit that was never serviced is a field item that may be routed to either place.`

**Trajectory citation.** Run 2, tool call 45 `create_records_for_table`: `MT-2026-PMP-S1` = "SOUTH cluster no-access unit. Tenant was out during the scheduled HVAC service window (ref OPS-43); the unit never received its coil cleaning ... Carlos Mendez to reschedule tenant access". Run 3, tool call 70: `MT-2026-PMF-02`, same content. Run 5, tool call 37: `MT-2026-086`, same content. All three passed criterion 12 (the South-unit content) and criterion 14 (the owner) **on the strength of those exact tickets**, and were failed on the container for the routing.

**Reasoning.** OE 28 names the South cluster unit that was never serviced in its boundary list and states *"No criterion may require or penalise a particular routing for any of them."* The verifier applied "tracking work" loosely on criteria 12 and 14 and "raises a tracking item" strictly on criterion 11, which is internally inconsistent grading produced by inconsistent phrasing inside the pipeline's own set.

**Second defect found while applying the fix: the container's scope was ambiguous.** As originally written, "covering the push **units**" could be read as requiring both tenant-access items in one record, which is the reading the verifier applied and which duplicates criteria 12 and 13. The applied fix therefore carries a third sentence: *"Because the South cluster unit and the two North cluster units are graded as separate criteria of their own, this criterion is satisfied by an item covering either of them and does not require both to sit in the same item."*

**Residual difficulty after the fix, measured rather than assumed.** Runs 2, 3 and 5 each wrote a maintenance ticket naming the South no-access unit explicitly (`MT-2026-PMP-S1`, `MT-2026-PMF-02`, `MT-2026-086`) and each passed criteria 12 and 14 on those tickets, so all three now pass criterion 11 as well: **6/6 fail becomes 3/6 fail.** Runs 1, 4 and 6 still fail, having created nothing covering tenant access anywhere. Criterion 13 (the OPS-56 North pair) is untouched and still fails 6/6, so the task's discriminating power on the tenant-access chain is preserved in the criterion designed to carry it. An earlier draft of this document asserted criterion 11 would still fail 6/6; that was an assumption from the verifier's strict plural reading and it is wrong.

**Cross-artifact check.** OE 31 currently reads *"Create a tracking item for the outstanding access reschedules using save_issue"*. Add one sentence to OE 31 mirroring OE 28's boundary latitude for the South unit, so the two OEs stop disagreeing:

> Append to OE 31: `Because OE 28 lists the South cluster unserviced unit as a boundary item, an agent that files the South unit in the maintenance ticket log and the North access-pending pair as a tracking item is not wrong, and the S3 criteria must accept either destination for the South unit.`

---

## Fix 3 — criterion 51: penalises a state flip that OE 15 explicitly permits

**Before:**

> title: `The Agent reports in its final response that none of Jaime Salinas's three QC spot-check records, OPS-87, OPS-96, and OPS-98, is in a completed workflow state.`
> evidence: `... FAIL if the response reports the QC records as complete, or generalises to a claim that no push work is in a completed state.`

**After:**

> title: `The Agent reports in its final response that none of Jaime Salinas's three QC spot-check records, OPS-87, OPS-96, and OPS-98, was in a completed workflow state as the Agent found them.`
> evidence: `Check the Agent's final response for a statement that the three spot-check records OPS-87, OPS-96 and OPS-98 were all in non-completed workflow states when the Agent retrieved them, against each record's own text claiming a move to Done or In Review. An Agent that reports the as-found states and then moves one of the three to a completed state itself satisfies this criterion, because correcting a record is a permitted action. FAIL if the response reports the QC records as having been complete on retrieval, or generalises to a claim that no push work is in a completed state.`

**Trajectory citation.** Run 2, tool call 35 `save_issue(id="OPS-96", state="Done")`, then final response: *"Filters (portfolio) | Genuine PASS | None - finalized OPS-96 to Done."* Verifier justification: *"The agent finalized OPS-96 to Done (a completed workflow state), so it cannot be said that none of OPS-87, OPS-96, and OPS-98 is in a completed workflow state."* Run 1, tool call 55 and run 5, tool call 43 made the same flip and drew the same reasoning.

**Reasoning.** OE 15 grading note two states verbatim: *"no state change is required on OPS-87, OPS-96 or OPS-98, and an agent that also flips one of them is not wrong."* The criterion as written is not robust to that permitted action, because it grades the state in the present tense after the agent has already written to it. Run 5's final response contains the finding in substance (*"none of my QC issues or the cluster issues were ever actually moved to Done in Linear despite the descriptions claiming so"*) and was still failed on the flip.

**Lever preservation.** This is the criterion carrying Lever 2, the structured-database skip, which is the symmetric backbone of the task. The fix must not weaken it, and does not: the agent still has to read the workflow-state column on all three records and report the prose-versus-state contradiction. Only the tense and the interaction with a permitted write change. Runs 1 and 2 still fail after the fix, because neither made the finding at all.

**Cross-artifact check.** OE 15 needs no change. Criteria 20, 21, 24, 32, 42 and 55 carry the same state-versus-prose determination on other records and none of them collides with a permitted write, so no further criterion needs this treatment.

---

## Advisories (NOT Bucket 1 — no change required, recorded for the next build)

These are flexibility risks that did not cause a false fail in this run set. They are logged so the pattern is visible, not actioned.

| Criterion | Risk | Why it is not Bucket 1 here |
|---|---|---|
| 7 (filter run container) | Reads "raises a tracking item". Run 4 recorded the same content on the existing filter record OPS-79 (tool call 39: "Portfolio HVAC filter replacements are NOT confirmed complete. 20x25 filter stock ran out mid-run (John, 5/23) ... Owner: John Smith") and was failed. | OE 30 carries no latitude clause, and three near-duplicate filter records already exist, so directing a fresh item is a deliberate design choice rather than an oversight. Five of six runs failed on content, not routing. Consider `raises or updates a dedicated tracking item` on the next build. |
| 3 (West container) | Same shape as 7. | No run routed the West QC coverage gap anywhere else, so no alternative path was penalised. |
| 24 (note on OPS-98) | Requires the note on OPS-98 specifically. Run 5 wrote the exact finding on OPS-87 instead. | OE 35 mandates three atomic per-record notes and the prompt says "a short note left on each one", so per-record placement is prompt-grounded. |
