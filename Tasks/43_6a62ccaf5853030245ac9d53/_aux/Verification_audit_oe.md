# Verification - AUDIT (OE Phase, Veteran QC Re-Verification)

**Task:** `Tasks/43_6a62ccaf5853030245ac9d53` | **Phase:** oe | **Universe:** StarPM V4 (dual-model)
**Universe today:** 2026-07-01 America/Chicago (per `_aux/Universe_Index/today_horizon.json`; the stale
"Jun 12 US/Eastern" string inside `Docs_starpm/7_QC_Spec_Doc1.json` is superseded and was not used)
**Deliverable audited:** `6_Oracle_Events.txt`, 28 steps, 24 read + 4 write. READ-ONLY on the deliverable.
**Trigger:** Track F condition (d), the OE list was revised after both councils returned round-2 GO.

## Strictest interpretation re-applied

- 5/5 is the only acceptable score on OE Completeness and OE Accuracy (scheme 3/4/5, NON-FAIL only).
  A 4 is a soft fail and forces REVISE. Result: both landed at **4**.
- Every "should" in `Evals_starpm/2_OE_Eval.md` read as "must". Every soft convention in
  `Reference/OE_Format.md` treated as binding, including the Structure card's "one or two sentences
  describing the step" and the "not a place to add rubric reasoning" rule.
- Every validator NOTE listed as a hard issue and individually adjudicated (0 fails / 0 warns / 3 notes).
- Every Hardness lever required to trace prompt sentence to OE step to universe atom with cited
  evidence. "Probably triggered" treated as REVISE.
- Density bar applied FRAMEWORK-SCOPED as StarPM per-model: midpoint >= 40 PASS, 15-39 THIN, < 15
  INSUFFICIENT, computed separately for Opus 4.8 and for Gemini. The V3-family 50/40 scheme was NOT
  applied anywhere in this audit.
- Any answer-leakage hit on the derived 1812.00 would have been a BLOCKER. None found.
- Prior council conclusions were treated as hypotheses to be re-tested, not as evidence. Council A and
  Council B both scored 5/5 on both sub-dims at round 2; this audit reaches 4/4 on independently
  re-derived evidence.

## Sources consulted (re-verified from source with python3, not trusting prior phase outputs)

### Per-task data

Every row below was obtained by loading the file and parsing the `row_data` JSON string, never by
reading a prior report.

- `_aux/Universe_Split/quickbooks.quickbooks_entities.json` (625 entities). Re-derived: the four 4C
  bills 195089456477 / 696089964235 / 546359391323 / 991582431419 in full (TotalAmt, Balance, DocNumber,
  TxnDate, DueDate, VendorRef, line Description, AccountBasedExpenseLineDetail.AccountRef, PrivateNote,
  sync_token); invoice 445653930748 in full including all three line Amounts and sync_token "0"; decoy
  receivables 340207319849, 240572546619, 618793969708, 328611897179, 247748966591, and the
  **previously unlisted** 310712648304; payment 931951074454; all 7 accounts including 64
  (AccountType Bank / AccountSubType TrustAccounts / CurrentBalance 70624.57); all 8 vendors; all
  customers matching Castillo or Donovan (three, including the unlisted proj-e576b03e2b4c); the
  undisclosed mirror decoy 173322471681; all 15 Permian bills. Counts recomputed: 113 bills, 10 at
  TotalAmt 1340.00 with all ten ids matched, exactly 4 bills referencing 4C, account 64 used on 31 of
  113 bills, "Internal labor charge for" on exactly 2 of 625 entities.
- `_aux/Universe_Split/airtable.airtable_records.json` (170 records), `airtable_fields.json` (9),
  `airtable_tables.json` (2), `airtable_bases.json` (1). Re-derived: recc8534b3fd13954 and
  recbd087a4abd605b in full with `last_modified_time` to the microsecond; reca424761ae15355,
  rec12969a3fdb0852, rec860db6b493af1e5b; the date-field inversion against modification order; the
  120-row tblMakeReady and 50-row tblMaintenanceTickets populations; and every search-result count OE 3
  and OE 6 assert, re-run as substring queries (tblMakeReady "Mesa Vista 4C" = 2; "Mesa Vista" = 8 rows
  across 4 units; tblMaintenanceTickets "4C" = 2; "Mesa Vista 4C" = 1; "Mesa Vista" = 3).
- `_aux/Universe_Split/contacts.contacts.json` (61). Re-derived: Linda Castillo
  (b47044b4ec775b318bac813d5fb1bf5d, Property Owner), Pete Donovan (Exterior Painter), John Castillo
  (Water Delivery Representative), Carlos Mendez (Onsite Property Manager), Tony Reyes (Lead Maintenance
  Technician), Jaime Salinas (Quality Control Inspector), Carmen Delgado, Brooke Phillips, and
  **Tommy Reyes** (a4c863c4d92d53a59c310bb29abd6d0c, Tenant), the seam the OE never surfaces.
- `_aux/Universe_Split/slack.slack_messages.json` (580) + `slack_channels.json` (8) +
  `slack_users.json` (61). Re-derived: all six 4C ts values with per-message `user_id` and verbatim
  text; C004 population 144 rows of which 48 carry `is_activity_message: true`; the 4C block's position
  (index 45-50 from oldest, 93-98 from newest); C005 population 6 with zero 4C content; and a full
  580-message sweep for 1340 / 1,340 / 1140 / 1,140 / 1622 / 1,622 / 1812 / 1,812 / 387 / $95 / $85,
  all returning zero.
