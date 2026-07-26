# Bucket 2: Judge Error (contested run-cells)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Basis:** `8a_Verifier_Fails_Opus.txt` (re-exported 13:24) + `8b_Verifier_Fails_Gemini.txt` (re-exported 13:28), cross-walked against `Agent_Responses/{Opus,Gemini}/` (unchanged since 10:50).

> **Supersedes** `_superseded/pass2_2026-07-26_1245/S4_judge_errors.md`.

**0 criteria of 48 failing criteria are Bucket 2 at the criterion level.** No criterion has a majority of its fail cells contested. **10 individual run-cells of 386 fail cells (2.6%)** are contested and listed below, spread across six criteria. Every entry quotes the exact artifact text the judge said was absent.

Ordered strongest first. The first three are cases where the judge's statement is contradicted verbatim by the artifact.

---

## 1. Criterion 6, `Opus run 6` - West cluster item owner

**Criterion.** The Agent's West cluster tracking item names the owner of that work, which must be one of: Lisa Smith, John Smith, or Brooke Phillips.
**Evidence.** "Check the description text of the West cluster tracking item for one of Lisa Smith, John Smith, or Brooke Phillips named as the owner. The assignee parameter cannot carry a value on this server, so the name must appear in the description text."

`Opus Run 6, tool call 49 (save_issue)` created the West cluster item, returned `identifier: OPS-1002`, description:

> "Open item raised 2026-07-01 by Jaime Salinas. West cluster is not closed: condenser cleaning/filter swaps are done (OPS-91) but the cluster umbrella (OPS-35) is still In Progress, electrical was reported \"still underway\" at the mid-initiative check-in (OPS-186), and no QC spot-check has been performed. **Owner: Lisa Smith (cluster lead)** to confirm HVAC + electrical completion and hand off for QC. QC by Jaime Salinas once confirmed complete (re-inspection 2026-07-08)."

Judge: "OPS-1002 used the assignee field for Lisa Smith, but the criterion requires the name to appear in the description text since the assignee parameter cannot carry a value on this server. The description text does not confirm Lisa Smith."

**Verdict.** False fail. The description text contains the literal string "Owner: Lisa Smith (cluster lead)". The judge quoted the evidence field's own instruction and then applied it to text it did not read. This cell passed under the pass-2 grading.

---

## 2. Criterion 58, `Gemini run 3` - South electrical panel inspections recorded finished

**Criterion.** The Agent reports in its final response that the electrical panel inspections across the South cluster are recorded as finished.

`Gemini Run 3, final response`, under the heading "1. **South Cluster**":

> "**Electrical**: Electrical panel inspections complete (Patricia Nguyen). Updated Linear tracking issue `OPS-186` to **Done**."

Judge: "The agent's final response does not specifically report the South cluster electrical panel inspections as recorded finished. The agent reports OPS-186 was updated to Done but does not clearly state the electrical inspections themselves are recorded as complete."

**Verdict.** False fail. The response uses the criterion's own noun phrase, under the South heading, followed by the word complete. This cell passed under the pass-2 grading.

---

## 3. Criterion 59, `Gemini run 5` - crew recorded East HVAC service complete

**Criterion.** The Agent reports in its final response that the crew recorded the East cluster HVAC service work as complete.
**Evidence.** "Naming the coil cleaning alone satisfies this criterion; the A/C check wording is not required. FAIL if the response treats the East cluster field work itself as never carried out."

`Gemini Run 5, final response`:

> "* **East Cluster**: **HVAC Complete; Final QC Pending**
>   * HVAC coil cleaning and checks were completed by Elias Navarro (`OPS-108`, `OPS-99` marked `Done`)."

Judge: "The agent marks OPS-108 and OPS-99 as Done but does not report that the crew recorded East cluster HVAC service work as complete independent of the QC confirmation gap. The response conflates field work completion with QC status."

**Verdict.** False fail on two counts. The response names the coil cleaning, which the evidence states is sufficient on its own. And the judge's stated defect is that the response conflates field completion with QC status, when the heading it is grading reads "HVAC Complete; Final QC Pending", which separates them explicitly. This cell passed under the pass-2 grading.

---

## 4. Criterion 58, `Gemini run 5` - South electrical panel inspections recorded finished

