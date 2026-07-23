# Council B — S1 Adversarial QC Report R3 (S1.5 revision pass)
# Task: 39_6a602c895d0b0ab6551a3a86 · Universe: StarPM V4

Context: R2 GO'd on prior prompt version. Platform linter blocked on cross-persona-scope violation (Jaime QC Inspector asked to write to HubSpot deals). L6 removed; density-recovery elevations added in-scope (Bennett per-ticket verify, Airtable pre-read discipline, Sandra tag on Slack). Net density delta -1.5 → new projected midpoint ~59.

## Five Lens Overview

- **Architect:** Structure unchanged. Six writes across six Jaime-owned services (Airtable, Linear x3, Slack, Gmail, GCalendar) plus 4 discovery / lookup surfaces. Persona-scope boundary cleanly respected — no CRM/HubSpot writes anywhere. Cohesion tight.
- **Implementer:** Every ask maps to a real StarPM tool. Slack `slack_send_message(channel_id, message)` for the #make-ready post. Sandra tag requires `contacts.contacts` lookup for user_id resolution. Gmail `create_draft(to[], body=...)` for the Carlos hand-off. Linear `save_comment` + `save_issue` for per-ticket closures. Airtable append via `airtable_update_records` on the Make-Ready record. GCalendar `create_event`. All runnable.
- **Red-team:** Attempted three alt-path breaks (see B2). None flip a required write action.
- **Ground-truth:** Every referenced entity (Las Vistas 3C, 6/18 QC pass, three punch items, Bennett notes on OPS-224/225/226, Brooke supervisory note, Carlos onsite PM, Sandra Allen leasing coord, Denise/Brooke gate on showings) is grounded in per-task Universe_Split. No base-universe assumptions.
- **Integration:** Prompt is now internally coherent. Hardness_Plan.md has stale L6 references + injected R10/R11 HubSpot deals; both must be reconciled downstream (see B6). Not blocking for prompt correctness.

## B1 — QC Sub-Dim Scoring

Per sub-dim scheme map (Council_Protocol.md):

1. **Coherence (Bolt-on)** [1/5 binary] → **5/5** — Remove-sentence tests:
   - Line 9 "Leasing has been waiting on 3C to open showings, so they'll want the heads-up from us before they can move on their end." — REMOVING this sentence weakens the motivation for lines 11 (Carlos email cc Brooke) + 13 (Slack post + Sandra tag). Both downstream asks EXPLICITLY reference leasing activation; line 9 is the shared premise, not a bolt-on. PASS.
   - Line 13 "tag Sandra so leasing sees it and can pick it up on their end" — REMOVING the Sandra clause still leaves the #make-ready post but severs the cross-team pickup signal. Sandra tag is load-bearing for the leasing hand-off, not decorative. PASS.