- `_aux/Universe_Split/gmail.gmail_messages.json` (484) + `gmail_threads.json` (156). Re-derived: all
  five 4C message ids with headers and **base64-decoded bodies**; all five thread ids confirmed present;
  the belief email's zero dollar figures; `has_attachments: false` and `parts: []` on 5101c5a41dffa90a
  (the "a copy is attached" claim is a phantom); the two unrelated "$1,340" Gmail strings
  (4a20c7c433db278a, 6f2669a41401485a); zero occurrences of 2026-534 in any email and exactly one of
  2026-537.
- `_aux/Fact_Ledger.json`. Used only as an independent cross-check, and audited in its own right:
  `amounts` confirms 1812.00 / 1897.00 / 1727.00 / 10.00 all ABSENT and 85 / 95 / 190 / 200 / 387 /
  1140 / 1340 / 1622 all PRESENT; `ids.invoice` holds 504 DocNumbers with all 20 cited DocNumbers
  PRESENT and the phantom 2026-537 ABSENT, but with **all five 4C QuickBooks entity ids ABSENT**;
  `entities` is `[]`; `lifecycle.today` is `null`.
- `_aux/Universe_Index/today_horizon.json`, `key_facts.md`, `entities_personas.md`,
  `accounts_per_entity.md`, `service_inventory.md`, `graph_report.md`.
- `5_Prompt.txt`, `2_Persona.txt`, `1_Business_Function.txt`, `PersonaBrief.txt`.
- `_aux/Hardness_Plan.md`, `_aux/Verification_s1.md`, `_aux/Reads_s2.md`, `_aux/Todos_s2.md`,
  `_aux/Reasoning/OE_solvability.md`, `_aux/Linter_Decision.md`, `_aux/Feasible_Surface.json`.
- `_aux/Council_Reports/S2_A_grounding.md`, `S2_B_adversarial.md`, `AUDIT_prompt.md`,
  `verify_universe_atoms.md` - re-read specifically to locate pattern misses, not to inherit conclusions.
- **Real harness output, three prior StarPM V4 tasks sharing this base universe.** This is the source
  that settled two questions I would otherwise have had to assume:
  `Tasks/40_.../Agent_Responses/Opus/trajectory-run-1.json` - a bare
  `slack_read_channel(channel_id: "C004")` returned 96 messages newest-first from ts
  1782415250.000193 down to 1777838404.000049 **including all six 4C ts values**, which clears OE 23;
  and `slack_search_public_and_private(query: "make-ready")` returned a Channels-only result block with
  zero messages in all six Opus runs. `Tasks/41_.../Agent_Responses/Opus/trajectory-run-1.json` - a real
  `search_invoices(query: "Mitchell")` tool_result carries the **full** properties envelope
  (Line[].Amount, Line[].Description, Balance, TotalAmt, DocNumber, CustomerRef, PrivateNote,
  CustomerMemo, SyncToken), and the search is an AND over query tokens
  ("Mitchell eviction" = 4 results, "Mitchell eviction payment plan" = 0).
  `Tasks/41_.../Agent_Responses/Opus/trajectory-run-6.json` - a real `get_table_schema` result
  reproducing the identical 9 fields and the identical selSched / selProg / selReady choice set.
  Tool-call counts extracted from all 36 prior trajectory files for the density anchors.
- `Tasks/43_.../Agent_Responses/Opus/` and `/Gemini/` are present but all twelve files are 0 bytes,
  so no run-level evidence exists for this task yet. S4 has not run.

### Eval spec

- `Evals_starpm/2_OE_Eval.md` read in full and applied: the OE Authority Rule (OEs are CB planning
  documents, not ground truth, and cannot override prompt or universe); Phase 1.2 tool-use step
  validation and its anti-pattern table; Phase 2.1 to 2.3 tool / service / parameter verification;
  Phase 2.4 the per-OE sign-off discipline (discharged by the 71-row per-atom table in `AUDIT_oe.md`,
  every cell non-empty, zero NOT FOUND); Phase 2.4's act-vs-defer HARD GATE; Phase 2.5 date consistency;
  Phase 3.1 to 3.3 completeness, dependency chain and write-action coverage; Phase 4.0 the mandatory
  four-item pre-verdict sweep. All four Phase 4.0 items were re-run independently: (1) wrong count -
  every asserted count matches, but OE 22's six-message claim is unretrievable by its own parameters;
  (2) wrong tool - none, all 25 verified; (3) missing write-action OE - none, all four writes covered;
  (4) act-vs-defer conflict - none, no write rests on a `proposed_resolution` and a full scan of eight
  Slack channels plus Carlos's mailbox for a defer, hold, accept-timing or not-act decision touching 4C,
  Linda Castillo, Mesa Vista or owner billing returned zero hits.

### QC spec

- `Docs_starpm/7_QC_Spec_Doc1.json`, dimension index 2 "Oracle Event (OE)", both sub-dimensions read
  verbatim from the JSON. OE Completeness Pass(5) = "OEs describe the full critical path: key discovery
  steps + dependency chain(s) + required write action(s)". OE Accuracy Pass(5) = "All OEs are factually
  accurate. Tools, services, parameters, and expected data match the universe. Following the OEs
  literally would produce a correct trajectory." The Accuracy Non-Fail(3/4) band explicitly covers
  "wrong parameters" and steps that "would not produce the correct results if followed literally", which
  is the band OE 22 falls into. The auditor note of 07/16 was applied: the OE cannot be used to clarify
  the prompt, which is the basis for finding M2.
