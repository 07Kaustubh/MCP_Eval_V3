# Council B - Adversarial QC + Density + Hardness Preservation - ROUND 2

**Phase:** S2 (Oracle Events) - **Task:** `Tasks/46_6a62ccb6ce2323b4b9e0c8d8`
**Deliverable:** `6_Oracle_Events.txt` (36 OEs, 71 lines), revised after round 1
**Universe:** `starpm`, V4 framework, dual-model, universe today 2026-07-01 America/Chicago
**Mode:** read-only. No file was edited.
**Round 1 report:** `S2_B_adversarial.md` (BLOCK, 6 MAJOR / 5 MODERATE / 6 MINOR)

**VERDICT: BLOCK** on 3 MODERATE and 2 MINOR. Completeness 5/5, Accuracy 4/5.

This is a one-pass BLOCK. Fifteen of seventeen round-1 findings are closed, four of them exhaustively verified against the rows. The residue is three wording fixes and two optional ones, with exact replacement text supplied. No structural, feasibility or density problem remains.

---

## Round-1 F9 WITHDRAWN: I was wrong, and the correction is accepted

I re-derived this against the rows before accepting it.

| Row | `ts` | `created_at` |
|---|---|---|
| Parent `831d2b6760205432a20487e2664a607e` | 1780002480.000000 | 2026-05-28T21:08:00+00:00 |
| Reply `a6779a055eaf5fb1893d0ed6d92e3b39` | **1780002481.000001** | **2026-05-28T21:08:01+00:00** |

The parent's `latest_reply` is `1782860664.000001`. Messages in the universe whose `ts` equals that value: **0**, on exact string match and on float comparison to 1e-6. `reply_count` is 1 and the single reply carries `thread_parent_id` pointing at the parent, so the thread is fully resolved without the pointer. The reply lands one second after the parent, well inside spring.

**Universe-wide:** 251 rows carry a `latest_reply`; **6 are dangling**. So this is a real and rare data defect, not a one-off.

**My error was method, not arithmetic.** I inferred a reply's date from the parent's pointer field while my own round-1 report stated in writing that I had not read the reply row. The primary record was one query away. OE 8's 2026-05-28 was correct throughout, and the file's new warning that the pointer matches no message is a genuine improvement that protects an agent from chasing it.

---

## Verification performed this round

Every claim below was re-derived from `_aux/Universe_Split/` or the tool catalog in this session.

### Verified CORRECT

| Claim | Where | Result |
|---|---|---|
| **All 21 tools' parameter names** the OE file uses | whole file | **21 of 21 exact.** `get_table_schema(baseId, tables)`, `search_records(baseId, table, query)`, `update_records_for_table(baseId, tableId, records)`, `list_events(calendarId, fullText)`, `update_event/delete_event(eventId, calendarId)`, `slack_read_thread(channel_id, message_ts)`, `slack_send_message(channel_id, message)`, `create_draft(to, subject, body)`, `save_issue(title, team, project, description)`, `save_comment(issueId, body)`, `get_aged_receivables(customer)`, and the rest. Zero mismatches. This closes my round-1 open item. |
| **`create_event` exists and is feasible** | OE 31 | Present in catalog. Required: `summary`, `startTime`, `endTime`. Optional: `calendarId`, `attendeeEmails`, `description`, `location`, `timeZone`. The new Finley path is fully supported. |
| **Per-calendar row ids** | OE 31 | `qqbwq3s2h7wh5udoek2940mffk-b6a1e41c` on `teresa.wood@starpm.com` and `qqbwq3s2h7wh5udoek2940mffk-0f82233a` on `brooke.phillips@starpm.com`, both `confirmed`. Exact. The event has 4 rows (patricia, aurora, teresa, brooke) and Lisa holds none. |
| **The 6 `selSched` rows** | OE 30 | Across the 16 rows in scope there are **exactly 6** `selSched` rows: `rec987aae7d522057`, `reca06d89f1a4ac5b`, `rec98bdfeec73545e`, `reca8230a8fd9ff51`, `rec88734a4fdfde57`, `rec8b679d92f30753`. OE 30 corrects 3 and excludes 3 by name. **3 + 3 = 6.** The set is closed. |
| **`rec8b679d92f30753` is `selSched`** | OE 19, OE 30 | Confirmed, `fldUnit` "Ridgeview - Roof Section (Common/Structural)". Finley now carries a correction. |
| **7 open maintenance rows** | OE 18 | Exactly 7 of 50 have an empty `fldCompletionDate`. Named correctly: `recb4aeaed326f156` MT-2026-047, `rec46234590708b5c` MT-2026-0184, `recc0ecc885e9645e` DLQ-2026-0601. |
| **Empty stored two ways** | OE 18 | Confirmed: 3 rows carry `''` and 4 carry `null`. A genuinely sharp trap and a new addition. |
| **OPS-39 / OPS-93 states** | OE 11 | OPS-39 `state_OPS_3` (In Review), OPS-93 `state_OPS_1` (Todo), `completed_at` null, titles exact. The issue whose title claims closure is the one in the earlier state. Correct. |
| **OPS-10, OPS-100 states** | OE 1, OE 10, OE 11 | `state_OPS_0` and `state_OPS_2`. Exact. |
| **The Oakfield 94% decoy** | OE 11 | Real. `deal_9664cf85817555d0b1e0dfddfc054c96` "Star PM - Oakfield Commons Portfolio Renewal" carries "Occupancy across the Oakfield Commons units held at 94% through the week". The numeral occurs in 5 places universe-wide, none of which independently supports Mesa Vista. |
| **346 of 580 thread replies** | OE 8 | Exactly 346. |
| **C006 carries 43 rows** | OE 7 | Exactly 43, and the remainder after the named cluster is exactly 37. |
| **The Harris bridge is the only one in the universe** | OE 13 | Swept every service for a row naming Harry Harris alongside any property token. **Exactly one row exists universe-wide:** QuickBooks invoice `113714702211`. Not Linear, not Slack, not HubSpot, not Airtable, not Gmail, not Calendar. |

