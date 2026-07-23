# Rubric Coverage Matrix — S3 (REDO)

**AUDIT verdict:** PASS (STRICT) Round 2 · 5/5 Overall Rubric Quality · Major=0 Moderate=0 Minor=0
**Validator:** PASS (0 fails, 0 warns, 5 notes)
**Council A:** GO (all 24 concrete title values grounded)
**Council B:** GO after Round 2 AUDIT reinterpretation (R18/R21 confirmed non-failing structured-field exact-match)
**Rubric count:** 26 outcome / 0 process
**Density:** THIN_DENSITY midpoint ~46-48 (policy escape from S2 carried forward — mandatory S4 Gemini attention flag)

---

## Forward map — prompt sentence → OE step(s) → rubric(s)

| Prompt line | Prompt ask | OE step(s) | Rubric(s) |
|---|---|---|---|
| L1 | Circling back today to finish closing 3C out; Brooke has followed up since | OE1 (narrative anchor) + OE24/OE26 (Brooke's Gmail + Slack follow-ups) | Implicit continuation cue — operationalized in R18/R21 threading discipline (per L26 lever) |
| L2-3 | All three punch items cleared on the re-check (baseboard, appliance interiors, towel ring) | OE1 narrative anchor | Implicit — grounds R2/R5/R8 per-item content and R14/R15/R16 per-item Airtable lines |
| L5 (Bennett verify) | Pull Bennett's note off each ticket and make sure item matches ticket before signing off | OE13/14/15 (Bennett comment reads) | Covered by Outcome R2/R5/R8 (per-item comment content proves the verify happened) — three-condition test rejects a Process rubric here |
| L5 (queue exit) | Get each ticket moved through my sign and out of my queue with the pass called out for each item, not a blanket close | OE17/18 (OPS-224), OE19/20 (OPS-225), OE21/22 (OPS-226) | **R1** save_comment OPS-224 · **R2** per-item baseboard content · **R3** save_issue OPS-224 → Done · **R4** save_comment OPS-225 · **R5** per-item appliance content · **R6** save_issue OPS-225 → Done · **R7** save_comment OPS-226 · **R8** per-item towel ring content · **R9** save_issue OPS-226 → Done |
| L7 (Airtable pull + signoff) | Pull the make-ready record on 3C and get my second-pass sign-off written into it. My name, the re-inspection date, and one line per punch item | OE7/8 (schema + record read), OE23 (update) | **R10** Airtable update on rec291f423370e2a2db · **R11** Jaime attribution · **R12** 2026-06-18 date · **R14** baseboard line · **R15** appliance interiors line · **R16** towel ring line |
| L7 (continuation) | Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement | OE8 (read existing narrative), OE23 (append) | **R13** update preserves existing narrative |
| L9 (leasing heads-up) | Leasing has been waiting on 3C to open showings, so they'll want the heads-up from us before they can move on their end | Sets up L11 + L13 | Implicit — no direct rubric; asks operationalized in R17-R19 (Gmail) + R20-R23 (Slack) |
| L11 (Gmail to Carlos + Brooke cc + hand-off framing) | Carlos needs an email from us that 3C is clear so leasing can start today. Copy Brooke so she knows the loop closed on 3C. Keep it short, this is a hand-off, not a report. | OE24 (Gmail thread discovery + decoy inspection), OE25 (create_draft) | **R17** create_draft to Carlos + cc Brooke (single 1.1 per V4 multi-recipient rule) · **R18** threads under Brooke's canonical closeout thread b8e4d0a3f2c5b9e7 via replyToMessageId d0e6f2c5b4a70b19 (L26 discriminator + implicit "loop closed" continuation) · **R19** body states 3C is QC-cleared / leasing can activate |
| L13 (Slack post + Sandra tag) | Post in the #make-ready channel that the formal close is done and 3C is live for showings, and tag Sandra so leasing sees it | OE26 (channel + decoy thread discovery), OE27 (slack_send_message) | **R20** slack_send_message on C004 · **R21** threaded under Brooke's canonical closeout parent thread_ts 1781788320.000202 (L26 discriminator + Brooke's verbatim "drop the closeout note here") · **R22** Sandra tag `<@UADB2B4E045>` · **R23** message states formal close + live for showings |
| L15 (calendar check + Friday reminder) | Check the calendar for any 3C showings booked between now and next Wednesday, and set me a reminder for Friday morning to spot-check 3C's fridge and oven interiors again before whichever tour hits earliest | OE28 (list_events, null-tolerant), OE29 (create_event) | **R24** create_event on Jaime's primary calendar · **R25** lands Friday 2026-07-03 morning window 07:00-11:00 CT · **R26** summary references 3C + fridge/oven spot-check |

**Coverage confirmation:** every prompt ask (10 explicit + implicit) has at least one rubric. OE28 (calendar-window read) is null-tolerant per prompt phrasing "any 3C showings ... if any" — no explicit rubric required; instrumental read only.

---

## Reverse map — rubric → prompt sentence + OE step

| Rubric | Sub-type | Trace to prompt | Trace to OE |
|---|---|---|---|
| R1 | 1.1 | L5 queue exit | OE17 |
| R2 | 1.2 | L5 "pass called out for each item, not a blanket close" | OE17 content |
| R3 | 1.1 | L5 "out of my queue" | OE18 |
| R4 | 1.1 | L5 queue exit | OE19 |
| R5 | 1.2 | L5 per-item | OE19 content |
| R6 | 1.1 | L5 queue exit | OE20 |
| R7 | 1.1 | L5 queue exit | OE21 |
| R8 | 1.2 | L5 per-item | OE21 content |
| R9 | 1.1 | L5 queue exit | OE22 |
| R10 | 1.1 | L7 "get my second-pass sign-off written into it" | OE23 |
| R11 | 1.2 | L7 "My name" | OE23 content |
| R12 | 1.2 | L7 "the re-inspection date" | OE23 content |
| R13 | 1.2 | L7 "continuation of the supervisory line, not a replacement" | OE8 (read) + OE23 (append) |
| R14 | 1.2 | L7 "one line per punch item" — baseboard | OE23 content |
| R15 | 1.2 | L7 "one line per punch item" — appliance interiors | OE23 content |
| R16 | 1.2 | L7 "one line per punch item" — towel ring | OE23 content |
| R17 | 1.1 | L11 "Carlos needs an email ... Copy Brooke" | OE25 |
| R18 | 1.2 | L1 + L11 implicit continuation ("Brooke's followed up since" + "loop closed on 3C") | OE24 (canonical thread discovery) + OE25 (replyToMessageId binding) |
| R19 | 1.2 | L11 "3C is clear so leasing can start today ... hand-off, not a report" | OE25 content |
| R20 | 1.1 | L13 "Post in the #make-ready channel" | OE27 |
| R21 | 1.2 | L1 + L13 implicit continuation (Brooke's verbatim "drop the closeout note here" in the universe atom + prompt "loop closed on 3C") | OE26 (canonical thread discovery) + OE27 (thread_ts binding) |
| R22 | 1.2 | L13 "tag Sandra so leasing sees it" | OE27 content |
| R23 | 1.2 | L13 "formal close is done and 3C is live for showings" | OE27 content |
| R24 | 1.1 | L15 "set me a reminder for Friday morning" | OE29 |
| R25 | 1.2 | L15 "Friday morning ... before whichever tour hits earliest" | OE29 timing |
| R26 | 1.2 | L15 "spot-check 3C's fridge and oven interiors again" | OE29 content |

**No surplus:** every rubric traces back to a prompt line. Zero rubrics go beyond the prompt.
**No gaps:** every write-action OE (10) has 1.1 coverage; every prompt ask has at least one rubric.
**0 x 2.1:** correct — R5 prompt has no explicit "tell me" cues (write-only task).

---

## Hardness lever coverage

| Lever | Rubric(s) that operationalize it | Discriminator |
|---|---|---|
| L1 Latching (Airtable already selReady) | R10-R16 Airtable append cluster | Agent that latches on "selReady" state skips R10 entirely, cascading zero-passes on R11-R16 |
| L8 Multi-link chain (3 Linear + Airtable + Slack + Gmail) | R1-R9 (Linear chain) + R10-R16 (Airtable) + R17-R19 (Gmail) + R20-R23 (Slack) + R24-R26 (Calendar) | Every rubric has a write-action component; missing any link fails a 1.1 |
| L9 Universe-grounded param traps | R10 (Airtable camelCase), R17 (Gmail body not content, draft not send), R20 (Slack message not payload; not slack_send_message_draft), R1/R4/R7 (Linear save_comment issueId+body) | Wrong parameter names cause tool errors that cascade into 1.1 failures |
| L25 Existing-output anchor trap | R10 + R13 | R10 fires when agent concludes "already Ready"; R13 fires when agent overwrites without pre-reading the existing narrative |
| L26 Decoy parent thread (Slack + Gmail) | **R18 (Gmail) + R21 (Slack)** | The ONLY 2 rubrics operationalizing L26 across both channels; R18 tests replyToMessageId d0e6f2c5b4a70b19 vs decoys a7f3c92e1b4d8e56 / 9f0bd31ccf588236; R21 tests thread_ts 1781788320.000202 vs decoys 1781645520.000200 / 1781620200.000000 |

All 5 preserved levers (post-S1.5 L6 removal) have Outcome rubric coverage. L26 preserved via Option A design-preservation call from AUDIT round 1, confirmed as non-failing structured-field exact-match by AUDIT round 2.
