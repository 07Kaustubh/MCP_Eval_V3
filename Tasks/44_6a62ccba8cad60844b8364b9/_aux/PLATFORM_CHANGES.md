# Platform change list - Task 44 (`44_6a62ccba8cad60844b8364b9`)

**Generated:** 2026-07-26 from `7_Rubrics.json` and `6_Oracle_Events.txt` as they stand after the QC 5/5 fix pass.
Paste-ready. Do not retype any field; copy the blocks below verbatim.

## 0. What does NOT change

- **`5_Prompt.txt`** - untouched. Do not re-upload.
- **Universe / `3_UniverseDataForThisTask.json` / `9_Universe_inject.sql`** - untouched.
- **Trajectories** - do NOT re-run. Density (Opus 62.5, Gemini 79.8) and pass@1 (0/6 both) are trajectory properties and already pass. None of the edits below can change them.
- **56 of 60 criteria** - unchanged.

## 1. Rubric criterion edits (4 criteria)

Edit these in place. The set must stay at 60 criteria: do not add, delete, split or merge anything.

### Criterion 6 - change title, evidence, justification

*Locate it on the platform by its current title:*

> The Agent's West cluster tracking item names the owner of that work, which must be one of: Lisa Smith, John Smith, or Brooke Phillips.

**NEW title:**

```
The Agent's West cluster QC coverage tracking item names the owner of that work, which must be one of: Lisa Smith, John Smith, or Brooke Phillips.
```

**NEW evidence:**

```
Check the description text of the newly created West cluster tracking item whose title or description concerns West cluster preventive maintenance QC coverage for one of Lisa Smith, John Smith, or Brooke Phillips named as the owner. The assignee parameter cannot carry a value on this server, so the name must appear in the description text. FAIL if no such item was created, because an owner named only on a comment written on a pre-existing West cluster record does not satisfy this criterion.
```

**NEW justification:**

```
The prompt requires the person who owns the work to be named on the tracking item that is raised for it. OPS-35 names Lisa as the West cluster onsite lead and John Smith as maintenance execution lead, and Brooke Phillips is the assignee on both OPS-35 and OPS-186, so any of the three is defensible. The owner has to be named on the item raised for the coverage gap, because a name added to a pre-existing West cluster record leaves the gap itself untracked.
```


### Criterion 58 - change title, evidence, justification

*Locate it on the platform by its current title:*

> The Agent reports in its final response that the electrical panel inspections across the South cluster are recorded as finished.

**NEW title:**

```
The Agent reports in its final response that the electrical panel inspections across the South cluster are finished.
```

**NEW evidence:**

```
Check the Agent's final response for the South cluster electrical panel inspections being reported as finished. Any wording that reports them as finished satisfies this criterion. Do not require the response to attribute the completion to a record, to name a record identifier, or to repeat the word South, because the South scoping comes from the record's own title while the record's description says her cluster. A response that reports the inspections as finished and also notes that the record carrying that statement is not itself in a completed workflow state satisfies this criterion. FAIL only if the response does not report the electrical panel inspections as finished, or if it asserts they were never completed. An Agent that separately carries the panel notes on the two flagged North cluster units as open work is not wrong and must not be penalised.
```

**NEW justification:**

```
The prompt asks the Agent to work out what is actually finished as well as what is not, and the push covered electrical alongside HVAC and plumbing. OPS-186, dated June 17, 2026, records that all electrical panel inspections across that cluster are finished with the findings documented, and nothing in the records contradicts it. The criterion grades whether the Agent reports that completion at all, not how it attributes it, because OPS-186 itself sits in a non-completed state and its description says her cluster rather than South.
```


### Criterion 59 - change title, evidence, justification

*Locate it on the platform by its current title:*

> The Agent reports in its final response that the crew recorded the East cluster HVAC service work as complete.

**NEW title:**

```
The Agent reports in its final response that the East cluster HVAC service work is recorded as complete.
```

**NEW evidence:**

```
Check the Agent's final response for the East cluster HVAC service work being reported as complete. Any wording that reports the East field work as done satisfies this criterion, however it is attributed: naming the crew, naming Elias Navarro, naming the record, or naming no source at all are all acceptable. Naming the coil cleaning alone satisfies this criterion; the A/C check wording is not required. A response that reports the service work as done while holding the QC on it as unconfirmed satisfies this criterion, and that separation is the intended reading. FAIL if the response does not report the East cluster field work as done, which includes a response that treats that work as never carried out, a response that carries it only as unconfirmed or still to be confirmed, and a response that omits the East cluster entirely.
```

