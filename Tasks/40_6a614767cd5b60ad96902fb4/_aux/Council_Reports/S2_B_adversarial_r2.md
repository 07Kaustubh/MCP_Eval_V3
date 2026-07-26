# Council B — Adversarial QC + Density + Hardness Preservation (OE phase, REVISE round 2)

**Task:** 40_6a614767cd5b60ad96902fb4 · **Deliverable:** `6_Oracle_Events.txt` (19 OEs, revised) · **Universe:** StarPM (V4, dual-model) · **Persona:** Lisa Smith
**Density scheme:** StarPM V4 — 40+ design target / 15 floor, applied PER MODEL (NOT V3 50/40).
**Scope:** DELTA re-review. Prior pass = GO (Completeness 5/5, Accuracy 5/5). Only OE 14 (co-target) and OE 9 (wording nit) changed. The 17 other OEs confirmed byte-unchanged and are NOT re-litigated.

---

## Delta confirmation (the only two changed OEs)

- **OE 14 — co-target accommodation applied (exactly the prior pass's S3 forward-note #1, now fixed in place at OE level).** Now blesses BOTH `recc83c05d889b354` (latest-modified, carries the possession-hold note) AND `reca8230a8fd9ff51` (fldUnit literally "Sunset Ridge Unit 14") as co-valid write targets for the one Tanya Sunset Ridge Unit 14 turn; explicitly bars `rec94e86a3007dd5e` (Rio Bend) as target; instructs grading on hold CONTENT + correct-tenant/correct-property record, NOT exact record id. The "keep fldTurnStatus at selSched / do NOT advance to selProg or selReady" instruction is retained verbatim.
- **OE 9 — wording nit only.** "a payment of 8173.44 is applied" -> "the invoice nets to zero". No value changed (TotalAmt 8173.44 and Balance 0.00 both retained). This sharpens the books-vs-notes trap framing (zero balance must NOT be read as resolved).

---

## [B1] QC sub-dim scoring

SUB-DIM OE Completeness -> SCORE 5/5 -> The write-target lock-in gap flagged in the prior pass is now closed at the OE level: OE 14 names both legitimately-updatable rows and grades on content + correct-record rather than a single id, so the critical path no longer over-commits to one identifier while remaining fully specified (hold at Scheduled, do-not-advance, do-not-market, possession-not-returned rationale). No dependency link lost; no step removed. Full critical path (OE1 discovery -> OE2 disambiguation -> OE3 hold-note read -> OE4/5/6/7/9 supersession+arrears -> OE10/11 ESA -> OE12/13 mirror+contact -> OE14-18 five writes -> OE19 content pin) intact.

SUB-DIM OE Accuracy -> SCORE 5/5 -> OE 9's "the invoice nets to zero" is ground-truth-exact: invoice `283231782926` (DocNumber 7214) carries TotalAmt 8173.44 with Balance 0.00 after payment `952690463873` (TotalAmt 8173.44, UnappliedAmt 0) is applied — confirmed in `quickbooks.quickbooks_entities.json`. Describing the invoice END-STATE (Balance 0.00) is at least as accurate as describing the payment mechanism, and it more directly names the graded fact behind the PrivateNote conflict. OE 14's two blessed ids re-verified in `airtable.airtable_records.json`: `reca8230a8fd9ff51` = "Sunset Ridge Unit 14"/selSched/mod 2026-06-07; `recc83c05d889b354` = "Unit 14"/selSched/mod 2026-07-01 11:18:57/possession-hold note; excluded `rec94e86a3007dd5e` = "Rio Bend - Unit 14"/selReady/"back to rent-ready, ticket closed". No new tool, param, id, status, or figure introduced that misgrounds. The two prior NON-load-bearing accuracy watch-items (EV-047 balance reconfirm; QR-2026-0441 VendorRef) are untouched by this delta and still route to S3.

---

## [B2] Adversarial re-test of the make-ready-target seam

The prior pass's MAKE-READY-TARGET divergence (Moderate/advisory) was: a competent agent could update `reca8230a8fd9ff51` (only row NAMING "Sunset Ridge") instead of `recc83c05d889b354` (latest), and a record-id lock would make that a false-fail / channel-lock-in Major. The revised OE 14 resolves this by blessing both rows and grading on content.

**Does the accommodation break unique ground truth? NO.** The two blessed rows are:
- both the SAME Tanya Sunset Ridge Unit 14 turn,
- both currently `selSched` (so "keep at Scheduled" is satisfied identically by either), and
- graded on the UPDATE CONTENT the agent writes (the possession-hold note), not the row's pre-existing note — so `reca8230a8fd9ff51`'s stale "committed to a payment timeline" note is irrelevant to the grade; the agent must still write the correct hold content into whichever row it targets.

The graded end-state is therefore INVARIANT across the two blessed targets: held at Scheduled, not advanced, Sunset Ridge (not Rio Bend), possession-not-returned rationale. The accommodation NARROWS the fail set correctly (Rio Bend `rec94e86a3007dd5e` still fails — different property, already `selReady`; advancing to selProg/selReady still fails — Alt-path B from the prior pass, hold is uniquely correct per `recc83c05d889b354` + Brooke's Slack + no possession-return event). It does NOT widen ground truth to admit any wrong end-state. **Seam resolved; unique ground truth intact.**

---

## [B3] Density (StarPM V4, per model) — UNCHANGED

The delta added zero tool calls: OE 14 is the same single `update_records_for_table` write (the co-target text is prose guidance, not an extra call); OE 9 is the same `search_invoices`/`read_invoice`/`search_bills` sequence with a prose rewording. Projection holds from the prior pass: **Opus ~46, Gemini ~43 — both >= 40 = PASS**, consistent with Hardness_Plan midpoint ~48. No regression toward the 15 floor.

## [B4] Hardness preservation — ALL 5 LEVERS INTACT

- **S1 (possession-not-returned / negative-directive hold)** — INTACT, reaffirmed: OE 14 keeps "keeping fldTurnStatus at selSched" + "Do NOT advance fldTurnStatus to selProg or selReady" + the crew-must-not-mobilize/must-not-market hold content. ✓
- **S2 (delinquency supersession / latching)** — INTACT: OE4/5/6/7/9 unchanged in substance; OE 9's "nets to zero" sharpens (does not remove) the books-vs-notes conflict. ✓
- **S3 (HubSpot ESA structured-DB skip)** — INTACT: OE10/11 untouched. ✓
- **S4 (Unit 14 near-miss across properties)** — INTACT and STRENGTHENED: OE 14 now states `rec94e86a3007dd5e` (Rio Bend) "must never be the target," hardening the near-miss exclusion at the write step. ✓
- **S5 (authority-relayed anchor)** — INTACT: OE5 untouched. ✓

No HARDNESS_REGRESSION. The edits strengthen S1/S4 and remove no lever.

---

## [B6] Upstream propagation — NO NEW FLAG

The delta is OE-internal (write-target relaxation + wording nit); it implies no prompt change, consistent with the AUDIT's finding of no S1 change. In fact OE 14 now PRE-RESOLVES the prior pass's S3 forward-note #1 (grade on content + correct-unit, not record id) inside the OE itself, which strengthens S3's guidance rather than adding an upstream flag. The S3 forward-notes remain valid (rubric fairness on the make-ready target; EV-047 balance / QR-2026-0441 VendorRef reconfirm). **No PROPAGATE TO S1.**

## Nothing else regressed

17 OEs confirmed unchanged (OE1-8, 10-13, 15-19). Service mapping (airtable source-of-record vs Linear mirror), OE Completeness must-take steps, and OE Accuracy grounding from the prior GO all hold. No new ungrounded token introduced by the delta.

---

## VERDICT: **GO**

OE Completeness **5/5** (write-target lock-in gap closed by the OE 14 co-target clause). OE Accuracy **5/5** (OE 9 "nets to zero" = Balance 0.00, ground-truth-exact; no value changed; both blessed ids re-verified). Co-target accommodation resolves the make-ready-target adversarial seam **without breaking unique ground truth** (invariant graded end-state; Rio Bend still fails; advancement still fails). Density **unchanged** (Opus ~46 / Gemini ~43, both >= 40 StarPM bar). **All 5 hardness levers intact** (S1/S4 strengthened). **No new PROPAGATE TO S1.** The two S3 forward-notes carry unchanged.