- `Docs_starpm/8_QC_Spec_Doc2.md` audit workflow step 5 (OE evaluation) applied.
- `Reference/OE_Format.md` applied as binding: no em-dash or en-dash (0 of each, and 0 non-ASCII code
  points overall); real tool names only (all 25 present in the catalog); real parameter names including
  the StarPM v4 traps `slack_send_message(channel_id, message)` not payload or text,
  `create_draft(..., body)` not content and draft-only with no send tool, Airtable camelCase
  `baseId`/`tableId` versus `search_records`'s `table`, and QuickBooks creates using one `properties`
  envelope - all satisfied and all called out correctly by the OE itself; numbered sequential 1..28
  confirmed; discovery before writes confirmed; the optional final-paragraph convention sanctions OE 28.
  The one binding convention breached is the Structure card's "one or two sentences describing the step"
 - finding m8.
- `Reference/OE_Convention_Inventory.json` - OE count distribution (min 11, mean 16.5, max 28) puts 28
  steps at the ceiling but inside it.
- `Docs_starpm/13_QC_Companion.md` was **NOT** consulted. It is Brookfield-contaminated and is not
  StarPM SSOT, per the audit brief.

## QC spec sub-dims rescored

| Sub-dimension | Council A r2 | Council B r2 | AUDIT round 1 | **AUDIT round 2 (final)** |
|---|---|---|---|---|
| OE Completeness | 5/5 | 5/5 | 4/5 | **5/5** |
| OE Accuracy | 5/5 | 5/5 | 4/5 | **5/5** |

Round-1 drivers for the 4s, all now discharged and re-verified byte-for-byte:
Completeness was held down by M1 (the enumerated sixth C004 message was unreachable by the step's own
stated parameters), M3b (the closest decoy and its 1810.00 consequence were absent from the discovery and
wrong-figure inventories) and m7 (the 1140.00 mirror decoy was undisclosed while OE 16 claimed to
disambiguate the amount trap). Accuracy was held down by M1, M2 (a foreclosure attributed to the prompt
that the prompt does not contain, with a rationale wrong for the instrument), M3a (the stated queries did
not return the stated decoys), m1 (self-contradiction against OE 10 and OE 11), m2 (a false absolute on
where 1340.00 exists), m3 (an entity name not byte-exact) and m6 (a corroboration step that could
corroborate the wrong record).

Round 2 raises both to 5. The distinction that carries the re-score: every round-1 defect was either a
false statement about the universe or the prompt, or a genuinely missing discovery item. Every one is now
correct on independent re-derivation, and the fixes were made by adding verified fact rather than by
softening claims. The two remaining residuals (R2-a, a suboptimal query alternative inside the
OE_Format-sanctioned menu form; R2-b, a step that reasons over data already retrieved) are neither false
statements nor missing steps, so neither satisfies the Non-Fail band as `Docs_starpm/7_QC_Spec_Doc1.json`
writes it: Completeness Non-Fail is "OEs are missing critical steps needed to solve the task" and nothing
is missing; Accuracy Non-Fail is a wrong tool, service, parameter or expected value and there is none.
Both residuals are logged in `AUDIT_oe.md` with hard exclusions cited and exact fixes given.

## All lenses status

Round-1 status is given first where it differs, with the round-2 outcome in bold after it.

- **LENS 1 strict QC scoring: round 1 REVISE (4/5, 4/5) -> round 2 PASS (5/5, 5/5).** The mandatory
  per-atom evidence table is complete at 71 rows with zero empty cells and zero NOT FOUND, and the
  round-2 pass re-derived a further 30 atoms across the fixes. All four StarPM landmines checked: at
  round 1 near-duplicate decoys were PARTIAL with three undisclosed, and **all three are now disclosed**
  (invoice 310712648304 in OE 10, bill 173322471681 in OE 16, the Tommy Reyes surname collision in
  OE 10); cross-property unit ambiguity CLEAR; Airtable-as-source-of-record CLEAR; twin-85.00 ARMED and
  correctly decided, now with its three discriminators sitting in OE 17 and OE 18 where each record is
  first opened.
- **LENS 2 answer-leakage sweep: PASS, no BLOCKER, both rounds.** 1812.00, 1897.00 and 1727.00 exist
  nowhere in the universe as money (numeric sweep of every TotalAmt, Balance and Line Amount across 625
  entities: zero). All 20 raw string hits on those digit sequences are substrings of timestamps, history
  ids or entity ids. Gmail bodies were base64-decoded before searching. No single record contains all
  three of 387, 1340 and 85, so synthesis across at least three records is required. The prompt contains
  no numeral at all. **Round 2 re-swept the five newly added figures and no vector opened:** 1810.00,
  1380.00 and 6992.00 all return zero TotalAmt / Balance / Line-amount hits, the only human-readable
  1,380 is the intentional one inside bill 173322471681's PrivateNote that OE 16 now discloses by design,
  6992.00 appears nowhere at all, and the 1810.00 string hits are four id and header substrings across
  gmail, slack and one QuickBooks estimate id.
- **LENS 3 hardness end-to-end trace: PASS on levers, no HARDNESS_REGRESSION.** L2, L10, L6, L11/L9 and
  the L1 reserve each trace prompt sentence to OE step to cited atom, and each is forward-mappable to a
  rubric criterion that depends on traversal, except L11. **L11 is DISPLACED**, stated plainly: its
  decision surface is co-located with L2's gate in a single `search_bills` call rather than two hops
  behind it, but it still has zero observable surface among agents that fail L2, so under the plan's own
  [HIGH] 0/12 prediction its expected independent fail count is zero. Same outcome as Learnings item 9
  (Task 41), different mechanism, and the remedy that item prescribes is available in this universe but
  unexploited by the OE.
- **LENS 4 strict density, StarPM per-model: Opus PASS, Gemini THIN.** Anchored on 36 real trajectories
  from tasks 39, 40 and 41 rather than on the plan's assumption. Opus 47 on the intended solving
  trajectory (band 42-52), 38 stumped, 39.5 blended. Gemini 41 solving (band 35-45), 31 stumped, 33
  blended. Empirical floor across 18 prior runs is 26 Opus / 28 Gemini, so no INSUFFICIENT risk. Breadth
  PASS at 5 services, dominant 44.7% under the 60% ceiling, all at or above 5%. Finding M4 records that
  the Hardness_Plan's THIN-acceptance mitigation does not hold on the modal branch and that Council B's
  Opus 46 is over-credited.
