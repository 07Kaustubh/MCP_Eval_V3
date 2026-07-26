# Council B — Adversarial QC + Density + Hardness Preservation (OE phase)

**Task:** 40_6a614767cd5b60ad96902fb4 · **Deliverable:** `6_Oracle_Events.txt` (19 OEs) · **Universe:** StarPM (V4, dual-model) · **Persona:** Lisa Smith (Onsite Property Manager)
**Density scheme:** StarPM V4 — 40+ design target / 15 floor, applied PER MODEL (NOT V3 50/40).
**Role lenses applied:** Architect · Implementer · Red-team · Ground-truth · Integration. Verdict = union.

Grounding spot-checks performed against the per-task split (`_aux/Universe_Split/`):
- All 8 Airtable IDs confirmed: `reca8230a8fd9ff51` ("Sunset Ridge Unit 14", selSched, mod 2026-06-07), `recc83c05d889b354` ("Unit 14", selSched, mod 2026-07-01 11:18:57, "cannot begin until…possession is formally returned"), `rec94e86a3007dd5e` ("Rio Bend - Unit 14", selReady, rent-ready), `rec769c9f03f0b85f` ("Las Palmas 4B", plan-active/stale), `rec8005502043b755` ("Delinquency Escalation", selProg, "Payment Plan Breached"), `rec91517a5acab558` ("Unit 14", 3-Day Notice Jun 26/deadline Jun 29), `rec922b9a2d1b9451` (EVF-2026-014, "Owner Approved - Ready to File", Linda Castillo, 2026-06-30), `recc0ecc885e9645e` (DLQ-2026-0601, selHigh, $75 late fee).
- QuickBooks: customer `proj-2e48c594aab7` = Tanya Mitchell / tanya.mitchell@gmail.com ✓; payment `952690463873` TotalAmt 8173.44 → Invoice `283231782926` (DocNumber 7214) ✓; bill `QR-2026-0441` (id 232176553533) Balance 2132.00 ✓; bill `2026-EV-047` (id 146128608253) present ✓.
- Tool catalog: every referenced tool + param verified (`update_records_for_table` baseId/tableId/records; `slack_send_message` message; `create_draft` body; `save_comment` issueId+body; `create_event` summary/startTime/endTime; `search_crm_objects`/`get_crm_objects` object_type/object_ids).

---

## [B1] QC sub-dim scoring (3/4/5 NON-FAIL-only scheme)

SUB-DIM OE Completeness -> SCORE 5/5 -> Full critical path present: discovery (OE1 base/tables), Unit-14 disambiguation (OE2), current-state read (OE3), the delinquency-supersession chain (OE4/5/6/7/9), the QuickBooks arrears quantification (OE8/9), the HubSpot ESA structured-DB surface (OE10) + Gmail approval (OE11), the Linear mirror (OE12), the recipient contact lookup before drafting (OE13), and all 5 write actions (OE14 Airtable update / OE15 Slack / OE16 Gmail draft / OE17 calendar / OE18 Linear comment), with OE19 pinning the content requirements. No missing dependency link.

