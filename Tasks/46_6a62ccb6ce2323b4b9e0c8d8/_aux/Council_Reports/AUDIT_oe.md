# AUDIT: 6_Oracle_Events.txt (closing round, strict)

sha256: a8522f8daa4162ed6b9199a58b769b00dfb3fa55dfc3632c328451ba0f2e6785

Matches the expected hash. The bytes graded here are the frozen bytes. Task 46, StarPM (V4),
universe today 2026-07-01 America/Chicago. Read-only round: nothing outside this report was written.

Method: every claim was re-derived from `_aux/Universe_Split/` by simulating the retrieval call the
step names, not by reading forward from earlier rounds. 321 behavioural assertions, 114 identifier
existence checks, 149 quoted-string checks. Prior rounds' conclusions were not carried forward.

## Verdict summary

| Check | Result |
|---|---|
| 1. Reachability (identifier and quoted title, service-bound) | PASS, 0 unreachable |
| 2. Count claims | PASS with 1 note (OE 13, semantics-dependent) |
| 3. Atom and quote accuracy | PASS, 149/149 quotes faithful |
| 4. Tool and parameter legality | PASS, 35/35 tools, all params exact |
| 5. Prompt coverage, forward and reverse | PASS, 8/8 requirements, 0 beyond-prompt |
| 6. Write lifecycle, ordering, single-target uniqueness | PASS |
| 7. Format, validator, S3 decompose mirroring | PASS |

## r6 blockers: both closed, verified on these bytes

1. **HubSpot reachability.** Zero `comp_*` tokens remain in the file. `search_crm_objects` with
   object_type "tickets" and query "Mesa Vista" returns exactly 3 tickets, all three titled
   "Move-Out - Connor Beaumont, Mesa Vista - Vacancy June 30", and
   `ticket_87552e6b23bc5a92bd2641b9054b8c13` is among them and is the only one of the three whose
   body names Finley. Confirmed by direct count, not by trusting the step.
2. **OE 21 Unit 14.** `search_records` on tblMakeReady with query "Unit 14" returns exactly 5 rows
   and `rec94e86a3007dd5e` is among them, fldUnit "Rio Bend - Unit 14", carrying no Tanya Mitchell
   token. The seven Tanya rows plus this one make the eight the step describes.

## The other closures since r6, each re-verified independently

* **OE 35 three events.** `list_events` fullText "Mesa Vista" across brooke.phillips and teresa.wood
  returns exactly 3 distinct post-today confirmed events: Mesa Vista HOA Management Review 2026-07-08,
  Make-Ready QC Inspection Mesa Vista 4C 2026-07-15 (`0hjw400xgjb3j7ay7ynuaqbnpi`), and Q3 Make-Ready
  Planning and Budget Review 2026-07-23. Titles and dates match the step exactly. The undercount is gone.
* **OE 8.** The reply `a6779a055eaf5fb1893d0ed6d92e3b39` is a thread reply (346 of 580 messages are),
  its parent `831d...` has exactly one reply, and the channel-level read returns 12 of 43 rows. The
  step now claims only that the OE 7 read does not return it, which is exactly true.
* **OE 13 scoping.** Exactly one record in the universe names Harris and the Sunset Ridge cluster in
  the same row: invoice 113714702211, DocNumber 4422. All eight further Harris records were checked
  one by one and each names the property the step attributes to it.
* **OE 33 symmetry.** Harris credit memos total exactly $1,975.00 and Finley's exactly $3,655.00, all
  six with Balance equal to TotalAmt, no LinkedTxn, and RemainingCredit 0. The decompose list carries
  10 elements and all 10 appear in the step body.
* **OE 30 invoice number.** Thread `66132537181ecbe1` names "2026-537" in its body and never names
  "2026-534"; no record anywhere carries DocNumber 2026-537; the record described is 445653930748,
  DocNumber 2026-534, CustomerRef Linda Castillo. The trap is stated correctly.
* **OE 10 HubSpot prose** now reads as background, and the only HubSpot call the chain needs is the
  ticket search, which resolves.

## Independent state, measured on these bytes

Reachability: 0 unreachable by identifier, 0 by quoted title, all service-bound. Every one of the 32
Airtable record ids exists and every cited fldTurnStatus matches the stored value. `validate.py
--phase oe` exits 0 with 36 sequential steps, 0 fails, 0 warns, 3 benign notes.
`verify_universe_atoms.py` reports 57 atoms, 0 fails, 4 warns; all four warns are the dates
2026-07-08, 2026-07-13, 2026-07-15 and 2026-07-23, and each is a real confirmed calendar event
verified individually, so all four are deliberate. Zero em-dashes, zero en-dashes, zero smart quotes,
zero non-ASCII characters.