2. **Coherence (Command List)** [1/5 binary] → **5/5** — Narrative paragraphs with rationale ("that kind of surface tends to get lived-back-in fast"). No bulleted drop.
3. **Truthfulness / Groundedness** [1/3/5] → **5/5** — QC pass on 18th, Brooke follow-up, three punch items (baseboard, appliance interiors, towel ring), Bennett rework-complete notes all trace to Universe_Split R7 (Brooke 6/18 Slack ping) + R2/R3/R4 (Bennett Linear comments) + Airtable rec291f423370e2a2db narrative.
4. **Alignment with Today's Date** [1/3/5] → **5/5** — 6/18 pass → 7/01 today (~13 days). Brooke's follow-up chase makes today's closeout believable. Friday spot-check reminder = 7/03; showings window "between now and next Wednesday" = 7/01 → 7/08. All grounded.
5. **Unique Ground Truth** [1/3/5] → **5/5** — "Formal side" unpacked verbatim by paragraphs 3-8. Two-reading test in B2 confirms no divergent write path.
6. **Feasibility / Achievability** [1/3/5] → **5/5** — Every ask maps to Jaime-accessible StarPM tools. No HubSpot writes; every remaining service is within the QC Inspector's documented systems.
7. **Explicit Tool Mention** [1/5 binary] → **5/5** — No tool / service / API names in prose. "#make-ready channel" is a channel-name reference, not a tool name.
8. **Contrived / Unnatural** [1/3/5] → **5/5** — Voice reads as a QC lead circling back on a paperwork closeout after Brooke's chase. Terse, observation-first, methodical. Matches Jaime's voice profile (formality 0.55, verbosity 0.30).
9. **Tool Use & Cross-Service** [1/5 binary] → **5/5** — Touches 6 services: Airtable (make-ready record) + Linear (3 tickets) + Contacts (Carlos/Brooke/Sandra lookups) + Slack (#make-ready post) + Gmail (Carlos draft cc Brooke) + GCalendar (Friday reminder). Above the 5+ bar.
10. **Investigation + Action** [1/5 binary] → **5/5** — Investigation: Bennett per-ticket note verification, Airtable notes pre-read, calendar range check for booked showings. Action: 3 Linear comments + 3 state flips, Airtable append, Gmail draft, Slack post, GCalendar reminder = 10 write actions.
11. **Persona / Scope Fit** [1/3/5] → **5/5** — HONEST RESCORE post-linter block. Every ask in the REVISED prompt maps to Jaime's documented systems: Airtable Make-Ready (QC signoff), Linear tickets (rework closure), Slack #make-ready (crew channel), Gmail to Carlos + Brooke cc (peer hand-off), GCalendar (self-reminder), Contacts (recipient resolution). ZERO writes to HubSpot, QuickBooks, or any system outside the QC Inspector scope. The R2 5/5 was wrong on this dim (HubSpot ask was cross-scope). This time the score is defensible.
12. **Business Function Match** [3/5 scheme] → **5/5** — BF3 Quality Control & Field Services. Post-inspection signoff, punch-item closure, Airtable make-ready state, cross-team pickup notice. Squarely BF3 — no drift into BF2 (owner relations) or BF5 (leasing).
13. **Length + Em-dash + At-least-N compliance** → **5/5** — 15 lines, ~290 words (well under 500), zero em-dashes, zero unmandated "at least N".

All applicable sub-dims: **5/5**.

## B2 — Adversarial Alt-Path

Three alt-path attacks attempted:

**(a) "tag Sandra" → post to #leasing instead of #make-ready + Sandra tag?**
Line 13 opens "Post in the #make-ready channel..." — channel is explicitly named FIRST, before the Sandra clause. Reading "and tag Sandra so leasing sees it" as "post to #leasing" reverses the sentence order and ignores an explicit channel name. Not a defensible alt-reading. **NO DIVERGENCE.**

**(b) "read what's already sitting in the notes so my sign-off reads as a continuation" → edit-in-place vs append?**
Line 7 continues: "**not a replacement**. Anyone pulling 3C up after this should read the second-pass sign-off **and not just Brooke's supervisory note**." Two explicit anti-replacement guards. Append is the only defensible reading. **NO DIVERGENCE.**

**(c) "Leasing has been waiting on 3C" → does the agent still write to HubSpot despite the removed ask?**
This is the ONLY nontrivial risk. Line 9's leasing-activation premise + universe R9 Gmail thread ("Denise is asking whether leasing can activate showings") could tempt an agent to update the CRM deal defensively. However:
- Lines 11-13 EXPLICITLY enumerate the leasing-notification mechanism: Carlos email + Slack post to #make-ready + Sandra tag. No CRM/HubSpot ask.
- An agent that additionally updates HubSpot is doing extra work, not flipping a required write. Rubric set (once updated) will not test HubSpot; extra-work is not a rubric fail.
- If R10/R11 deals are hit accidentally, worst case is the agent picks 9D instead of 3C (L6 trap fires as noise). Neither outcome is prompt-driven, so this is a rubric-neutral density noise contribution.
**NO DIVERGENCE** in the prompt-required write set. The HubSpot deal removal is CLEAN.

Verdict: no adversarial divergence found. PASS.

## B3 — Tool-Call Density Projection

Sketch the Opus-4.8 trajectory. Two scenarios:

| Component | Low-effort | High-effort | Midpoint |
|---|---|---|---|
| Base discovery (universe today, Carlos/Brooke/Sandra contact lookups, thread/channel resolves) | 6 | 10 | 8 |
| L1 Latching (Airtable Make-Ready read + Linear ticket list + re-read to confirm state) | 5 | 8 | 6.5 |
| L8 Multi-link chain (3 OPS closures: verify Bennett note per ticket via linear_get_comments/read + save_comment + save_issue state flip) | 9 | 12 | 10.5 |
| **Bennett per-ticket verify ELEVATION (NEW, was implicit in R2)** | +2 | +4 | +3 |
| L9 Parameter-shape retries (Slack message vs payload; Gmail body vs content; Airtable camelCase; Linear teamId trap) | 2 | 4 | 3 |
| L25 Existing-output anchor (extra Airtable re-reads confirming Ready state before the append) | 4 | 6 | 5 |
| L26 Decoy parent thread (Slack #make-ready history + Gmail thread search + disambiguation between 6/16 FAIL and 6/18 CLOSEOUT) | 4 | 6 | 5 |
| **Airtable pre-read ELEVATION (NEW)** — read fldNotes2 before update to preserve Brooke's supervisory line | 1 | 2 | 1.5 |
| **Sandra contact lookup (NEW)** — contacts resolve for @-tag user_id | 1 | 2 | 1.5 |
| Write actions (Airtable append + 3x Linear save_comment + 3x Linear save_issue + Slack post + Gmail draft + GCalendar create_event) | 10 | 10 | 10 |
| Cross-service triangulation buffer | 3 | 6 | 4.5 |
| **TOTAL projected** | **47** | **70** | **~58.5** |

**Classification: PASS.** Midpoint 58.5 clears the 50+ design target. No THIN_DENSITY acceptance needed.

L31 realization rate application:
- Opus 74% × 58.5 = **43.3** expected avg (clears 40 floor).
- Gemini 70% × 58.5 = **41.0** expected avg (clears 40 floor by narrow margin).

**Margin note:** Gemini expected avg 41.0 is only +1.0 above the 40 floor. If real-world Gemini realization runs a few points below the L31 baseline (as observed in the failed REDO — Gemini realized ~35 against a 50 midpoint projection = 70% is optimistic), Gemini could underflow. NOT a blocker at this phase (midpoint math is sound), but flag for S4 attention: if S4 Gemini avg lands 38-40, the failure is density-margin, not lever design.

## B4 — Hardness Preservation

Surviving 5 levers:

- **L1 (Latching — Airtable selReady anchor):** PRESERVED. Line 7 "Pull the make-ready record on 3C and get my second-pass sign-off written into it" forces the Airtable read where `fldTurnStatus=selReady` is the trap. Line 5 also forces Airtable-adjacent reads.
- **L8 (Multi-link chain — 3 Linear closures across services):** PRESERVED and STRENGTHENED by the Bennett verify elevation. Line 5: "Pull his note off each ticket and make sure the item he's writing up actually matches what the ticket is about before I sign off. Then get each ticket moved through my sign and out of my queue with the pass called out for each item, not a blanket close." Three per-item comments + three state flips + per-ticket read verification.
- **L9 (Universe-grounded gotcha — StarPM param traps):** PRESERVED. Slack post, Gmail draft, Linear save_comment, Airtable camelCase all exercised. Sandra contact tag ADDS a contacts.contacts call which uses standard param shape (no trap there, but the Slack tag mechanism requires user_id resolution which is a param-shape moment).
- **L25 (Existing-output anchor trap):** PRESERVED and STRENGTHENED by the Airtable pre-read elevation. Line 7: "Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement. Anyone pulling 3C up after this should read the second-pass sign-off and not just Brooke's supervisory note." Explicit anti-no-op instruction; explicit append-vs-replace instruction.
- **L26 (Decoy parent thread — Slack 6/16 FAIL vs 6/18 CLOSEOUT):** PRESERVED. Line 13 requires Slack post; agent must disambiguate the 6/16 FAIL parent (R5) from Brooke's 6/18 closeout ping (R7). Gmail parallel: line 11 Carlos email must land as a NEW thread or on R9 canonical, not on R8 fail thread.

**L6 intentionally removed** — per user instruction, not flagged as regression.

**New soft levers (density-recovery, in-scope):**

- **Bennett per-ticket verify** (elevated): "Pull his note off each ticket and make sure the item he's writing up actually matches what the ticket is about before I sign off." — semantically visible. Forces `linear_search_issue_comments` or `linear_get_comments` per ticket. Language is explicit, not implicit.
- **Airtable pre-read discipline** (elevated): "Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement." — semantically visible. Forces a pre-write Airtable read. Language is explicit.
- **Sandra contact lookup** (added): "tag Sandra so leasing sees it and can pick it up on their end" — semantically visible for a Slack @-tag mechanism (user_id resolution requires contacts lookup). Slightly weaker than the other two — an agent might use a plaintext "@Sandra" string without resolving to user_id, but StarPM Slack tagging convention expects user_id via mentions payload, which forces the lookup. Acceptable.

Hardness surface: **5 preserved + 3 soft-lever elevations, all agent-visible.** PASS.

## B6 — Upstream Propagation

Two upstream artifacts are now stale relative to the revised prompt. Neither blocks the prompt itself; both must be reconciled downstream before S2/S3.

**PROPAGATE TO HARDNESS: `_aux/Hardness_Plan.md` still lists L6 as a selected lever + carries R10/R11 HubSpot injection specs — recommended upstream fix: (a) demote L6 to "Considered / withdrawn — cross-persona-scope violation per platform linter"; (b) mark R10/R11 in the Injection Plan section as "ABANDONED decoys — already injected but no longer prompt-referenced; leave in universe as passive noise"; (c) update the density table to reflect the ~58.5 midpoint post-revision; (d) update the Stump Hypothesis to remove prediction #5 (HubSpot 9D-vs-3C selection).**

**Assessment: NON-BLOCKING for prompt phase.** The prompt is correct on its own; Hardness_Plan staleness affects S2/S3 authorship (they must not carry HubSpot rubrics forward from any prior draft), not prompt correctness. Flag as coordination note for S2 kickoff.

**Injected R10/R11 HubSpot deals — status assessment:**
- Both deals are already INSERTed on the platform per the R2 injection cycle.
- Prompt no longer references leasing pipeline deal activation.
- Rubric set MUST NOT include a HubSpot deal update criterion (would fail agents who correctly followed the revised prompt).
- OE chain MUST NOT include HubSpot deal search/update steps.
- Universe impact: extra noise — an exploration-heavy agent may still `manage_crm_objects(search)` on "Las Vistas" and surface both deals. This is DENSITY-POSITIVE and rubric-neutral, so acceptable.
- **Verdict: ACCEPTABLE noise. No universe cleanup required.** The decoys sit passively.

No other upstream propagation flags.

## VERDICT

**GO (S1.5 R3).**

- Every applicable QC sub-dim ≥ 5.
- No adversarial divergence found. HubSpot removal is clean (no second reading forces a HubSpot write).
- Projected midpoint 58.5 ≥ 50 design target. Gemini expected avg 41.0 clears floor with narrow margin — flag for S4 attention if Gemini underflows.
- All 5 surviving hardness levers still triggered; 3 soft-lever density-recovery elevations are semantically visible to the agent.
- Hardness_Plan.md stale-doc reconciliation flagged for S2 kickoff (non-blocking for prompt phase). R10/R11 injected deals accepted as passive universe noise (density-positive, rubric-neutral once S3 confirms no HubSpot rubrics).

Prompt phase is clear to proceed to S2. S2 kickoff MUST update Hardness_Plan.md and confirm no HubSpot OE steps carry forward.
