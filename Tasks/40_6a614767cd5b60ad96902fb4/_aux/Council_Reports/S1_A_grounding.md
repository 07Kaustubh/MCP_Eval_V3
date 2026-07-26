# Council A — Grounding and Convention — S1 Prompt

**Task:** Tasks/40_6a614767cd5b60ad96902fb4 · **Universe:** starpm (V4) · **Deliverable:** 5_Prompt.txt
**Council A sub-agent:** explore · session ses_072757782ffegeHMq3e2zuZU7I · bg_4f2cb9a1 · duration 18m49s
**Persistence note:** The sub-agent completed its full grounding analysis but the harness truncated its final file-write, and session resume was gated ("reserved"). This report is persisted by the S1 orchestrator as a faithful transcription of the council's completed streamed analysis. Every finding below is the council's own stated conclusion, verbatim or lightly condensed; nothing was added.

## A1 — Grounding + Truthfulness + Cross-Service
Every concrete prompt claim grounds to a per-task Universe_Split record:
- Tanya Mitchell (tenant) — present across contacts + airtable + hubspot.
- Brooke Phillips — brooke.phillips@starpm.com, Apartment Property Supervisor; HubSpot owner of the ESA tickets; plausible supervisor of the Onsite PM; conducts owner reviews. Grounds "draft me an email to Brooke ... her owner review".
- Owner sign-off / ready-to-file belief — GROUNDED: airtable rec922b9a2d1b9451 (EVF-2026-014, "Owner Approved - Ready to File", owner authorization Linda Castillo, 2026-06-30). Lisa's belief is anchored in a real record, not fabricated.
- Possession-HOLD — airtable recc83c05d889b354, confirmed the NEWEST make-ready row for Unit 14 (modified 2026-07-01 11:18:57); notes: make-ready cannot begin until the legal process concludes and possession is formally returned.
- Stale payment-plan — airtable rec769c9f03f0b85f ("payment plan agreement ... tenancy continues"; drifting label "Las Palmas 4B"; last modified June, never updated -> stale).
- Breach + 3-day — airtable rec8005502043b755 ("Payment Plan Breached") + rec91517a5acab558 ("3-Day Notice") + Slack C003 breach/eviction thread (ts ...1782673930 "the tracking ticket is open in Airtable").
- Near-miss Unit 14 — airtable rec94e86a3007dd5e "Rio Bend Unit 14" (already rent-ready, unrelated) vs reca8230a8fd9ff51 "Sunset Ridge Unit 14" (Tanya); plus a Tommy Reyes "Unit 14" renewal in HubSpot (additional near-miss).
- make-ready channel — Slack C004 #make-ready; grounds the status-post ask.
- account/ledger — Tanya present in QuickBooks entities.
Zero ungrounded prompt claims.

## A2 — Convention
Plain persona prose, mid-thought entry, 312 words (<=500), zero em/en dashes (only hyphens in compounds: make-ready, go-ahead, re-rent). No tool/MCP names; "email", "make-ready channel", "Google Calendar" are natural surfaces ("Google Calendar" is a product name, not an MCP tool identifier, acceptable). No internal IDs. No pre-solving (the prompt asserts Lisa's mistaken belief, never the true state). No convention drift vs Prompt_Format.md or the V4 voice samples.

## A3 — Narrative State Consistency
Lisa's state-implying phrases ("we finally got the go-ahead", "the nonpayment side is cleared and the filing is squared away", "past the holdup", "ready to re-rent") voice her MISTAKEN belief. Acceptable because BOTH exist in-universe: the grounding record (owner-approved/ready-to-file, 2026-06-30) AND the correcting records (possession-hold 2026-07-01; breach/eviction; approved ESA on record). The agent can discover the correction. No unsupported false state.

## A4 — Action-vs-Universe-Prescription — ACCEPTED
The prompt asks Lisa's believed actions (move the turn forward, post status, draft to Brooke, reminder, update ticket) while the newest record prescribes HOLD. The diligence hooks ("confirm where it genuinely stands today before you touch anything", "keep your update tight and true to the actual state", "move it forward only as far as the facts support", "I do not want it marked further along than it really is") subordinate the belief to ground truth. HOLD is therefore the UNIQUE correct end-state; "schedule/advance anyway" is a discoverable trap, not a co-valid end-state. Not an unflagged ACTION_DIVERGENCE.
Authority: Onsite PM Lisa has standing to update the make-ready record (her domain), post to the make-ready channel, draft (not send) an email to her supervisor Brooke, and set her own reminder. No AUTHORITY_GAP.

## A6 — Persona Scope
"my open list", "her account", "the ticket we have open" — Tanya's unit/account/ticket are within Lisa's assignment scope (PersonaBrief: leads fair_housing_reasonable_accommodation, drives one make-ready end-to-end; the Slack forward puts the accommodation on her desk). No SCOPE_DRIFT.

## A7 — Clarity & Specificity
One ambiguity: line-9 "the ticket we have open on it" (candidate targets: Airtable eviction ticket EVF-2026-014 / Linear mirror OPS-32/38/54 / the literally-OPEN HubSpot ESA ticket). Judged NOT MAJOR: the semantic write outcome is identical (update tracking to reflect the true hold/eviction state), "on it" anchors to Unit 14, Slack C003 explicitly says "the tracking ticket is open in Airtable", and the staleness framing points to the actively-worked eviction/turn ticket (the ESA ticket was updated in July, not stale). Recorded as a downstream watch item for S2/S3. No MAJOR clarity gap; no second reading flips a write action.

## A10 — Business Function
assigned=Property Operations, prompt_primary=Property Operations (make-ready turn + tenant account + team coordination), match=true.

## A11 — End-to-End Solvability
Every step of the Hardness_Plan trajectory has materialized source data in Universe_Split (Tanya's unit+account; HOLD record; stale-plan+breach chain; ESA ticket + Gmail approval thread; Unit-14 disambiguation; the 5 write surfaces incl. C004 + Google Calendar + Linear mirror). No SOLVABILITY_BREAK.

## NOTES / PROPAGATE (downstream, not S1-blocking)
- PROPAGATE TO S3: the ESA has three HubSpot tickets (NEW b9ad..., OPEN 8faab..., CLOSED 34cb... "interactive process completed in full") plus a Gmail "APPROVED, effective immediately" thread. Frame the S3 rubric as "approved reasonable-accommodation on record" rather than "open ESA ticket". The fair-housing lever survives either way. The PROMPT makes no ESA claim, so this does NOT block S1.
- PROPAGATE TO S2/S3: pin the line-9 ticket-update target to the eviction/turn tracking ticket; treat the ESA ticket as flag-only.
- Universe quirk (not a prompt defect): the HOLD record's status field is selSched (scheduled) while its notes say hold; this strengthens the lever (the agent must read the notes, not the status field). Minor delinquency date artifact (notice served late June vs rent-due May 1) noted for S2/S3 awareness.

VERDICT: GO