### Verified and found DEFECTIVE

Three items, all detailed in the findings below: OE 7's message accounting, OE 13's decoy discriminator, and OE 30's stated reason for excluding Mesa Vista 207A and 4C. Plus the uncorrected round-1 F10 on OE 27.

---

## ROUND-1 FINDINGS: disposition

| # | Round-1 finding | Status | Verification |
|---|---|---|---|
| F1 | OE 15 superlative false | **CLOSED** | Superlative replaced with "both unresolved and untracked". MT-2026-047 and the 2026-07-13 Ridgeview walk-through both named as tracked elsewhere. Both confirmed to exist. The reframing is sound and survives the calendar sweep. |
| F2 | OE 35 naive-agent target | **CLOSED** | Untracked-vs-tracked discriminator now stated as the reason. See B-RULE13(c). |
| F3 | OE 30 correction set open | **CLOSED, exhaustively** | 6 `selSched` rows verified, 3 corrected and 3 excluded with a per-row ground reason. Fires on both owners. This is the strongest fix in the revision. |
| F4 | OE 31 bare base id | **CLOSED** | Per-calendar row ids verified exact against the rows. |
| F5 | `respond_to_event` on a past event | **CLOSED** | Path removed. `create_event` verified feasible. Both owners now required. |
| F6 | OE 28 Castillo result set | **CLOSED** | Castillo named, and explicitly placed out of scope with a reason. |
| F7 | Harris bridge missing | **PARTIALLY CLOSED** | A bridge now exists and is the only one available. But see **N2**. |
| F8 | Fourth calendar event absent | **CLOSED** | `ti5zt1xubdggbehtp79um9mim6` named by full title in OE 29 with the discriminator. |
| F9 | OE 8 reply date | **WITHDRAWN** | My error. See above. |
| F10 | OE 27 "makes both look settled" | **NOT FIXED** | Still present verbatim. Carried forward as a BLOCK finding. |
| F11 | Occupancy source-absence unearned | **MOSTLY CLOSED** | OE 11 is now much stronger on the 94% figure and adds the Oakfield decoy. The 97% collections figure remains unaddressed. Downgraded to MINOR. |
| F12 | OE 20 partial enumeration | **NOT FIXED** | Still names two destinations under a universe-wide negative. MINOR. |
| F13 | HubSpot unreachable assertion | **CLOSED** | Now reframed as "HubSpot is not a route to it", which is a stated exclusion rather than an unreachable claim. Good fix. |
| F14 | OE 34 permissive transition | **CLOSED** | Now "optional and must not be graded", with the four-owner-parent reason. |
| F15 | OE 33 decompose desync | **CLOSED** | Late-payment correction now listed. Ten elements. |
| F16 | OPS-39 / OPS-93 absent | **CLOSED** | Added in OE 11 (not OE 34 as the change summary said). States verified exact. |
| F17 | OE 18 only-open claim | **CLOSED** | Now "only open repair ticket", with the two delinquency records and the 7-row total named. Verified exact. |

**15 closed, 1 withdrawn, 1 partial, 2 uncorrected (F10, F12).**

---

## NEW FINDINGS

### N1 - MODERATE - OE 7 - the message accounting contradicts itself, and contradicts OE 8

