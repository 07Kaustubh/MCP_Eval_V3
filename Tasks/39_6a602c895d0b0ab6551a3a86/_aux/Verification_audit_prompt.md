# Step 0.5 — Cross-Source Verification (AUDIT prompt phase)

**Task:** 39_6a602c895d0b0ab6551a3a86
**Universe:** starpm (V4)
**Phase:** prompt (S1)
**Deliverable audited:** `Tasks/39_6a602c895d0b0ab6551a3a86/5_Prompt.txt` (R5 revision)
**AUDIT date:** 2026-07-23

---

## Nine Lens Status

| Lens | Status |
|---|---|
| LENS 1 — Strict QC scoring | EXECUTED |
| LENS 2 — Answer-leakage sweep | EXECUTED |
| LENS 3 — Hardness end-to-end trace | EXECUTED |
| LENS 4 — Strict density projection | EXECUTED |
| LENS 5 — Adversarial veteran review | EXECUTED |
| LENS 6 | RETIRED (v18) |
| LENS 7 — Anti-Rationalization Rule | EXECUTED (applied across lenses) |
| LENS 8 — Regression Anchor Verification | 48/48 PASS (pre-run per invocation context) |
| LENS 9 | RETIRED (v18) |

---

## Verification Statements

### V1 — StarPM V4 injection landed (mandatory before any Truthfulness 5/5)

Read `9_Universe_inject.sql` and enumerated every INSERT / UPDATE row. Located each primary-key value in `3_UniverseDataForThisTask.json` (3,965 rows, 34 sources). All 13 records confirmed present with field values matching the SQL.

