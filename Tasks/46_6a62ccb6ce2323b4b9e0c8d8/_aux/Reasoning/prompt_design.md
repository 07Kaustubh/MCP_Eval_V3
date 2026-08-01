# S1 Prompt Design Report

**Task** `Tasks/46_6a62ccb6ce2323b4b9e0c8d8` · **Universe** starpm (V4, dual-model) · **Universe today** 2026-07-01 America/Chicago
**Final state:** revision 5, 261 words, 0 em-dashes. Validator PASS (0 fails / 0 warns / 3 services).
**Verdicts:** Council A **GO** · Council B **GO** · AUDIT **PASS (STRICT)** · Similarity **27.8** (ceiling 40).

## What the prompt asks

Lisa Smith is a day late on her half of the mid-year owner package. She owns Harry Harris and Robert
Finley under Brooke's split; drafts were due to owners before end of June and today is July 1. She
asks for the real position on each owner, correction of any unit/turn record that does not match the
ground, correction of either owner's review meeting if it did not end up settled, and four
deliverables: an email to Brooke, an update on the mid-year review item, a new item for what is
unresolved, and a post in owner relations.

Six writes across five services: gmail (draft), linear x2, slack, gcalendar, airtable.

## Levers engineered in (all 5 preserved)

| Lever | How the prompt surfaces it | Withheld inference |
|---|---|---|
| **L1** latching | "I gave Brooke a rough read on my two earlier in the spring, so a fair bit of this should just be confirming it" | That anything she reported was wrong |
| **L2** structured-DB skip | "anything on the money side either of them is likely to raise with me" | That money lives in the books, not the chatter |
| **L10** reversal/supersession | "Do the same for their review meetings if either of those did not end up properly settled" | That a review was duplicated, superseded, or never took |
| **L11** net-vs-gross | rides L2's money clause plus "with the specifics in it" | That credits exist and are unapplied |
| **L7** multi-write | the four named deliverables plus two correction licences | n/a |

**The governing constraint was L36 (withheld inference), not trap density.** Task 45 shipped on this
same universe at Opus pass@1 = 100% because its prompt named its own discriminators. This prompt
names only the two owners and the missed deadline. No figure, no property, no discrepancy, no record
state, no service.

## Expected stump targets

H1 unapplied credit memos silently netted or ignored (SYMMETRIC) · H2 Lisa's own May claim repeated
rather than reconciled (OPUS-SELECTIVE) · H3 the double-booked Harris review reported as a clean
reschedule (SYMMETRIC) · H4 "all four owner reviews are confirmed" accepted at face value
(GEMINI-SELECTIVE; David Shea confirmed at 0 of 565 calendar rows).

## Density

Opus **63.5** / Gemini **66.0** against the V4 design target of 40 (floor 15), applied per model.
Margins +23.5 and +26.0. A transient THIN risk (Opus floor ~37-40) existed at revision 4 and was
removed at revision 5; see below.

## Similarity

