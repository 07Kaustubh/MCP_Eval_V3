# Council B — S3 Rubrics (Adversarial QC + Density + Hardness Preservation)

Task: `24_6a36e84723508b4e3f391cfc` (AP / Vendor Operations — Lena Park, Procurement Officer; REDO rebuild)
Deliverable: `7_Rubrics.json` — **25 rubrics, all `outcome`** (Round 2, post-split + de-bundle + polish)
Universe today: 2026-06-12 (US/Eastern)
Method: five role lenses (Architect, Implementer, Red-team, Ground-truth, Integration). Every load-bearing atom independently re-derived from `_aux/Universe_Split/` via Python. Validator (`rubrics.md`) re-confirmed on the updated file: PASS, 0 fails / 0 warns, outcome=25 / process=0.

**VERDICT: GO (re-affirmed on the updated set).** The two Major atomicity violations the grounding/convention council raised are resolved by the split and the de-bundle; both new rubrics are cleanly atomic and grounded. Every applicable QC sub-dimension still scores 5. No new adversarial divergence — the index-12/13 split did not create an over-specific rubric that a valid compound-ranking trajectory fails. Density unchanged (~46-48, >= 40). All five hardness levers still tied to outcome rubrics (L1 is now reinforced by two explicit anti-latch rubrics). No new phrasing hits. Both S2 upstream guards still honored.

> **Count note (accuracy correction):** the on-disk set is **25 rubrics**, not 26. The single compound-ranking split (1 rubric -> 2) takes the set from 24 to 25; the TimeLedger de-bundle (index 16) and the three polish edits (index 0, index 16, index 20) are all in-place and do not change the count. 25 is the correct, complete post-split count — coverage is intact, no rubric is missing.

---

## What changed since Round 1 (verified on disk)

| Change | Round 1 | Round 2 (on disk) | Verified |
|---|---|---|---|
| Compound-ranking split | one combined rubric (old idx 12): "VaultKey not leader + BeaconPay outranks" | idx 12 (VaultKey top-dollar but not most-severe) + idx 13 (BeaconPay high-age mid-dollar surfaces) | both atomic, both grounded |
| TimeLedger de-bundle | idx (old) bundled "missing credit memo" + "distinct from VEN-010-693199" in title | idx 16 title asserts only the missing-credit-memo / AP classification; VEN-010-693199 disambiguation moved to justification + evidence | atomic; within prompt scope (prompt never names VEN-010-693199) |
| Polish — idx 0 | "(channel_id C010)" | "(channel_id C010 or channel name vendor-bills-and-ap)" | both forms offered; no channel-form lock-in |
| Polish — idx 16 | "(or similar)" abutted VEN-010-693199 | resolved by de-bundle (id no longer in title) | clean |
| Polish — idx 20 | "(or similar)" abutted doc_0036f5b991574808 | hedge expanded to "(or similar statement that Northstar's scope sits in a single executed engagement letter)" | referent now explicit (the statement, not the id) |

---

## Rubric inventory (0-based index = array order)