**This defect is NEW. The round-1 fix introduced it.** Round 1 said "43 messages, of which 36 belong to an unrelated mass email campaign thread and 7 form a 2026-05-28 owner cluster" with no ids. The revision changed the split to 37/6 and named the six ids, which made the error explicit and checkable.

**Measured.** C006 holds **43 rows: 12 top-level and 31 thread replies.**

OE 7 names six ids as the owner cluster the agent "finds" via `slack_read_channel`. All six exist in C006. But one of them, **`a6779a055eaf5fb1893d0ed6d92e3b39`, is a thread reply** (`thread_parent_id` set). OE 7 then closes with "A channel-level read shows the parent but not its reply", and OE 8 says the reply "is invisible without a thread read".

So OE 7 asserts both that the channel read surfaces the reply and that it does not.

The arithmetic is right on rows and wrong on what the call returns. If `slack_read_channel` returns top-level messages, the agent sees **12**, of which 5 are the owner cluster. If it returns every row, the agent sees 43 including the reply, and **the L1/L5 thread-blindness gate collapses entirely**. The file needs to commit to one, and the rest of the file (OE 7's own last sentence, OE 8, the Hardness Plan's L5) commits to the first.

**Why MODERATE and not MINOR:** this sits on L1, the highest-yield cross-model differentiator in the plan, and S3 will read OE 7 to size the discovery criterion.

**Fix, replacement for OE 7's opening.**

> OE 7: Read C006 using slack_read_channel with channel_id "C006". The channel holds 43 rows in total but a channel-level read surfaces only the 12 top-level messages, because the other 31 are thread replies. Seven of those top-level messages belong to an unrelated mass email campaign and five form a 2026-05-28 owner cluster (56e1b950bbfa5ac9b241d7e13587e299, 831d2b6760205432a20487e2664a607e, 679eac61fae45c2b9c545f4268396c41, 654d7dd532e45ddba60015c69f25b122 and 2687eb8d7cae501ea99b8c8305f12217). Message 831d2b6760205432a20487e2664a607e (Brooke Phillips) asks Lisa for "occupancy numbers, rent collection status, maintenance ticket activity, and make-ready turn progress" for Robert Finley's Mesa Vista May report. Its one reply is the sixth member of the cluster and is not returned here, which is why OE 8 is a separate call.

### N2 - MODERATE - OE 13 - the Harris bridge names the decoy but not the discriminator that defeats it, and reaches only Unit 14

**The bridge is real and it is the only one.** Sweeping every service for a row naming Harry Harris alongside any property token returns **exactly one row in the whole universe**: QuickBooks invoice `113714702211`. Finding it was good work. But two problems remain.

**Problem 1: the two invoices are near-identical, and OE 13 cites the field they share rather than the field that separates them.**

| | Harris `113714702211` | Okafor `110274597983` |
|---|---|---|
| DocNumber | 4422 | 4418 |
| TotalAmt | $60.00 | $325.00 |
| TxnDate | **2026-05-13** | **2026-05-13** |
| DueDate | **2026-06-12** | **2026-06-12** |
| CustomerMemo | "Confirmation of lease renewal processing - Unit 14, Sunset Ridge Apartments, October 2026." | "Lease renewal processing fee - Unit 14, Sunset Ridge Apartments. Please retain for your records." |
| **ItemRef** | **Monthly Management Fee** | **Unit Turn / Make-Ready** |
| Line description | Lease document scanning and filing fee | Lease renewal coordination fee |

OE 13 rests the bridge on the CustomerMemo, which **both** invoices carry, on the same unit, on the same date. It then says "the memo must be read on the Harris invoice specifically", which tells the agent which row to look at without saying why that row is the right one. On the memo alone, Simone Okafor has an equally good claim to Sunset Ridge, which means the memo cannot establish ownership.

The discriminator exists and is strong: **`ItemRef` "Monthly Management Fee" is an owner-side charge, while "Unit Turn / Make-Ready" is not.** That is what separates an owner from a tenant here, and it is unnamed. Note that Handoff obligation 4 already flagged "Unit Turn / Make-Ready" as a near-miss magnet on credit memo `920762830750`; the same ItemRef now sits on the decoy invoice.

**Problem 2: the bridge reaches Unit 14, and the work does not live there.**

The memo names "Unit 14, Sunset Ridge Apartments". That unit is `reca8230a8fd9ff51`, which is:
- the Tanya Mitchell delinquency row,
- flagged by OE 13 itself as a string that "collides across several properties",
- and one of the three rows **OE 30 excludes** from correction.