**NEW justification:**

```
The prompt asks what is actually finished as well as what is not. OPS-99 and OPS-108 both record the East cluster service work as finished, and separating that recorded field work from the unconfirmed QC on it is what keeps the report from overstating how much of the push is open. The criterion grades whether the Agent reports the field work as done, not how it attributes that, because both records sit in non-completed states.
```


### Criterion 33 - change evidence

*Locate it on the platform by its current title:*

> The Agent's channel status update tells the crew that the West cluster went through the push without any QC spot-check coverage.

**NEW evidence:**

```
Check the posted channel message for a statement that no QC spot-check record covers the West cluster's preventive maintenance work. The portfolio-wide filter spot-check does not count as coverage of the West cluster's preventive maintenance service, so a message that names it and still reports the West cluster as uncovered satisfies this criterion. FAIL if the message instead asserts that no West cluster work finished.
```


## 2. Oracle event edit (1 event)

**OE 29** only. Replace the whole event body with the text now in `6_Oracle_Events.txt` line 57.
Two changes: the West dated-status element no longer requires naming OPS-186 or the June 17 date, and the
decompose directive now carries the owner-binding rule. All other 37 events are unchanged.

```
OE 29: Create a tracking item for the West cluster QC coverage gap using save_issue (title: relating to West cluster preventive maintenance QC coverage or similar, description: covering that no QC spot-check record covers the West cluster, that the most recent dated status statement on the West cluster records that work as still underway (that statement is carried on OPS-186, dated 2026-06-17, whose description reads that the West Cluster work is still underway; naming the record identifier or the date is not required), and naming the owner of that work in the description text, team: "OPS", project: "Preventive Maintenance Push" optionally, state: "Todo" or "Backlog" optionally). The owner named should be one of Lisa Smith (onsite lead per OPS-35), John Smith (maintenance execution lead per OPS-35) or Brooke Phillips (assignee on OPS-35 and OPS-186); any of the three is defensible. S3 must decompose this into one criterion per content element (that no QC spot-check record covers the West cluster, and that the most recent dated status statement on the West cluster records that work as still underway) plus a separate criterion for the named owner, never one criterion enumerating them. The owner criterion must be bound to this newly created item, because an owner named only on a comment written on a pre-existing West cluster record leaves the coverage gap itself untracked. The item is the QC coverage gap and the later status statement, not an assertion that no West work finished, because OPS-91 is in state Done. Note that the save_issue assignee parameter cannot carry a value on this server, so the owner must be written into the description text rather than assigned. This is the unambiguous tracking-item side of the routing split.
```

## 3. All-failing rubric justifications (34 criteria)

Full text is in `_aux/Council_Reports/S4_AF_justifications.md`, where each section heading **is** the
criterion title, so it matches what the platform shows. Voice gate clean, zero em-dashes.

