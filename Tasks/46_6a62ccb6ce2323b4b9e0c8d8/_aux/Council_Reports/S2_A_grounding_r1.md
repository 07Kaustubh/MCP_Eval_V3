# Council A - Grounding and Convention - S2 (Oracle Events)

Task: `Tasks/46_6a62ccb6ce2323b4b9e0c8d8` | Universe: starpm (V4) | Universe today: 2026-07-01 America/Chicago
Deliverable: `6_Oracle_Events.txt` (36 OEs, 71 lines, 21,467 bytes)
Mode: read-only. No file other than this report was written.

## VERDICT: BLOCK

7 BLOCK findings, 6 MODERATE, 3 MINOR. A2 (convention) and A-TOOLS pass clean.

The quantitative spine of this OE file is excellent. Every QuickBooks figure, every Airtable
record id, every calendar row count, every Slack verbatim and every Linear comment id resolves
exactly. The blocks are concentrated in four places: three universe-wide uniqueness claims that
are false, one write target that is not uniquely addressable, one open-ticket claim contradicted
by the ticket table, and one missing discovery step.

---

## A1 - Grounding sweep

### Verified EXACT (no action)

Linear
```
OPS-10                                   -> linear.linear_issues.json:number=10
  title "Mid-Year Owner Portfolio Reviews - June 2026"  -> EXACT
  team_001 / proj_002 / state_OPS_0 / assignee Brooke Phillips -> EXACT
  created_at == updated_at == 2026-05-03T22:11:57.112604-05:00 -> EXACT
  description: four owners + four coordinators + "before end of June" -> EXACT
only issue carrying "Mid-Year" in title  -> CONFIRMED (1 of 230)
comment_248a843fe7db59e8afaf8d5b6c71c387 -> linear.linear_comments.json (Brooke, 2026-05-07) EXACT
  "occupancy rates, outstanding maintenance backlog, and make-ready status" -> EXACT
comment_79dc83838bd65d678c48b5911f942412 -> (2026-05-17) EXACT
  "locked in for the first week of June, 60 minutes in the afternoon" -> EXACT VERBATIM
comment_179d6b0702be5ca1b0a1e967e1e136e0 -> (2026-06-10) EXACT
  "all four owner meetings are confirmed on the calendar" -> EXACT VERBATIM
state_OPS_0..4 Backlog/Todo/In Progress/In Review/Done -> EXACT, 5 states, team_001 only team
OPS-100 "May Monthly Owner Report - Finley Properties" state_OPS_2 proj_002 -> EXACT
  4 comments -> EXACT count
comment_5a6d779a715f587392dd00b9c8dbbd4a  -> contains "94% figure" -> EXACT
comment_42a514c0161254a7992a137d50d3be45  -> "moving this to Done" -> EXACT VERBATIM
team_001 next_issue_number = 1000 -> EXACT (OE 35 claim holds)
```

Slack
```
C001..C008 names -> EXACT all eight; every purpose and topic empty -> CONFIRMED
C006 "#owner-relations" -> EXACT
C006 message count 43 -> EXACT
580 total messages / 346 thread replies -> EXACT BOTH
831d2b6760205432a20487e2664a607e ts "1780002480.000000" -> EXACT
  "occupancy numbers, rent collection status, maintenance ticket activity, and
   make-ready turn progress" -> EXACT VERBATIM
a6779a055eaf5fb1893d0ed6d92e3b39 thread_parent_id 831d2b67... 2026-05-28 -> EXACT
  full Lisa quote (94% / early June / 97% / water heater / on track) -> EXACT VERBATIM
297f14105d465ce1b7e66a59f1ad3ecb C004 Brooke 2026-05-07 -> EXACT
49b2873d46d55e4291a78d91d91a5054 "occupancy is solid, two make-readies on track,
   no escalations to flag" -> EXACT VERBATIM (2026-05-12 14:39:04 CDT)
5f60afa12c4c53b6b7694d59373acae8 "occupancy is strong, two make-readies wrapping on
   schedule, nothing escalated on maintenance" -> EXACT VERBATIM (2026-05-12 14:58:04 CDT)
nineteen minutes apart -> EXACT (14:39:04 -> 14:58:04)
```