Neither Harris correction lands there. Both land on 309C (`rec987aae7d522057`) and 104B (`rec98bdfeec73545e`). The chain from "Harris is billed a management fee on one unit at Sunset Ridge" to "309C and 104B are Harris's rows" is a property-level inference the OE asserts but never states. It is almost certainly the intended reading, and it is defensible once the management-fee point is made, but as written the OE leaves the load-bearing step silent.

**Fix, replacement for OE 13's first three sentences.**

> OE 13: Establish which property is Harry Harris's before pulling any of his rows, because Airtable has no owner field. QuickBooks invoice 113714702211 (DocNumber 4422, CustomerRef Harry Harris) carries the CustomerMemo "Confirmation of lease renewal processing - Unit 14, Sunset Ridge Apartments, October 2026" and a PrivateNote naming the Sunset Ridge Unit 14 renewal fee. This is the only row anywhere in the universe that names Harry Harris alongside a property. Invoice 110274597983 (DocNumber 4418, $325.00) is a near-duplicate on the same unit with the same TxnDate 2026-05-13 and the same DueDate 2026-06-12, billed to Simone Okafor, so the memo text alone does not settle who the owner is. What settles it is the line item: the Harris invoice carries ItemRef "Monthly Management Fee", which is the charge a manager raises against a property owner, while the Okafor invoice carries "Unit Turn / Make-Ready". Harris is therefore the Sunset Ridge owner, which puts the whole Sunset Ridge cluster in his portfolio rather than only the unit the invoice happens to name. Then search Airtable using search_records with baseId "appPropertyOps", table "tblMakeReady" and query "Sunset Ridge" to pull his cluster.

### N3 - MODERATE - OE 30 - Mesa Vista 207A and 4C are excluded on a pinning constraint, not on the ground

**Round 1 asked for this to be adjudicated at S2. It has been restated rather than adjudicated.**

OE 30 says both units "each carry a selProg row alongside a selReady row on the same unit, which looks like the same defect shape, but both units were excluded upstream as ambiguous targets and neither is a correction target here."

"Excluded upstream as ambiguous targets" is Handoff obligation 10, which is a **rubric-authorship constraint about what S3 may pin**. It is not a statement about whether the record matches the ground. The OE uses it as though it were.

**Measured, and the units do look like genuine mismatches:**

| Row | Status | `fldNotes2` |
|---|---|---|
| `reca4aa17f0755b55` | selProg | "Paint and cleaning underway. HVAC filter swap needed - parts ordered July 10. Flooring inspection pending sign-off." |
| `rec4081fd2ccde95a` | selProg | "HVAC parts arrived July 11. Technician confirmed for July 14 install. Flooring crew scheduled to follow same day." |
| `rec591a0f70432651` | **selReady** | **"All work completed July 17. Final walk-through passed. Unit cleared for leasing as of July 17."** |
| `recbd087a4abd605b` | selProg | "Internal punch list work underway. Tony has completed the kitchen faucet cartridge replacement..." |
| `recc8534b3fd13954` | **selReady** | **"QC walkthrough completed by Jaime Salinas... Touch-up routed to Tony Reyes and resolved same day."** |

On both units a sibling row states the unit is finished and cleared for leasing while other rows still read In Progress. Under the prompt's own test, "records do not line up with what you actually find on the ground", those are mismatches.

**Severity is MODERATE, not MAJOR, for three reasons.** The three `selSched` corrections are exhaustive within their own shape and are correctly derived. No criterion fails if an agent also corrects 207A or 4C. And the units genuinely cannot be pinned. The defect is that the OE gives a reason that does not survive contact with the prompt, which leaves S3 without a defensible boundary and leaves a competent agent's extra correct work unaccounted for.

**Fix, replacement for OE 30's 207A / 4C sentence.**

> Mesa Vista 207A and Mesa Vista 4C each carry selProg rows alongside a selReady row that states the unit is finished and cleared for leasing, so those rows are also out of step with the ground. They are deliberately left outside the graded correction set for a different reason: each unit string matches several rows, so no criterion can pin one of them without becoming ambiguous. An agent that corrects them as well has not made an error and must not be penalised, but the graded set is the three selSched rows named above.

---

## CARRIED-FORWARD FINDINGS

### F10 (carried) - MODERATE - OE 27 - "makes both look settled" is still false

Unchanged from round 1 and still present verbatim: "Scoping the calendar to the persona alone shows exactly one review per owner and makes both look settled."

Lisa's row on the Finley review, `8mwlxrq5w5oodwdpmvo83e00f2-b0504ab4`, reads `responseStatus: declined`, and **OE 29 says so itself two OEs later**. A declined meeting does not look settled. The file contradicts itself.

The true version is sharper and is what Handoff obligation 14 pre-registered: the persona-scoped view returns exactly two events, one per owner, which **positively confirms the prompt's "either of those"** while the Harris duplicate stays invisible.