| # | Fails on | Criterion title (match on this) |
|---|---|---|
| 2 | Gemini | The Agent's new maintenance ticket describes the two North cluster units Jaime Salinas flagged on May 23, 2026 as needing HVAC attention right away. |
| 4 | Gemini | The Agent's West cluster tracking item states that the West cluster's preventive maintenance work was never covered by a QC spot-check record. |
| 5 | Gemini | The Agent's West cluster tracking item states that the most recent dated status statement on the West cluster records that work as still underway. |
| 7 | Gemini | The Agent raises tracking work on the Operations board for the portfolio HVAC filter replacement run that was never finished. |
| 8 | Gemini | The Agent's filter run tracking work states that John Smith reported on May 23, 2026 that a 20x25 filter shortage was blocking him from finishing the run. |
| 9 | Opus + Gemini | The Agent's filter run tracking work records Brooke Phillips's outstanding request to Elias Navarro for a filter stock count ahead of a bulk order. |
| 10 | Gemini | The Agent's filter run tracking work names the owner of that work, which must be one of: John Smith, Elias Navarro, or Brooke Phillips. |
| 11 | Gemini | The Agent raises tracking work or a maintenance ticket covering the push units still waiting on tenant access. |
| 12 | Gemini | The Agent's tracking work or maintenance ticket for outstanding tenant access covers the single South cluster unit that was never serviced because the tenant was not home during the scheduled access window. |
| 13 | Opus + Gemini | The Agent's tracking work for outstanding tenant access covers the two North cluster units that OPS-56 records as still held up by tenant scheduling conflicts. |
| 14 | Gemini | The Agent's tracking work for outstanding tenant access names the owner, which must be one of: Carlos Mendez, Elias Navarro, or Tony Reyes. |
| 18 | Gemini | The Agent's plumbing tracking work states that the water heater replacements were escalated to a budget priority. |
| 20 | Opus + Gemini | The Agent records that OPS-99 and OPS-108 carry the same East cluster HVAC QC title while sitting in two different workflow states. |
| 21 | Opus + Gemini | The Agent records that neither East cluster QC record, OPS-99 nor OPS-108, is in a completed workflow state. |
| 22 | Gemini | The Agent leaves a note on OPS-87 stating that the record does not stand as a close-out of the South and North cluster QC. |
| 23 | Gemini | The Agent leaves a note on OPS-96 stating that the portfolio filter spot-check does not stand because the filter run was still blocked on a 20x25 filter restock when it was logged. |
| 24 | Gemini | The Agent leaves a note on OPS-98 recording that the South and North cluster QC did not land where the record claims, with the reason. |
| 29 | Gemini | The Agent's channel status update states that one South cluster unit was never serviced because the tenant was not home during the scheduled access window. |
| 30 | Gemini | The Agent's channel status update states that the two units Jaime Salinas flagged in the North cluster on May 23, 2026 still need the HVAC work she called out. |
| 31 | Opus + Gemini | The Agent's channel status update states that the access follow-up on two North cluster units held up by tenant scheduling conflicts is still open. |
| 32 | Gemini | The Agent's channel status update states that the East cluster QC record is not in a completed workflow state. |
| 33 | Gemini | The Agent's channel status update tells the crew that the West cluster went through the push without any QC spot-check coverage. |
| 38 | Gemini | The Agent's draft to Brooke Phillips states that the South cluster's open item is the unit that was never serviced because the tenant was not home during the scheduled access window. |
| 39 | Gemini | The Agent's draft to Brooke Phillips states that the missed South cluster unit still has to be re-scheduled for service before the push can close. |
| 40 | Gemini | The Agent's draft to Brooke Phillips states that the two North cluster units flagged on May 23, 2026 still need a technician back onsite. |
| 41 | Opus + Gemini | The Agent's draft to Brooke Phillips separately identifies two North cluster units held up by tenant scheduling conflicts whose access follow-up is still open. |
| 42 | Gemini | The Agent's draft to Brooke Phillips states that the East cluster QC is unconfirmed because the East cluster QC record is not in a completed workflow state. |
| 43 | Gemini | The Agent's draft to Brooke Phillips states that the East cluster QC has to be confirmed before the push can close. |
| 46 | Gemini | The Agent's draft to Brooke Phillips names the person holding the outstanding tenant access work, which must be one of: Carlos Mendez, Elias Navarro, or Tony Reyes. |
| 48 | Gemini | The Agent's draft to Brooke Phillips names the person holding the East cluster QC confirmation, which must be one of: Elias Navarro, Jaime Salinas, or Brooke Phillips. |
| 51 | Gemini | The Agent reports in its final response that none of Jaime Salinas's three QC spot-check records, OPS-87, OPS-96, and OPS-98, was in a completed workflow state as the Agent found them. |
| 53 | Gemini | The Agent reports in its final response that the South cluster still has one unit that was never serviced because of a missed tenant access window. |
| 54 | Gemini | The Agent reports in its final response that the two North cluster units Jaime Salinas flagged on May 23, 2026 still require the HVAC work she called out. |
| 55 | Gemini | The Agent reports in its final response that the East cluster QC is unconfirmed rather than complete. |

**Do not submit an all-failing justification for criterion 59.** It was graded 0/6 on Opus, but two of
those cells were misgraded and the criterion has been rewritten (see section 1). Under the corrected text
it passes on Opus and is not all-failing on either model.

## 4. Disputes / per-cell appeals (14 cells)

File only if the platform accepts per-cell disputes. Each rests on artifact text that contradicts the
judge's stated reason word for word. Ordered strongest first.

**1. Opus run 4 - criterion 22** (Note on OPS-87 does not stand as a South/North close-out)

