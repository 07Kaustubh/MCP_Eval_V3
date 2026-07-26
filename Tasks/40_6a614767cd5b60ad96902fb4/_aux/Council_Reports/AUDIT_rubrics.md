# AUDIT — 7_Rubrics.json (veteran QC, strictest interpretation)

**Task:** `Tasks/40_6a614767cd5b60ad96902fb4` · **Universe:** StarPM (V4, confirmed `_aux/Universe.txt`) · **Today:** 2026-07-01 America/Chicago
**Artifact:** `7_Rubrics.json` — 16 Outcome, 0 Process · **Phase:** rubrics · **Mode:** read-only, independent re-grounding (prior council verdicts NOT inherited)
**Reading:** 5/5-only; every "should" = "must"; every WARN = hard issue; every lever traced end-to-end · **Timestamp:** 2026-07-23

## VERDICT: **PASS (STRICT)**

Zero BLOCKER · zero LENS-1 sub-dim < 5 · all 6 catalog levers + all 5 Hardness_Plan levers trace end-to-end · density ≥ 40 per model (StarPM bar). Validator exit 0 (62/62 anchors); all 4 WARNs adjudicated benign-false-positive with cited universe evidence; all 5 NOTEs informational. Three informational watch-notes recorded (non-scoring, no fix required). I independently re-grounded every concrete value in all 16 titles and found no defect the two S3 councils missed.

---

## LENS 1 — Strict QC scoring (Docs_starpm/7_QC_Spec_Doc1.json rubric dimension)