| # | Sub | Claim (truncated) | Surface |
|---|---|---|---|
| 0 | 1.1 | Posts standalone summary to #vendor-bills-and-ap (channel_id C010 or name vendor-bills-and-ap), not a thread reply | Slack write |
| 1 | 1.2 | Slack: GraniteRack = stale/superseded SOW, procurement's | Slack content |
| 2 | 1.2 | Slack: TimeLedger VEN-010-514242 = missing credit memo, AP's | Slack content |
| 3 | 1.2 | Slack: high-compound acme items = orphan approval chains, no AP owner | Slack content |
| 4 | 1.1 | Adds comment to Linear issue_378874ffeb8f4cb0b0417021f2d3d647 | Linear write |
| 5 | 1.2 | Linear: 320/320 pending carry null approver (or similar systemic evidence) | Linear content |
| 6 | 1.2 | Linear: post-patch invoices (VEN-028-492596 5/18; MetroShield 5/31) still orphaned | Linear content |
| 7 | 1.1 | Email lena.park -> daniel.jones, CC steven.perry | Email write |
| 8 | 1.2 | Email: GraniteRack VEN-012-753165 void-and-rebill needs partner sign-off | Email content |
| 9 | 1.2 | Email: TimeLedger VEN-010-514242 needs partner sign-off | Email content |
| 10 | 1.1 | Reminder due 2026-06-19 to re-check pending AP backlog | Reminder write |
| 11 | 2.1 | Ranks worst offenders by compound exposure (age x $), not top-dollar | Final response |
| **12** | 2.1 | **VaultKey VEN-029-961721 $460,556.46 = single largest-dollar item but NOT most severe by compound** (split A) | Final response |
| **13** | 2.1 | **Surfaces a high-age mid-dollar item such as BeaconPay VEN-033-26339 $108,826.27 ~320d that top-dollar underweights** (split B) | Final response |
| 14 | 2.1 | CivicSquare VEN-024-891664 $289,217.86 ~302d acme = leading compound offender | Final response |
| 15 | 2.1 | GraniteRack VEN-012-753165 = stale/superseded SOW (SOW-2024-GR-rev3 vs SOW-2025-GR-rev1), procurement | Final response |
| **16** | 2.1 | **TimeLedger VEN-010-514242 $24,475.25 = missing credit memo, AP's** (de-bundled; VEN-010-693199 disambiguation in justification/evidence) | Final response |
| 17 | 2.1 | Pinecrest VEN-006-193120 $1,040.63 ~338d brookfield = active vendor dispute; NOT pinned to a side | Final response |
| 18 | 2.1 | High-compound acme items (CivicSquare, BeaconPay, Clearpoint, PensionBridge, AssurePath) = orphan chains, AP's | Final response |
| 19 | 2.1 | Acme scope from addendum doc_eb7cb30c59bd4f03 + change order doc_2d85ac5a698745c5, not missing | Final response |
| 20 | 2.1 | Northstar scope from engagement letter doc_0036f5b991574808 | Final response |
| 21 | 2.1 | Scope docs restricted, unreadable without an access grant, not missing | Final response |
| 22 | 2.1 | Routing fix did NOT hold (post-patch still orphaned); live AP-side signal for Priya | Final response |
| 23 | 2.1 | Distinguishes 210000 external-vendor vs 219000 employee-reimb; scopes to external-vendor; 219000-surfacing agent still passes | Final response |
| 24 | 2.1 | Defers approval/routing to Daniel/Steven/Priya; no self-claim of approving/routing | Final response |

Writes (1.1): idx 0, 4, 7, 10 = the four mandated writes (unchanged). Content (1.2): 1/2/3, 5/6, 8/9. Findings (2.1): 11-24.

---

## Ground-truth re-verification of the changed rubrics (re-derived from `Universe_Split/`)

| Atom | Re-derived value | Match |
|---|---|---|
| idx 12 — VaultKey VEN-029-961721 = single largest-dollar pending item | $460,556.46; #1 by dollar in the >80d 210000 pending set | exact |
| idx 12 — VaultKey is NOT most severe by compound | compound 63.1M = #2, behind CivicSquare 87.3M (#1) | correct |
| idx 13 — BeaconPay VEN-033-26339 $108,826.27, ~320 days | exact; 320d; compound 34.8M = #10, but ranks above larger-dollar items (ArchiveHaven $122,800.90, Northloop $131,935.56) -> age-promoted, top-dollar-underweighted | exact + claim correct |
| idx 14 — CivicSquare leads compound | 87.3M = #1 compound | correct |
| idx 16 — TimeLedger VEN-010-514242 $24,475.25, acme, 210000, pending | exact | exact |
| idx 16 (judge guidance) — separate TimeLedger VEN-010-693199 = expired-W-9 hold | exact; same vendor_id VEN-010-B, distinct invoice ($21,777.01) | exact |

All other atoms were re-derived exact in Round 1 and are unchanged by these edits.

---

## [B1] QC sub-dimension scoring (bar is 5)