> Comment written on OPS-87 by internal record id 1d96db3b-56d6-4530-b2e6-afc6df6354c3, which resolves to OPS-87. Judge mis-resolved it as OPS-99 and reported no comment on OPS-87. The run wrote no comment on OPS-99 at all. Evidence field accepts the internal id form.

**2. Opus run 1 - criterion 43** (Draft names East QC confirmation as a close condition)

> Draft EAST section: 'To close: I run the East QC spot-check and it passes'. Closing summary also lists 'East QC' among what stands between us and closing.

**3. Opus run 1 - criterion 48** (Draft names the person holding East QC confirmation)

> Draft: 'I've raised OPS-1000 (owned by me) for the outstanding East QC', signed 'Thanks, Jaime'. Evidence field explicitly accepts a first-person self-reference as naming Jaime Salinas.

**4. Opus run 1 - criterion 55** (Final response reports East QC unconfirmed rather than complete)

> Final response table row: '| East | Service done; QC never run |', plus 'OPS-99/OPS-108 record the East cluster as QC passed / Jaime confirmed - I never ran that inspection.'

**5. Opus run 1 - criterion 56** (Final response reports plumbing findings incl. water heaters still open)

> Final response table row: '| South | Electrical done; plumbing open | 2 water heaters + hose bibs - John Smith |'. The same cell the judge cited reads 'plumbing open'.

**6. Opus run 6 - criterion 32** (Channel update states the East QC record is not in a completed workflow state)

> Channel message: 'East - service done, but QC never done. Elias wrapped the service (OPS-99, In Review) and handed it to me'. Names the record and its non-completed state.

**7. Opus run 6 - criterion 46** (Draft names the person holding outstanding tenant access work)

> Draft SOUTH section: 'Open before close: confirm the one earlier no-access unit (OPS-43) was actually serviced. Owner: Elias Navarro / Carlos Mendez (access).' Two of the three permitted owners are named.

**8. Gemini run 6 - criterion 28** (Channel update states the end-of-June target passed with work still open)

> Channel message first line: 'Team, the end-of-June target to close out the Preventive Maintenance Push has passed.' Also 'this push cannot be closed yet'. Judge reasoned from the run summary, not the sent payload.

**9. Gemini run 4 - criterion 36** (Channel update states plumbing findings incl. water heaters still open)

> Channel message: 'MT-2026-1327: Replace 2 aging water heaters past serviceable life' under a Plumbing heading, plus 'The PM Push remains OPEN until ... South Cluster plumbing repairs are completed.'

**10. Gemini run 5 - criterion 36** (Channel update states plumbing findings incl. water heaters still open)

> Channel message: 'South Cluster: HVAC & Electrical Complete; Plumbing Field Follow-Up Open' and '2 water heater replacements, hose bib repairs ... require tech dispatch'.

**11. Gemini run 5 - criterion 43** (Draft names East QC confirmation as a close condition)

> Draft East Cluster block: 'Status: OPEN - Final QC Spot-Check Pending' and 'Action Needed to Close: Jaime Salinas conducts final QC spot-check walk and logs passing verification on OPS-1002.'

**12. Gemini run 5 - criterion 48** (Draft names the person holding East QC confirmation)

> Draft East Cluster block: 'Who is Holding It: Jaime Salinas (QC Inspector).'

**13. Gemini run 5 - criterion 56** (Final response reports plumbing findings incl. water heaters still open)

> Final response: 'South Cluster: HVAC & Electrical Complete; Field Follow-Up Open ... Plumbing audit flagged 2 water heater replacements and exterior hose bib repairs ... requiring on-site tech work.'

**14. Gemini run 2 - criterion 45** (Draft states the West cluster must be QC walked before close)

> Draft West block, quoted by the judge itself: Jaime must 'conduct a final QC spot-check and issue a passing sign-off'. The judge quoted the passing text and still returned Fail.

**Do not file disputes on criteria 58 or 59** (7 cells). Those were rubric defects and are fixed at
source in section 1. Disputing text that no longer exists would be incoherent.

## 5. After upload

Re-request a verifier export and re-derive every per-cell count from it. Two independent regradings of
these identical trajectories moved 9.3% and 8.6% of decision cells in opposite net directions, and the
four edited criteria are no longer graded by the current export. Then run `PIPELINE COMPARE` against the
platform paste-back to catch silent platform-side mutation of the rubric text.
