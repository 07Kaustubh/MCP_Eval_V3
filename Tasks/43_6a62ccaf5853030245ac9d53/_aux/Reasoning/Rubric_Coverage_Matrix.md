# Rubric Coverage Matrix — Tasks/43_6a62ccaf5853030245ac9d53

| | |
|---|---|
| Universe | **starpm** (V4 framework) |
| Persona | Carlos Mendez · Onsite Property Manager · `carlos.mendez@starpm.com` (p_009) |
| Business function | Property Operations (StarPM BF1) |
| Rubric set | **25 rubrics · 25 outcome / 0 process** · flat four-field schema |
| Validator | `validate.py --phase rubrics` = **PASS** (0 fails) |
| Council A | **GO** (iteration 4) |
| Council B | **GO** (iteration 4) — 0 Major / 0 Moderate / 0 Minor; all 5 sub-dims 5 |
| **AUDIT verdict** | **PASS (STRICT)** — `_aux/Council_Reports/AUDIT_rubrics.md`, after 3 REVISE rounds |
| Regression anchors | **62/62 PASS** |
| Similarity | max composite **27.4** (< 40 ceiling) |

Rubric ids are 1-based (`R1` = `7_Rubrics.json[0]`).

## Rubric index

| Id | Sub-type | Criterion (abbreviated) |
|---|---|---|
| R1 | 2.1 | reports corrected owner pass-through **$1,812** |
| R2 | 2.1 | reports the **$1,622** charged does not line up with what was paid out (**verdict**) |
| R3 | 2.1 | repaint **$1,340** vs **$1,140** charged = **$200** understated |
| R4 | 2.1 | closet trim **$85** vs **$95** charged = **$10** overstated |
| R5 | 2.1 | deep clean **$387** is the one line that matches Sunshine Cleaning |
| R6 | 2.1 | reports net understatement **$190** |
| R7 | 2.1 | **$85** Alamo condition walk (bill 2026-481-566) stays off the owner side |
| R8 | 2.1 | **$85** Permian closet trim stays on the owner side |
| R9 | 1.1 | updates existing owner invoice **2026-534** |
| R10 | 1.2 | corrects 2026-534 **so that it totals $1,812** (end-state phrased) |
| R11 | 1.2 | raises repaint line **$1,140 → $1,340** |
| R12 | 1.2 | lowers trim line **$95 → $85** |
| R13 | 1.2 | keeps deep clean line at **$387** |
| R14 | 1.1 (guard) | does **not** create a second owner invoice, amending 2026-534 instead |
| R15 | 1.1 | updates the make-ready record carrying the **Ready** turn status |
| R16 | 1.2 | states in that record the final owner pass-through is **$1,812** |
| R17 | 1.2 | states in that record the 4C turn is closed on the owner side |
| R18 | 1.1 | drafts email to **linda.castillo@gmail.com** |
| R19 | 1.2 | states in the draft that the invoice was corrected to **$1,812** |
| R20 | 1.2 | states in the draft repaint **$1,340** vs **$1,140** originally billed |
| R21 | 1.2 | states in the draft the corrected figure is **$190** more than originally billed |
| R22 | 1.2 | states in the draft that 4C is now closed on her side |
| R23 | 1.1 | posts about the corrected cost in **a StarPM team channel** (channel-agnostic) |
| R24 | 1.2 | states in the channel message the pass-through is corrected to **$1,812** |
| R25 | 1.2 | states in the channel message it supersedes the **$1,622** originally billed |

Distribution: **8 × 2.1** · **5 × 1.1** · **12 × 1.2**.

## Forward coverage — prompt sentence → OE step(s) → rubric(s)

Sentence ids are `P<paragraph>.<sentence>`.

