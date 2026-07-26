# Bucket 2: Judge Error, contested run-cells (pass 4)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Basis:** `8a_Verifier_Fails_Opus.txt` (re-exported 16:18) + `8b_Verifier_Fails_Gemini.txt` (re-exported 16:19), cross-walked against `Agent_Responses/{Opus,Gemini}/` (unchanged since 10:50).

> **Supersedes** `_superseded/pass3_2026-07-26_1342/S4_judge_errors.md`.
>
> **Quoting policy.** Artifact text is quoted byte-exact, including em-dashes. An earlier
> revision of this file altered a verbatim agent artifact to satisfy the project's em-dash
> style rule, inside the one document whose purpose is proving what the artifact actually
> said. Style rules never apply inside a quoted span.

**0 criteria of 50 failing criteria are Bucket 2 at the criterion level.** No criterion has a majority of
its fail cells contested. **21 individual run-cells of 404 fail cells (5.2%)** were contested and are listed
below, spread across 12 criteria. Every entry quotes the exact artifact text the judge said was absent.

> **POST-FIX STATUS.** Groups A1 and A2 below (**7 cells** on the South-electrical and East-service criteria)
> are **no longer filed as appeals.** Both criteria were reclassified as Bucket 1 Overly Specific defects and
> fixed in place, because the same misreading recurred on five and three cells respectively and the title
> wording was inviting it. See `S4_fixes.md` entries B1-1 and B1-2. They are retained here as the evidence
> trail for that reclassification. **Remaining appeal set: 14 cells (Group B1 + Group C).**

Bucket 2 is scoped tightly. A cell is listed only where the artifact text contradicts the judge's stated
reason, or where the judge applied a requirement the criterion's own evidence field explicitly disclaims.
Borderline readings stay in Bucket 3.

---

## Group A: judge applied a requirement the evidence field explicitly disclaims

Two criteria carry evidence text that names what is *not* required. The judge required it anyway.

### A1. Electrical panel inspections recorded as finished (4 cells)

Evidence states: *"naming the record identifier is acceptable but is not required, and a response that
attributes the completion to the record titled Electrical panel inspections complete - South Cluster
wrap-up without repeating the word South also satisfies this criterion."* The only two FAIL conditions
given are (a) not reporting the inspections as recorded finished, and (b) asserting they were never
completed. Neither applies to these four cells.

**Opus run 1, final response.** Table row reads `| **South** | Electrical done; plumbing open | ...`, and
the actions list reads `Cluster records reconciled: North reopened, South electrical closed`. Judge:
*"the summary table only says 'Electrical done' without attributing it to the record."* Attribution to the
record is disclaimed by the evidence.

**Opus run 6, final response.** Table row reads `| **South** | Serviced; electrical confirmed (Patricia) |
**PASS** ...`. Judge: *"references electrical confirmation by Patricia, not that OPS-186 records South
electrical panel inspections as finished."* Patricia Nguyen is the person named inside the record itself.

**Gemini run 1, final response.** Text reads `**South Cluster**: **HVAC & Electrical Complete; Plumbing
Field Repairs Open**. Electrical panel inspections (Patricia) and HVAC run (Elias) are finished.` Judge:
*"only says 'HVAC & Electrical Complete' without specifically mentioning panel inspections as recorded
finished on a record."* The following sentence names panel inspections explicitly as finished.

**Gemini run 4, final response.** Text reports `OPS-186 was updated to Done confirming Patricia Nguyen's
completion of electrical panel inspections`. Judge: *"This is borderline, but the agent does report
electrica[l] ..."* and then returned Fail. The judge's own text concedes the criterion is met, and the
artifact names the record identifier as well. Internally inconsistent decision.

### A2. Crew recorded the East cluster HVAC service work as complete (3 cells)

Evidence states: *"Naming the coil cleaning alone satisfies this criterion"* and gives exactly one FAIL
condition: *"FAIL if the response treats the East cluster field work itself as never carried out."*

