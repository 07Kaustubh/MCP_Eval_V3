# Council B — Adversarial QC + Density + Hardness Preservation

**Task:** `43_6a62ccaf5853030245ac9d53` · **Phase:** S2 (Oracle Events) · **Universe:** starpm (V4)
**Deliverable under review:** `Tasks/43_6a62ccaf5853030245ac9d53/6_Oracle_Events.txt` (28 steps)
**Persona:** Carlos Mendez, Onsite Property Manager (`carlos.mendez@starpm.com`)
**Method:** five role lenses (Architect / Implementer / Red-team / Ground-truth / Integration), verdict = union not average. Every value re-verified independently from `_aux/Universe_Split/` (`row_data` parsed) and `StarPM_Base_Universe/7_Server_Tools_Details.json`. No upstream claim (Hardness_Plan, Verification_s1, Reads_s2) was taken on trust.

---

## Independent ground-truth re-verification (basis for everything below)

| Claim re-verified | Source file | Value found | Match |
|---|---|---|---|
| AR invoice 2026-534 = id 445653930748, Linda Castillo `proj-4ae920b7c9e8`, lines 387.00 / 1140.00 / 95.00, TotalAmt + Balance 1622.00, sync_token "0", TxnDate 2026-05-01 | `quickbooks.quickbooks_entities.json` | exact | YES |
| Exactly 4 bills reference "Unit 4C": 195089456477 / 546359391323 / 696089964235 / 991582431419; 1 invoice (445653930748) | same | exact, no 5th | YES |
| Repaint bill PD-2026-09 = 696089964235, Permian Make-Ready Crew (204), 1340.00 | same | exact | YES |
| Closet trim bill 2026-519 = 546359391323, Permian (204), 85.00 | same | exact | YES |
| Alamo bill 2026-481-566 = 991582431419, Alamo HVAC (200), 85.00, "Unit condition inspection and punch list documentation" | same | exact | YES |
| 10 bills at TotalAmt exactly 1340.00, all ten ids + vendors + properties as listed in OE 16 | same | all ten exact | YES |
| Decoy AR 340207319849 (2026-AP-0184, 1340.00, Linda Castillo, 412 Mesquite) | same | exact | YES |
| Pete Donovan receivables 240572546619 / 618793969708 / 328611897179 | same | exact | YES |
| No DocNumber 2026-537 anywhere | same | 0 hits | YES |
| Payment 931951074454 (510.00) links to 247748966591, NOT to 445653930748; it is the only Linda payment | same | exact | YES |
| No credit memo and no bill_payment touches 4C | same | 0 hits | YES |
| Airtable base `appPropertyOps`; tables `tblMakeReady` + `tblMaintenanceTickets`; fields fldUnit/fldTurnStatus/fldMoveOut/fldTargetReady/fldNotes2; **no cost field, no "Closed" status** | `airtable.airtable_fields.json`, `..._tables.json`, `..._bases.json` | exact (3 choices only: selSched/selProg/selReady) | YES |
| Exactly 2 `tblMakeReady` rows for "Mesa Vista 4C": recc8534b3fd13954 (selReady, mod 2026-05-29 14:26:59) + recbd087a4abd605b (selProg, mod 2026-05-22 21:14:34); siblings 107A/207A/310C | `airtable.airtable_records.json` | exact | YES |
| Tickets reca424761ae15355 (MR-4C-2026-08, selHigh, 2026-05-01) + rec12969a3fdb0852 (MT-2026-084) | same | exact | YES |
| Belief email 5101c5a41dffa90a in thread 66132537181ecbe1, Carlos→Linda, cc x5, cites "owner invoice 2026-537", "covers the vendor work only", zero dollar figures | `gmail.gmail_messages.json`, `..._threads.json` | exact | YES |
| Contacts: Linda Castillo `b47044b4ec775b318bac813d5fb1bf5d` job "Property Owner"; Pete Donovan job "Exterior Painter"; John Castillo decoy | `contacts.contacts.json` | exact | YES |
| Slack C004 = #make-ready, C005 = #vendors with exactly 6 messages none about 4C | `slack.slack_channels.json`, `..._messages.json` | exact | YES |
| Gmail has **no send tool** (create_draft only) | tool catalog | confirmed | YES |
| All 25 distinct tool names + every parameter name used in the OE | tool catalog | all exist, all on the right server, all params correct incl. `search_records.table`, `get_table_schema.tables`, `update_invoice.SyncToken/properties`, `create_draft.body`, `slack_send_message.message`, hyphenated `get-bill` | YES |
| **Answer-leak check:** "1812" / "1,812" as a dollar figure anywhere in universe or prompt | `Universe_complete_data.json`, `5_Prompt.txt` | 17 raw "1812" hits, **all** timestamps/ids; 0 as a figure. Prompt contains **zero** numerics except the "4" in "4C" | CLEAN |

**Two findings from this sweep that upstream artifacts did not record and that drive this report:**

1. **`546359391323` PrivateNote in full:** *"**Internal labor charge for Tony Reyes touch-up on Mesa Vista 4C closet trim.** Flagged during Jaime Salinas's QC inspection; completed same day. Routed and logged by Carlos Mendez. Pass-through to owner - pair with corresponding AR invoice to Pete Donovan's owner account for 4C make-ready close-out."* The phrase **"Internal labor charge"** occurs on **exactly two bills in the entire 625-entity ledger** — the two 85.00 4C bills. It is not boilerplate; it is a high-signal, symmetric cue.
2. **A sixth message belongs to the C004 4C trail:** ts `1779501872.000004`, from **Jaime Salinas (U2CD1BC03B2)**, not Carlos: *"Jaime flagged a paint touch-up on the bedroom closet trim. **Tony got it done today**, Airtable updated."* It sits between the two ts values the OE does list (…871.000003 and …873.000005).

Together with `recc8534b3fd13954` fldNotes2 (*"Touch-up routed to Tony Reyes and resolved same day"*), **three independent records attribute the closet trim to Tony Reyes, StarPM's own technician** — the exact counter-cue to the OE's pivotal exclusion decision, and the OE quotes none of it.

---

## [B1] QC sub-dim scoring — Oracle Events dimension

```
SUB-DIM OE Completeness -> SCORE 5/5 -> REASON Forward map has zero gaps: all 11 prompt asks covered, all four required writes carry tool + key params + expected content, the negative guard (no second owner invoice) is explicit in OE 24, the Airtable write mechanism is pre-resolved against the real schema in OE 5, and the dependency chain bills -> invoice -> writes is unbroken.
SUB-DIM OE Accuracy -> SCORE 4/5 -> REASON Substantively correct and following it literally reaches 1812.00, but four verified expected-data imprecisions: OE 17 quotes bill 546359391323's PrivateNote from its second sentence and omits the opening "Internal labor charge for Tony Reyes touch-up on Mesa Vista 4C closet trim"; OE 8 presents four message ids as the return of a search_threads step whose real thread ids are 525641a76c00fbe0 / c138c134b23d60d3 / 83872812663ee5c9 / f43fdaee4372a09b; OE 22 attributes the "in the vendors channel" claim to summary email 5101c5a41dffa90a when it is in 13385eee8206db79; OE 22 and OE 23 enumerate the C004 4C trail as five Carlos messages and omit ts 1779501872.000004 from Jaime Salinas.
```