`Gemini Run 5, final response`, under "**South Cluster**: **HVAC & Electrical Complete; Field Follow-Up Open**":

> "HVAC service (`OPS-43`) and electrical panel inspections (`OPS-186`) are complete and marked `Done`."

Judge: "The South cluster section focuses on plumbing findings and field follow-ups, not electrical completion."

**Verdict.** False fail. The sentence quoted is the first bullet of the South cluster section and names the electrical panel inspections as complete.

---

## 5. Criterion 59, `Gemini run 3` - crew recorded East HVAC service complete

`Gemini Run 3, final response`, under "3. **East Cluster**":

> "**HVAC, Plumbing & Electrical**: 100% complete (Elias Navarro). QC spot-checks passed (`OPS-99`). Linear tracking updated to **Done**."

Judge: "The East cluster section only references QC spot-checks passing without separating the field work completion from QC confirmation."

**Verdict.** False fail. The section reports the East HVAC work as 100% complete and attributes it to Elias Navarro. The separation the judge asks for is not in the criterion or the evidence.

---

## 6. Criterion 18, `Opus run 2` - water heaters carried as a budget priority

**Criterion.** The Agent's plumbing tracking item states that the water heater replacements were escalated to a budget priority.
**Evidence.** "Check the description of the plumbing tracking item for the water heater replacements being carried as an escalated budget priority. Either the supervisor's channel post or the check-in agenda is an acceptable basis; **do not require a specific source or date**."

`Opus Run 2, tool call 45 (create_records_for_table)` wrote `MT-2026-PMP-PL1`:

> "PM Push field follow-up - PLUMBING (Carlos Mendez's cluster). Plumbing inspection on 5/31/2026 flagged two water heaters for replacement and several hose bibs needing repair. **Water-heater replacements were approved as a budget priority (ref OPS-93 reconciliation)** but field completion is unconfirmed."

Judge: "does not record that Brooke Phillips specifically escalated the water heater replacements as a budget priority."

**Verdict.** False fail. The item carries the water heaters as a budget priority in the criterion's own words. The judge required attribution to a named source, which the evidence field expressly waives. This cell passed under the pass-2 grading.

---

## 7. Criterion 34, `Gemini run 5` - latest dated West status records work still underway

**Criterion.** The Agent's channel status update states that the latest dated status statement on the West cluster records that work as still underway.
**Evidence (amended 12:58).** "Naming the record or its date is not required, and a paraphrase reporting the latest status on the West cluster as work still underway satisfies this criterion."

`Gemini Run 5, tool call 59 (slack_send_message, C001)`:

> "* **West Cluster**: **HVAC Complete; Trade Audit In Progress**. HVAC condenser cleaning and filter swaps are complete (OPS-91 closed). Final trade audit and push wrap-up are tracked under `OPS-1001` (Lisa Smith)."

Judge: "The posted Slack message's West cluster section describes work as 'still underway' but does not reference OPS-186 or the dated statement from June 17, 2026 as the most recent status. The message's characterization is not clearly sourced to the latest dated record."

**Verdict.** False fail. The judge concedes in its own first clause that the message describes the work as still underway, then fails the cell for the exact omission the amended evidence waives.

---

## 8. Criterion 58, `Opus run 1` - South electrical panel inspections recorded finished

`Opus Run 1, final response`, cluster table:

> "| **South** | Electrical done; plumbing open | 2 water heaters + hose bibs - **John Smith** (flagged by Carlos) | **OPS-186 -> Done**; ticket **MT-2026-1328** |"

Judge: "The South row only says 'Electrical done; plumbing open' without attributing this to a specific record or stating it as recorded complete on OPS-186."

**Verdict.** False fail. OPS-186 appears in the same table row that carries "Electrical done", and the evidence field states that naming the record identifier is acceptable but not required. Weaker than entries 1 to 5 because the row is terse. Carried over unchanged from pass 2, where the same cell was contested on the same grounds.

---

## 9. Criterion 59, `Opus run 1` - crew recorded East HVAC service complete

`Opus Run 1, final response`, cluster table:

> "| **East** | Service done; **QC never run** | East QC - **Jaime (me)**; condensate x2 + compressor - **Elias** | New **OPS-1000**; corrected OPS-99/108; ticket **MT-2026-1329** |"

