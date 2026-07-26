# FINAL CROSS-ARTIFACT COUNCIL — Task 43_6a62ccaf5853030245ac9d53

**Universe:** StarPM V4 (dual-model: 6x Opus 4.8 + 6x Gemini) · **Persona:** Carlos Mendez (`carlos.mendez@starpm.com`, Onsite Property Manager, p_009) · **Business Function:** Property Operations · **Today in-universe:** 2026-07-01 America/Chicago.
**Scope:** last cross-artifact gate before platform upload. Read `5_Prompt.txt` + `6_Oracle_Events.txt` + `7_Rubrics.json` + `_aux/Hardness_Plan.md` + `_aux/Fact_Ledger.json` + `_aux/Universe_Split/` TOGETHER. Every tight identifier, every derived figure, and every tool-parameter binding was **independently re-derived from source** (python3 over `_aux/Universe_Split/*.json` and `StarPM_Base_Universe/7_Server_Tools_Details.json`). Prior-phase councils were **not** trusted.
**State of downstream files:** `8a_Verifier_Fails_Opus.txt`, `8b_Verifier_Fails_Gemini.txt`, `9_QC_Feedback.txt`, PT-dispute/final-QC files, and all 12 `Agent_Responses/{Opus,Gemini}/RunN_Trajectory.json` are **0 bytes** → task not yet run. Density is therefore a **projection**, as expected at this stage. `4_Changelog.json` is `[]` and `9_Universe_inject.sql` carries no statements → confirmed **no-injection task**, consistent with `Hardness_Plan.md`.

**Ground truth independently confirmed:** `387.00` (bill `195089456477`, Doc `2026-SC-4C`, Sunshine Cleaning) + `1340.00` (bill `696089964235`, Doc `PD-2026-09`, Permian Make-Ready Crew) + `85.00` (bill `546359391323`, Doc `2026-519`, Permian) = **1812.00**. Invoice `445653930748` (Doc `2026-534`, Linda Castillo `proj-4ae920b7c9e8`) carries lines `387.00` / `1140.00` / `95.00`, TotalAmt `1622.00`, Balance `1622.00`, sync_token `"0"`. Net delta `190.00` = `200.00` under (repaint) less `10.00` over (trim). Decoys recompute exactly: `1897.00` = +`85.00` Alamo walk (`991582431419`); `1727.00` = drop the trim; `1810.00` = substitute the `385.00` Rio Bend deep clean (invoice `310712648304`, Doc `2547`).

---

## LENS 1 — Truthfulness (identifier grounding, derived-figure recomputability, answer leakage)

**PASS — zero phantom identifiers, zero answer leakage.**

### Identifiers verified against `_aux/Universe_Split/` (source file named per item)