**Opus run 1, final response.** Table row reads `| **East** | Service done; **QC never run** | ...`.
Judge: *"treats East service as done but doesn't attribute the completion statement to the crew's
records."* Reporting the field work as done is exactly what the criterion asks; the sole FAIL condition
does not apply and crew attribution is not a stated requirement.

**Opus run 6, final response.** Table row reads `| **East** | Service done, handed to me | **NOT DONE** —
never inspected |`. Judge: *"only states 'Service done, handed to me' without explicitly reporting the
crew's recorded completion of the HVAC service work."* "Service done, handed to me" is the crew's recorded
completion, held separate from the QC verdict on the same row.

**Gemini run 1, final response.** Text reads `**East Cluster**: **Complete**. Coil cleanings and filter
swaps finished by Elias Navarro and verified via QC spot-check.` Judge: *"does not specifically state that
the crew recorded the East cluster HVAC service work (coil cleanings) as complete as a separate fact from
the unconfirmed QC."* The evidence says naming the coil cleaning alone satisfies the criterion. Lower
confidence than the two Opus cells, because this run also falsely asserts the QC passed. Logged for
completeness, not recommended for appeal.

---

## Group B: comment target resolved by internal id, judge read it as absent

### B1. Note on OPS-87 that the record does not stand as a close-out (1 cell)

Criterion evidence: *"The comment target may be identified either by the issue identifier or by the
record's internal id; both forms are accepted."*

**Opus run 4, tool call 35:** `save_comment(issueId="1d96db3b-56d6-4530-b2e6-afc6df6354c3", body="QC
close-out reconciliation (2026-07-01) - Jaime Salinas. This duplicates OPS-98 (same 5/25 South+North
spot-check). Same outcome: South pass holds; North sign-off withdrawn - two units flagged on my 5/23 walk
for immediate HVAC (coil/plumbing/panel) were never confirmed repaired or re-inspected. North re-work is
routed to the maintenance ticket log (MT-2026-1330) for a tech return + QC re-inspection. The North reopen
is tracked on OPS-98; leaving this open as a duplicate reference.")` returned success.

Judge: *"The trajectory shows no comment was written on OPS-87. The agent wrote comments on OPS-98,
OPS-99, OPS-96, OPS-186, OPS-79, and OPS-35, but not OPS-87. The final response claims a note was left on
OPS-87, but this is contradicted by the actual trajectory."*

`1d96db3b-56d6-4530-b2e6-afc6df6354c3` **is OPS-87.** Resolved from the issue-retrieval tool results in
this same run set, where the identifier and the uuid are returned as one pair. The judge listed six comment
targets for the run's six comment calls and mis-resolved this one as OPS-99. The run wrote no comment on
OPS-99 at all. Two errors compound: the target resolution, and the resulting accusation that the final
response misreports its own actions.

The comment body also satisfies the criterion on its merits. It withdraws the North sign-off and leaves the
record open, which is more than a restatement of the passing spot-check.

---

## Group C: artifact text states the required fact, judge reason contradicted verbatim

**Opus run 1, draft names East QC confirmation as a close condition.** Draft EAST section: `To close: I run
the East QC spot-check and it passes; condensate/compressor items cleared.` Closing summary: `Summary of
what stands between us and closing: North HVAC repairs, South plumbing, East QC + HVAC follow-ups, and West
completion`. Judge: *"The email draft does not name confirming the East cluster QC as what has to happen
before the push can close."*

**Opus run 1, draft names the person holding East QC confirmation.** Draft: `I've raised OPS-1000 (owned by
me) for the outstanding East QC`, then `To close: I run the East QC spot-check and it passes`, signed
`Thanks, Jaime`. The criterion's evidence explicitly accepts a first-person self-reference as naming Jaime
Salinas. Judge: *"does not name the East cluster QC holder ... because the East QC open item is not properly
identified in the draft."*

