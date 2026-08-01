# OE Solvability — S2

Task: `Tasks/46_6a62ccb6ce2323b4b9e0c8d8` · Universe: `starpm` (V4) · Universe today 2026-07-01 America/Chicago
`6_Oracle_Events.txt`: 36 steps, OE 1 to OE 29 discovery, OE 30 to OE 36 write.

## Forward coverage: every prompt ask maps to at least one OE

| Prompt clause | Ask type | OE steps |
|---|---|---|
| "Brooke split the mid-year owner reviews between me and Patricia... I have Harry Harris and Robert Finley" | explicit scope | 1, 2, 3, 9 |
| "drafts due to owners before the end of June. It is now July, so I am already late" | explicit state | 2, 4 |
| "work out where each one actually stands today" | explicit | 13, 14, 18, 19, 22 to 26 |
| "the real position on occupancy" | explicit | 8, 11, 13, 14 |
| "on what maintenance is still outstanding" | explicit | 18, 20 |
| "on where the turns have got to" | explicit | 13, 14, 15, 16, 17, 19 |
| "anything on the money side either of them is likely to raise with me" | explicit | 22, 23, 24, 25, 26 |
| "I gave Brooke a rough read on my two earlier in the spring... confirming it and filling in the gaps" | implicit reconciliation | 7, 8, 9, 20, 21 |
| "Where the unit and turn records do not line up... put those records right" | explicit write | 16, 17, 19, 30 |
| "Do the same for their review meetings if either of those did not end up properly settled" | explicit write | 27, 28, 29, 31 |
| "Put an email together for Brooke covering both owners with the specifics in it" | explicit write | 32, 33 |
| "Bring the mid-year review item up to date on the issue tracker with where my half has landed" | explicit write | 34 |
| "open a separate item for whatever is still genuinely unresolved" | explicit write | 15, 35 |
| "Post a short version in the owner relations channel" | explicit write | 6, 36 |

## Reverse coverage: every OE maps to a real prompt ask

No OE goes beyond the prompt. The three that are not directly named by a prompt clause are enabling steps for clauses that are: OE 5 (workflow states) enables the tracker update, OE 6 (channel resolution) enables the channel post, OE 12 (Airtable schema) enables the record corrections. OE 10 and OE 11 establish the owner-to-property link that every downstream Finley step depends on, since Airtable carries no owner field.

## The owner-to-property bridges, which are the load-bearing discovery

Airtable has no owner field, no owner table and no property table, and the string "Harris" appears zero times across all 170 Airtable records. Both bridges therefore come from outside Airtable and both are named explicitly in the OE chain.

- **Finley to Mesa Vista** (OE 10): OPS-100's description, corroborated by Slack `831d2b6760205432a20487e2664a607e`, `a6779a055eaf5fb1893d0ed6d92e3b39` and `2687eb8d7cae501ea99b8c8305f12217`, and three OPS-100 comments. HubSpot ticket `ticket_87552e6b23bc5a92bd2641b9054b8c13` also states it in prose.
- **Finley to Ridgeview** (OE 19): `rec8b679d92f30753` names Robert Finley directly, corroborated by invoice `2026-494`.
- **Harris to Sunset Ridge** (OE 13): the weak one. Four records converge on it, all through the same contested unit: Linear OPS-32, calendar event `nuh928ma4rwhwf1bnap30rmfli`, Airtable `reca8230a8fd9ff51`, and QuickBooks invoice `113714702211`. Two claims made about this bridge earlier in S2 were false and were struck at AUDIT: it is not the only row naming Harris alongside a property (he carries ten such line items across eight records), and `ItemRef` "Monthly Management Fee" does not discriminate ownership (24 customers carry it, including a delinquent tenant, while Robert Finley carries none). Counter-evidence stays visible: invoice `110274597983` bills Simone Okafor for the same unit on the same dates, and Gmail `2ae48555b3009a95` requests eviction authorization from Castillo rather than Harris.

**Carry-forward for S3.** Do not write any criterion that requires the agent to name the owner of Sunset Ridge Unit 14, and do not write one that depends on Harris's ownership of Sunset Ridge being cleanly established, because it is not. Grade the Sunset Ridge make-ready work itself, which is unambiguous, rather than the ownership inference that reaches it.

## OE-to-rubric preview

| OE | Write action | Rubric shape |
|---|---|---|
| 30 | `update_records_for_table` on 3 make-ready rows | one Outcome 1.1 per row, 3 total, per the decompose directive |
| 31 | calendar resolution, both owners | Outcome 1.1 ×2 (Harris duplicate resolved, Finley review rescheduled or replaced) |
| 33 | `create_draft` to Brooke | Outcome 1.1 for the draft, plus Outcome 1.2 per the 10 named content elements |
| 34 | `save_comment` on OPS-10 | Outcome 1.1. The OPS-10 state change is explicitly NOT expected and NOT graded |
| 35 | `save_issue`, exactly one new issue | Outcome 1.1, graded on title and description because `next_issue_number` is 1000 so the identifier cannot be predicted |
| 36 | `slack_send_message` to C006 | Outcome 1.1, plus Outcome 1.2 per the 4 named content elements |

