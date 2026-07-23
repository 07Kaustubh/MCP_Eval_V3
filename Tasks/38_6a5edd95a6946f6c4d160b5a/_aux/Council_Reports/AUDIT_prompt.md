# AUDIT — Prompt Phase (STRICT Veteran QC, S1.5 iter-2 re-audit, POST F1 retarget)

**Task:** Tasks/38_6a5edd95a6946f6c4d160b5a
**Deliverable:** 5_Prompt.txt (S1.5 iter-2, Airtable retarget applied to Item 2 write)
**Universe:** starpm (Star Property Management, San Antonio TX)
**Universe today:** 2026-07-01 (Wednesday, America/Chicago)
**Persona:** Brooke Phillips (p_000, Apartment Property Supervisor · BF 2 Portfolio Coord & Owner Relations)
**Auditor:** Veteran QC — STRICTEST interpretation (5/5-only, every "should" → "must", every validator WARN listed, StarPM V4 density floor 40+)
**Audit date:** 2026-07-22
**Trigger:** S1.5 iter-2 unconditional MANDATORY AUDIT — iter-1 AUDIT returned PASS (STRICT) but MISSED a defect that iter-1 Council A caught (Ridgeview Linear issue non-existence). Iter-2 fix: Item 2 write retargeted from Linear to Airtable maintenance record. This audit OVERWRITES iter-1 AUDIT_prompt.md.

**Delta from iter-1 (self-critique on the miss):** Iter-1 Lens 3 asserted "L11 TRIGGERED" and "L8 TRIGGERED" via cited prompt sentences but did NOT verify the write TARGET existed in universe. Iter-1 Lens 5 checked persona-scope fit for each ask but did NOT independently query `linear.linear_issues.json` for a Ridgeview/roof/Finley/Big Bend match. Both lenses stayed at the semantic level ("agent must find the Linear issue for Ridgeview") and never asked the ledger question ("does that Linear issue exist"). Iter-2 hard-fixes this by requiring per-write-target universe grounding at Lens 3, mirroring the atom-evidence table pattern from Lens 1.

---

## LENS 1 — Strict QC scoring (per-atom evidence table)

Reading `Docs_starpm/7_QC_Spec_Doc1.json` under Brooke, 5/5-only.

**SUB-DIM Unique Ground Truth → 5/5.** Three items converge on single end-states: (a) SR 208B AC = compressor failure per Alamo HVAC email; Tony's clogged-filter Slack is L9 discardable evidence; (b) Ridgeview owner exposure = $8,400 net (not $16,800 gross double-count) with $640 partial + outstanding balance; (c) Tanya's current unit resolved via Airtable-timeline freshness + Slack C003 + QB customer triangulation. All write targets are single ("the maintenance record", "#maintenance", "a Gmail to Aurora" — definite articles resolve unambiguously given the topic-sentence disambiguation of each item). What iter-1 missed: nothing on UGT specifically; L6 Tanya call remains the softest UGT — carries forward as WATCH-OUT #2.

**SUB-DIM Feasibility → 5/5.** All services present in StarPM catalog per `StarPM_Base_Universe/7_Server_Tools_Details.json` (airtable, slack, gmail, quickbooks, contacts, linear-read, hubspot, gcalendar). 3 writes + 5-hop chain feasible under one-session Opus 4.8 within Brooke persona.

**SUB-DIM Explicit Tool Mention → 5/5.** Zero MCP tool identifiers. "Slack", "#maintenance", "Gmail" are colloquial. No `slack_send_message` / `airtable_update_records` / `create_draft` / `save_issue` string hits.

**SUB-DIM Prompt Clarity & Specificity → 5/5.** Each item names artifact + write action + target. All reasonable readings converge on same write set: Airtable MT-2026-063 update + Slack #maintenance post + Airtable Ridgeview maintenance-record update + Gmail draft to Aurora. Iter-2 retarget REMOVES the prior clarity risk (Linear-issue write target was under-specified because no such issue existed).

**SUB-DIM Contrived / Unnatural → 5/5.** End-of-week pre-departure brief to President. Direct/organized/coaching Brooke voice. No numbered steps, no format constraints, no arbitrary precision.