**Opus run 1, final response reports East QC unconfirmed rather than complete.** Table row `| **East** |
Service done; **QC never run** |`, and body text `OPS-99/OPS-108 record the East cluster as "QC passed /
Jaime confirmed" - I never ran that inspection.` Judge: *"does not clearly report the East cluster QC as
unconfirmed ... it conflates field work and QC status without a clear 'unconfirmed' verdict."* The artifact
separates the two on a single table row.

**Opus run 1, final response reports plumbing findings including the two water heaters still open.** Table
row `| **South** | Electrical done; plumbing open | 2 water heaters + hose bibs - John Smith (flagged by
Carlos) |`, and the actions list `MT-2026-1328 (South plumbing) ... all open, owners named`. Judge:
*"doesn't clearly report plumbing as still open"* while conceding the table *"marks South electrical as
Done"*. The same table cell reads `plumbing open`.

**Opus run 6, channel update states the East QC record is not in a completed workflow state.** Channel
message: `**East - service done, but QC never done.** Elias wrapped the service (OPS-99, In Review) and
handed it to me - I have not QC'd it.` Judge: *"does not specifically state that the East cluster QC record
is not in a completed workflow state."* The message names the record and its non-completed state.

**Opus run 6, draft names the person holding outstanding tenant access work.** Draft SOUTH section: `Open
before close: confirm the one earlier no-access unit (OPS-43) was actually serviced. Owner: Elias Navarro /
Carlos Mendez (access).` Judge: *"the draft does not identify tenant access work as an open item at all."*
It is carried as an open item with two of the three permitted owners named. Note that the two neighbouring
South-unit criteria fail correctly on this run, because the draft hedges to "confirm ... was actually
serviced" rather than stating the unit was never serviced. Only the owner-naming criterion is contested.

**Gemini run 6, channel update states the end-of-June target passed with work still open.** Channel
message, first line: `Team, the end-of-June target to close out the Preventive Maintenance Push has
passed.` Also: `my earlier sign-off does NOT hold for full closeout and this push cannot be closed yet`.
Judge: *"does not explicitly state that the end-of-June close-out target has passed with work still open.
The response summary does not show this framing in the posted Slack message."* Both halves are in the
posted payload. The judge reasoned from the run's summary rather than the sent message.

**Gemini run 4, channel update states plumbing findings including water heaters still open.** Channel
message under a `Plumbing` heading: `MT-2026-1327: Replace 2 aging water heaters past serviceable life
(High Priority)`, and `Overall Status: The PM Push remains OPEN until West Cluster PM scope is finished and
South Cluster plumbing repairs are completed.` Judge: *"It is not clear from the response that the channel
post explicitly states plumbing findings including the two water heater replacements are still open."*

**Gemini run 5, channel update states plumbing findings including water heaters still open.** Channel
message: `**South Cluster**: **HVAC & Electrical Complete; Plumbing Field Follow-Up Open**` and `Field
items flagged during Carlos's plumbing walk (2 water heater replacements, hose bib repairs) and 2
condensate drain flushes require tech dispatch.` Judge: *"The channel status update does not report the
plumbing findings, including the two water heater replacements, as still open."*

**Gemini run 5, final response reports plumbing findings including water heaters still open.** Final
response: `**South Cluster**: **HVAC & Electrical Complete; Field Follow-Up Open** ... Plumbing audit
flagged 2 water heater replacements and exterior hose bib repairs, plus 2 condensate drain flushes
requiring on-site tech work.` Judge: *"does not report the plumbing findings, including the two water
heaters needing replacement, as still open."*

**Gemini run 5, draft names East QC confirmation as a close condition.** Draft East Cluster block: `Status:
OPEN - Final QC Spot-Check Pending` and `Action Needed to Close: Jaime Salinas conducts final QC spot-check
walk and logs passing verification on OPS-1002.` Judge: *"The draft does not name confirming the East
cluster QC as what has to happen before the push can close."*