**Why Completeness holds at 5 and is not docked for OE 19.** OE 19 is a pure-reasoning step (no tool call) and by the phase-eval anti-pattern table that maps to a Non-Fail Completeness blemish. Scored against the QC spec's own PASS(5) text — *"OEs describe the full critical path: key discovery steps + dependency chain(s) + required write action(s)"* — nothing is **missing**: the reads OE 19 reasons over are OE 17 and OE 18, both present with exact ids, and the four grounds it states are content the spec wants documented. All four QC_Passed V4 reference OEs contain a tool-like token in every step, so the fold-in is a real convention fix (logged Minor below), not a missing critical step.

**Why Accuracy is 4 and not 3.** None of the four items is a wrong tool, wrong service, or wrong parameter *name*; every id, amount, date, address, and count in the OE is exactly right; an agent following the chain literally lands on 1812.00 and executes the four correct writes. That is the NON-FAIL(4) band ("substantively correct but contain minor imprecisions"), not NON-FAIL(3) ("would not produce the correct results if followed literally"). The OE 17 omission is nonetheless **Major in consequence** (see B6) because the sentence it drops is the single strongest argument for the competing 1727.00 end-state, and S3 will write the 1812.00 rubric from an OE that never mentions it.

**All four fixes are surgical; applying them lifts Accuracy to 5.**

---

## [B2] Adversarial alt-paths

Nine readings tested. For each: does the OE chain hold, or is the root cause upstream?

| # | Alternative agent path | Resulting end-state | Foreclosed by | Verdict |
|---|---|---|---|---|
| A | Trust AR 2026-534 + Carlos's "fully wrapped up" email; declare charges clean; take the "log 4C closed and that is the end of it" branch | 1622.00, one write (Airtable close), no email, no Slack, no invoice edit | Prompt S7: *"Go back to what each vendor charged us for the 4C work and set it against the line items I sent her"* — an agent that never opens an AP bill has not performed the instructed comparison | **OE correct.** This is the designed L2 flagship stump, not ambiguity |
| B | Include the Alamo 85.00 because "we actually paid it out on that unit" to an outside vendor | **1897.00**, adds a 4th line to her invoice | Prompt S9 names both nouns: bill 991582431419 is literally *"Unit condition inspection and punch list documentation"* with note *"Internal labor charge for Carlos Mendez's make-ready walk"* = "an internal walk or a condition check we handled in house"; and it was never a line on 2026-534 | **OE correct** (OE 18 + OE 19 + OE 21 cover it) |
| C | **Drop the closet trim 85.00 as our own time** — cites bill note *"Internal labor charge for Tony Reyes"*, Airtable *"routed to Tony Reyes"*, Slack *"Tony got it done today"*, against prompt S9 *"Anything that was our own time on the unit … stays off her bill entirely"* | **1727.00**, removes line 3 from her invoice | Prompt S8 *"Only outside vendor work belongs on her side"* + payee is Permian Make-Ready Crew (204), an active third-party vendor we actually paid; prompt S9's appositive names a *walk* and a *condition check*, not a trim repair; belief email puts the trim **inside Pete Donovan's vendor repaint scope** and buckets Tony's work separately as "internal repairs in-house"; the same PrivateNote directs *"Pass-through to owner"*; the three genuinely in-house items (faucet / GFCI / drywall) carry **no AP bill at all**, so "our own time" produces no payout to pass through | **OE chain is right but UNDER-ARMED.** Not a prompt defect — see B6 adjudication. Fix belongs in OE 17 + OE 19 |
| D | Issue a credit memo against 2026-534 instead of amending | cannot reach 1812.00 | **Structurally foreclosed by the direction of the error**: the correction *raises* 1622.00 to 1812.00; a credit memo only reduces AR. No 4C credit memo exists in the ledger | **OE correct.** OE 24 forecloses `create_invoice` explicitly; adding "and no credit memo" is optional polish (Minor) |
| E | `delete_invoice` 445653930748 then `create_invoice` re-issuing DocNumber 2026-534 at 1812.00 | same figure, same DocNumber, new record id | Not foreclosed — but converges on the load-bearing end-state (one owner invoice for the turn, carrying 1812.00) | **Not a UGT divergence.** Carry to S3: grade on "the single owner invoice for the 4C turn carries 1812.00 across the three corrected lines and no second owner invoice exists", **not** on `update_invoice` being called against id 445653930748 |
| F | Bill **Pete Donovan** (`proj-f6f9edfeae5c`) — both 4C bill notes say *"pair with corresponding AR invoice to Pete Donovan's owner account"* | 1812.00 on the wrong customer | Prompt S2 *"Linda Castillo owns that unit"*; AR 2026-534 CustomerRef = Linda; Contacts job "Property Owner" vs "Exterior Painter" | **OE correct** (OE 1 / 9 / 10 = designed L6 near-miss) |
| G | Write the close to the stale `recbd087a4abd605b`, or to both rows, or create a new row | Airtable end-state varies by record id | OE 25 already grades on content not id and explicitly permits bringing the stale row into line | **OE correct and deliberately id-agnostic** |
| H | Post to C005 #vendors or C006 #owner-relations instead of C004 | different channel | Prompt S15 is channel-agnostic ("our channel for the crew and front office"); OE 27 pre-authorises all three | **OE correct** — S1 watch-item #1 discharged |
| I | Resolve owner identity in HubSpot (`contact_25b3475250fb5726b54874670b946bbe`, jobtitle "Property Owner") instead of Contacts | same identity | n/a — equivalent surface | **Not a divergence.** OE 1 does not foreclose it; no fix needed |

**Net:** exactly one alt-path (C) has real teeth, and its teeth are in evidence the OE never confronts. No alt-path produces a second *defensible* end-state.

---

## [B3] Tool-call density projection — StarPM per-model scheme

Gate confirmed from `AGENTS.md` line 23 + `Reference/Hardness_Playbook.md` line 32: **StarPM v4, per model — midpoint >= 40 = PASS, 15-39 = THIN, < 15 = INSUFFICIENT.** Never the V3 50/40 scheme.
**`## THIN density acceptance` section verified present** in `_aux/Hardness_Plan.md` (line 96, with three per-task justifications and an S4 watch-item) — so a THIN band is an operator decision here, not a block.

### Opus 4.8 trajectory sketch (competent run, solved branch)

| OE | Calls | Tools |
|---|---:|---|
| 1 | 3 | `contacts_search_contacts` x2, `contacts_get_contact` |
| 2 | 2 | `list_bases`, `list_tables_for_base` |
| 3 | 1 | `search_records` (tblMakeReady) |
| 4 | 1 | `list_records_for_table` (recordIds x2) |
| 5 | 1 | `get_table_schema` |
| 6 | 1 | `search_records` (tblMaintenanceTickets) |
| 7 | 2 | `search_threads`, `get_thread` |
| 8 | 4 | `search_threads` x2, `get_thread` x2 |
| 9 | 1 | `search_customers` |
| 10 | 3 | `search_invoices` x3 (owner / unit / "2026-537") |
| 11 | 1 | `read_invoice` |
| 12 | 2 | `get_aged_receivables`, `get_customer_balance` |
| 13 | 2 | `search_bills` x2 ("Unit 4C", "Mesa Vista 4C") |
| 14-15, 17-18 | 4 | `get-bill` x4 |
| 16 | 1 | `search_bills` (amount cluster) |
| 19 | 0 | reasoning |
| 20 | 2 | `search_vendors` x2 |
| 21 | 1 | `get_vendor_expenses` (optional corroboration) |
| 22 | 2 | `slack_search_public_and_private` x2 |
| 23 | 1 | `slack_read_channel` |
| 24 | 2 | `update_invoice` + `read_invoice` re-verify |
| 25 | 2 | `update_records_for_table` (live row, then stale row) |
| 26 | 1 | `create_draft` |
| 27 | 1 | `slack_send_message` |
| 28 | 3 | `read_invoice`, `list_records_for_table`, `list_drafts` verification reads |