**SUB-DIM Alignment with Today's Date → 5/5.** Today = 2026-07-01. "Thursday" resolves to 2026-07-02 (matches Tony's C001 post ts=1782914700 on 2026-07-01 planning Thursday PM rounds). "before I leave" = end-of-day today. No forward/past inversion.

**SUB-DIM Truthfulness → 5/5.** Per-atom re-verification against `_aux/Universe_Split/` (re-queried this audit, NOT trusting prior council):

| Atom asserted / presupposed | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Aurora (recipient, President) | `contacts.contacts` | first_name=Aurora, last_name=Winona, email=aurora.winona@starpm.com, title=President | GROUNDED |
| Brooke Phillips (author, is_user=true) | `contacts.contacts` + `StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md` L117-139 | brooke.phillips@starpm.com, Apartment Property Supervisor, is_user=true, U9741B657FE | GROUNDED |
| Sunset Ridge 208B AC ticket | `airtable_records` tblMaintenanceTickets `rec7f6e5d4c3b2a1e` | fldTicketNumber=MT-2026-063, desc="Sunset Ridge Unit 208B -- tenant reports no AC. Tony Reyes on-site assessment: dirty filter caused unit to trip. Scheduled for Thursday PM rounds." | GROUNDED |
| Tony (Reyes) Slack post on 208B | `slack_messages` C001, user UD4432C1F56 (tony.reyes), ts=1782914700, thread_parent=null | "Swung by 208B on Sunset Ridge this morning. Dirty filter tripped the unit, nothing serious. Got her penciled in for Thursday…" | GROUNDED |
| #maintenance = C001, public | `slack_channels` | id=C001, name=#maintenance, is_private=False | GROUNDED |
| Alamo HVAC inspection thread (L9 landing) | `gmail_messages` | 1 hit "Alamo", 1 hit "compressor" (per S1_A + S1_B verifications) — thread subject "HVAC Inspection Findings - Sunset Ridge Unit 208B" from service@alamohvac.com | GROUNDED |
| **Ridgeview roof maintenance record (Item 2 retarget target)** — NEW verification for iter-2 | `airtable_records` tblMaintenanceTickets `recb4aeaed326f156` | fldTicketNumber=MT-2026-047, fldPriority=selHigh, desc="Top-floor unit at Finley portfolio property showing missing shingles and interior ceiling water staining - roof damage appears to exceed routine patching and requires professional evaluation. Flagged by Lisa Smith for priority assessment and licensed roofing contractor inspection." | **GROUNDED** — write target now exists (fix confirmed effective) |
| Ridgeview roof make-ready mirror | `airtable_records` tblMakeReady `rec8b679d92f30753` | fldUnit="Ridgeview - Roof Section (Common/Structural)", fldNotes2="Owner authorization received from Robert Finley for structural roof repair. Pete Donovan assigned as approved vendor following owner sign-off on the $8,400 estimate. Ticket updated to reflect approved status and vendor assignment…" | GROUNDED (second real record — see WATCH-OUT #3 below on which Airtable record the OE targets) |
| Robert = Robert Finley (Ridgeview owner) | `contacts.contacts` | first_name=Robert, last_name=Finley, email=robert.finley@gmail.com, job=Property Owner | GROUNDED |
| $8,400 approved scope + $640 partial payment | Fact_Ledger amounts | "8400.00" + "640.00" both present; Hardness_Plan L8 chain traces to QB bills 2026-481 / PD-2026-084, invoice 2026-494, payment 972286822645 | GROUNDED |
| Tanya Mitchell (escalation subject) | `contacts.contacts` + `airtable_records` tblMakeReady multi-row set (rec769c9f03f0b85f, rec8005502043b755, rec91517a5acab558, recc83c05d889b354) | tanya.mitchell@gmail.com; escalation timeline 2026-06-12 → 2026-07-01 | GROUNDED |

**Iter-1 escape pattern closure:** The strict "does the write target exist" row is now table-mandatory. Zero unverified write targets remain.

**SUB-DIM Tool Use & Cross-service → 5/5.** ≥6 services required: Airtable, Slack, Gmail, QuickBooks, contacts, Linear (read: SR 208B mirror). Not single-service.

**SUB-DIM Investigation → 5/5.** Investigation cues non-preemptive ("Check what the current status really is", "Figure out what the real owner exposure is", "confirm her current status and the unit reference"). Root causes not disclosed. Tony's dirty-filter framing planted as anchor, not stated as truth.

**SUB-DIM Coherence (Bolt-on) → 5/5.** Validator emitted 2 bolt-on WARNs (Tony sentence + $8,400 sentence — note iter-2 dropped from 3 WARNs to 2 because Item 2's third-WARN sentence changed with the retarget). Remove-sentence test at paragraph level:
- Tony sentence: removing kills L9 anchor + orphans "but I want to know what actually came back" contrast → LOAD-BEARING.
- $8,400 sentence: removing kills L11 anchor + orphans "but when I tried to pull the actual billing picture didn't come out clean" contrast → LOAD-BEARING.
Both WARNs are heuristic false positives (named-entity overlap heuristic misclassifies multi-item briefs). Coherence spine = enumerating framing sentence + shared Aurora recipient + shared final Gmail write.

**SUB-DIM Persona → 5/5.** Brooke's `owner_capex_approval_roof` (leads, 8 actions) + `owner_portfolio_review_midyear` (leads, coordinates with Aurora Winona) + `property_ops_weekly_cycle` + escalation-target role cover all 4 asks. Empirically corroborated: 15 direct C001 posts on record + owns the Ridgeview roof approval thread. Aurora briefing is her signature workflow.

**SUB-DIM Business Function → 5/5.** BF 2 Portfolio Coord & Owner Relations. Cross-portfolio brief to President = exact category match. Not BF 1 (Onsite PM territory).

**LENS 1 verdict: 12/12 at 5/5. PASS.**

---

## LENS 2 — Answer-leakage sweep (iter-2 re-scan of revised prompt)

Prompt string-search (case-insensitive):
- `compressor` → 0 hits ✓
- `Alamo` / `alamohvac` → 0 hits ✓
- `$16,800` / `16800` / `16,800` → 0 hits ✓ (naive-sum wrong answer not planted)
- `$640` / `640` → 0 hits ✓
- `Las Palmas` / `4B` / `Unit 14` → 0 hits ✓
- `2026-481` / `2026-494` / `PD-2026-084` / `972286822645` → 0 hits ✓
- `pass-through` / `pass through` → 0 hits ✓
- `credit memo` / `CM-2026-0095` → 0 hits ✓

Arithmetic-neighbor scan for $8,400 anchors: prompt frames $8,400 explicitly as Brooke's TENTATIVE anchor ("I've been working off the '$8,400 approved scope'…"), not as the answer. L11 correctness requires the agent to affirm this figure is the net (not double it).

Read-side artifact leakage: Tony's C001 post contains "clogged filter" + "Thursday" (WRONG anchor for L9 to work — intentional). Alamo HVAC Gmail contains "compressor" (agent-DISCOVERABLE ground truth — the L9 landing zone). QB PrivateNote fields hold the pass-through disambiguation (L2 structured-DB skip zone). No single conversational surface leaks the correct net figure. Airtable Tanya rows conflict by design (L6 landing).

**LENS 2 verdict: 0 BLOCKERS.** No exact-figure or state leaks.

---

## LENS 3 — Hardness end-to-end trace + PER-WRITE-TARGET universe verification (iter-1 escape closure)

### Write action → tool → target existence table (NEW mandatory check)

| # | Prompt sentence | Write tool (per `7_Server_Tools_Details.json`) | Specific target | Universe row | Verdict |
|---|---|---|---|---|---|
| W1 | "update the maintenance record with it" (Item 1) | `airtable_update_records` (verified in catalog) | Airtable tblMaintenanceTickets, row for SR 208B AC | `rec7f6e5d4c3b2a1e` / MT-2026-063 | **EXISTS** |
| W2 | "drop a note in #maintenance" (Item 1) | `slack_send_message(channel_id=C001, message=…)` (verified — note param is `message`, NOT `payload`; StarPM-specific per registry) | C001 (#maintenance, public) | `slack_channels` id=C001 | **EXISTS** |
| W3 | "update the maintenance record on it with the current status" (Item 2 — RETARGET) | `airtable_update_records` (verified) | Airtable Ridgeview roof record — either `recb4aeaed326f156` / MT-2026-047 (tblMaintenanceTickets, Finley portfolio roof) OR `rec8b679d92f30753` / tblMakeReady "Ridgeview - Roof Section" | **BOTH EXIST** (see WATCH-OUT #3 on rubric-time disambiguation) |
| W4 | "draft a Gmail to Aurora with the full update" (Item 4) | `create_draft(to=[…], subject, body)` (verified — StarPM Gmail is DRAFT-ONLY per registry; `body` param, NOT `content`) | aurora.winona@starpm.com | `contacts.contacts` | **EXISTS** |

Every write action names an existing tool and an existing target. **Iter-1's specific miss (W3 pointing to a non-existent Linear issue) is CLOSED.**

### Lever-by-lever preservation under the retarget

**L9 (Authority-figure dismissal) → TRIGGERED.** Sentence: *"Tony told me on Slack it's probably a clogged filter and he'd get someone in Thursday, but I want to know what actually came back from the inspection before I report anything."* Tony's C001 post is discoverable via channel scan; Alamo HVAC formal email requires Gmail search. Retarget does NOT touch Item 1 — L9 unaffected.

**L11 (Net-vs-gross framing) → TRIGGERED, IMPROVED.** Sentence: *"I've been working off the '$8,400 approved scope' from the back-and-forth with Robert, but when I tried to pull the actual billing picture it didn't come out clean. Figure out what the real owner exposure is on that job and update the maintenance record on it with the current status once you have it."* The retarget is a NET POSITIVE for L11: writing the "current status" to the Airtable maintenance record REQUIRES the agent to actually derive the net owner exposure ($8,400 gross vendor spend, $640 partial paid, balance outstanding) — the write forcing-function on-chain is stronger than a Linear generic-issue update would have been. Prior Linear write was off-chain (agent could write "reconciliation in progress" without deriving numbers); Airtable maintenance-record status update requires the actual reconciled state.

**L2 (Structured-DB skip) → TRIGGERED, IMPROVED.** Same sentence. Pushing the write target ONTO the L8 chain (Airtable is hop 1-2 of 5) means the agent must traverse hops 3-5 (QB bills → invoice → payment + PrivateNote read) to know WHAT status to write. Prior Linear write let the agent bypass QB entirely.

**L8 (Multi-link chain) → TRIGGERED, IMPROVED.** Sentence same. Chain: Airtable MR `rec8b679d92f30753` → MT-2026-047 → QB bill 2026-481 ($8,400) → QB bill PD-2026-084 ($8,400 pass-through restatement per PrivateNote) → QB invoice 2026-494 ($8,400 owner AR) → QB payment 972286822645 ($640 partial). Now the WRITE TARGET is on the chain — 5 hops required to fill it correctly. Prior Linear write was chain hop-0 (off-chain); retarget puts the write at hop 1-2 forcing chain-completion.

**L6 (Near-miss entity / record-freshness) → TRIGGERED.** Sentence: *"Pull up her make-ready record and confirm her current status and the unit reference on that record."* Airtable Tanya rows: `rec769c9f03f0b85f` (2026-06-12 Las Palmas 4B pre-breach) vs `rec91517a5acab558` (2026-06-28 Unit 14, 3-day notice) vs `recc83c05d889b354` (2026-07-01 Unit 14 JP coordination). Prompt does NOT name unit — verify-and-reconcile ask. Retarget does NOT touch Item 3 — L6 unaffected.

### Retarget net summary

L9 (Item 1): unchanged (STRONG).
L11 + L2 + L8 (Item 2): all THREE IMPROVED by the retarget — write is now on-chain, forcing chain-completion for the write to be correct.
L6 (Item 3): unchanged (STRONG).

**LENS 3 verdict: 5/5 levers preserved end-to-end. Retarget IMPROVES 3 of 5. Every write action has a verified existing tool + verified existing target. NO HARDNESS_REGRESSION. Iter-1 escape pattern closed.**

---

## LENS 4 — Strict density projection under the retarget (StarPM V4 40+ floor)

Density delta from retarget:
- REMOVED: `save_issue(id=…, state_id=…)` on the phantom Linear issue → net -1 Linear write, but Linear reads (SR 208B mirror) remain (Council A grounding confirms Linear issue `Sunset Ridge 208B - HVAC filter issue, Thursday slot` exists — natural Item 1 mirror read).
- ADDED: `airtable_update_records(base_id=…, table_id=tblMaintenanceTickets, record_id=recb4aeaed326f156, fields={…})` → net +1 Airtable write.
- INDIRECT: writing a REAL Airtable status forces agent to derive numbers → +1-2 additional QB reads (PrivateNote confirmation + payment cross-check) that a Linear filler write would have permitted skipping.

Re-projected midpoint:
- Base discovery: 6.5 (unchanged)
- L9 subchain: 4.0 (unchanged)
- L2 subchain: 5.5 → 6.5 (+1 PrivateNote confirmation read forced by real Airtable write)
- L11 subchain: 5.5 → 6.0 (+0.5 payment cross-check forced by real Airtable write)
- L8 chain: 7.5 (unchanged — was already assumed 5-hop; now write forces it)
- L6 subchain: 4.0 (unchanged)
- Writes: 10.5 → 10.5 (net 0: -1 Linear write, +1 Airtable write, wash)
- Cross-service triangulation buffer: 6.5 (unchanged)

**Re-projected: 50.5 midpoint (range 40-62).** Above the StarPM V4 40+ design bar; NOT THIN_DENSITY. Slight net UP from prior 50.0 midpoint because the retarget converts a filler write into a force-function write.

Best-case minimal (competent agent, strictest reading): ~30-32. Realistic (Opus 4.8 broad-then-narrow with cross-verification): 45-52.

**LENS 4 verdict: PASS.** Midpoint ~50.5, comfortably above 40+ StarPM V4 floor. WATCH-OUT #1 preserved: lower-bound (40) is exactly at the floor — S4 trajectory review must flag any run < 40 as density underflow.

---

## LENS 5 — Adversarial veteran review (ITER-1 escape emphasis)

**1. Framing preservation across artifacts.** Prompt uses GOAL framing throughout ("figure out what the real owner exposure is"). No implicit method-lock. Downstream rubric check is out of scope for prompt-phase audit.

**2. Entity-drift seams.**
- Aurora vs Aurora Winona: one match. GROUNDED. Persona brief names "Aurora Winona" as coordination peer.
- Robert vs Robert Finley: one Robert in Ridgeview roof context. GROUNDED.
- Sunset Ridge 208B: canonical "Sunset Ridge 208B" then short "208B" within Item 1 — consistent.
- "the maintenance record" (Item 1 vs Item 2): both items say "update the maintenance record"; disambiguated by TOPIC SENTENCE of each paragraph. Item 1's topic sentence is "The Sunset Ridge 208B AC is where I'm most uncomfortable"; Item 2's topic sentence is "The Ridgeview roof billing is the other one nagging at me". "It" / "on it" refer to the paragraph subject. No cross-item confusion under reasonable reading.
- **NEW iter-2 check:** does Item 2's Airtable-write target uniquely resolve? Two candidate records exist (MT-2026-047 tblMaintenanceTickets = Finley portfolio roof; rec8b679d92f30753 tblMakeReady = "Ridgeview - Roof Section"). Under strictest reading, "the maintenance record" preferentially points to tblMaintenanceTickets (that's what "maintenance record" is called in StarPM). MT-2026-047's description says "Finley portfolio property" not "Ridgeview" by name — mild disambiguation friction because Finley may own more properties. Not a fail because MT-2026-047 is the only tblMaintenanceTickets row where roof + Finley coincide, AND the Hardness_Plan L8 explicitly names MT-2026-047 as the chain hop. WATCH-OUT #3 for OE/rubric.

**3. Tool-name leaks.** Zero hits.

**4. Em-dash / "at least N" / "approximately" near IDs.** Zero. Straight ASCII throughout.

**5. Single-channel lock-in.** Prompt names `#maintenance` for Item 1's Slack post — MINOR at most. `#maintenance` is where Tony posted and where Brooke has 15 prior posts on record; no realistic alternative channel would be rejected. Not a fail.

**6. Per-ask persona-scope fit (empirical re-verification).**
- (a) SR 208B AC ticket + #maintenance post: Brooke has 15 C001 posts on record → PASS.
- (b) Ridgeview billing recon + Airtable maintenance-record update: Brooke's own C001 post ts=1779995737 ("Roof repair at Ridgeview is approved and Pete Donovan is confirmed") empirically ties her to this thread → STRONG PASS.
- (c) Tanya escalation pull: escalation-target role → PASS.
- (d) Aurora Gmail draft: signature scenario coordinates with Aurora Winona → STRONG PASS.

**7. Item 1 vs Item 2 write-ask ambiguity check (NEW per iter-2 emphasis).** Both items now instruct "update the maintenance record". Does each item's opening sentence disambiguate the property/job clearly?
- Item 1 opener: "The Sunset Ridge 208B AC is where I'm most uncomfortable" → binds the paragraph to SR 208B AC. The subsequent "update the maintenance record with it" resolves via anaphora to the SR 208B AC ticket (MT-2026-063). Clear.
- Item 2 opener: "The Ridgeview roof billing is the other one nagging at me" → binds paragraph to Ridgeview roof. Subsequent "update the maintenance record on it" resolves via "it" → "that job" → Ridgeview roof (MT-2026-047 or rec8b679d92f30753). Clear.
- Cross-item confusion risk: near-zero. Different topic sentences, different explicit anchor phrases ("with it" vs "on it with the current status"). Sequential paragraph reading preserves scope.

**LENS 5 verdict: All 7 checks pass under strictest reading. No entity drift, no persona-scope fail, no write-ask ambiguity between Item 1 and Item 2.**

---

## LENS 7 — Anti-rationalization

Re-scan for "I considered flagging X but decided it's fine because…" lines in this audit:

1. **"Two Airtable candidate records for Item 2 (MT-2026-047 vs rec8b679d92f30753) — is this UGT/clarity failure?"** — considered. NOT talked out — WATCH-OUT #3 raised. Not promoted to REVISE because Hardness_Plan L8 explicitly identifies MT-2026-047 as the chain hop AND both records ARE existing universe targets (the risk is downstream rubric-tightening, not upstream prompt failure). Hard exclusion: two-valid-target ambiguity is downstream rubric territory when both targets are semantically equivalent for the write action asked.

2. **"Density lower bound 40 sits exactly at the floor — is this THIN_DENSITY?"** — considered. NOT talked out — WATCH-OUT #1 raised. Not promoted to REVISE because midpoint (50.5) is comfortably above 40+ floor; only pathological lower-bound crosses. Hard exclusion: StarPM V4 density gate is midpoint-based per `Docs_starpm/1`.

3. **"Iter-1 said 12/12 sub-dims at 5/5; iter-2 says 12/12 at 5/5 — am I just cargo-culting iter-1's verdict?"** — considered. NOT talked out. Independently re-verified every atom in the evidence table by re-querying `_aux/Universe_Split/` this pass (specifically MT-2026-047 existence + tblMakeReady rec8b679d92f30753 co-existence — neither was queried in iter-1). Delta from iter-1: added the per-write-target row-existence verification as a Lens 3 hard gate. This audit's PASS is not a copy of iter-1's PASS; it is a re-derivation with the escape-pattern gap closed.

4. **"2 bolt-on WARNs from validator — false positives again, right?"** — considered. NOT talked out. Explicit remove-sentence test applied at paragraph level (see Lens 1 Coherence). Both sentences fail the test → confirmed false positives via test, not via convenience.

5. **"Retarget was minimal (one sentence changed) so nothing else needs re-verification"** — considered. NOT talked out. Every write action re-verified against tool catalog + universe rows this pass, not just the changed Item 2 write. Every hardness lever re-traced. Density re-projected with actual delta math.

Zero findings talked out of. All concerns either resolved with deterministic evidence or promoted to WATCH-OUT.

---

## LENS 8 — Regression anchor verification

`python3 Validators/test_regression_anchors.py` executed during this audit pass.

**Result: 61/61 PASS, 0 FAIL.** Full anchor set including v-wave3 StarPM param-trap anchors (SP-7 slack_send_message `payload` vs `message`; SP-8 create_draft `content` vs `body`) and v-wave4 injection/submission anchors (SP-INJ-1/2, SP-SUB-1/2). No silent validator regression.

---

## VERDICT

**PASS (STRICT)**

Rationale:
- Zero BLOCKER hits (Lens 2 clean).
- Zero Lens-1 sub-dims below 5 (12/12 at 5/5).
- Every hardness lever traces end-to-end with cited prompt sentence + universe evidence (Lens 3).
- **Every write action verified for tool-existence AND target-existence — iter-1's specific escape (non-existent Linear issue) closed** (Lens 3 write-target table).
- Retarget IMPROVES L11 + L2 + L8 chain forcing-function (write now on-chain).
- Density midpoint ~50.5, comfortably above StarPM V4 40+ floor (Lens 4).
- Zero true bolt-ons (Lens 1 Coherence + Lens 5).
- Persona-scope empirically corroborated (Brooke 15 C001 posts + own Ridgeview roof approval thread) (Lens 5).
- Item 1 vs Item 2 "update the maintenance record" is disambiguated by paragraph topic sentence (Lens 5.7).
- Regression anchors 61/61 PASS (Lens 8).

Prompt cleared for S1.5 iter-2 phase exit. OE (`6_Oracle_Events.txt`) and rubrics (`7_Rubrics.json`) already reference Denise per prior councils; the persona propagation to Brooke + retarget propagation to Airtable are downstream S2/S3 responsibilities. Prior `AUDIT_oe.md` and `AUDIT_rubrics.md` must be re-run after those propagations land.

---

## WATCH-OUT NOTES (for downstream phases)

1. **[DENSITY LOWER-BOUND AT FLOOR]** Re-projected range 40-62 (midpoint 50.5). Lower bound sits exactly at StarPM V4 40+ floor. At S4 trajectory review, flag any individual run < 40 as density-underflow candidate; if a cluster of runs THINs out, add breadth via OE granularity.

2. **[TANYA UGT — DESIGN HARDNESS]** Airtable holds conflicting unit labels for Tanya (Las Palmas 4B in `rec769c9f03f0b85f` vs Unit 14 in `rec91517a5acab558` + `recc83c05d889b354`). Slack C003 + QB customer record are the disambiguators. S3 rubric MUST cite the disambiguating sources and MUST NOT accept a defensible-but-wrong alternate unit from Airtable-only paths.

3. **[ITEM 2 AIRTABLE TARGET DISAMBIGUATION]** Two Ridgeview-roof Airtable rows exist: `recb4aeaed326f156` / MT-2026-047 (tblMaintenanceTickets, "Finley portfolio property" desc) and `rec8b679d92f30753` (tblMakeReady, "Ridgeview - Roof Section", $8,400 owner-sign-off note). Hardness_Plan L8 designates MT-2026-047 as the chain hop. S2 OE must NAME the specific record_id target for the Airtable update to preserve unique-write-target; S3 rubric must accept the OE-designated target and reject the other only if the OE-designated one is more canonical for "current status". If both are semantically equivalent for a status update, rubric may accept either — decide at S3.

4. **[DOWNSTREAM PERSONA + RETARGET CASCADE]** Prompt persona is now Brooke; Item 2 write is now Airtable (was Linear). OE + rubrics still reference Denise + Linear per prior councils. Downstream phase MUST propagate: author-of-writes = `brooke.phillips@starpm.com` / `U9741B657FE`; Item 2 write tool = `airtable_update_records` with record_id per WATCH-OUT #3. Re-run AUDIT_oe.md and AUDIT_rubrics.md after propagation.

5. **[MT-2026-047 DESC DOES NOT NAME "RIDGEVIEW"]** MT-2026-047's description says "Top-floor unit at Finley portfolio property" not "Ridgeview" by name. Agent must cross-reference Robert Finley → Ridgeview via `contacts` or Airtable MR row `rec8b679d92f30753`. If Finley owns multiple properties in the universe, an agent might land on MT-2026-047 uncertain of the Ridgeview link. Not a prompt fail (Hardness_Plan L8 confirms this is intentional structural-DB-skip forcing function), but S3 rubric should not require exact "Ridgeview" text on the ticket — the derivation path is Finley → Ridgeview via contacts, not literal ticket text match.