**Fix, replacement for OE 27's final sentence.**

> Scoping the calendar to the persona alone returns exactly one review per owner, which positively confirms the prompt's "either of those" while hiding the Harris duplicate entirely, so the agent must widen the search to the other attendees' calendars.

### F12 (carried) - MINOR - OE 20 - universal negative under a partial enumeration

Unchanged. OE 20 claims "no water heater record in the universe is associated with Mesa Vista or with either of Lisa's owners", then lists 412 Mesquite and Pinecrest 12. The Hardness Plan's H2 lists four destinations, adding Dunmore Unit 3 and 2214 Oleander. An agent that finds one of the two unlisted destinations has reason to think the OE is wrong.

**Fix.** Either enumerate all four, or drop the enumeration and state the sweep method that supports the negative.

### F11 residue - MINOR - the 97% collections figure is mandated but never established

OE 11 now handles the 94% occupancy figure thoroughly, including the Oakfield decoy. OE 33 requires the draft to state that "the 94 percent occupancy **and 97 percent collections** figures have no supporting record", and the decompose directive grades it as "the occupancy and collections correction". No OE establishes the collections half. OE 21 tests the related late-payment claim, which is a different assertion.

**Fix.** Add one clause to OE 11 or OE 21 naming what was swept for a collections source (QuickBooks carries invoices and payments, not a collections rate) so the negative is earned rather than asserted.

---

## [B1] QC sub-dim scoring

`SUB-DIM OE Completeness -> SCORE 5/5 -> REASON Both round-1 critical-path gaps are closed and verified: OE 13 now supplies the Harris-to-Sunset-Ridge bridge from the only row in the universe that carries it, and OE 30's correction set is exhaustive against the measured 6-row selSched population, so all six writes now have determined targets.`

`SUB-DIM OE Accuracy -> SCORE 4/5 -> REASON Two stated expected values still do not match: OE 7 lists a thread reply among what a channel read returns and then says that read does not surface it (N1), and OE 27's "makes both look settled" is contradicted by OE 29's own record of Lisa's declined row (F10).`

**Why Completeness reaches 5.** Every element PASS(5) names is present. Key discovery steps: both owner-to-property bridges, the thread read, the calendar widening past the persona, the QuickBooks sweep including the negative confirmation. Dependency chains: OE 13 precedes the Harris cluster pull, OE 32 precedes the draft, OE 19 precedes the Ridgeview correction. Every required write action: all six, each licensed by the prompt, each with a decompose directive. The 97% collections residue is a sub-element of one graded criterion rather than a missing step, so it is recorded as MINOR rather than scored against this sub-dim.

**Why Accuracy stops at 4.** The measured accuracy rate is high: 21 of 21 parameter sets exact, 4 of 4 issue states exact, the 6-row selSched population exact, 7 of 7 open tickets exact including the empty-string-versus-null split, 2 of 2 per-calendar row ids exact, 346 of 580 exact, the Oakfield decoy real, and all four money totals verified in round 1. Against that, N1 is a self-contradiction inside a single OE on the file's highest-value lever, and F10 is a direct contradiction between OE 27 and OE 29. Both are stated expected values that do not match, which is what this sub-dim measures.

---

## [B2] Adversarial alt-path

### (a) Different Airtable rows than the OE names

**Now FORECLOSED, with one bounded residue.** Round 1 found this wide open. The revision enumerates the `selSched` population exhaustively, and I verified the count independently: 6 rows in scope, 3 corrected and 3 excluded, each exclusion carrying a ground reason (`rec88734a4fdfde57` waiting on a July 16 inspection, `reca06d89f1a4ac5b` waiting on an unresolved utility transfer, `reca8230a8fd9ff51` conditional on an incomplete eviction). An agent that runs the same test reaches the same three rows.

The residue is Mesa Vista 207A and 4C (N3), where the OE declines two genuine mismatches for a reason that does not survive the prompt. That is a grading-boundary problem, not a divergence problem: an agent that corrects them is not wrong and is not penalised.

### (b) One owner only

**FORECLOSED.** OE 31 now opens "Resolve both owners' review meetings on the calendar. Both are required, because the prompt's condition fires on each of them independently." That is explicit, and it is backed by a decompose directive naming two content elements. The round-1 permissive framing is gone.

### (c) Different new-issue target

**FORECLOSED.** See B-RULE13(c).

### New probe this round: could an agent scope Harris to Unit 14 alone?

**Partially open (N2).** The only bridge names Unit 14. An agent that takes the bridge literally scopes Harris to `reca8230a8fd9ff51`, which is the Tanya Mitchell delinquency row and which OE 30 excludes from correction. It would then produce zero Harris corrections. The property-level inference that carries Harris from one unit to the whole cluster is correct but unstated. The N2 fix states it.

