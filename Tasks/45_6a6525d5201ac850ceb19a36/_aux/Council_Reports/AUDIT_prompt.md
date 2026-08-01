# AUDIT - S1 PROMPT (Veteran QC, strictest interpretation)

**Task:** `45_6a6525d5201ac850ceb19a36` · **Universe:** starpm (V4, dual-model Opus 4.8 + Gemini) confirmed via `_aux/Universe.txt` (`#QV|starpm`) · **Today:** 2026-07-01 America/Chicago
**Deliverable:** `5_Prompt.txt` (275 words) · **Mode:** READ-ONLY (no edit made)
**Correct answer:** KICK-BACK / HOLD (current turn `recbd087a4abd605b` = selProg, deep-clean + interior-repaint "still tracking", 6/30 target past-due, two unpaid vendor bills, 7/15 QC re-inspection pending) while a maintenance ticket + a prior completed turn both say "done".
**Prior councils:** S1_A (grounding) GO after delta; S1_B (adversarial) GO after delta. This audit hunts what both missed.

## Deterministic gates (cited, not re-derived)
- `validate.py --phase prompt`: PASS (0 fails, 0 warns, 4 notes); word count 275. Independently corroborated: my byte scan = 275 words, dash-codepoint scan (U+2012/2013/2014/2015/2212) = 0 hits.
- `calc_similarity.py`: max composite 31.2 < 40 (top match Task 44, StarPM). PASS.
- `test_regression_anchors.py`: 62/62 PASS (Lens 8).
- `check_qc_binary.py` / `check_ordering_coverage.py`: N/A at prompt phase (require `7_Rubrics.json`; run at S3). Prompt binary sub-dims scored directly in Lens 1.
- 4 validator NOTES exist; their bodies were not provided to this audit. Under strictest policy each should be eyeballed by the operator; from the clean fails/warns they are informational (word-count / dash / tool-token / date-phrase class), not blockers.