| Prompt sentence | Ask type | OE step(s) | Rubric(s) | Covered |
|---|---|---|---|---|
| P1.1 "…Mesa Vista 4C is one I want fully closed on the owner side." | Goal / framing | OE 25, 26 | R17, R22 | yes |
| P1.2 "Linda Castillo owns that unit." | Given fact (not an ask) | OE 1, 9 | bound in R9, R18 | n/a — given |
| P1.3 "…I billed her for the work and sent her a summary calling it done, the post-move-out deep clean, the full interior repaint, and the closet trim touch-up." | Belief anchor; names the 3 scopes | OE 7, 11 | R3, R4, R5 | yes |
| P1.4 "I moved on to the next unit and left it there." | Framing | — | — | n/a — framing |
| P1.5 "Before I log 4C as truly closed I want to be sure what she was actually charged holds up…" | **Verdict / determination** | OE 11, 21 | **R2** | yes |
| P2.1 "…every dollar on her bill has to line up with what we actually paid out on that unit, to the dollar, no more and no less." | **Derived figure** | OE 14, 15, 17, 21 | **R1**, R10 | yes |
| P2.2 "Go back to what each vendor charged us for the 4C work and set it against the line items I sent her." | **Per-line comparison (3 lines)** | OE 11, 14, 15, 17 | **R3, R4, R5** + R11, R12, R13 | yes |
| P2.3 "Only outside vendor work belongs on her side." | **Inclusion rule** | OE 17, 19, 20 | **R8** | yes |
| P2.4 "Anything that was our own time on the unit, an internal walk or a condition check we handled in house, stays off her bill entirely." | **Exclusion rule** | OE 18, 19 | **R7** + R10 entailment clause | yes |
| P3.1 "If her charges come out clean against what we paid, log 4C closed…" | Conditional — branch NOT taken | OE 21 | R2 establishes the branch; R17/R22 carry the closure | yes |
| P3.2 "…I do not want a second bill created next to the one she already has." | **Negative constraint** | OE 24 | **R14** | yes |
| P3.3 "Correct the invoice she is holding so it carries the right figure," | **Write 1 — invoice** | OE 10, 12, 24 | **R9** (1.1) + R10, R11, R12, R13 (1.2) | yes |
| P3.4 "…get our 4C make-ready record in Airtable updated so it shows the final owner cost and the unit fully closed." | **Write 2 — Airtable; compound (cost AND closure)** | OE 3, 5, 25 | **R15** (1.1) + **R16** (cost) + **R17** (closure) | yes — both halves |
| P3.5 "Then email Linda a short note letting her know where it landed, so she is not sitting on a summary that no longer matches." | **Write 3 — owner email** | OE 1, 26 | **R18** (1.1) + R19, R20, R21, R22 (1.2) | yes |
| P3.6 "And drop a line in our channel for the crew and front office, so whoever else touches her account is working off the corrected number rather than the one I originally sent." | **Write 4 — channel; compound (number AND supersession)** | OE 22, 23, 27 | **R23** (1.1) + **R24** (number) + **R25** (supersession) | yes — both halves |
| P4.1 "I would sooner square this myself now than have Linda find the gap in her own paperwork…" | **Quantify the gap** | OE 21 | **R6** | yes |

**No gaps.** Every explicit ask, both compound halves (P3.4, P3.6), the verdict ask (P1.5), and both scoping constraints (P2.3, P2.4) carry a covering Outcome rubric.

## Final-Response Coverage gate (Eval Phase 3.1, Gap 3)

| User-facing ask | Type | 2.1 rubric | Covered |
|---|---|---|---|
| whether what she was charged holds up | verdict | R2 | yes |
| what the pass-through should be, to the dollar | derived figure | R1 | yes |
| each vendor charge set against each invoice line | 3-way comparison | R3, R4, R5 | yes |
| the size of the gap | derived delta | R6 | yes |
| what stays off her bill as in-house time | exclusion | R7 | yes |
| what stays on her bill as outside vendor work | inclusion | R8 | yes |

## OE-to-Rubric cross-reference (Eval Phase 3.1, Gap 4)

| OE | Type | Action | 1.1 | 1.2 |
|---|---|---|---|---|
| OE 24 | Write | correct invoice 2026-534 in place | R9 | R10, R11, R12, R13 (+ guard R14) |
| OE 25 | Write | update the live 4C make-ready row | R15 | R16, R17 |
| OE 26 | Write | draft the owner note | R18 | R19, R20, R21, R22 |
| OE 27 | Write | post the corrected figure to a team channel | R23 | R24, R25 |

Key-discovery OEs surfacing a user-asked fact: OE 11 → R2/R3/R4; OE 14 → R5; OE 15 → R3; OE 17 → R4/R8; OE 18 → R7; OE 21 → R1/R6; OE 28 (load-bearing fact list) → R1-R8 collectively.