| Sub-dimension | Score | One-line reason |
|---|---|---|
| Overall Rubric Quality | **5** | 0 Major, 0 Moderate. The two Major atomicity violations are fixed. Only non-failing cosmetic notes remain (< 5%). |
| Rubric Category Balance | **5** | 25 outcome > 0 process; binary PASS. |
| Process Rubrics | **5** | Zero process rubrics; three-condition test vacuously satisfied. |
| Agent-Centric Phrasing | **5** | All 25 titles begin "The Agent ..."; no tool **function** name in any title (idx 0 `channel_id` is a parameter, now paired with the channel name). |
| All-Failing Rubrics | **5 (N/A at S3)** | No verifier runs yet. No false-negative-shaped rubric present. |
| **Atomicity** | **5** | The split makes idx 11/12/13/14 four single-claim rubrics (method / VaultKey-anti-latch / BeaconPay-surfacing / CivicSquare-leader). idx 16 is now a single classification claim. No rubric fails for two unrelated reasons. |
| Self-Containment | **5** | Every email, invoice id, doc id, amount, account, SOW ref, date embedded; channel given by both name and id. |
| **Completeness** | **5** | No gap, no surplus (map below). The two split rubrics and the de-bundled idx 16 each tie to a distinct prompt ask; none reaches beyond the prompt. |
| Flexibility | **5** | Exact for ids/emails/amounts/dates/accounts; "(or similar)" on freetext 2.1 findings; ages carry "approximately". |
| Accuracy | **5** | Every atom independently re-derived exact. |

### Completeness — the split + de-bundle each tie to a prompt ask (no surplus, no gap)

- **idx 11** -> "I want the lens to be age against outstanding dollars together rather than top-dollar alone" (the method).
- **idx 12** -> "rather than top-dollar alone" (the anti-latch on the single biggest-dollar item, VaultKey). Grounded: VaultKey is the dollar leader and not the compound leader.
- **idx 13** -> "because a long-aged mid-dollar invoice can drift past us" (the explicit prompt concern that an aged mid-dollar item must not be buried by the dollar lens). Grounded: BeaconPay is the canonical 320-day mid-dollar item; the OE and Hardness_Plan (Stump Prediction 4) name it as the documented prior miss.
- **idx 16** -> "a missing credit memo ... [is] AP's" (the AP-owned root-cause category). The de-bundled VEN-010-693199 clause is now judge guidance, not a standalone claim — correct, since the prompt never names VEN-010-693199, so it cannot be an independent gradable requirement.

No prompt ask lost coverage in the split. No new rubric exceeds the prompt.

---

## [B2] Adversarial alt-path — does the idx-12/13 split over-specify? (the focus of this re-review)

**idx 12 (VaultKey).** Claim: VaultKey is the single largest-dollar item but not the most severe by compound. A valid compound-ranking trajectory ranks CivicSquare #1 and necessarily places VaultKey below it, so it recognizes VaultKey is not the most severe -> passes. The only trajectory that fails is one that headlines VaultKey as the worst offender, i.e. the dollar-latch the prompt explicitly warns against. **No valid path fails idx 12.**

**idx 13 (BeaconPay) — examined hardest.** Claim: the agent surfaces a high-age mid-dollar item (such as BeaconPay) that a top-dollar ranking underweights. Re-derived facts: BeaconPay ($108,826.27, 320 days) is compound #10 — outside a strict top-5 — but it is age-promoted well above its dollar rank and sits above larger-dollar items (ArchiveHaven $122,800.90, Northloop $131,935.56) on compound. The potential concern: would an agent that lists only the strict top-5 compound (all high-dollar: CivicSquare/VaultKey/Clearpoint/PensionBridge/AssurePath) and never mentions a mid-dollar aged item fail idx 13?