Max composite **27.8** against a 45-prompt corpus. Top match `QC_Tasks/V3_Tasks/Task13` at 27.8.
The one that matters is **Task 40 at 27.5 with multiplier 1.000**: same persona, same business
function, so NO contextual-differentiator credit was applied and that number is pure lexical
distinctness. The pivot from Task 40 (single tenant's unit turn, Airtable + email) to this task
(two-owner portfolio reporting, receivables + calendar) is genuine, not weighted.

## Revision history and what each round cost

| Rev | Change | Why |
|---|---|---|
| 1 | first draft, 252 w | - |
| 2 | named email / issue tracker / owner relations channel | Validator FAIL: cross-service needs 2+ service references. Satisfied from DELIVERABLE surfaces only, leaving investigation surfaces unnamed to preserve L2. |
| 3 | merged the deadline clause into sentence 1 | Bolt-on WARN was a regex artifact (`NAMED_ENTITY_RE_PROMPT` tokenises consecutive capitals, so "The Harris" never matched "Harry Harris"). Fixed structurally, not suppressed. |
| 4 | "our own records ... what you find" -> "the unit and turn records ... on the ground" | **Council B BLOCK.** Para 2 scopes the investigation to include "anything on the money side"; para 3's "what you find" carried the correction mandate into QuickBooks by anaphora, where all six Harris/Finley credit memos read `RemainingCredit 0` with `Balance == TotalAmt` and no `LinkedTxn`. The agent that reasoned CORRECTLY about L11 was the one pushed into an unplanned write moving Finley $10,980 -> $7,325. Gradient inversion, hence BLOCKER not MODERATE. |
| 5 | "anything on the scheduling side" -> "their review meetings"; split into two sentences | **AUDIT REVISE.** The phrase denoted **Airtable, not Calendar**: `fldTurnStatus` has an option literally named Scheduled (43/120), a field literally named `fldTargetReady`, 99/120 rows past target and not Ready, and both owners have a qualifying row. "Do the same" inherited the correction verb across a comma splice, so an agent could discharge the clause inside Airtable and never open Calendar, making the calendar criterion beyond-prompt. |

## What the gates actually caught (worth keeping)

- **Council B overturned Council A under rule 19.** Council A found the money-clause ambiguity, called
  it MODERATE, and declined it as an S2/S3 problem. Council B validated it as real and blocked. Rule
  19 exists precisely for this and it worked.
- **AUDIT overturned BOTH councils.** They debated the scheduling clause on one axis only, whether it
  over-signposted, and never asked what it denotes. AUDIT's diagnosis: they did not agree themselves
  into a leak, they agreed themselves into an artificially narrow option set (keep vs delete, never
  reword). The third option existed and worked.
- **`check_council_yield.py` flagged Council A DECLINE-HEAVY (6/11) and the flag was predictive twice.**
- **A Hardness Plan error was caught and corrected.** It certified the Harris calendar pair as "safe to
  pin (distinct base ids)". Calendar stores one row per invitee calendar, so those ids match 5 and 4
  rows. Both councils repeated the claim; Council A had `copies: 5` / `copies: 4` in its OWN iteration-1
  output and did not connect it. Root cause: the uniqueness check was run against Airtable, where one
  record is one row, then carried to Calendar without re-deriving against Calendar's storage shape.
- **The calendar defect is not Harris-only.** Verified at S1: Finley's mid-year review is 05-19
  11:45-13:15 against a comment saying "first week of June, 60 minutes in the afternoon", with ZERO
  Finley events in 06-01..09; Lisa and Aurora both declined it; and the Harris original is 30 minutes
  at midday on June 2 against a Slack note promising a 45-minute morning call in late June.

## Open items for downstream phases

Full list in `_aux/Todos_s1.md` and in the four correction sections appended to `_aux/Hardness_Plan.md`.
The load-bearing ones:

1. **Never pin a bare calendar base id** (F7). Pin the per-calendar row or describe by content plus calendar.
2. **Calendar accept-set must span `update_event` / `delete_event`** and must never require
   `respond_to_event` on the Harris Rescheduled event, where Lisa has no row.
3. **"May Owner Report Review - Finley Properties" is an F7 near-miss.** Pin by full title.
4. **L11 has no Outcome 1.1 carrier** and is gradable only via 1.2 / 2.1. AUDIT ruled this correct
   (giving it a write carrier reintroduces the blocked defect) but it must be explicitly budgeted at
   S3 or it vanishes at the 60-criterion ceiling. Never cut a lever carrier (rule 14).
5. **`tblMaintenanceTickets` writes are beyond-prompt.** Four fields, no unit field. Maintenance is
   read-and-report. AUDIT adjudicated for Council A over Council B.
6. **Zero Process rubrics remains valid** (rule 23): all 6 `ORDERING` patterns return zero hits.
7. **Business Function** is an agreed 5/5 but recorded for FINAL, because Council A revised 3 -> 5
   toward agreement and that is where groupthink hides.
8. **Pre-registered for S4 (rule 21):** an agent scoping Calendar to Lisa sees only 2 review meetings,
   one per owner, and concludes settled. Intended difficulty, but it raises all-fail risk on any
   criterion requiring the Rescheduled duplicate to be found.

## Known pipeline defect (surfaced, not patched)

`Validators/validate.py:472` falls back to a hardcoded Brookfield `2026-06-12` when
`Fact_Ledger.lifecycle.today` is null, which it is for every StarPM task. The fallback is
universe-blind: the same function branches on `universe == "starpm"` two lines earlier for internal
IDs. Consequence if trusted, this prompt's "It is now July" reads as a future reference on a BINARY
sub-dim. Not patched because `validate.py` is covered by frozen report hashes in
`Validators/regression_baseline/`. AUDIT ruled the disposition sufficient because the sub-dim is
established by direct query of `today_horizon.json` against the OPS-10 deadline rather than by
judgement. Carry as a pipeline TODO.