---

## [B3] Tool-call density projection, PER MODEL

The revision added calls and removed none.

| Change | Effect |
|---|---|
| OE 13 adds the QuickBooks bridge lookup plus the decoy invoice read | +2 to +3 |
| OE 12 now names a two-table `get_table_schema` | +0 to +1 |
| OE 19 adds two calendar cross-references and an invoice cross-reference | +2 to +3 |
| OE 24 adds `get_aged_receivables` to confirm the negative | +1 |
| OE 18 and OE 20 specify more explicit searches | +1 to +2 |
| OE 31 may now use `create_event` in place of one `update_event` | 0 |

| Model | Round 1 | Round 2 | V4 band | Margin over 40 |
|---|---:|---:|---|---:|
| Opus 4.8 | 66.0 | **69.5** (range 56 to 83) | **PASS** | **+29.5** |
| Gemini | 74.5 | **78.0** (range 59 to 97) | **PASS** | **+38.0** |

Against the Hardness Plan's projection of Opus 63.5 and Gemini 66.0, the chain runs **+6.0 and +12.0** above plan. The enrichment source is unchanged from round 1 and is now larger: the file specifies per-record confirmation across QuickBooks (7 invoices, 6 credit memos, 2 customers, 1 aged-receivables call) and per-event confirmation across Calendar, both of which exceed the plan's per-segment budgets.

The Gemini-above-Opus sign matches the plan's empirical anchor, which is that Gemini's count scales with explicit enumeration. This chain enumerates 16 make-ready rows, 7 invoices, 6 credit memos, 7 maintenance rows and 5 calendar events by id.

**One downward pressure, unchanged:** OE 12's three plumbing calls may be skipped by an agent that goes straight to `search_records`. Worst case Opus 66.5 and Gemini 75.0. Still far above 40.

**No fix in this report reduces density.** N1 is neutral, N2 and F11-residue each add a call or two, N3 is neutral, F12 is neutral.

---

## [B4] Hardness preservation

| Lever | Status | OE steps |
|---|---|---|
| **L1** Latching on the persona's own undispositioned claim | **PRESERVED (strong)** | OE 7 (parent), OE 8 (the claim, thread-gated, plus the new dangling-pointer warning), OE 9 (the C004 pair extending it to both owners), OE 11 (propagation into `comment_5a6d779a715f587392dd00b9c8dbbd4a`, now with the Oakfield decoy strengthening the "no independent source" finding), OE 14 (four Mesa Vista units against "one unit"), OE 20 (water heater), OE 21 (late payment), OE 33 (all four corrections mandated and decomposed) |
| **L2** Structured-DB skip | **PRESERVED, strengthened** | QuickBooks: OE 22 to OE 26, now including `get_aged_receivables` to confirm the Harris negative rather than resting it on an empty search. Calendar: OE 27, OE 28, OE 29. The QuickBooks half also now carries the Harris bridge (OE 13), which makes the store load-bearing for discovery and not only for money |
| **L7** Multi-write diversification | **PRESERVED (no longer at risk)** | Six writes across five services: OE 30 airtable (3 rows), OE 31 gcalendar (2 owners), OE 33 gmail, OE 34 linear comment, OE 35 linear issue, OE 36 slack. Round 1 rated this at risk because two writes were underspecified. Both are now specified: OE 30's set is exhaustive and OE 31 pins per-calendar rows with a verified-feasible verb set |
| **L10** Reversal / supersession | **PRESERVED, strengthened** | Harris double-booking (OE 28), OPS-10 state against its own narration (OE 4, OE 34), OPS-100 "moving this to Done" at `state_OPS_2` (OE 11), Finley review against `comment_79dc83838bd65d678c48b5911f942412` (OE 29), the Harris original against its Slack announcement (OE 29, new), and **OPS-39 versus OPS-93 (OE 11, new, states verified)**. Round 1's HARDNESS_PARTIAL is closed |
| **L11** Net-vs-gross | **PRESERVED (strong), sharpened** | OE 25 now leads with `Balance` equal to `TotalAmt` and absent `LinkedTxn` as what governs, then names `RemainingCredit: 0` explicitly as the trap that "reads the other way". That ordering is better than round 1, which listed them flat. OE 26 names the $7,325 netting error. OE 33 mandates the written finding. Still correctly carried with no write carrier, per Handoff obligation 6 |

**No HARDNESS_REGRESSION. No HARDNESS_PARTIAL.** All five levers fire, two are stronger than at round 1, and the one round-1 partial is closed.

