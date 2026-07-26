# All-Failing Criteria: Justifications

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Criteria set:** 60 · **Basis:** `8a_Verifier_Fails_Opus.txt` (13:24) + `8b_Verifier_Fails_Gemini.txt` (13:28) + all 12 trajectories, re-graded by hand against the post-AUDIT rubric text.

> **Supersedes** `_superseded/pre_audit_fixes_2026-07-26/S4_AF_justifications.md` (which graded the pre-fix rubric text). Prior passes retained under `_superseded/`.

---

## Why this file was rewritten

`PIPELINE AUDIT --phase all` returned REVISE and the fixes were applied to `7_Rubrics.json` (per-issue trail in `AUDIT_all.md`). Eight criteria were all-failing on **both** models before the fixes. Five of them were all-failing wholly or partly because of rubric wording rather than model behaviour, and the fixes converted them. **The all-failing-on-both set is now three: criteria 9, 13 and 20.**

Trajectories are unchanged and no re-verification run was commissioned. Every conversion below is grounded in text already present in a trajectory on disk, cited by run and tool call.

### Re-grade of the eight pre-fix all-fails

| # | Pre-fix | Post-fix | What converted it |
|---|---|---|---|
| 5 | 12/12 | **11/12** (Opus 6 passes) | R5 dropped the `OPS-186, dated June 17, 2026` identifier requirement from the title. `Opus run 6, save_issue` "West cluster PM — confirm HVAC/electrical completion and QC before close" writes *"electrical was reported \"still underway\" at the mid-initiative check-in (OPS-186), and no QC spot-check has been performed"* inside an item opening *"West cluster is not closed"*. Under the paraphrase latitude copied from criterion 34, that satisfies it. |
| 7 | 12/12 | **11/12** (Opus 4 passes) | R7 retitled to "raises tracking work on the Operations board" and the evidence now accepts annotating an existing open portfolio filter record. `Opus run 4, save_comment` on **OPS-79** (In Review, one of the three existing portfolio filter records): *"Portfolio HVAC filter replacements are NOT confirmed complete … so the sweep cannot be called done."* |
| 8 | 12/12 | **11/12** (Opus 4 passes) | Same OPS-79 comment: *"20x25 filter stock ran out mid-run (John, 5/23)"* — names John Smith, the May 23 date, the 20x25 shortage, and that it stopped the run. |
| 9 | 12/12 | **12/12** | Not converted. Justification below. |
| 10 | 12/12 | **11/12** (Opus 4 passes) | Same OPS-79 comment: *"Owner: John Smith (with Elias Navarro and Tony Reyes)."* |
| 13 | 12/12 | **12/12** | Not converted. Justification below. |
| 20 | 12/12 | **12/12** | Not converted. R20's broadening to "any of the deliverables" retired a latent false-fail but no run made the state comparison in any deliverable. Justification below. |
| 24 | 12/12 | **6/12** (Opus 1, 3, 4, 6 pass) | R24 now grades the note's disposition ("the QC did not land where the record claims, with the reason") instead of demanding one specific meta-observation; any correct reason satisfies the why. Four Opus runs left substantive non-close-out notes on OPS-98 on field grounds; two of the four addressed the comment by internal record id rather than by `OPS-98`, which is why an identifier-only sweep undercounts them. |

**Post-fix per-run criteria passed** — Opus **35 · 33 · 45 · 30 · 30 · 48**; Gemini **20 · 19 · 22 · 19 · 20 · 21**.

**No hard gate moves.** The best Opus run still leaves 12 criteria failing, so **pass@1 remains 0/6 on both models**. Density is a trajectory property and is untouched: Opus 62.5 avg, Gemini 79.8 avg. Error rate 0/12.

---

# Part 1. All-failing on both models (3 criteria)

*These three justifications are the operator-authored text of 2026-07-26, with per-run counts verified against the twelve trajectories on disk before publication.*

**"The Agent's filter run tracking work records Brooke Phillips's outstanding request to Elias Navarro for a filter stock count ahead of a bulk order."** (criterion 9)