**Gemini run 5, draft names the person holding East QC confirmation.** Draft East Cluster block: `Who is
Holding It: Jaime Salinas (QC Inspector).` Judge: *"The East cluster QC section does not identify a
specific owner for the confirmation item."*

**Gemini run 2, draft states the West cluster must be QC walked before close.** Draft West block, quoted by
the judge itself: Jaime must `conduct a final QC spot-check and issue a passing sign-off`. The judge quotes
the passing text, writes *"This does partially mention a QC walk"*, and returns Fail. The criterion's
evidence asks only for a QC walk or spot-check of the West cluster named as a close condition.

---

## Cells checked and found genuine (not filed)

Examined because they moved Pass to Fail between the two gradings, and the fail is correct:

- **Opus run 3, East QC record state in the channel update.** Message says East is "NOT QC'd" with no statement about the record's workflow state.
- **Opus run 6, South no-access unit in the channel update and in the draft.** Both hedge to "confirm the earlier no-access unit got serviced" rather than stating it was never serviced for a missed access window. Correct fail on both South-unit criteria and on the re-scheduling close condition.
- **Opus run 1, as-found states of the three QC spot-check records.** The response lists what it did to each record but never reports their as-found workflow states.
- **Opus runs 1 and 6, portfolio filter run left unfinished.** Neither final response carries the unfinished filter run.
- **Opus run 5, West cluster QC coverage gap.** The response reports `HVAC - West | Complete (Lisa, OPS-91)`, which is the intended trap.
- **Gemini runs 2, 5, 6, West cluster QC coverage-gap tracking item.** The items raised concern West completion and trade audits, not QC coverage. The pass-3 grading of these three cells was the error, not this one.
- **Gemini run 4, latest dated status statement on the West cluster.** The message cites OPS-35 rather than the dated status statement that records West work as underway.
- **Gemini run 3, West QC coverage in the channel update.** "QC Spot-Check: Outstanding. QC spot-check cannot occur until field wrap-up is confirmed" sequences the QC rather than reporting the coverage gap. Defensible.
- **Gemini runs 3 and 5, closeability verdict in the final response.** Both list open items without reaching a closeability verdict, which the criterion's evidence names as a FAIL condition.
- **Gemini run 4, end-of-June target in the channel update.** The message opens "following up on the end-of-June target" without stating it has passed. Strict but defensible, unlike the run 6 cell where the text is explicit.

---

## Effect on all-failing status

One criterion is affected. **The East service-recorded criterion is graded 0/6 on Opus, and 2 of those 6
cells (runs 1 and 6) are contested above.** The criterion is demonstrably achievable: it passes 4 of 6
Gemini runs. It is therefore not presented as a clean model failure in the AF batch, and no rubric change
is warranted.

No Gemini all-failing criterion contains a contested cell. All 34 stand as genuine model failures.

## Appeal recommendation (post-fix)

**File Group B1 (1 cell) and Group C (13 cells): 14 cells of 404 (3.5%).** Each rests on artifact text that
contradicts the judge's stated reason word for word, which is the bar an appeal on this task has to clear given
the measured grader variance.

**Do not file Groups A1 and A2 (7 cells).** Those criteria were rewritten instead, so the next grading should
resolve them at source. Filing an appeal against text that no longer exists would be incoherent.

Strongest four in the remaining set:
1. `Opus run 4 / OPS-87 note` (Group B1) - a record-id resolution error, not a judgment call, and it produced a false accusation that the run misreports its own actions.
2. `Gemini run 5 / East QC owner` - the draft reads `Who is Holding It: Jaime Salinas (QC Inspector).`
3. `Gemini run 5 / East QC close condition` - the draft reads `Action Needed to Close: Jaime Salinas conducts final QC spot-check walk`.
4. `Gemini run 6 / end-of-June target` - the posted message's first line is the criterion.
