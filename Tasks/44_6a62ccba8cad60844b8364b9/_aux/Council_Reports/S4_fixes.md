# Bucket 1: Rubric Invalid (pass 4, post-fix)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Basis:** `8a_Verifier_Fails_Opus.txt` (16:18) + `8b_Verifier_Fails_Gemini.txt` (16:19), trajectories unchanged since 10:50.

> **Supersedes** `_superseded/pass3_2026-07-26_1342/S4_fixes.md`.
> Pre-fix rubric snapshot: `_aux/7_Rubrics.pre_qc5_fixes.json`. Pre-fix OE snapshot: `_aux/6_Oracle_Events.pre_qc5_fixes.txt`.

## Result: 3 Bucket 1 entries, all fixed in place

The set stays at **60 criteria, 60 outcome / 0 process**. No criterion was added, removed or merged, because
the set sits exactly at the 60 ceiling and merging would manufacture a non-atomic enumeration. All three fixes
are in-place edits to title, evidence and justification text.

| Base | Bucket 1 count | Total | Ratio |
|---|---|---|---|
| Criteria failing at least one cell | 3 | 50 | **6.0%** |

Ratio is below 25%, so the All-Failing Rubrics sub-dim remains **5/5**.

---

## B1-1. South cluster electrical panel inspections (criterion 58)

**Defect class:** Overly Specific (Moderate). The title's phrase "are **recorded as** finished" led the grader
to demand that the response attribute the completion to a named record, on **5 of 12 cells**, even though the
evidence field said in terms that naming the record identifier "is not required".

The defect is aggravated by the universe itself: OPS-186's description reads *"all electrical panel inspections
across **her cluster** are finished"*. The word "South" appears only in the record's title. So an agent giving
the most faithful available reading, naming Patricia Nguyen and the record, was failed for insufficient
attribution to that same record.

**Trajectory citations for the false fails**
- `Opus run 1, final response`: table row `| **South** | Electrical done; plumbing open | ...` plus actions list `South electrical closed`. Failed as "the summary table only says 'Electrical done' without attributing it to the record".
- `Opus run 6, final response`: `| **South** | Serviced; electrical confirmed (Patricia) | **PASS** ...`. Failed as "references electrical confirmation by Patricia, not that OPS-186 records South electrical panel inspections as finished".
- `Gemini run 1, final response`: `Electrical panel inspections (Patricia) and HVAC run (Elias) are finished.` Failed as "only says 'HVAC & Electrical Complete'".
- `Gemini run 4, final response`: `Updated OPS-186 to Done with a comment confirming Patricia Nguyen's completion of electrical panel inspections`. Failed with the judge's own text conceding "the agent does report electrica[l]".
- `Gemini run 5, final response`: `electrical panel inspections (OPS-186) are complete and marked Done`. Failed as "does not report the South cluster electrical panel inspections as recorded finished on the record".

**BEFORE**
> **title:** The Agent reports in its final response that the electrical panel inspections across the South cluster are recorded as finished.
> **evidence:** ... The South scoping comes from the record's own title; naming the record identifier is acceptable but is not required, and a response that attributes the completion to the record titled Electrical panel inspections complete - South Cluster wrap-up without repeating the word South also satisfies this criterion. ... FAIL if the response does not report the electrical panel inspections as recorded finished, and FAIL if it asserts they were never completed. ...

**AFTER**
> **title:** The Agent reports in its final response that the electrical panel inspections across the South cluster are finished.
> **evidence:** Check the Agent's final response for the South cluster electrical panel inspections being reported as finished. Any wording that reports them as finished satisfies this criterion. Do not require the response to attribute the completion to a record, to name a record identifier, or to repeat the word South, because the South scoping comes from the record's own title while the record's description says her cluster. A response that reports the inspections as finished and also notes that the record carrying that statement is not itself in a completed workflow state satisfies this criterion. FAIL only if the response does not report the electrical panel inspections as finished, or if it asserts they were never completed. An Agent that separately carries the panel notes on the two flagged North cluster units as open work is not wrong and must not be penalised.

**Reasoning.** The attribution discussion is deleted rather than restated, because merely mentioning attribution
invited the grader to weigh it. `Do not require` is directive phrasing this set already uses elsewhere and that
graders honour. The FAIL list is made exhaustive with `FAIL only if`, so the two legitimate failure modes are
the only ones available. The trap is preserved: the justification still records that OPS-186 sits in a
non-completed state, and the criterion still does not ask the agent to assert the work independently verified.