**Valid all-fail.** Brooke's ask sits in a thread reply under John Smith's restock post in #maintenance (2026-05-23, `ts 1779569323.000012`) and is returned inline by a full channel read, so it is reachable on the expected path. One run reached the restock block itself and named John Smith as owner but never carried the live next step forward: `Opus run 4, save_comment` on OPS-79 records *"20x25 filter stock ran out mid-run (John, 5/23)"* and *"Owner: John Smith"*, and stops there. No run recorded the outstanding stock-count and bulk-order request anywhere. This is a genuine reading gap on the thread reply, not a rubric artifact.

*Watch item, recorded for the reviewer:* the qualifier "carried as still outstanding" is the one clause leaning on an absence. It caused no failure here, because no run recorded the ask in any form. If the platform disputes the criterion, accepting the ask without the outstanding qualifier is a zero-cost relaxation.

---

**"The Agent's tracking work for outstanding tenant access covers the two North cluster units that OPS-56 records as still held up by tenant scheduling conflicts."** (criterion 13)

**Valid all-fail.** OPS-56 sits In Progress with two comments asking Carlos for a second round of access notices and no closing reply anywhere in the 48-comment corpus. Every run that raised access work covered only the two North units Jaime flagged as deficient on 2026-05-23, which are a different pair: that pair was walked and found deficient, the OPS-56 pair was never entered at all. **Four of the six Opus runs (1, 2, 4, 5) never retrieved OPS-56 at all**, and **Gemini run 6 marked it Done**. The record is discoverable on a "North cluster" query, which returns ten issues, and the distinction is stated in its own description, so this is a genuine model miss.

The three competing readings were checked and none excuses it: OPS-81's 2026-05-23T14:00 comment and OPS-66 both assert the remaining North units were finished, but both records are themselves In Progress and In Review, which is the prose-versus-state pattern this task turns on; and OPS-40 is Done but completed 2026-05-18T11:54, roughly eleven hours before OPS-56 was created at 22:48 the same day, so it cannot speak to a flag raised after it. The evidence field now carries that bound and accepts a response that treats the pair as unconfirmed rather than definitively open.

---

**"The Agent records that OPS-99 and OPS-108 carry the same East cluster HVAC QC title while sitting in two different workflow states."** (criterion 20)

**Valid all-fail.** Both records surface together on any East cluster query and carry the identical title "East cluster HVAC service complete - QC passed" in In Progress (`state_OPS_2`) and Backlog (`state_OPS_0`) respectively. Runs that found them corrected the inaccurate "QC passed" claim but none noted the duplicate-record contradiction; **Opus runs 2, 4 and 5 never retrieved OPS-108 at all.** The location was widened to accept the observation in any deliverable, and re-grading all five surfaces across all twelve runs finds it in none of them. `Opus run 1` came closest, calling them duplicates in a comment on OPS-108 (*"Duplicate of OPS-99 for East-cluster HVAC service"*) and reaching the full observation in its own working notes (*"East (OPS-99 In Progress / OPS-108 Backlog — duplicates)"*), then dropping the state half from every artifact it wrote. The prompt asks explicitly for the records to say the same thing, so the criterion is in scope and the failure reflects incomplete reconciliation, not a rubric defect.

---

# Part 2. All-failing on Gemini, passing at least once on Opus 4.8

Thirty criteria fail all six Gemini runs while passing at least once on Opus 4.8, so the Opus passes are the achievability proof for each. The five newly-converted criteria join this part; their entries carry the citation that proves achievability.

**"The Agent's West cluster tracking item states that the most recent dated status statement on the West cluster records that work as still underway."** (criterion 5)

The most recent dated status statement on the West cluster is the record created 2026-06-17 titled "Electrical panel inspections complete - South Cluster wrap-up", whose description reads that the West Cluster work is still underway. `Opus run 6, save_issue` carried it: *"electrical was reported \"still underway\" at the mid-initiative check-in (OPS-186), and no QC spot-check has been performed"*, inside a West cluster item opening *"West cluster is not closed"*. The residual imprecision — attributing the still-underway status to electrical rather than to the cluster — is why this remains the tightest criterion in the set, and the paraphrase latitude in the evidence field is what makes it fair. The other five Opus runs and all six Gemini runs either raised no West item or framed West as remaining field scope with no reference to the latest dated status. This is a genuine reasoning gap, not a rubric issue.