`quickbooks.quickbooks_entities.json` (625 rows; 113 bills, 155 invoices):
- Bill `195089456477` · Doc `2026-SC-4C` · TotalAmt/Balance `387.00` · VendorRef Sunshine Cleaning `proj-d016366b403c` · AccountRef **Contract Labor (62)** · PrivateNote ends "...paired receivable invoice to be issued to **Pete Donovan** for same scope and unit." ✔ (matches OE 14 verbatim)
- Bill `696089964235` · Doc `PD-2026-09` · TotalAmt/Balance `1340.00` · VendorRef Permian Make-Ready Crew `204` · AccountRef **Management Fee Income (63)** · line "Interior repaint, full unit - Mesa Vista Apartments Unit 4C..." ✔
- Bill `546359391323` · Doc `2026-519` · TotalAmt/Balance `85.00` · VendorRef Permian `204` · AccountRef **Owner Reserve (Trust) (64)** — account type `Bank` / subtype `TrustAccounts`, confirmed the only trust-coded account in the ledger ✔ · PrivateNote opens "Internal labor charge for Tony Reyes..." and closes "Pass-through to owner - pair with corresponding AR invoice to **Pete Donovan's** owner account..." ✔
- Bill `991582431419` · Doc `2026-481-566` · TotalAmt/Balance `85.00` · VendorRef Alamo HVAC Services `200` · AccountRef **Supplies (61)** · line "Unit condition inspection and punch list documentation - Mesa Vista Unit 4C, vacated turnover..." · PrivateNote "Internal labor charge for Carlos Mendez's make-ready walk..." ✔
- Invoice `445653930748` / Doc `2026-534` — all three lines, TotalAmt, Balance, sync_token, PrivateNote, CustomerMemo verified verbatim ✔
- Decoys `340207319849` (Doc `2026-AP-0184`, `1340.00`, Linda Castillo, "412 Mesquite, **Tommy Reyes** unit"), `310712648304` (Doc `2547`, `385.00`, Linda Castillo, Rio Bend A Plus deep-clean), `240572546619` (`2026-STD-042`, `3780.00`, Pete Donovan), `618793969708` (`2026-419`, `805.00` with a `190.00` service-call line, Pete Donovan), `328611897179` (`INC-2026-041`, `185.00`, Pete Donovan), `173322471681` (`INV-2026-0417`, `1140.00`, Hill Country Plumbing, **also AccountRef 63** — OE 16's "same account code" claim confirmed) ✔
- **OE 16's ten-bill `1340.00` cluster verified exactly** — programmatic filter `entity_type==bill and TotalAmt==1340.0` returns exactly the ten ids OE 16 lists, with the vendors and property descriptions OE 16 assigns to each. The three A Plus bills map to vendor `proj-a989f559245a` ("A Plus Carpet Cleaning & Repairs") ✔
- **OE 13's "exactly four bills reference Unit 4C" verified** ✔ · the only receivable naming Unit 4C is `2026-534` (the three other invoices containing the string "4C" are `14C` substrings: `167610388277`, `336966753058`, `933333877782`) ✔
- **Doc `2026-537` does not exist** in the 625-row entity set ✔ (OE 7/10 and rubric 9's trap confirmed)
- Payment `931951074454` · `510.00` · `LinkedTxn: [{TxnId: 247748966591, TxnType: Invoice}]` · invoice `247748966591` = Doc `INV-2026-0214`, `510.00`, Linda Castillo ✔ — **nothing is applied against `445653930748`**, so amend-in-place is the correct instrument (OE 12/24) ✔
- Vendor master holds **exactly 8** vendors; **neither Tony Reyes nor Jaime Salinas is a vendor** ✔ (OE 20)
- OE 21's `get_vendor_expenses` corroboration: Permian bills with TxnDate in `2026-05-01..2026-05-31` = **12 bills totalling 6992.00**, including the second `1340.00` (`102111031436`, grounds maintenance 4821 Oleander Dr) and the two other paint touch-ups (`167365280749` Cascade Hills 7C `610.00`, `358082173277` Elm Street `310.00`) ✔ — exact match

`airtable.airtable_records.json` / `airtable_tables.json` / `airtable_fields.json` / `airtable_bases.json`:
- Base `appPropertyOps` ("Property Operations"), tables `tblMakeReady` ("Make-Ready Turns") and `tblMaintenanceTickets` ("Maintenance Tickets") ✔
- `recc8534b3fd13954` — fldUnit "Mesa Vista 4C", fldTurnStatus `selReady`, fldMoveOut `2026-06-01`, fldTargetReady `2026-06-14`, last_modified `2026-05-29 14:26:59.557207`, fldNotes2 "QC walkthrough completed by Jaime Salinas - bedroom closet trim flagged for paint touch-up. Touch-up routed to Tony Reyes and resolved same day. Unit confirmed ready for leasing." ✔
- `recbd087a4abd605b` — `selProg`, fldMoveOut `2026-06-15`, fldTargetReady `2026-06-30`, last_modified `2026-05-22 21:14:34.331831`, fldNotes2 "...Deep clean and interior repaint still tracking..." and "...coordinated in **#maintenance**..." ✔
- **OE 3's date-inversion trap confirmed:** the STALE row carries the LATER fldMoveOut and fldTargetReady, so a sort on either date field selects the wrong row ✔
- Exactly two `tblMakeReady` rows for Mesa Vista 4C (out of 120 rows) ✔; siblings 107A/207A/310C exist and are out of scope ✔
- `reca424761ae15355` (MR-4C-2026-08, `selHigh`, fldCompletionDate `2026-05-01`) and `rec12969a3fdb0852` (MT-2026-084) are the **only two** `tblMaintenanceTickets` rows containing "4C" ✔; a "Mesa Vista" query additionally returns the pool-pump record `rec860db6b493af1e5b` (MT-2026-1326) ✔ — every OE 6 search-shape claim verified
- Schema: fldUnit / fldTurnStatus (`selSched|selProg|selReady` **only**) / fldMoveOut / fldTargetReady / fldNotes2. **No cost field, no Closed option** ✔ (OE 5)

`slack.slack_messages.json` / `slack_channels.json` / `slack_users.json`:
- 8 channels; C004 = `#make-ready` (144 messages), C005 = `#vendors` (**exactly 6 messages, none touching 4C** — OE 22's unreliable-mailbox claim confirmed) ✔
- Regex `\b4C\b` over all 580 messages returns **exactly 5** hits, all in C004, all Carlos Mendez `U07E4512181`, at ts `...868.000000` / `...869.000001` / `...870.000002` / `...871.000003` / `...873.000005` ✔
- Narrower "Mesa Vista 4C" returns **exactly 3** ✔
- The sixth message ts `1779501872.000004` from Jaime Salinas `U2CD1BC03B2` ("Jaime flagged a paint touch-up on the bedroom closet trim. Tony got it done today, Airtable updated.") **names neither the unit nor the property** and is reachable only via `slack_read_channel` ✔ — OE 22/23's keyword-invisibility claim is exactly right
- User ids verified: `U07E4512181` Carlos Mendez, `U2CD1BC03B2` Jaime Salinas, `U9741B657FE` Brooke Phillips ✔

`gmail.gmail_messages.json` / `gmail_threads.json`:
- Message `5101c5a41dffa90a` in thread `66132537181ecbe1`, dated `2026-06-02T22:47:34+00:00`, from carlos.mendez@starpm.com to linda.castillo@gmail.com, cc tony.reyes / pete.donovan / carmen.delgado / brooke.phillips / jaime.salinas, subject "Mesa Vista 4C Make-Ready Complete. Cost Summary for Your Records". Body (base64-decoded) confirmed **verbatim**: "...Pete Donovan finished the interior repaint (including a touch-up on the bedroom closet trim that came out of our QC walkthrough), and **Tony's team handled all internal repairs in-house**. I've put together owner invoice **2026-537**... This covers the vendor work only." **No dollar figure anywhere in the body** ✔
- Threads `525641a76c00fbe0`, `c138c134b23d60d3`, `83872812663ee5c9`, `f43fdaee4372a09b` and their message ids all present ✔
- OE 15's two `1,340` red herrings verified: `4a20c7c433db278a` ("His current rate is $1,340 per month" — Delgado renewal) and `6f2669a41401485a` ("The invoice total is $1,340" — Reyes Plumbing standup). Neither concerns 4C ✔

`contacts.contacts.json` (61 rows): Linda Castillo `b47044b4ec775b318bac813d5fb1bf5d` job **"Property Owner"** linda.castillo@gmail.com ✔ · Pete Donovan `8628aa258df55e62a6d89f64897fce77` job **"Exterior Painter"** ✔ · John Castillo `6268dbedf36a5967be2d1304e74bab58` "Water Delivery Representative" ✔ · Tony Reyes "Lead Maintenance Technician" ✔ · Jaime Salinas "Quality Control Inspector" ✔.

`Fact_Ledger.json`: `2026-534`, `2026-SC-4C`, `PD-2026-09`, `2026-519`, `2026-481-566`, `2026-AP-0184`, `2547` all present in `ids.invoice`. `2026-537` **absent** ✔. `recc8534b3fd13954` / `recbd087a4abd605b` / `reca424761ae15355` in `ids.airtable_record`; `C004` in `ids.slack_channel`; `U07E4512181` / `U2CD1BC03B2` in `ids.slack_user` ✔. Amounts `387.00 / 1340.00 / 85.00 / 1622.00 / 1140.00 / 95.00` present; **`1812.00` ABSENT** ✔ — confirms the answer is derive-only. `lifecycle.closed_periods = []` (no closed fiscal periods → no unlock precondition applies).

### Derived-figure recomputability
Every figure in every rubric is recomputable from stored atoms with no external input: `387+1340+85=1812`; `1622-1812=-190`; `1340-1140=200`; `95-85=10`; `1812+85=1897`; `387+1340=1727`; `385+1340+85=1810`. **Nothing is asserted that cannot be rebuilt from the four bills and the one invoice.**

### ANSWER-LEAKAGE — CLEAN (independently re-greped, two methods)
- `5_Prompt.txt`: **zero** hits for `1812` / `1,812` / `1812.00` / `190` / `$190` in any form.
- **Method 1 (raw regex over every `row_data` string in all 34 split files):** the token `1812` occurs 11 times universe-wide and **every occurrence is a timestamp or object-id substring** — gmail `history_id`/`internal_date` `1780181254000`, `1781218127000`, `1781812211000`; slack ts `1781812060.000184` (an inspector-scheduling message, its thread parent, and its activity record); airtable `created_time`/`last_modified_time` `2026-05-09 15:22:48.518124`. **Never a money value.** Comma-formatted `1,812` = **0 hits** universe-wide.
- **Method 2 (recursive walk of every string leaf in every parsed record, matching `$1,812` / `$1812` / `$190` / `190 dollars` / `1,812`):** **0 hits across all 34 files.** No email body, Slack text, Airtable note, invoice memo, bill PrivateNote, Linear issue/comment, HubSpot note or calendar description contains either figure as money.
- The bare numeric `190.0` exists as an **unrelated invoice line amount** on `618793969708` (Doc `2026-419`, "Service call fee - diagnostic visit, 4408 Elmwood Ave", customer **Pete Donovan**, different property). This is a coincidental collision that OE 10 already identifies as a decoy — it is not the 4C net delta and cannot be used to derive it.
- Grader-side statement of `1812.00` / `190.00` in OE 21/24-28 and in rubric titles is **required and correct** (self-containment mandate) and is not leakage.

---

## LENS 2 — Rubric binding (25 rubrics)

**PASS.** Programmatic census: **25 Outcome / 0 Process**. All 25 titles begin "The Agent". **Zero** tool names in any title (checked against the full 200+ tool-name set extracted from `7_Server_Tools_Details.json`). **Zero** em-dashes across all three deliverables. **Zero** occurrences of `approximately` / `roughly` / `about $`. **Zero** subjective terms (`thorough` / `professional` / `enough` / `properly` / `appropriate` / `adequate` / `comprehensive`). **Every one of the 25 `evidence` fields cites at least one OE step** ("Per OE N."). Outcome (25) > Process (0) — and 0 process rubrics is `[Non-Fail - Missing Process Rubric]` under `8_QC_Spec_Doc2.md`, with Category Balance scoring a 5.

**Self-containment:** every expected value is embedded in the criterion or evidence text — `$1,812`, `$1,622`, `$1,340`, `$1,140`, `$387`, `$95`, `$85`, `$190`, `$200`, `$10`, DocNumber `2026-534`, id `445653930748`, bill Doc `2026-481-566`, `linda.castillo@gmail.com`, "Ready (stored as selReady)", "In Progress (selProg)", "Property Operations base", "Make-Ready Turns table". A judge needs no universe access. Record ids are **deliberately not** used as accept-keys for the Airtable write (rubric 15 grades on turn status + notes content per OE 25's "grade on the content, not on the exact record id") — this directly implements the Task 41 post-fix lesson (`Learnings.md`, 2026-07-24 item 12).

**"(or similar)":** exactly one occurrence, in rubric 18's evidence, attached to the **email subject** — a freetext field where `8_QC_Spec_Doc2.md` (Overly Specific Criteria) makes "(or similar)" *mandatory*. It is not attached to any email address, id, channel, date or dollar amount. Correct usage.

**Too-tight check:** none. Rubric 23 deliberately does **not** pin a channel ("any StarPM team channel"), matching the prompt's channel-by-description phrasing ("our channel for the crew and front office") and OE 27's "graded on the corrected figure and the supersession of the old one, not on the channel id". Rubric 15 accepts either record so long as the Ready row is covered. Rubric 18 accepts a threaded reply as a variation. Rubric 10 explicitly accepts a line-array-only envelope ("the Agent does not have to set a total field explicitly"). No method or tool path is locked anywhere.

**Too-loose check:** none. Every exact value is exact; rubrics 1 and 6 carry explicit anti-rounding instructions with stated justification (the `1,810` decoy sits within 0.2% of `1,812`; both `190` inputs are whole-dollar). No "approximately" anywhere.

### Stress-test: the exclusion/inclusion pair (rubrics 7 and 8) — the most contestable judgment in the task

Rubric 7 excludes the `85.00` Alamo condition walk (`991582431419`). Rubric 8 keeps the `85.00` Permian closet trim (`546359391323`). Both `85.00`, both dated `2026-05-01`, both with `Balance 85.00`, and — this is the sharp edge — **both PrivateNotes open with the identical template "Internal labor charge for &lt;StarPM person&gt;"**.

I verified this programmatically: the string `"Internal labor charge for"` appears on **exactly 2 records in the entire universe**, and they are precisely these two bills. That is decisive for the design: the phrase cannot discriminate, because it appears on the one that is billable and the one that is not. OE 19 makes exactly this argument and it is factually correct.

**The case for keeping the closet trim on the owner side (five independent, converging discriminators):**
1. **The prompt's own rule is dispositive.** "Only outside vendor work belongs on her side." The `85.00` is a payable to **Permian Make-Ready Crew** (`204`, billing@permianmakeready.com), a third-party vendor in the 8-vendor master, with `Balance 85.00` still owed. It is outside vendor work on the prompt's literal test.
2. **The prompt's exclusion clause is narrowly scoped and does not reach it.** "Anything that was our own time on the unit, **an internal walk or a condition check we handled in house**, stays off her bill entirely." The appositive narrows the exclusion to walks and condition checks. A bedroom closet trim paint touch-up is neither — whereas `991582431419`'s line is *literally* "Unit condition inspection and punch list documentation", matching the prompt almost word for word.
3. **The agent-readable summary email settles it explicitly.** Message `5101c5a41dffa90a` says the trim was part of "**Pete Donovan finished the interior repaint (including a touch-up on the bedroom closet trim...)**" and, in the same sentence, that "**Tony's team handled all internal repairs in-house**". The email affirmatively places the trim on the vendor side of the split and off the in-house side.
4. **The genuinely in-house 4C work produced no bill at all.** The faucet cartridge, GFCI swap and drywall patch (Airtable `recbd087a4abd605b`, Slack ts `...869.000001`) have **zero** corresponding vendor bills — verified, only four bills reference Unit 4C. StarPM staff time never becomes a payable in this ledger, so the existence of a real `85.00` payable proves an outside party was paid.
5. **Account coding.** `546359391323` posts to **Owner Reserve (Trust) (64)** — a `Bank`/`TrustAccounts` account holding the owner's own funds — and is the only one of the four 4C bills coded there. `991582431419` posts to **Supplies (61)**, an operating expense. OE 19 correctly limits this to a tiebreaker between these two records only (the other two owner-billable bills post to 62 and 63), which is intellectually honest rather than over-claimed.
6. **Status quo.** The trim is *already* line 3 of invoice `2026-534` at `95.00`. Keeping it is the conservative read; removing it is the active change the prompt never asks for.

**The case against (the honest counter):** three records attribute the *doing* of the trim to a StarPM employee — the bill note ("Internal labor charge for Tony Reyes"), the Airtable note ("routed to Tony Reyes and resolved same day"), and the Slack post ("Tony got it done today"). A reviewer reading only "Anything that was our own time on the unit... stays off her bill" and only the bill's opening phrase can land on `1,727`.

**Verdict — is this a Unique Ground Truth risk?** *Honestly: yes, a QC reviewer could reasonably raise it, and I am logging it as a MAJOR.* But it does **not** meet the `[Fail - Multiple Valid Answers]` bar in `8_QC_Spec_Doc2.md`, for one reason above all others: the competing reading requires the reviewer to *ignore the prompt's first exclusion sentence* ("Only outside vendor work belongs on her side"), which the trim satisfies unambiguously, and to *stretch the second sentence past its own appositive*. Add the summary email's explicit in-house/vendor split, the self-neutralizing "Internal labor charge for" template, and the absence of any bill behind the genuinely in-house items, and the ground truth is unique under any reading that applies the prompt's stated rule. The rubrics are gradable: rubric 7's criterion names the bill by DocNumber and vendor; rubric 8's names the vendor and the scope; both evidence fields name the wrong-total each error produces (`1,897` / `1,727`). If an agent fails rubric 8 it will be because it read the bill note and dropped the line — the **designed** stump, i.e. Bucket 3.

**Recommended cheap hardening (optional, not required for PASS):** add one clause to rubric 8's evidence — *"the summary email Carlos already sent Linda places this touch-up inside Pete Donovan's vendor repaint scope and separately states that Tony's team handled the internal repairs"* — so the judge has the corroborating agent-readable surface in hand and the adjudication is visible on the face of the rubric.

---

## LENS 3 — Cross-artifact holism

### Forward map (every prompt ask → ≥1 OE AND ≥1 rubric)
| # | Prompt ask (`5_Prompt.txt`) | OE | Rubrics |
|---|---|---|---|
| A | "Before I log 4C as truly closed I want to be sure what she was actually charged holds up" (L1) | OE 11, 21 | 2 |
| B | "every dollar on her bill has to line up with what we actually paid out on that unit, to the dollar, no more and no less" (L3) | OE 13-17, 21 | 1, 3, 4, 5, 6 |
| C | "Go back to what each vendor charged us for the 4C work and set it against the line items I sent her" (L3) | OE 13-18 | 3, 4, 5 |
| D | "Only outside vendor work belongs on her side... an internal walk or a condition check we handled in house, stays off her bill entirely" (L3) | OE 18, 19, 20 | 7, 8 |
| E | "I do not want a second bill created next to the one she already has" (L5) | OE 24 | 14 |
| F | "Correct the invoice she is holding so it carries the right figure" (L5) | OE 10, 12, 24 | 9, 10, 11, 12, 13 |
| G | "get our 4C make-ready record in Airtable updated so it shows the final owner cost and the unit fully closed" (L5) | OE 2-5, 25 | 15, 16, 17 |
| H | "Then email Linda a short note letting her know where it landed" (L5) | OE 1, 7, 26 | 18, 19, 20, 21, 22 |
| I | "And drop a line in our channel for the crew and front office, so whoever else touches her account is working off the corrected number rather than the one I originally sent" (L5) | OE 22, 23, 27 | 23, 24, 25 |

**No prompt ask is unrepresented.**

### Reverse map (every OE and every rubric traces back)
All 28 OEs trace: OE 1 (identity, asks H/F), OE 2-6 (Airtable discovery, ask G), OE 7-8 (the summary she keeps, asks A/H), OE 9-12 (the receivable, ask F), OE 13-21 (the cost side, asks B/C/D), OE 22-23 (channel of record, ask I), OE 24-27 (the four writes, asks E/F/G/H/I), OE 28 (verification of asks A-I). All 25 rubrics map as tabled. **No orphan OE, no orphan rubric, no rubric checking something the prompt never asks.** OE 2 and OE 5 carry no rubric — correct, they are enabling reads and V4 makes process rubrics optional.

### Lever map — all four selected levers plus the reserve trace end-to-end
| Lever | Prompt sentence that triggers it | OE step | Rubric | Atom verified |
|---|---|---|---|---|
| **L2 structured-DB skip** (flagship) | "Go back to what each vendor charged us for the 4C work and set it against the line items I sent her." | OE 13, 15, 17 | 1, 3, 10, 11 | `1340.00` exists **only** on bill `696089964235` — not on `2026-534`, not in the summary email (body carries no figures), not in any Slack message. Confirmed by exhaustive scan. |
| **L10 reversal / supersession** | "that summary is the record she keeps"; "working off the corrected number rather than the one I originally sent" | OE 7, 11, 21, 23, 27 | 2, 25 | Invoice `2026-534` + email `5101c5a41dffa90a` are the stale mirror; the AP bills supersede. No Slack post carries an owner cost (verified across all 580 messages). |
| **L6 near-miss entity** | "Go back to what **each vendor** charged us **for the 4C work**" (forces bind-by-unit) | OE 10, 16, 21 | 1, 5, 9, 18 | 10-bill `1340.00` cluster verified exactly; `385.00` Rio Bend pass-through to the **same owner**; `1140.00` Hill Country bill on the **same account 63**; Linda / Pete / John Castillo triple. |
| **L11 net-vs-gross** | "Only outside vendor work belongs on her side. Anything that was our own time on the unit, an internal walk or a condition check we handled in house, stays off her bill entirely." | OE 18, 19 | 7, 8 | Twin `85.00` bills with the identical (and therefore self-neutralizing) "Internal labor charge for" template. |
| **L1 latching** (reserve) | "sent her a summary calling it done"; "I moved on to the next unit and left it there" | OE 3, 4, 6 | 15 | Two `tblMakeReady` rows, date fields inverted against modification order. |

**No lever has a missing piece.** See MAJOR-1 below for a yield (not preservation) concern on L2.

### Entity map
| Entity | Prompt | OE | Rubrics | Drift |
|---|---|---|---|---|
| Linda Castillo | named ("Linda Castillo owns that unit") | OE 1, 9, 10, 12 | 1-5, 7-9, 18-22, 25 | none — `linda.castillo@gmail.com`, contact `b47044b4ec775b318bac813d5fb1bf5d`, customer `proj-4ae920b7c9e8` used consistently |
| Pete Donovan | **absent** (correct — decoy kept out of the prompt) | OE 1, 7, 9, 14, 17 | rubric 18 evidence only, as a FAIL condition | none |
| Tony Reyes | **absent** | OE 4, 7, 17, 19, 20, 23 | none | none |
| Jaime Salinas | **absent** | OE 4, 6, 17, 19, 23 | rubric 15 evidence, as a row discriminator | none — matches `recc8534b3fd13954` fldNotes2 verbatim |
| Mesa Vista 4C | named | all | all | none |
| Carlos Mendez | first-person persona | OE 1, 18, 22 | none | none — matches `2_Persona.txt` and `PersonaBrief.txt` |

**Zero entity drift.** Decoys (Pete Donovan as owner, John Castillo, Tommy Reyes, Rio Bend, the nine wrong `1340.00` bills) appear **only** in OE disambiguation prose and rubric FAIL clauses — never in the prompt, which stays clean and implicit.

### Implicit-prompt framing preserved
Carlos believes the `1,622` is right ("I billed her for the work and sent her a summary calling it done"). The prompt never hints a figure is wrong and never says "check whether the repaint is understated". Per `Learnings.md` L15/L16 this is the correct implicit framing. **No rubric demands an investigation step the prompt forecloses, and no rubric fails a correct executor.** Rubric 14 is the single negative guard (`Learnings.md` L21: one per task).

### Prompt-validator WARN adjudication — "bolt-on candidate"
`Validator_Reports/prompt.md` WARNs: *"bolt-on candidate: sentence 'Correct the invoice she is holding so it carries the right figure, and get our 4C make-ready record in Airtable updated...' shares no named entities with the rest of the prompt."*

**Remove-sentence test applied.** Deleting the sentence leaves: *"If they do not, I do not want a second bill created next to the one she already has. Then email Linda a short note letting her know where it landed..."* — the corrective action disappears entirely, "Then" dangles with no antecedent action, "where it landed" loses its referent, and the opening premise ("Before I log 4C as truly closed I want to be sure what she was actually charged holds up") never resolves. The remainder **does not still make sense**. Per `8_QC_Spec_Doc2.md` Coherence, that is the definition of *not* a bolt-on.

**Ruling: validator FALSE POSITIVE.** The heuristic keys on proper-noun overlap; this sentence carries its subjects as pronouns ("she", "her", "our 4C") and short-forms ("4C", "Airtable") because it is the *consequent* of the immediately preceding conditional. Every sub-ask in the prompt flows from one situation — closing Mesa Vista 4C on the owner side. **Not a Major. No change required.**

---

## LENS 4 — Red-team adversarial

**Shortcut analysis.** Four shortcut paths were traced and all four fail loudly:
- *Trust the invoice + the "complete" email* → reports `1,622`, logs closed → fails rubrics 1, 2, 3, 4, 6, 10, 11, 12, 16, 19, 20, 21, 24, 25.
- *Sum all four 4C bills* → `1,897` → fails 1, 7, 10, 16, 19, 24 (rubrics 1, 7 and 10 name `1,897` explicitly as the reject value).
- *Drop the trim as internal* → `1,727` → fails 1, 8, 10, 12, 16, 19, 24.
- *Substitute the Rio Bend deep clean* → `1,810` → fails 1, 5, 10, 13, 16, 19, 24 (rubric 1 names `1,810` and explains why rounding must not admit it).

**No shortcut satisfies the prompt without exercising ≥2 levers.** Reaching `1,812` requires at minimum L2 (open the AP bills), L6 (bind by unit, not by amount or by the email's `2026-537`), and L11 (discriminate the twin `85.00`s).

**Can `$1,812` be recovered from one obvious first search?** **Partially — and this is the one genuine shallowness.** A single `search_bills(query="Mesa Vista 4C")` returns all four bills and therefore the candidate set `{387, 1340, 85, 85}`. It does **not** resolve which `85.00` belongs, and it does **not** surface the `1,140`/`95` invoice lines the figures must be set against. The naive one-search sum is `1,897`, a graded wrong answer. So the trap is **not** trivially shallow, but the *discovery* hop (repaint is `1,340`, not `1,140`) is one call deep once the agent decides to look at bills. See MAJOR-1.

**Second valid reading producing a different write-action set or final universe state?**
- *`$1,727` reading* — the only substantive divergence. Adjudicated in Lens 2; logged as MAJOR-2.
- *"log 4C closed" as an Airtable status change* — foreclosed: the schema offers only `selSched|selProg|selReady` (verified), OE 5 and rubric 17 route closure to `fldNotes2`, and rubric 17's evidence warns that inventing a Closed value produces no successful write. No divergence.
- *Which channel* — rubric 23 is channel-agnostic; all 8 channels carry the same 21 members, so any choice genuinely reaches crew and front office. No divergence in final state that any rubric grades.
- *Whether to also update the stale row* — rubric 15's evidence explicitly permits it. No divergence.
- *Send vs draft* — Gmail is draft-only (no send tool exists in the catalog); rubric 18 grades a draft. No divergence.
- *Credit memo instead of amendment* — foreclosed: the correction **raises** the receivable from `1,622` to `1,812`, and a credit memo reduces. OE 24 and rubric 14 both state this. No divergence.

**Drift sweep across all three files.**
| Check | Result |
|---|---|
| Em-dashes | `5_Prompt.txt` 0 · `6_Oracle_Events.txt` 0 · `7_Rubrics.json` 0 |
| "at least N" without prompt mandate | 0 hits in any file |
| Tool names in rubric titles | 0 (checked against the full extracted tool-name set) |
| Cross-universe tokens (`mortgage_los`, `stripe`, `keystonemortgage`, `brookfieldcpas`, `moveops`, `keystone`, `brookfield`, "April 28 2026") | **0 hits across all three files** |
| Subjective terms in rubrics | 0 |
| "approximately" / "(or similar)" misuse | 0 (the single "(or similar)" is on a freetext subject — mandatory usage) |

---

## LENS 5 — Narrative-State + Action-Prescription (per-tool strictness)

**PASS.**

**State-implying claims vs universe lifecycle.** Every claim checked:
- "Linda Castillo owns that unit" → contact job "Property Owner"; invoice `2026-534` CustomerRef Linda Castillo. ✔
- "When the turn wrapped back in the spring I billed her for the work and sent her a summary calling it done" → invoice TxnDate `2026-05-01`; email dated `2026-06-02` (both spring, against today `2026-07-01`). ✔
- "the post-move-out deep clean, the full interior repaint, and the closet trim touch-up" → invoice lines 1/2/3 recite exactly these three scopes, and CustomerMemo names all three ("...post-move-out deep cleaning and full interior repaint, including the QC-flagged closet trim correction"). ✔
- "The 4C costs are a straight pass-through to Linda" → invoice PrivateNote "Owner cost pass-through invoice..."; bill notes "Owner pass-through". ✔
- The turn genuinely is physically complete (`recc8534b3fd13954` selReady + ticket `reca424761ae15355` "market-ready" + Slack ts `...873.000005`), which is what makes the *billing* question the live one. The OE and rubric chain assume the **same** state throughout — no rubric expects the agent to reopen the turn. ✔

**Action-prescription vs record-prescribed actions.** Two bills carry an operative instruction naming **Pete Donovan** as the owner account (`195089456477`: "paired receivable invoice to be issued to Pete Donovan"; `546359391323`: "pair with corresponding AR invoice to Pete Donovan's owner account"). The prompt supplies **explicit override language on its first line — "Linda Castillo owns that unit"** — which names the owner directly rather than leaving the agent to resolve the tangle. Corroborated four ways (invoice CustomerRef, contact job title, the summary email's recipient, and Pete's "Exterior Painter" role). This is a designed L6 near-miss with prompt-side disambiguation, **not** an unresolved prescription divergence. No record prescribes creating a *second* invoice for the same scope; `991582431419`'s note positions its punch list as *upstream* of later pass-through invoices, which is consistent with excluding it. ✔

**Per-tool parameter binding — all 27 bindings checked against `StarPM_Base_Universe/7_Server_Tools_Details.json`, per-tool, not per-service:**
| OE | Tool | Params used | Catalog | Verdict |
|---|---|---|---|---|
| 1 | `contacts_search_contacts` / `contacts_get_contact` | `query` / `contact_id` | matches | ✔ |
| 2 | `list_bases` / `list_tables_for_base` | none / `baseId` | matches | ✔ |
| 3, 6 | `search_records` | `baseId`, **`table`**, `query` | catalog: `baseId`(req), **`table`**(req), `query`(req) | ✔ correct — `table`, not `tableId` |
| 4 | `list_records_for_table` | `baseId`, **`tableId`**, `recordIds` | catalog: `baseId`, `tableId`, `recordIds` | ✔ correct — `tableId`, not `table` |
| 5 | `get_table_schema` | `baseId`, **`tables`** (array) | catalog: `baseId`, `tables`(array, req) | ✔ |
| 7, 8 | `search_threads` / `get_thread` | `query` / `threadId` | matches | ✔ |
| 9 | `search_customers` | `query` | matches | ✔ |
| 10 | `search_invoices` | `query` | matches | ✔ |
| 11 | `read_invoice` | **`invoice_id`** | catalog: `invoice_id`(req) | ✔ correct — not `id` |
| 12 | `get_aged_receivables` / `get_customer_balance` | `customer` / `customer`,`start_date`,`end_date` | matches | ✔ |
| 13, 16 | `search_bills` | `query` / `max_results`, `start_position` | matches | ✔ |
| 14, 15, 17, 18 | **`get-bill`** | `id` | catalog: **`get-bill`** (hyphenated), `id`(req) | ✔ hyphenated form is correct; `get_bill` does **not** exist |
| 20 | `search_vendors` | `query` | matches | ✔ |
| 21 | `get_vendor_expenses` | `vendor`, `start_date`, `end_date` | matches | ✔ |
| 22 | `slack_search_public_and_private` | `query` | matches | ✔ |
| 23 | `slack_read_channel` | `channel_id` | matches | ✔ |
| 24 | `update_invoice` | `id`, **`SyncToken`**, `properties` | catalog: `id`, `SyncToken`, `properties` | ✔ exact casing |
| 25 | `update_records_for_table` | `baseId`, `tableId`, `records` | matches | ✔ camelCase correct |
| 26 | `create_draft` | `to`, `subject`, **`body`**, `replyToMessageId` | catalog: `to`,`cc`,`bcc`,`subject`,`body`,`htmlBody`,`replyToMessageId` | ✔ `body` is the content param; **no send tool exists in the gmail server** → draft is the correct deliverable |
| 27 | `slack_send_message` | `channel_id`, **`message`** | catalog: `channel_id`(req), `message`(req) | ✔ `message`, not `text`, not `payload` |
| 24 (negative) | `create_invoice` | — | exists in catalog | ✔ the "do NOT call" guard names a real tool |

**Zero parameter-on-wrong-tool errors.**

**Lifecycle-precondition check:** `Fact_Ledger.lifecycle.closed_periods = []` — no closed fiscal periods exist in this universe. Invoice `445653930748` has `sync_token "0"` and `Balance == TotalAmt` (nothing collected, verified via payment `931951074454`'s LinkedTxn), so it is amendable in place with no unlock step required. The Airtable row is unlocked. **No OE step writes to a lifecycle-locked state.** ✔

---

## LENS 6 — Verifier-Fails-Spec Pre-Upload Bucket-1 Check

Every one of the 25 rubrics was simulated against `Evals_starpm/4_Verifier_Fails_Eval.md` Phase 2 (tool existence, "(or similar)" validity, expected-value existence, achievability, prompt grounding, rationale alignment, parameter existence) and against the anti-pattern list. Summary of the clean checks: **tool existence** — no rubric names a tool; **expected-value existence** — all 25 rubrics' values re-verified against `Universe_Split` in Lens 1; **achievability** — all four writes are performable with existing tools and existing parameters; **prompt grounding** — all 25 map to a prompt ask (Lens 3 forward map); **service metadata** — rubric 18 carries the recipient (`linda.castillo@gmail.com`) and rubric 23 carries the channel scope; **write-verb Process rubrics** — none possible (0 process rubrics); **account-number entity-trap** — none (StarPM has 7 accounts, single-entity); **persona-scope drift** — none (the prompt's possessives "our channel", "our 4C make-ready record" are correctly resolved to StarPM-owned surfaces).

### Rubrics flagged at Bucket-1 risk — 4 of 25 (16%)

**[BUCKET_1_RISK] rubric[4]: "The Agent identifies the Mesa Vista 4C post-move-out deep clean as the one line where the $387 charged to Linda Castillo matches what Sunshine Cleaning billed StarPM."**
— risk: *criterion demands an affirmative "no variance" assertion about a line that did not change.* An agent that reports the corrected breakdown (`$387 + $1,340 + $85 = $1,812`) and narrates only the two lines that moved has done the work correctly but may not state that the deep clean "ties with no difference", and a literal judge could fail it. That failure would be Bucket 1 (rubric phrasing), not Bucket 3.
— fix: append to the evidence — *"A line-item reconciliation that carries the deep clean at $387 unchanged against the vendor bill satisfies this criterion; the Agent does not have to use the word 'matches'."*

**[BUCKET_1_RISK] rubric[19]: "The Agent states in the email draft to Linda Castillo that the interior repaint was $1,340 rather than the $1,140 she was originally billed."**
— risk: *AND-bundling of two values with no disjunctive escape, and it is inconsistent with rubric[2], which grades the identical fact pair in the final response and DOES offer one ("...or for the $200 shortfall on that line").* An owner-facing note that says "the interior repaint came in at $1,340" without restating the superseded `$1,140` is a plausible correct behavior and would fail.
— fix: mirror rubric[2] — extend the evidence to *"...or a statement that the repaint line was raised by $200 from the figure she was originally billed."*

**[BUCKET_1_RISK] rubric[21]: "The Agent states in the email draft to Linda Castillo that Mesa Vista 4C is now closed on her side."**
— risk: *beyond-prompt-literal ask on a specific deliverable.* The prompt asks for "a **short** note letting her know where it landed, so she is not sitting on a summary that no longer matches" — the explicit ask is the corrected figure. Closure is prompt-framed at the task level ("Mesa Vista 4C is one I want fully closed on the owner side"; "log 4C closed") but is not an explicit content requirement for the email, and "short note" actively pushes agents toward brevity.
— fix: broaden slightly — *"...that Mesa Vista 4C is now closed or finalized on her side, or that no further owner charges are outstanding for this turn."*

**[BUCKET_1_RISK] rubric[24]: "The Agent states in the channel message that the corrected Mesa Vista 4C figure supersedes the $1,622 Linda Castillo was originally billed."**
— risk: *criterion is stricter than its own evidence.* The title requires naming `$1,622`; the evidence's closing sentence only requires "flagging that it supersedes the earlier one". Judges grade the criterion first, so a post reading "corrected to $1,812 on invoice 2026-534, replacing the figure in my earlier summary to Linda" could be failed on the missing token even though it delivers the supersession the prompt demands ("rather than the one I originally sent").
— fix: align the criterion to the evidence — *"...supersedes the figure Linda Castillo was originally billed (the $1,622 on invoice 2026-534)"*, with the parenthetical as grounding rather than a required token. (This is the same "id-that-looks-like-grounding gets graded as a token" defect documented in `Learnings.md` 2026-07-23 item 5 / 2026-07-24 item 7.)

### Rubrics examined and cleared (notable adjudications)
- **rubric[2] / rubric[3]** (three-value comparisons in the final response) — cleared. Both carry a disjunctive "or" in the evidence, both draw all values from a single comparison, and both are the coupled-facts exception in `8_QC_Spec_Doc2.md` ("Assessment of multiple components within one tool output can be grouped").
- **rubric[7]** (keep the closet trim) — adjudicated **Bucket 3**, not Bucket 1. A failure here is an agent misapplying the prompt's stated rule against five converging discriminators — the designed L11 stump. Logged separately as MAJOR-2 for UGT visibility.
- **rubric[13]** (no second invoice / no credit memo) — cleared. The gating clause and both negatives are satisfied simultaneously by any correct trajectory; no plausible false-fail. One dead clause noted as MINOR-2.
- **rubric[14]** (target the Ready row) — cleared and commended. Grades on turn status + notes content rather than on `recc8534b3fd13954`, which is the exact remedy `Learnings.md` (2026-07-24, item 12) prescribes after Task 41's R6 false-fail.
- **rubric[22]** (post in a team channel) — cleared. Channel-agnostic by design; all 8 channels carry the same 21 members, so the enumerated alternatives are all genuinely valid and none is an invalid path admitted by over-breadth.

**Bucket_1_Risk = 4 / 25 = 16.0% ≤ 20% → PASS**, with 4 cheap, concrete hardening fixes listed above.

---

## Deterministic-gate COUNCIL-notes adjudication

**`validate --phase injection`: PASS, 0 fails, 0 warns, 4 COUNCIL notes.**
- *P4 fact/status/amount/timeline contradiction vs base universe* — **CONFIRM no contradiction.** `4_Changelog.json` is `[]` and `9_Universe_inject.sql` carries no statements: nothing was injected, so there is no CB edit that could contradict the base. Every atom the task relies on was re-verified as pre-existing base data.
- *P5 formality/register vs channel norms* — **CONFIRM.** Slack C004 posts are terse operational updates; the Gmail summary is a formal owner-facing cost letter; QuickBooks PrivateNotes are clipped internal AP shorthand. All register-appropriate.
- *P6 tool-call chain depth (>5)* — **CONFIRM.** 28-step OE, ~40+ canonical calls, five services. Far exceeds 5.
- *P8 injection difficulty ≥ 3.5* — **My score: ~4.2 / 5.** Drivers: the answer exists as a total nowhere and must be assembled from three of four candidate bills; a ten-bill `1,340` amount cluster plus a same-owner `385.00` deep-clean pass-through plus a same-account-code `1,140.00` bill make amount-based search actively hostile; the twin `85.00` bills share an identical PrivateNote template; the summary email quotes a **non-existent** invoice number; the Airtable row pair inverts its date fields against modification order; the sixth Slack message is keyword-invisible; and four writes across four services are required. Clears 3.5 comfortably.

**`validate --phase submission_gate`: PASS, 0 fails, 0 warns, 2 notes.**
- *6.3 under-strictness* — **CONFIRM adequate.** Every dollar figure is exact with explicit anti-rounding rationale on the two derived ones; every id is exact; no "approximately" anywhere.
- *6.6 exclusion coverage* — **CONFIRM.** All four wrong totals are named as reject values inside rubric evidence (`1,622` / `1,897` / `1,727` / `1,810`), plus the Rio Bend `385` substitution and the Pete-Donovan-as-recipient error.
- *6.8 UGT convergence* — **CONFIRM with the MAJOR-2 caveat.** `$1,812`, amend-in-place on `2026-534`, Ready-row Airtable write, draft to Linda, team-channel post: single-valued. The `$1,727` alternative reading is disclosed and adjudicated in Lens 2.
- *6.9 OE authority* — **CONFIRM.** OE 25 explicitly instructs "grade on the content, not on the exact record id"; OE 27 explicitly de-pins the channel. Rubrics 14 and 22 honour both.
- *6.10 strict feasibility* — **CONFIRM.** All 27 tool-parameter bindings verified on the exact named tool; all four writes performable.
- *6.11 date alignment* — **CONFIRM.** All task-relevant records fall inside `2026-05-01..2026-07-01`; the invoice (`2026-05-01`) and the summary email (`2026-06-02`) both sit in "the spring" relative to today `2026-07-01`, matching the prompt's phrasing.

**`validate --phase rubrics`: PASS, 0 fails, 33 warns, 0/25 Major, 0/25 Moderate, 0/25 any issue.** All 33 warns adjudicated as **validator false positives**:
- The 22 `X2 rubric-OE consistency` warns ("typed value N in title has no OE step referencing any amount value") are an extractor artifact: the validator's amount matcher requires a `$` prefix, and `6_Oracle_Events.txt` writes bare figures. I verified **by hand** that every rubric amount appears in the OE text — `1812.00` (OE 21/24/25/26/27/28), `1622.00` (OE 10/11/21/24/27/28), `1140.00` (OE 11/15/26), `1340.00` (OE 13/15/16/21/24/25/26/27), `200.00` (OE 15/21/28), `10.00` (OE 17/21/28), `85.00` (OE 13/17/18/19/21/24/25/27), `95.00` (OE 11/17/26), `387.00` (OE 13/14/21/24/25/27), `190.00` (OE 21/26/28). **Zero real gaps.**
- The 6 `$1,812 not in Fact_Ledger amounts` warns are the **desired** state — they are positive evidence the answer is derive-only.
- The 2 `$190 not in Hardness_Plan ground-truth atoms` warns: `190` is `1812 − 1622`, derived, stated in OE 21. Correct.
- The `$10 not in Fact_Ledger amounts` warn: `10` is `95 − 85`, derived. Correct.

**`validate --phase oe`: PASS, 0 fails, 0 warns.** 28 steps — inside the `OE_Convention_Inventory.json` distribution (min 11, max 28, mean 16.5; Task13 is also 28). Sequential `OE N:` numbering, varied imperative openers (Look / List / Pull / Read / Retrieve / Cross-reference / Search / Resolve / Locate / Confirm / Open / Disambiguate / Use / Compute / Correct / Update / Draft / Post / Verify), zero em-dashes. **No convention drift.**

**`validate --phase prompt`: PASS, 0 fails, 1 warn (the bolt-on candidate).** Adjudicated a false positive in Lens 3 above.

---

## Per-model density projection

Trajectories are 0 bytes (task not yet run), so this is a **projection**. I sketched the integrated trajectory independently rather than adopting the Hardness_Plan's number.

**Minimal-path floor (one call per OE step, no exploration, no verification re-reads): ~31 calls.** That floor already clears the 15 INSUFFICIENT line by 2x.

**Realistic Opus 4.8 expansion over the floor:** 3-4 Gmail search variants plus 4-5 thread reads across the five 4C threads (+4); 2-3 `search_invoices` query variants to get past `2026-537` and the two same-owner decoys (+2); 3-4 `search_bills` calls including the `max_results=200` / `start_position` page-through the 113-bill ledger requires (+2); 2-4 opens of wrong `1,340.00` bills during cluster disambiguation (+3); both `get_aged_receivables` and `get_customer_balance` (+1); 2 Slack search variants before the channel read (+1); `search_vendors` twice, targeted then full master (+1); `get_vendor_expenses` corroboration (+1); post-write verification re-reads on the invoice, the Airtable row and the channel (+3).

| Model | Band | **Midpoint** | StarPM V4 band |
|---|---|---:|---|
| **Opus 4.8** | 38 – 53 | **~45** | **PASS (≥ 40)** |
| **Gemini** | 30 – 43 | **~36** | **THIN (15 – 39)** — above the 15 INSUFFICIENT floor |

The Gemini figure applies the empirically measured −9 to −10 spread from Tasks 39/40/41 (Task 40's measured Gemini run set was 47/45/37/38/33/40, avg 40.0). My Opus midpoint runs ~1.5 calls above the Hardness_Plan's 43.5 because the delivered OE locks four real writes plus the ten-bill disambiguation; my Gemini midpoint runs ~2 above the plan's ~34 for the same reason.

**Gemini THIN is accepted, not waived.** `Hardness_Plan.md` §"THIN density acceptance" carries the required per-task justification (the symmetric flagship swept 0/12 on two prior StarPM tasks regardless of call count; the mitigation was to lock a 4-write OE). **I verified the mitigation was actually delivered:** OE 24 `update_invoice`, OE 25 `update_records_for_table`, OE 26 `create_draft`, OE 27 `slack_send_message` — **4 writes across 4 services**, all model-agnostic. THIN is not INSUFFICIENT and is not a blocker under the StarPM per-model tiering; it is the top S4 watch-item.

**Service breadth (from the delivered OE chain, not the plan):** quickbooks ~18-20 calls (~42%), airtable ~7-8 (~17%), gmail ~7-9 (~18%), slack ~4-5 (~10%), contacts ~3 (~7%). **5 distinct services**, each ≥5%, dominant service <60% → **PASS**. Note the Hardness_Plan claimed 6 services including a Linear leg (~3 calls, "optional Linear OPS-39 budget comment") that the final OE dropped; see MINOR-1.

**Dual-model sign-off:** both **Opus 4.8** and **Gemini** runs are expected downstream — 6 each, with results landing in `8a_Verifier_Fails_Opus.txt` / `8b_Verifier_Fails_Gemini.txt` and `Agent_Responses/{Opus,Gemini}/`.

---

## Issue list

**BLOCKERs: 0.**

**[MAJOR] L2 flagship yield is optimistic — the prompt points the agent straight at the vendor cost side, per the `Learnings.md` L29 escape-valve pattern** — `5_Prompt.txt:3` ("Go back to what each vendor charged us for the 4C work and set it against the line items I sent her") — **exact fix: none applied; accept with re-scoped expectations.** The lever is *preserved* (verified: `1340.00` exists only on bill `696089964235`, absent from the invoice, the summary email and all 580 Slack messages) but its *stump rate* will not match the Hardness_Plan's projected ~0/12. That sentence cannot be removed without making the prompt a riddle and failing QC Feasibility/Clarity. The real difficulty engine here is L6 (10-bill `1,340` cluster + `385` Rio Bend to the same owner + `1,140` on the same account code + `2026-537` phantom + Pete/Linda/John Castillo) and L11 (twin `85.00`), plus the L31-shaped supersession beat in rubric 24. **Action: re-attribute the expected stump to L6/L11 in `Hardness_Plan.md` §Stump Hypothesis at S4, and do not credit L2 with the sweep if the trajectories show agents reaching the bills easily.** Difficulty overall remains adequate: passing all 25 rubrics requires the exact `$1,812`, the exact `$190`, the twin-`$85` call, four correct invoice lines, the Ready-row write, and an explicit supersession of `$1,622` in the channel post.

**[MAJOR] Disclosed Unique-Ground-Truth contest on the `$85` closet trim — a QC reviewer could reasonably raise it** — `7_Rubrics.json` rubric[7] + `5_Prompt.txt:3` — **exact fix (cheap, recommended): append to rubric[7]'s `evidence`** — *"The summary email Carlos already sent Linda places this touch-up inside Pete Donovan's vendor repaint scope and separately states that Tony's team handled the internal repairs, so the record the owner holds already treats it as vendor work."* Adjudicated in Lens 2: the ground truth **is** unique under the prompt's own rule ("Only outside vendor work belongs on her side", with the exclusion narrowed to "an internal walk or a condition check"), backed by five converging discriminators including the fact that the "Internal labor charge for" template appears on **both** `85.00` bills and therefore separates nothing. Does **not** meet the `[Fail - Multiple Valid Answers]` bar. Logged as MAJOR for reviewer visibility, not as a defect requiring REVISE.

**[MINOR-1] Hardness_Plan claims 6 services / a Linear leg the delivered OE does not use** — `_aux/Hardness_Plan.md:70-82` vs `6_Oracle_Events.txt` — fix: update the Service Breadth table to the delivered 5 services (quickbooks / airtable / gmail / slack / contacts) and drop the "optional Linear OPS-39 budget comment" line, or add a Linear read to the OE if Gemini density needs the lift. Breadth still passes at 5 services with the dominant service under 60%.

**[MINOR-2] rubric[13] evidence contains a logically dead clause** — `7_Rubrics.json` rubric[13] evidence ("...or if a credit memo was issued **in place of** amending it") — a credit memo issued *in place of* amending means no `2026-534` update call exists, which the criterion's own gating sentence already fails. Harmless but confusing to a judge. Fix: change to *"or if a credit memo was also issued against 2026-534"*.

**[MINOR-3] rubric[22] evidence carries a vestigial tool-parameter instruction** — `7_Rubrics.json` rubric[22] evidence, final sentence ("The text parameter for this tool is message.") — this is OE-facing guidance that does not belong in a judge-facing field. It names no tool, so it does not trip the Agent-Centric-Phrasing fail, but it should be deleted.

**[MINOR-4] Four Bucket-1 hardening fixes** — rubric[4], rubric[19], rubric[21], rubric[24] — exact fixes given in Lens 6. All are one-sentence evidence/criterion edits. Recommended before upload; none is REVISE-triggering.

**[MINOR-5] Prompt word count 364 (>300)** — `5_Prompt.txt` — validator NOTE only; inside the sweet spot, no action needed.

---

## Hard-rules PASS-evidence table (all 13 rules from `Reference/Sessions/FINAL.md`)

| # | Hard rule | Verdict | Evidence |
|---|---|---|---|
| 1 | Correct derived figure NEVER stated verbatim in prompt / email body / Slack body / document body / record content | **PASS** | Two independent scans of all 34 `Universe_Split` files: raw-regex (`1812` occurs 11x, **all** gmail `history_id`/`internal_date`, slack ts `1781812060.000184`, airtable microsecond timestamps) and recursive string-leaf walk for `$1,812`/`$1812`/`$190`/`1,812` (**0 hits**). `5_Prompt.txt` zero hits. Grader-side statement in OE 21/24-28 and rubric titles is the required answer key, per scope note. |
| 2 | Every tight identifier exists in `Fact_Ledger.json` / universe | **PASS** | Lens 1 table. Bill ids `195089456477`/`696089964235`/`546359391323`/`991582431419`, invoice `445653930748`, all 10 `1340.00` cluster ids, decoys `340207319849`/`310712648304`/`618793969708`/`240572546619`/`328611897179`/`173322471681`, records `recc8534b3fd13954`/`recbd087a4abd605b`/`reca424761ae15355`/`rec12969a3fdb0852`/`rec860db6b493af1e5b`, contact `b47044b4ec775b318bac813d5fb1bf5d`, customer `proj-4ae920b7c9e8`, vendors `204`/`200`/`proj-d016366b403c`/`proj-a989f559245a`, accounts `61`/`62`/`63`/`64`, channel `C004`, users `U07E4512181`/`U2CD1BC03B2`, all 6 Slack ts, thread `66132537181ecbe1` + 4 more, message `5101c5a41dffa90a` + 5 more, payment `931951074454`, DocNumbers `2026-534`/`2026-SC-4C`/`PD-2026-09`/`2026-519`/`2026-481-566` — **every one resolved to a real row.** `2026-537` confirmed absent (intended). Zero phantoms. |
| 3 | Every Hardness lever still triggered end-to-end | **PASS** | Lens 3 lever map: L2 / L10 / L6 / L11 / L1 each mapped to a prompt sentence + OE step + rubric + a verified atom. Yield caveat on L2 logged as MAJOR-1, not a preservation failure. |
| 4 | Integrated tool-call density projection (StarPM per-model: ≥40 PASS, 15-39 THIN, <15 INSUFFICIENT) | **PASS (Opus) / THIN (Gemini)** | Independent trajectory sketch: minimal floor ~31; Opus midpoint ~45 (band 38-53) → PASS; Gemini midpoint ~36 (band 30-43) → THIN, well above the 15 floor. `Hardness_Plan.md` §THIN density acceptance carries the required per-task justification and the 4-write mitigation, which I confirmed was delivered (OE 24/25/26/27). |
| 5 | Outcome > Process; no tool name in title; no em-dashes anywhere | **PASS** | 25 Outcome / 0 Process (programmatic census; `[Non-Fail - Missing Process Rubric]` per `8_QC_Spec_Doc2.md`). 0 tool names in titles (checked against the full extracted tool-name set). 0 em-dashes in `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json`. All 25 titles begin "The Agent". |
| 6 | Entity references consistent across prompt / OE / rubrics | **PASS** | Lens 3 entity map. Linda Castillo / Pete Donovan / Tony Reyes / Jaime Salinas / Mesa Vista 4C / Carlos Mendez all consistent. Decoys appear only in OE disambiguation and rubric FAIL clauses, never in the prompt. Zero drift. |
| 7 | Implicit-prompt framing preserved | **PASS** | Prompt never hints a figure is wrong ("I billed her for the work and sent her a summary calling it done"); no rubric demands an investigation the prompt forecloses; no rubric fails a correct executor. `Learnings.md` L15/L16 satisfied. Single negative guard (rubric 13) per L21. |
| 8 | OE step count + opening-verb coverage match `OE_Convention_Inventory.json` | **PASS** | 28 steps vs distribution min 11 / max 28 / mean 16.5 (Task13 also 28). Sequential `OE N:` prefix, 19 distinct imperative openers, `em_dash_banned` satisfied. |
| 9 | Every state-implying claim matches universe lifecycle state | **PASS** | Lens 5: owner, billing date, summary date, the three scopes, pass-through framing, and physical-completion state each verified against `quickbooks_entities` / `airtable_records` / `gmail_messages`. OE and rubric chain assume the same state. |
| 10 | Every prompt action aligns with record-prescribed actions OR carries explicit override | **PASS** | Two bills prescribe pairing the receivable to **Pete Donovan's** owner account; the prompt overrides explicitly on line 1 ("Linda Castillo owns that unit"), corroborated by the invoice CustomerRef, the contact job titles, and the summary email recipient. No record prescribes a second invoice for the same scope. |
| 11 | Every OE tool-parameter binding on the EXACT named tool | **PASS** | Lens 5 table: all 27 bindings checked per-tool against `StarPM_Base_Universe/7_Server_Tools_Details.json`. `search_records`→`table` vs `list_records_for_table`/`update_records_for_table`→`tableId` correctly split; `get_table_schema`→`tables` array; `read_invoice`→`invoice_id` not `id`; `get-bill` hyphenated (`get_bill` does not exist); `update_invoice`→`id`/`SyncToken`/`properties`; `create_draft`→`body`; `slack_send_message`→`message` not `text`. Zero errors. |
| 12 | Every OE step writing to a lifecycle-locked state includes the prerequisite unlock earlier | **PASS (n/a satisfied)** | `Fact_Ledger.lifecycle.closed_periods = []` — no closed fiscal periods exist. Invoice `445653930748` has `sync_token "0"`, `Balance == TotalAmt`, and no applied payment (payment `931951074454` links to `247748966591`), so it is amendable in place. Airtable row unlocked. No OE writes to a locked state. |
| 13 | ≤ 20% of rubrics surface as Bucket_1_Risk | **PASS** | **4 / 25 = 16.0%** — rubric[4], rubric[19], rubric[21], rubric[24]. All four carry one-sentence fixes. Threshold is >20% = BLOCKER; 16% clears it with 1 rubric of headroom. |

---

**0 BLOCKER · 2 MAJOR (≤2) · 5 MINOR · Lens-6 Bucket_1_Risk 16.0% (≤20%) · injection difficulty ~4.2/5 (≥3.5) · Opus density PASS, Gemini THIN (accepted with documented justification and delivered 4-write mitigation).**

This deliverable set survived adversarial reading. Every identifier was re-derived from source rather than accepted from a prior council; the answer-leakage scan was run twice by two different methods and is clean; all four levers plus the reserve trace prompt→OE→rubric→atom; every tool-parameter binding is correct against the catalog; and the single most contestable judgment in the task (the twin `$85` charges) resolves uniquely under the prompt's own stated rule with five converging discriminators, one of which — the "Internal labor charge for" template appearing on exactly two records universe-wide, both of them the twin bills — I verified programmatically.

VERDICT: PASS

---

## ADDENDUM — operator actions applied after the council returned (2026-07-25)

Verdict stands at **PASS**. The runbook's `<= 20% Bucket_1_Risk` policy is "fix where cheap, ship if expensive"; all four Lens-6 flags and the MAJOR-2 disclosure were cheap, so all five were applied in place. Re-verified: `validate.py --phase all` PASS, `--phase injection` PASS, `--phase submission_gate` PASS after the edits.

### Pre-council deterministic FAIL fixed by the operator (before the council ran)
`validate.py --phase submission_gate` initially returned **4 FAILs** — Evals_starpm/5 defect family **F5 NEEDS_TOOL_OUTPUT** (spec rows 19-21: "criterion checks 'tool returned success'"). Rubrics 9 / 15 / 18 / 23 (1-indexed) each closed their `evidence` with "and confirm the tool returned a success response", which the judge cannot verify from call arguments. All four were rewritten to grade from call arguments only ("whose arguments target / carry / post to ..."). Gate now 0 fails.

### Lens-6 hardening fixes applied (4)
| Rubric (0-idx) | Anti-pattern | Change |
|---|---|---|
| `rubric[4]` deep clean $387 | affirmative "no variance" assertion demanded | evidence now accepts a reconciliation carrying $387 unchanged, "does not have to use the word matches" |
| `rubric[19]` email repaint | AND-bundle with no disjunction (inconsistent with `rubric[2]`) | `$200` promoted into the **criterion** (mirrors `rubric[2]`), evidence accepts "raised by $200" as the alternative |
| `rubric[21]` email closure | beyond-prompt-literal against "a short note" | evidence broadened to "closed or finalized ... or that no further owner charges are outstanding" |
| `rubric[24]` channel supersession | criterion stricter than its own evidence | criterion demotes `$1,622` to a parenthetical grounding; evidence accepts naming the figure OR referring to the original owner summary |

`rubric[19]`'s first rewrite (disjunction in evidence only) tripped a fresh validator WARN — *"evidence contains amounts NOT in criterion: ['$200']"*, the same evidence-stricter-than-criterion rule Lens 6 polices. Corrected by moving `$200` into the criterion so the judge grades it first. Warn cleared.

### MAJOR-2 disclosure applied (1)
`rubric[7]` (keep the $85 closet trim on the owner side) evidence now carries the corroborating split from the summary email — verified verbatim at FINAL from `gmail.gmail_messages.json` id `5101c5a41dffa90a`: *"Pete Donovan finished the interior repaint (including a touch-up on the bedroom closet trim that came out of our QC walkthrough), and Tony's team handled all internal repairs in-house."* This is the fourth converging discriminator and it is now visible to the judge.

### MAJOR-1 — no artifact change, carry-forward recorded
The L2-yield caveat was **not** fixed by editing the prompt (removing the reconciliation ask would cost Feasibility/Clarity). It is recorded as an S4 scoring watch-item in `_aux/Hardness_Plan.md` under "FINAL-council carry-forward", re-attributing the expected sweep to L6/L11.

### Operator-independent re-verification of council claims
- `"Internal labor charge for"` census over the raw universe: **exactly 2 hits**, `Carlos Mendez` and `Tony Reyes` — both $85 bills. Confirms OE 19's "separates nothing" argument.
- `$1,340` money hits in Gmail: only `4a20c7c433db278a` (rent rate) and `6f2669a41401485a` (Reyes Plumbing total). Slack `1340` hits are hash-id substrings. Confirms the L2 surface.
- `1812` in the universe: 17 raw hits, **all** timestamp / `history_id` / `internal_date` substrings; zero as money. `190` as money: zero. Leakage clean.
- All four 4C bills, invoice `445653930748` (`sync_token` `"0"`, TotalAmt 1622.0, lines 387/1140/95), and both Airtable rows re-read from `_aux/Universe_Split/` and matched to OE 3/4/11/13/14/15/17/18 verbatim.
- All write-tool parameter lists re-extracted from `StarPM_Base_Universe/7_Server_Tools_Details.json`: `update_invoice(id, SyncToken, properties)`, `update_records_for_table(baseId, tableId, records)`, `create_draft(... body ...)`, `slack_send_message(channel_id, message)`, `search_records(baseId, table, query)` vs `list_records_for_table(baseId, tableId, recordIds)`, `get_table_schema(baseId, tables)`, `get-bill(id)`, `read_invoice(invoice_id)`. All OE bindings exact.

**Post-addendum verdict: PASS — cleared for platform upload (6 Opus 4.8 runs + 6 Gemini runs).**

---

## ADDENDUM 2 — platform QC atomicity challenge, adjudicated (2026-07-25)

A reviewer-side check returned `Rubrics Atomicity: FALSE`, naming four criteria as non-atomic. Adjudicated against the three governing spec surfaces. **Verdict: 3 of 4 rejected on the merits, 1 accepted for a different reason than given, plus 1 genuine stack the check missed.** Re-ran all 5 gates after the edits: PASS.

### Governing rule (all three surfaces agree the test is INDEPENDENCE, not value count)
- `Docs_starpm/8_QC_Spec_Doc2.md` (Criteria Not Atomic, 05/22): *"Acceptable bundling (NOT a violation): Outcome rubrics may bundle tightly coupled facts from the same source ... Name + company + city are all attributes of the same relocation record and would be right or wrong together."*
- `Docs_starpm/3_Rubrics_V3_One_Pager.md:126`: *"Bundle only when two facts come from the same tool call or the same data record and would fail together."*
- `Docs_starpm/12_Always_Failing_Rubrics.md:20`: *"If the rubric checks two or more facts that can independently pass or fail ..."*
- `Docs_starpm/2_Rubrics_V3_Guidelines.md:500` (Mistake 6, Stacked Rubrics): *"Split independent claims."*

Every formulation gates on independence / co-failure. None gates on how many values a criterion names — the spec's own accepted example carries three attributes.

### Claim 1 — rubric[0] "reports ... to Linda Castillo as $1,812" — REJECTED as atomicity, ACCEPTED as phrasing
"to Linda Castillo" was a possessive scope qualifier (WHOSE pass-through), not a delivery recipient — necessary disambiguation given OE 9's near-miss customers `proj-f6f9edfeae5c` (Pete Donovan) and `proj-e576b03e2b4c` (John Castillo). The evidence grades the final response to Carlos, not a message to Linda; delivery to Linda is graded separately at rubric[18]. So there was never a second action bundled in.
**But the reviewer's misreading is the point:** "reports X to Y as Z" is grammatically ambiguous and a judge could take Y as a recipient. Retitled to remove the ambiguity at zero cost: **"The Agent reports $1,812 as the corrected owner pass-through on Linda Castillo's Mesa Vista 4C make-ready."**

### Claims 2 / 3 / 4 — the variance criteria (rubric[2], rubric[3], rubric[19]) — REJECTED
Each states **one variance finding**, not three claims.
- **Arithmetic identity.** 1340 − 1140 ≡ 200; 95 − 85 ≡ 10. The difference cannot be wrong while both sides are right, so it is not an independent fact. Only two values carry information, and they are the two sides of a single comparison.
- **Co-failure holds in both directions.** Miss AP bill `696089964235` (the flagship lever) → the Agent reports the repaint as 1,140 → every facet fails together. Open it → both sides are in hand from the same reconciliation → every facet passes together. That is the spec's stated test, and the 07/16 example makes the principle explicit: *"if Y was not found, whether or not this was split, the criteria would fail together."*
- **A variance is inherently relational.** "Atomic" cannot mean one number per criterion, or no reconciliation rubric could ever be written — and reconciliation is the entire task category.
- **Splitting would manufacture a free-pass rubric.** "The Agent identifies the invoice line as $1,140" passes on the mandatory `read_invoice` call that five other rubrics already depend on. Zero discriminative power, and dilution of the threshold math that `AGENTS.md` adds absolute-count gates to prevent.
- **The one legitimate residue was already closed at FINAL.** A strict judge failing "$1,340, up $200" for not restating $1,140 is the AND-bundling risk Lens 6 flagged; all three carry a disjunctive escape in `evidence` ("...or for the $200 shortfall on that line").
**Action:** no structural change. `justification` on all three now cites the acceptable-bundling rule and the co-failure test explicitly, since that field exists to explain build choices to reviewers.

**Honest note on the one real tension:** $1,340 (`get-bill`) and $1,140 (`read_invoice`) are separate tool outputs, and the 03/04 general rule says components from separate tool outputs should not be grouped. That rule operationalizes the co-failure test rather than replacing it, and the $1,140 side is not an independent *discovery* — it is the baseline claim under test, produced by a read every trajectory must perform. The finding being graded is the variance, produced by one comparison.

### MISSED BY THE CHECK — rubric[13] was genuinely stacked, now fixed
Old title: *"The Agent does not create a second owner invoice for the Mesa Vista 4C make-ready, **amending the existing 2026-534 instead**."* That is a negative claim plus a positive claim, and the positive duplicates rubric[8] ("The Agent updates the existing Mesa Vista 4C owner invoice 2026-534"). Textbook Mistake 6 shape, and unlike the variance criteria the two halves genuinely can fail independently.
Retitled to the pure negative: **"The Agent does not create a second owner invoice for the Mesa Vista 4C make-ready alongside the existing 2026-534."** Lossless — the amend was already graded at rubric[8], and the evidence's gating clause is unchanged.

**Post-adjudication: 25 Outcome / 0 Process · all 5 gates PASS · VERDICT: PASS stands.**

---

## ADDENDUM 3 — atomicity challenge, second pass: ADDENDUM 2 PARTIALLY REVERSED (2026-07-25)

The reviewer check returned `Rubrics Atomicity: FALSE` a second time, narrowed to two criteria (rubric[2] and rubric[19], platform #3 and #20), with a materially stronger argument than the first pass. **On re-reading the spec, the reviewer is right and ADDENDUM 2's defense of those criteria was wrong. Reversed and fixed.**

### Where ADDENDUM 2 erred
ADDENDUM 2 argued the co-failure test governs and that the same-source rule "operationalizes the co-failure test rather than replacing it." Re-read of `Docs_starpm/8_QC_Spec_Doc2.md` (Criteria Not Atomic, 05/22) shows that is not what the spec says. Verbatim:

> *"Acceptable bundling (NOT a violation): Outcome rubrics may bundle tightly coupled facts **from the same source**: 'The final response lists Noah Fitzgerald (GreenStack Solutions) relocating to Seattle.' Name + company + city are all attributes of **the same relocation record** ... General rule (03/04): Assessment of multiple components within one tool output can be grouped. **Components from separate tool outputs should NOT be grouped.**"*

The carve-out is explicitly scoped to one source / one record, and the general rule is explicitly prohibitive across sources. The reviewer's distinction is exactly right: name + company + city are attributes of ONE record, whereas $1,340 (`get-bill` on `696089964235`) and $1,140 (`read_invoice` on `445653930748`) are values from TWO records reached by two different calls. ADDENDUM 2 argued around an explicit rule instead of applying it. The `07/16` example points the same way for email content: *"The email mentions the storm, provides the new city, and includes flight details." → three rubrics (unless all come from the same tool output).*

### Fix applied — tighten to one source-value per criterion, do NOT split into three
Splitting into three would have created the free-pass rubric problem ("the Agent identifies the invoice line as $1,140" passes on the mandatory `read_invoice` every trajectory makes). The correct remedy is narrower: each criterion now carries the **single value read from the single bill**, with the invoice-side figure and the derived delta demoted to `evidence` as explicit judge grounding, marked "not an additional required token."

| # | Old title | New title |
|---|---|---|
| 3 | "...repaint as $1,340 on the vendor bill against the $1,140 charged on Linda Castillo's invoice, a $200 understatement." | **"The Agent identifies the Mesa Vista 4C interior repaint on the vendor bill as $1,340."** |
| 4 | "...closet trim touch-up as $85 on the vendor bill against the $95 charged on Linda Castillo's invoice, an overstatement of $10." | **"The Agent identifies the Mesa Vista 4C bedroom closet trim touch-up on the vendor bill as $85."** |
| 20 | "...the interior repaint was $1,340 rather than the $1,140 she was originally billed, a $200 increase on that line." | **"The Agent states in the email draft to Linda Castillo that the interior repaint was $1,340."** |

**#4 was fixed although the reviewer dropped it this round.** It is the identical shape to #3 (two records, derived delta); the second pass flagging #3 but not #4 is an inconsistency in the check, not an exoneration. Fixing only what was flagged would guarantee a third round.

### Nothing lost from the graded set
- $1,140 is still graded, at #11 (the repaint line the write has to raise).
- $95 is still graded, at #12 (the closet trim line the write has to lower).
- The variance itself is still graded, at #2 (the $1,622 verdict) and #6 (the $190 net understatement).
- Discrimination on the flagship lever is fully retained: #3's evidence keeps the hard fail-guard *"a response that reports the 4C repaint as 1,140 fails."*
- The Lens-6 AND-bundling risk previously logged against rubric[19] is now structurally eliminated rather than mitigated by a disjunction. **Bucket_1_Risk drops from 4/25 (16.0%) to 3/25 (12.0%).**

### #11 and #12 deliberately NOT changed
"...raises the interior repaint line ... **from $1,140 to $1,340**" survives the atomicity test on a principled distinction: these are **write-state** criteria. The judge grades one value, the post-state in the `update_invoice` line array. The "from" value is the universe pre-state, which the Agent never asserts and which therefore cannot independently pass or fail. Spec test — *"if this criterion fails, is there exactly one clear reason why?"* — yes: the amended repaint line is not $1,340. Flagged here as the residual exposure if a later reviewer pattern-matches on "two dollar figures in a title."

### Regression caught during the fix
The first rewrite tripped 3 fresh `Eval5 P5 NEEDS_TOOL_OUTPUT` FAILs because the new `justification` text contained the literal phrase "tool output" while explaining the spec rule. `TOOL_OUTPUT_DEP_RE` matches that token anywhere in the rubric blob. Reworded to "a single call"; gate back to 0 fails.

**Post-reversal: 25 Outcome / 0 Process · all 5 gates PASS (`all`, `injection`, `submission_gate`) · rubric WARNs 34 -> 27 · VERDICT: PASS stands.**

---

## ADDENDUM 4 — atomicity challenge, third pass: reasoning rejected, remedy applied anyway (2026-07-25)

Third `Rubrics Atomicity: FALSE`, this time on rubric[24] (platform #25), the channel supersession criterion. **The stated reasoning is wrong. The residual title risk it points at is real, and the fix was applied for consistency with ADDENDUM 3.**

### The reasoning is wrong — the check misread the evidence field
It quoted *"a post that names the earlier figure or refers to it as the figure in the original owner summary both satisfy this criterion"* as proof of bundling. That sentence is a **disjunction that makes naming the amount optional**, which is the opposite of a bundle. The criterion never required the Agent to produce `$1,622`; the evidence had already made the amount discretionary since the ADDENDUM 1 Lens-6 fix.

### The residual risk is real
`$1,622` still sat in the criterion as a parenthetical, and judges grade the criterion first. That is the same "criterion-stricter-than-evidence" defect Lens 6 logged against this exact rubric in the original FINAL run. This is the **second independent pass to land on this line**, which is signal regardless of the argument used to get there. Fixed with the identical remedy applied to #3 / #4 / #20: the parenthetical is removed from the title and the amount is carried in `evidence` marked "grounding for the judge and not an additional required token."

**New title:** *"The Agent states in the channel message that the corrected Mesa Vista 4C figure supersedes the figure Linda Castillo was originally billed."*

The criterion is still self-contained and gradable on its own: the judge asks whether the post flags the corrected figure as replacing the earlier one. The identity of the earlier amount is not needed to answer that. **Bucket_1_Risk drops 3/25 (12.0%) -> 2/25 (8.0%).**

### The check's "all other criteria are atomic" is accepted, with one distinction recorded
rubric[10] and rubric[11] (platform #11 / #12) keep two dollar figures in their titles ("raises ... from $1,140 to $1,340", "lowers ... from $95 to $85") and remain correct as written. The governing distinction, which also explains why #25 had to change:

| | Producible elements in the criterion | Ways it can fail | Verdict |
|---|---|---|---|
| #25 (before fix) | supersession language **and** the amount, both Agent-authored message content | two | non-atomic, fixed |
| #11 / #12 | one, the post-state amount in the `update_invoice` line array | one | atomic, unchanged |

On #11 / #12 the "from" value is universe **pre-state**. The Agent never asserts it and cannot get it wrong, so it cannot contribute an independent failure. Spec test — *"if this criterion fails, is there exactly one clear reason why?"* — yes: the amended repaint line is not $1,340. A criterion is non-atomic when it demands two things **the Agent must produce**, not when it names a fixed fact that locates the thing being graded.

**Post-fix: 25 Outcome / 0 Process · all 5 gates PASS · rubric WARNs 27 -> 26 · Bucket_1_Risk 8.0% · VERDICT: PASS stands.**

---

## ADDENDUM 5 — fourth pass: one stale finding, one invalid overlap finding (2026-07-25)

### Finding 1 (atomicity, rubric[24] / platform #25) — STALE, already fixed in ADDENDUM 4
The check quotes the title as *"...originally billed **(the $1,622 on invoice 2026-534)**"*. That parenthetical was removed in ADDENDUM 4; the local title has read *"...supersedes the figure Linda Castillo was originally billed."* since then. The check is reading a platform copy that has not been re-synced. **No action beyond uploading the ADDENDUM 4 text.**

### Finding 2 (overlap, rubric[9] / platform #10 vs #11+#12+#13) — INVALID, decisive counter-example
Claim: "if criteria 11, 12, and 13 all pass, then the total IS $1,812, so criterion 10 is automatically satisfied."

**That is false, and the task's own designed decoy is the counter-example.** An Agent that amends the invoice to four lines, keeping the three graded lines correct and adding the 85 internal condition walk:

| Line | Amount | Line criterion |
|---|---:|---|
| Deep clean | 387 | #13 **PASSES** |
| Interior repaint | 1,340 | #11 **PASSES** |
| Closet trim | 85 | #12 **PASSES** |
| Condition walk (must not be here) | 85 | not graded by any line criterion |
| **Receivable total** | **1,897** | **#10 FAILS** |

All three line criteria pass; #10 fails. The aggregate is the only place on the **write** where the 1,897 path is caught, and 1,897 is one of the two designed wrong answers in `_aux/Hardness_Plan.md` (Stump Hypothesis prediction 3). The check actually noticed the fourth-line clause and dismissed it as *"grounding/evidence text, not the core criterion title"* — but the title reads *"so that it **totals** $1,812"*, and a four-line invoice totals 1,897, so the title itself fails. The dismissal is what is wrong, not the criterion.

The implication does not hold in the other direction either, which the check derived correctly before setting it aside: lines of 1,350 / 75 / 387 also total 1,812, so #10 can pass while #11 and #12 fail. Neither direction implies the other; both have concrete counter-examples in this universe.

**On the check's fallback ("the no-fourth-line aspect is arguably covered by criterion 7"):** #7 grades the **final response** (the Agent's stated reasoning that the condition walk is excluded); #10 grades the **write** (the invoice end state). An Agent can state the exclusion correctly and still write the charge onto the receivable. This is the same different-surfaces principle the check applied correctly to exonerate six other pairs in its own analysis (#19 vs #24, #3 vs #11, #3 vs #20, #6 vs #21, #1 vs #19 vs #24, #9 vs #10); it was abandoned only here.

**Action taken:** no structural change. rubric[9]'s `justification` now states the non-redundancy with both counter-examples, since that field exists to explain to reviewers why a criterion is present. The title was deliberately NOT amended to something like "totals $1,812 across three lines" — that would add a second graded element and trip the atomicity check, which pulls in the opposite direction from the overlap check.

### Watch-item recorded for a possible fifth pass
If an overlap pass challenges **#2 vs #6** (the "$1,622 does not line up" verdict vs the "$190 net understatement" figure), the defense is that #2 carries a FAIL clause #6 does not reach: *"Fail a response that concludes her charges hold up, or that reports the pass-through as $1,622 and logs 4C closed on that basis."* That is the L1/L10 latching failure mode, and an Agent can miss the netting while still being caught by it. #2 passes independently of #6 and is not a partial restatement of it.

**Post-adjudication: 25 Outcome / 0 Process · all 5 gates PASS · Bucket_1_Risk 8.0% · VERDICT: PASS stands.**