### Contrast pair: Harris operationally blocked versus Finley cash-blocked

**PRESERVED, and now symmetric in the action set.** Round 1's complaint was that every operational write landed on Harris, so the contrast survived in prose but not in behaviour. That is fixed: OE 30 now corrects `rec8b679d92f30753` on Finley's Ridgeview property alongside the two Harris rows, so both owners carry an operational correction and both carry a calendar resolution (OE 31), while only Finley carries a money position (OE 23, OE 25, OE 26).

The prose statement is also stronger. OE 24 retains "The two owners are behind for different reasons, and reporting them as a single 'both owners are behind' position loses that distinction", and OE 33 now states Harris's position in terms that survive the agent's own writes: "every make-ready row on his Sunset Ridge units sitting in Scheduled or In Progress and none in a Ready state". I verified that holds after OE 30's corrections: Harris's 7 rows end at 5 `selProg` and 2 `selSched`, zero `selReady`. Round 1's round-count phrasing would have been a meta-statement about the agent's own writes; this phrasing is not.

---

## [B6] Upstream propagation

**ZERO flags.**

The round-1 conditional flag on the prompt's "spring read" phrasing is **withdrawn**, because the finding that generated it was my error. The reply is dated 2026-05-28 on both `ts` and `created_at`, so `5_Prompt.txt:3` is accurate against the universe.

**Write-licensing re-audit.** All six writes remain licensed by the prompt, unchanged from round 1. One new item to note without propagating:

OE 31 now offers `create_event` as an alternate for the Finley half. The prompt's "Do the same for their review meetings if either of those did not end up properly settled" inherits the correction verb, and creating a replacement review is a reasonable way to put an unsettled meeting right, so this is licensed rather than beyond-prompt. **Watch item for S3, not a propagate:** `update_event` and `create_event` are alternate paths to one outcome and must sit inside a single accept-set, never as two criteria. OE 31's decompose directive already frames it that way ("the Finley review is rescheduled or replaced"), which is correct.

---

## [B8] OE Completeness semantic

| Required step | Present? | Where |
|---|---|---|
| Contact lookup before the draft | Yes | OE 32, immediately preceding OE 33 |
| Owner-to-cluster bridge, Finley | Yes | OE 10, now correctly scoped to what the universe actually supports |
| Owner-to-cluster bridge, Harris | **Yes (new)** | OE 13, via the only row in the universe that carries the link. See N2 for the unstated inference |
| Thread reply rather than channel only | Yes | OE 7 then OE 8, with the dangling-pointer warning added |
| Calendars the persona is not on | Yes | OE 27 then OE 28 |
| Full mismatch sweep across both owners | **Yes (new)** | OE 16, OE 17 for Harris; OE 19 for Ridgeview; OE 30 enumerating the whole `selSched` population |
| Fourth calendar event discriminated | **Yes (new)** | OE 29, pinned by full title |

Round 1 raised four `OE_INCOMPLETE` findings. Three are closed. One residue remains, downgraded:

`OE_INCOMPLETE (MINOR): OE 33 mandates asserting that the 97 percent collections figure has no supporting record, and grades it in the decompose directive, but no OE establishes it. The 94 percent occupancy half is now thoroughly established by OE 11. (F11 residue)`

---

## [B9] OE Service Mapping

**ZERO `OE_SERVICE_MISMATCH`,** and the finding is stronger than at round 1 because parameter names are now verified as well as tool names.

| OEs | Service | Correct? |
|---|---|---|
| 1 to 5, 10, 11, 34, 35 | linear | Yes. Coordination and project items |
| 6 to 9, 36 | slack | Yes |
| 12 to 17, 19, 20, 30 | airtable | Yes. Make-ready and unit records, system of record |
| 18 | airtable `tblMaintenanceTickets` | Yes. Maintenance tickets correctly in Airtable, not Linear |
| 21 | gmail | Yes. Tenant correspondence, with the base64url decode noted |
| **13**, 22 to 26 | quickbooks | Yes. Read-only throughout. OE 13's use of an invoice memo as an ownership bridge is unusual but correct: it is the only place the link exists |
| 27 to 29, 31 | gcalendar | Yes. `create_event` verified present |
| 32 | contacts | Yes |
| 33 | gmail `create_draft` | Yes, with the draft-only constraint stated |
| (excluded) | hubspot | OE 10 now states HubSpot is **not** a route, which is a correct exclusion rather than round 1's unreachable assertion |

One residual scope note, unchanged from round 1 and not scored here: I did not independently verify the Linear `team_001` description text that asserts Airtable primacy for maintenance. OE 18's placement is correct against the AGENTS.md StarPM universe card regardless.

---