Airtable
```
appPropertyOps "Property Operations"     -> EXACT, only base
tblMakeReady 120 / tblMaintenanceTickets 50 -> EXACT BOTH
fldUnit fldTurnStatus fldMoveOut fldTargetReady fldNotes2 -> EXACT
selSched Scheduled / selProg In Progress / selReady Ready -> EXACT, exactly 3 choices
Sunset Ridge: 7 rows / 3 unit strings / zero selReady -> EXACT (selProg 3, selSched 4)
  rec987aae7d522057 recf50eb955a10651 rec2471fac3f9ae51 reca06d89f1a4ac5b -> 309C  EXACT
  rec98bdfeec73545e rec7d202aed68c95c -> 104B  EXACT
  reca8230a8fd9ff51 -> Sunset Ridge Unit 14  EXACT
Mesa Vista: 8 rows / 4 unit strings -> EXACT
  rec23600780ef4053 rec35a6c4f2e50657 -> 107A both selProg  EXACT
  reca4aa17f0755b55 rec4081fd2ccde95a rec591a0f70432651 -> 207A  EXACT
  rec88734a4fdfde57 -> 310C selSched  EXACT (MoveOut 2026-05-22, Target 2026-05-22 EXACT)
  recbd087a4abd605b recc8534b3fd13954 -> 4C  EXACT
rec88734a4fdfde57 fldNotes2 (subfloor) -> EXACT VERBATIM, full note
rec98bdfeec73545e fldNotes2 (vacated early / walk-through July 14) -> EXACT VERBATIM
rec7d202aed68c95c fldNotes2 (repaint started July 15) -> EXACT VERBATIM
rec987aae7d522057 fldNotes2 (Alicia to confirm) -> EXACT VERBATIM
recf50eb955a10651 fldNotes2 (Alicia confirmed) -> EXACT VERBATIM
rec2471fac3f9ae51 "July 21 and July 22 vendor schedule locked in" -> EXACT VERBATIM
recb4aeaed326f156 MT-2026-047 selHigh fldCompletionDate "" -> EXACT
  full description quoted -> EXACT VERBATIM
rec8b679d92f30753 "Ridgeview - Roof Section (Common/Structural)" selSched -> EXACT
  "$8,400 estimate" + "Pete Donovan" + "Robert Finley" -> EXACT VERBATIM
"Unit 14" collides across properties -> CONFIRMED: 'Unit 14' x2, 'Rio Bend - Unit 14',
  'Sunset Ridge Unit 14', 'Unit 14 - Tanya Mitchell Eviction'
recb5119334a90255 / recf040e18d826352 Pinecrest 12, both completed 2026-05-11 -> EXACT
rec18899b6ec2a65f / rec8c69237d76b259 Tommy Reyes, both open -> EXACT
no water heater record ties to Mesa Vista, Harris or Finley -> CONFIRMED
```

QuickBooks (all arithmetic re-derived from source rows)
```
proj-e59d4a436ed7 Robert Finley robert.finley@gmail.com -> EXACT, exactly 1 customer row
proj-e6adffd68bf9 Harry Harris harry.harris@gmail.com  -> EXACT, exactly 1 customer row
customer fields Active/CompanyName/DisplayName/PrimaryEmailAddr -> EXACT
109367557444 2026-494  $8,400.00 Txn 2026-05-01 Due 2026-05-31 Bal 8400 -> EXACT
129552155569 2026-303  $2,190.00 Due 2026-06-05 Bal 2190 -> EXACT
793996025934 4421      $390.00   Due 2026-06-12 Bal 390  -> EXACT
110099741914 5848      $640.00   Bal 0, payment 972286822645 linked -> EXACT (settled)
  Finley open receivable 8400+2190+390 = $10,980.00 -> ARITHMETIC EXACT
  all three past due vs 2026-07-01 -> CONFIRMED
317923399822 B2026-086 $510.00 Bal 0, payment 995379039053 $510 -> EXACT
113714702211 4422      $60.00  Bal 0, payment 919443518242 $60  -> EXACT
879979204592 2026-057  $1,345.00 Bal 0, payment 903909330408 $1345 -> EXACT
  Harris open receivable $0.00 -> EXACT
920762830750 2026-B-317        $2,755.00 -> EXACT
203129812397 INV-2026-0718     $490.00   -> EXACT
152560067925 BILL-2026-0335    $410.00   -> EXACT
  Finley credit memos 2755+490+410 = $3,655.00 -> ARITHMETIC EXACT
390637322875 2026-CM-089       $195.00   -> EXACT
120329707702 INV-2026-0841-572 $1,250.00 -> EXACT
262820673328 BILL-2026-0336    $530.00   -> EXACT
  Harris credit memos 195+1250+530 = $1,975.00 -> ARITHMETIC EXACT
all six: RemainingCredit 0, Balance == TotalAmt, LinkedTxn absent -> EXACT all six
four of six carry BILL-/INV- prefix -> EXACT (2 Finley, 2 Harris)
net 10980-3655 = $7,325.00 -> ARITHMETIC EXACT
2026-494 is 31 days past due (Due 2026-05-31 -> 2026-07-01) -> EXACT
$8,400 invoice matches $8,400 estimate in rec8b679d92f30753 -> EXACT
```