Resolution — this is the **intended L1 discriminator, not an over-specification defect**, for three independent reasons:
1. **The prompt makes it an explicit ask.** "because a long-aged mid-dollar invoice can drift past us" is a direct instruction to make sure aged mid-dollar items are not buried — not merely a rationale for the lens. An agent that ignores every aged mid-dollar item has missed that explicit concern; failing it is correct.
2. **No lock-in to BeaconPay.** "such as BeaconPay ... (or similar)" plus the evidence ("a high-age mid-dollar item such as BeaconPay ... despite not being a top-dollar item") lets any genuine high-age mid-dollar item (BeaconPay, Pine & Meridian $121,886.62/326d, ArchiveHaven $122,800.90/282d, Northloop $131,935.56/227d) satisfy it. A valid agent is not forced onto one literal.
3. **Grounded end-to-end.** OE5 lists BeaconPay among the items the compound lens surfaces and names it the top-dollar-underweighted exemplar; Hardness_Plan Stump Prediction 4 names BeaconPay as the prior-miss item. The rubric is the faithful encoding of that discriminator.

Residual phrasing nuance (non-blocking): "among the worst offenders" is slightly generous given BeaconPay's strict compound rank (#10); the evidence's "despite not being a top-dollar item" framing and the "(or similar)" hedge keep a fair judge from reading it as "BeaconPay must be in the literal top-5." Logged as cosmetic note 1.

**Reverse-coverage.** All 25 rubrics still trace to an explicit or directly-implied prompt ask; none exceeds the prompt. The de-bundle removed the only title clause (VEN-010-693199) that was arguably beyond the prompt and reframed it as judge guidance — a coverage improvement.

**Conclusion:** the split introduced no over-specific rubric that fails a valid compound-ranking trajectory; no rubric beyond prompt; no prompt ask uncovered.

---

## [B3] Tool-call density projection

The split and de-bundle are wording/structure-only: no discovery step, cross-service chain, or write was added or removed. The implied competent-Opus-4.8 trajectory is unchanged — contact + channel resolution, paginated 320-row AP pull, per-invoice gets on worst offenders + GraniteRack siblings, Linear list+gets (~6 issues), email multi-query, Slack history + the Daniel thread reply, 2-entity x 3-kind RV sweep + access grants, four writes. Low ~40, high ~60, **mid ~46-48** — on the Hardness_Plan midpoint (47) and matching S2 (~46-48). **Density gate: PASS (>= 40). No INSUFFICIENT_DENSITY.**

---

## [B4] Hardness preservation (each lever -> >= 1 outcome rubric)

| Lever | Outcome rubric(s) | Status |
|---|---|---|
| L1 Latching (dollar-bias anchor + Daniel-Jones dismissal) | **reinforced** — now idx 11 (method) + idx 12 (VaultKey anti-latch) + idx 13 (BeaconPay surfacing) + idx 14 (CivicSquare leader); idx 22 (+6) for the dismissal-vs-post-patch reconciliation | TRIGGERED (stronger) |
| L2 Structured-DB scope skip | idx 19 (Acme addendum + change order), idx 20 (Northstar letter), idx 21 (restricted) | TRIGGERED |
| L7 Multi-write diversification | idx 0 (Slack), idx 4 (Linear), idx 7 (email), idx 10 (reminder) | TRIGGERED |
| L8 Multi-link chain (SAP -> Linear -> email per vendor) | idx 15 (GraniteRack), idx 16 (TimeLedger), idx 17 (Pinecrest), idx 18 (orphan cluster) | TRIGGERED |
| L9 Universe-grounded gotcha | idx 21 (restricted), idx 5 (320/320 null), idx 23 (210000 vs 219000) | TRIGGERED |

All five levers tied to >= 1 outcome rubric. The split **strengthens** L1 (two explicit anti-latch rubrics instead of one bundled). **No HARDNESS_REGRESSION.**

---

## [B5] Tool-leak / phrasing scan (re-run on the 25-rubric set) + atomicity + process