SUB-DIM OE Accuracy -> SCORE 5/5 -> Every load-bearing tool, service, parameter-trap, record ID, status, dollar figure ($8173.44 applied payment, $2132.00 QR-2026-0441 balance, $75 late fee), ticket number (DLQ-2026-0601, EVF-2026-014), date (2026-07-06 "early next week" from 2026-07-01 America/Chicago), channel (C003 #general, C004 #make-ready), and email matches the universe. Two NON-load-bearing residuals are logged as materialization watch-items (do not dock to 4 — neither misleads a rubric): (a) base literal `appPropertyOps` is discovered at runtime via OE1's `list_bases`→`list_tables_for_base`, so the string is non-load-bearing; (b) bill `2026-EV-047` Balance "185.00" was not independently reconfirmed this pass (existence + DocNumber confirmed) and `QR-2026-0441` is labeled "Tanya Mitchell, Unit 14" though its VendorRef is Alamo HVAC (PrivateNote is the Tanya eviction rent ledger, Balance 2132.00 exact) — verify EV-047 balance at S3.

---

## [B2] Adversarial alt-path

**Baseline OE chain:** disambiguate → read latest hold record → trace supersession → quantify arrears → surface ESA → update `recc83c05d889b354` held at Scheduled + 4 comms writes.

**Alt-path A — make-ready update TARGET (the flagged pressure point).** There are FIVE `tblMakeReady` rows for the one Tanya/Sunset-Ridge saga with drifting labels: `reca8230a8fd9ff51` ("Sunset Ridge Unit 14", the only row that NAMES the property, mod 06-07), `rec769c9f03f0b85f` ("Las Palmas 4B", mislabeled), `rec8005502043b755` ("Delinquency Escalation"), `rec91517a5acab558` ("Unit 14", 3-day), `recc83c05d889b354` ("Unit 14", LATEST, mod 07-01 11:18:57). The OE points OE14 at `recc83c05d889b354` (latest) and treats `reca8230a8fd9ff51` as the naming anchor. **Is this defensible?** Yes — the prompt says update "the *current* make-ready record on Unit 14," and `recc83c05d889b354` is the newest-modified and carries the true current state; `reca8230a8fd9ff51` describes a SUPERSEDED pre-breach state ("committed to a payment timeline"), so updating it would be *less* correct. **But a competent agent could legitimately update `reca8230a8fd9ff51`** precisely because it is the only row that disambiguates "Sunset Ridge," and might not realize the newer same-unit row exists. **Divergence named: MAKE-READY-TARGET (Moderate, ADVISORY — non-blocking).** Unique GROUND TRUTH is NOT broken: the graded end-state is content (held at selSched, not advanced, unit = Sunset Ridge not Rio Bend, possession-not-returned rationale), which is identical whichever row is written. The OE does not "over-commit" fatally — it names both rows and explains the relationship — but the risk propagates to S3: **the OE14 rubric MUST grade on update CONTENT + correct-unit, NOT on record-ID `recc83c05d889b354`**, or it becomes a record-lock-in Major. Carry to S3 (not an S1/OE defect).

**Alt-path B — advance vs HOLD (the core lever).** Could the agent read "owner signed off / Ready to File" (`rec922b9a2d1b9451`) and legitimately ADVANCE (selProg/selReady)? **No — hold is the UNIQUE correct end-state.** The latest record `recc83c05d889b354` (07-01) explicitly forbids it ("make-ready work…cannot begin until…possession is formally returned"); Brooke's Slack (ts 1782881568) confirms "JP coordination is underway"; the "crew to mobilize immediately" in `rec91517a5acab558` was CONDITIONAL on vacancy by Jun 29, which did not occur; there is no possession-return event anywhere. An agent that advances is latching on the superseded instruction — exactly the intended Gemini stump (L31). **OE3/OE6/OE14 make the hold uniquely correct.** No ground-truth divergence.

---

## [B3] Tool-call density projection (StarPM V4 — per model)

Per-OE minimal-path tally (dedup): OE1 base+tables 2 · OE2 disambig search+list 2 · OE3 read latest 1 · OE4 delinquency reads 2 · OE5 ticket search 2 · OE6 slack search+read 2 · OE7 slack read 1 · OE8 search_customers 1 · OE9 invoices+read+bills 3.5 · OE10 hubspot 2 · OE11 threads search+gets 3 · OE12 list+get issue 2 · OE13 contacts x2 2 · OE14 write 1 · OE15 write 1 · OE16 write 1 · OE17 (+list_calendars) write 2 · OE18 write 1 = **~33 floor**. The hardness is cross-record reconciliation (latching forces re-reading contradictory rows; multi-record `tblMakeReady` scans; Slack fan-out; sibling issues OPS-38/54; calendar-id resolution), which realistically adds the Hardness_Plan's cross-service buffer.

- **Projected Opus 4.8 count: ~46** (thorough: opens HubSpot ESA S3 surface, reconciles the latch across Airtable↔Slack↔QuickBooks, individual invoice/bill reads). **PASS (>=40).**
- **Projected Gemini count: ~43** (thinner margin: may skip/underweight the HubSpot ESA dig, shaving 2-4 calls, but fans out more searches on the disambiguation + eviction thread). **PASS (>=40), note it is the leaner model — still above the 40 design target and well above the 15 floor.**

Consistent with Hardness_Plan midpoint ~48 (my floor-only count is more conservative; the reconciliation buffer closes the gap). **Both models >= 40 = PASS.**

---

## [B4] Hardness preservation (5 levers)

- **S1 (possession-not-returned / negative-directive hold)** — EXERCISED: OE3 reads the hold note, OE6 corroborates JP-coordination in Slack, **OE14 issues the explicit hold + "do NOT advance fldTurnStatus,"** OE15/16/19 state the hold. ✓
- **S2 (delinquency supersession / latching)** — EXERCISED: OE4 traces stale plan-active vs breach vs eviction across the Airtable rows, OE5 (DLQ+EVF tickets), OE6 (Slack breach), OE7 (superseded payment-date commitment), OE9 (arrears). ✓
- **S3 (HubSpot ESA structured-DB skip)** — EXERCISED: OE10 pulls `ticket_8faab56c663352cfb8d61c994b2bae88` (OPEN ESA), OE11 the Gmail approval threads. ✓
- **S4 (Unit 14 near-miss across properties)** — EXERCISED: OE2 disambiguates Sunset Ridge vs Rio Bend vs the "4B" label, OE14 writes Sunset Ridge not Rio Bend, OE16/19 state the disambiguation. ✓
- **S5 (authority-relayed anchor)** — EXERCISED (prompt-carried; OE surfaces + reconciles): OE5 surfaces the genuine `rec922b9a2d1b9451` "Owner Approved - Ready to File" anchor and explicitly notes "owner approved the eviction FILING, which is not the same as possession having been returned"; OE3/6/14 supply the reconciling facts. ✓

**No HARDNESS_REGRESSION.** All 5 levers triggered by at least one OE step.

---

## [B6] Upstream propagation

**No upstream propagation flags.** The only substantive finding (B2 MAKE-READY-TARGET) has its root cause in the UNIVERSE (five drifting-label rows for one saga), not the prompt — and the prompt's "the current make-ready record on Unit 14" language actually helps select the latest row. The prompt correctly carries the persona's false "we're clear" belief (intended hardness) while the universe makes hold the truth; it correctly omits the ESA (S3 self-discovery). All prompt asks map to OEs. Nothing to re-run at S1. The B2 finding routes FORWARD to S3 (rubric grading), not back to S1.

---

## [B8] OE Completeness semantic (must-take steps)

- Disambiguate Unit 14 property → OE2 ✓
- Read the make-ready hold note → OE3 ✓
- Establish account is in active eviction, not on a plan → OE4/5/6/7/9 ✓
- Surface the approved ESA accommodation → OE10 (HubSpot) + OE11 (Gmail) ✓
- Resolve Brooke's email before drafting → OE13 (contacts → brooke.phillips@starpm.com) ✓
- The 5 writes → OE14 (Airtable) / OE15 (Slack) / OE16 (Gmail draft) / OE17 (calendar) / OE18 (Linear) ✓

No `OE_INCOMPLETE` lines. Zero missing must-take steps → **NON-FAIL not triggered (Completeness PASS).**

---

## [B9] OE Service mapping

- airtable (SOURCE OF RECORD): OE1-5, OE14 — make-ready + delinquency/eviction tickets (tblMaintenanceTickets DLQ/EVF correctly live in Airtable, not Linear/QuickBooks) ✓
- slack: OE6/7 (C003 eviction thread), OE15 (C004 #make-ready status) ✓
- quickbooks: OE8 (customer), OE9 (invoices/bills) ✓
- hubspot: OE10 (ESA ticket) ✓
- gmail: OE11 (ESA threads), OE16 (draft-only, correct — no send tool) ✓
- linear: OE12 (find OPS-32), OE18 (comment on mirror) ✓
- gcalendar: OE17 ✓
- contacts: OE13 ✓

No `OE_SERVICE_MISMATCH` lines. **Airtable-as-source-of-record vs Linear-OPS-32-as-secondary-mirror is CONSISTENT:** OE14 writes the authoritative Airtable row; OE18 only *comments* on the Linear mirror. ✓

---

## VERDICT: **GO**

Both OE sub-dims 5/5. No adversarial divergence breaks unique ground truth (hold is uniquely correct; the make-ready-target ambiguity preserves the graded end-state content). Density PASS on both models (Opus ~46, Gemini ~43, both >= 40). All 5 levers triggered — no HARDNESS_REGRESSION. No PROPAGATE TO S1. Every must-take step covered; every OE targets the correct StarPM service.

**Carry-forward to S3 (non-blocking, MANDATORY for rubric fairness):**
1. **[Moderate/advisory] MAKE-READY-TARGET** — the OE14 update rubric must grade on update CONTENT (held at Scheduled, not advanced) + correct-unit (Sunset Ridge, not Rio Bend), NOT on record-ID `recc83c05d889b354`. Two rows (`recc83c05d889b354` latest, `reca8230a8fd9ff51` explicitly "Sunset Ridge") are legitimately updatable; a record-ID lock would be a Major channel-lock-in.
2. **[Minor/accuracy] EV-047 balance** — reconfirm bill `2026-EV-047` Balance = 185.00 before it flows into any OE16 draft-content rubric; and note `QR-2026-0441`'s VendorRef is Alamo HVAC (its PrivateNote is Tanya's rent ledger, Balance 2132.00 exact) so any rubric citing it should key on the $2132.00 arrears + Tanya linkage, not the vendor label.