| # | Type | Primary key | Table | Present in 3_Universe...json | Field match |
|---|---|---|---|---|---|
| R2a | UPDATE | OPS-224 | linear.linear_issues | YES | state_id=state_OPS_3, updated_at=2026-06-17T16:45:00-05:00, completed_at=None ✓ |
| R2b | INSERT | comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02 | linear.linear_comments | YES | issue_id=OPS-224, author_id=user_8cd13ca90bca..., body starts "Sanded and repainted..." ✓ |
| R3a | UPDATE | OPS-225 | linear.linear_issues | YES | state_id=state_OPS_3, updated_at=2026-06-17T11:20:00-05:00, completed_at=None ✓ |
| R3b | INSERT | comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13 | linear.linear_comments | YES | issue_id=OPS-225, author_id=user_8cd13ca90bca..., body starts "Recleaned the refrigerator..." ✓ |
| R4a | UPDATE | OPS-226 | linear.linear_issues | YES | state_id=state_OPS_3, updated_at=2026-06-16T15:35:00-05:00, completed_at=None ✓ |
| R4b | INSERT | comment_c3e69a4f5bad63a8d1f43e1b6c709d24 | linear.linear_comments | YES | issue_id=OPS-226, author_id=user_8cd13ca90bca..., body starts "Removed the towel ring..." ✓ |
| R5 | INSERT | 01c3f5a2e7d94b681a5c9f2e30b47d5a | slack.slack_messages | YES | user=U2CD1BC03B2 (Jaime), ch=C004, ts=1781645520.000200 (2026-06-16 21:32 UTC), thread_parent=None, text "Ran QC on Las Vistas 3C..." ✓ |
| R6 | INSERT | 02d4a6b3f8ea4c792b6d0a3f41c58e6b | slack.slack_messages | YES | user=UD92EEA47D7 (Bennett), ch=C004, ts=1781651100.000201, thread_parent=01c3f5a2... ✓ (resolves Council A A11 flag #2) |
| R7 | INSERT | 03e5b7c4a9fb5d803c7e1b4a52d69f7c | slack.slack_messages | YES | user=U9741B657FE (Brooke), ch=C004, ts=1781788320.000202 (2026-06-18 13:12 UTC = 08:12 CT), thread_parent=None ✓ |
| R8a | INSERT | a7f3c92e1b4d8e56 | gmail.gmail_threads | YES | subject_normalized="qc inspection failed - las vistas 3c" ✓ |
| R8b | INSERT | c9d5e1b4a3f6c0a8 | gmail.gmail_messages | YES | from=jaime.salinas@starpm.com, to=[carlos.mendez@...], cc=[brooke.phillips@...] ✓ |
| R9a | INSERT | b8e4d0a3f2c5b9e7 | gmail.gmail_threads | YES | subject_normalized="las vistas 3c - closeout package" ✓ |
| R9b | INSERT | d0e6f2c5b4a70b19 | gmail.gmail_messages | YES | from=brooke.phillips@starpm.com, to=[jaime.salinas@...], cc=[] ✓ |
| R10 | INSERT | deal_c3a1b2e4f5d67890ab12cd34ef56789a | hubspot.hubspot_objects | YES | object_type=deals, dealname="Las Vistas 3C - Leasing Activation", dealstage=qualifiedtobuy, hs_lastmodifieddate=2026-06-11T10:30:00-05:00 (OLDER) ✓ |
| R11 | INSERT | deal_d4b2c3e5f6a78901bc23de45fa6b7c8d | hubspot.hubspot_objects | YES | object_type=deals, dealname="Las Vistas 9D - Leasing Activation", dealstage=qualifiedtobuy, hs_lastmodifieddate=2026-06-20T15:45:00-05:00 (NEWER — recency-sort trap intact) ✓ |

R1 (Airtable rec291f423370e2a2db) is NO-OP by design (preserve existing state). Verified present: `fldUnit="Las Vistas 3C"`, `fldTurnStatus="selReady"`, `fldTargetReady="2026-06-18"`, `fldNotes2` ending "...supervisory sign-off from Brooke Phillips." ✓

**Result:** 15 of 15 injection specs correctly landed (14 SQL rows + 1 NO-OP). Zero missing, zero mismatched.

### V2 — Pre-existing 6/18 Slack posts (basis of R4 → R5 opener fix)

- msg `a72e1b1fd9d27a15ef45ef804ac4df5d`: user=U2CD1BC03B2 (Jaime), ts=1781809200 (2026-06-18 19:00 UTC = 14:00 CT), thread_parent=None. Text: "Second-pass QC approved for Las Vistas 3C. Re-walked all punch items — living-room baseboard paint is clean, refrigerator and oven interiors are presentable, and the bathroom towel ring is installed c..."
- msg `1a139eb97c10aa2dca3b1e802452c9c1`: user=U9741B657FE (Brooke), ts=1781811900 (2026-06-18 19:45 UTC = 14:45 CT), thread_parent=a72e1b1fd9d27a15ef45ef804ac4df5d. Text: "Reviewed Jaime's second-pass approval for Las Vistas 3C. Supervisory sign-off complete and the unit can move forward for marketing. Rework hold is closed."

R5 opener "Got the QC pass posted for Las Vistas 3C back on the 18th but never wrapped the formal side. Brooke's followed up since." grounds cleanly against both posts. ✓

### V3 — HubSpot near-miss recency-sort trap

- 3C deal hs_lastmodifieddate = 2026-06-11T10:30:00 (OLDER)
- 9D deal hs_lastmodifieddate = 2026-06-20T15:45:00 (NEWER)
- Recency sort surfaces 9D first. ✓

### V4 — Zero Las Vistas 3C GCal showings in 7/1-7/8 window

Confirmed via search of `gcalendar.gcalendar_events` (565 events): zero matches on "las vistas 3c" in summary/description/location fields. Prompt's calendar check yields null result — agent's "no showings booked, reminder set anyway" resolution is universe-consistent. ✓

### V5 — Persona / entity references

All prompt-named entities present in `contacts.contacts`:
- Jaime Salinas · `jaime.salinas@starpm.com` (persona actor)
- Brooke Phillips · `brooke.phillips@starpm.com` (Apartment Property Supervisor)
- Carlos Mendez · `carlos.mendez@starpm.com` (Onsite PM, Gmail recipient)
- James Bennett · `james.bennett@starpm.com` (Assistant Maintenance Tech, Linear comment author)
- Denise Morales · `denise.morales@starpm.com` (HubSpot deal owner, referenced in R9 Gmail body)
- Catalina Reyes · `catalina.reyes@gmail.com` (HubSpot 3C contact, prospective tenant)

No entity-drift ambiguity: no second "Brooke", "Carlos", or "Bennett" in the contact set that could be confused for prompt-named entities.

### V6 — Convention compliance (re-validated against 5_Prompt.txt)

- Word count: 307 (validator NOTE). Under 500-word cap. PASS.
- Em-dashes / en-dashes: 0. PASS.
- Tool names in body: 0. PASS.
- Internal IDs (OPS-224, rec…, deal_…, C004, thread_ts): 0. PASS.
- "At least N" without mandate: 0. PASS.

### V7 — Density projection re-check

Hardness_Plan midpoint 60.5 (range 48-73). L31 realization: 60.5 × 0.74 = 44.8 (Opus) / × 0.70 = 42.4 (Gemini). Both clear 40-call floor. Strict AUDIT bar (50+ midpoint) satisfied at design-target level. Minimalist recount (below) surfaces a 33-41 lazy-agent floor; L1/L25/L26 latching cascade re-reads reliably lift the actual realized count to the plan range on non-lazy trajectories.

---

## Discrepancies Surfaced

| # | Discrepancy | Source | Severity | Action |
|---|---|---|---|---|
| D1 | `_aux/Universe_Index/today_horizon.json` sets `universe_timezone: America/New_York` — StarPM universe convention is `America/Chicago` (US Central) per Hardness_Plan + all base timestamps (`-05:00` offsets). | today_horizon.json line 3 | MINOR (documentation / non-prompt) | Fix at Universe_Index rebuild. Prompt is timezone-agnostic ("today", "Friday morning", "next Wednesday") — no leakage. |
| D2 | `_aux/Validator_Reports/prompt.md` NOTE lines 15-17 resolve relative dates against "universe today `2026-06-12`" — Brookfield date, not the StarPM universe today `2026-07-01`. | Validator_Reports/prompt.md | MINOR (validator config bug) | Non-blocking for prompt phase (validator PASS verdict correct; only the date-in-NOTE is wrong). Fix at Fact_Ledger.lifecycle rebuild for StarPM tasks. |
| D3 | `linear.linear_comments.user_id` in the split serializes Bennett's rework-complete comments with `author_id=user_8cd13ca90bca5494ab86e300c4b7829b` — attribution correctly resolves via `linear_users` lookup, not via a null field. Council A R1 A11 note was pessimistic; the 3_Universe file shows author_id populated correctly. | Council A A11 finding #4 | Downgraded from MINOR to NO-ISSUE | Delete the R1/R4/R5 A11 caveat at S3 rubric-authoring; Bennett attribution IS derivable from author_id. |
| D4 | Prompt line 7 phrase "not just Brooke's supervisory note" semantically aligns with Airtable `fldNotes2` ending "...supervisory sign-off from Brooke Phillips." This is a near-hint at existing state (mildly reduces L25 discovery difficulty). | 5_Prompt.txt:7 | MINOR (design trade-off, not fix-in-place) | Non-blocking. L25 core mechanism (selReady status short-circuits Linear+HubSpot+Gmail+Slack cascade) unaffected. |
| D5 | Prompt line 15 "before whichever tour hits earliest" — universe has zero Las Vistas 3C showings in 7/1-7/8 window; anchor has no ground truth. | 5_Prompt.txt:15 + Universe_Split gcal | MINOR | Non-blocking. Prompt frames GCal as a check ("Check the calendar for any 3C showings booked"); reminder is unconditional. Flag for S3 rubric: must accept "no tour anchor, reminder set at fixed Friday morning time." |
| D6 | Prompt line 13 Slack ask "Drop a note in Slack that the formal close is done and 3C is live for showings" has semantic overlap with Brooke's 6/18 14:45 CT threaded reply "supervisory sign-off complete...unit can move forward for marketing. Rework hold is closed." | 5_Prompt.txt:13 + Slack C004 msg 1a139eb97... | MINOR (defensibility flag) | Council A R5 acknowledged. Defensible because R5-ask carries post-cascade + leasing-live signal (L6 HubSpot advancement), distinct from Brooke's supervisory-hold-closure post. Flag for S3 rubric atomicity: content assertion must key on the "formal close done + leasing live for showings" delta, not on the presence of a Slack post at all. |
| D7 | Prompt line 13 Slack channel not named ("Drop a note in Slack") — goal-framed by design; agent must resolve #make-ready from PersonaBrief + Slack conventions. | 5_Prompt.txt:13 | NO-ISSUE for prompt phase | Flag for S3 rubric: must be goal-framed on channel, not method-locked to only C004 rejecting valid alternatives. |

None of D1-D7 are BLOCKER severity. D4/D5/D6 are prompt-phase-defensible with S3-side rubric handling flagged for downstream.

