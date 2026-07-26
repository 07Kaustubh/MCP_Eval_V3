# Bucket 1: Rubric Invalid (fixes)

**Task:** `Tasks/44_6a62ccba8cad60844b8364b9` · **Universe:** starpm · **Framework:** V4 (dual-model)
**Date:** 2026-07-26 · **Criteria set:** 60 · **Basis:** `8a_Verifier_Fails_Opus.txt` + `8b_Verifier_Fails_Gemini.txt` as re-exported 2026-07-26 12:04, graded against the current 60-criterion set, cross-walked against `Agent_Responses/{Opus,Gemini}/`.

> **Supersedes** `_superseded/S4_fixes.md`. That file was written against an earlier `8a` export that did not match the Opus trajectories on disk. See `S4_verdict.md` for the reconciliation.

---

## Summary

**1 criterion of 52 failing criteria (1.9%) is classified Bucket 1.**

The three fixes proposed in the superseded file (tenant-access container, plumbing container, QC-record states) were **already applied** to `7_Rubrics.json` before the re-graded verifier output arrived, and the re-grade confirms all three: the plumbing container now passes 12/12, and the other two still discriminate (tenant access 3/6 Opus and 6/6 Gemini; QC-record states 4/6 Opus and 6/6 Gemini). Nothing is rolled back.

---

## B1-1: East cluster QC holder: the accept-set does not admit a first-person self-reference

**Criterion (idx 48, title unchanged by this fix):**
> The Agent's draft to Brooke Phillips names the person holding the East cluster QC confirmation, which must be one of: Elias Navarro, Jaime Salinas, or Brooke Phillips.

**Fail record.** Opus 3/6 (runs 2, 4, 5) · Gemini 6/6.

**Trajectory citation.** `Opus Run 2, tool call 54 (create_draft)`: the EAST CLUSTER section of the draft body reads "East QC is raised as its own item (OPS-1000), **owned by me**, blocked until service is confirmed", and the draft is signed "Thanks, Jaime". The holder named is Jaime Salinas, expressed in the first person by the sender of the email. The verifier failed the cell with "It says the QC needs to be confirmed but does not name who holds that work."

**Why this is the criterion and not the model.** The prompt asks for an email from Jaime saying "who is holding it". When the holder is the sender, a first-person "owned by me" in a signed email is the natural business expression and is unambiguous to the recipient. The criterion's accept-set is a list of proper names, so a correct answer written in the only voice the prompt allows can fail it. That is the phrasing-fails-a-valid-expression shape. The two sibling holder criteria (West cluster, tenant access) have accept-sets that do not include Jaime Salinas, so the defect does not propagate.

**5-point checklist.** Q2 = **NO** (does not allow a valid alternative expression). Q1, Q3, Q4, Q5 = YES. One NO, so this is reclassified out of Bucket 3.

**Fix: evidence field only. Title, category and justification unchanged.**

*Before:*
> Check the draft body for one of Elias Navarro, Jaime Salinas, or Brooke Phillips named as holding the outstanding East cluster QC confirmation.

*After:*
> Check the draft body for one of Elias Navarro, Jaime Salinas, or Brooke Phillips named as holding the outstanding East cluster QC confirmation. Because the draft is written and signed by Jaime Salinas, a first-person self-reference that assigns the outstanding East cluster QC to the sender, for example wording that says the item is owned by me or that I will run it, satisfies this criterion as naming Jaime Salinas.

**Impact of the fix, recomputed against the same twelve trajectories.** One cell flips: Opus run 2 Fail to Pass. Opus goes 3/6 to 2/6 failing; Gemini stays 6/6, because no Gemini draft assigns the East QC to anyone in first person. The criterion keeps its discrimination on both models and pass@1 is unchanged at 0/6 on both.

**Cross-artifact check.** No Oracle Event edit needed. No OE decomposition directive names an element that this fix removes; the fix only widens an accept-set expression.

**Cross-reference.** One further cell on this criterion, `Gemini Run 5`, is a judge error rather than a phrasing gap: that draft names "Jaime Salinas (QC Inspector)" in full under "Who is Holding It" for the East cluster. It is logged in `S4_judge_errors.md` and needs no fix.

---

## Criteria examined and deliberately NOT reclassified to Bucket 1

Recorded so the Bucket 1 count is auditable rather than merely small.

| Criterion | Fail record | Why it stays out of Bucket 1 |
|---|---|---|
| Plumbing item owner accept-set (Carlos Mendez / Brooke Phillips) | Opus 1/6, Gemini 0/6 | `Opus Run 1, tool call 9`: the ticket reads "Owner: John Smith (execution); flagged by Carlos Mendez". Carlos appears, but as the flagger. Widening the accept-set to add John Smith would dilute a criterion eleven of twelve runs pass, and the records tie the plumbing work to Carlos for coordination and Brooke for budget. Genuine miss. |
| South electrical recorded finished | Opus 4/6, Gemini 4/6 | Four of eight fail cells are judge errors against evidence that already grants the latitude the judge withheld. The only title change that would help, dropping the recorded-as hedge, would reintroduce the overclaim the criterion was written to avoid, because OPS-186 itself sits in Todo. Bucket 2, not Bucket 1. |
| Crew recorded East HVAC service complete | Opus 4/6, Gemini 4/6 | Six of eight fail cells are genuine: those runs asserted the East field work was never carried out, which the criterion's own FAIL clause targets. Two disputed cells are logged as judge errors. |
| West cluster tracking item for the QC coverage gap | Opus 4/6, Gemini 4/6 | Two Gemini passes and two Opus passes prove achievability. The fails are runs that raised a West item about finishing PM work rather than about the missing spot-check, which is the distinction the criterion exists to draw. |
| Tenant-access container and its two content criteria | Opus 3/6, Gemini 6/6 | Already carries the either-destination latitude applied earlier this phase. The remaining fails are runs that logged no tenant-access work anywhere. |