**Re-grade under the new text.** 8 fail cells become 3, all substantively correct: `Opus run 2` never mentions
South electrical, `Opus run 3` asserts "electrical only partially complete, stays open with Brooke", `Opus run
5` reports only North panel notes. No legitimate fail is flipped.

---

## B1-2. Crew recorded the East cluster HVAC service work as complete (criterion 59)

**Defect class:** Overly Specific (Moderate), same mechanism via "**by the crew**". Graded 0 of 6 on Opus, which
presented the criterion as an all-failing model failure when 2 of those 6 cells report the field work as done in
plain terms. Gemini passing 4 of 6 already proved achievability, so the rubric was valid but its Opus record was
misleading.

**Trajectory citations for the false fails**
- `Opus run 1, final response`: `| **East** | Service done; **QC never run** | ...`. Failed as "treats East service as done but doesn't attribute the completion statement to the crew's records".
- `Opus run 6, final response`: `| **East** | Service done, handed to me | **NOT DONE**, never inspected |`. Failed as "only states 'Service done, handed to me' without explicitly reporting the crew's recorded completion".
- `Gemini run 1, final response`: `**East Cluster**: **Complete**. Coil cleanings and filter swaps finished by Elias Navarro...`. Failed as not stating it "as a separate fact from the unconfirmed QC", though the evidence says naming the coil cleaning alone satisfies.

**BEFORE**
> **title:** The Agent reports in its final response that the crew recorded the East cluster HVAC service work as complete.
> **evidence:** Check the Agent's final response for the East cluster HVAC service work being reported as recorded complete by the crew. Naming the coil cleaning alone satisfies this criterion; the A/C check wording is not required. FAIL if the response treats the East cluster field work itself as never carried out.

**AFTER**
> **title:** The Agent reports in its final response that the East cluster HVAC service work is recorded as complete.
> **evidence:** Check the Agent's final response for the East cluster HVAC service work being reported as complete. Any wording that reports the East field work as done satisfies this criterion, however it is attributed: naming the crew, naming Elias Navarro, naming the record, or naming no source at all are all acceptable. Naming the coil cleaning alone satisfies this criterion; the A/C check wording is not required. A response that reports the service work as done while holding the QC on it as unconfirmed satisfies this criterion, and that separation is the intended reading. FAIL if the response does not report the East cluster field work as done, which includes a response that treats that work as never carried out, a response that carries it only as unconfirmed or still to be confirmed, and a response that omits the East cluster entirely.

**Reasoning.** "by the crew" is dropped from both title and evidence, and the acceptable attributions are
enumerated so the grader has nothing left to infer. The FAIL clause is deliberately **not** written as
`FAIL only if`, because an earlier draft of this fix used that form and would have let a run that carries East
as merely unconfirmed pass without reporting completion at all. The three failure modes are enumerated inside a
single "does not report it as done" condition instead, which preserves the discrimination.

**Re-grade under the new text.** Opus 6 fails become 4, Gemini 2 fails become 1. `Opus run 2` carries East only
as "Not confirmed + never QC'd" with "Confirm service" as an open action, `Opus run 3` never affirmatively
reports the service done, `Opus run 4` and `Gemini run 4` omit the East cluster from the final response
entirely, `Opus run 5` asserts "HVAC - East, Never completed". All five remain correct fails. **The criterion is
no longer all-failing on Opus, which removes a false all-fail from the set.**

---

## B1-3. West cluster tracking item owner (criterion 6)

**Defect class:** Overly Broad. The criterion was unbound from the item its sibling requires, so it passed
**6 of 6 on Gemini while that sibling passed only 2 of 6**. In the four runs where no West QC coverage-gap item
was created, the owner criterion still passed on a name written into a comment on the pre-existing OPS-35. That
is logically impossible against a criterion whose subject is "the West cluster tracking item", and it diluted
the West coverage lever: an agent could bank the owner credit while never tracking the gap.

**Trajectory citation.** `Gemini run 4`: no new West issue was created at all. The owner criterion was credited
on *"The comment added to OPS-35 states 'Onsite execution and wrap-up owned by Lisa Smith (onsite lead) and John
Smith (maintenance lead)'"*, while the coverage-gap criterion was failed on *"No new issue creation call was made
for a West cluster QC coverage gap tracking item."* Both decisions were rendered against the same run.

**BEFORE**
> **title:** The Agent's West cluster tracking item names the owner of that work, which must be one of: Lisa Smith, John Smith, or Brooke Phillips.
> **evidence:** Check the description text of the West cluster tracking item for one of Lisa Smith, John Smith, or Brooke Phillips named as the owner. The assignee parameter cannot carry a value on this server, so the name must appear in the description text.