Intermediate-lookup OEs needing no rubric (per the eval's explicit carve-out): OE 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 16, 19, 20, 22, 23.

**No orphan write-action OEs. No rubric without an OE.**

## Reverse coverage — no surplus

| Rubric | Traces back to |
|---|---|
| R1 | P2.1 |
| R2 | P1.5 |
| R3, R4, R5 | P2.2 (one per invoice line) |
| R6 | P4.1 + P2.1 |
| R7 | P2.4 |
| R8 | P2.3 |
| R9 | P3.3 |
| R10 | P2.1 + P3.3 |
| R11, R12, R13 | P2.2 + P3.3 (one per invoice line) |
| R14 | P3.2 |
| R15, R16, R17 | P3.4 |
| R18, R19, R20, R21, R22 | P3.5 |
| R23, R24, R25 | P3.6 |

Zero rubrics go beyond the prompt (Council B B2b: all mapped to a named prompt sentence).

## Exclusion / decoy coverage gate

| Decoy | Wrong total it yields | Guarding rubric(s) |
|---|---|---|
| $85 Alamo condition walk, bill 2026-481-566 (over-inclusion) | $1,897 | R7 (report) + R10 (a fourth line cannot total $1,812) |
| dropping the $85 Permian closet trim as internal labor (under-inclusion) | $1,727 | R8 (report) + R12 (invoice line) |
| $385 Rio Bend deep-clean pass-through on invoice 2547, same owner | $1,810 | R5 (report) + R13 (invoice line) |
| trusting the existing invoice lines | $1,622 | R2 (verdict) + R1 + R10 |
| ten distinct $1,340 bills; only PD-2026-09 is the 4C repaint | wrong record, right number | R11 binds the figure to the repaint line on 2026-534 |
| Pete Donovan as owner (bill notes point at him) | wrong recipient | R9 (customer Linda Castillo) + R18 (recipient linda.castillo@gmail.com) |
| stale In Progress row recbd087a4abd605b ("still tracking") | wrong record updated | R15 pins the **Ready**-status row (Selection-Logic, not record id) |
| invoice 2026-537 quoted in the summary email (does not exist) | no write at all | R9 binds to 2026-534 |
| credit memo instead of an amendment (117 credit_memo records exist) | receivable reduced, not raised | R14 |

The over-inclusion guard is an **entailment** rather than a separate rubric: `TotalAmt == sum(Line.Amount)` holds across **385/385** QuickBooks records with zero counterexamples, so a four-line invoice declaring $1,812 is unrepresentable and R10 fails it on the criterion's own face.

## Hardness lever preservation (Council B-B4, AUDIT LENS 3)

| Lever | Rubric that cannot be satisfied without traversing it |
|---|---|
| **L2 structured-DB skip (flagship)** | R1, R3, R10, R11 — $1,340 and the $1,812 total exist only on the AP bills, on no readable surface |
| **L10 reversal / supersession** | R2, R25 — the stale $1,622 must be identified as superseded |
| **L6 near-miss entity** | R5, R11, R13 — $385/$387 and the ten-bill $1,340 cluster must be disambiguated by unit, not amount |
| **L11 net-vs-gross** | R6, R7, R8 — the two $85 charges must be split correctly to reach $190 |
| **L1 latching** (was reserve, now **live**) | R15, R16, R17 — the Ready-status row must be picked over the "still tracking" snapshot |

## Density (Council B-B3 / AUDIT LENS 4, adjudicated)

StarPM per-model bands (≥ 40 PASS · 15-39 THIN · < 15 INSUFFICIENT):

| Model | Midpoint | Range | Band |
|---|---|---|---|
| Opus 4.8 | **~42** | 32-48 | **PASS** (knife-edge) |
| Gemini | **~32** | — | **THIN** (accepted under the plan's documented `## THIN density acceptance`) |

AUDIT initially projected Opus ~37 and **conceded** on repo evidence: Task 39 logged Opus 43.5 at 0/6, Task 41 logged Opus 48.0 at 0/6 on the identical L2 vendor-linked-AP-bill flagship, and the minimum across all recorded 0%-pass run sets is 41.5 — a stumped agent keeps searching rather than skipping the AP leg. All four writes are hard-forced by the rubric set.

**S4 re-open triggers (per model):** Gemini **< 24**, Opus **< 32**. Remedy is a grounded fifth write or an added OE cross-service read — **not** rubric padding.

Two corrections to carry to FINAL: delivered service breadth is **5, not 6** (nothing forces Linear or HubSpot), and `_aux/Hardness_Plan.md` still labels L1 "reserve" though it is now live and graded.
