# ⛔ SUPERSEDING FINDING (2026-07-27, skeptical Oracle verify `ses_05b6e0cf9ffejpRfT6lm4MbmtF`) — INJECTION PATH DEAD; ESCALATE

**This overturns the "authorize INJ-1 injection" recommendation below.** A schema check of the split (verified this session) invalidated the mechanism the whole plan rested on:

- `credit_memo` is **117/117 CustomerRef** (AR/customer-side); there is **no vendor-credit entity type** in this universe. INJ-1 ("unapplied vendor credit nets repaint `PD-2026-09` to $1,000") is **schema-invalid** — a credit_memo cannot reduce an AP vendor bill.
- The only AP-side substitute (a partial bill-payment vs `PD-2026-09`) contradicts the **frozen base `Balance=1340`** (paid bills store net Balance; base rows cannot be UPDATE'd) → Eval0 P4. Also invalid.
- Vendor-credit gone + recency/latching already retired as 4.8-robust (L36) ⇒ **the plan has ZERO Opus-selective mechanism left.**

**Native alone does NOT clear T2.** The graded $1,727 (deep clean 387 + repaint 1340) is a determinate sum of readable `Balance` fields → Opus-easy. Honest Opus pass@1 ≈ **55-70%** (floor ~48% only by shipping the **F8** ambiguous condition-bill exclusion, which the submission gate rejects). Above the 40% ceiling either way.

**Coherence kill (independent 2nd reason):** a **QC inspector** (Jaime Salinas, p_007, BF3) producing an exact *net vendor-liability figure with prior-turn/intake exclusions* is AP/controller work, not QC — Contrived/Unnatural-Prompt exposure. The coherent QC ask ("the two open scopes' vendor invoices are unpaid, so the turn can't close") is single-hop and Opus-trivial.

## ⚠️ OPERATOR DECISION (STOP — injection NOT authored; do NOT proceed to S1 on this anchor)
The retained persona (QC Inspector, BF3) × Mesa Vista 4C anchor **cannot yield a fair Opus-4.8-≤40% task.** Per Oracle, do NOT persona-swap *within* BF3 (all QC/field personas share the single-hop physical-truth problem). Choose:
1. **[recommended] Business-function pivot to Finance or Portfolio-Coordination / Owner-Relations.** There the customer-side `credit_memo` (117 available) is schema-valid against owner AR invoice `2026-534`, and the native **$200 AP-vs-AR repaint gap** ($1,340 vendor bill vs $1,140 owner line) becomes the persona's job. CAVEAT: clearing ≤40% still needs a **semantic hidden operand** (unstated apportionment / pass-through-markup / credit-application rule where no single field states the answer — NOT search-eviction, which is 4.8-robust); must be freshly grounded before committing. Changes the fixed BF anchor `REDO_reason.md` retained — operator call.
2. **Task-swap** — this universe's QC/field surface has no fair Opus-≤40% mechanism.
3. **Accept sub-T2** (~55-70% Opus) — not advisable; re-ships a difficulty fail.

**The instruction "author INJ-1 + clear validate.py --phase injection" was NOT executed:** INJ-1 is schema-invalid; authoring a hollow row to green the deterministic validator would fail the P8 difficulty council + coherence and would be gaming the gate. Awaiting the decision above.

---

# ✅ ATOMS FULLY GROUNDED (2026-07-27, parsed from `_aux/Universe_Split/`) — AUTHORITATIVE FINAL NUMBERS

These verified numbers supersede any conflicting figure below (the "Verified atoms" table and the original "Record census correction"). All parsed from the `row_data` of the split JSON this session (`entity_type` confirmed).

## Verified QB entities
| Doc | entity_type | vendor / customer | amount | balance | scope | turn |
|---|---|---|---|---|---|---|
| PD-2026-09 | **bill (AP)** | Permian Make-Ready | 1,340 | **1,340 unpaid** | interior repaint | CURRENT (recbd087) |
| 2026-SC-4C | **bill (AP)** | Sunshine Cleaning | 387 | **387 unpaid** | deep clean | CURRENT |
| 2026-481-566 | **bill (AP)** | Alamo HVAC | 85 | 85 unpaid | condition / punch intake | CURRENT (not an open scope) |
| 2026-519 | **bill (AP)** | Permian Make-Ready | 85 | 85 unpaid | closet-trim touch-up | **PRIOR (recc8534 QC) — EXCLUDE** |
| 2026-534 | **invoice (AR)** | owner Linda Castillo | 1,622 | 1,622 | deep clean 387 + repaint **1,140** + trim 95 (pass-through) | W-AR decoy |

## Corrections to the plan below
1. **INJ-2 DROPPED.** A current-turn deep-clean AP bill ALREADY EXISTS: `2026-SC-4C` (Sunshine, $387 unpaid), buried among **9 Sunshine bills** (native L6 near-miss / L4 eviction — the agent must pick the 4C one). No second injection needed. The earlier "Record census correction" claiming the $387 is "only an AR line" is itself WRONG — it is BOTH a standalone AP bill (2026-SC-4C) AND an AR line (2026-534). L36's "$387 + $1,340 unpaid AP bills" was essentially right.
2. **Native net-vs-gross discovered (bonus symmetric pressure).** The vendor AP repaint bill ($1,340) vs the owner AR pass-through repaint line ($1,140) DISAGREE by **$200** (trim AP $85 vs AR $95 by $10). No single field reconciles them — a native L11 that backs the injected credit and lowers reliance on INJ-1.
3. **Computed target = current-turn OPEN-scope vendor liability (deep clean + interior repaint):**
   - GROSS (no credit) = 387 + 1,340 = **$1,727**.
   - NET of INJ-1 credit ($340 off repaint) = 387 + 1,000 = **$1,387** ← the graded figure; stated by NO single field.
   - Intermediate WRONG answers: `1,727` (gross, credit missed) · `1,622` (grabbed the owner AR invoice — whose note even says "all work confirmed complete") · `1,812` (added the $85 condition intake) · `1,897` (added prior-turn trim too) · `1,000` (repaint-only, missed deep clean) · `1,140` (used the owner's repaint figure). Whether the $85 condition bill is inside "cost to close" is an S3 atomicity call — pin ONE accept-set.
4. **7/15 event confirmed.** The ONLY future 4C calendar event is `Make-Ready QC Inspection - Mesa Vista 4C` **2026-07-15T10:00 CDT**, status confirmed, desc "Final make-ready QC inspection ... after interior repaint and deep clean." The deep-clean and repaint events are PAST (both 5/21). → H4 / F9 stands: a hold / only-X-outstanding deliverable MUST reconcile the confirmed 7/15 re-inspection.
5. **recbd087 note confirmed verbatim** (justifies injection): *"...Deep clean and interior repaint still tracking on their respective schedules. Will update status to Ready once all vendor and in-house scopes are signed off."* → one field states the ready/not-ready answer (binary is single-hop); the DOLLAR reconciliation (net-of-credit) is the part that survives careful reading.

## Injection scope (FINAL)
**INJ-1 ONLY:** one QB `credit_memo` (unapplied, ~$340, vendor Permian, ties to `PD-2026-09`, DocNumber `CM-2026-04xx`, PrivateNote = short-pay / re-do dispute; vendor-scoped, NOT keyword-"4C"). Base rows untouched. Clears `validate.py --phase injection` (7 gates + difficulty ≥ 3.5). **INJ-2 removed** (deep-clean AP bill exists natively).

---

# ✅ ATOMS GROUNDED (2026-07-27, post-oracle) — corrections supersede the plan below

Every atom here is PARSED from `_aux/Universe_Split/` (row_data JSON), not token-only. Where these differ from the REDO plan or oracle's trace, **THESE WIN.**

## Corrected QB census (verified by entity_type)
| DocNumber | entity_type | vendor / customer | scope | Amount | Balance | Turn |
|---|---|---|---|---|---|---|
| `2026-SC-4C` | **bill (AP)** | Sunshine Cleaning | post-move-out deep clean 4C | 387 | **387 unpaid** | **current** |
| `PD-2026-09` | **bill (AP)** | Permian Make-Ready | interior repaint 4C | 1,340 | **1,340 unpaid** | **current** |
| `2026-481-566` | **bill (AP)** | Alamo HVAC | condition / punch-list doc (Carlos walk) | 85 | **85 unpaid** | current (intake) |
| `2026-519` | **bill (AP)** | Permian Make-Ready | closet-trim touch-up (QC correction) | 85 | **85 unpaid** | **PRIOR** (recc8534) |
| `2026-534` | **invoice (AR)** | Linda Castillo (owner) | pass-through: deep clean 387 + repaint **1,140** + trim 95 | 1,622 | 1,622 | receivable |

**INJ-2 DROPPED** — a current-turn deep-clean AP bill already exists (`2026-SC-4C`, $387 unpaid). Injection stays at **1 row (INJ-1 only)**. **INJ-1 schema-safe** — `credit_memo` is a valid QB entity_type (117 present).

**Two NATIVE levers oracle did not have (they REINFORCE the symmetric stump, but do NOT replace INJ-1 — native figures are all readable, so Opus sums them):**
- **AP-vs-AR repaint gap:** vendor AP repaint bill **$1,340** vs owner AR pass-through line **$1,140** = a **$200** discrepancy stated by no single field (native L11).
- **9-way Sunshine near-miss:** the 4C deep-clean bill `2026-SC-4C` is one of **9 Sunshine Cleaning bills** — selecting it is a native L6/L4 hop.

## Corrected computed target (open-scope vendor liability — the graded figure)
Open scopes per `recbd087.fldNotes2` = **deep clean + interior repaint** (the 3 in-house punch items are done).
- **GROSS** current-turn open-scope AP = deep clean 387 + repaint 1,340 = **$1,727**.
- **NET of the INJ-1 unapplied $340 credit on the repaint** = 387 + (1,340 − 340) = **$1,387** — stated by NO single field. ← the discriminating figure.
- **Intermediate WRONG answers (L18 catalog):** `1,727` (gross; credit missed) · `1,622` (grabbed owner AR invoice) · `1,812` (+ condition $85) · `1,897` (+ prior-turn trim $85) · `1,527` (used AR repaint 1,140, not AP 1,340) · `1,000` (repaint-net only, dropped deep clean). Correct $1,387 appears in NO artifact (L6-safe).
- S3 pins whether the $85 condition bill is in/out of the open-scope set — it is intake, not an open scope, so **EXCLUDED by default**; the prompt must not let this become an ambiguous target (F8).

## `recbd087.fldNotes2` (verbatim — the single-field answer that mandates injection)
"...All three items marked done in this record... **Deep clean and interior repaint still tracking on their respective schedules. Will update status to Ready once all vendor and in-house scopes are signed off.**" → one read yields "not ready / hold." The binary is single-hop; the ≤40% workhorse must be the NET figure (INJ-1), per oracle + L36.

## Future 4C calendar events (F9 / H4)
Exactly **ONE** future 4C event: **`2026-07-15 10:00` "Make-Ready QC Inspection – Mesa Vista 4C"** (confirmed) — desc "Final make-ready QC inspection... after interior repaint and deep clean." All other 4C events (Sunshine deep clean 5/21, interior repaint 5/21) are past. → H4 valid: any "only X outstanding" claim must reconcile this un-occurred QC inspection. Single clean future event → F9-safe provided the deliverable does not over-claim completeness.

## Injection decision — UNCHANGED, now firmer
Path **(a)** stands: **INJ-1 only** — an unapplied ~$340 QuickBooks `credit_memo` vs `PD-2026-09`, Permian-vendor-scoped (a "Mesa Vista 4C" sweep misses it) → true repaint outstanding $1,000, so the open-scope net is $1,387 stated nowhere. Additive (base rows untouched); operator-authorized; clears `validate.py --phase injection` (7 gates + difficulty ≥ 3.5). The native AP/AR $200 gap + 9-Sunshine near-miss are bonus symmetric pressure.

---
> ⬇️ Below: the REDO plan (still valid on levers/density/breadth/stumps) then the superseded original. Numeric census in the REDO plan's "Verified atoms" table is superseded by the table above (it had INJ-2 conditional + the $387-is-only-AR error).
---

# Hardness Plan — Task 45 (StarPM V4) — REDO REBUILD (2026-07-27)

Universe: **starpm** · Framework **V4** (dual-model: Opus 4.8 + Gemini) · Universe today **2026-07-01** America/Chicago.
Density scheme: **StarPM per-model** — design 40+, floor 15 (NOT the V3-family 50/40 scheme).

> **This section supersedes the original pre-REDO plan below.** The original failed T2 difficulty — Opus 4.8 passed 6/6 (pass@1 0.75). Root causes: (A) total prompt leakage; (B) the Opus-selective lever (L1/L10 recency/latching/supersession) is 4.8-robust. Autopsy: `_aux/REDO_reason.md`; empirical finding: Learnings **L36**; failing evidence + originals: `_aux/Candidate_Originals/`. Oracle consult driving this rebuild: `ses_05ba878c1ffeqGmkLJDrrW46Ku`.

## ⚠️ HEADLINE — OPERATOR DECISION REQUIRED BEFORE S1

Oracle ruled, after grounding every atom against the split: **a prompt-only rebuild will NOT push Opus 4.8 to ≤40%.** The truth (`recbd087.fldNotes2`) states "deep clean and interior repaint still open" in a SINGLE field; the arithmetic on top is trivial for Opus; the current-vs-prior-turn attribution is the exact semantic disambiguation Opus already aced. Estimated prompt-only Opus pass ≈ 50–67%.

**To defeat Opus 4.8 you need a graded value that survives careful reading — a value conflict between structured records where NO single field states the answer.** On this universe that requires **minimal V4 injection** (adding rows; base rows untouched). This EXCEEDS `REDO_reason.md`'s "prompt-only, no universe edits" scoping, so it is an operator call — see `## Injection requirement & operator decision`.

## Persona and Business Function (UNCHANGED — retained from S0)
- **Jaime Salinas** (QC Inspector, `p_007`, jaime.salinas@starpm.com) — impartial QC sign-off: walks units after maintenance declares complete, validates punch-list, signs off marketing-ready OR kicks work back. Never the primary actor.
- **Business Function 3 · Quality Control & Field Services.**
- Systems: Airtable (Make-Ready QC), Slack #make-ready (C004) / #maintenance (C001), Linear (QC issues), Gmail draft (onsite-PM/owner), QuickBooks (vendor bills). Voice: short, factual, observation-first, zero emoji.

## Verified atoms (grounded against `_aux/Universe_Split/` this session)
Token-count + oracle field-read confirmation. Exact QB balances / AP-vs-AR carry `[VERIFY-AT-INJECTION]` — pinned when injection is authored and run through `validate.py --phase injection`.

| Atom | id / doc | Exists? | Role |
|---|---|---|---|
| Live current turn | airtable `recbd087a4abd605b` (tblMakeReady, selProg, moveOut 6/15, target 6/30, note "deep clean + interior repaint still open") | yes (token+field) | **TRUTH: not ready** |
| Decoy prior turn | airtable `recc8534b3fd13954` (selReady, moveOut 6/1, "confirmed ready") created 5/29 | yes | W1 decoy |
| Decoy "complete" ticket | airtable `reca424761ae15355` (MR-4C-2026-08, "all complete, market-ready, Brooke notified") | yes | W3 decoy |
| Open turn ticket | airtable `rec12969a3fdb0852` (MT-2026-084, turn opened 5/1) | yes | corroborator |
| Repaint bill (current) | QB `PD-2026-09` (Permian, interior repaint, ~$1,340, unpaid) | yes (token) | L11 gross anchor |
| Punch/condition bill (current) | QB `2026-481-566` (~$85, unpaid) | yes (token) | current-turn line |
| Closet-trim bill (PRIOR) | QB `2026-519` (Permian, ~$85, prior turn recc8534) | yes (token) | W2 wrong-include bait |
| Owner AR invoice | QB `2026-534` (Linda Castillo, deep clean+repaint+trim ~$1,622) | yes (token) | W-AR bait (receivable, NOT payable) |
| credit_memo schema | QB entity_type `credit_memo` (117 present) | yes | INJ-1 is schema-consistent |
| Future QC event | gcalendar "Make-Ready QC Inspection – Mesa Vista 4C" 2026-07-15 (4C events ×20) | yes (token; oracle field-read 7/15) | L9 open-gate |

**Census correction vs original plan + L36:** the "$387 + $1,340 unpaid bills" claim is WRONG. $387 is a *line inside* AR invoice `2026-534` (owner receivable), not a standalone AP bill. Actual current-turn AP payables = repaint `PD-2026-09` (~$1,340) + condition `2026-481-566` (~$85). The prior-turn closet-trim `2026-519` (~$85) must be EXCLUDED from any current-turn figure. `[VERIFY-AT-INJECTION]` exact amounts + whether a standalone current-turn deep-clean AP bill exists (drives INJ-2).

## Levers Available
| # | Lever | Status | Evidence | Learnings |
|---|---|---|---|---|
| 1 Latching | decoy-only | reca424 + recc8534 say "done" vs recbd087 selProg | L1/L13 |
| 2 Structured-DB skip | **yes (primary)** | QB payables + recbd087 not mirrored in chatter | L2 / item11 |
| 3 Missing reply | partial | C004 chatter, no decisive resolver | L3 |
| 4 Search-cap eviction | **yes (support)** | INJ-1 credit memo vendor-scoped, evades "4C" sweep | L4 |
| 5 Thread-reply blindness | partial | — | L5 |
| 6 Near-miss entity | decoy-only | cross-property Unit 14 / Las Palmas 8D | L4 |
| 7 Multi-write | **yes (density)** | Airtable+Linear+Slack+Gmail+QC-log writes | L7 |
| 8 Multi-link chain | **yes (Opus-pressure)** | turn→bill attribution + precedence | L36 |
| 9 Universe gotcha | **yes (support)** | 7/15 future QC event + past-due 6/30 | L9/L14 |
| 10 Reversal/supersession | RETIRED (4.8-robust) | recency proven aced | — |
| 11 Net-vs-gross | **yes (primary, needs INJ-1)** | gross $1,340 vs net $1,000 via credit | L11/L18/L34 |
| L31 Negative directive | **yes (Gemini-sel)** | do-not-sign / do-not-list | L31 |

## Selected Levers (dual-model recipe: 1 symmetric + 1 Opus-pressure + 1 Gemini-sel + 2 support)
1. **SYMMETRIC PRIMARY — L2 QB-skip × L11 net-vs-gross, hardened by INJ-1.** Graded value = current-turn unpaid vendor liability NET of an unapplied credit. Gross ($1,340 / $1,510) is wrong; net ($1,000 → total ~$1,085) is stated by NO single field. Both models fail if they report the Balance field. **The ≤40% workhorse.** Cost +7–10 (QB sweep incl. vendor-scoped credit hunt).
2. **OPUS-PRESSURE — L8 current-vs-prior-turn bill attribution + precedence.** Which payables belong to the LIVE turn (recbd087) vs the PRIOR turn (recc8534) when the "complete" ticket and prior selReady both say done. **Honest label: trends SYMMETRIC on 4.8 — NOT a reliable Opus-selective lever; difficulty must NOT rest on it alone.** Cost +4–6.
3. **GEMINI-SELECTIVE — L31 explicit negative directive.** Close-out must explicitly say do-NOT-sign-off / do-NOT-release-for-marketing / hold. Gemini omits ~100%; Opus issues it. De-scaffolded (prompt must NOT contain "hold it"). Folded into writes.
4. **SUPPORT — L4 eviction** (INJ-1 credit memo vendor-scoped, not keyword-"4C") **+ L9 future-event** (7/15 QC inspection + past-due 6/30). Cost +3–5.

**RETIRED:** L1/L10 recency/latching/"latest-row"/"trust-the-DONE-ticket"/supersession — proven 4.8-robust on THIS universe (REDO_reason + L36). recc8534 / reca424 remain ONLY as decoys, never the disambiguation load.

## The new hardness engine — computed net-vs-gross (replaces the retired recency lever)
- **INJ-1** (QB `credit_memo`, UNAPPLIED): Permian Make-Ready, ties to repaint `PD-2026-09`, RemainingCredit ~$340, DocNumber `CM-2026-04xx`, PrivateNote = short-pay / re-do dispute on the 4C repaint. **Vendor-scoped, NOT keyword-"4C"** → a "Mesa Vista 4C" sweep misses it; only a Permian-vendor sweep finds it (L4 eviction). Base rows untouched; `PD-2026-09.Balance` stays $1,340.
- **INJ-2** (conditional — only if injection-authoring confirms NO current-turn deep-clean AP bill): one QB `bill`, Sunshine Cleaning, deep-clean 4C, Balance >0, so "deep clean" (a scope recbd087 names open) carries a real payable and the outstanding set is arithmetically complete. Keep injection to **1–2 rows.**
- **Computed target (pin at injection):** current-turn unpaid vendor liability NET of credit = repaint ($1,340 − $340 = **1,000**) + condition 2026-481-566 (**85**) [+ deep-clean if INJ-2] = **~$1,085**.
- **Intermediate WRONG answers (for the L18 rubric):** `1,510` (gross; credit missed + prior-turn trim wrongly included) · `1,425` (trim excluded, credit missed) · `1,622` (grabbed owner AR invoice) · `3,132` (AP+AR double-count) · `1,170` (kept prior trim, applied credit). The correct figure appears in NO artifact (L6-safe).

## Prompt-leakage contract (HARD — the primary root-cause fix, carry to S1)
The prompt MUST force discovery. It MUST NOT: define billed-but-unpaid or say a bill's status gates closure; enumerate the open scopes (deep clean / interior repaint); pin the turn by move-out (6/15) or target (6/30) dates; name the 7/15 re-inspection as a gate; scaffold the negative ("hold it" / "say so plainly").
It CAN say: the onsite PM reported Mesa Vista 4C wrapped from its recent turn and wants it released for listing; run your QC pass and record your determination + what (if anything) is outstanding to close the turn, including the dollars still owed to vendors.
**S1 audit rule:** for each rubric discriminator, find the prompt sentence that satisfies it without discovery. If one exists, the prompt leaks — tighten it. (This is exactly what the original failed — L36.)

## Tool-Call Density Projection (per model — StarPM: 40+ design, 15 floor)
| Component | MCP calls |
|---|---|
| Turn + ticket discovery (list + read 4 airtable rows) | 6–8 |
| Slack #make-ready/#maintenance + Calendar sweep | 4–7 |
| QB sweep (bills + owner invoice + **vendor-scoped credit hunt**) | 7–10 |
| Vendor/contacts cross-ref | 2–4 |
| Reconciliation re-reads | 2–4 |
| Writes (5–6) | 5–7 |
| **Subtotal MCP / total (×~1.35)** | **26–40 / ~35–54, mid ~45** |

**Per-model verdict: Opus ≈ 45 projected (margin +5 over 40).** ⚠️ **THIN in practice** — the original projected ~45 and Opus ran **37.0 actual**; real StarPM runs land 33–38. Clears the StarPM QC-spec floor (15) with wide margin but is at genuine risk of a sub-40 real-run average.

## THIN density acceptance + mandatory downstream mitigations
- Hold **5–6 DISTINCT writes** (do NOT collapse to 3): (1) Airtable QC determination on `recbd087`; (2) Airtable QC-log row; (3) Linear `save_issue` for open scopes; (4) Linear `save_comment` enumerating each remaining scope + net dollars; (5) Slack `slack_send_message` #make-ready (C004); (6) Gmail `create_draft` to Brooke/onsite PM.
- The **vendor-scoped credit hunt** is the density engine that also carries L2/L4 — S2/S3 must force it via the "dollars still owed to close the turn" deliverable.
- **Hard S4 gate:** per-model average tool calls < 40 → PIPELINE REDO (AGENTS.md rule 11). Do not ship on a sub-40 real-run average.

## Service Breadth
| Service | Calls | % | ≥5% |
|---|---|---|---|
| airtable | 8–11 | 24% | yes |
| quickbooks | 7–10 | 21% | yes |
| slack | 4–6 | 12% | yes |
| linear | 3–4 | 9% | yes |
| gcalendar | 2–3 | 6% | yes |
| gmail (draft) | 2–3 | 6% | yes |
| contacts | 2–4 | 7% | yes |
| **Distinct services** | **7 of 8** | — | **PASS** |

## Stump Hypothesis (pre-registered, item-20 discipline)
1. **[HIGH] SYMMETRIC (L2×L11×INJ-1)** — both models report the GROSS figure ($1,510 / $1,622), not the net current-turn $1,085 → the close-out's outstanding-dollars criterion fails. **The ≤40% workhorse on both models.** Landing: W-gross / W-AR.
2. **[MED] symmetric-leaning (L8)** — prior-turn closet-trim $85 wrongly folded into current-turn outstanding. Landing `1,170`. Not relied on for Opus-selectivity.
3. **[HIGH] GEMINI-SELECTIVE (L31)** — reaches "not ready" but omits the explicit do-not-sign / do-not-list negative. Opus issues it.
4. **[MED] SYMMETRIC (L9)** — Calendar not swept → misses the 7/15 re-inspection as an open gate; over-claims "only X outstanding".

**Pre-registered:** Opus fails on **H1** (net figure); Gemini fails on **H1 + H3**. If a run reaches QB but lands on $1,510/$1,622, score L11 firing (not L2 failing).

## Lever changes from previous attempt (REDO delta)
| Slot | BEFORE (Opus 6/6 FAIL) | AFTER | Material difference |
|---|---|---|---|
| Symmetric | L2 QB-skip, NOT load-bearing | **L2 × L11 net, INJ-1 evicted credit** | net outstanding stated by NO single field; gross is wrong |
| Opus slot | **L1/L10 recency — FAILED (4.8-robust)** | **L8 turn-attribution (honestly symmetric-leaning); reliance shifted to symmetric H1** | recency RETIRED; difficulty no longer rests on the semantic disambiguation Opus aced |
| Gemini slot | L31, prompt-scaffolded ("hold it") | **L31 de-scaffolded** | keeps L31 live, removes the leak |
| Prompt | every discriminator named | **discovery-forcing; leakage contract above** | inference load restored (L36 fix) |
| Source of hardness | prompt-leaked single-field lookup | **injected value-conflict (net-vs-gross)** | binary/scope answer no longer sufficient to pass |

## Injection requirement & operator decision
**Oracle's committed ruling: minimal V4 injection is REQUIRED for ≤40%.** Sanctioned (AGENTS.md rule 4 — INJECTION is first-class for V4; the task already carries `9_Universe_inject.sql` + `4_Changelog.json`) and additive (base rows never modified/deleted). Adds the `validate.py --phase injection` gate (7 hard gates + difficulty ≥ 3.5 at council).

**It exceeds `REDO_reason.md`'s "prompt-only" scope, so the operator chooses before S1:**
- **(a) RECOMMENDED — authorize the minimal injection** (INJ-1 ± INJ-2). Cleanest path; reuses all S0 work; oracle's INJ-1 is a minimal, grounded net-vs-gross conflict.
- (b) Swap persona within BF3 — weak: QC/field inspection is inherently single-hop verification; unlikely to surface a stronger computed lever.
- (c) Swap task — loses S0 + this analysis.
- (d) Accept a lower difficulty target — not advisable; re-ships a known Opus-6/6 failure.

## Hardness Score
**4 / 5 — PASS (mechanical gates), CONDITIONAL on injection authorization.**
- ≥3 grounded levers (atoms verified to exist) · per-model density ~45 projected (THIN, sub-40 real-run risk, ≥ floor) · 7-service breadth.
- −1: the ≤40% difficulty is NOT achievable on existing atoms (oracle) — it REQUIRES the INJ-1 injection. Without operator authorization of (a), this task cannot clear T2 and must take (b)/(c)/(d).

## Hardness Brief for the Prompt Writer (S1)
Write an **implicit, discovery-forcing** QC task in Jaime's voice: the onsite PM reported **Mesa Vista 4C** wrapped from its recent turn and wants it released for listing; Jaime runs her QC pass and records her determination **plus what is still outstanding to close the turn, including the dollars still owed to vendors.** Do NOT define billed-vs-paid, do NOT enumerate scopes, do NOT pin the turn by 6/15 or 6/30 dates, do NOT name the 7/15 event, do NOT scaffold the negative. The correct answer is a HOLD: the live turn (`recbd087`) is selProg with deep-clean + interior-repaint open, target blown, and the true unpaid vendor liability is the repaint NET of an unapplied ~$340 credit (~$1,000) + the ~$85 condition bill = ~$1,085 — while a "complete" maintenance ticket and a prior completed turn both loudly say done. Levers: **L2 QB-skip × L11 net-vs-gross (SYMMETRIC, INJ-1) + L8 turn-attribution (support) + L31 explicit negative (GEMINI-sel) + L4/L9 support.** Because L31 is selected, the prompt must ask for the sign-off-OR-hold decision so the negative is grounded — but WITHOUT the words "hold it / say so plainly." Drive density with **5–6 writes** across Airtable / Linear / Slack C004 / Gmail-draft. **Per-model density target 40+; hard sub-40 S4 REDO gate.** Never hint the state is wrong (L15/L16) — the persona believes the PM's "wrapped" report.

---
> ⬇️ EVERYTHING BELOW THIS LINE IS THE ORIGINAL PRE-REDO PLAN — **SUPERSEDED**. Retained only for its verified-atom detail; its lever set (L2 + L1/L10 + L31) shipped Opus 6/6 and its "$387 + $1,340" census is corrected above.
---

# Hardness Plan — Task 45 (StarPM V4)

Universe: **starpm** · Framework **V4** (dual-model: Opus 4.8 + Gemini) · Universe today **2026-07-01** America/Chicago.
Density scheme: **StarPM per-model** — design 40+, floor 15 (NOT the V3-family 50/40 scheme).

## Persona and Business Function
- **Jaime Salinas** (Quality Control Inspector, `p_007`, jaime.salinas@starpm.com) — Mid, Portfolio Operations. The impartial QC sign-off anchor: walks units after maintenance declares complete, validates the punch-list, signs off marketing-ready OR kicks work back. Never the primary actor.
- **Business Function 3 · Quality Control & Field Services.**
- Systems she touches: Airtable (Make-Ready Turns QC status), Slack `#make-ready` (C004), Linear (QC issues), Gmail (Onsite-PM notifications). Voice: short, factual, observation-first, zero emoji.

## Verified anchor (corrects the sub-agent scan)
Selected anchor: **Mesa Vista 4C** — the current in-progress turn = Airtable **`recbd087a4abd605b`** (tblMakeReady, `fldTurnStatus=selProg`). A grounded grep (not the sub-agent's claim of 2 rows) shows **3 records across 2 tables** share "Mesa Vista 4C":

| Record | Table | Status | Distinguishing fields | Role |
|---|---|---|---|---|
| `recbd087a4abd605b` | tblMakeReady | **selProg** | fldMoveOut **2026-06-15**, fldTargetReady **2026-06-30**, fldNotes2 "deep clean and interior repaint **still tracking**… will update status to Ready once all vendor and in-house scopes are signed off" | **TRUTH — current turn, NOT ready** |
| `recc8534b3fd13954` | tblMakeReady | selReady | fldMoveOut 2026-06-01, fldTargetReady 2026-06-14, fldNotes2 "QC walkthrough by Jaime… **confirmed ready for leasing**" · created **2026-05-29** | DECOY — prior completed turn |
| `reca424761ae15355` | tblMaintenanceTickets | selHigh (pri) | fldTicketNumber MR-4C-2026-08, fldCompletionDate 2026-05-01, fldDescription "**All make-ready work… complete… market-ready**… Brooke Phillips notified to move forward with listing" | DECOY — maintenance ticket asserting DONE |

**The disambiguation trap (genuine, verified):** the DECOY selReady row `recc8534` was **created 2026-05-29 — LATER than** the truth selProg row `recbd087` (created 2026-05-22). An agent using a "latest record = current state" heuristic picks the completed prior turn and signs off. The correct signal is the **move-out date** (6/15 > 6/1 → the selProg row is the current turn) and the **past-due target** (6/30, now blown as of 7/01). Two make-ready rows with DIFFERENT move-out dates = two legitimate sequential turns of the same unit, not a duplicate.

## Levers Available (all 11)

| # | Lever | Status | Evidence (grounded) | Engineer into a natural ask | Learnings |
|---|---|---|---|---|---|
| 1 | Latching (first-framing "it's done") | **yes** | 2 of 3 "4C" records say DONE (`reca424` maint ticket "complete/market-ready"; `recc8534` selReady) vs `recbd087` selProg "still tracking"; onsite-PM chatter in Slack C004 reinforces "wrapped" | "Onsite PM says 4C wrapped — run your QC pass and get it listed" | L1/L13 |
| 2 | **Structured-DB skip** | **yes** | The "not ready" truth is ONLY in tblMakeReady `recbd087` (`fldTurnStatus=selProg`, fldNotes2 "still tracking") — never in Slack/Gmail chatter, which says done | Agent must query Airtable make-ready table (SoR), not stop at chatter | L2/L10/L11 |
| 3 | Missing reply | partial | C004 make-ready chatter but no decisive thread-reply resolver on the repaint/deep-clean state | not selected | L3 |
| 4 | Search-cap eviction | partial | C004 #make-ready = 144 msgs (busiest channel); 4C posts buried under Las Palmas / Las Vistas traffic | flavour only | L4 |
| 5 | Thread-reply blindness | partial | some C004 threads; no load-bearing reply pinned | not selected | L5/L12 |
| 6 | Near-miss entity confusion | **yes** | cross-property "Unit 14" (~8 rows: Rio Bend / Sunset Ridge / Tanya eviction); near-dup decoy PDFs `report-laspalmas-8d-qc-inspection.pdf` vs `-2.pdf` | keep as DECOY, never the named target | L4 |
| 7 | Multi-write diversification | **yes (density)** | write surface: Airtable update `recbd087` + Slack C004 post + Linear save_issue+save_comment + Gmail create_draft to onsite PM | prompt asks to record decision + open punch ticket + notify | L7 |
| 8 | Multi-link chain | partial | Slack "repaint done" → QB unpaid bills → Airtable selProg → 7/15 QC event | folds into L2 discovery | L8 |
| 9 | Universe-grounded gotcha | **yes** | confirmed FUTURE `Make-Ready QC Inspection – Mesa Vista 4C` **2026-07-15** (only future 4C event); target-ready **6/30 past-due**; Airtable-is-SoR not Slack/Linear | "the re-inspection hasn't even happened yet" punishes assumed-complete | L9/L14 |
| 10 | **Reversal / supersession** | **yes** | prior-turn selReady `recc8534` (created 5/29, later) supersedes-trap vs current selProg `recbd087`; + maint-ticket `reca424` "complete" | agent grabs the stale/completed record and signs off | L10 |
| 11 | Net-vs-gross | partial | 4C vendor bills unpaid (deep-clean + repaint balances > 0) — "work closed?" ≠ "bill paid?" | secondary corroborator to L2 | L11 |

## Selected Levers (3 stump + 2 supporting = 5 engaged)
Deliberate StarPM dual-model recipe (Learnings items 9-12, 11, 20): **one SYMMETRIC stump + two complementary asymmetric stumps**, supplemented by L7 + L9 for density/breadth.

1. **L2 Structured-DB skip — SYMMETRIC (primary).** The "4C is NOT ready" fact lives only in the tblMakeReady `selProg` row `recbd087`; the more-findable signals (maintenance ticket `reca424`, prior selReady row `recc8534`, Slack chatter) all say DONE. Both models fail if they stop at chatter. Reachable via Airtable list/get records on tblMakeReady. Cost **+4-7**.
2. **L1 latching + L10 supersession — OPUS-SELECTIVE.** The completed prior turn (`recc8534` selReady, created LATER) + the "complete" maintenance ticket bait "pick the latest / trust the ticket." Correct read: the current turn is the earlier-created, later-move-out selProg row. Cost **+4-6**.
3. **L31 explicit negative directive — GEMINI-SELECTIVE.** Correct output is a kick-back: "Mesa Vista 4C is **NOT** ready — do **NOT** mark Ready / do **NOT** release for marketing; hold until deep-clean + interior-repaint sign-off." Gemini omits the negative ~100%; Opus issues it. Grounded in Jaime's real footprint (she posts QC-fail / rework directives in C004). **PROMPT MUST ask for the sign-off-OR-kick-back decision** so the negative is grounded (avoids the Task-39 R6 "phrase never asked" defect). Cost folded into writes.

Supporting (density/breadth, not stumps): **L7 multi-write** (+9-12) and **L9 future-event gotcha** (+3-5).

## Tool-Call Density Projection (per model — StarPM: target 40+, floor 15)

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (sweep 4C across airtable/linear/slack/gmail/QB/calendar/contacts) | 14-24 | 19 |
| L2 structured-store-skip (reconcile 2 make-ready rows + maint ticket + QB open balances) | 4-7 | 5.5 |
| L1+L10 latching/supersession (current-turn vs prior-turn vs ticket cross-check) | 4-6 | 5 |
| L9 universe gotcha (7/15 future QC event + past-due 6/30 target + SoR reasoning) | 3-5 | 4 |
| Write actions (Airtable update `recbd087` · Slack C004 · Linear issue+comment · Gmail draft) + post-write verify | 6-9 | 7.5 |
| Cross-service buffer (param traps: slack `message`, gmail draft-only `body`, linear `team`; retries) | 3-6 | 4.5 |
| **TOTAL projected** | **34-57** | **~45.5** |

**Per-model verdict:** Opus ≈ **45**, Gemini ≈ **43** (same discovery sweep; the negative-directive delta is behavioral, not call-count). **Both ≥ 40 → PASS** on the StarPM per-model band; well above the 15 floor.

## Service Breadth (v11 G1 — of ~45 midpoint calls)

| Service | Calls | % of total |
|---|---|---|
| airtable | ~12 | 27% |
| linear | ~6 | 13% |
| slack | ~6 | 13% |
| quickbooks | ~6 | 13% |
| gcalendar | ~5 | 11% |
| gmail | ~5 | 11% |
| hubspot / contacts | ~5 | 11% |
| **Distinct services** | **7 of 8** | — |

**Breadth gate:** ≥ 4 distinct services each ≥ 5% → **PASS** (cross-service, not a single-service deep trap).

## Stump Hypothesis
1. **[HIGH] SYMMETRIC.** Agent latches on "done" — finds maintenance ticket `reca424` ("all complete, market-ready, Brooke notified") + selReady `recc8534`, and signs off / marks 4C Ready. **Missed:** current turn `recbd087` = selProg, deep clean + interior repaint "still tracking." **Mechanism:** L1 latching + L2 structured-DB skip. (Both models.)
2. **[HIGH] OPUS-SELECTIVE.** Agent reconciles the two make-ready rows but picks the WRONG one — the selReady `recc8534` is created 5/29 (LATER than the selProg row's 5/22), so a "latest record" heuristic misleads; or the agent treats the maintenance ticket as authoritative. **Missed:** the current turn is the earlier-created / later-move-out selProg row. **Mechanism:** L10 supersession + "latest-row" trap.
3. **[HIGH] GEMINI-SELECTIVE.** Agent describes 4C's state but omits the explicit NEGATIVE directive — no "do NOT mark Ready / do NOT release for marketing / hold." **Missed:** the kick-back instruction. **Mechanism:** L31 (Gemini omits negatives ~100%).
4. **[MED] SYMMETRIC.** Agent asserts "4C's only remaining item is X" without reconciling the confirmed future **2026-07-15** QC inspection and the past-due **6/30** target. **Mechanism:** L9 future-event / past-due gotcha (F9-adjacent).

## Single-target uniqueness pre-check (pipeline rule 13 — Task 39 origin)

| Candidate | tblMakeReady rows (verified count) | Verdict |
|---|---|---|
| **Las Palmas 8D** | **3 make-ready + 1 maint ticket** (`receb057…` selReady / `recf7aecc…` selProg / `rec651427…` selProg make-ready; + `recb403fe…` MT-2026-1325 maint ticket) + near-dup decoy PDFs + Task-39 history | **DO NOT NAME — reproduces the exact Task-39 fault** |
| **Las Vistas 9D** | **7** rows mixed status | **DO NOT NAME — most ambiguous** |
| **Unit 14** | ~8 across Rio Bend / Sunset Ridge / Tanya eviction | **DO NOT NAME bare — cross-property** |
| **Mesa Vista 4C** | **3** (2 make-ready: `recbd087` selProg LIVE / `recc8534` selReady prior; + 1 maint ticket `reca424`) | **USABLE — prompt MUST pin the current turn by content** |
| **Las Palmas 212D** | **1** (`rec184a5c…` selProg, "electrician visit needed") | **clean zero-ambiguity FALLBACK** |
| **Las Vistas 3C** | **1** (`rec291f42…`) — UNIQUE but CLOSED (passed 6/18) | reference/decoy only |

**Disambiguation contract (HARD requirement for S1 + S3):** because Mesa Vista 4C has 2 make-ready rows, the prompt MUST identify the target turn by distinguishing content — the **mid-June (6/15) move-out**, the **end-of-June (6/30) target-ready**, and/or the **upcoming 7/15 QC re-inspection** — NEVER by bare "Mesa Vista 4C." Any S3 write-action rubric on the make-ready record MUST bind to the **current in-progress turn** described by that content (row `recbd087`, selProg, move-out 6/15), never to bare unit name or to a bare record id. This closes F7 (ambiguous target) and the wrong-row-passes hole. If the councils judge 4C's disambiguation too fragile, fall back to **Las Palmas 212D** (bare-unique, no calendar conflict).

**Reachability / safety:** load-bearing fact reachable via `airtable` list/get records on tblMakeReady → read `fldTurnStatus` + `fldNotes2`. Answer is **not verbatim** anywhere (L6). Discriminator is a structured single-select + QB open balance + calendar event — **not** a base64 Gmail body (StarPM item-17 safe). Only future 4C event = the 7/15 QC inspection (the task's own forward action, not a competing open item → F9-clean as long as the prompt does not over-claim "only open item").

## Hardness Score
**4 / 5 — PASS.** Three grounded levers spanning the full dual-model recipe (1 symmetric + 1 Opus-selective + 1 Gemini-selective) + L7/L9 support; per-model density ~45/~43 (both ≥ 40); 7-service breadth. Deducted 1 point: the primary anchor is a multi-row unit (3 records) requiring the disambiguation contract above to clear F7 — it is not bare-unique on its own.

## Hardness Brief for the Prompt Writer
Write an **implicit** QC task (Jaime's voice): the onsite PM has reported **Mesa Vista 4C** wrapped from its **mid-June turn** and wants it released for listing — Jaime must run her QC pass and **record a sign-off OR kick-back decision**. **Pin the current turn** (`recbd087a4abd605b`) by content — the mid-June (6/15) move-out / end-of-June (6/30) target / the upcoming 7/15 QC re-inspection — **never bare "Mesa Vista 4C," and never Las Palmas 8D / Las Vistas 9D / Unit 14.** The correct answer is a **kick-back / hold**: the current row is `selProg` with deep-clean + interior-repaint "still tracking," target date already blown, vendor bills unpaid, QC re-inspection not yet performed — while a maintenance ticket and a prior completed turn both loudly say "done." Levers: **L2 structured-store-skip (SYMMETRIC)** + **L1/L10 stale-record/latest-row supersession (OPUS-SEL)** + **L31 explicit negative directive (GEMINI-SEL)**. Because L31 is selected, the prompt **must** ask for the hold/kick-back (do-not-market) decision so the negative is grounded. Drive density with 3+ writes across Airtable / Slack C004 / Linear / Gmail-draft. **Per-model density target: 40+.** Never hint the number/state is wrong (L15/L16) — the persona believes the PM's "wrapped" report and asks Jaime to execute.

**Density margin (Learnings L33 — design for margin):** the ~45 per-model midpoint clears the 40 target by only ~5 and leans on a generous base-discovery estimate while 3 writes are under-budgeted. Hold the write mix at **4-5 writes** across Airtable / Slack C004 / Linear / Gmail-draft (not 3) so real per-run counts do not dip under 40 — StarPM runs have landed at 33-38 per run.


## THIN density acceptance (added at S1 AUDIT — 2026-07-27)

S1 AUDIT (`_aux/Council_Reports/AUDIT_prompt.md`) found per-model density is THIN under the strictest minimizing read, below this plan's ~45/43 projection:
- Minimizing-agent sketch: ~21 tool calls per model (efficient discovery, no post-write verify).
- Council B competent-trajectory projection: Opus ~43 / Gemini ~41 (meets the StarPM 40+ design target).
- Empirical anchor (Learnings L33): real StarPM runs land 33-38 per run, in the THIN band (15-39), below the 40 design target.

**Accepted as THIN with per-task justification.** Density clears the StarPM QC-spec fail floor (15) with wide margin. The prompt text is sound (AUDIT: all 12 sub-dims 5/5, zero blocker) and already scaffolds the maximum reasonable write set without bolt-on; no prompt-side lever lifts the minimizing floor to 40 without adding unrelated asks (which would fail Coherence). Prompt-side floor-raisers already applied at S1: F2 reword ("record your QC determination on that turn" guarantees a valid Airtable write on the hold path, closing the fldTurnStatus-has-no-HOLD-enum no-op trap) and F1/F4 softening ("still tracking" -> "still open", removing the verbatim keyword shortcut to the target row).

**Mandatory downstream mitigations (carry to S2/S3/S4):**
1. S2/S3 preserve 5-6 DISTINCT writes, do NOT collapse to 3: Airtable QC determination on the current turn (recbd087), Linear issue, Linear comment enumerating each remaining scope, Slack C004 #make-ready post, Gmail draft to Carlos, Brooke notification as its own write (goal-only, rubric accepts any channel).
2. Hard S4 gate: per-model average tool calls < 40 -> PIPELINE REDO (AGENTS.md rule 11). Do not ship on a sub-40 real-run average.
3. S3 QC-status rubric binds to the current in-progress turn (recbd087, mid-June move-out / end-of-June target) and checks "did NOT advance to Ready" + "recorded the QC hold determination" - never a nonexistent hold enum value; not satisfiable by either "done" maintenance ticket or the prior selReady turn.

## Record census correction (added at S1 — 2026-07-27)

Council B + AUDIT corrected the anchor census above (lines 12, 89): Mesa Vista 4C has **4 records (2 make-ready + 2 maintenance tickets)**, not 3. The undercount missed the turn-OPEN maintenance ticket (rec12969a3fdb0852, MT-2026-084) alongside the "complete" ticket (reca424761ae15355, MR-4C-2026-08). This STRENGTHENS the latching bait (two "done"-flavored tickets, not one). S3: bind the QC-status rubric to recbd087, satisfiable by neither maintenance ticket nor the prior selReady turn recc8534.