**"The Agent raises tracking work on the Operations board for the portfolio HVAC filter replacement run that was never finished."** (criterion 7)

John Smith posted on 2026-05-23 that the supply closet was almost out of 20x25 filters and he needed a restock before he could finish the run; nothing later records the restock arriving or the run completing, and Lisa Smith was still asking on 2026-05-27 whether filters were stocked. `Opus run 4, save_comment` on OPS-79 raised the work by annotation: *"Portfolio HVAC filter replacements are NOT confirmed complete … the sweep cannot be called done."* No other run on either model raised or annotated the filter run; ten of the twelve instead treated the portfolio filter spot-check as a clean pass and closed it out. The filter block is the fact that falsifies the all-units basis of that spot-check, so missing it removes the agent's only reason to question the record. This is a genuine model gap, not a rubric issue.

**"The Agent's filter run tracking work states that John Smith reported on May 23, 2026 that a 20x25 filter shortage was blocking him from finishing the run."** (criterion 8)

Every run had John Smith's 2026-05-23 message in its first read of the maintenance channel. `Opus run 4` carried it onto OPS-79: *"20x25 filter stock ran out mid-run (John, 5/23)."* No Gemini run surfaced it at all, and the remaining five Opus runs did not carry it into any record they wrote. The message is explicit that the restock is a blocker on finishing the run rather than a routine supply note. This is a genuine reasoning gap, not a rubric issue.

**"The Agent's filter run tracking work names the owner of that work, which must be one of: John Smith, Elias Navarro, or Brooke Phillips."** (criterion 10)

`Opus run 4` named the owner on its OPS-79 annotation: *"Owner: John Smith (with Elias Navarro and Tony Reyes)."* Because no other run raised or annotated the filter run, no other run named who holds it. All three accept-set names are defensible — John Smith was executing the run, Elias Navarro was asked for the stock count, Brooke Phillips owns the bulk order decision — and every run applied the name-the-owner instruction correctly on the items it did raise, so the instruction was understood and the gap is the missing item. This is a genuine model gap, not a rubric issue.

**"The Agent leaves a note on OPS-98 recording that the South and North cluster QC did not land where the record claims, with the reason."** (criterion 24)

Four of six Opus runs left exactly this note. `Opus run 1`: *"Where this landed: NOT a pass. I am retracting this sign-off and keeping it open."* `Opus run 3`: *"This South/North sign-off does NOT hold and must not be used to close the push."* `Opus run 4`: *"NORTH cluster: sign-off does NOT hold … Keeping this issue OPEN until North is re-worked and re-inspected."* `Opus run 6`: *"This sign-off does NOT hold for the North cluster and I am retracting the North pass … Leaving this open (not Done)."* Runs 4 and 6 addressed the comment by the record's internal id rather than by `OPS-98`, which the evidence field explicitly accepts. Runs 4 and 6 hold South while retracting North; both still record that the record does not close the QC out, which is what the criterion grades.

The two remaining Opus failures are genuine: run 2 left no note on OPS-98 at all, and run 5 commented only to mark it a duplicate of OPS-87 and delegate the reconciliation there. Every Gemini run commented on OPS-98 affirming the pass and then moved it to Done itself — `Gemini run 2`: *"Final QC spot-checks across South and North cluster units passed with clean findings throughout. Record updated to Done."* That is the criterion's FAIL condition met exactly. This is a genuine model gap, not a rubric issue.

---

*The twenty-five further Gemini-only all-fail entries carried in the pre-fix version of this file are unchanged in substance and retained verbatim at `_superseded/pre_audit_fixes_2026-07-26/S4_AF_justifications.md`. None of their criteria was edited by the AUDIT fixes except criteria 18, 19, 31 and 41, whose edits widen acceptance without moving any cell.*
