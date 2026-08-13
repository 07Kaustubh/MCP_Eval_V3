# S3 Rubric Coverage Matrix

**Task:** `Generated_Tasks/3_6a797ca9aaeb231749d71fc3`
**Rubric count:** 30 (6 Outcome 1.1 write-action results, 20 Outcome 1.2 write-action content, 4 Outcome 2.1 reply facts, 0 Process)
**AUDIT verdict:** PASS (STRICT) — see `_aux/Council_Reports/AUDIT_rubrics.md`
**Council A verdict:** GO (all 26 -> 30 concrete values grounded)
**Council B verdict:** REVISE applied (F1 category enum + F3 concrete diff scale + F4/F5/F6/F7 atomicity splits) -> re-verified 0 fails, 7% Moderate+ (well below 15% FAIL line)

## Prompt sentence -> OE step(s) -> Rubric(s)

| Prompt clause | OE step(s) | Rubric(s) |
|---|---|---|
| Para 1: "Before Monday I need to know what has actually merged on Combo-Fighters over the last quarter, what is still open, and who owns each piece." | OE 1-11 (discovery reads) | Covered indirectly through R12-R16 (brief) + R25-R29 (reply). |
| Para 2: "Start on the Combo-Fighters repo. Walk the pull-request history since December..." | OE 1, 2, 5, 6, 7, 10 | R2, R3, R4, R12, R13, R14 (identify PR #1 draft, PR #36 merged, PR #16 merged in comment + brief). |
| Para 2: "If a merged PR still has review pushback that never got resolved, that counts as still open for the brief." | OE 8, 9 | R5 (ART comment), R15 (brief), R25 (reply), R10 (Trello comment). |
| Para 2: "If a draft PR has no code in it at all, note that separately so we can decide whether to close it out later." | OE 2 | R2 (ART comment), R12 (brief), R25 (reply). |
| Para 3: "Then cross-check that against the Zombie Match 3D roadmap board... Read the checklist items on those cards, not just the card names." | OE 15-22 | R7 (toggle Marcus complete), R8 (leave Engineer incomplete), R18 (brief toggled), R19 (brief incomplete), R27 (reply Engineer open). |
| Para 4: "Get the owner attribution right... If you list a Marcus as the owner of something, be specific about which Marcus." | OE 11, 12, 13 | R6 (ART comment), R16 (brief GitHub-Marcus), R17 (brief enumerates 3 mailboxes), R28 (reply). |
| Para 5: "put a reconciliation comment on the ART tracking ticket in Linear" | OE 24, 25 | R1 (create Linear comment on ART-770) + R2-R6 (content). |
| Para 5: "and update the affected roadmap card in Trello. Leave a comment there on what still needs owner attention" | OE 26, 27 | R7 (toggle), R8 (leave incomplete), R9 (add Trello card comment), R10 (comment content). |
| Para 5: "close out any checklist items that the merged code actually finished" | OE 26 | R7 (toggle Marcus-to-create complete). |
| Para 5: "Then write me a short status brief in a Drive doc I can send Leonard on Monday morning" | OE 28 | R11 (create GDoc) + R12-R22 (11 content rubrics for the brief). |
| Para 5: "put the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet so I have one place to work from" | OE 29 | R23 (create GSheet) + R24 (Leapblock row) + R24a (Martin Walsh row = R24-alt). |
| Para 6: "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read, or whether I need to push back on it Monday morning." | OE 30 | R25 (supports parking), R26 (push back on broader framing), R27 (Engineer open), R28 (Marcus attribution). |

## OE write actions -> Rubric coverage

| OE | Action | Category coverage | Rubrics |
|---|---|---|---|
| OE 25 | Linear create_comment on ART-770 | 1.1 + 5x 1.2 | R1, R2, R3, R4, R5, R6 |
| OE 26 | Trello update_check_item x1 (complete) + preserve x1 (incomplete) | 1.1 x2 | R7, R8 |
| OE 27 | Trello add_comment on card | 1.1 + 1.2 | R9, R10 |
| OE 28 | GDocs create_document | 1.1 + 11x 1.2 | R11, R12-R22 |
| OE 29 | GSheets create_spreadsheet | 1.1 + 2x 1.2 | R23, R24, R25 (note: R24 = Leapblock row, R25 = Martin Walsh row per updated numbering — see raw file for exact indices) |
| OE 30 | Reply to Victor | 4x 2.1 | R26-R29 |

## Hardness lever preservation (from Hardness_Plan.md)

| Lever | Predicted stump | Rubric carriers |
|---|---|---|
| L1 Latching (PR #1 as stale anchor) | Agent reports PR #1 as active in-progress art-import | R2 (draft/no-code call-out in ART comment), R12 (brief), R25 (reply parking) |
| L2 Structured-DB skip (GitHub review_comments carrier) | Agent misses PR #37 unresolved CHANGES_REQUESTED | R5 (ART comment), R10 (Trello comment), R15 (brief), R26 (reply push back) |
| L2 Structured-DB skip (Trello check_items carrier) | Agent will not surface incomplete check_items | R7 (toggle), R8 (leave incomplete), R18 (brief closed), R19 (brief still open), R27 (reply) |
| L6 Marcus disambiguation (4 Marcuses) | Agent conflates GitHub Marcus with Marcus Bennett | R6 (ART comment), R16 (brief GitHub-Marcus), R17 (brief enumerates 3 mailboxes), R28 (reply triangulation) |
| L9 Authority dismissal (Leonard's "treat as parked") | Agent accepts dismissal wholesale | R21 (brief parking safe), R22 (brief broader claim overstates), R25 (reply parking), R26 (reply push back) |
| L10 Reversal / supersession (PR #1 superseded by #36/#16) | Agent misses supersession | R3 + R4 (ART comment: PR #36 + PR #16 merged), R13 + R14 (brief), R7 (toggle Marcus complete = the supersession act) |

All 5 predicted stumps have rubric carriers. Lever coverage preserved through the F4-F7 atomicity splits — splits only tightened discrimination, not weakened it.

## Coverage sanity checks

- Zero prompt asks without a rubric.
- Zero rubrics beyond prompt scope (each traces to a prompt clause + an OE step).
- Zero Process rubrics needed: no prompt-mandated ordering constraint (Para 3 "Then" and Para 5 "Then" are enumerative-narrative, not sequential).
- 30 rubrics << 60 ceiling (rule 14).
- Process 0/30 = 0% << HG cap of 40% (rule 8 HG variant): PASS.
- Density projection 56 midpoint x 7 services (from Hardness_Plan): PASS HG authoring target 40+ AND 3+ services.
- Every write-action rubric pins a unique universe target (rule 13): ART-770 (deterministic via OE 24 fallback), Trello card 6851a9942b47001e59c8e777, check_items 6855f20fb11687de8c0be3c8 and 6855f2153528bf8d9fb8e116, PRs #1/#16/#36/#37, PERSON_0396_GITHUB_USERNAME, martin.walsh@harmonygames.co, three .co Marcus mailboxes.
