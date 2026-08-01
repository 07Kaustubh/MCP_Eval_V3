# Rubric Coverage Matrix - Tasks/46_6a62ccb6ce2323b4b9e0c8d8

Universe: starpm (V4). Criteria: 34 (34 outcome / 0 process). Ceiling: 60 (AGENTS.md rule 14).
AUDIT verdict: REVISE (round 1), all findings applied; re-audit pending.

Every prompt ask maps to at least one criterion (no gaps). Every criterion maps back to a prompt
sentence (no surplus). Criterion indices are 0-based, matching `7_Rubrics.json`.

## Prompt sentence -> OE step(s) -> criteria

| # | Prompt sentence (abridged) | OE step(s) | Criteria |
|---|---|---|---|
| P1 | "Brooke split the mid-year owner reviews between me and Patricia ... I have Harry Harris and Robert Finley with drafts due to owners before the end of June." | OE 1-5 | scope-setting; consumed by 18 (the split names Lisa's half) |
| P2 | "It is now July, so I am already late, and I would rather hand over something complete than something fast." | OE 2 | framing; motivates the hand-off graded at 5 and 18 |
| P3 | "Take both of my owners and work out where each one actually stands today." | OE 3, 13, 14, 19 | 34 (the OPS-10 state contradicts its own comment narrative); otherwise umbrella over P4 |
| P4a | "I need the real position on occupancy" | OE 11, 20 | 12, 26 |
| P4b | "on what maintenance is still outstanding" | OE 18 | 11, 27 |
| P4c | "and on where the turns have got to" | OE 13-17, 19 | 6, 14, 28, 29 |
| P4d | "plus anything on the money side either of them is likely to raise with me" | OE 22-26 | 7, 8, 9, 10, 23, 30, 31, 32 |
| P5 | "I gave Brooke a rough read on my two earlier in the spring, so a fair bit of this should just be confirming it and filling in the gaps." | OE 8, 9, 20, 21 | 12, 13, 14, 15, 16, 26, 29 |
| P6 | "Where the unit and turn records do not line up with what you actually find on the ground, put those records right rather than working around them." | OE 30 | 0, 1, 2 |
| P7 | "Do the same for their review meetings if either of those did not end up settled." | OE 27-29, 31 | 3, 4 |
| P8 | "Put an email together for Brooke covering both owners with the specifics in it." | OE 32, 33 | 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16 |
| P9 | "Bring the mid-year review item up to date on the issue tracker with where my half has landed" | OE 34 | 17, 18, 19 |
| P10 | "and open a separate item for whatever is still genuinely unresolved so it does not quietly disappear once this is handed over." | OE 35 | 20 |
| P11 | "Post a short version in the owner relations channel as well so Patricia and the rest of the team can see where my two sit without having to come and ask me." | OE 36 | 21, 22, 23, 24, 25 |

## Reverse map: every criterion traces to a prompt ask

| idx | Sub-type | Prompt ask | OE |
|---|---|---|---|
| 0, 1, 2 | 1.1 write | P6 | OE 30 |
| 3, 4 | 1.1 write | P7 | OE 31 |
| 5 | 1.1 write | P8 | OE 33 |
| 6 | 1.2 content | P8 + P4c | OE 33 |
| 7, 8, 9, 10 | 1.2 content | P8 + P4d | OE 33 |
| 11 | 1.2 content | P8 + P4b | OE 33 |
| 12, 13 | 1.2 content | P8 + P5 + P4a | OE 33 |
| 14 | 1.2 content | P8 + P5 + P4c | OE 33 |
| 15, 16 | 1.2 content | P8 + P5 | OE 33 |
| 17 | 1.1 write | P9 | OE 34 |
| 18, 19 | 1.2 content | P9 | OE 34 |
| 20 | 1.1 write | P10 | OE 35 |
| 21 | 1.1 write | P11 | OE 36 |
| 22, 23, 24, 25 | 1.2 content | P11 | OE 36 |
| 26 | 2.1 final response | P4a | OE 11, 20 |
| 27 | 2.1 final response | P4b | OE 18 |
| 28, 29 | 2.1 final response | P4c | OE 13-17, 19 |
| 30, 31, 32 | 2.1 final response | P4d | OE 23-26 |
| 33 | 2.1 final response | P3 | OE 4, 11 |

No criterion is unmapped. No prompt ask is uncovered.

## OE decompose-directive fulfilment

| OE | Directive | Carriers | Note |
|---|---|---|---|
| OE 30 | one criterion per row corrected | 0, 1, 2 | 3 of 3 |
| OE 31 | one criterion per calendar outcome | 3, 4 | 2 of 2 |
| OE 33 | one criterion per content element | 5-16 | 12 of 12 after the S3 mirror |
| OE 34 | one criterion per content element | 18, 19 | 2 of 2; directive ADDED at S3 to mirror the atomicity split |
| OE 35 | a single criterion with a two-item accept-set | 19 | 1 of 1 |
| OE 36 | one criterion per content element | 21-25 | 5 of 5; directive widened at S3 to restore the Harris position its own prose named |

Three OE directives were edited in this phase to mirror S3 decompositions. OE 33 was edited to mirror two splits, per AGENTS.md rule 14:
"Harris receivable position including his unapplied credits" became two elements, and "the occupancy
and collections correction" became two. Pre-edit copy at `_aux/6_Oracle_Events.pre_s3_mirror.bak`.
`validate.py --phase oe` still returns 0 fails / 0 warns after the edit.

## Hardness lever coverage (Council B-B4)

| Lever | What it demands | Carrier criteria | Kind |
|---|---|---|---|
| L1 latching on the persona's own spring claim | disposition the claim as wrong rather than repeat it | 12, 13, 14, 15, 16, 24, 27 | report + the 0/1/2 corrections |
| L2 structured-DB skip | query QuickBooks AR and Calendar, neither named in the prompt | 7-10, 22, 28-30 (QuickBooks); 3, 4, 31 (Calendar) | report + write |
| L7 multi-write diversification | 6 writes across 5 services | 0-2 Airtable, 3-4 Calendar, 5 Gmail, 17/19 Linear, 20 Slack | write |
| L10 reversal / supersession | detect the duplicate that never took, and rows the record has moved past | 3, 31 (calendar); 0, 1, 2 (Airtable supersession) | write + report |
| L11 net-vs-gross | state the credits are unapplied rather than netting them | 8, 10, 29 | report only |

L10 history, recorded because it drove two gate rounds. Council B round 2 found the lever carried only by
two criteria that BOTH depended on discovering the June 3 duplicate, the retrieval the Handoff
pre-registers as this task's highest all-fail risk, so criterion 33 was added to reach the lever through
Linear instead. The strict AUDIT then confirmed on independent evidence that the pair tripped the Eval's
"2 or more predicted always-failing" hard gate: it swept all five non-calendar services for any on-persona
pointer to the duplicate and found zero, and noted the prompt's conditional "if either of those" gives an
agent a positive reason to stop once the Finley review is found unsettled. The 2.1 restatement was cut
under rule 21, whose default for an all-failing criterion is removal. The write criterion 3 survives
because it is the prompt-mandated act, and criterion 33 carries the lever on a path the persona can
actually reach, so rule 14's never-cut-a-lever-carrier holds.

L11 is report-only by design: QuickBooks is read-only in this universe, so no write criterion may
touch it (Handoff obligation 4). Its carriers are two 1.2 content criteria and one 2.1, which is the
budgeted arrangement Handoff obligation 6 required be made explicit at S3.

L5 (thread-reply blindness) and L6 (near-miss entity) are sub-levers that the Hardness Plan states
ride L1 and L11 respectively and are "not independently graded", so they carry no separate criterion
by design.