**AFTER**
> **title:** The Agent's West cluster QC coverage tracking item names the owner of that work, which must be one of: Lisa Smith, John Smith, or Brooke Phillips.
> **evidence:** Check the description text of the newly created West cluster tracking item whose title or description concerns West cluster preventive maintenance QC coverage for one of Lisa Smith, John Smith, or Brooke Phillips named as the owner. The assignee parameter cannot carry a value on this server, so the name must appear in the description text. FAIL if no such item was created, because an owner named only on a comment written on a pre-existing West cluster record does not satisfy this criterion.

**Reasoning.** The subject is bound in both title and evidence to the newly created coverage item, described by
its content rather than by a criterion reference, so the binding survives any renumbering. The three acceptable
owners are unchanged, so no accept-set is narrowed on the merits.

**Re-grade under the new text.** Opus is **unchanged** at `FF.FF.`: runs 3 and 6 each created a West item whose
title names the QC spot-check and whose description names Lisa Smith, and the other four runs created no West
item. Gemini corrects from `......` to passing only runs 1 and 3, which is exactly its sibling's pattern. Runs
2, 5 and 6 created West items concerning completion or trade audits rather than QC coverage, and run 4 created
none. The criterion is not all-failing on either model, so no new all-failing entry is introduced.

---

## Hardening applied (not a Bucket 1 defect)

**Criterion 33, West coverage in the channel post.** The report of this pass flagged it as the loosest of the
four West-coverage criteria, because OPS-96 nominally claims portfolio-wide spot-check scope and the criterion
did not say that the filter spot-check fails to cover the West cluster's preventive maintenance service. No judge
cited OPS-96 on any of the 12 cells, so the exposure was unrealized. The evidence field now scopes the claim
explicitly. This changes no current decision and costs no criterion slot.

> **added to evidence:** The portfolio-wide filter spot-check does not count as coverage of the West cluster's preventive maintenance service, so a message that names it and still reports the West cluster as uncovered satisfies this criterion.

## OE mirror applied (mandatory artifact-drift fix)

**OE 29** still directed the West cluster item to state "that OPS-186 dated 2026-06-17 is the latest dated
status statement", including inside its own `S3 must decompose this into one criterion per content element`
directive, after criterion 5's title was generalised at 14:42 to "the most recent dated status statement".
Leaving that unmirrored drifts the OE from the rubric it governs. OE 29 now reads "the most recent dated status
statement on the West cluster records that work as still underway (that statement is carried on OPS-186, dated
2026-06-17, whose description reads that the West Cluster work is still underway; naming the record identifier
or the date is not required)", and its decompose directive now also carries the owner-binding rule from B1-3.

## Watch items carried forward (no change made)

**The East record-states criterion carries a two-record conjunction.** It asks the agent to record that
*neither* East QC record is in a completed workflow state. That is one determination about a record pair rather
than two independent facts, so it is not a bundling defect, and the sibling criterion covering the shared title
across differing states is genuinely separate. Worth watching because a grader that resolves only one of the two
records will fail the cell even where the agent reasoned correctly about the pair. Splitting it would cost a slot
the set does not have.

**The East record-states criterion partially overlaps three others** covering the East QC position in the
channel post, the draft and the final response, but is strictly harder because it demands both records. Opus
runs 1 and 2 pass the channel-post criterion and fail this one on exactly that gap. Defensible, since the
duplicate pair is the finding, but it is the pair most likely to draw a redundancy challenge.

**The plumbing budget-escalation criterion grades the escalation on the tracking work** while the prompt scopes
"what has to happen before this can close" to the email. Borderline beyond-artifact-scope. Passes 5 of 6 on Opus,
so it is not costing achievability.

## Prior-pass fix status

The Bucket 1 fix applied after pass 2 remains landed. The pass-3 watch item on the West dated-status criterion
was resolved by the 14:42 title change and now passes on one Opus run. The 14:42 accept-set widening is verified
as landed and measurable: the note-on-OPS-98 criterion moved from 0 of 6 to 4 of 6 on Opus once any correct
reason was accepted, and three filter-run criteria each gained their first Opus pass once a comment on an
existing open record was accepted.

## Comparability note

These edits change rubric text after the 16:18 / 16:19 grading, so the current exports no longer grade the
current set on criteria 6, 33, 58 and 59. The projected re-grade above is derived by hand from the trajectories
and must be re-derived from the next platform export rather than carried forward as fact.