| Rubric sub-dim | Score | One-line reason | Prior-council miss? |
|---|---|---|---|
| Overall Rubric Quality | **5** | Validator: 0/16 Major, 0/16 Moderate, 0/16 any-issue. Independently re-confirmed: 0 Major / 0 Moderate / 0 Minor. Well under thresholds. | none |
| Rubric Category Balance | **5** | 16 Outcome > 0 Process; Process 0% < 50%; Outcome ≠ 0. | none |
| Process Rubrics | **5** | Zero present; three-condition test fails for every candidate (read-before-write, derive-hold-from-notes, trace-breach, open-HubSpot are all captured by Outcome end-states [0][1][2][4][8][12]). Adding any would violate zero-process design. | none |
| Agent-Centric Phrasing | **5** | All 16 titles open "The Agent …" / valid possessive "The Agent's email/message/update/comment …". Tool-name-in-title scan = 0 violations. | none |
| All-Failing Rubrics | **5 (N/A→5)** | Every target reachable + every read-graded literal present in split; re-assessed at S4/verifier stage. | none |
| Atomicity | **5** | Each title = one write-action or one content-judgment. Watch-items [2]/[4]/[8]/[11] resolve to single-write-action coherent-state bundling (see LENS 7); eval's Major "not atomic" trigger is cross-service/cross-action bundling — none present. | none |
| Self-Containment | **5** | Every value embedded (rec-ids, brooke.phillips@starpm.com, $2,132.00, QR-2026-0441, EVF-2026-014, invoice 7214, OPS-32, C004/#make-ready, selSched/selProg/selReady, 07-06/07-07). [0]'s two-id set is a CLOSED named set, not a catch-all. | none |
| Completeness / Coverage | **5** | All 6 prompt asks → rubric; all 5 write OEs → a write-action rubric; all 3 decoys have an exclusion ([0] bars Rio Bend, [8] bars 7214-zero, [9] bars vendor label). No user-facing report gap (prompt routes every finding into a write: "lay it all out in that email … and I will take it from there"). | none |
| Flexibility | **5** | Exact where one grounded truth exists (emails, ids, $2,132.00 literal Balance, EVF/OPS ids, status enums); dual-accept where universe is open ([0] either Sunset Ridge rec id; [13] either 07-06/07-07; [1] status left-unchanged OR explicitly-set). No spurious "approximately"; no "at least N". | none |
| Accuracy / Truthfulness | **5** | Every embedded literal verified against `_aux/Universe_Split/` (per-atom table below). Zero fabricated values. | none |

**Rubric dimension = 5/5 (grade-to-lowest).**

### PER-ATOM EVIDENCE TABLE (required for Accuracy 5/5)

| Atom asserted | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| `recc83c05d889b354` = Sunset Ridge Unit 14 turn (accept) | airtable_records | fldUnit "Unit 14", fldTurnStatus **selSched**, notes "Eviction petition for **Tanya Mitchell** … coordinated with the **Justice of the Peace** — make-ready … cannot begin until … **possession is formally returned**", mod **2026-07-01 11:18:57** (newest) | GROUNDED |
| `reca8230a8fd9ff51` = Sunset Ridge Unit 14 turn (accept) | airtable_records | fldUnit **"Sunset Ridge Unit 14"**, selSched, notes name Tanya + Brooke/Teresa, mod 2026-06-07 | GROUNDED |
| `rec94e86a3007dd5e` = Rio Bend Unit 14 (FAIL target) | airtable_records | fldUnit **"Rio Bend - Unit 14"**, **selReady**, "back to rent-ready condition. Ticket closed out." | GROUNDED (decoy = correct exclusion) |
| selSched=Scheduled / selProg=In Progress / selReady=Ready | airtable_fields | fldTurnStatus singleSelect choices `{selSched:Scheduled, selProg:"In Progress", selReady:Ready}`, tblMakeReady | GROUNDED (both excluded values exist) |
| stale fldMoveOut 2026-05-02 (BC1 not-possession-returned) | airtable_records | recc83c05d889b354 fldMoveOut/fldTargetReady **2026-05-02** contradicts hold note → planning field, NOT possession-return | GROUNDED (trap handled by [1]/[2]) |
| `brooke.phillips@starpm.com` | gcalendar_calendars + QB PrivateNote | calendar id "brooke.phillips@starpm.com" (owner); QB QR-0441 PrivateNote "forwarded to … Brooke Phillips" | GROUNDED |
| `$2,132.00` on bill QR-2026-0441 = Tanya rent arrears | quickbooks_entities id 232176553533 | entity_type **bill**, DocNumber **QR-2026-0441**, **Balance 2132.0 / TotalAmt 2132.0**; 4 lines all "…**Tanya Mitchell, Unit 14**" (847 May arrears + 925 June rent + 210 late fees + 150 plan-credit line); VendorRef **"Alamo HVAC Services"** (decoy) | GROUNDED (amount+tenant exact; vendor is decoy, [9] grades on content) |
| invoice **7214** Balance 0.00 (zero-balance trap) | quickbooks_entities id 283231782926 | entity_type **invoice**, DocNumber "7214", CustomerRef **Tanya Mitchell**, **Balance 0.0**, TotalAmt 8173.44; PrivateNote "**Mitchell account remains delinquent with no cure received**"; linked payment 952690463873 (8173.44) zeroes it | GROUNDED (trap handled by [8]) |
| `EVF-2026-014` owner-approved, in JP coord | airtable_records rec922b9a2d1b9451 (tblMaintenanceTickets) | fldTicketNumber "EVF-2026-014", "Owner authorization received from Linda Castillo … **Owner Approved - Ready to File**", fldCompletionDate 2026-06-30; JP-coordination half in recc83c05d889b354 notes + Brooke Slack | GROUNDED (Fact_Ledger index gap only; split has it) |
| approved ESA on record | hubspot_objects + gmail | ticket_8faab…bae88 status OPEN + ticket_34cb…dd5 status **CLOSED** "Brooke Phillips **approved** the accommodation, Tanya signed ESA lease addendum"; gmail thread 9f2b3cd66c907597 "**approved, effective immediately**" | GROUNDED (approval is the dominant truth) |
| `OPS-32` eviction tracker | linear_issues | id "OPS-32", title "**Eviction Hearing - Mitchell, Harris Property**", number 32, priority 1 (Urgent), state_id state_OPS_2 (In Progress), desc "keep all prep steps … in one place through the conclusion" (master tracker), updated 2026-05-11 (stale) | GROUNDED |
| C004 = #make-ready | slack_channels | id "C004", name "#make-ready" | GROUNDED |
| 2026-07-06 / 2026-07-07 = "early next week" | today_horizon + weekday calc | today 2026-07-01 **Wednesday**; 07-06 **Monday**, 07-07 **Tuesday** | GROUNDED (derived, exact) |

Empty-evidence column count: **0** → Accuracy floor not triggered; Accuracy = 5.

---

## LENS 2 — Answer-leakage sweep

Core "answer" = hold state (account in active eviction / possession not returned / turn stays Scheduled) **+** $2,132.00 arrears. **No single tool read hands the synthesized position.** The disposition is distributed across ≥5 services and multiple contradictory rows:
- Hold requires correlating recc83c05d889b354 notes (possession) **+** rec8005502043b755 (breach) **+** Brooke Slack (JP coordination) **+** rec922b9a2d1b9451 (owner-approved filing) **+** invoice 7214 (zero-but-delinquent). No row states "eviction AND turn-held AND $2,132 AND ESA-approved" together.
- `$2,132.00` lives only on bill QR-2026-0441, gated behind the "Alamo HVAC Services" vendor decoy; not surfaced as a pre-computed arrears total anywhere.
- The stale rec769c9f03f0b85f actively **mis-leads** ("plan active, tenancy continues") — anti-leakage, not a giveaway.

**LENS 2 = CLEAN (no BLOCKER).** No derived figure is leaked; every content rubric requires cross-source synthesis.

---

## LENS 3 — Hardness end-to-end trace (prompt → OE → rubric → grounded atom)

| Lever (Hardness_Plan) | Prompt sentence | OE step | Rubric criterion | Grounded atom | Trace |
|---|---|---|---|---|---|
| L31 possession-not-returned negative directive (Gemini stump, S1) | L1 "we are past the holdup"; L3 "move it forward only as far as facts support" | OE3/OE14 | [1] status stays Scheduled + [2]/[5]/[10]/[15] hold-until-possession | recc83c05d889b354 (in Fact_Ledger ids) + notes | ✅ |
| Delinquency supersession / latching (S2) | L1 "nonpayment side is cleared" | OE4/OE7 | [4] Slack breached-not-active + [8] email delinquent+eviction | rec769c9f03f0b85f vs rec8005502043b755 (Fact_Ledger ids) | ✅ |
| HubSpot ESA structured-DB skip (Opus stump, S3) | L7 "anything still open on it" | OE10/OE11/OE19.5 | [12] approved ESA fair-housing before turnover | ticket_8faab…bae88 + gmail 9f2b3cd66c907597 (split) | ✅ |
| Cross-property Unit 14 near-miss (S4) | L3 "tied to Tanya Mitchell's unit specifically" | OE2/OE14 | [0] target Sunset≠Rio Bend + [7] email disambiguation | recc83c05…/reca8230a8…/rec94e86a3… (Fact_Ledger ids) | ✅ |
| Authority-relayed "cleared" frame (S5, prompt-side L9/L15/L16) | L1 "owner signed off … we are past the holdup" | OE5 anchor rec922b9a2d1b9451 | rebutted by [1]/[2]/[8]/[11] | rec922b9a2d1b9451 "Ready to File" (split) | ✅ |
| invoice 7214 zero-balance decoy | L1 "nonpayment side is cleared" | OE9 | [8] not-resolved-by-7214 | invoice 283231782926 Balance 0.0 (Fact_Ledger id 7214) | ✅ |
| QR-2026-0441 vendor-label decoy | L7 "the account" | OE9 | [9] grade on amount+tenant not vendor | QR-2026-0441 Balance 2132.0 (Fact_Ledger) | ✅ |

All 6 catalog levers + all 5 selected Hardness_Plan levers trace prompt→OE→rubric→atom. Where the atom is a free-text status/option-id not indexed by Fact_Ledger's structured surface (selSched, "possession", "accommodation"), the **record id IS the Fact_Ledger anchor** and the status text is grounded directly in the split. **No HARDNESS_REGRESSION.**

---

## LENS 4 — Strict density projection (per model, StarPM 40+ bar)

Minimizing-exploration sketch: discovery 2 + Unit-14 disambig 1-2 + hold read 1 + delinquency chain 1-3 + maintenance tickets 1-2 + Slack eviction/commit 2-3 + QB customer/7214/QR-0441/EV-047 3-5 + HubSpot ESA + gmail approval 3-5 + Linear OPS-32 1-2 + contacts 1-2 + **5 writes** + cross-service verify buffer 4-8.

| Model | Midpoint | Band verdict |
|---|---|---|
| **Opus** | **~41** (rng 38-45; at design target) | **PASS** (≥40; the audit's own rule: ~40-42 = PASS, not thin-fail) |
| **Gemini** | **~44** (rng 40-48) | **PASS** |

Both **>> 15 floor**; even the aggressive minimizer (~24) clears the floor. The rubric set is **density-positive** — [8]/[9]/[11]/[12] each force distinct cross-service reads and the write-action rubrics enforce all 5 writes; the rubrics do not erode density. Honest note: Opus sits right at the 40 target — an upstream S1/hardness property, not a rubric defect. **LENS 4 = PASS per model.**

---

## LENS 5 — Adversarial veteran review

- **Implicit-prompt framing preserved:** yes — prompt asserts the wrong "it's cleared / squared away" belief; rubrics grade the corrected end-state on every surface. Coherent across prompt/OE/rubric.
- **Entity-drift seams:** none. brooke.phillips@starpm.com (supervisor, gcalendar-confirmed), tanya.mitchell@gmail.com (tenant, QB CustomerRef), lisa.smith@starpm.com (persona/user, [13] "the user's calendar"). John Smith decoy in gcalendar is unreferenced. No email drift.
- **Silent process rubrics (three-condition test):** none — all 16 grade write artifacts/end-states, not intermediate reads/searches. Validator confirms outcome=16/process=0.
- **Tool-name leaks in titles:** 0 (scan clean). "make-ready channel/#make-ready", "the user's calendar", "issue OPS-32" are surfaces/ids, not tool identifiers. "Linear" appears only in [14] evidence (allowed).
- **Em-dashes / en-dashes:** 0 in prompt, OE, rubrics.
- **"at least N":** 0. **"approximately"/"(or similar)":** 0 in rubrics; the single OE "or similar" is on a Slack search-query suggestion, not near an exact value — benign.
- **Internal IDs mis-used:** none. OPS-32 (human id, not uuid, per OE18), rec-ids (Airtable), QR-2026-0441 (QB DocNumber), EVF-2026-014 (Airtable fldTicketNumber), C004 (Slack id) — all at the correct surface.
- **Single-channel lock-in:** none improper. #make-ready, "email to Brooke", "my Google Calendar" are prompt-named surfaces. [14] OPS-32 = the uniquely-correct stale eviction tracker (see watch-note N1).
- **Reverse-coverage surplus ([5]/[7]/[15]):** none. [5] = Slack-surface hold (distinct write from Airtable [2]); [7] = email-narrative disambiguation (distinct from Airtable write-target [0]); [15] = Linear-comment content (distinct from the other three write surfaces). Each is a separately-required deliverable; the possession-hold appearing on 4 surfaces is by-design multi-write coverage, not duplication.
- **Draft-only correctness ([6]):** CORRECT — StarPM Gmail is draft-only (no send tool); "created as a draft and not sent" honors the prompt's "Do not send it." Not a defect.

---

## LENS 7 — Anti-rationalization self-scan

Every matched pattern was LOGGED, then cleared only against a **hard structural exclusion** (never "most likely / natural channel"):
- **[4]/[8] "delinquent + active eviction + not-on-plan" conjunction** → hard exclusion: single write-action, single coherent "account not cleared" judgment that rebuts the ONE prompt misconception ("nonpayment side is cleared"); eval's atomicity Major trigger is cross-service/cross-action bundling (structural), not intra-statement coherent-state conjunction. Cleared.
- **[2] "held because possession not returned + cannot begin until returned"** → hard exclusion: one notes field, fact-plus-its-consequence (near-synonymous), one hold judgment. Cleared.
- **[11] "owner-approved(EVF) but still in JP coord"** → hard exclusion: one contrastive "approved-but-open" status. Cleared.
- **[9] "rent arrears balance of $2,132.00"** → hard exclusion: graded atoms (amount+bill+tenant) are exact and evidence explicitly scopes grading to them; "rent arrears" descriptor matches OE9's own "rent arrears and late fees". Cleared (see N2).
- **[0] accept-either-Sunset-Ridge-record** → hard exclusion: both rec-ids denote the SAME turn; OE14 blesses both; graded content is hold+correct-property-not-Rio-Bend (flexibility for genuinely-equivalent targets). Cleared.
- **[14] OPS-32 pin** → hard exclusion: structured one-correct-value field (OPS-32 is the unique open + genuinely-stale + master eviction tracker; EVF is complete/not-stale, ESA is a different matter, make-ready is write-#1's target, OPS-38/54 are subtasks). Cleared — but surfaced as N1 (not buried).

No "considered flagging X but it's fine because [soft reason]" survives — each carries a structural citation. LENS 7 satisfied.

---

## LENS 8 — Regression anchors + validator adjudication

- `test_regression_anchors.py` → **62 passed / 0 failed of 62.** No silent validator regression.
- `validate.py --phase rubrics` → **exit 0**, PASS, 0 fails / 4 warns / 5 notes.

**WARN adjudication (each treated as a hard issue):**

| WARN | Adjudication |
|---|---|
| write-verb `escalat` has no Outcome rubric | **BENIGN false-positive.** Matches prompt L9 "before I **escalat**e anything … I will take it from there" — the persona's explicit self-deferral; the agent must NOT escalate. Correctly no rubric. Absence is required. |
| write-verb `forwar` has no Outcome rubric | **BENIGN false-positive.** Matches "move it **forwar**d only as far as facts support" (prompt L3) — "move forward" (advance record), not a forwarding write-action. No forward-action rubric needed. |
| rubric[9] `$2,132.00` not in Hardness_Plan atoms nor prompt | **BENIGN false-positive.** Amount IS in OE9/OE16 and IS the QuickBooks bill QR-2026-0441 Balance (2132.0, verified). Hardness_Plan lever 11 marked QB figures "do not rely" (unverified at hardness stage); S2 grounded it. Not fabricated; contradicts nothing. Honors S2 grade-on-content carry. |
| rubric[9] X2 consistency: `2132.00` in title, no OE amount step | **BENIGN false-positive (format sensitivity).** OE9 states "Balance 2132.00" and OE16 "arrears … of 2132.00"; the validator's amount regex keys on `$X,XXX.XX` format, missing the bare `2132.00`. Value IS OE-grounded. |

**NOTE:** all 5 informational (universe=starpm; Feasible_Surface 15 tables; Fact_Ledger 403 amounts/206 emails; counts outcome=16/process=0; Overall Rubric Quality 0/16 any-issue). No action.

---

## Informational watch-notes (NON-scoring — no fix required, no REVISE)

- **N1 — [14] OPS-32 pin is the lowest-confidence item.** OPS-32 is the design-intended unique referent for the prompt's definite "the ticket we have open on it … not sitting there stale" (self-described master eviction tracker, In Progress, genuinely stale since 2026-05-11; siblings OPS-38/54 are subtasks). The evidence FAIL-clause correctly targets the real anti-pattern (creating a NEW issue). Honestly flagged: if platform trajectories show agents validly landing on OPS-54 (hearing-prep, In Progress), widen the evidence to accept it. Cleared as a one-correct-value pin; S1-BC2 ("no object lock-in") was correctly RESOLVED (not violated) once S2 grounding established OPS-32 as the unique stale tracker, with [15] keeping the content grading goal-phrased.
- **N2 — [9] "rent arrears" descriptor** is a mild simplification of a consolidated rent ledger (May arrears + June rent + late fees, net of a partial-credit line = $2,132.00). Fully grounded on the graded atoms (amount/bill/tenant); matches OE9 phrasing. Not a fabrication, not a fail.
- **N3 — Fact_Ledger index gap (upstream tooling, not a rubric defect).** EVF-2026-014, "Sunset Ridge", "Rio Bend", "make-ready", selSched/selProg/selReady, "possession", "accommodation" are absent from `Fact_Ledger.json` but present in the universe split (SSOT). Council A already noted this. Non-blocking; consider backfilling `build_fact_ledger.py` so status/option atoms index. **Not PROPAGATE-TO-S1/S2** — it is a derived-index completeness gap, and grounding holds via the split.
- **Property-name variance across services** (Airtable "Sunset Ridge Unit 14" = QB "Sunridge Apartments" = Linear "Harris Property", per S2 carry): no rubric relies on cross-service name-matching; [7] grades the make-ready canonical "Sunset Ridge" on the Sunset-vs-Rio-Bend axis, which is the correct disambiguation. Non-blocking.

---

## Cross-check vs prior councils

S3 Council A (grounding) = GO and S3 Council B (adversarial, round-2 strict re-score after a round-1 15-rubric BLOCK) = GO. Independent re-grounding **confirms** both: the round-1 fixes (split [8]/[9] state-vs-amount; de-bundle OPS-32 comment [15]; widen date [13] to 07-06/07-07; accept status-unchanged [1]) are all present and correct. I found **no defect the councils missed**; the strictest-scrutiny items all resolve to defensible 5/5 with structural exclusions, and the residual watch-items (N1-N3) are informational, not scoring.

## FINAL: **PASS (STRICT)** — ship. No REVISE, no REBUILD. Rubric dimension 5/5; all levers trace; density ≥ 40 per model.