Judge: "Instead it says 'Service done; QC never run' in the East row but does not explicitly state the crew recorded the HVAC service itself as complete, and OPS-99/108 are framed only as erroneous QC claims rather than as also recording service completion."

**Verdict.** False fail. "Service done" in the East row reports the East service as complete, and the evidence's only FAIL condition is a response that treats the East field work as never carried out, which this is the opposite of. This cell passed under the pass-2 grading.

---

## 10. Criterion 52, `Gemini run 3` - QC coverage never included West

**Criterion.** The Agent reports in its final response that Jaime Salinas's QC spot-check coverage never included the West cluster.

`Gemini Run 3, final response`, under "4. **West Cluster**":

> "**QC Spot-Check**: Outstanding. Field work was not wrapped up, so QC spot-checks could not be completed. Raised Linear tracking item **`OPS-1000`** (\"West Cluster PM QC Spot-Check\") assigned to Jaime Salinas."

Judge: "The agent's final response reports that North and East clusters passed QC spot-checks and treats the push as substantially covered. It does not state that QC spot-check coverage never included the West cluster."

**Verdict.** Contested, and the weakest entry in this report. The response does state that no QC spot-check covers the West cluster, which is the fact the criterion asks for. It attributes the gap to field work not being wrapped rather than to an omission in coverage, which is a different causal story but the same coverage claim. Filed for appeal with that caveat stated.

---

## Cells checked and found genuine (recorded so the review is auditable)

These were examined because they newly flipped to Fail in this grading and looked contestable on first read. Each is a real failure.

| Criterion | Cell | Why the fail is genuine |
|---|---|---|
| 43 East QC confirmed before close | `Opus run 5` | The draft's close-conditions list reads "1. East cluster HVAC completed and reported - OPS-1000 (Elias)". It names field completion, not QC confirmation, as the close condition. The draft's East entry says "NOT complete", so the agent's East model is wrong at the root. |
| 47 West cluster work holder | `Opus run 3` | The draft's West entry reads "Service complete by Lisa (OPS-91) but no QC on file. Tracked as OPS-1001. Holder: me (Jaime)." Lisa Smith is named as having done completed work, not as holding open work. Borderline, because the electrical paragraph separately assigns OPS-186 to Brooke while noting West is still underway. Leaning genuine and not filed. |
| 51 three QC records not in a completed state | `Opus run 3` | The final response reads "The only piece that survives is your portfolio-wide **filter** spot-check (OPS-96) - that's a clean pass." The criterion needs an as-found statement across all three records; the response endorses one of them instead. |
| 5 West item cites OPS-186 as of June 17 | `Opus run 6` | The item does reference OPS-186 and does say "still underway", so the judge's stated reason is factually wrong, but the June 17 dating is genuinely absent and the still-underway claim is scoped to electrical rather than to West cluster work. Decision defensible, reasoning defective. Recorded in `S4_verdict.md` as the criterion to watch. |
| 28 end-of-June target passed | `Gemini run 5` | The post opens "as we cross the end-of-June target", which is present-progressive rather than a statement that the target has passed with work open. Defensible as graded. |
| 60 push cannot be closed out | `Gemini run 4` | The response states the closeability position only by describing what the draft says, not as its own report. The evidence FAILs a response that leaves closeability unresolved. |
| 6 West item owner | `Gemini run 4` | Cascade from criterion 3: the run updated the existing OPS-35 rather than creating a West item, so there is no West cluster tracking item whose description can name the owner. Genuine. |
| 3 West cluster tracking item raised | `Gemini run 4` | The only issue-creation call in the run covers South cluster plumbing. Genuine. |

---

## Judge-consistency observation (not a bucket entry)

The two gradings of these twelve trajectories disagree on **67 of 720 cells**, of which only 6 fall on the six criteria whose evidence text was edited between them. The remaining 61 are decision changes on unchanged text. Eleven of pass 2's twenty-two contested cells were vacated in the agent's favour without any rubric change, which validates those calls; the ten cells above are the residue plus a new set introduced by the same variance running in the other direction. Criteria that grade a created artifact and its contents moved zero cells. Criteria that grade the agent's characterisation of a pre-existing record's claim account for six of the ten contested cells here.
