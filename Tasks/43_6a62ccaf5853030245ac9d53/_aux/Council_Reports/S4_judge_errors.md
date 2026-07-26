# Bucket 2 — Judge Errors · Task 43_6a62ccaf5853030245ac9d53 (StarPM V4, dual-model)

Rubric-level Bucket 2 count: **0**. No rubric is mis-scored across the board.

Run-cell-level judge errors: **6 cells** (2 wrong-FAIL, 4 wrong-PASS). Recorded here because the S4 spec requires every failing cell to carry a trajectory citation and because the wrong-PASS cells inflate the apparent pass counts in the run matrix.

---

## A. Wrong FAIL (appealable) — 2 cells

### `rubric[3]` "The Agent identifies the Mesa Vista 4C bedroom closet trim touch-up on the vendor bill as $85." — Opus Run 2, Opus Run 3

**The judge applied the evidence field's vendor attribution inconsistently across the six Opus runs.** The criterion title asks only that the agent identify the trim touch-up on the vendor bill as $85. The evidence field adds "as the amount Permian Make-Ready Crew billed StarPM". The judge enforced that vendor attribution on Runs 2 and 3 and did not enforce it on Runs 1, 4 and 6, which stated the same $85 with the same non-Permian attribution and were passed.

| Run | Verdict | What the final response actually said |
|---|---|---|
| Opus Run 1 | **Pass** | `Closet trim touch-up \| $95.00 \| $85.00 (2026-519) \| Tony Reyes (tony.reyes@starpm.com, Lead Maint Tech) \| Internal labor` |
| Opus Run 2 | **Fail** | `Closet-trim touch-up \| $85.00 (2026-519) — Tony Reyes/Jaime/Carlos, all @starpm.com \| In-house labor` |
| Opus Run 3 | **Fail** | `Closet-trim closeout (bill 2026-519 = $85)` |
| Opus Run 4 | **Pass** | `Closet-trim touch-up (inv 2026-519, $85): billed TO Tony Reyes; all in-house staff time` |
| Opus Run 5 | **Pass** | `2026-519 ($85, Permian Make-Ready Crew) — closet trim` |
| Opus Run 6 | **Pass** | `Closet trim touch-up — Tony Reyes, in-house crew, bill 2026-519 ("Internal labor charge"): $85.00` |

Runs 1, 4 and 6 named Tony Reyes rather than Permian Make-Ready Crew and passed. Runs 2 and 3 did the same thing and failed. Only Run 5 actually named Permian. Trajectory citation for the two disputed cells:

- `Opus Run 2, tool call 5 (search_bills "Mesa Vista 4C")`: returned bill `546359391323`, `TotalAmt 85.0`, `DocNumber 2026-519`, `VendorRef.name "Permian Make-Ready Crew"`. The final response then states `$85.00 (2026-519)` in the "Vendor AP bill (what we paid)" column of its reconciliation table.
- `Opus Run 3, tool call 5 (search_bills "Mesa Vista 4C")`: same record returned. Final response states `bill 2026-519 = $85`.

**Disposition:** appealable on consistency grounds. The two cells do not change any verdict in this report, because the rubric fails on six Gemini runs for a substantive reason (those runs never state $85 anywhere) and stays Bucket 3 at the rubric level either way.

**Caveat worth stating plainly:** Opus Run 3's response also fabricates a breakdown of the $85 bill into "Jaime's QC walk $35 + Carlos's routing $20 + Tony's in-house touch-up $25 + Carlos's Airtable update $5". No such breakdown exists in the data; the bill carries one line. A judge could reasonably fail Run 3 on that basis. The appeal is therefore strong for Run 2 and weaker for Run 3.

---

## B. Wrong PASS (not appealable, recorded for matrix integrity) — 4 cells

### `rubric[14]` "The Agent updates the Mesa Vista 4C make-ready record that carries the Ready turn status." — Opus Run 2, Opus Run 4
### `rubric[16]` "The Agent states in the Mesa Vista 4C make-ready record carrying the Ready turn status that the 4C turn is closed on the owner side." — Opus Run 2, Opus Run 4

The evidence field for `rubric[14]` is explicit: "An Agent that also brings the stale In Progress row into line still satisfies this criterion; an Agent that updates only the stale In Progress row does not." Per OE 3, `recc8534b3fd13954` is the live Ready row and `recbd087a4abd605b` is the stale In Progress snapshot.

Airtable write targets, all twelve runs:

| Run | `update_records_for_table` targets | Correct? | Verdict given |
|---|---|---|---|
| Opus 1 | c31 `recc8534b3fd13954`, c32 `recbd087a4abd605b` | yes (both) | Pass |
| **Opus 2** | **c39 `recbd087a4abd605b` only** | **no (stale only)** | **Pass (wrong)** |
| Opus 3 | c32 both | yes | Pass |
| **Opus 4** | **c49 `recbd087a4abd605b` only** | **no (stale only)** | **Pass (wrong)** |
| Opus 5 | c32 both | yes | Pass |
| Opus 6 | c24 `recc8534b3fd13954`, c25 `recbd087a4abd605b` | yes | Pass |
| Gemini 1 | c30 both | yes | Pass |
| Gemini 2 | c32 both | yes | Pass |
| Gemini 3 | c34 `recbd087a4abd605b` only | no (stale only) | **Fail (correct)** |
| Gemini 4 | c40 both | yes | Pass |
| Gemini 5 | c31 both | yes | Pass |
| Gemini 6 | c32 both | yes | Pass |

Gemini Run 3 did exactly what Opus Runs 2 and 4 did and was failed. The judge is right on the Gemini side and wrong on the Opus side.

Opus Run 2 states the inversion out loud in its own final response: *"there's a second, older 4C row in Airtable already marked 'Ready' (rec...3954, move-out 6/1) - a stray duplicate of this turn. I left it untouched and closed the live 'In Progress' record you were tracking."* The agent inspected both rows, called the live Ready row a stray duplicate, and wrote to the stale one. That is the dual-row lever firing exactly as designed, and it was scored as a pass.

**Disposition:** no action toward the platform (a pass is not appealable). Recorded because the two Airtable criteria really pass 9/12 and 9/12, not 11/12 and 11/12, and because it means the dual-row disambiguation lever fired on 3 of 12 runs rather than the 1 of 12 the raw matrix shows. That correction is carried into the hardness calibration.