Calendar / Contacts / Gmail
```
20 calendars -> EXACT
Lisa 16 event rows, latest 2026-06-02, none on/after 2026-07-01 -> EXACT
1pon50ds1aevem63td6f7emdn3 5 rows, 2026-06-02 12:15-12:45, confirmed -> EXACT
  all four attendees accepted -> EXACT; Lisa row ...-b0504ab4 -> EXACT
qqbwq3s2h7wh5udoek2940mffk 4 rows, 2026-06-03 15:00-16:30, confirmed -> EXACT
  Aurora declined, Patricia declined, Teresa accepted -> EXACT
  Lisa holds no row and is not an attendee -> CONFIRMED
8mwlxrq5w5oodwdpmvo83e00f2 4 rows, 2026-05-19 11:45-13:15 -> EXACT
  Lisa declined, Aurora declined, Robert Finley not an attendee -> EXACT
  Lisa row ...-b0504ab4 -> EXACT
90 minutes not 60, late morning not afternoon, May not June -> ALL EXACT
sweep 2026-06-01..2026-06-09 returns no Finley event -> CONFIRMED (18 bases, none Finley)
c46d47256fd95ca6aca770c8dddda5eb brooke.phillips@starpm.com
  job "Apartment Property Supervisor" -> EXACT; exactly one Brooke Phillips -> CONFIRMED
Gmail payload.body.data base64url encoded -> CONFIRMED (decoded both Tanya messages)
Tanya Mitchell past-due correspondence at Sunset Ridge Unit 14 -> CONFIRMED
comp_mesaverde "Mesa Verde Investments", Finley filed under it -> EXACT
```

### BLOCK findings

**BLOCK-1 [OE 7] C006 message split is wrong in both directions.**
Claim: "43 messages, of which 36 belong to an unrelated mass email campaign thread and 7 form a
2026-05-28 owner cluster."
Actual: 37 campaign / 6 owner cluster. The owner cluster is
`56e1b950bbfa5ac9b241d7e13587e299`, `831d2b6760205432a20487e2664a607e`,
`a6779a055eaf5fb1893d0ed6d92e3b39`, `679eac61fae45c2b9c545f4268396c41`,
`654d7dd532e45ddba60015c69f25b122`, `2687eb8d7cae501ea99b8c8305f12217` = 6 rows, all
2026-05-28 CDT. Remainder = 37. Secondary error: the campaign traffic is 7 distinct root
threads, not "an unrelated mass email campaign thread".
Fix: "of which 37 belong to unrelated mass email campaign threads and 6 form a 2026-05-28
owner cluster".

**BLOCK-2 [OE 11] "The 94 percent figure appears in exactly one Slack message and one Linear
comment and nowhere else in the universe" is false.**
`94%` also occurs in:
- `hubspot.hubspot_objects.json` `deal_9664cf85817555d0b1e0dfddfc054c96` -> "Occupancy across the
  Oakfield Commons units held at 94% through the week". This is an OCCUPANCY figure, the same
  metric type, and is the most damaging of the three.