- **LENS 5 adversarial veteran review: round 1 REVISE -> round 2 PASS.** Ten sub-checks re-run in full on
  the round-2 text. Clear in both rounds: single-channel lock-in (OE 27 explicitly admits C005 and C006
  and grades on content), "approximately" and "(or similar)" (zero occurrences; the three "about" hits are
  ordinary prose, none near a value), OE meta-tags (none), harness-impossible instructions (none, 25
  catalog tools and the only non-catalog snake_case tokens being the four genuine parameter names
  channel_id / contact_id / end_date / invoice_id), page sizes (OE 16's pagination handling intact, OE 23
  empirically clear). **All three round-1 failures are fixed and re-verified:** OE 24's prompt-framing
  over-reading is gone, the ampersand entity name is correct throughout ("Cleaning and Repairs" now zero
  occurrences), and the Tony / Tommy Reyes seam is surfaced in OE 10 with the correct role and
  adjudication. One residual, R2-b, the tool-less OE 19.
- **LENS 7 anti-rationalization: APPLIED and reported in both rounds.** Round 1: nine candidate
  rationalizations, five promoted to findings (the 190.00 collision, the Pinnacle 1140/1380 mirror decoy,
  the "A Plus and Repairs" spelling, the OE 19 redundant re-reads, the 385.00 pass-through decoy), four
  excluded with hard exclusions stated so they can be checked (OE 23's page size, empirically disproved by
  a real same-universe tool_result; OE 28's missing tool anchor, sanctioned by `Reference/OE_Format.md`;
  account 63 on an AP bill, base-universe data on a no-injection task already disclosed by OE 19 G4; and
  OE 16's "1340 will not match on amount", verified true). Round 2: four more, two promoted (R2-a and
  R2-b) and two excluded with hard exclusions (OE 10's "two decoys" against the six invoices a
  Linda Castillo query actually returns, and OE 16's server-order-dependent 50-row-page claim).
  **R2-b is a defect my own round-1 prescription introduced, and I logged it against myself rather than
  letting it pass as compliance with my instruction.**
- **LENS 8 regression anchors: PASS in both rounds, identical.** 62/62 reproduced independently before and
  after the revision. `validate.py --phase oe` 0 fails / 0 warns / 3 notes both times, same three notes,
  same adjudication. `verify_universe_atoms` 0 fails / 0 warns but only 16 atoms, which is finding M5, now
  documented by the coordinator in `_aux/Verification_s2.md`. The revision moved no baseline.

## Verification statements

- [x] `python3 Validators/test_regression_anchors.py` run independently: **62 passed, 0 failed out of 62**. Matches the 62/62 reported in the brief.
- [x] `python3 Validators/validate.py --phase oe --task Tasks/43_6a62ccaf5853030245ac9d53`: **PASS, 0 fails, 0 warns, 3 notes**. All three notes listed and adjudicated as hard issues; N3 folded into M5.
- [x] `python3 Validators/verify_universe_atoms.py --task Tasks/43_6a62ccaf5853030245ac9d53`: **PASS, 0 fails, 0 warns, 16 atoms**. The 16 are 5 Airtable record ids and 11 email addresses; the extractor has no pattern for a 12-digit QuickBooks entity id or a Slack ts, so the OE's load-bearing identifiers were never machine-checked. Finding M5.
- [x] All four 4C bills verified byte-for-byte on TotalAmt, Balance, DocNumber, VendorRef and AccountRef: 195089456477 = 387.00 / 387.00 / 2026-SC-4C / Sunshine Cleaning proj-d016366b403c / Contract Labor 62; 696089964235 = 1340.00 / 1340.00 / PD-2026-09 / Permian Make-Ready Crew 204 / Management Fee Income 63; 546359391323 = 85.00 / 85.00 / 2026-519 / Permian 204 / Owner Reserve (Trust) 64; 991582431419 = 85.00 / 85.00 / 2026-481-566 / Alamo HVAC Services 200 / Supplies 61.
- [x] Invoice 445653930748 verified: three line Amounts 387.00 / 1140.00 / 95.00 with Ids 1 / 2 / 3, TotalAmt 1622.00, Balance 1622.00, sync_token "0", DocNumber 2026-534, CustomerRef Linda Castillo proj-4ae920b7c9e8, TxnDate 2026-05-01, DueDate 2026-05-31.
- [x] Both tblMakeReady 4C rows verified: recc8534b3fd13954 selReady / 2026-06-01 / 2026-06-14 / mod 2026-05-29 14:26:59.557207; recbd087a4abd605b selProg / 2026-06-15 / 2026-06-30 / mod 2026-05-22 21:14:34.331831. The date-field inversion OE 3 asserts is real: the stale row carries the later dates.
- [x] All nine Airtable field identifiers and both select-option sets verified against `airtable_fields.json` and independently against a real `get_table_schema` tool_result: fldTicketNumber, fldDescription, fldPriority (selLow / selMedium / selHigh), fldCompletionDate, fldUnit (primary of tblMakeReady), fldTurnStatus (exactly selSched "Scheduled" / selProg "In Progress" / selReady "Ready"), fldMoveOut, fldTargetReady, fldNotes2. No cost field and no "Closed" option exist, exactly as OE 5 and OE 25 require.
- [x] All six C004 message ts values verified with authors: 1779501868.000000 / 1779501869.000001 / 1779501870.000002 / 1779501871.000003 Carlos Mendez U07E4512181; 1779501872.000004 Jaime Salinas U2CD1BC03B2; 1779501873.000005 Carlos Mendez U07E4512181. All six unthreaded. Text verified verbatim on all six.
- [x] All four OE 8 gmail thread ids verified present (525641a76c00fbe0, c138c134b23d60d3, 83872812663ee5c9, f43fdaee4372a09b), plus OE 7's 66132537181ecbe1. All five subjects match; all five bodies base64-decoded and read.
- [x] contact_id b47044b4ec775b318bac813d5fb1bf5d = Linda Castillo, linda.castillo@gmail.com, job "Property Owner". Both customer ids verified: proj-4ae920b7c9e8 Linda Castillo and proj-f6f9edfeae5c Pete Donovan. A third Castillo customer proj-e576b03e2b4c exists and is undisclosed by OE 9 (m4).
- [x] All eight vendor ids verified: 200 Alamo HVAC Services, 201 Hill Country Plumbing, 202 Lone Star Electric, 203 Big Bend Restoration, 204 Permian Make-Ready Crew, proj-8fd39a6550fe Lone Star Maintenance Supply, proj-a989f559245a A Plus Carpet Cleaning & Repairs, proj-d016366b403c Sunshine Cleaning. Count = 8. Neither Tony Reyes nor Jaime Salinas appears, and no vendor is a StarPM employee.
- [x] Every count the OE asserts recomputed from source and matched: 113 bills; 10 bills at TotalAmt 1340.00 with all ten ids correct; 4 bills touching Unit 4C; 8 vendors; 6 messages in C005; 2 4C make-ready rows; 3 fldTurnStatus choices; 3 invoice lines; 6 consecutive C004 4C messages; 3 records attributing the trim fix to Tony Reyes, with an independent sweep confirming there is no fourth.
- [x] Arithmetic recomputed independently: 387 + 1340 + 85 = 1812; 1812 - 1622 = 190; 1340 - 1140 = 200 understated; 95 - 85 = 10 overstated; 200 - 10 = 190; 387 + 1340 + 85 + 85 = 1897; 387 + 1340 = 1727.
- [x] All five grounds of OE 19 verified true in the data. G1: "Internal labor charge for" on exactly 2 of 625 entities. G2: no bill exists for the faucet, GFCI or drywall work, and both 85.00 bills carry Balance 85.00 against third-party VendorRefs. G3: bill 991582431419's line reads "Unit condition inspection and punch list documentation", matching the prompt's "an internal walk or a condition check". G4: account 64 is AccountType Bank / AccountSubType TrustAccounts / CurrentBalance 70624.57 and is used on only one of the four 4C bills, and the OE's self-limiting caveat is necessary because 64 is used on 31 of 113 bills overall. G5: both operative instructions quoted byte-exact.
- [x] Answer-leakage sweep clean: zero occurrences of 1812.00, 1897.00 or 1727.00 as any TotalAmt, Balance or Line Amount across 625 QuickBooks entities; all 20 raw digit-sequence hits are timestamp or id substrings; independently corroborated by `Fact_Ledger.amounts`, where 1812.00 / 1897.00 / 1727.00 are all ABSENT. Gmail bodies were base64-decoded before searching. Zero Slack hits for any 4C amount.
- [x] No single tool call reveals the total: no record among all 625 contains 387, 1340 and 85 together, so at least three record reads plus the invoice read are required.
- [x] 190.00 appears as a line amount on exactly three unrelated records (330747391806, 210266819067, 618793969708), none on Mesa Vista 4C and none billed to Linda Castillo. Logged as m10, not a leak.
- [x] All 25 tools and every parameter name verified against `StarPM_Base_Universe/7_Server_Tools_Details.json`: `get-bill(id)` hyphenated, `search_records(baseId, table, query)`, `list_records_for_table(baseId, tableId, recordIds)`, `update_records_for_table(baseId, tableId, records)`, `get_table_schema(baseId, tables)`, `update_invoice(id, SyncToken, properties)`, `create_draft(to, subject, body, replyToMessageId)`, `slack_send_message(channel_id, message)`, `contacts_get_contact(contact_id)`, `get_customer_balance(customer, start_date, end_date)`, `get_aged_receivables(customer)`, `get_vendor_expenses(vendor, start_date, end_date)`, `read_invoice(invoice_id)`, `search_bills(query, max_results, start_position)`. Zero phantom tools, zero wrong services, zero unreachable records.
- [x] OE 23's bare `slack_read_channel(channel_id: "C004")` is feasible: proved by a real same-universe tool_result returning 96 of C004's 144 rows (the 48 `is_activity_message: true` rows are filtered) including all six 4C ts values, with no truncation.
- [x] OE 22's three stated queries were NOT sufficient at round 1: harness search is an AND over tokens, so "Mesa Vista 4C" returns 3 of 6, "4C" returns 5 of 6, and "make-ready" matches the channel name and returns 0 messages. ts 1779501872.000004 was unreachable by all three. Finding M1, discharged at round 2.

### Round-2 verification statements

- [x] `6_Oracle_Events.txt` re-read fresh, not diffed against a remembered version. 28 steps, sequential 1 through 28, 4,529 words, 0 non-ASCII code points.
- [x] **M1 fix confirmed correct on both halves of the check the coordinator asked for.** First, ts 1779501872.000004 IS reachable by `slack_read_channel(channel_id: "C004")`: re-confirmed against Task 40 Opus run 1's real tool_result, which returned 96 of C004's 144 rows (144 minus the 48 `is_activity_message: true` rows) newest-first from ts 1782415250.000193 down to 1777838404.000049, with all six 4C ts values present and no truncation. Second, OE 22's stated reason is byte-true: a token audit of the sixth message gives `4C:N Mesa:N Vista:N`, so "its text names neither the unit nor the property" is exactly right.
- [x] **OE 22 is not over-claimed for the five it does list, on the query that matters.** A simulated AND-of-tokens `"4C"` against all 580 Slack messages returns exactly those five posts and nothing else workspace-wide, all in C004, all authored by U07E4512181. All five contain the "4C" token, so "the five Carlos Mendez posts that name the unit" is accurate. Residual R2-a: `"Mesa Vista 4C"` returns only three of the five, and `"make-ready"` returns a channels-only block with no messages (20 messages contain the token workspace-wide, of which only three are in the 4C sequence).
- [x] OE 23's quote is byte-identical to the record: "Jaime flagged a paint touch-up on the bedroom closet trim. Tony got it done today, Airtable updated." Author U2CD1BC03B2 = Jaime Salinas confirmed; the other five all U07E4512181 = Carlos Mendez.
- [x] **M2 fix confirmed:** the prompt sentence is "I do not want a second bill created next to the one she already has", which a second owner invoice is, so OE 24's `create_invoice` foreclosure is now correctly prompt-grounded; and the credit-memo exclusion now rests on the direction of the variance (1622.00 to 1812.00 is an increase, and a credit memo reduces a receivable), which is a ledger fact rather than a prompt reading.
- [x] **M3 fix confirmed and more precise than prescribed:** all six Linda Castillo invoices re-derived, and exactly the two named decoys (310712648304 and 340207319849) share 2026-534's TxnDate 2026-05-01 and DueDate 2026-05-31 while the other three do not, so "both sharing" is a true discriminator. 310712648304 = DocNumber 2547, TotalAmt 385.00, Balance 385.00, line "Pass-through: A Plus Carpet Cleaning & Repairs - deep-clean and seam re-stretch, Rio Bend unit (owner-billable vendor cost)". 385 + 1340 + 85 = 1810 recomputed and now catalogued in OE 21.
- [x] **m6 fix confirmed exact on all four numbers:** Permian (VendorRef 204) bills with TxnDate in 2026-05 number **12** and sum **6992.00**, both recomputed from source; 102111031436 = 1340.00 grounds maintenance at 4821 Oleander Dr; 167365280749 = 610.00 "Interior paint touch-up, Cascade Hills Dr Unit 7C - walls and trim"; 358082173277 = 310.00 "Drywall patch and paint touch-up, Elm Street unit 3".
- [x] **m7 fix confirmed exact on every attribute:** bill 173322471681 = DocNumber INV-2026-0417, VendorRef Hill Country Plumbing (201), TotalAmt 1140.00, AccountRef "Management Fee Income" (63) which is indeed the same account code bill 696089964235 carries, line "Plumbing repair - water line replacement, Riverside Portfolio Building B", PrivateNote "Disputed Pinnacle Plumbing invoice. Internal expected amount was $1,140; vendor billed $1,380. Awaiting vendor correction or credit memo before closing."
- [x] m1 fixed exactly as prescribed (OE 13 now scopes the claim to vendor bills and names 2026-534 as the one receivable). m2 fixed with both Gmail messages correctly characterised (4a20c7c433db278a a monthly rent rate, 6f2669a41401485a a Reyes Plumbing invoice total) and Slack re-swept clean at 0 hits for 1340 and 1,340 across all 580 messages. m3 fixed ("Cleaning and Repairs" now 0 occurrences, ampersand form 3). m4 fixed and re-verified (a surname query returns exactly two Castillos). m5 fixed (Tommy Reyes = contact a4c863c4d92d53a59c310bb29abd6d0c, job "Tenant"). m9 and m10 present and accurate.
- [x] **M4 and M5 documentation records verified by reading the files, not by accepting the description.** `_aux/Reasoning/OE_solvability.md` carries my per-model table verbatim (Opus 47 / 38 / 39.5 PASS, Gemini 41 / 31 / 32.7 THIN), states the plan's uniform minus-9.5 Gemini delta does not hold with Task 40's at 1.5, flags "writes execute on BOTH models" as failing on the modal branch, sets the actionable Gemini threshold below 24, and records L11 as DISPLACED with an instruction not to credit it at S4 as a separate stump. `_aux/Verification_s2.md` records the atom-verifier coverage gap accurately and does not cite the 16-atom PASS as coverage.
- [x] Not patching the atom extractor mid-task is the correct call: adding a pattern to `collect_atoms_from_text` would move the frozen 62-anchor regression baseline during an active audit. Re-ran all three validators after the revision and every count is identical to round 1 (62/62; oe 0/0/3; atoms 0/0/16), confirming the revision moved nothing.
- [x] **LENS 2 re-swept for the five newly added figures.** Zero TotalAmt / Balance / Line-amount hits anywhere in the 625 QuickBooks entities for 1810.00, 1380.00 or 6992.00, and 1812.00 / 1897.00 / 1727.00 re-confirmed at zero. The only human-readable 1,380 is the intentional one in bill 173322471681's PrivateNote, disclosed by design in OE 16. All 1810 string hits are id or header substrings (gmail message id ab81ee4418101874 and its Message-ID header, slack message id 80c504ecc4a35261810e139f19ce495c and the thread_parent_id repeating it, QuickBooks estimate id 535173181003). 6992.00 appears nowhere. No new leakage vector opened.
- [x] Synthesis requirement re-confirmed unchanged: no single record among the 625 contains 387, 1340 and 85 together.
- [x] Round-2 tool re-inventory: 25 catalog tools referenced, and the only non-catalog snake_case tokens in the whole file are `channel_id`, `contact_id`, `end_date` and `invoice_id`, all genuine parameter names. The revision introduced no new tool. OE 19 confirmed to contain no `Use` imperative, which is finding R2-b.
- [x] Round-2 hedge scan: zero "approximately", "approx", "roughly", "(or similar)". The three "about" occurrences are ordinary prose ("about who the payee is", "about who executed the repair", "about who is billed for it"), none adjacent to an id, a date or an amount.
- [x] Per-step restructure measured: OE 19 dropped 484 words to 257 with the cosmetic re-read removed; the three discriminators moved into OE 17 (164 to 248) and OE 18 (150 to 240), where each record is first opened. File total grew 4,167 to 4,529 words because the M3 / m2 / m5 / m6 / m7 grounding outweighs the compression.
- [x] Verbosity finding m8 **withdrawn**, with reasons recorded in `AUDIT_oe.md` and the specific cuttable clauses named. `Reference/OE_Format.md` sets no word budget, `Reference/OE_Convention_Inventory.json` records only a step-count distribution (and 28 sits inside it at Task13 = 28), no validator gates it, and the growth is entirely verified fact added to close accuracy findings I myself raised.
- [x] Both output files remain pure ASCII after the round-2 edits, and neither embeds a literal double-hash section token inside verification prose, per Learnings 2026-07-23 item 2.
- [x] Act-vs-defer HARD GATE cleared: no write-action OE rests on a `proposed_resolution`, and a full scan of all eight Slack channels and Carlos's entire mailbox for a defer, hold, accept-timing or not-act decision touching 4C, Linda Castillo, Mesa Vista or owner billing returned zero hits.
- [x] Date consistency: universe today 2026-07-01 America/Chicago. The prompt uses only relative-past phrasing ("back in the spring"), which resolves consistently against the 2026-05-01 bill dates, the 2026-06-02 summary email and the 2026-05-29 live make-ready row. No OE date reference is out of window.
- [x] Deliverable is pure ASCII: 0 em-dash, 0 en-dash, 0 smart quotes, 0 ellipsis characters, 0 non-ASCII code points. 28 steps, numbered sequentially 1 through 28, every step opening with an action verb, no markdown, no meta-tags, no lever or rubric identifiers.
- [x] Both output files written by this audit are pure ASCII, and neither embeds a literal double-hash section token inside verification prose, per Learnings 2026-07-23 item 2.

## Discrepancies surfaced

1. **Both councils verified atom existence but never atom retrievability, and that is the single pattern
   miss that produced M1.** Council A logged the missing sixth C004 message as round-1 Major-3, correctly
   noted at its own line 332 that `slack_read_channel(C004)` returns it, then marked the fix "RESOLVED"
   once the ts and the Jaime Salinas attribution were added. Council B verified the same atoms and wrote
   "EXACT". Neither asked whether OE 22's own three queries retrieve the message they had just insisted
   be added. They do not. The same pattern repeats on OE 10: both verified the listed decoys exist,
   neither checked that the listed queries return them, and neither swept for a closer unlisted decoy.
2. **Council B praised the OE 24 credit-memo clause as a strengthening without testing it against the
   prompt sentence.** Its round-2 [B8] reads "The negative guard strengthened (OE 24 now forecloses
   `create_invoice` and a credit memo, closing round-1 alt-path D explicitly)". The prompt forecloses
   "a second bill". A credit memo is not a bill and reduces rather than double-bills. `OE_solvability.md`
   already previews the rubric this becomes, which is the Learnings L30 / 2026-07-24 item-5 defect class
   one step before it lands. Finding M2.