- **Tool function names in titles:** 0. idx 0 `channel_id` is a parameter and is now explicitly paired with the channel name; validator's tool regex does not match it.
- **Em / en / figure dash / minus:** 0 in any field.
- **"at least N":** 0.
- **"approximately" before id / date / account / exact single-record $:** 0. idx 13 / idx 14 / idx 17 "approximately" precede a day-age (calculated value); the single-record dollar amounts are stated exactly.
- **"(or similar)" adjacent to an exact email/id/amount/date:** Round 1's two hits are reduced to one residual, and it is now defused — idx 16's id (VEN-010-693199) was removed from the title by the de-bundle; idx 20's hedge was expanded to "(or similar statement that Northstar's scope sits in a single executed engagement letter)", so the parenthetical now self-describes that it modifies the *statement*, not the doc id. Validator does not flag it (its check only fires near an `@email`). Cosmetic note 2.

**Adversarial atomicity pass.** idx 11/12/13/14 are now four single-claim rubrics (the prior bundling is gone). idx 16 is a single classification claim. idx 15 (SOW classification + procurement ownership) remains acceptable same-finding bundling (the prompt deterministically couples SOW -> procurement). No split required.

**Adversarial process pass.** Zero process rubrics. None of the 25 outcome rubrics is a disguised execution trace; idx 11/12/13 are final-response findings (compound-ranking outputs), not tool-call sequences. Clean.

**B5: CLEAN on all substantive checks; 2 cosmetic non-failing notes.**

---

## Upstream-guard re-check

**Guard 1 — "active vendor dispute" unassigned; no rubric hard-pins Pinecrest to a side.** HONORED (unchanged). idx 17 reads "(or similar)" with "The prompt does not assign an owning side ... so this rubric does not require one"; evidence: "Do not require it to be pinned to procurement or AP."

**Guard 2 — backlog count robust; no hard external-vendor count; 219000-surfacing / broader-count agent must not fail.** HONORED (unchanged). idx 23 scopes by account family and states "An agent that surfaces 219000 miscoding should still pass." idx 5's "320" is the null-approver total (320/320, robust) with an "(or similar)" hedge, not the backlog count. The split/de-bundle touched neither rubric.

---

## Numbered issue list

No Major, Moderate, or failing-Minor issues. Two cosmetic, non-failing notes (neither blocks; neither affects judge evaluation, hardness, density, or the guards):

1. **[B2 / cosmetic] idx 13 — "among the worst offenders" is slightly generous.** BeaconPay is compound #10, outside a strict top-5, though age-promoted above larger-dollar items and grounded in the prompt's explicit mid-dollar concern. The "such as ... (or similar)" hedge and the evidence's "despite not being a top-dollar item" framing keep a fair judge from requiring a literal top-5 placement. *Optional:* soften to "among the items it flags" if zero ambiguity is desired.
2. **[B5 / cosmetic] idx 20 — "(or similar ...)" still textually follows the exact doc id.** The hedge now reads "(or similar statement that Northstar's scope sits in a single executed engagement letter)", so its referent (the statement, not the id) is explicit and the id cannot read as fuzzy; validator does not flag it. *Optional:* move the parenthetical ahead of the id for full convention compliance.

Plus one **accounting note** (not a rubric defect): the on-disk count is **25**, not 26 — the split adds exactly one rubric (24 -> 25); the de-bundle and polish edits are in-place. Coverage is complete at 25.

---

## FINAL VERDICT: GO (re-affirmed)

The two Major atomicity violations are resolved: the compound-ranking rubric is cleanly split into idx 12 (VaultKey anti-latch) and idx 13 (BeaconPay surfacing), and idx 16 (TimeLedger) is de-bundled with the VEN-010-693199 disambiguation correctly demoted to judge guidance (the prompt never names that invoice). Every applicable QC rubric sub-dimension scores 5 (Overall Quality, Category Balance, Process, Agent-Centric Phrasing, Atomicity, Self-Containment, Completeness, Flexibility, Accuracy). The split introduced no over-specific rubric that a valid compound-ranking trajectory would fail — idx 13 encodes the prompt's explicit "long-aged mid-dollar invoice can drift past us" concern with non-locking "(or similar)" flexibility. Density is unchanged at ~46-48 (>= 40). All five hardness levers remain tied to outcome rubrics, with L1 reinforced. No new phrasing hits (Round 1's two cosmetic hits are now reduced to one defused residual). Both S2 upstream guards remain honored. Clear to proceed to FINAL.