- `hubspot.hubspot_objects.json` `deal_7a67fc76208652468be023d7dad1c224` -> deliverability 94%.
- `linear.linear_issues.json` OPS-119 -> Mailchimp send quota 94%.
The intended point (no independent corroboration for Finley's Mesa Vista occupancy) survives;
the universe-wide uniqueness assertion does not.
Fix: "appears nowhere else in the universe in connection with Finley or Mesa Vista".

**BLOCK-3 [OE 10] "the only place in the universe that link is stated" is false and contradicts
OE 7 and OE 8 of this same file.**
The Finley-to-Mesa-Vista link is also stated in:
- Slack `831d2b6760205432a20487e2664a607e` -> "Robert Finley's May report for Mesa Vista"
  (quoted by OE 7)
- Slack `a6779a055eaf5fb1893d0ed6d92e3b39` -> "Robert's Mesa Vista portfolio" (quoted by OE 8)
- Slack `2687eb8d7cae501ea99b8c8305f12217` -> "Mesa Vista ... That was Robert's main question"
- OPS-100 comments `comment_5a6d779a715f587392dd00b9c8dbbd4a`,
  `comment_b575411ba2be5ceaa0ab28094905f844`, `comment_42a514c0161254a7992a137d50d3be45`
The OE file cites two of these itself, so the claim is internally inconsistent, and it
materially overstates how hard the Finley bridge is.
Fix: "which Airtable itself never records" or "the only Linear issue description stating it".

**BLOCK-4 [OE 1] OPS-23's title is misquoted.**
Claim: "OPS-11, OPS-13 and OPS-23 (all titled 'Owner review packages: data compilation and
presentation prep')".
Actual: OPS-11 and OPS-13 carry that title byte-identically. OPS-23 is
`Owner Review Packages - Data Compilation and Presentation Prep` (title case, hyphen not colon).
The S1 handoff's own table at obligation 3 records the correct OPS-23 title, so this is a
regression against a binding input.
Fix: attribute the quoted string to OPS-11 and OPS-13 only; describe OPS-23 as a title-case
variant.

**BLOCK-5 [OE 18] "This is the only open ticket in either owner's scope" is false.**
`tblMaintenanceTickets` holds 7 rows with an empty `fldCompletionDate`. Two are Tanya Mitchell's,
and Tanya Mitchell's unit is Sunset Ridge Unit 14, which OE 13 assigns to Harry Harris and OE 21
independently confirms:
- `rec46234590708b5c` MT-2026-0184, `fldPriority` selHigh, completion empty, "Account flagged for
  second-month delinquency - Tanya Mitchell ... Status: Past Due - Second Month"
- `recc0ecc885e9645e` DLQ-2026-0601, `fldPriority` selHigh, completion empty, "Delinquency logged
  for Tanya Mitchell - rent due June 1 remains unpaid past the five-day grace period"
Both satisfy the OE's own open-ticket test ("open status must be read from an empty
fldCompletionDate"). The prompt asks for "what maintenance is still outstanding" on both owners,
and OE 33 mandates a Harris paragraph that carries only make-ready position and a $0.00
receivable, so this omission propagates into the graded email.
Fix: either restate as "the only open ticket in either owner's scope that is a repair item rather
than a delinquency record" and add the two delinquency tickets to Harris's position in OE 33, or
state explicitly why delinquency rows are out of scope.

**BLOCK-7 [OE 13] The Harris-to-Sunset-Ridge bridge is never materialized.** (see A11)

---

## A2 - Convention sweep

**PASS. Zero drift.**

| Check | Result |
|---|---|
| em dash / en dash / minus sign | 0 / 0 / 0 |
| smart quotes, ellipsis, NBSP | 0 |
| markdown headers, bullets, blockquotes | none |
| bold / italic markers | 0 |
| inline rubric meta-tags (`[[`, `{{`, `<tag>`) | 0 |
| `OE <n>:` numbered prose | 36 of 36 lines |
| sequential 1..36, no gaps, no duplicates | true |
| stray non-OE non-blank lines | none |
| action-verb opening | 36 of 36 (Search, Call, Read, Compare, Determine, Update, Resolve, Look, Create, Post, Open) |
| discovery before write | OE 1-29 discovery, OE 30-36 write |

`Reference/OE_Convention_Inventory.json` `hard_traps` correctly disregarded as Brookfield-derived.
The five StarPM traps are all handled correctly (see A-TOOLS).

---

## A3 - Narrative State Consistency

```
"OPS-10 still reads state_OPS_0 (Backlog)"                  -> CONSISTENT
"its updated_at equals its created_at"                      -> CONSISTENT
"the issue never moved"                                     -> CONSISTENT
"OPS-100, state state_OPS_2 (In Progress)"                   -> CONSISTENT
"says 'moving this to Done' while the issue still reads state_OPS_2" -> CONSISTENT
"rec88734a4fdfde57 (Mesa Vista 310C, selSched)"             -> CONSISTENT
"rec98bdfeec73545e is recorded selSched"                    -> CONSISTENT
"rec987aae7d522057 is recorded selSched"                    -> CONSISTENT
"rec8b679d92f30753 ... selSched"                            -> CONSISTENT
"recb4aeaed326f156 ... fldCompletionDate empty, so still open" -> CONSISTENT
"two still-open maintenance records rec18899b6ec2a65f and rec8c69237d76b259" -> CONSISTENT
"three open invoices, all past due"                         -> CONSISTENT
"each carrying a Balance of $0.00"                          -> CONSISTENT
"both status confirmed and neither cancelled" (both Harris events) -> CONSISTENT
"Lisa holds no row on the rescheduled instance"             -> CONSISTENT
"Lisa Smith and Aurora Winona both declined"                -> CONSISTENT
"Robert Finley not an attendee at all"                      -> CONSISTENT
"none of them is applied ... none reduces the receivable"   -> see MOD-2
"This is the only open ticket in either owner's scope"      -> CONTRADICTING RECORDS
      airtable.airtable_records.json:rec46234590708b5c (MT-2026-0184, open, selHigh)
      airtable.airtable_records.json:recc0ecc885e9645e (DLQ-2026-0601, open, selHigh)
      = BLOCK-5
```

**MOD-2 [OE 25] The "unapplied" inference partly runs backwards.**
"Every one of these carries a RemainingCredit of 0 with Balance equal to TotalAmt and no
LinkedTxn, so none of them is applied against anything."
In QuickBooks semantics `RemainingCredit = 0` normally means the credit is fully consumed, which
argues the opposite way. The sound evidence is `Balance == TotalAmt` and absent `LinkedTxn`, both
verified on all six. Because OE 33 mandates the email assert the credits are "unapplied", an
agent that reads `RemainingCredit = 0` the conventional way and omits or reverses the claim will
be graded wrong for a defensible reading.
Fix: drop `RemainingCredit` from the justification, or state that it conflicts with `Balance` and
`LinkedTxn` and that the latter two govern.

---

## A4 - Action vs Universe Prescription

Checked `fldNotes2` prose, all 48 Linear comment bodies and all 580 Slack messages for a
documented decision to defer, leave as-is, or act differently on each written object.

| OE | Object | Competing prescription in universe? |
|---|---|---|
| 30 | `rec98bdfeec73545e` | none found |
| 30 | `rec987aae7d522057` | none found |
| 31 | `qqbwq3s2h7wh5udoek2940mffk` | none found |
| 31 | `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4` | none found |
| 33 | Gmail draft to Brooke | none found |
| 34 | `save_comment` on OPS-10 | none found |
| 35 | new issue on team_001 | none found |
| 36 | `slack_send_message` C006 | none: Brooke's own 2026-05-28 top-level posts `679eac61fae45c2b9c545f4268396c41`, `654d7dd532e45ddba60015c69f25b122`, `2687eb8d7cae501ea99b8c8305f12217` establish the precedent, as OE 36 claims. CONFIRMED |

No ACTION_DIVERGENCE.

**AUTHORITY.** Lisa Smith is a `@starpm.com` persona, is named in the OPS-10 description as a
coordinator, is assigned Harris and Finley by `comment_248a843fe7db59e8afaf8d5b6c71c387` and by
Slack `297f14105d465ce1b7e66a59f1ad3ecb`, holds Airtable edit rights on `appPropertyOps`, and is
an attendee with a row on three of the four review events. Standing confirmed for every write
in OE 30 and OE 33 to OE 36.

**MOD-3 [OE 31] The Finley `respond_to_event` path settles nothing.**
`8mwlxrq5w5oodwdpmvo83e00f2` starts 2026-05-19 11:45, six weeks before universe today
2026-07-01. Accepting a meeting that already happened does not answer the prompt's "Do the same
for their review meetings if either of those did not end up properly settled", and OE 29 itself
concludes the Finley meeting is defective in date, duration and time of day.
Fix: restrict the Finley accept-set to `update_event` moving it to a future date, or drop the
`respond_to_event` option.

**MOD-4 [OE 28 / OE 29] Third calendar carrier omitted.**
S1 handoff item 12 records three calendar carriers as binding. The OE covers two. The third is
the Harris ORIGINAL (2026-06-02, 12:15 to 12:45, 30 minutes, midday) contradicting Slack
`2b4b2265ca3b5e709becebe1dabfb8f1` and `7e8901f9449e5124b3d5f8c860d8596e`, both of which state
"Harry Harris is set for a casual 45-minute morning call late June".
Fix: add the contradiction to OE 28.

---

## A11 - End-to-End Solvability

**Link 1a: prompt owner name "Robert Finley" -> Mesa Vista cluster. REACHABLE, well specified.**
Bridges: OPS-100 description (named by OE 10), Slack `831d2b6760205432a20487e2664a607e`,
`a6779a055eaf5fb1893d0ed6d92e3b39`, `2687eb8d7cae501ea99b8c8305f12217`.

**Link 1b: "Robert Finley" -> Ridgeview. REACHABLE.**
`rec8b679d92f30753` `fldNotes2` names Robert Finley directly. Corroborated by QuickBooks invoice
`109367557444` (2026-494, roof section repair, Ridgeview) at the matching $8,400.

**Link 1c: prompt owner name "Harry Harris" -> Sunset Ridge cluster. BLOCK-7.**

```
SOLVABILITY_BREAK (soft): OE 13 asserts "Harry Harris's cluster" with no discovery step anywhere
in the file. Airtable carries no owner field. The bridge exists but the OE never names it.
```
The only records that bridge Harris to Sunset Ridge:
- `quickbooks.quickbooks_entities.json:113714702211` (DocNumber 4422, `CustomerRef` Harry Harris),
  `CustomerMemo` "Confirmation of lease renewal processing - Unit 14, Sunset Ridge Apartments,
  October 2026", `PrivateNote` "renewal fee for Sunset Ridge Unit 14". This is the single
  cleanest bridge and the OE cites this invoice in OE 24 for its amount only, never for its memo.
- Indirect chain: `linear.linear_issues.json:OPS-32` "Eviction Hearing - Mitchell, Harris
  Property" plus `gcalendar` `nuh928ma4rwhwf1bnap30rmfli-*` "JP court hearing for the Mitchell
  eviction at the Harris property", combined with Tanya Mitchell at Sunset Ridge Unit 14
  (`reca8230a8fd9ff51`, Slack `a718e828a5e85e16b037d8a3bd058d0c`, Gmail `38bd9dac5d3dae8b`).

Both bridges are contested by decoys that the OE also never mentions:
- `quickbooks.quickbooks_entities.json:110274597983` (DocNumber 4418, $325) bills **Simone
  Okafor** for "Lease renewal processing fee - Unit 14, Sunset Ridge Apartments", a near-duplicate
  of the Harris invoice 4422.
- `airtable.airtable_records.json:rec769c9f03f0b85f` places **Tanya Mitchell at "Las Palmas 4B"**,
  so "the Harris property" in OPS-32 is not uniquely Sunset Ridge by that route.

This is not a hard break, so it is a BLOCK on OE completeness rather than on feasibility. The
asymmetry is the problem: OE 10 spends a full sentence materializing the easier Finley bridge
while the harder Harris bridge, which is load-bearing for OE 13, both mandated writes in OE 30
and the Harris half of OE 33 and OE 36, is asserted without evidence.
Fix: insert a discovery OE before OE 13 that names QuickBooks invoice 4422's `CustomerMemo` and
`PrivateNote` as the owner-to-property bridge, and note the 4418 / Simone Okafor decoy.

**Link 2: `slack_read_thread` with `message_ts` from OE 8 resolves to Lisa's reply. VERIFIED.**
Parent `831d2b6760205432a20487e2664a607e` has `ts` exactly `1780002480.000000`, matching the OE
string byte for byte. Exactly one reply has `thread_parent_id` equal to that parent id:
`a6779a055eaf5fb1893d0ed6d92e3b39`. That reply also carries `thread_ts_legacy`
`1780002480.000000`, so both resolution strategies land on it. `slack_read_thread` requires
`channel_id` and `message_ts`, both supplied. RESOLVES.

**Link 3: the tools named can address the calendar targets in OE 31. PARTIAL. See BLOCK-6.**
`update_event`, `delete_event` and `respond_to_event` all exist and take `eventId` with
`calendarId` optional, so Lisa is not gated by calendar ownership. The Finley target
`8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4` is a real row id and addressable. The Harris rescheduled
target is not uniquely addressable.

---

## A-TOOLS - Tool and parameter verification

**PASS. 33 of 33 tools exist verbatim. Zero phantom tools. Zero phantom parameters. All five
StarPM parameter traps navigated correctly.**

| Tool | Exists | Server | Binding used by OE | Verdict |
|---|---|---|---|---|
| `list_issues` | yes | linear | `query` (optional) | OK |
| `get_issue` | yes | linear | `id` (optional) | OK |
| `list_comments` | yes | linear | `issueId` | OK |
| `save_comment` | yes | linear | `issueId` + `body` | OK, trap navigated |
| `save_issue` | yes | linear | `team` `project` `title` `description` `state` | OK, `team` not `teamId` |
| `list_issue_statuses` | yes | linear | `team` | OK, `team` is REQUIRED and supplied |
| `slack_search_channels` | yes | slack | `query` (required) | OK |
| `slack_read_channel` | yes | slack | `channel_id` (required) | OK |
| `slack_read_thread` | yes | slack | `channel_id` + `message_ts` (both required) | OK |
| `slack_search_public` | yes | slack | `query` (required) | OK |
| `slack_send_message` | yes | slack | `channel_id` + `message` | OK, trap navigated (not `payload`/`text`) |
| `list_bases` | yes | airtable | none | OK |
| `list_tables_for_base` | yes | airtable | `baseId` (required) | OK |
| `get_table_schema` | yes | airtable | none named | see MIN-2 |
| `search_records` | yes | airtable | `baseId` + `table` + `query` | OK, uses `table` NOT `tableId` |
| `update_records_for_table` | yes | airtable | `baseId` + `tableId` + `records` | OK, uses `tableId` correctly |
| `list_records_for_table` | yes | airtable | not invoked | n/a |
| `search_threads` | yes | gmail | `query` (optional) | OK |
| `get_thread` | yes | gmail | none named (`threadId` required) | OK, no wrong param |
| `create_draft` | yes | gmail | `to` + `subject` + `body` | OK, trap navigated (`body` not `content`) |
| `search_customers` | yes | quickbooks | `query` | OK |
| `search_invoices` | yes | quickbooks | `query` | OK |
| `read_invoice` | yes | quickbooks | none named (`invoice_id` required) | OK |
| `search_credit_memos` | yes | quickbooks | `query` | OK |
| `get_credit_memo` | yes | quickbooks | none named (`id` required) | OK |
| `get_aged_receivables` | yes | quickbooks | `customer` | OK, real optional param |
| `list_calendars` | yes | gcalendar | none | OK |
| `list_events` | yes | gcalendar | `calendarId`, `fullText` | OK, both real optionals |
| `get_event` | yes | gcalendar | `eventId` required | see BLOCK-6 for the value passed |
| `update_event` | yes | gcalendar | `eventId` required | see BLOCK-6 |
| `delete_event` | yes | gcalendar | `eventId` required | see BLOCK-6 |
| `respond_to_event` | yes | gcalendar | `eventId` + `responseStatus` | OK, both required and supplied |
| `contacts_search_contacts` | yes | contacts | `query` (required) | OK |

No Brookfield-shaped token appears anywhere. The only remaining underscore tokens in the file are
`comp_mesaverde` and `comp_riogrande`, which are HubSpot company ids, not tool names.

**MIN-1 [OE 20] `search_records` under-specified.** OE 20 names only `baseId "appPropertyOps"`.
The tool requires `baseId`, `table` and `query`. No wrong parameter is named, so this is a
completeness nit, not a phantom.
**MIN-2 [OE 12] `get_table_schema` required `tables` param not named.** Completeness only.

---

## A-F7 - Single-target uniqueness (hard rule 13)

| Pinned target | Matching universe rows | Verdict |
|---|---|---|
| `rec98bdfeec73545e` | 1 | UNIQUE |
| `rec987aae7d522057` | 1 | UNIQUE |
| `rec88734a4fdfde57` | 1 (Mesa Vista 310C is a single-row unit string) | UNIQUE |
| `recb4aeaed326f156` | 1 | UNIQUE |
| `rec8b679d92f30753` | 1 (only Ridgeview row) | UNIQUE |
| OPS-10 | 1 of 230, only "Mid-Year" title | UNIQUE |
| `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4` | 1 | UNIQUE |
| `c46d47256fd95ca6aca770c8dddda5eb` | 1 Brooke Phillips in contacts | UNIQUE |
| C006 | 1 | UNIQUE |
| **rescheduled Harris event (OE 31 write)** | **4** | **F7 AMBIGUOUS_TARGET** |

**BLOCK-6 [OE 31] F7 AMBIGUOUS_TARGET on the mandated calendar write.**
"the accepted paths are `delete_event` with `eventId` set to the rescheduled instance, or
`update_event` with `eventId` set to the rescheduled instance".

The rescheduled instance is base id `qqbwq3s2h7wh5udoek2940mffk`, which resolves to FOUR rows:
```
qqbwq3s2h7wh5udoek2940mffk-0cc810d3   patricia.nguyen@starpm.com
qqbwq3s2h7wh5udoek2940mffk-a2adb7dc   aurora.winona@starpm.com
qqbwq3s2h7wh5udoek2940mffk-b6a1e41c   teresa.wood@starpm.com
qqbwq3s2h7wh5udoek2940mffk-0f82233a   brooke.phillips@starpm.com
```
Measured: **0 of 565** calendar event ids exist without a per-invitee suffix, so the bare base id
is not a valid `eventId` and cannot be passed to `delete_event` or `update_event`. The OE
therefore pins a write target that (a) is not a real id and (b) fans out to four candidates.

Compounding it, the OE's own success condition is "the two confirmed instances stop standing as
two separate live meetings". A single-row delete or update leaves three rows live, so satisfying
the OE's literal instruction does not satisfy the OE's stated success condition.

This directly violates S1 handoff BLOCKING obligation 1 ("Never pin a bare calendar base id"),
which tabulated this exact event at 4 rows.

Fix: state the accept-set explicitly, for example "any one of the four rows
`qqbwq3s2h7wh5udoek2940mffk-0cc810d3`, `-a2adb7dc`, `-b6a1e41c`, `-0f82233a`", and restate the
success condition as "the rescheduled instance is cancelled or retitled on the calendar the agent
addresses". If the intent is that all four must go, say so and price the cost.

Related, non-blocking: OE 29 says "Call `get_event` on the Finley review ... base id
`8mwlxrq5w5oodwdpmvo83e00f2`". `get_event` requires a real `eventId`, and the bare base id is not
one. OE 29 does supply `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4` in the same sentence, so an agent
recovers. Recommend naming the row id as the argument to avoid teaching the wrong pattern. The
same applies to OE 28's `1pon50ds1aevem63td6f7emdn3` and `qqbwq3s2h7wh5udoek2940mffk`, which are
correctly labelled "base id" and used descriptively, so those are acceptable as written.

**MOD-5 [OE 30] Two of at least five rows matching the prompt's described class are pinned.**
The prompt describes a class: "Where the unit and turn records do not line up with what you
actually find on the ground". Applying the OE's own test from OE 16 and OE 17 (recorded status
contradicted by a sibling row on the same unit), three further rows match:
```
reca4aa17f0755b55  Mesa Vista 207A  selProg  "Flooring inspection pending sign-off"
rec4081fd2ccde95a  Mesa Vista 207A  selProg  "Technician confirmed for July 14 install"
   sibling rec591a0f70432651 selReady "All work completed July 17 ... cleared for leasing"
recbd087a4abd605b  Mesa Vista 4C    selProg  "Will update status to Ready once ... signed off"
   sibling recc8534b3fd13954 selReady "Unit confirmed ready for leasing"
```
S1 handoff obligation 10 already excluded 207A and 4C as carriers, so OE 30's selection is
handoff-compliant and gradeable: an agent that fixes the two pinned rows passes whether or not it
also fixes the others. The residual risk is that S3 reads OE 30's decompose directive as an
exhaustive enumeration and penalizes thoroughness.
Fix: add one sentence to OE 30 stating that corrections to other mismatching rows are acceptable
and not graded.