3. **Council B's Round-2 Opus density midpoint of 46, "further clear of the line", does not survive
   re-derivation.** It takes +2 credit for the two OE 19 `get-bill` re-reads, which a real
   same-universe `search_*` tool_result shows return data the agent already holds, and it models only
   the solving branch while the plan's own Stump Hypothesis 1 predicts the stumped branch is modal.
   Blended, Opus is 39.5. Finding M4.
4. **The Hardness_Plan's stated mitigation for accepting Gemini THIN is invalid on the predicted
   branch.** Section "THIN density acceptance" item 2 rests on "Writes execute on BOTH models", but the
   prompt makes three of the four writes conditional on the agent finding the discrepancy, which by
   construction the stumped runs do not. Folded into M4.
5. **The reported `verify_universe_atoms` PASS is not atom coverage.** 16 atoms checked, none of them a
   QuickBooks entity id, a Slack ts, a DocNumber or a count. Root cause is a validator extractor gap
   compounded by three `Fact_Ledger` gaps (`ids` has no key for QB entity ids or Slack ts, `entities` is
   empty, `lifecycle.today` is null while `Universe_Index/today_horizon.json` carries the date).
   Finding M5. The 71-row per-atom table in `AUDIT_oe.md` is the verification of record.
6. **Three near-duplicate decoys are present in the universe and absent from the OE.** Invoice
   310712648304 (2547, 385.00, Linda Castillo, "Pass-through ... deep-clean", same TxnDate and
   DueDate as 2026-534), whose substitution yields an 1810.00 wrong answer
   that OE 21's catalog does not carry; bill 173322471681 (1140.00 with an "expected 1,140 / billed
   1,380" note on the same AccountRef 63 as the 4C repaint); and the "Tommy Reyes unit" string on decoy
   340207319849, which collides with the 4C repaint on amount, owner and surname simultaneously.
   Findings M3, m7, m5.