Pure discovery steps carrying no rubric: OE 1 to OE 29, except where a value they establish becomes a graded content element in OE 33 or OE 36.

Budget: 6 write-action carriers plus 19 content elements = 25 criteria before any Outcome 2.1 for the final response. The hard ceiling is 60 (rule 14), so S3 has real headroom. Do not spend it on existence-only criteria that a sibling already grades (rule 28).

**Process rubrics.** Handoff item 11 records that all six `ORDERING` patterns in `check_ordering_coverage.py` return zero hits, so zero Process rubrics is valid. One thing S3 should re-test rather than inherit: the prompt asks for the record corrections and then for an email carrying "the specifics", which could be read as requiring the email to reflect the corrected state. If S3 concludes that is a genuine ordering constraint, rule 23 says it needs a Process rubric and the default-to-zero heuristic does not override it.

## Hardness lever coverage

| Lever | Covering OE steps |
|---|---|
| L1 latching on the persona's own undispositioned claim | 8, 9, 20, 21, and the correction elements in 33 |
| L2 structured-DB skip (QuickBooks AR, unmirrored Calendar) | 22 to 26, 27, 28 |
| L7 multi-write diversification | 30, 31, 33, 34, 35, 36 across six services |
| L10 reversal and supersession | 4, 11 (OPS-39 / OPS-93), 16, 17, 19, 28, 29, 31 |
| L11 net-vs-gross on unapplied credit memos | 25, 26, and the graded content element in 33 |

The contrast pair survives and is stated explicitly in OE 24 and OE 33: Harris is operationally blocked with $0.00 open receivable, Finley is cash-blocked with $10,980.00 past due. An agent reporting "both owners are behind" has retrieved everything and reasoned about none of it.

## Known hazards recorded for S4

1. **The Harris calendar duplicate is reachable only by enumerating calendars Lisa is not on.** She holds no row on `qqbwq3s2h7wh5udoek2940mffk`. An agent scoping Calendar to the persona sees one review per owner and never finds it. This is intended difficulty, and it is the single highest all-fail risk in the task. Rule 21's default for an all-failing criterion is removal, not justification.
2. **Two items in the clusters are unresolved and untracked, not one.** The Mesa Vista 310C subfloor assessment and the Sunset Ridge 309C utility transfer confirmation on `reca06d89f1a4ac5b`, which is the only row in the universe containing the string "utility transfer". OE 15 and OE 35 name the subfloor as the expected target and explicitly accept the 309C blocker as a defensible alternative. S3 must not write a criterion that fails an agent for picking the second one.
3. **Sunset Ridge Unit 14 ownership is contested in the universe.** OPS-32 calls it "one of Harry Harris's units"; Gmail `2ae48555b3009a95` has Brooke requesting eviction authorization from `linda.castillo@gmail.com`; Patricia Nguyen runs the delinquency. The OE chain declines to resolve it and excludes both delinquency records from graded Harris content. S3 must not reintroduce them.
4. **`RemainingCredit: 0` reads as "consumed" and argues against the correct answer.** `Balance == TotalAmt` with absent `LinkedTxn` is what establishes the credits are unapplied. All 117 credit memos share the shape.
5. **Six of 251 Slack `latest_reply` pointers are dangling**, including the one on the C006 thread parent this task depends on. An agent that follows the pointer instead of `thread_parent_id` finds nothing.
6. **A fifth owner-review calendar event exists** (Linda Castillo, `epax0kiwoq0ygmqxezm2pax18l`, Lisa holds a row and accepted). She is Patricia's owner. No criterion may sweep her in, and no enumeration claim may be written that she would falsify.

## Gate history

Thirteen rounds. Council A x4 (BLOCK, BLOCK, BLOCK, BLOCK, blockers 7 -> 4 -> 1 -> 1), Council B x4
(BLOCK x4, closing at Completeness 5/5 and Accuracy 4/5 with the 4 attributed to one sentence), AUDIT
x5 (REVISE, REVISE, REVISE, PASS STRICT, REVISE). Every finding applied. All three gates converged on
one final defect, a false sentence in OE 30 claiming Gmail and Slack rows carry "207A"; direct
measurement found exactly 3 such records, all in Airtable, and the sentence was deleted.

Reports: `_aux/Council_Reports/` AUDIT_oe.md, AUDIT_oe_r2.md, AUDIT_oe_r3.md, AUDIT_oe_r4.md,
AUDIT_oe_r5.md, S2_A_grounding.md, S2_A_grounding_r2.md, S2_A_grounding_r3.md, S2_A_grounding_r4.md,
S2_B_adversarial.md, S2_B_adversarial_r2.md, S2_B_adversarial_r3.md, S2_B_adversarial_r4.md.

No gate re-read the file after the final deletion; three closing runs produced no output. The edit was
a pure deletion of a claim measured false, so it introduced no new assertion.