## Ground-truth re-verification (my own grep of `_aux/Universe_Split/airtable.airtable_records.json`, not the plan's claims)
| Record | Table | Status enum | Distinguishing content | Role |
|---|---|---|---|---|
| `recbd087a4abd605b` | tblMakeReady | **selProg** (In Progress) | fldMoveOut **2026-06-15**, fldTargetReady **2026-06-30**, fldNotes2: faucet/GFCI/drywall done, "Deep clean and interior repaint **still tracking** ... Will update status to Ready once all vendor and in-house scopes are signed off" | **TRUTH - current turn, NOT ready** |
| `recc8534b3fd13954` | tblMakeReady | selReady (Ready) | fldMoveOut 2026-06-01, fldTargetReady 2026-06-14, "Unit confirmed ready for leasing"; created 2026-05-29 (LATER than recbd087's 05-22) | DECOY - prior completed turn |
| `reca424761ae15355` | tblMaintenanceTickets | selHigh | MR-4C-2026-08, "All make-ready work at Mesa Vista 4C is complete ... market-ready ... Brooke Phillips has been notified to move forward with listing", fldCompletionDate 2026-05-01 | DECOY - "done" ticket |
| `rec12969a3fdb0852` | tblMaintenanceTickets | selHigh | MT-2026-084, "Make-ready turn opened for unit 4C at Mesa Vista ... full unit turnover scope initiated", fldCompletionDate 2026-05-01 | DECOY - turn-open ticket |

Confirmed this pass: **`fldTurnStatus` singleSelect choices = {Scheduled, In Progress, Ready}** (no Hold / Kickback / Fail value - see F2). 7/15 "Make-Ready QC Inspection - Mesa Vista 4C" (`0hjw400x...`) `status=confirmed` on `carlos.mendez` / `wesley.tran` / `brooke.phillips` calendars, NOT `jaime.salinas`. Scope bills `195089456477` (Sunshine / deep clean) + `696089964235` (Permian / interior repaint) exist; balances 387 / 1340 unpaid are councils-verified and consistent with Fact_Ledger amounts (`387.00`, `1340.00`).

Census note: Council B's "4 records (2 make-ready + 2 tickets)" is correct; Council A and the Hardness Plan say "3". Immaterial to F7 (dates pin the make-ready row); carry the two-decoy-ticket correction to S3.

---

## LENS 1 - Strict QC scoring (Docs_starpm/7_QC_Spec_Doc1.json), bar = 5
| Sub-dim | Score | One-line reason | What prior council under-weighted |
|---|---|---|---|
| Unique Ground Truth | 5 | Single end-state = HOLD; selProg + still-tracking + past-due 6/30 + two unpaid bills, doubly locked by the prompt's own "billed-but-unpaid = not closed" rule. Sign-off reachable only by latching. | Nothing. Agreed. |
| Feasibility | 5 | Every ask maps to a tool; every load-bearing fact exists and is retrievable. | The Airtable "set QC status" ask has **no enum value for HOLD** (F2). Feasible via notes/keep-selProg, so not a Feasibility fail, but neither council checked the enum. |
| Explicit Tool Mention | 5 (binary) | No MCP tool/function names; "issue tracker / make-ready channel / get an email together / set the QC status / put it on record" are natural artifact references. | Agreed. |
| Clarity & Specificity | 5 | One coherent investigate-then-record ask; sign-off/hold conditional resolves by data to one write action (hold). | "Set the QC status" is loose for the hold branch (F2); correct branch ("hold it ... does not go to listing") is unambiguous, so 5 stands - flagged not buried (Lens 7). |
| Contrived / Unnatural | 5 | Natural QC scenario in Jaime's voice; difficulty is conflicting cross-service data, not arbitrary constraints. | Agreed. |
| Alignment with Today's Date | 5 | 6/15 past, 6/30 "come and gone" (one day past, accurate on 7/01), 7/15 future event permitted. | Agreed. |
| Truthfulness | 5 | Per-atom table below; all asserted atoms grounded. | "two scopes ... deep clean and interior repaint" is a persona narrowing of a 5-item turn (F3) - grounded, but neither council registered the omitted-internal-items simplification. |
| Tool Use & Cross-service | 5 (binary) | Reconciliation spans Airtable + QuickBooks + GCalendar + Contacts + Slack + Linear + Gmail. | Agreed. |
| Investigation + Action | 5 (binary) | Heavy investigation feeds 4-5 writes; cannot act without reconciling. | Agreed on requirement; but the prompt scaffolds discovery enough to *shorten* it (F1/F4). |
| Coherence / Bolt-on | 5 (binary) | Remove-a-sentence: every ask flows from the single QC-decision situation. | Agreed. |
| Persona | 5 | Jaime = impartial QC sign-off/kick-back anchor; voice short/factual/observation-first. | Agreed. |
| Business Function | 5 | BF3 Quality Control & Field Services - squarely in-function. | Agreed (council-prompt "cat 5" vs doc "Cat 3" is a label quirk, not a defect). |

**All 12 prompt sub-dims = 5.** (Trajectory sub-dim **Tool Call Count** is not a prompt sub-dim; it is a projection here and is scored against real runs at S4 - see Lens 4, where it is THIN.)

### Truthfulness per-atom evidence (required for 5/5)
| Atom asserted in prompt | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Carlos has 4C "wrapped ... released for listing" | airtable `reca424` + slack C004 | "All make-ready work ... complete ... market-ready ... Brooke Phillips has been notified to move forward with listing" | SUPPORTED |
| Brooke would list/market on his word | airtable `reca424` + persona index | "Brooke Phillips ... notified to move forward with listing"; persona = Apartment Property Supervisor | SUPPORTED |
| moved out middle of June | airtable `recbd087`.fldMoveOut | "2026-06-15" | SUPPORTED |
| target-ready end of month, come and gone | airtable `recbd087`.fldTargetReady vs today | "2026-06-30" (today 2026-07-01) | SUPPORTED (past-due) |
| two scopes = deep clean + interior repaint | airtable `recbd087`.fldNotes2 | "Deep clean and interior repaint still tracking on their respective schedules" | SUPPORTED (as the two open/vendor scopes; internal punch items existed but done - F3) |
| billed-but-unpaid vendor scopes | quickbooks `195089456477` (Sunshine/deep clean) + `696089964235` (Permian/repaint) | both `entity_type=bill`, balances 387 / 1340 unpaid (councils-verified; ledger has 387.00, 1340.00) | SUPPORTED |
| re-inspection mid-this-month on the calendar | gcalendar `0hjw400x...` | "Make-Ready QC Inspection - Mesa Vista 4C" 2026-07-15 `status=confirmed` | SUPPORTED ("on the calendar" true; on Carlos/Wesley/Brooke) |

Evidence column non-empty on every row -> Truthfulness 5 upheld.

---

## LENS 2 - Answer-leakage
Correct conclusion = "4C NOT ready -> HOLD" and its derived figures ($387 / $1,340, selProg, past-due).
- Derived-figure scan: no dollar amounts, no "selProg"/"In Progress"/status codes, no record IDs in the prompt. **No derived figure leaked -> no BLOCKER.**
- Conclusion scan: prompt never asserts "not ready". It presents Carlos's "wrapped" claim as bait (line 1) and asks a neutral sign-off-OR-hold verification (line 5). Correct.
- **Vocabulary near-miss (not a BLOCKER):** the prompt's phrase **"still tracking"** is the verbatim discriminator string in `recbd087`.fldNotes2, and it names **both** exact open scopes. It is used in a genuinely conditional frame ("whether both are genuinely closed and signed off **or** still tracking"), so it asserts nothing - it does not meet the "derived figure asserted" BLOCKER bar. But priming the exact status phrase + the two exact scopes lets a keyword/semantic-searching agent jump straight to the target row, shortening required discovery (compounds the Lens-4 density finding). Logged as F4 [MINOR].

**Lens 2 verdict: no BLOCKER.** One MINOR hardness-erosion vocabulary note (F4).

---

## LENS 3 - Hardness end-to-end (each lever -> surfacing sentence)
| Lever | Surfacing prompt sentence | Status |
|---|---|---|
| L2 structured-DB skip (SYMMETRIC) | "before anyone lists it I need the real state of that turn" + "whether both are genuinely closed and signed off or still tracking" | PRESERVED - forces the SoR make-ready row over chatter/ticket. |
| L1 latching (OPUS-SEL) | "Carlos has Mesa Vista 4C down as wrapped ... Brooke is ready to put it on the market on his word." | PRESERVED - explicit "done" bait. |
| L10 supersession (OPUS-SEL) | "its June turn ... moved out in the middle of June with a target-ready date at the end of the month" | PRESERVED (subordinated to F7 date-pin per Council B; the trust-the-done-ticket variant survives). |
| L31 explicit negative directive (GEMINI-SEL) | "if it is not, say so plainly and hold it, because it does not go to listing until every outstanding scope is closed and signed off ... Brooke needs to hear it from us before she markets it." | PRESERVED + GROUNDED - the do-not-market negative is an explicitly requested output (avoids Task-39 "phrase never asked"). |
| L7 multi-write | "Set the QC status ... Open a ticket ... post where it lands in the make-ready channel ... get an email together for Carlos ... Brooke needs to hear it from us." | PRESERVED - 4-5 writes across 4 services. |
| L9 future-event | "There is also a re-inspection on the calendar for the middle of this month, and it factors into whether I can call this one done." + "target-ready ... already come and gone." | PRESERVED + F9-clean (no "only open item" over-claim). |

**Every lever traces to a prompt sentence. No HARDNESS_REGRESSION.** OE-step + rubric-column mapping is N/A at prompt phase -> **carry to S2/S3.**

---

## LENS 4 - Strict density (StarPM per-model: >=40 PASS, 15-39 THIN, <15 BLOCKER)
**This is the audit's material disagreement with both councils.** Council B projected Opus ~43 / Gemini ~41 by counting a *thorough* trajectory (16 discovery + 8 reconcile + 4 L9 + 9 writes + 4 buffer = 41) and labelled the margin "thin" - but neither council performed the **minimizing** sketch the audit mandates.

Minimizing-but-correct-and-compliant trajectory (batched reads, no post-write re-reads, skip non-load-bearing Slack):
| Component | Minimizing calls |
|---|---|
| airtable get tblMakeReady + tblMaintenanceTickets (2 rows + 2 tickets returned in-list) | 2-3 |
| quickbooks reconcile 2 vendor bills + balances | 2-4 |
| gcalendar cross-calendar search for 7/15 (not on own cal) | 2-3 |
| contacts resolve Carlos (+ Brooke) | 1-2 |
| slack #make-ready context (skippable for the answer) | 0-1 |
| writes: airtable notes/status + Linear issue + Linear comment + Slack post + Gmail draft (+ Brooke) | 5-6 |
| post-write verify (minimizing agent skips) | 0 |
| **Per-model total** | **~15-28, midpoint ~21** |

~21 is **THIN**, and the low end (~15-18) brushes the INSUFFICIENT floor. The Hardness Plan's own L33 note records real StarPM runs landing **33-38 per run** - also THIN, below 40. So the councils' clean ">=40" is not robust: it holds only for a thorough agent, while both the minimizing sketch and the plan's own empirical note land in the THIN band.

Aggravators specific to this prompt: (a) F1/F4 discovery-scaffolding ("two scopes named" + verbatim "still tracking") lets a keyword agent shortcut the sweep; (b) F2 - because the correct outcome (hold) leaves `fldTurnStatus` unchanged (already selProg), the "Airtable status write" can collapse to a no-op on the correct path, subtracting a write from the count.

**Lens 4 verdict: THIN (>=15 floor cleared, no BLOCKER; below the >=40 PASS(STRICT) bar).** Challenges and does not confirm Council B's 41-43.

---

## LENS 5 - Adversarial veteran checklist
| Check | Result |
|---|---|
| Implicit QC framing, no pre-solve of "not ready" | PASS - conditional sign-off/hold; state never asserted. |
| Entity drift | PASS - Carlos Mendez / Brooke Phillips / Jaime (first-person) all verified. |
| Single-channel lock-in where only a goal was needed | PASS - the ticket/channel-post/email are legitimate distinct-audience write mandates (density-intended); the **Brooke** notification is goal-only ("needs to hear it from us", no channel named) = correctly open. Carry to S3: the Brooke-notify rubric must accept any channel. |
| Tool-name leaks | PASS - 0. |
| em/en/figure dashes | PASS - 0 (hyphens in target-ready / re-inspection / make-ready are ASCII). |
| Internal IDs | PASS - 0. |
| "at least N" | PASS - absent. |
| "approximately" / "(or similar)" near values | PASS - absent. |
| F7: "mid-June move-out + end-of-June target" uniquely pins current turn | PASS - `recbd087` (6/15 // 6/30) unique; prior turn is 6/01 // 6/14; date content excludes it; 7/15 re-inspection further pins. |

One non-checklist adversarial note already covered: F1/F4 discovery scaffolding.

---

## LENS 7 - Anti-rationalization sweep
Every "considered flagging but it's fine" line is promoted to a listed finding unless a hard exclusion is cited:
- "still tracking" verbatim + two scopes named -> **promoted** to F1/F4 [MINOR] (hard exclusion from BLOCKER: conditional framing, no derived figure asserted; but not dismissed - it erodes density).
- "Set the QC status" kept at Clarity 5 -> **promoted** to F2 [MINOR prompt / MODERATE S3 carry] (hard exclusion from a 4: the correct branch "hold it ... does not go to listing" is unambiguous; only the status-verb is loose).
- "two scopes that carried this turn" simplification -> **promoted** to F3 [MINOR] (hard exclusion from a Truthfulness fail: both named scopes are grounded as the open/vendor scopes; the omitted internal punch items are done).
- bill TxnDate 2026-05-01 predates the 6/15 move-out -> **excluded** (hard: prompt cites no bill dates; universe-internal noise) -> S2 grounding carry only.
- density "thin margin" -> **promoted** to the headline (F-DENSITY), not softened.

---

## LENS 8 - Regression anchors
`test_regression_anchors.py`: **62/62 PASS.** No validator regression.

---

## Findings
- **F-DENSITY [MODERATE, non-blocking].** Per-model density is **THIN**, not the >=40 both councils asserted. Minimizing sketch ~21; plan's own L33 empirical note 33-38. Clears the 15 floor -> not a BLOCKER, but fails the clean PASS(STRICT) >=40 bar. **Fix (downstream, no prompt-text edit required):** (1) S2/S3 must preserve **5-6 distinct writes** (Airtable determination-on-record, Linear issue, Linear comment enumerating each remaining scope, Slack C004 post, Gmail draft to Carlos, Brooke notification as its own write) - do not collapse to 3; (2) set a hard **S4 gate: per-model average < 40 -> REDO** (AGENTS.md rule 11). Optional prompt-side lever to raise the minimizing floor: soften the verbatim "still tracking" and/or the pre-named two scopes (trades against clarity - operator's call).
- **F2 [MINOR prompt / MODERATE S3 carry].** `fldTurnStatus` enum = {Scheduled, In Progress, Ready}; there is **no HOLD/kickback value**. The correct outcome (hold) = keep selProg + record the determination; "Set the QC status on the turn" (line 5) has no valid enum target for that branch and can collapse the Airtable write to a no-op. **Fix:** S3 write-action rubric on the make-ready record must bind to the current turn (`recbd087`, mid-June move-out) and check **"did NOT advance to Ready" + "recorded the QC hold determination"** - it must **not** require a nonexistent hold status value. Optional prompt clarify: "record your QC determination on that turn's record" reads cleaner than "set the QC status" and guarantees an Airtable write exists on the correct path.
- **F1 / F4 [MINOR].** Discovery scaffolding: the prompt names both exact open scopes and uses the target row's verbatim "still tracking", letting a keyword agent shortcut the reconciliation sweep -> compounds F-DENSITY. Non-blocking; consider softening if the operator also acts on F-DENSITY.
- **F3 [MINOR].** "the two scopes that carried this turn were the deep clean and the interior repaint" narrows a 5-item turn (3 internal items done + 2 vendor scopes tracking) - grounded and natural for a QC persona, logged for completeness.

## Carries to S2/S3
- Census: 4 records (2 make-ready + **2** decoy "done"-flavored tickets); bind the QC-status rubric to `recbd087` current turn, satisfiable by neither ticket nor the prior selReady row.
- Cross-calendar discovery: the 7/15 event is on Carlos/Wesley/Brooke calendars, not Jaime's - OE/discovery must search beyond the actor's default calendar (it also aids density).
- OBS carries: repaint vendor = Permian (not the calendar-event's Pete Donovan); bill TxnDate 5/01 chronology noise - ground "not closed" on selProg + unpaid balances, not calendar dates.
- Brooke-notify rubric = goal-only, must accept any channel.

## Disposition
Zero BLOCKER. All 12 prompt sub-dims = 5. Zero leaked derived figures. Every lever traces to a prompt sentence. The **only** obstacle to a clean PASS(STRICT) is F-DENSITY: under the mandated minimizing reading (and the plan's own L33 empirical note) per-model density is THIN, not the >=40 the audit's PASS(STRICT) conjunct requires. Because THIN is explicitly non-blocking (>15) and documented, this is a **soft REVISE**, not a REBUILD: the prompt TEXT is sound. If the operator accepts the documented THIN justification and installs the mandatory S4 per-model density gate, this converts to a conditional PASS; under the strict letter of the >=40 bar it is REVISE.

VERDICT: REVISE -- [MODERATE] per-model density THIN (~21 minimizing / 33-38 real per L33), not the >=40 councils claimed -- Tasks/45_6a6525d5201ac850ceb19a36/5_Prompt.txt (whole-trajectory projection; no BLOCKER, clears the 15 floor) -- FIX: preserve 5-6 distinct writes through S2/S3 + hard S4 gate (per-model avg <40 -> REDO); [MINOR] fldTurnStatus has no HOLD enum -- line 5 "Set the QC status on the turn" -- FIX: S3 rubric checks "not advanced to Ready" + "hold determination recorded", never a nonexistent status value (optionally reword to "record your QC determination on that turn's record").

## Re-review (delta) -- 2026-07-27 (veteran QC, strictest interpretation)

**Trigger:** prior REVISE (above) on F2 [MINOR] + F-DENSITY [MODERATE]. Both edits landed; re-verified against the current `5_Prompt.txt` (271 words, validator PASS 0/0), the Hardness_Plan THIN-acceptance + census-correction sections, and a re-grep of Universe_Split. Council A/B continuation sessions expired; this Lens-1 re-grounding + full sub-dim rescore is a superset of their checks under a stricter bar.

### F2 -- RESOLVED
- Line 5 now reads *"record your QC determination on that turn"* (was *"Set the QC status on the turn"*). Grep-confirmed: the old string "Set the QC status" is absent from the file.
- Grounding: the anaphor chain (line 1 "the real state of that turn" -> line 3 "this turn" -> line 5 "that turn") pins the June turn by content (6/15 move-out, 6/30 target past-due, 7/15 re-inspection) = `recbd087a4abd605b` (selProg), never the prior selReady `recc8534` (6/01 // 6/14) nor either maintenance ticket.
- Hold-path validity: "record your QC determination" is a determination-write onto the current make-ready record, satisfiable via an `airtable` update to a notes/determination field with `fldTurnStatus` left at selProg. It no longer depends on a HOLD/kickback value absent from the {Scheduled, In Progress, Ready} enum. The no-op trap is closed: a valid write exists on BOTH branches.
- Side effect: STRENGTHENS L31 (the do-not-market negative now has a concrete write target) and removes the prior Feasibility caveat outright. No new ambiguity -- "your QC determination" is bound by the immediately preceding clause ("sign it off ... or ... hold it").

### F-DENSITY -- RESOLVED (documented-and-mitigated THIN, AGENTS.md rule 11)
- Prompt-side floor-raiser landed: line 3 now reads *"or still open"* (was *"still tracking"*), breaking the verbatim match to `recbd087`.fldNotes2. Grep-confirmed "still tracking" is absent from the prompt; the keyword shortcut to the target row is gone, marginally lifting the minimizing-agent floor. "still open" is a faithful paraphrase -- Truthfulness intact, and the prior Lens-2 F4 vocabulary near-miss is now eliminated, not merely non-blocking.
- Hardness_Plan "## THIN density acceptance" (lines 106-118) documents all three required elements: (a) per-task justification (floor 15 cleared with wide margin; prompt text sound; no bolt-on lever reaches 40 without failing Coherence); (b) the 5-6 distinct-write mandate for S2/S3 (Airtable determination on recbd087 + Linear issue + Linear comment + Slack C004 + Gmail draft + Brooke-notify); (c) the hard S4 gate (per-model avg <40 -> PIPELINE REDO). "## Record census correction" (lines 120-122) fixes the 3->4 record count (2 make-ready + 2 tickets), strengthening the latching bait.
- Per this report's own stated conversion condition and AGENTS.md rule 11, documented+mitigated THIN with the S4 REDO gate is an acceptable prompt-phase resolution. Not re-flagged as a fresh REVISE.

### New-issue scan (both edits) -- NONE
- All 12 prompt sub-dims re-scored: still 5/5. Feasibility and Clarity are now clean 5s (their F2 caveats resolved); none dropped.
- Answer-leakage: no derived figure, status code, or record id added; the symmetric sign-off-OR-hold conditional is preserved; "record your QC determination" and "still open" assert nothing about the outcome. No BLOCKER.
- Levers: L2 (structured-DB skip) + L1/L10/L31/L7/L9 all still trace to a prompt sentence; L31's hold-write path is now grounded to a concrete write. No HARDNESS_REGRESSION.
- Dashes: 0 introduced. Word count 271 < 500; validator PASS. Gates re-confirmed: validate.py --phase prompt PASS (0/0, 271w); calc_similarity 30.8 < 40; test_regression_anchors 62/62; verify_universe_atoms PASS.

### Disposition (delta)
Both REVISE findings resolved by sound prompt-text edits that improve, not merely patch, the two weak spots; zero new issue; all 12 sub-dims 5/5; zero BLOCKER; zero leaked figure; every lever preserved. The only residual (THIN density) is documented-and-mitigated with the mandatory S4 REDO gate per rule 11. Carries to S2/S3/S4 unchanged (5-6 distinct writes; bind the QC-status rubric to recbd087 checking "did NOT advance to Ready" + "recorded the QC hold determination"; Brooke-notify rubric accepts any channel; S4 REDO on any sub-40 per-model average).

VERDICT: PASS (STRICT) -- F2 resolved (line 5 "record your QC determination on that turn" grounds to recbd087, valid write on both branches, no nonexistent-enum dependency) and F-DENSITY resolved (line 3 "still open" floor-raiser applied; THIN accepted with per-task justification + 5-6-write mandate + hard S4 per-model <40 REDO gate documented in Hardness_Plan, per AGENTS.md rule 11); all 12 prompt sub-dims 5/5, zero BLOCKER, zero leaked figure, every lever preserved; no new fix-in-place issue introduced by either edit -- Tasks/45_6a6525d5201ac850ceb19a36/5_Prompt.txt