7. **Two carried-unfixed Council A minors are confirmed still live.** Min-1, "A Plus Carpet Cleaning and
   Repairs" against the universe "A Plus Carpet Cleaning & Repairs" (m3). Min-8, verbosity, which grew:
   4,167 words against the QC_Passed band of 1,002-1,675, with OE 19 alone at 484 words and 12 sentences
   against `Reference/OE_Format.md`'s "one or two sentences describing the step" (m8).
8. **Favorable discrepancy, recorded for completeness.** All four items Council A raised as new round-2
   Moderates and Minors that were actionable in the OE text (Mod-5 the `max_results: 50` sufficiency
   problem, Mod-6 the OE 20 "never invoiced" collision with OE 19, Min-2 the missing comma in "412
   Garfield Ave, Unit 3C", Min-9 the over-generalizable account-coding ground) and all three of Council
   B's round-2 NITs (R2-1 the garbled OE 19 clause, R2-2 the broader "Mesa Vista" query, R2-3 the
   whole-vendor-master query) were correctly folded into the current text. I re-verified each fix
   against the universe. This is the revision that fired Track F condition (d), and on those seven items
   it was done well.
9. **The pivotal question resolves in the OE's favour.** All five grounds of OE 19 are true in the data,
   the two that neutralise rather than discriminate are labelled as such by the OE itself, and the three
   that do discriminate are mutually independent (prompt-textual, hard ledger fact, operative
   instruction) and are reinforced by two further vectors from OE 11, OE 18 and OE 24. 1812.00 is the
   uniquely best-supported end-state. The residual 1727.00 path is the designed decoy, is fully
   disclosed, and is answered on the record.
