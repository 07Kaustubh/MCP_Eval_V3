# S4 Bucket 2 — Judge Error

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm (V4) · **Model set:** Opus 4.8 (6 runs)
**Gemini half not classified** — `8b_Verifier_Fails_Gemini.txt` is 0 bytes on disk.

One criterion is Bucket 2 at the criterion level. Three further per-run misreads sit under criteria whose overall bucket is 3 and are recorded separately below so the pattern is visible without inflating the Bucket 2 count.

---

## Bucket 2, criterion level

### Criterion 58 — "The Agent reports in its final response that the electrical panel inspections across the South cluster are recorded as finished."

Failed 6/6. Three of the six runs satisfied it in substance and were marked Fail on a reading stricter than the criterion's own evidence field authorises.

The evidence field reads: *"The South scoping comes from the record's own title; naming the record identifier is acceptable but is not required, and a response that attributes the completion to the record titled Electrical panel inspections complete - South Cluster wrap-up without repeating the word South also satisfies this criterion."*

**Run 1, final response.** Cluster table row: `| **South** | Electrical done; plumbing open | ... | **OPS-186 → Done**; ticket **MT-2026-1328** |`, plus the actions list: *"Cluster records reconciled: North reopened, **South electrical closed**, East duplicates corrected."* Trajectory corroboration: run 1, tool call 60 `save_comment(issueId="OPS-186")` = *"South-cluster electrical panel inspections are complete and documented (Patricia Nguyen), so I'm marking this Done to match reality."*
Verifier said: *"The South cluster entry in the table marks electrical as 'done' but the criterion requires the electrical inspections specifically to be called out as recorded finished."* That distinction is not in the criterion.

**Run 4, final response.** Cluster table row: `| South HVAC + electrical | ✅ Done | Patricia (elec.) | Nothing outstanding |`, plus *"Tracking fixed to reality: **OPS-186 (South electrical) → Done**."* Trajectory corroboration: run 4, tool call 38 `save_comment` on OPS-186 = *"South Cluster electrical panel inspections were reported complete and documented by Patricia Nguyen at the mid-initiative check-in."*
Verifier said: *"does not specifically mention the electrical panel inspections as a distinct finished item per OPS-186."* The response names OPS-186, names South electrical, and names Patricia.

**Run 6, final response.** Cluster table row: `| **South** | Serviced; **electrical confirmed (Patricia)** | **PASS** - holds |`.
Verifier said: *"does not separately call out that the electrical panel inspections are recorded as complete."* "Electrical confirmed (Patricia)" against the record whose title is `Electrical panel inspections complete - South Cluster wrap-up` is exactly the attribution the evidence field says is sufficient.

**Runs 2, 3, 5 are correct Fails.** Run 2 never fetched OPS-186 and never mentions South electrical. Run 3 asserted the opposite (*"electrical is NOT portfolio-complete and this issue should stay open"*). Run 5 reported electrical as *"Only North panel notes"* with no South completion.

**Ground truth confirmed.** `linear.linear_issues.json` OPS-186, state `Todo` (`state_OPS_1`), created 2026-06-17, assignee Brooke Phillips, title `Electrical panel inspections complete - South Cluster wrap-up`, description opens *"Patricia confirmed at the mid-initiative check-in that all electrical panel inspections across her cluster are finished and the findings have been documented."* The criterion's premise is sound; only its application was.

**Action.** No rubric change required. Optional hardening for the next build: append `(or similar)` after "recorded as finished" in the title so a table-cell expression is unambiguously in scope. Appeal 3 of 6 runs if the platform supports per-run appeals.

---

## Per-run misreads under Bucket 3 criteria (recorded, not counted)

These do not change their criterion's bucket, because a majority of runs failed each of them for correct reasons.

| Criterion | Run | What the trajectory shows | What the verifier said |
|---|---|---|---|
| 59 — "reports that the crew recorded the East cluster HVAC service work as complete" | Run 1 | Final response cluster table: `| **East** | Service done; **QC never run** | ...`. That is precisely the separation of recorded field completion from unconfirmed QC that the criterion asks for. | *"does not report the East cluster HVAC service work as recorded complete by the crew ... without distinguishing the field work (recorded complete) from the QC (unconfirmed)."* Runs 2, 3, 4, 5 are correct Fails; run 5 asserted the opposite (`East: Never completed`). |
| 51 — "reports that none of ... OPS-87, OPS-96, OPS-98 is in a completed workflow state" | Run 5 | Final response: *"none of my QC issues or the cluster issues were ever actually moved to Done in Linear despite the descriptions claiming so, so the sign-off wasn't even real in the records."* The finding is present; the three records are not named individually. | Failed on the agent's own flip of OPS-96 to Done. This is the defect handled as Bucket 1 Fix 3, so it is not double-counted here. |
| 33 — "channel status update tells the crew that the West cluster went through the push without any QC spot-check coverage" | Run 5 | Correct Fail. Run 5's channel post reads `*West* - ✅ Done (Lisa, OPS-91)` with no coverage-gap statement. Listed only to record that the walk was performed. | Correct. |

---

## Bucket 2 verification statement

Every entry above was reached by walking the run's trajectory write calls and final response text before reading the verifier justification, and every cited value was re-confirmed against `_aux/Universe_Split/linear.linear_issues.json`. No Bucket 2 entry rests on the verifier text alone.