## [B-RULE13] Hard rule 13 audit

### (a) Targets satisfied by two or more records

**CLEAN.** Round 1's single hit is closed and verified.

- **OE 31** now pins `qqbwq3s2h7wh5udoek2940mffk-b6a1e41c` (teresa.wood) and `qqbwq3s2h7wh5udoek2940mffk-0f82233a` (brooke.phillips). Both verified to exist on those calendars, both `confirmed`. The event has 4 rows and Lisa holds none, exactly as the file states. The bare base id is explicitly rejected in the OE text.
- **OE 30** pins three unique `rec` ids, verified unique.
- **OE 35** target now discriminated (see (c)).
- **OE 13** correctly warns that "Unit 14" collides and must be qualified by property, and correctly separates invoice 4422 from the 4418 decoy, though see N2 on the discriminator.

### (b) Completeness claims unreconciled against Calendar

**CLEAN on the material claim.** OE 15's superlative is gone. The replacement claim, that the subfloor assessment is the only item in either cluster that is both unresolved **and untracked**, holds against every service including Calendar: MT-2026-047 is tracked as a ticket, the Ridgeview work is tracked by the 2026-07-13 walk-through, Mesa Vista 4C is tracked by the 2026-07-15 QC inspection, and none of the nine future events tracks a subfloor assessment. OE 18's claim is now correctly narrowed to "only open **repair** ticket" and names the other two in-scope open rows.

**One MINOR residue:** OE 20's universe-wide water-heater negative under a two-of-four enumeration (F12).

### (c) Naive-agent simulation

**Materially CLEAN.** Reading `5_Prompt.txt` cold:

- **New issue.** OE 15 and OE 35 now share an untracked-versus-tracked discriminator, and OE 35 states it as the reason: MT-2026-047 already exists as a ticket and the Ridgeview follow-up already has a booked walk-through, "so neither of those needs a new item to survive". That directly answers the prompt's own stated purpose, "so it does not quietly disappear once this is handed over". A naive agent that nominates MT-2026-047 now has a stated reason in the ground truth for why that is the weaker answer. The target is uniquely determined.
- **Airtable rows.** Determined by the exhaustive `selSched` enumeration, with the 207A/4C boundary noted in N3.
- **Calendar.** Both owners required.

**One residue:** the Harris cluster scope under a Unit-14-only bridge (N2).

### Linda Castillo cross-owner bleed

**CLEAN, and improved.** OE 28 now states that the `fullText "Portfolio Review"` query "returns every mid-year portfolio review in the universe, including 'Linda Castillo Mid-Year Portfolio Review'", names her base id, and rules her out: "Castillo is Patricia's owner under the OE 3 split, so she is out of scope here and **no conclusion in this task may rest on her**." It also states that Shea "returns nothing at all", which is correct and doubles as H4 material.

No OE makes an enumeration claim Castillo would falsify, and no write step touches a Castillo record. Round 1's F6 is fully closed.

---

## VERDICT

`VERDICT: BLOCK`

| Gate | Round 1 | Round 2 |
|---|---|---|
| OE Completeness = 5 | FAIL (3) | **PASS (5)** |
| OE Accuracy = 5 | FAIL (3) | **FAIL (4)** |
| No adversarial divergence | FAIL (3 probes) | **PASS with 1 bounded residue** |
| Density Opus >= 40 | PASS (66.0) | **PASS (69.5)** |
| Density Gemini >= 40 | PASS (74.5) | **PASS (78.0)** |
| Every Hardness lever triggered | PASS with caveats | **PASS, no caveats** |
| No PROPAGATE flags | FAIL (1 conditional) | **PASS (0)** |
| Zero OE_INCOMPLETE | FAIL (4) | **FAIL (1 MINOR)** |
| Zero OE_SERVICE_MISMATCH | PASS (0) | **PASS (0)** |
| Zero rule-13 hits | FAIL (a, b, c) | **PASS on (a), MINOR on (b), 1 residue on (c)** |

**Five findings block: three MODERATE and two MINOR.** No MAJOR remains. Nothing structural, nothing infeasible, nothing that touches density or the levers.

### Work remaining, in order

1. **N1** paste the OE 7 replacement. Removes the internal contradiction on L1.
2. **F10** paste the OE 27 replacement. One sentence.
3. **N2** paste the OE 13 replacement. Adds the ItemRef discriminator and the property-level inference.
4. **N3** paste the OE 30 replacement sentence for 207A and 4C.
5. **F12** and the **F11 residue**, both MINOR, both one clause.

All five are wording edits to existing OEs. No new OE is required, no OE is removed, and no downstream artifact assumption changes. On a clean application of these five this council expects Accuracy 5/5 and a GO.