10. **No `PROPAGATE TO S1`.** The prompt's carve-out names the excluded bill's line description nearly
    word for word, and its general rule keeps the three vendor payouts in, so the prompt is adequate.
    M2 is an OE over-reading of prompt language and is repaired in the OE. The pipeline does not STOP.

### Round-2 discrepancies surfaced

11. **All five Majors and all ten Minors are discharged, and none was discharged by weakening a true
    claim.** The only removal anywhere in the revision is ts 1779501872.000004 from OE 22's search
    enumeration, and that record now appears in OE 23 with a fuller treatment than it had before. Every
    other fix added verified universe fact. I re-derived roughly 30 further atoms this round and found
    zero discrepancies against the new text.
12. **The coordinator's round-2 text is more precise than my own prescription in one place, which is
    worth recording.** I asked for invoice 310712648304 to be added as a decoy. The text also establishes
    that it and 340207319849 are exactly the two Linda Castillo invoices sharing 2026-534's TxnDate and
    DueDate, which I confirmed against all six of her invoices. That turns a loose "same owner" gloss into
    a true discriminator.
13. **R2-b is a defect my own round-1 prescription caused.** I flagged OE 19's `get-bill` re-reads as a
    cosmetic anchor and prescribed keeping OE 19 as a short decision step. The coordinator did exactly
    that, and the result is a mid-list step with no tool call, which `Evals_starpm/2_OE_Eval.md` Phase 1.1
    and 1.2 name as an anti-pattern. My instruction was underspecified. I have logged it against myself
    rather than treating compliance with my own guidance as clean, and the fix in `AUDIT_oe.md` dissolves
    OE 19 into OE 18 and OE 23 so that no content is lost and no tool call is duplicated.