**MOD-6 [OE 33] "7 make-ready rows across 3 Sunset Ridge units" is a string-query artifact.**
Six further `tblMakeReady` rows describe the same Tanya Mitchell Unit 14 turn under `fldUnit`
strings that do not contain "Sunset Ridge": `rec3782834f35df50` ("Tanya Mitchell - Eviction
Track"), `rec8005502043b755` ("Tanya Mitchell - Delinquency Escalation"), `rec91517a5acab558`
("Unit 14"), `recc83c05d889b354` ("Unit 14"), `receee45491536859` ("Unit 14 - Tanya Mitchell
Eviction"), `rec769c9f03f0b85f` ("Las Palmas 4B"). The figure 7 is defensible only as "rows whose
Unit field contains 'Sunset Ridge'". Because OE 33 mandates it as a graded content element, an
agent that sweeps more thoroughly and reports a different count is penalized for being right.
Fix: phrase the graded element as "no Sunset Ridge row is in a Ready state" rather than pinning
the integer 7, or qualify the count in the OE.

**MIN-3 [OE 13] "a Tanya Mitchell delinquency and eviction row".** `reca8230a8fd9ff51`'s own
`fldNotes2` records a delinquency and a tentative turn; the word eviction appears only in sibling
records (`rec3782834f35df50`, `receee45491536859`, `recc83c05d889b354`) and in OPS-32. Accurate in
substance, but not from the row cited.

---

## Additional grounding drift

**MOD-1 [OE 10] "the Mesa Vista deals sit under comp_riogrande".**
Of three HubSpot deals naming Mesa Vista, only `deal_mesavista4a` sits under `comp_riogrande`.
`deal_8cd04fe1a35d515296c66cdd0cf3f842` sits under `comp_proj_fef06d5fa2b2` and
`deal_f170c3055ebe53229289277be13c0033` under `comp_proj_8a64d674466b`. The definite plural
overstates it.
Fix: "while the Mesa Vista 4A lease-renewal deal sits under comp_riogrande".

---

## Summary table

| ID | Perspective | OE | Severity | One-line |
|---|---|---|---|---|
| BLOCK-1 | A1 | 7 | BLOCK | C006 split is 37/6, not 36/7; 7 root threads not one |
| BLOCK-2 | A1 | 11 | BLOCK | "94 percent nowhere else" false: 3 more hits incl. an occupancy figure |
| BLOCK-3 | A1/A3 | 10 | BLOCK | "only place the link is stated" false and self-contradicting |
| BLOCK-4 | A1 | 1 | BLOCK | OPS-23 title misquoted against the S1 handoff's own table |
| BLOCK-5 | A1/A3 | 18 | BLOCK | two open Harris-scope delinquency tickets contradict "only open ticket" |
| BLOCK-6 | A-F7 | 31 | BLOCK | rescheduled Harris event fans to 4 rows; bare base id is not a valid eventId |
| BLOCK-7 | A11 | 13 | BLOCK | Harris-to-Sunset-Ridge bridge never materialized |
| MOD-1 | A1 | 10 | MODERATE | only 1 of 3 Mesa Vista deals is under comp_riogrande |
| MOD-2 | A3 | 25 | MODERATE | RemainingCredit=0 argues against the "unapplied" conclusion |
| MOD-3 | A4 | 31 | MODERATE | accepting a 2026-05-19 meeting settles nothing |
| MOD-4 | A4 | 28/29 | MODERATE | third calendar carrier from handoff item 12 omitted |
| MOD-5 | A-F7 | 30 | MODERATE | 2 of >=5 class members pinned; say extra fixes are ungraded |
| MOD-6 | A1 | 33 | MODERATE | the integer 7 is a string-query artifact |
| MIN-1 | A-TOOLS | 20 | MINOR | search_records missing required table and query |
| MIN-2 | A-TOOLS | 12 | MINOR | get_table_schema required `tables` not named |
| MIN-3 | A1 | 13 | MINOR | "eviction" is from sibling rows, not the cited row |

## Clean perspectives

- **A2 convention**: PASS, zero drift on every checked dimension.
- **A-TOOLS**: PASS, 33 of 33 tools verbatim, every parameter binding correct, all five StarPM
  traps navigated (`message`, `body`, `team`, `issueId`+`body`, camelCase `baseId`/`tableId`), and
  the `search_records` `table` versus `update_records_for_table` `tableId` distinction handled
  correctly.
- **A4 action divergence**: PASS, no competing prescription found; Lisa's authority confirmed for
  every write.
- **All QuickBooks arithmetic**: EXACT. $10,980.00, $3,655.00, $1,975.00, $0.00, $7,325.00 and the
  31-day figure all re-derived from source rows.

## Verdict

**BLOCK.** Seven blocking findings. The file's factual spine is unusually strong and the
convention and tool layers are clean, so all seven are correctable in place without restructuring
the OE list. BLOCK-6 and BLOCK-7 are the substantive ones: one mandated write has no addressable
target, and the discovery path for half the task is missing. BLOCK-1 through BLOCK-5 are
overstated uniqueness or count claims that need scoping.
