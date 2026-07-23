# OE Solvability — 39_6a602c895d0b0ab6551a3a86 (REDO — R5 build, 2026-07-23)

## OE-to-prompt coverage map

| Prompt sentence / ask | Covered by |
|---|---|
| Trigger: never got a proper closeout together on 3C after second-pass re-check "back on the 18th"; Brooke's followed up since | OE1 (orientation), OE2 (Brooke identity), OE24 (Brooke canonical Gmail thread), OE26 (Brooke canonical Slack parent) |
| All three punch items cleared on the re-check (baseboard, appliance interiors, towel ring) | OE1 (narrative anchor), OE10-12 (Linear ticket subjects), OE13-15 (Bennett per-item observations) — ground truth Jaime carries into the closeout writes |
| Bennett dropped a completion note on each of the three 3C punch items | OE13-15 (list_comments per ticket, surfaces Bennett rework-complete comments) |
| Pull his note off each ticket and make sure the item he's writing up actually matches what the ticket is about before I sign off | OE10-12 (get_issue per ticket, confirm subject) + OE13-15 (Bennett comment read + explicit "Verify... matches... Conclude: item matches" clause) |
| Get each ticket moved through my sign and out of my queue with the pass called out for each item, not a blanket close | OE16 (Done state resolve) + OE17/OE19/OE21 (per-item Jaime closeout comments) + OE18/OE20/OE22 (state → Done, individually per ticket) |
| Pull the make-ready record on 3C and get my second-pass sign-off written into it. My name, the re-inspection date, and one line per punch item | OE6 (base + table discovery) + OE7 (schema fetch) + OE8 (record fetch + existing narrative pre-read) + OE23 (update_records_for_table append to fldNotes2) |
| Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement | OE8 (explicit read of full fldNotes2 body verbatim) + OE23 (append preserving existing narrative — L25 anchor trap defused) |
| Anyone pulling 3C up after this should read the second-pass sign-off and not just Brooke's supervisory note | OE23 (append lands in fldNotes2 narrative itself, not a comment substitute) |
| Leasing has been waiting on 3C to open showings, so they'll want the heads-up from us | OE3 (Carlos identity), OE5 (Sandra identity — leasing-side pickup), OE25 (Gmail hand-off to Carlos), OE27 (Slack #make-ready post tagging Sandra) |
| Carlos needs an email from us that 3C is clear so leasing can start today. Copy Brooke so she knows the loop closed on 3C. Keep it short | OE24 (Gmail canonical thread discovery + decoy verification via 2 get_thread calls) + OE25 (create_draft to Carlos, cc Brooke, replyToMessageId, short body per requester instruction) |
| Post in the #make-ready channel that the formal close is done and 3C is live for showings, and tag Sandra so leasing sees it | OE26 (channel resolution + canonical parent identification + 2 decoy enumeration) + OE27 (slack_send_message threaded under canonical, message content, Sandra `<@UADB2B4E045>` tag) |
| Check the calendar for any 3C showings booked between now and next Wednesday | OE28 (list_events on Jaime's calendar 7/1-7/8 window, fullText "Las Vistas 3C"; null-result acceptable per S1 flag) |
| Set me a reminder for Friday morning to spot-check 3C's fridge and oven interiors again before whichever tour hits earliest | OE29 (create_event Friday 2026-07-03 morning America/Chicago, summary + description tying to 6/18 second-pass QC pass + any earliest 3C showing from OE28) |

## OE-to-rubric mapping preview (S3 forward projection)

| OE | OE type | Predicted rubric type | Notes |
|---|---|---|---|
| OE1 | Orientation | none | anti-latching guidance embedded; not a rubric-covered step |
| OE2-5 | Contact discovery | none | read-only lookups; downstream Outcome rubrics prove they happened |
| OE6-8 | Airtable discovery + pre-read | none | read-only; OE23 Outcome rubric proves OE8 happened via preserved-narrative check |
| OE9 | Linear enumeration | none | read-only; downstream write Outcomes prove |
| OE10-15 | Per-ticket detail + Bennett comment verification | none | read-only; OE17/19/21 per-item Outcome rubrics prove content-derived attribution match |
| OE16 | Done state resolution | none | read-only |
| OE17 | Jaime closeout comment OPS-224 | Outcome 1.1 (comment posted) + Outcome 1.2 (baseboard-specific content) | atomic — one 1.1 per save_comment |
| OE18 | State flip OPS-224 → Done | Outcome 1.1 (issue state=state_OPS_4) | atomic |
| OE19 | Jaime closeout comment OPS-225 | Outcome 1.1 (comment posted) + Outcome 1.2 (appliance-interiors-specific content) | atomic |
| OE20 | State flip OPS-225 → Done | Outcome 1.1 (issue state=state_OPS_4) | atomic |
| OE21 | Jaime closeout comment OPS-226 | Outcome 1.1 (comment posted) + Outcome 1.2 (towel-ring-specific content) | atomic |
| OE22 | State flip OPS-226 → Done | Outcome 1.1 (issue state=state_OPS_4) | atomic |
| OE23 | Airtable fldNotes2 append | Outcome 1.1 (update_records call) + Outcome 1.2 (Jaime attribution) + Outcome 1.2 (existing-content preservation) + Outcome 1.2 (per-item detail — 3 items) | multi-atomic 1.2 per V4 spec — DO NOT bundle |
| OE24 | Gmail canonical thread discovery + decoy verification | none | read-only; OE25 Outcome rubric proves canonical thread lock via replyToMessageId |
| OE25 | Gmail draft to Carlos + Brooke cc'd | Outcome 1.1 (draft created) + Outcome 1.2 (recipient list) + Outcome 1.2 (subject + replyToMessageId thread lock) + Outcome 1.2 (short body content confirming 3C clear + leasing-live) | cc does NOT split into separate 1.1 per V4 atomicity; body atomic |
| OE26 | Slack channel resolution + canonical vs decoy identification | none | read-only; OE27 Outcome rubric proves thread lock |
| OE27 | Slack post with Sandra tag threaded under canonical | Outcome 1.1 (send_message call) + Outcome 1.2 (message body content) + Outcome 1.2 (Sandra `<@UADB2B4E045>` EXACT tag) + Outcome 1.2 (thread_ts = canonical Brooke ping) | multi-atomic 1.2 per V4 spec — tag stays EXACT (structured field) |
| OE28 | Calendar showings check | Outcome 2.1 (fact reported — null-result acceptable) | optional Outcome 2.1; primary purpose is informing OE29 description |
| OE29 | Friday reminder create_event | Outcome 1.1 (event created) + Outcome 1.2 (Friday 2026-07-03 window) + Outcome 1.2 (summary + description tying to fridge/oven spot-check + 3C) | event window 07:00-10:00 CT rather than exact clock time (per AUDIT R4 guardrail) |

**Rubric count projection:** ~10 Outcome 1.1 + ~13 Outcome 1.2 + up to 1 Outcome 2.1 = ~23-24 total rubrics. Zero Process rubrics (three-condition test fails for Bennett-verify / Airtable pre-read / canonical thread selection — all capturable via tight Outcome rubrics).

## Density profile

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (contacts, base + table + schema, channel resolution) | 8-11 | 9.5 |
| L1 Latching (Airtable pre-read + re-read on hesitation) | 2-4 | 3 |
| L8 Multi-link chain (3× get_issue + 3× list_comments with pagination + Done state resolve) | 8-11 | 9.5 |
| L9 StarPM parameter gotcha (retry loops on Slack/Gmail/Airtable/Linear parameter shapes) | 2-4 | 3 |
| L25 Existing-output anchor (extra Airtable + Linear re-reads to confirm state before write) | 2-4 | 3 |
| L26 Decoy parent thread (Slack channel walk + 2 Gmail decoy get_thread + 2 Slack 6/16 decoy observations) | 4-6 | 5 |
| Sandra hand-off contact lookup | 1-2 | 1.5 |
| Write actions (3 Linear comment + 3 Linear state flip + Airtable update + Slack post + Gmail draft + calendar event) | 10-13 | 11.5 |
| Cross-service triangulation buffer | 2-4 | 3 |
| **TOTAL projected** | **39-59** | **~48-49** |

**Density gate:** midpoint 48-49 → **THIN_DENSITY** (band 40-49). Above 40 absolute floor; below 50+ STRICT bar. Accepted per pipeline v21 policy with mandatory S4 attention flag on Gemini avg tool-call count (if < 40 on real trajectories → PIPELINE REDO with different lever combination).

## AUDIT verdict summary

- Round 1 AUDIT: **REVISE** (Lens 5 density THIN under STRICT 50+ bar; Lenses 1-4, 6, 7, 8 PASS).
- R1+R2+R3 recommendations applied in-place (OE9 broader list_issues, OE13-15 pagination + explicit content-derivation attribution, OE24 explicit get_thread on both decoys, OE26 list_channels + second-decoy enumeration, OE27 generalized anti-fail-branch guidance).
- R4 recommendations propagated to S3 (5 rubric-authoring guardrails documented in Verification_s2.md Discrepancies section).
- Post-fix state: **PASS with THIN_DENSITY policy escape** — ~48-49 midpoint after amplifications; density ceiling is R5-prompt-scope constraint (S1.5 lever set), not OE authoring defect. Further AUDIT iteration would not change verdict.

## S2 exit — hand-off to S3

- `6_Oracle_Events.txt` finalized (29 OEs, 57 lines, validator PASS, 0 em/en-dashes).
- All 5 preserved hardness levers exercised end-to-end; L6 HubSpot correctly absent.
- Forward-map to S3 rubrics complete (~23-24 rubrics predicted, zero Process).
- Mandatory S4 attention flag documented (Gemini avg tool-call count threshold).
- 5 PROPAGATE-TO-S3 rubric-authoring guardrails documented for S3 kickoff.