On count claims I verified more than the 19 previously reported and found one that the prior tally
did not cover. It is described below as note 1. Every other count claim is exact, including the
harder ones: 43 rows in C006 split 12 and 31, 346 of 580, 120 and 50 Airtable records, 7 Sunset Ridge
rows across 3 unit strings with zero selReady, 8 Mesa Vista rows across 4 unit strings, exactly 2
Tanya maintenance rows, 7 open maintenance rows, exactly 7 Tanya make-ready rows, exactly 2 Sunset
Ridge invoices, exactly 1 Mesa Vista invoice, 117 credit memos sharing one shape, 20 calendars, 565
calendar rows, 16 Lisa rows, and the 19 minute gap between Lisa's two C004 messages, which is 19.00.

## Notes for S3, none blocking

1. **OE 13, "which returns three events".** `list_events` fullText "Harris" across the three named
   calendars returns 3 distinct events if fullText matches title, description and location, which is
   what the step needs and is a standard reading. It returns 4 if fullText also matches attendee
   emails, as the Google `q` parameter does: the fourth is `vwdtvhm1y7ukp2v2vm5ytr9dpi`, "Mitchell
   Eviction Case-Prep Review" on 2026-05-21, which matches only because `harry.harris@gmail.com` is
   an accepted attendee. This is not a blocker for three reasons: the step's actual target
   `nuh928ma4rwhwf1bnap30rmfli` is returned under both readings, so reachability is unaffected; the
   fourth event corroborates rather than contradicts, since Harry Harris personally accepting an
   invitation to the Mitchell eviction case-prep review is further evidence for the very link OE 13 is
   building; and no graded outcome depends on the numeral. If S3 wants it airtight, changing "which
   returns three events" to "which returns the Harris events including" costs nothing and removes the
   dependence on tool semantics. Worth knowing regardless, because Harris's attendance on that event
   is a fifth piece of evidence the step does not currently use.
2. **Gmail id types.** The file writes "Gmail 2ae48555b3009a95" and "Gmail 66132537181ecbe1" in the
   same shape, but the first is a message id and the second is a thread id. Both are correct and both
   are reachable by the named `search_threads` then `get_thread` path, and `get_thread` takes a
   threadId, so the thread id is the right kind of id to cite for that call. The note is only that a
   reader cannot tell which is which. Naming them "Gmail message" and "Gmail thread" would remove the
   ambiguity for S3.
3. **OE 30 and Mesa Vista 107A.** OE 30 dispositions 207A, 4C, Unit 14, 310C and reca06d explicitly,
   but not 107A. Both 107A rows are already selProg, so there is no selSched row to advance and no
   selReady row to contradict, which means 107A cannot qualify under the rule the step itself states.
   The exclusion is correct but implicit. One clause would make it explicit.
4. **OE 1 secondary query.** The primary query "mid-year owner portfolio review" returns OPS-10 under
   both phrase and token matching, so the step is sound. The alternative "owner review" returns
   OPS-11, OPS-13, OPS-20 and OPS-23 and not OPS-10 under phrase matching, which is precisely the
   four decoys the step goes on to name. The "(or similar)" hedge covers it, and the coincidence is
   a point in the step's favour rather than against it.

## What I checked hardest and what held

Single-target uniqueness (rule 13) holds on every write. OE 30 grades exactly three rows, each
uniquely identified, each moving selSched to selProg, and I confirmed no record on any service stands
against that direction: 207A and 309C appear on no service outside Airtable at all, and the only
104B records outside Airtable sit on Fernwood Gardens rather than Sunset Ridge. Every ambiguous row
in both clusters carries an explicit accept-set instead of a pinned id. OE 31 targets the one
duplicated Harris review and the one Finley review, and the two per-calendar rows it names for the
rescheduled instance both exist on the calendars stated. OE 33's recipient is unique in contacts,
Slack and HubSpot. OE 35 is graded on title and description because team_001 next_issue_number is
1000, which is correct.

The rule 13 sweep requirement for an "only unresolved item" claim is satisfied. OE 35 sweeps the
calendar, and I extended that sweep universe-wide: there are exactly 8 distinct confirmed events
after today, and not one carries Sunset Ridge, 309C, 104B, subfloor or utility. Both candidates the
step calls "carried nowhere" are genuinely carried nowhere, and the Ridgeview follow-up and
MT-2026-047, which are carried, are correctly excluded. The universe's near-miss decoys, "Las Vistas"
against Mesa Vista and "Sunridge Apartments" against Sunset Ridge, are not confused anywhere in the file.

OE 33's delinquency timeline sources exactly: the email body gives first notice June 6, plan declared
breached June 25 and cure deadline expired June 29, and OE 30's separate "June 23 installment" is the
missed second installment from the same timeline, so the two steps are consistent rather than in
conflict. OE 20's negative is properly established: no water heater record on any service resolves to
Mesa Vista or Finley, and the attribution is traced to a comment dated 2026-05-26 that predates
Lisa's 2026-05-28 message.

Known and not treated as defects, as scoped: `check_qc_binary.py`, `check_oe_rubric_sync.py` and
`check_ordering_coverage.py` fail only because `7_Rubrics.json` still holds its scaffold placeholder
text and S3 has not run.

VERDICT: PASS (STRICT)