### Per-model result

| Model | Range | **Midpoint** | Band | Gate |
|---|---|---:|---|---|
| **Opus 4.8** | 36-52 | **44** | >= 40 | **PASS** |
| **Gemini** (solved branch, empirical −9.5 on this universe) | 26-40 | **34** | 15-39 | **THIN_DENSITY** — accepted (Hardness_Plan `## THIN density acceptance` present) |
| **Gemini** (stumped branch, see caveat) | 24-32 | **~28** | 15-39 | **THIN_DENSITY** — still well clear of the 15 INSUFFICIENT floor |

Gemini's economies, step by step: OE 1 collapses to 1 call, OE 8 to 2, OE 10 to 2, OE 12 to 1, OE 13 to 1, OE 20 to 1, OE 24/25 to 1 each, OE 28 to 1, and it skips the optional `get_vendor_expenses`. That reconstructs to 30 on a lean run and ~38 on a thorough one — consistent with the Hardness_Plan's independent ~34.

**Density caveat the Hardness Plan's mitigation does not cover (new finding).** Hardness_Plan `## THIN density acceptance` item 2 argues "writes execute on BOTH models", but prompt S10 makes three of the four writes **conditional**: *"If her charges come out clean against what we paid, log 4C closed and that is the end of it."* A model that stumps at 1622.00 legitimately takes the one-write branch and never drafts the email or posts to Slack, shedding ~4-5 calls. Since the L2 flagship is projected to sweep Gemini (~0/12 on the two prior StarPM tasks), the **modal** Gemini run is the stumped branch at ~28, not the solved branch at ~34. Still THIN, never INSUFFICIENT — but the Hardness_Plan's "write-heavy OE pulls Gemini toward ~40" claim does not hold for stumped runs. **Carry to S4:** if the first Gemini run lands < 30 that is expected, not anomalous; the actionable threshold is < 24.

### Service breadth (against the Opus 44-call sketch)

| Service | Calls | Share | OE steps |
|---|---:|---:|---|
| quickbooks | 20 | 45.5% | 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 24, 28 |
| airtable | 9 | 20.5% | 2, 3, 4, 5, 6, 25, 28 |
| gmail | 8 | 18.2% | 7, 8, 26, 28 |
| slack | 4 | 9.1% | 22, 23, 27 |
| contacts | 3 | 6.8% | 1 |
| **Distinct** | **5** | — | dominant quickbooks **45.5% < 60%**, every service >= 5% |

**Breadth: PASS.** Reconciliation note: Hardness_Plan's breadth table projected **6** services by including linear (~7%) and hubspot. The OE realizes **5** and uses neither — and that is **correct, not a regression**: per `Validators/universes.py` `oe_service_map`, `maintenance_tickets -> airtable` with Linear as the secondary mirror, so a Linear step here would have earned an `OE_SERVICE_MISMATCH`. The Hardness Brief's operative target was "4-write / 5-service OE" and that is met exactly.

---

## [B4] Hardness preservation

