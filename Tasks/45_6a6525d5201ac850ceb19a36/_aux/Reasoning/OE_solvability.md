# OE Solvability + Coverage Map — Task 45 (StarPM V4)

Deliverable: `6_Oracle_Events.txt` (15 OEs). Correct outcome = **HOLD / kick-back**: Mesa Vista 4C current turn (recbd087a4abd605b) is NOT marketing-ready. Universe today 2026-07-01.

## Forward coverage (every prompt ask maps to >=1 OE step)

| Prompt ask | OE step(s) |
|---|---|
| Carlos reports 4C "wrapped", wants it listed (latching context) | OE4 (MR-4C-2026-08 "complete" ticket), OE5 (Carlos 5/23 #make-ready "market-ready/good to list") |
| Brooke ready to market on his word | OE8 (resolve Brooke), OE15 (notify Brooke) |
| "run my own pass... the real state of that turn" | OE1-OE9 (full QC investigation + determination) |
| moved out mid-June, target-ready end of month already come and gone | OE1/OE2 (disambiguate to recbd087: move-out 2026-06-15, target 2026-06-30), OE3 (target past due vs today 2026-07-01) |
| deep clean + interior repaint genuinely closed/signed off or still open | OE3 (notes: "still tracking"), OE6 (both bills unpaid) |
| vendor side reconciled; billed-not-finished OR finished-bill-unpaid != closed | OE6 (QuickBooks: Sunshine deep-clean $387 unpaid bill 195089456477; interior repaint $1340 unpaid bill 696089964235; pass-through invoice 445653930748 $1622 unpaid) |
| re-inspection on the calendar mid-month factors into "done" | OE7 (Make-Ready QC Inspection 4C, 2026-07-15, future/confirmed) |
| record QC determination on that turn + give the call | OE9 (determination), OE10 (Airtable write on recbd087) |
| marketing-ready -> sign off; not -> say so plainly and HOLD; no listing until every scope closed+signed off | OE9 (HOLD, the sign-off-OR-kickback decision; L31 explicit negative) |
| open a ticket spelling out exactly what is left | OE11 (Linear issue) + OE12 (Linear comment enumerating each remaining scope) |
| post where it lands in the make-ready channel | OE13 (slack_send_message channel_id C004) |
| get an email together for Carlos with the specifics | OE14 (gmail create_draft to carlos.mendez@starpm.com) |
| if holding, Brooke hears it from us before she markets | OE15 (notify Brooke, goal-level any channel) |

## Reverse coverage (every OE step maps to a real prompt ask)

OE1-OE9 serve "run my own pass / the real state" (implicit investigation ask) and the explicit determination ask. OE10-OE15 are the six explicit/implicit write asks. No OE goes beyond the prompt. **No scope creep.**

## OE -> rubric preview (for S3)

**Outcome 1.1 (one per write action):**
- OE10 -> QC determination recorded on the CURRENT in-progress turn recbd087a4abd605b AND status NOT advanced to Ready (bind by content: mid-June move-out / end-of-June target; recording = update fldNotes2 or a record comment while keeping selProg; never a nonexistent hold enum). Not satisfiable by the prior selReady turn recc8534 nor by either "done" maintenance ticket.
- OE11 -> Linear issue opened (Operations team) for the 4C QC hold.
- OE13 -> Slack post in #make-ready (C004) stating the hold.
- OE14 -> Gmail draft to carlos.mendez@starpm.com.
- OE15 -> Brooke notified (any channel) to hold marketing.

**Outcome 1.2 (content, only if it adds a distinct check beyond 1.1):**
- OE12 -> Linear comment enumerates each remaining scope. S3 must decompose this into one criterion per content element (deep-clean bill unpaid; interior-repaint bill unpaid; make-ready still In Progress with 2026-06-30 target past due; 2026-07-15 QC re-inspection pending) rather than one bundled "lists everything" criterion.
- OE14 -> email body carries the specifics (held, both bills unpaid, In Progress/target past due, 7/15 pending, no listing until closed+signed off).

**Outcome 2.1 (key fact in final response):**
- OE9 / final paragraph -> response states plainly 4C is NOT marketing-ready / held (L31 explicit negative), with the reasons.

**Pure discovery (no rubric; downstream Outcome rubrics prove the reads happened):** OE1, OE2, OE3, OE4, OE5, OE6, OE7, OE8.

**Process rubric candidates:** none obvious. The prompt names a SET of writes, not a strict ordering; the determination logically precedes the writes but any valid write order passes. Default to zero Process rubrics; S3 applies the three-condition test + `check_ordering_coverage.py`.

## Density note (StarPM per-model, target 40+, floor 15)

Discovery (airtable make-ready x2 + maintenance tickets + slack C004 + quickbooks aged-payables/get-bill x2 + calendar + contacts/linear/hubspot) + 6 writes + post-write verify projects ~40-45 per model. Hardness_Plan documents `## THIN density acceptance` (real StarPM runs land 33-38); the 5-6 distinct-write mandate is preserved in OE10-OE15 to hold the floor. Hard S4 gate: per-model avg < 40 -> PIPELINE REDO.

## Council results (both GO)
- **Council A (grounding): GO** — 28/28 concrete values grounded verbatim vs Universe_Split; fldTurnStatus has no HOLD enum (confirmed); single-target uniqueness holds (F7 clean); Jaime QC sign-off/kick-back authority confirmed in persona brief; zero BLOCK. Non-blocking notes: OE5 post-date is the raw UTC date (5/22 in local Chicago) = cosmetic; invoice 445653930748 ($1622) is a receivable, correctly excluded from the pinned hold criteria.
- **Council B (adversarial QC): GO** — OE Completeness 5/5, OE Accuracy 5/5; HOLD uniquely determined (the four "done" decoys are defeated by the prompt's content-pin on the mid-June/end-of-month turn); all 5 hardness levers preserved; 6 distinct writes correctly mapped + channel-appropriate; no B6 upstream propagation. Density THIN per-model (~30 Opus / ~26 Gemini; empirical StarPM anchor 33-38) — pre-accepted per Hardness_Plan; S4 sub-40 REDO gate live.

## S3 carry-forwards (Council B — 3 Minor, none block S2)
1. **OE12 Linear comment**: "open a ticket spelling out what is still left" is satisfiable by OE11's issue DESCRIPTION alone. S3 must NOT bind a hard rubric to "a distinct Linear comment artifact exists" (Overly Specific / F8 non-atomic risk). Phrase the enumeration coverage so the four remaining items can live in the issue description OR a comment. Keep OE12 as a density write, not a separately-graded artifact.
2. **OE5 attribution** "Carlos Mendez": grounded (Council A confirmed slack user U07E4512181 = Carlos Mendez). Cosmetic; "onsite-PM chatter" is equally safe if S3 quotes it.
3. **Density THIN**: enforce the S4 per-model avg < 40 -> PIPELINE REDO gate. Not an S2 defect.

## AUDIT (--phase oe) — round 1: REVISE (PROPAGATE TO S1), adjudicated to S2, fix applied, re-verify pending

**AUDIT round-1 finding [MODERATE]:** a rule-13 QuickBooks sweep found FOUR unpaid "Mesa Vista 4C" entity_type=bill rows due 2026-05-31, not the two OE6 originally named; OE6/OE9 presented a bounded outstanding set. AUDIT flagged PROPAGATE TO S1 (claimed root cause = the prompt's "the vendor side reconciled too").

**Orchestrator adjudication (rule 19, quote-backed): root cause is S2, NOT S1.** The prompt names exactly two scopes verbatim: "The two scopes that carried this turn were the deep clean and the interior repaint" — the vendor clause is bound to those two. Re-read of the two extra $85 bills confirms neither is a named carrying scope:
- 991582431419 (doc 2026-481-566, $85): line "Unit condition inspection and punch list documentation"; PrivateNote "Internal labor charge for Carlos Mendez's make-ready walk ... turnover intake process" = a THIRD scope (intake-walk labor), NOT the deep clean or the interior repaint.
- 546359391323 (doc 2026-519, $85): line "Bedroom closet trim paint touch-up ... following final QC walkthrough"; PrivateNote "... 4C make-ready close-out" = the PRIOR turn's close-out (matches selReady recc8534's closet-trim narrative), NOT the current turn.
The prompt is therefore already bounded and not defective; no S1 re-run warranted.

**Fix applied in place (OE6):** OE6 now acknowledges the full four-bill get_aged_payables sweep (closes the rule-13 omission-blind gap), maps the two carrying scopes to bill 195089456477 ($387 deep clean) + 696089964235 ($1340 repaint), explicitly sets aside 991582431419 (intake-walk labor) + 546359391323 (prior-turn close-out) with grounded reasons, clarifies 445653930748 ($1622) is a receivable (corroboration only), and concludes the determination turns on the two named scopes. validate.py --phase oe = PASS; atom-verifier = 0 fails, 1 benign 7/15 WARN; both new bill IDs grounded.

**S3 note (added carry-forward):** bind vendor-bill rubrics to the two carrying scopes ONLY (deep-clean bill unpaid; interior-repaint bill unpaid). Do NOT require the two $85 charges (intake-inspection / prior-turn touch-up) — a rubric requiring them would be Overly Specific and would false-fail a correct agent that scopes to the two prompt-named scopes.

**Re-verify (REVISE round 1) — RESOLVED, all three gates clear:**
- **AUDIT resume bg_914b9088 = PASS (STRICT).** Conceded both round-1 errors on quote-backed re-read: (a) PROPAGATE-TO-S1 withdrawn (prompt names exactly two scopes, not unbounded); (b) "991582431419 in scope" retracted (its line is inspection/documentation labor, a third scope, not deep clean or repaint). Agreed the set-aside disposition is better than its own S2 fallback (forcing the $85 bill into outstanding items would drive an Overly Specific S3 rubric). Gates re-run: validate PASS, atom-verifier 0/1-benign, regression 62/62.
- **Council A resume bg_fae4dc9e = GO.** Both new bill atoms grounded verbatim; "four bills" confirmed exact (paid property-level landscaping bill GH-0526 correctly outside the unit sweep); 445653930748 confirmed receivable (resolves its prior Obs-2); carrying-scope bills unchanged; 0 dashes. Revision tightens the determination.
- **Council B fresh bg_8a5579aa = GO.** OE Completeness 5/5 (improved, closes rule-13 gap), OE Accuracy 5/5; four-bill sweep exhaustive + correctly typed (invoice vs bill); set-aside defeats the conflation decoys; HOLD uniquely determined; no scope creep; no dashes.

## Consolidated S3 carry-forwards (from Council B + AUDIT, all Minor, none block S2)
1. Bind the unpaid-scope vendor rubrics to the two carrying scopes ONLY, by content ($387 deep-clean bill + $1340 interior-repaint bill). Do NOT create a criterion requiring the agent to enumerate / classify / exclude the two $85 bills (Overly Specific = MODERATE; false-fails a correct two-scope HOLD).
2. Do NOT bind any rubric to the recc8534 attribution of the $85 closet-trim bill (546359391323) — it is a grounded inference ("following final QC walkthrough" + current turn's QC still future), not a hard field. It is oracle set-aside rationale only.
3. OE12 Linear comment: accept the four-item enumeration in the issue DESCRIPTION or a comment; no distinct-comment-artifact rubric (F8 risk).
4. OE5 "2026-05-23" is the raw UTC date (5/22 local) — cosmetic; "onsite-PM chatter" equally safe if S3 quotes attribution.
5. Density THIN per-model (~30 Opus / ~26 Gemini; empirical 33-38): enforce the S4 per-model avg < 40 -> PIPELINE REDO gate (Hardness_Plan mitigation #2 / AGENTS.md rule 11).
6. QC-status rubric (Outcome 1.1) binds to recbd087a4abd605b: "did NOT advance to Ready" + "recorded the QC hold determination" (fldNotes2 update or record comment) — never a nonexistent hold enum; not satisfiable by either "done" maintenance ticket (reca424) or the prior selReady turn (recc8534).