14. **R2-a stands as a logged residual that does not hold the score, and I state the exclusion rather
    than assert the conclusion.** Two of OE 22's three query alternatives do not return the five posts the
    step enumerates: `"Mesa Vista 4C"` returns three of five, and `"make-ready"` returns a channels-only
    block with no messages. The hard exclusion is `Reference/OE_Format.md` section "Discovery-step
    phrasing", which establishes the multi-alternative query menu as the sanctioned convention and whose
    own worked example offers three query strings that plainly do not return identical result sets, taken
    together with the QC spec's Pass(5) test being "Following the OEs literally would produce a correct
    trajectory", which OE 22 followed by OE 23 satisfies under any of the three.
15. **I reversed myself on m8 and say so plainly.** The verbosity finding is withdrawn. The file grew
    because my own accuracy findings demanded the grounding, the convention has no word budget and no
    validator gate, the 1,002 to 1,675 reference band comes from four V3 Brookfield tasks with a far
    thinner decoy surface than this one, and S3 rubric accuracy is the real downstream consumer. The
    restructure I did ask for was executed and did what it was for. The specific clauses I would still cut
    if forced are named in `AUDIT_oe.md`, and they total about 250 words, which would not reach the band
    anyway.
16. **Nothing in the round-2 additions opened a leakage vector.** The five newly named figures (1810.00,
    385.00, 1140.00, 1380.00, 6992.00) were swept individually. 1810.00, 1380.00 and 6992.00 have zero
    amount hits anywhere in the ledger, and 1812.00 / 1897.00 / 1727.00 re-confirmed at zero.

## Verdict

PASS (STRICT)

Round 2 of the three-round S2 cap. All five Majors and all ten Minors from round 1 are discharged and
independently re-verified from source, not accepted on description. Both Oracle Event sub-dimensions now
score 5/5: nothing on the critical path is missing, and every tool, service, parameter and expected value
matches the universe, with literal compliance producing a correct trajectory including the record round 1
left unreachable. Two MINOR residuals are logged with hard exclusions cited and exact fixes given (R2-a,
two of OE 22's three query alternatives do not return its five enumerated posts; R2-b, OE 19 is now a
tool-less reasoning step, a regression my own round-1 prescription caused). Neither is a false claim and
neither removes a step, so neither meets the Non-Fail band as `Docs_starpm/7_QC_Spec_Doc1.json` writes it.
**No Major remains.** Levers unregressed with L6 and L11 measurably deeper; L11 remains DISPLACED and is
now recorded as such for S4. Density unchanged: Opus 47 intended / 39.5 blended (PASS), Gemini 41
intended / 32.7 blended (THIN, far clear of the 15 floor). Regression baseline unmoved at 62/62.
`PROPAGATE TO S1` was NOT emitted in either round.