| Lever | Status | OE steps that exercise it |
|---|---|---|
| **L2 — Structured-DB skip (SYMMETRIC flagship)** | **PRESERVED** | **OE 13** (the four AP bills are the entire payout universe, "no total is stored anywhere"), **OE 15** (1340.00 vs the 1140.00 charged; "This figure exists nowhere except on this bill, not in the invoice, not in the summary email, and not in Slack"), **OE 17** (85.00 vs 95.00), **OE 21** (derives 1812.00). Re-verified: 1812.00 appears **zero** times as a figure in the universe — the answer is genuinely derived |
| **L10 — Reversal / supersession** | **PRESERVED** | **OE 11** ("these three amounts are the claim under test and must not be trusted as the cost side"), **OE 15 / 17** (AP bills supersede the AR lines), **OE 3** (selReady row supersedes the stale selProg snapshot), **OE 7** (the email's own invoice number 2026-537 does not exist), **OE 24** (amend in place), **OE 27** ("superseding the 1622.00 figure") |
| **L6 — Near-miss entity (OPUS-asymmetric)** | **PRESERVED** | **OE 1** (Linda vs Pete vs John Castillo), **OE 9** (`proj-4ae920b7c9e8` vs `proj-f6f9edfeae5c`), **OE 10** (decoy 340207319849 at 1340.00 to the *same owner, different property* + three Pete receivables), **OE 16** (all ten 1340.00 bills enumerated and correct; "Bind by unit, never by amount"), **OE 19** (twin 85.00 charges) |
| **L11 / L9 — Net-vs-gross + universe-grounded gotcha (GEMINI-leaning)** | **PRESERVED but WEAKENED** | **OE 18** (the internal walk), **OE 19** (four-ground discrimination), **OE 21** (1897.00 and 1727.00 named as wrong), **OE 25 / 28** (exclusion carried into the writes). **Weakening:** OE 19's ground #2 rests on "the instruction on each record" — but both records open with the identical sentence template *"Internal labor charge for <@starpm.com person>"*, which OE 17 does not quote and OE 19 never rebuts. The lever survives; its rubric-side defensibility does not, until fixed |
| **L1 — Latching (reserve, not summed into density)** | **PRESERVED** | **OE 3** ("its 'still tracking' language must not be read as the current state"), **OE 4**, **OE 6** ("The physical work being complete is not evidence that the owner billing is correct"), **OE 7** (belief email "fully wrapped up") |

**`HARDNESS_REGRESSION`: none.** 4/4 selected levers plus the L1 reserve are each exercised by named OE steps.

**Stump-leak check.** The OE states 1812.00 openly at OE 21, 24, 25, 26, 27 and 28 — allowed and expected; the OE is a CB planning document. The prompt is clean: `5_Prompt.txt` contains **no numeric token at all** other than the "4" inside "4C", no invoice number, no vendor amount, and no hint that any figure is wrong. Re-grepped the whole per-task universe for "1812"/"1,812": 17 raw hits, **all** epoch timestamps and Slack ts values, **zero** as a dollar figure. The stump is intact.

---

## [B6] Upstream propagation

**Adjudication of the one candidate — the twin 85.00 charges and the 1727.00 end-state.**

The brief's premise is confirmed exactly: **both** bills open their PrivateNote with *"Internal labor charge for <an @starpm.com person>"* — 546359391323 for **Tony Reyes**, 991582431419 for **Carlos Mendez** — and that phrase appears on **no other bill in the 625-entity ledger**. Two further records reinforce the trim-was-internal reading: `recc8534b3fd13954` fldNotes2 *"Touch-up routed to Tony Reyes and resolved same day"* and Slack C004 ts `1779501872.000004` *"Tony got it done today"*. This is a materially stronger counter-case than any upstream artifact recorded.

Weighing it against the prompt as written, not against the OE:

| Pro-1727 (exclude the trim) | Pro-1812 (keep the trim) |
|---|---|
| Bill note sentence 1: "Internal labor charge for Tony Reyes touch-up" | Prompt S8: *"Only outside vendor work belongs on her side"* — the payee is **Permian Make-Ready Crew (204)**, an active third-party vendor with `billing@permianmakeready.com`; the 85.00 genuinely left the business |
| Airtable: "routed to Tony Reyes and resolved same day" | Prompt S9's appositive names *"an internal walk or a condition check"* — 991582431419 is literally *"Unit condition inspection and punch list documentation"* for *"Carlos Mendez's make-ready walk"*; a bedroom trim repaint is neither |
| Slack: "Tony got it done today" | Belief email (the very record prompt S5 puts under test): *"Pete Donovan finished the interior repaint (**including a touch-up on the bedroom closet trim** that came out of our QC walkthrough), **and** Tony's team handled all internal repairs in-house"* — trim is placed on the vendor side of the sentence's own conjunction |
| Prompt S9 leading clause: *"Anything that was our own time on the unit"* | Same PrivateNote, final sentence: *"**Pass-through to owner** - pair with corresponding AR invoice … for 4C make-ready close-out"* — self-contradicting the opener, and the operative billing instruction |
| | The trim is **already** line 3 of 2026-534, labelled *"(QC correction, vendor pass-through)"*; prompt S12 asks that the invoice *"carr[y] the right figure"*, not that lines be added or removed |
| | The three genuinely in-house items (faucet cartridge, GFCI, drywall — bucketed as in-house by `recbd087a4abd605b` and by Slack ts …869.000001) carry **no AP bill at all**. "Our own time" generates no payout, so there is nothing to pass through; the existence of a vendor bill is itself evidence the work was not our own time |

**Ruling: this is NOT a prompt-level Unique Ground Truth failure. NO propagation.** The prompt supplies its own discriminator: S9's appositive names the Alamo item almost verbatim while describing nothing about the trim, and S8's "outside vendor work" test is satisfied by the Permian payee. Both pro-1727 cues are contradicted inside their own records — the bill note by its own final sentence, the "Tony did it" attributions by the belief email's explicit placement of the trim in Pete's vendor scope and by the fact that Tony is also the person Carlos routes *vendor* invoices to for processing (`a88bb5b7d1eb215b`: "Hi Tony, Please find attached my invoice … Kindly process"). 1727.00 is a rebuttable trap with a discoverable key, which is exactly what Hardness_Plan designed it to be — not an equally defensible end-state.

**But the OE must carry the rebuttal, and today it does not.** OE 17 quotes the PrivateNote starting from sentence 2. OE 19's four grounds never mention the "Internal labor charge" opener. OE 4 states the Airtable "routed to Tony Reyes" line but never reconciles it with OE 19's conclusion. OE 22/23 omit the Slack message entirely. S3 will therefore write the 1812.00 rubric from an OE that has never seen the strongest argument against it, and a PT dispute quoting one sentence from the graded record will have leverage the rubric author was never armed against.

**No `PROPAGATE TO S1` items are raised. Prompt-phase carry-forward (informational, non-blocking):** if S4 shows runs landing on 1727.00 *and citing the "Internal labor charge for Tony Reyes" sentence*, the REDO delta belongs at S1 — tighten S9 to name the excluded work by what it was (e.g. "our own walk-through and condition check before the vendors started") — **not** at the OE. Log this in `Tasks/_meta/Stump_Hypotheses.md` alongside prediction 3.

---

## [B8] OE Completeness semantic — forward and reverse maps

### Prompt decomposition (sentence by sentence)

| # | Prompt sentence (abbrev.) | Type |
|---|---|---|
| S1 | Closing out finished make-readies; want Mesa Vista 4C "fully closed on the owner side" | Goal |
| S2 | "Linda Castillo owns that unit" | Identity |
| S3 | Billed her in the spring + sent a summary naming deep clean / full repaint / closet trim touch-up | Context |
| S4 | "I moved on to the next unit and left it there" | Context |
| S5 | Verify "what she was actually charged holds up" — the summary is the record she keeps | **Explicit ask** |
| S6 | Straight pass-through: every dollar must match what we paid out, "to the dollar, no more and no less" | **Rule** |
| S7 | "Go back to what each vendor charged us … and set it against the line items I sent her" | **Explicit ask** |
| S8 | "Only outside vendor work belongs on her side" | **Scoping rule** |
| S9 | "Anything that was our own time … an internal walk or a condition check we handled in house, stays off her bill entirely" | **Exclusion rule** |
| S10 | If clean: log 4C closed, end of it | **Conditional branch** |
| S11 | "I do not want a second bill created next to the one she already has" | **Negative guard** |
| S12 | "Correct the invoice she is holding so it carries the right figure" | **WRITE 1** |
| S13 | "get our 4C make-ready record in Airtable updated so it shows the final owner cost and the unit fully closed" | **WRITE 2** |
| S14 | "email Linda a short note letting her know where it landed" | **WRITE 3** |
| S15 | "drop a line in our channel for the crew and front office … working off the corrected number" | **WRITE 4** |
| S16 | "I would sooner square this myself now than have Linda find the gap" | **Act-now, not defer** |

### FORWARD map — every prompt ask to its covering OE step

| Prompt ask | Covering OE(s) | Coverage |
|---|---|---|
| S1 close 4C on the owner side | OE 24, OE 25, OE 28 | Full |
| S2 Linda is the owner | OE 1, OE 9 | Full |
| S3 the invoice she holds | OE 10, OE 11 | Full |
| S3/S5 the summary she was sent | OE 7 | Full |
| S3 the three named scopes | OE 11 (lines 1-3), OE 14, OE 15, OE 17 | Full |
| S5 verify the charges hold up | OE 11 + OE 13-21 | Full |
| S6 dollar-exact match to payouts | OE 21 | Full |
| S7 what each vendor charged us | OE 13, 14, 15, 17, 18, 20 | Full |
| S7 set it against her line items | OE 11 + OE 21 | Full |
| S8 only outside vendor work | OE 19, OE 20 | Full |
| S9 exclude our own time / walk / condition check | OE 4, OE 18, OE 19 | Full (content complete; **rebuttal under-armed** — see B6) |
| S10 conditional close | OE 21 establishes not-clean; OE 25 closes | Full |
| S11 no second bill | OE 24 ("Do NOT call `create_invoice`") | Full |
| S12 **WRITE 1** correct the invoice in place | OE 24 — `update_invoice(id 445653930748, SyncToken "0", properties)`; lines 387 / 1340 / 85, TotalAmt 1812.00 | Full |
| S13 **WRITE 2** Airtable final cost + fully closed | OE 25 — `update_records_for_table(baseId appPropertyOps, tableId tblMakeReady, records[recc8534b3fd13954])`, fldTurnStatus selReady + fldNotes2 content; mechanism pre-resolved by OE 5 | Full |
| S14 **WRITE 3** email Linda | OE 26 — `create_draft(to ["linda.castillo@gmail.com"], subject, body, replyToMessageId "5101c5a41dffa90a")`; draft-only noted | Full |
| S15 **WRITE 4** channel post for crew + front office | OE 27 — `slack_send_message(channel_id "C004", message)`; C004 verified to reach crew (Tony/John/Jaime) and Brooke Phillips; C005/C006 pre-authorised | Full |
| S16 act now, do not defer | All four writes; OE 12 grounds amend-over-credit | Full |

**`OE_INCOMPLETE`: none.** All four required write actions carry tool + key params + expected content, and the negative guard is present and explicit.

### REVERSE map — every OE step to the ask it serves

| OE | Serves | Note |
|---|---|---|
| 1 | S2, S14 | identity + recipient binding |
| 2 | S13 | identifier binding for the Airtable write |
| 3 | S13 | pins the live row (L1 latch) |
| 4 | S9 | separates in-house scope from vendor scope |
| 5 | S13 | write mechanism — no cost field, no "Closed" option |
| 6 | S1, S5 | corroborates "actually finished"; explicitly notes it carries no cost figures |
| 7 | S3, S5, S14 | the summary under test |
| 8 | S7, S8 | vendor-scope trail; establishes that no email carries an amount (feeds L2) |
| 9 | S2 | customer resolution + Pete near-miss |
| 10 | S3, S12 | locates the invoice; decoy exclusion |
| 11 | S7 | the claim under test |
| 12 | S11, S12 | unpaid, so amend rather than credit/re-issue |
| 13-18 | S7, S8, S9 | the payout side |
| 19 | S8, S9 | the pivotal discrimination |
| 20 | S8 | payee identity does not settle billability |
| 21 | S6 | the derived figure + decoy figures |
| 22-23 | S15 | channel-of-record discovery |
| 24 | S12, S11 | WRITE 1 + negative guard |
| 25 | S13 | WRITE 2 |
| 26 | S14 | WRITE 3 |
| 27 | S15 | WRITE 4 |
| 28 | S5, S16 | load-bearing facts for the final reply |

**`SCOPE_CREEP`: none.** OE 6, 8, 16, 20 and 23 are corroborative rather than strictly necessary, but each serves a named prompt ask and each states its own evidentiary limit, so none exceeds the prompt. **S3 warning:** these five are corroborative-only — converting any of them into a Process rubric would be execution-trace over-specification and would fail condition (3) of the three-condition test.

### S3 rubric-mapping preview

| Bucket | OE steps | What the rubric asserts |
|---|---|---|
| **Outcome 1.1** — write action result | **24** · **25** · **26** · **27** | invoice 2026-534 amended in place and no second owner invoice exists; the live 4C `tblMakeReady` row updated; a draft to Linda exists (never sent); a channel post exists |
| **Outcome 1.2** — write content | **24** (lines 387.00 / 1340.00 / 85.00, TotalAmt 1812.00) · **25** (fldNotes2 carries 1812.00 + component breakdown + the internal-walk exclusion + the closed state; fldTurnStatus held at selReady) · **26** (corrected to 1812.00; repaint 1340.00 not 1140.00; trim 85.00 not 95.00; net 190.00 more; internal walk not passed through; no second invoice) · **27** (1812.00 supersedes 1622.00, per-bill attribution PD-2026-09 / 2026-519, internal walk excluded) |
| **Outcome 2.1** — tell-me facts in the reply | **21** + **28** | 1812.00 corrected total; 200.00 understated on the repaint, 10.00 overstated on the trim, net 190.00; the 85.00 internal condition walk stays off her bill; amended not duplicated; Linda is the owner, Pete is the painter |
| **Process candidates (recommend NONE)** | 12 (unpaid-before-amending), 13+15+17 (AP re-derivation), 3+4 (live vs stale row) | Each is fully captured by a tightened Outcome — the exact 1812.00 with its 1340.00 / 85.00 components, and "amended in place, no second invoice". Writing Process rubrics here would fail condition (2) |
| **Pure discovery, no rubric** | 2, 5, 6, 8, 9, 16, 20, 22, 23 | identifier binding, schema, corroboration, channel discovery |

**Two S3 guard-rails from this review:** (1) do **not** id-lock the invoice rubric to `update_invoice` on 445653930748 — grade the end-state (alt-path E); (2) the 1812.00 Outcome 2.1 rubric should require the *reasoning that excludes the internal walk while keeping the trim*, so a 1727.00 answer fails on substance rather than on a bare number match.

---

## [B9] OE Service Mapping

Checked against `Validators/universes.py` starpm `oe_service_map` (`make_ready`/`turns`/`maintenance_tickets` -> airtable; `rent_invoices`/`vendor_bills` -> quickbooks; `leasing_deals` -> hubspot; `tickets`/`issues` -> linear; `email_threads`/`drafts` -> gmail; `chat`/`channels` -> slack; `contacts` -> contacts).

| OE | Data type | Tool | Server | Correct service |
|---|---|---|---|---|
| 1 | contacts | `contacts_search_contacts`, `contacts_get_contact` | contacts | YES |
| 2 | Airtable structure | `list_bases`, `list_tables_for_base` | airtable | YES |
| 3 | make-ready turns | `search_records` | airtable | YES — **not** Linear |
| 4 | make-ready turns | `list_records_for_table` | airtable | YES |
| 5 | table schema | `get_table_schema` | airtable | YES |
| 6 | maintenance tickets | `search_records` (tblMaintenanceTickets) | airtable | YES — Airtable is system of record (`tblMaintenanceTickets.description`: "Linear is secondary"); a Linear step here would have been a mismatch |
| 7-8 | email threads | `search_threads`, `get_thread` | gmail | YES |
| 9 | customers | `search_customers` | quickbooks | YES |
| 10-11 | invoices | `search_invoices`, `read_invoice` | quickbooks | YES |
| 12 | receivables reports | `get_aged_receivables`, `get_customer_balance` | quickbooks | YES |
| 13-18 | vendor bills | `search_bills`, `get-bill` | quickbooks | YES |
| 20 | vendors | `search_vendors` | quickbooks | YES |
| 21 | vendor expenses | `get_vendor_expenses` | quickbooks | YES |
| 22-23 | chat | `slack_search_public_and_private`, `slack_read_channel` | slack | YES |
| 24 | invoice write | `update_invoice` | quickbooks | YES |
| 25 | make-ready write | `update_records_for_table` | airtable | YES |
| 26 | draft | `create_draft` | gmail | YES (draft-only correctly noted; no send tool exists) |
| 27 | chat write | `slack_send_message` | slack | YES |

**`OE_SERVICE_MISMATCH`: none.** HubSpot and GCalendar are unused and correctly so — the prompt asks nothing about owner deals or scheduling. Linda also exists as a HubSpot contact, an equivalent identity surface OE 1 does not foreclose.

---

## Phase 4.0 mandatory pre-verdict sweep (`Evals_starpm/2_OE_Eval.md`)

| # | Check | Finding |
|---|---|---|
| 1 | **Any OE with a wrong count** | **FLAG (Minor).** All stated counts are right — 2 4C rows, 4 bills at Unit 4C, 10 bills at 1340.00 (all ten ids verified), 3 invoice lines, 3 status choices, 6 messages in C005. But OE 22/23's enumeration of the C004 4C trail is **incomplete**: five Carlos messages listed, ts `1779501872.000004` from Jaime Salinas omitted, and OE 22's "all from Carlos Mendez (U07E4512181)" is therefore true only of the subset it lists |
| 2 | **Any OE referencing a non-existent tool or a tool from another service** | **PASS.** All 25 distinct tool names exist on the named server; every parameter name verified, including the traps (`search_records.table` not tableId, `get_table_schema.tables`, `update_invoice.SyncToken`, `create_draft.body` not content, `slack_send_message.message` not payload/text, hyphenated `get-bill`) |
| 3 | **Any required write action with no covering OE** | **PASS.** 4 writes -> OE 24 / 25 / 26 / 27, each with tool + key params + expected content; negative guard explicit in OE 24 |
| 4 | **Any act-vs-defer conflict** | **PASS.** Scanned every accessible Slack channel and Carlos's full mailbox for hold/defer/accept-timing language tied to 4C, Linda, Mesa Vista, or owner billing — **zero hits**. The only "on hold" text in the ledger (invoice 618793969708) is a different property and customer. Prompt S16 affirmatively instructs acting now |

---

## Issue list (severity-tagged)

| # | Sev | OE | Issue | Evidence | Fix |
|---|---|---|---|---|---|
| 1 | **MAJOR** | 17, 19 | OE 17 quotes bill 546359391323's PrivateNote from sentence 2, omitting *"Internal labor charge for Tony Reyes touch-up on Mesa Vista 4C closet trim."* — the single strongest cue for the competing 1727.00 end-state. OE 19's four grounds never rebut it, and its ground #2 ("the instruction on each record") is undercut because **both** 85.00 bills open with the identical *"Internal labor charge for <@starpm.com person>"* template. The phrase occurs on exactly 2 of 625 ledger entities, so it is high-signal, not noise | `quickbooks.quickbooks_entities.json` :: 546359391323 + 991582431419 PrivateNote | Quote the PrivateNote **in full** in OE 17. Add a fifth ground to OE 19: the trim's payee is Permian Make-Ready Crew (204), an outside vendor we actually paid; the same note's operative instruction is "Pass-through to owner"; the belief email places the trim inside Pete Donovan's vendor repaint scope while bucketing Tony's work separately as in-house; and the genuinely in-house items (faucet / GFCI / drywall) carry no AP bill at all, so "our own time" produces no payout to pass through |
| 2 | MINOR | 22, 23 | The C004 4C trail omits ts `1779501872.000004` from **Jaime Salinas** (U2CD1BC03B2): *"Jaime flagged a paint touch-up on the bedroom closet trim. Tony got it done today, Airtable updated."* It sits between two listed ts values and carries a third "Tony did it" attribution. OE 22's "all from Carlos Mendez" is scoped only to its own list | `slack.slack_messages.json`, `slack.slack_users.json` | Add the message to OE 22's enumeration, attribute it to Jaime Salinas, and note in OE 19 that it is coordination/routing language rather than evidence of in-house billing |
| 3 | MINOR | 8 | The four ids listed as `search_threads` discoveries are **message** ids. The real thread ids are `525641a76c00fbe0`, `c138c134b23d60d3`, `83872812663ee5c9`, `f43fdaee4372a09b`. OE 7 gets this distinction right, so the OE is internally inconsistent, and `get_thread(threadId="e845219255a2bdb4")` would fail | `gmail.gmail_threads.json` vs `gmail.gmail_messages.json` | List the thread ids, keeping message ids parenthetically as OE 7 does |
| 4 | MINOR | 22 | *"the summary email claims confirmation was posted 'in the vendors channel'"* — that claim is in message **13385eee8206db79** (Carlos to Brooke, "Pete Donovan Painting Invoice Received and Entered"), not in the summary email 5101c5a41dffa90a, whose body never mentions a channel | `gmail.gmail_messages.json` | Re-attribute to 13385eee8206db79 (already discovered at OE 8) |
| 5 | MINOR | 19 | Pure-reasoning step with no tool call, against the Phase 1.2 anti-pattern and against the reference corpus (all four QC_Passed V4 OEs have a tool-like token in every step). OE 28 is exempt — it is the "key facts the user asked to be told" type that feeds Outcome 2.1; OE 21 is borderline but carries an optional `get_vendor_expenses` | `Evals_starpm/2_OE_Eval.md` Phase 1.2; `QC_Tasks/V4_Tasks/QC_Passed/*/6_Oracle_Events.txt` | Fold OE 19's grounds into OE 17/18 as their conclusions, or re-anchor OE 19 on a tool (e.g. `search_bills` filtered to the two 85.00 bills, or `get-bill` re-reads) |
| 6 | NIT | 6 | Query `"Mesa Vista 4C"` matches reca424761ae15355 but **not** rec12969a3fdb0852, whose text reads "unit 4C at Mesa Vista". Under substring search the intake ticket would not return | `airtable.airtable_records.json` | Offer `"4C"` or `"Mesa Vista"` as the alternative query |
| 7 | NIT | 16 | Query `"1340"` will not match on TotalAmt (no description contains it). The OE already hedges with `max_results: 50` + inspect TotalAmt, so the step is workable | tool catalog + ledger | Lead with the `max_results` variant |
| 8 | NIT | 20 | Phrased as though `search_vendors` reveals Tony Reyes and Jaime Salinas to be internal staff; they are not vendor records at all — their **absence** from the vendor list is the discovery | ledger (8 vendors, none internal) | Reword to "neither appears in the vendor list" |
| 9 | NIT | 24 | Forecloses `create_invoice` but not a credit memo. Structurally moot (the correction raises 1622.00 to 1812.00; a credit memo only reduces AR) | ledger — no 4C credit memo | Optional: add "and do not raise a credit memo" |
| 10 | INFO | B3 | Prompt S10 makes three of the four writes conditional, so a stumped model takes the one-write branch and sheds ~4-5 calls. Hardness_Plan `## THIN density acceptance` item 2 ("writes execute on BOTH models") does not hold for stumped runs; modal Gemini is ~28, not ~34 | `5_Prompt.txt` S10; Hardness_Plan line 99 | Carry to S4: Gemini < 30 is expected, not anomalous; actionable threshold is < 24 |
| 11 | INFO | B4 | Hardness_Plan's breadth table claims 6 services (incl. linear ~7%, hubspot); the OE realizes 5 and is **right** to — maintenance tickets map to Airtable with Linear as secondary, so a Linear step would have been an `OE_SERVICE_MISMATCH`. The operative Hardness Brief target ("4-write / 5-service OE") is met | `Validators/universes.py` `oe_service_map` | No OE change; correct the Hardness_Plan breadth table if it is re-cited downstream |

**`PROPAGATE TO S1`: none.** See B6 — 1727.00 is a rebuttable trap, foreclosed by prompt S8's "outside vendor work" test and S9's naming of *a walk* and *a condition check*, reinforced by the belief email's placement of the trim inside Pete Donovan's vendor scope. Informational carry-forward only: if S4 shows runs landing on 1727.00 while citing the "Internal labor charge for Tony Reyes" sentence, the REDO delta belongs at S1 (tighten S9's exclusion wording), not at the OE.

---

## Round-1 verdict rationale

The chain is solvable, correctly serviced, tool-accurate, fully write-covered, and every lever including the L1 reserve is exercised. Density passes on Opus and is documented-THIN on Gemini. One issue blocks: the OE decides the task's pivotal question — which of two identical 85.00 charges is owner-billable — while omitting the one sentence in the graded record that argues the other way, and omitting two further records that reinforce it. That is a cheap fix (Issue 1, plus Issues 2-5 in the same pass) and it must land before S3 writes the 1812.00 rubric from an under-armed OE.

Re-run Council B after the fix; Issues 1-5 resolved lifts OE Accuracy to 5/5 and clears this to GO.

**ROUND-1 VERDICT: BLOCK** (superseded by round 2 below)

---
---

# ROUND 2 — re-review of the revised `6_Oracle_Events.txt`

File re-read fresh (28 steps, no em-dash, validator re-run: **PASS, 0 fails / 0 warns / 3 notes**). Every changed and newly added claim was re-verified independently against `_aux/Universe_Split/` — I did not accept the coordinator's change list on trust.

## Round-2 verification of the fixes

| Fix | Claim in revised OE | Independent verification | Result |
|---|---|---|---|
| **Issue 1a** | OE 17 quotes bill 546359391323's PrivateNote **in full** | Byte-for-byte string containment test against `quickbooks.quickbooks_entities.json` PrivateNote | **VERBATIM MATCH** |
| **Issue 1b** | OE 17: Balance 85.00, AccountRef "Owner Reserve (Trust)" (64) | ledger: `Balance 85.0`, `AccountRef {"name":"Owner Reserve (Trust)","value":"64"}` | **EXACT** |
| **Issue 1c** | OE 18: Balance 85.00, AccountRef "Supplies" (61); both 85.00 bills open with the same "Internal labor charge for" template so the phrase discriminates nothing | ledger: `Balance 85.0`, `AccountRef {"name":"Supplies","value":"61"}`; phrase present on both and on **only** these 2 of 625 entities | **EXACT** |
| **Issue 1d — ground 2** | The genuinely in-house 4C work (faucet cartridge, GFCI, drywall) produced **no AP bill at all**; both 85.00 records are real payouts with an open balance | Only 4 bills touch Unit 4C; none covers faucet/GFCI/drywall; both 85.00 bills carry `Balance 85.0` (unpaid, no bill_payment rows exist anywhere) | **CORRECT** |
| **Issue 1e — ground 4 (new)** | 2026-519 posts to Owner Reserve (Trust) 64, "the owner's own funds", and is **the only one of the four 4C bills coded there**; 2026-481-566 posts to Supplies 61, "a StarPM operating account" | Four-bill coding: 195089456477 → 62 Contract Labor · 696089964235 → 63 Management Fee Income · **546359391323 → 64 Owner Reserve (Trust)** · 991582431419 → 61 Supplies. Account master: 64 is `AccountType "Bank"`, `AccountSubType "TrustAccounts"`, CurrentBalance 70624.57; 61 is `AccountType "Expense"` | **CORRECT, and stronger than the OE claims** — 64 is a trust *bank* account, so "the owner's own funds" is literal, not interpretive |
| **Issue 1f** | Counter-evidence stated and answered: bill opening phrase, Airtable `recc8534b3fd13954` "routed to Tony Reyes and resolved same day", Slack C004 ts `1779501872.000004` "Tony got it done today" | All three present and quoted accurately | **CORRECT** — the round-1 Major is fully discharged |
| **Issue 1g** | Summary email demoted to corroboration only | OE 19 now states the email "points the same way but is corroboration only, since OE 7 already showed that email is unreliable on details" | **RESOLVED** — the self-undermining dependency (OE 7 calls the email unreliable, then OE 19 leaned on it) is gone |
| **Issue 2** | OE 22/23 enumerate **six** C004 messages, Jaime Salinas post at ts `1779501872.000004` attributed to U2CD1BC03B2 | All six ts values, all five Carlos attributions, the Jaime attribution and the quoted substring "Tony got it done today, Airtable updated" verified against `slack.slack_messages.json` + `slack.slack_users.json` | **EXACT** |
| **Issue 3** | OE 8 lists thread ids with message ids parenthetically | 525641a76c00fbe0←e845219255a2bdb4 · c138c134b23d60d3←ab11ac615e2563f8 · 83872812663ee5c9←a88bb5b7d1eb215b · f43fdaee4372a09b←13385eee8206db79 | **ALL FOUR CORRECT** |
| **Issue 4** | "posted confirmation in the vendors channel" re-attributed to 13385eee8206db79 (OE 8 and OE 22) | Exact phrase confirmed in that message body; absent from 5101c5a41dffa90a | **CORRECT** |
| **Issue 5** | OE 19 anchored on `get-bill` re-reads of both 85.00 ids | Present; **no pure-reasoning step remains** in the OE list | **RESOLVED** |
| **Nit 6** | OE 6 query widened to "4C" or "Mesa Vista"; a narrow "Mesa Vista 4C" returns only the completion record because the intake reads "unit 4C at Mesa Vista" | Simulated against the 50 `tblMaintenanceTickets` rows: `"Mesa Vista 4C"` → 1 hit (reca424761ae15355); `"4C"` → **exactly the 2 rows the OE lists**; `"Mesa Vista"` → 3 | **CORRECT** (one residual nit, below) |
| **Nit 7** | OE 16 leads with `max_results: 50`; a "1340" query will not match on amount | No description text contains "1340"; ten-bill cluster ids all still exact | **CORRECT** |
| **Nit 8** | OE 20: master of only eight vendors; neither Tony Reyes nor Jaime Salinas appears in it | Vendor entity count = **8**; zero Reyes/Salinas vendor records | **CORRECT** |
| **Nit 9** | OE 24 also forecloses a credit memo | Present | **RESOLVED** |
| **New — OE 3** | Date-field inversion: the stale row carries the **later** fldMoveOut/fldTargetReady, so sorting on date fields picks the wrong row | recc8534b3fd13954 (live, mod 2026-05-29): 2026-06-01 / 2026-06-14. recbd087a4abd605b (stale, mod 2026-05-22): **2026-06-15 / 2026-06-30** | **CORRECT** — genuine, previously undocumented trap; a real L1/L6 reinforcement |
| **New — OE 14** | Full PrivateNote for 195089456477 + AccountRef "Contract Labor" (62) | Byte-for-byte containment test | **VERBATIM MATCH** |

## Round-2 [B1] sub-dim re-score

```
SUB-DIM OE Completeness -> SCORE 5/5 -> REASON Forward map still has zero gaps and all four writes retain tool + key params + expected content plus the negative guard, now also foreclosing a credit memo; the last structural blemish is gone because OE 19 is tool-anchored on get-bill re-reads rather than pure reasoning, and the counter-evidence discovery is now complete with the sixth C004 message enumerated.
SUB-DIM OE Accuracy -> SCORE 5/5 -> REASON All four round-1 imprecisions are fixed and re-verified byte-for-byte, and every newly added claim checks out exact against the ledger: both full PrivateNotes verbatim, AccountRef 62/63/64/61 across the four 4C bills with 546359391323 the only one coded to trust account 64, Balance 85.00 on both 85.00 bills, the eight-vendor master with no Tony or Jaime, four correct thread ids, six C004 messages with correct per-message attribution, and the OE 3 date-field inversion. Nothing remaining is a wrong tool, service, parameter or expected value.
```

Both sub-dims are now at the bar of 5. Three residual **NIT**-level items are logged below; none is a factual imprecision and none blocks.

## Round-2 [B3] density re-run

The revision added roughly 700 words of grounding and **two** firm new tool calls (the `get-bill` re-reads in OE 19), plus a soft one (OE 6's narrow-then-widen pattern, which the OE now describes explicitly).

| Model | Round 1 | **Round 2** | Delta | Band |
|---|---:|---:|---|---|
| **Opus 4.8** | 44 (36-52) | **46** (37-54) | +2 firm (OE 19 re-reads) +0-1 soft (OE 6) | **PASS** (>= 40), now further clear of the line |
| **Gemini** (solved branch) | 34 (26-40) | **35** (30-40) | +0-1 — Gemini economises exactly on re-reads it already holds in context | **THIN_DENSITY** (15-39), unchanged, accepted per Hardness_Plan `## THIN density acceptance` |
| **Gemini** (stumped branch) | ~28 | **~29** | +1 | THIN, unchanged, far above the 15 floor |

**Bands do not move.** The grounding expansion was prose, not trajectory, which is the right way to fix an under-armed OE — it hardens rubric defensibility without inflating density.

### Service breadth (against the 46-call Opus sketch)

| Service | R1 calls | **R2 calls** | R2 share |
|---|---:|---:|---:|
| quickbooks | 20 | **22** | 47.8% |
| airtable | 9 | **10** | 21.7% |
| gmail | 8 | 8 | 17.4% |
| slack | 4 | 4 | 8.7% |
| contacts | 3 | 3 | 6.5% |
| **Distinct** | 5 | **5** | dominant 47.8% **< 60%**, all >= 5% |

**Breadth: PASS.** Both new calls are QuickBooks, so its share ticks 45.5% → 47.8% — still comfortably inside the ceiling.

## Round-2 [B4] lever re-check — L6 and L11 now strengthened

| Lever | R1 | **R2** | What changed |
|---|---|---|---|
| **L2** flagship | PRESERVED | **PRESERVED** | Unchanged. OE 13/15/17/21 intact; 1812.00 still appears zero times as a figure anywhere in the universe |
| **L10** supersession | PRESERVED | **PRESERVED** | Unchanged, plus OE 3's date inversion adds a second supersession surface (modification order supersedes date-field order) |
| **L6** near-miss | PRESERVED | **STRENGTHENED** | The twin-85 near-miss is now fully armed: OE 17 and OE 18 both surface the shared "Internal labor charge for" template and OE 19 ground 1 names it as a non-discriminator present on only 2 of 625 records. OE 3's date-field inversion is a **new** near-miss surface — an agent sorting on fldMoveOut/fldTargetReady picks the stale row |
| **L11 / L9** net-vs-gross | PRESERVED **but WEAKENED** | **STRENGTHENED / ARMED** | The round-1 weakness is gone. OE 19 now runs five grounds, one of which (account coding: trust bank account 64 versus operating expense 61, with 2026-519 the only 4C bill coded to 64) is a hard ledger fact independent of any free-text note, and the three-record counter-evidence cluster is stated and answered rather than hidden. A 1727.00 PT dispute now has to defeat a documented five-ground argument instead of exploiting an omission |
| **L1** latching reserve | PRESERVED | **STRENGTHENED** | OE 3's date inversion gives the latch a second, sharper edge |

**`HARDNESS_REGRESSION`: none.** 4/4 selected levers plus the L1 reserve, with L6, L11 and L1 measurably harder than at round 1.

## Round-2 [B8] forward / reverse re-check — no scope creep

**Forward map: unchanged, zero gaps.** No prompt ask lost coverage. The negative guard strengthened (OE 24 now forecloses `create_invoice` **and** a credit memo, closing round-1 alt-path D explicitly).

**Reverse map: no `SCOPE_CREEP`.** Every addition is grounding for an ask the prompt already makes:

| Addition | Serves | Beyond the prompt? |
|---|---|---|
| OE 3 date-field inversion | S13 (pin the right make-ready row) | No |
| OE 14 full PrivateNote + AccountRef 62 | S7 (what each vendor charged), S2 (Pete decoy) | No |
| OE 17 full PrivateNote + Balance + AccountRef 64 | S8/S9 (outside vendor work vs our own time) | No |
| OE 18 AccountRef 61 + shared-template note | S9 (the exclusion) | No |
| OE 19 five grounds + counter-evidence | S8/S9 (the pivotal exclusion) | No |
| OE 20 eight-vendor master | S8 (only outside vendor work) | No |
| OE 22/23 sixth C004 message | S15 (channel of record) + S9 (counter-evidence) | No |
| OE 24 credit-memo foreclosure | S11 (no second bill) | No |

No new write action, no new ask, no new entity outside the 4C scope. **`OE_INCOMPLETE`: none. `SCOPE_CREEP`: none.**

The S3 rubric-mapping preview from round 1 stands unchanged, with one addition: OE 19's five grounds are now rich enough that the **Outcome 2.1** rubric can require the *reasoning* that keeps the trim while excluding the walk (work kind + account coding + no-bill-for-in-house-work), so a 1727.00 answer fails on substance rather than on a bare number mismatch. Still recommend **no Process rubrics** — all three candidates remain captured by tightened Outcomes.

## Round-2 Phase 4.0 sweep

| # | Check | Round 1 | **Round 2** |
|---|---|---|---|
| 1 | **Any OE with a wrong count** | FLAG (C004 trail enumerated as 5, sixth message omitted) | **PASS.** Six C004 messages enumerated with correct per-message attribution; eight-vendor master verified = 8; four bills at Unit 4C; ten bills at 1340.00; two 4C make-ready rows; three status choices; three invoice lines; six C005 messages. Every stated count matches the universe |
| 2 | **Any non-existent or wrong-service tool** | PASS | **PASS.** No new tools introduced; the OE 19 `get-bill` re-reads use the correct hyphenated catalog name; all parameters re-verified |
| 3 | **Any required write action with no covering OE** | PASS | **PASS.** Four writes → OE 24/25/26/27, each with tool + key params + expected content; negative guard now covers both a second invoice and a credit memo |
| 4 | **Any act-vs-defer conflict** | PASS | **PASS.** Unchanged — zero hold/defer/accept-timing hits across all Slack channels and Carlos's full mailbox for 4C, Linda, Mesa Vista or owner billing |

## Round-2 residual issues

| # | Sev | OE | Issue | Fix |
|---|---|---|---|---|
| R2-1 | NIT | 19 | Garbled clause in ground 2: *"so our own time on this unit generated no payout there is anything to pass through"* — words are missing. OE 19 is the step S3 will read most closely, so the copy defect matters more here than elsewhere | Reword to "…generated no payout, so there is nothing there to pass through" |
| R2-2 | NIT | 6 | The `"Mesa Vista"` alternative query returns **three** `tblMaintenanceTickets` rows — the two listed plus unrelated pool-pump ticket `rec860db6b493af1e5b` (MT-2026-1326). The `"4C"` alternative returns exactly the two listed rows | Prefer `"4C"`, or add "the broader Mesa Vista query also returns the unrelated pool pump ticket rec860db6b493af1e5b, which is out of scope" |
| R2-3 | NIT | 20 | The eight-vendor master size and the Tony/Jaime absence are both true, but they do not follow from the stated targeted query for three named vendors | Add "or `search_vendors` with no query to see the full master of eight" |
| R2-4 | INFO | 19 | Ground 4 is correctly scoped as between the two 85.00 charges, but a rubric writer could over-generalise it into "owner-billable items post to account 64" — which the other two owner-billable 4C bills (62 Contract Labor, 63 Management Fee Income) would fail | S3 note only: keep account coding as a twin-85 tiebreaker, never as a general billability test |

**`PROPAGATE TO S1`: none** (round-1 B6 adjudication stands: 1727.00 is a rebuttable trap foreclosed by prompt S8's "outside vendor work" test and S9's naming of *a walk* and *a condition check*, and the OE now carries the full rebuttal). The informational S4 carry-forwards from round 1 remain: Gemini < 30 is expected not anomalous (actionable at < 24), and a 1727.00 sweep citing the "Internal labor charge" sentence would put the REDO delta at S1's exclusion wording, not at the OE.

## Round-2 verdict rationale

The round-1 Major is fully discharged, and discharged well: the OE no longer hides its strongest counter-evidence, it states all three "Tony did it" records and answers them, and it replaces a note-quoting argument with a five-ground argument anchored on a hard ledger fact (trust account 64 versus operating account 61) that I verified independently and found *stronger* than the OE claims — account 64 is literally a trust bank account holding 70,624.57 of owner funds. All four round-1 accuracy imprecisions are fixed and re-verified byte-for-byte. The last structural blemish is gone. Both sub-dims sit at 5. Density bands are unchanged with Opus further clear of the 40 line, breadth still passes, all four levers plus the reserve are preserved with L6, L11 and L1 strengthened, no scope creep entered with the new text, and all four Phase 4.0 sweep items now pass. The four residual items are copy polish and query-breadth phrasing — worth folding in on the next touch, none of them a reason to hold S3.

VERDICT: GO
