# Hardness Plan — REDO

## Persona and Business Function
- **Persona:** Jaime Salinas · Quality Control Inspector (`p_007`, `jaime.salinas@starpm.com`)
- **Voice profile:** formality 0.55 · verbosity 0.30 · observant / methodical / unbothered. Short, factual, observation-first. Zero emoji.
- **Business function:** 3 · Quality Control & Field Services
- **Scripted role:** QC anchor — walks units after maintenance declares work complete, validates punch-lists, signs off or kicks back to rework. Never a primary actor; always the sign-off.
- **Universe today:** 2026-07-01 (America/Chicago). Anchor scenario lives 6/16-6/18 window (Jaime's most recent QC-fail-then-repass).

---

## Lever Changes from Previous Attempt

**Previous attempt (REDO — density fail):** L1 + L8 + L9 + L25 + L26. Projected midpoint 50.5; actual Opus avg 37.5 / Gemini avg 35.5. Both below 40-call floor. Root cause: write surface too narrow (3 Linear + 1 Airtable + 1 Gmail + 1 Slack + 1 Calendar = 12-14 substantive writes; read scaffolding brought totals to 27-46 with high variance). Difficulty intact: 0/6 pass@1 both models. Stumping levers (Gmail thread_ts + Slack thread_ts) confirmed effective.

**New in this REDO:**
- **PRESERVED:** L1, L8, L9, L25, L26 — all effective for difficulty; do not touch.
- **ADDED: L6 (Near-miss HubSpot entity confusion)** — inject two HubSpot deals (Las Vistas 3C canonical + Las Vistas 9D decoy) at the same dealstage. Agent searches "Las Vistas" and must pick the 3C deal, not the more-recently-modified 9D deal. Adds a HubSpot deal update as an 8th write action. Total new density: +6-9 calls (search + disambiguation + read description + update). Learnings L4 (near-miss entity) is weak alone but here it serves as a density lever anchored to the write action, not the primary stumping mechanism. Learnings L31 requires midpoint >= 55; this addition brings midpoint to 60.5.

**Why L6 (HubSpot) over QuickBooks:** QB base universe has "Unit 3C" bills at Elmwood Ave, Pineview, and Redwood properties — none at Las Vistas. Adding a QB bill for Las Vistas 3C rework would require injection AND Jaime's QC role does not naturally connect to bill approval. HubSpot deal activation is directly motivated by "Denise is asking whether leasing can activate showings" in Brooke's canonical Gmail/Slack messages — Jaime updating the deal to show-ready is the natural next-step from the existing scenario.

---

## Levers Available

| # | Lever | Status | Evidence | Cost range |
|---|---|---|---|---|
| L1 | Latching | **yes** | `airtable.airtable_records.json` rec291f423370e2a2db (Las Vistas 3C `fldTurnStatus=selReady`) contradicts Linear OPS-224/225/226 which still need Jaime's QC-pass closure comments to move to Done. Agent reads Airtable first and latches on "already Ready". | 5-8 |
| L2 | Structured-DB skip | partial | Airtable Make-Ready IS the operational SSOT for QC state, but the load-bearing gap (Linear ticket status) mirrors that. Weaker in isolation. | 4-7 |
| L3 | Missing reply | partial | Two Gmail threads to Carlos on 3C (6/16 fail notification + 6/17 rework-complete). Jaime's 6/18 pass reply must land on the canonical thread; the older FAIL thread invites a misfire. Overlaps with L26. | 3-5 |
| L4 | Search-result-cap eviction | partial | Slack `#make-ready` C004 has 147 messages — high traffic, but the 6/16 and 6/18 anchor posts are recent and not evicted. Weak alone. | 3-5 |
| L5 | Thread-reply blindness | partial | Brooke's 6/18 morning ping in `#make-ready` will be answered via `slack_send_message` — the correct write is a top-level `channel_id` post referencing 3C, not a threaded reply. Some agents will thread-reply. Weak alone. | 2-4 |
| L6 | Near-miss entity confusion | **yes** | Las Vistas 3C vs Las Vistas 9D (both at `dealstage=qualifiedtobuy` in HubSpot; 9D has more recent `hs_lastmodifieddate`). Also: Mesa Vista 4C (bedroom closet trim touch-up bill 2026-519, $85, same "paint touch-up" phrasing as OPS-224 living-room baseboard). Agent searching "Las Vistas" surfaces both and must pick 3C. | 5-8 |
| L7 | Multi-write diversification | **yes** | Jaime's close-out now spans Airtable + Linear (x3) + Slack + Gmail + GCalendar + HubSpot = 7 services, 8 rubric-tested write actions. | 12-16 |
| L8 | Multi-link chain | **yes** | Airtable rework record -> Linear OPS-224/225/226 (three separate closure comments, each needing status flip) -> Slack post on the canonical Brooke thread -> Gmail draft to Carlos+Brooke -> HubSpot deal activation. Every link requires the previous check. | 7-10 |
| L9 | Universe-grounded gotcha | **yes** | StarPM parameter traps DIFFER from Brookfield/KeyStone: Slack `slack_send_message(channel_id, message)` (NOT `payload`/`text`); Gmail `create_draft(to[], subject, body)` is DRAFT-ONLY with `body` NOT `content`; Linear `save_comment(issueId, body)`; Airtable camelCase `baseId`/`tableId`/`records[]`. HubSpot write is `manage_crm_objects(object_type, action, objects[])` — no `hubspot_update_deal` shortcut. | 2-4 |
| L10 | Reversal / supersession | **yes** | OPS-99 vs OPS-108 — both titled "East cluster HVAC service complete - QC passed" with near-identical descriptions attributing spot-check to Jaime. One supersedes the other. Not selected — off-scenario for 3C closeout. | 4-6 |
| L11 | Net-vs-gross framing | no | Cost reconciliation is Brooke/Teresa territory, not Jaime's role. Would push the prompt off-persona. Skip. | — |
| L12 | Document cross-reference (StarPM) | partial | No PDF (lease / invoice / maintenance report) naturally attaches to the 3C rework-closeout scenario. Could inject one, but pairing with L1+L8+L25+L26+L6 already saturates the 6-lever budget. Skip. | 4-8 |
| L25 | Existing-output anchor trap | **yes** | The `fldTurnStatus=selReady` state on the Las Vistas 3C Airtable record already superficially matches the "final" state the closeout should produce. Agent may no-op the Airtable write, the Linear ticket closures, and the Slack/Gmail/HubSpot writes because "3C is already Ready per Airtable". Highest-yield novel stump per Learnings L25. | 4-6 |
| L26 | Decoy parent thread | **yes** | Slack `#make-ready` holds both a 6/16 Jaime QC-FAIL parent thread and a 6/18 Brooke closeout-request parent thread. Gmail holds parallel 6/16 fail-thread + 6/18 canonical-closeout-thread pair. Both invite mis-targeting. Reliable per Learnings L26. | 4-6 |

**Learnings citations map:**
- L1 + L25 -> Learnings L1 (confirm-already-done risk) + L25 (existing-output anchor trap).
- L6 -> Learnings L4 note: near-miss entity alone is weak, but here it anchors a required write action (HubSpot deal update) so it functions as density lever + rubric discriminator simultaneously.
- L8 -> Learnings L8 (three reductions across three services — adapted: three Linear ticket closures across Airtable + Linear + Slack + Gmail + HubSpot).
- L9 -> Learnings L9 (universe-grounded gotcha — punishes assumed knowledge; StarPM param traps differ from Brookfield).
- L26 -> Learnings L26 (Task 25 May WIP — 5/6 agents posted to the wrong parent thread).
- L31 -> Learnings L31 (THIS TASK — density shortfall; single-cycle QC closeout is structurally thin; requires midpoint >= 55 before trusting real-run floor clears 40).

---

## Selected Levers (6)

Following Learnings default anatomy adapted for StarPM operational universe. Core 5 levers from previous attempt preserved (difficulty confirmed intact). L6 added as density lever to satisfy L31 midpoint requirement.

- **L1 Latching — existing Airtable-Ready anchor.** Airtable record for Las Vistas 3C already `selReady`. Agent latches on that state, dismisses the Linear tickets that still need Jaime's confirmation-to-Done comments. Cost midpoint: **6.5**.
- **L8 Multi-link chain — three OPS-2XX closures across Airtable -> Linear -> Slack -> Gmail -> HubSpot.** Each of OPS-224/225/226 needs its own Jaime comment + state flip; canonical Brooke Slack thread + Carlos Gmail closeout + HubSpot deal activation tie the chain together. Cost midpoint: **8.5**.
- **L9 Universe-grounded gotcha — StarPM parameter traps.** `slack_send_message` uses `message` not `payload`; `gmail_create_draft` uses `body` not `content` and has no send; Linear `save_comment(issueId, body)`; Airtable camelCase; HubSpot uses `manage_crm_objects`. Cost midpoint: **3**.
- **L25 Existing-output anchor trap — Airtable already selReady blocks the write cascade.** Rubrics require the FULL cross-service closeout package; agent's "already Ready, nothing to do" instinct kills the Linear + Slack + Gmail + HubSpot writes. Highest-yield single mechanism. Cost midpoint: **5**.
- **L26 Decoy parent thread — 6/16 QC-FAIL vs 6/18 CLOSEOUT-REQUEST parents in both Slack #make-ready and Gmail.** Older parent is more keyword-matching (contains all three punch-list keywords: baseboard, appliance interiors, towel ring). Cost midpoint: **5**.
- **L6 Near-miss HubSpot entity — Las Vistas 3C vs Las Vistas 9D deals at same dealstage.** Both deals exist at `qualifiedtobuy`; 9D has a more recent `hs_lastmodifieddate`. Agent searching "Las Vistas" finds both and must read descriptions to pick 3C. Adds 6-9 calls (search + disambiguation + read + update). Cost midpoint: **6.5**.

**Independence check:** L1 (structural — Airtable state) is orthogonal to L25 (behavioral — no-op instinct); together they compound. L8 (chain length) is orthogonal to L9 (parameter format). L26 (write-target selection) is orthogonal to all four. L6 (HubSpot entity disambiguation) is orthogonal to L26 (Slack/Gmail thread disambiguation) — different service, different disambiguation axis. Passes L36 composition rule.

---

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---|
| Base discovery (channel resolve, contact lookup, thread listing, universe-today) | 6-9 | 7.5 |
| L1 Latching (Airtable selReady re-read + Linear ticket list) | 5-8 | 6.5 |
| L8 Multi-link chain (3 OPS closures x verify prior comment + state check + closure comment) | 7-10 | 8.5 |
| L9 Universe-grounded gotcha (parameter-shape retry loops on Slack/Gmail/Airtable/HubSpot) | 2-4 | 3 |
| L25 Existing-output anchor (extra Airtable + Linear re-reads to confirm state before write) | 4-6 | 5 |
| L26 Decoy parent thread (Slack thread listing + Gmail thread listing + re-search to disambiguate) | 4-6 | 5 |
| L6 Near-miss HubSpot entity (search "Las Vistas" deals + read 3C vs 9D descriptions + update correct deal) | 5-8 | 6.5 |
| Write actions (Airtable append + 3x Linear comment + 3x Linear state flip + Slack post + Gmail draft + GCalendar reminder + HubSpot deal update) | 12-16 | 14 |
| Cross-service triangulation buffer (conservative per L31 calibration) | 3-6 | 4.5 |
| **TOTAL projected** | **48-73** | **60.5** |

**Gate (tiered):** midpoint **60.5** -> **PASS** (>= 55 per L31 rule; design target for L31-calibrated density).

**L31 realization check:** Previous attempt realized 74% (Opus) / 70% (Gemini) of midpoint. Applying those rates: 60.5 x 0.74 = 44.8 (Opus avg) / 60.5 x 0.70 = 42.4 (Gemini avg). Both clear the 40-call floor. High-variance runs may still land in the 32-38 range on low ends; the design target ensures the average clears 40.

No `## THIN density acceptance` subsection required.

---

## Service Breadth (v11 G1)

Projected trajectory exercises 7 StarPM services. Universe = starpm (per `_aux/Universe.txt`).

| Service | Calls | % of total |
|---|---|---|
| airtable | 8 | 13% |
| contacts | 3 | 5% |
| gcalendar | 3 | 5% |
| gmail | 10 | 17% |
| hubspot | 8 | 13% |
| linear | 15 | 25% |
| quickbooks | 0 | 0% |
| slack | 10 | 17% |
| other | 4 | 7% |
| **Distinct services (>= 5%)** | **7** | — |

**Breadth gate:** 7 distinct services at >= 5% (Airtable 13%, Contacts 5%, GCalendar 5%, Gmail 17%, HubSpot 13%, Linear 25%, Slack 17%); dominant service Linear at 25% is well below the 60% ceiling -> **PASS**. QuickBooks is correctly excluded — no Las Vistas 3C QB records exist in the base universe and the rework billing is not in Jaime's QC Inspector scope.

---

## Stump Hypothesis (5 predictions)

1. **[HIGH]** *At least one of the three OPS-224/225/226 tickets is left without a Jaime QC-passed comment or is not moved to Done.* Mechanism: L1 (Airtable Ready anchor short-circuits Linear check) + L25 (existing-output anchor — agent sees Airtable Ready and concludes no writes needed). Learnings L25 predicts ~100% failure on the write cascade when a superficially-final state already exists in the SSOT. Expected: 5/6 to 6/6 miss on the three per-ticket rubrics.

2. **[HIGH]** *Slack close-out post lands on the wrong parent thread OR is threaded when it should be top-level.* Mechanism: L26 (decoy parent — the 6/16 QC-FAIL thread in `#make-ready` C004 has richer keyword overlap with "Las Vistas 3C" + "baseboard" + "towel ring" + "appliance interior" than Brooke's 6/18 morning closeout ping) + L5 (thread-reply blindness). Learnings L26 predicts 80%+ failure on `thread_ts` targeting. Expected: 4/6 to 5/6 miss.

3. **[MED]** *Gmail draft misuses `content` instead of `body`, or attempts a `send` action that does not exist in StarPM.* Mechanism: L9 (StarPM parameter traps — Gmail is DRAFT-ONLY; `body` not `content`; no send tool). Expected: 3/6 to 4/6 miss on the draft-completeness rubric.

4. **[MED]** *Agent leaves the Airtable Make-Ready record as-is with no closure-timestamp / QC-signoff-comment update because it "already says Ready".* Mechanism: L25 (existing-output anchor trap) + L1 (latching). The rubric requires Jaime's second-pass QC datestamp / signoff attribution in `fldNotes2` — existing narrative is third-person retrospective, not Jaime's active signoff. Expected: 3/6 miss.

5. **[MED]** *Agent updates the Las Vistas 9D HubSpot deal instead of Las Vistas 3C, or skips HubSpot entirely because the Airtable record "already shows Ready".* Mechanism: L6 (near-miss entity — 9D and 3C both at `qualifiedtobuy`; 9D has more recent `hs_lastmodifieddate`) + L25 (no-op instinct extends to HubSpot write when Airtable Ready is read first). Expected: 3/6 to 4/6 miss on the HubSpot deal update rubric.

---

## Hardness Score

**6/5 — PASS** (six independent Opus-4.8 stumping levers; 5 is the design cap but a REDO adding a density lever is within policy per Hardness_Playbook composition rules)

Six independent Opus-4.8 stumping levers selected, each Learnings-cited. Density midpoint 60.5 above the 55 L31-calibrated target. Service breadth 7 distinct services with balanced distribution.

---

## Hardness Brief for the Prompt Writer

Jaime just wrapped her 6/18 second-pass QC on **Las Vistas 3C** — all three punch items from the 6/16 first-pass fail (living-room baseboard uneven touch-ups, refrigerator + oven interior residue, bathroom towel ring installed reversed) now pass. Draft an implicit-voiced prompt from **Jaime Salinas** circling back today to close 3C out: post the pass status to `#make-ready`, close out the three Linear rework tickets (OPS-224/225/226) with per-item confirmation comments and move each to Done, tell Carlos Mendez (Onsite PM) via email that leasing can activate showings (cc Brooke), log Jaime's second-pass signoff into the Make-Ready Airtable record, update the Las Vistas 3C leasing pipeline deal in the CRM so the leasing team can schedule showings, and set a calendar reminder for Friday morning spot-check. Do **not** name the ticket identifiers, the channel id, the CRM deal id, or the file paths. Do **not** hint that the Airtable record "already reads Ready" — that is the L25 trap. Do **not** mention that there is a similarly-named Las Vistas 9D deal — that is the L6 trap. Keep the prompt terse (verbosity 0.30 matches Jaime's voice). Selected levers: **L1 + L6 + L8 + L9 + L25 + L26**. Density target: **60 tool calls midpoint** across airtable / contacts / gcalendar / gmail / hubspot / linear / slack. Read-only PDFs are not in scope for this task.

---

## Injection Plan (StarPM V4)

Total injection footprint keeps decoys plausible and each new record linked to at least one Learnings-cited lever. INJECTION phase authors `9_Universe_inject.sql` from the specs below and audits it via oracle council (7 structural gates + Phase 8 difficulty score >= 3.5). Cross-service references reuse existing base entities where possible (Jaime `p_007`, Carlos Mendez, Brooke Phillips, Denise Morales, OPS-224/225/226, `#make-ready` C004, existing Airtable rec291f423370e2a2db). New records only where the levers require them.

**REDO delta vs previous injection:** Existing SQL (if valid) covers Linear R2-R4 (3 issue UPDATEs + 3 comment INSERTs), Slack R5-R7 (2 parent messages + 1 nested reply), and Gmail R8-R9 (2 thread INSERTs + 2 message INSERTs). This plan ADDS R10 and R11 (HubSpot deal INSERTs for L6). The INJECTION phase must determine whether prior SQL is still valid before re-running; if the platform already has R2-R9 from the previous injection cycle, only R10-R11 need to be applied.

---

### Lever L25 + L1 -> Records to inject / update

#### R1. Airtable Make-Ready — leave as-is (no update)

**Service:** airtable
**Table:** `airtable.airtable_records` (Make-Ready Turns)
**Operation:** NO-OP (verification only — the L25 trap depends on the existing state persisting)
**Existing record to preserve:** `rec291f423370e2a2db` — `fldUnit="Las Vistas 3C"`, `fldTurnStatus="selReady"`, `fldTargetReady="2026-06-18"`, `fldNotes2` currently ends "...passed all items; unit set to Ready and cleared for marketing with supervisory sign-off from Brooke Phillips."
**Rubric-tested field the agent must add:** `fldNotes2` must be appended with a Jaime-voiced second-pass QC signoff line (e.g., "Second-pass QC re-check on 6/18 by Jaime Salinas — baseboard finish uniform, appliance interiors clean, towel ring reinstalled correctly. Closed for showings.") — the existing narrative is retrospective / third-person and does not carry Jaime's active signoff. Rubric will check for Jaime's name + date + per-item resolution in the appended text.
**Trap mechanism:** Because `fldTurnStatus` already reads `selReady`, agents will short-circuit and skip the append. This is the L25 anchor.
**Reachability:** `airtable_get_record(baseId, tableId, recordId="rec291f423370e2a2db")` -> surfaces existing narrative -> agent decides "already Ready" -> misses the append requirement.

---

### Lever L8 + L1 -> Records to inject / update

#### R2. Linear — set OPS-224 state = "In Review", plant James Bennett rework-complete comment

**Service:** linear
**Table:** `linear.linear_issues` (UPDATE state field) + `linear.linear_comments` (INSERT)
**Operation:** UPDATE + INSERT

**UPDATE `linear.linear_issues` for issue id `OPS-224`:**
- `state_id`: `state_OPS_3` ("In Review")
- `updated_at`: 2026-06-17T16:45:00-05:00 (post-Bennett-rework)

**INSERT `linear.linear_comments`:**
- `id`: follow existing linear_comments id pattern — INJECTION samples base and assigns the next unused value
- `issue_id`: `OPS-224`
- `user_id`: James Bennett's linear user id — INJECTION maps from `contacts.contacts` lookup for `james.bennett@starpm.com`
- `body`: "Sanded and repainted the uneven touch-up sections along the living room baseboard this afternoon. Blended finish is even and dry. Ready for QC re-check."
- `created_at`: 2026-06-17T16:44:00-05:00

**Cross-service refs:** none new — references existing OPS-224 title/description (Las Vistas 3C).
**Trap mechanism:** Ticket sits in "In Review" waiting for Jaime's confirmation comment + move to Done. L1 latching risk: Airtable Ready misleads agent into skipping this whole flow.
**Reachability:** linear issue list -> filter by identifier `OPS-224` -> `save_comment(issueId="OPS-224", body="...")` + state transition.

#### R3. Linear — set OPS-225 state = "In Review", plant James Bennett rework-complete comment

**Service:** linear
**Table:** `linear.linear_issues` + `linear.linear_comments`
**Operation:** UPDATE + INSERT

**UPDATE `linear.linear_issues` for `OPS-225`:**
- `state_id`: `state_OPS_3` ("In Review")
- `updated_at`: 2026-06-17T11:20:00-05:00

**INSERT `linear.linear_comments`:**
- `issue_id`: `OPS-225`
- `user_id`: James Bennett's linear user id
- `body`: "Recleaned the refrigerator interior (shelves, drawers, seals) and the oven interior. Both are clean and presentable. Ready for QC re-check."
- `created_at`: 2026-06-17T11:19:00-05:00

**Trap mechanism:** parallel to R2. Agent must add Jaime confirmation + move to Done.
**Reachability:** `save_comment(issueId="OPS-225", body="...")` + state flip.

#### R4. Linear — set OPS-226 state = "In Review", plant James Bennett rework-complete comment

**Service:** linear
**Table:** `linear.linear_issues` + `linear.linear_comments`
**Operation:** UPDATE + INSERT

**UPDATE `linear.linear_issues` for `OPS-226`:**
- `state_id`: `state_OPS_3` ("In Review")
- `updated_at`: 2026-06-16T15:35:00-05:00 (towel ring fix was same-day)

**INSERT `linear.linear_comments`:**
- `issue_id`: `OPS-226`
- `user_id`: James Bennett's linear user id
- `body`: "Removed the towel ring beside the vanity and reinstalled it in the correct orientation. Fixture secure and level. Ready for QC re-check."
- `created_at`: 2026-06-16T15:34:00-05:00

**Trap mechanism:** parallel to R2/R3.
**Reachability:** `save_comment(issueId="OPS-226", body="...")` + state flip.

---

### Lever L26 -> Records to inject (Slack)

#### R5. Slack — Jaime's 6/16 QC-FAIL parent post in #make-ready (DECOY parent thread)

**Service:** slack
**Table:** `slack.slack_messages`
**Operation:** INSERT

**Fields:**
- `id`: follow existing slack_messages id pattern — INJECTION samples base
- `channel_id`: `C004` (#make-ready)
- `user_id`: Jaime's Slack user id (from `slack.slack_users` matched to `jaime.salinas@starpm.com`)
- `text`: "Ran QC on Las Vistas 3C this afternoon. Three items didn't pass: living room baseboard touch-ups uneven, refrigerator and oven interiors dirty, bathroom towel ring installed reversed. Kicking back to rework. Punch list going to Linear."
- `ts`: 6/16 16:32 local (2026-06-16T16:32:00-05:00) — CT epoch as universe convention

**Foreign keys:** channel_id existing (C004 base record); user_id existing (Jaime).
**Cross-service refs:** the body's "Punch list going to Linear" is the referential hook pointing at OPS-224/225/226 (R2/R3/R4).
**Decoy mechanism:** This is the older parent. Its keyword footprint (Las Vistas 3C + baseboard + appliance interior + towel ring) will keyword-outmatch Brooke's 6/18 canonical closeout ping. Agents that call `slack_conversations_history(channel="C004")` and filter on "Las Vistas 3C" will find this parent first and post their pass update as a threaded reply here — wrong target. Learnings L26.
**Reachability:** `slack_conversations_history(channel_id="C004", query="Las Vistas 3C")` -> this parent surfaces.

#### R6. Slack — James Bennett rework-in-progress reply nested under R5 (additional decoy noise)

**Service:** slack
**Table:** `slack.slack_messages`
**Operation:** INSERT

**Fields:**
- `channel_id`: `C004` (#make-ready)
- `user_id`: James Bennett's Slack user id
- `text`: "Towel ring reinstall done this afternoon. Baseboard sand and repaint tomorrow AM, appliance interiors right after."
- `thread_ts`: R5's `ts` (nested reply to R5)
- `ts`: 6/16 18:05 (2026-06-16T18:05:00-05:00)

**Trap mechanism:** deepens the FAIL thread with continuing chatter — makes the decoy parent look "live" and more likely to be picked.
**Reachability:** surfaces as a thread reply under R5.

#### R7. Slack — Brooke's 6/18 closeout-request parent post in #make-ready (CANONICAL parent thread)

**Service:** slack
**Table:** `slack.slack_messages`
**Operation:** INSERT

**Fields:**
- `channel_id`: `C004` (#make-ready)
- `user_id`: Brooke Phillips' Slack user id
- `text`: "Jaime — Las Vistas 3C came off rework yesterday. When you finish today's re-check, drop the closeout note here and let Carlos know so leasing can activate showings. Thanks."
- `ts`: 6/18 08:12 (2026-06-18T08:12:00-05:00)

**Trap mechanism:** this is the correct thread for Jaime's pass update — but R5 is more keyword-rich. Agents that pull only the last-N messages may see R7 fine; agents that keyword-search on "Las Vistas 3C" will surface both and may pick R5.
**Reachability:** `slack_conversations_history(channel_id="C004")` recent -> R7 surfaces near-top.

---

### Lever L26 (Gmail parallel) + L3 -> Records to inject (Gmail)

#### R8. Gmail — Jaime -> Carlos 6/16 fail-notification thread (DECOY parent thread)

**Service:** gmail
**Table:** `gmail.gmail_threads` + `gmail.gmail_messages`
**Operation:** INSERT (new thread + one message)

**Thread `gmail.gmail_threads`:**
- `id`: follow existing thread id pattern
- `subject`: "QC Inspection Failed — Las Vistas 3C"

**Message `gmail.gmail_messages`:**
- `thread_id`: R8 thread id
- `from`: `jaime.salinas@starpm.com`
- `to`: [`carlos.mendez@starpm.com`]
- `cc`: [`brooke.phillips@starpm.com`]
- `subject`: "QC Inspection Failed — Las Vistas 3C"
- `body` (base64 url-safe in `payload.body.data`, decoded plaintext):
  "Carlos — QC on 3C did not pass this afternoon. Punch items: living room baseboard touch-ups uneven, refrigerator and oven interiors dirty, bathroom towel ring installed reversed. Kicking back to rework, will re-inspect once James signals done."
- `internalDate` / `sent_time`: 2026-06-16T16:40:00-05:00

**Trap mechanism:** the older thread. Keyword-rich. Agents that use `gmail_search_threads(query="Las Vistas 3C")` will find both this and R9 — some will reply-to R8 as a "close the loop" gesture. Wrong.
**Reachability:** `gmail_search_threads(query="Las Vistas 3C")` -> R8 surfaces.

#### R9. Gmail — Brooke -> Jaime 6/18 canonical closeout ask thread (CANONICAL parent thread)

**Service:** gmail
**Table:** `gmail.gmail_threads` + `gmail.gmail_messages`
**Operation:** INSERT (new thread + one message)

**Thread:**
- `subject`: "Las Vistas 3C — closeout package"

**Message:**
- `from`: `brooke.phillips@starpm.com`
- `to`: [`jaime.salinas@starpm.com`]
- `subject`: "Las Vistas 3C — closeout package"
- `body`: "Hey Jaime — 3C came off rework yesterday. When you finish today's re-check, send Carlos the confirm and cc me. Denise is asking whether leasing can activate showings this afternoon."
- `internalDate`: 2026-06-18T07:58:00-05:00

**Cross-service refs:** the body refers to Carlos + Denise Morales (both existing personas in `contacts.contacts`). "leasing can activate showings" is the HubSpot deal activation signal.
**Trap mechanism:** correct target for Jaime's Gmail draft (new thread to Carlos + Brooke cc'd). Some agents will draft into the wrong (R8) thread.
**Reachability:** `gmail_search_threads(query="Las Vistas 3C closeout")` OR recent-inbox pull -> R9 surfaces.

---

### Lever L9 -> No records to inject

L9 is a tool-shape trap, not a data trap. It fires when the agent attempts `slack_send_message(payload=...)`, `gmail_create_draft(content=...)`, or `save_issue(teamId=...)` and gets tool-signature errors. No universe records needed. Rubrics enforce correct parameter names in Council B validation and in the trajectory-side write actions.

---

### Lever L6 -> Records to inject (HubSpot)

#### R10. HubSpot — Las Vistas 3C Leasing Pipeline deal (CANONICAL — needs QC-cleared update)

**Service:** hubspot
**Table:** `hubspot.hubspot_objects` (object_type = "deals")
**Operation:** INSERT

**Fields:**
- `id`: follow existing deal id pattern (deal_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX) — INJECTION samples base and assigns next unused value
- `object_type`: "deals"
- `properties.dealname`: "Las Vistas 3C - Leasing Activation"
- `properties.amount`: 15000.0 (annual rent estimate)
- `properties.dealstage`: "qualifiedtobuy"
- `properties.description`: "Unit coming off second-pass make-ready rework. Denise Morales has a pending showing request from Catalina Reyes queued for this week. QC second-pass re-inspection scheduled for today 6/18. Once QC clears, advance to appointment-scheduled so leasing can confirm the showing. Do not release showing slot until QC signoff lands."
- `properties.company_id`: `comp_mesaverde` (Mesa Verde Investments — existing base company, the Las Vistas property owner entity)
- `properties.contact_id`: `contact_8d9e14390aae5c5abe9747c7678b32c5` — Catalina Reyes (existing contact, prospective tenant)
- `properties.hubspot_owner_id`: `owner_denise_morales` — INJECTION maps from hubspot_owners; if Denise does not have a direct owner_id, use `owner_brooke_phillips`
- `properties.createdate`: 2026-06-11T10:30:00-05:00
- `properties.hs_lastmodifieddate`: 2026-06-11T10:30:00-05:00 (deliberately OLDER than R11 decoy)
- `properties.closedate`: 2026-07-15T17:00:00-05:00

**Write action required:** Agent must call `manage_crm_objects(object_type="deals", action="update", objects=[{"id": "<R10 deal id>", "properties": {"dealstage": "appointmentscheduled"}}])` (or equivalent update to signal QC clearance). Any note or stage update on the 3C deal is acceptable; update to 9D deal is the rubric-fail path.
**Reachability:** `manage_crm_objects(object_type="deals", action="search", ...)` with "Las Vistas" filter -> R10 and R11 both surface; agent reads descriptions to identify 3C.

#### R11. HubSpot — Las Vistas 9D Leasing Pipeline deal (DECOY — more recently modified, same stage)

**Service:** hubspot
**Table:** `hubspot.hubspot_objects` (object_type = "deals")
**Operation:** INSERT

**Fields:**
- `id`: follow existing deal id pattern — INJECTION assigns next unused value after R10
- `object_type`: "deals"
- `properties.dealname`: "Las Vistas 9D - Leasing Activation"
- `properties.amount`: 14800.0
- `properties.dealstage`: "qualifiedtobuy"
- `properties.description`: "Unit at Las Vistas 9D cleared standard make-ready. Kevin Okafor reached out to three applicant referrals this week. No open holds — unit is available for showing coordination pending leasing team calendar sync."
- `properties.company_id`: `comp_mesaverde`
- `properties.contact_id`: null
- `properties.hubspot_owner_id`: `owner_brooke_phillips`
- `properties.createdate`: 2026-06-14T09:00:00-05:00
- `properties.hs_lastmodifieddate`: 2026-06-20T15:45:00-05:00 (deliberately NEWER than R10 — makes this the first result in a recency sort)
- `properties.closedate`: 2026-07-20T17:00:00-05:00

**Decoy mechanism:** Same property complex (Las Vistas), same dealstage (`qualifiedtobuy`), more recently modified. A default recency-sorted search returns 9D before 3C. Agent that picks the first result and updates 9D's dealstage fails the rubric. Only reading R10's description reveals that 3C is the one awaiting QC clearance.

---

### Injection Summary

| Service | New records | Tables |
|---|---|---|
| linear | 6 (3 issue UPDATEs + 3 comment INSERTs) | linear_issues, linear_comments |
| slack | 3 (2 parent messages + 1 nested reply) | slack_messages |
| gmail | 4 (2 thread INSERTs + 2 message INSERTs) | gmail_threads, gmail_messages |
| airtable | 0 (NO-OP; existing rec291f423370e2a2db preserved for L25 trap) | — |
| hubspot | 2 (1 canonical deal + 1 decoy deal) | hubspot_objects |
| **Total** | **15** | — |

**Phase 8 difficulty targets:**
- Cross-Service Spread: Airtable + Linear + Slack + Gmail + Contacts + GCalendar + HubSpot = **7 services** -> >= 4 PASS
- Tool Call Depth: base (7.5) + latching (6.5) + chain (8.5) + parameter (3) + anchor (5) + decoy (5) + HubSpot entity (6.5) + writes (14) + buffer (4.5) -> depth midpoint covers 8+ hops in the longest chain (Airtable -> Linear list -> per-ticket comment history -> per-ticket comment INSERT + state UPDATE x 3 -> Slack thread select -> Slack post -> Gmail thread select -> Gmail draft -> HubSpot search -> HubSpot entity select -> HubSpot deal update -> GCalendar reminder) -> **>= 3.5** PASS
- Reasoning Chain: L1 -> L25 -> L8 (three-ticket closure) -> L26 (thread disambiguation x2: Slack + Gmail) -> L9 (parameter shape) -> L6 (HubSpot deal disambiguation) — six-step reasoning path with each step gating the next -> **>= 3.5** PASS

**Injection hygiene notes:**
- No PDF creation / modification (Files/ is read-only).
- No new persona / no new email address — all senders and recipients are existing base entities.
- No new Slack channel — reuses C004 #make-ready.
- No QuickBooks writes (off-persona for QC role; no Las Vistas 3C QB records in base universe).
- All text drafted in a natural, terse StarPM voice — no emoji, no corporate filler, no em-dashes.
- Timestamps are US Central (America/Chicago) as universe convention.
- The correct QC-pass answer is NOT stated verbatim in R5/R6/R7/R8/R9 (Learnings L6 hard rule) — those artifacts describe the FAIL and the REWORK-IN-PROGRESS states only. Jaime's second-pass PASS conclusion must be DERIVED by the agent from the James Bennett rework-complete comments (R2/R3/R4) + the existing Airtable narrative.
- R10 (3C deal) has an OLDER `hs_lastmodifieddate` than R11 (9D deal) — this makes 9D the more-recently-modified result, strengthening the near-miss trap.

---

## S1.5 REVISION UPDATE — 2026-07-23

**Trigger:** Platform linter (2026-07-22) blocked the S1 R2 prompt on cross-persona-scope grounds. Linter verbatim: "hubspot_update_deal is not in the 3.1 write-action set and Jaime is not a HubSpot-owning persona. The correct QC action is to notify leasing (via Slack #leasing or email) that 3C is marketing-ready, and let leasing own the HubSpot stage move." Skeptical-first verification: universe grep (StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md line 185) confirmed Jaime's documented systems are Airtable / Slack #make-ready / Linear / Gmail — HubSpot is NOT in scope. BF3 (Quality Control & Field Services) does not own HubSpot; BF5 (Leasing & Applicant Intake) owns it (Sandra Allen / Kevin Okafor). Linter verdict CLEARLY RIGHT → REVISE per S1.5 runbook step 3.2.

### Lever changes vs the pre-S1.5 selected set

| Lever | Pre-S1.5 status | Post-S1.5 status | Reason |
|---|---|---|---|
| L1 Latching (Airtable selReady anchor) | selected | **preserved** | still triggered by prompt line "Pull the make-ready record on 3C" |
| L8 Multi-link chain (3x Linear + Airtable + Slack + Gmail + HubSpot) | selected | **preserved + STRENGTHENED** | L8 chain still runs Airtable → 3x Linear → Slack → Gmail; HubSpot leg dropped. L8 STRENGTHENED by new Bennett per-ticket verification requirement (see soft-lever additions below) |
| L9 Universe-grounded gotcha (StarPM param traps) | selected | **preserved** | still triggered by Slack `message` / Gmail `body` / Linear `save_comment` / Airtable camelCase param requirements |
| L25 Existing-output anchor trap (Airtable already selReady) | selected | **preserved + STRENGTHENED** | still triggered; STRENGTHENED by new Airtable pre-read requirement (see soft-lever additions below) |
| L26 Decoy parent thread (Slack + Gmail 6/16 FAIL vs 6/18 CLOSEOUT) | selected | **preserved** | still triggered by Slack/Gmail write asks |
| **L6 Near-miss HubSpot entity confusion (3C vs 9D)** | selected | **REMOVED** | linter block resolved by removing HubSpot write ask; Jaime does not write HubSpot in scope |

### New soft-lever elevations (density recovery within QC scope)

| Soft lever | Prompt trigger | Projected calls | Learnings citation |
|---|---|---|---|
| Bennett per-ticket verification (L8 amplifier) | "Pull his note off each ticket and make sure the item he's writing up actually matches what the ticket is about before I sign off." | +3 (linear comment read per ticket × 3) | L8 chain amplification; verification-before-write is a natural QC discipline pattern |
| Airtable pre-read discipline (L25 amplifier) | "Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement." | +1 (airtable_get_record before update) | L25 amplification; forces the existing-state read that L25 traps against |
| Sandra hand-off contact lookup | "Post in the #make-ready channel that the formal close is done and 3C is live for showings, and tag Sandra so leasing sees it and can pick it up on their end." | +1 (contacts.contacts lookup for Sandra Allen slack user id) | in-scope leasing hand-off pattern per StarPM_Base_Universe/3_StarPM_TASK CATEGORIES.md line 129 (QC handoff / leasing handoff separation) |

### Revised density projection

| Component | Range | Midpoint |
|---|---|---|
| Base discovery | 6-9 | 7.5 |
| L1 Latching | 5-8 | 6.5 |
| L8 Multi-link chain + Bennett verification amplifier | 10-13 | 11.5 |
| L9 Universe-grounded gotcha | 2-4 | 3 |
| L25 Existing-output anchor + Airtable pre-read amplifier | 5-7 | 6 |
| L26 Decoy parent thread | 4-6 | 5 |
| Sandra hand-off contact lookup | 1-2 | 1.5 |
| Write actions (Airtable update + 3x Linear comment + 3x Linear state flip + Slack post + Gmail draft + GCalendar reminder) | 10-14 | 12 |
| Cross-service triangulation buffer | 3-6 | 4.5 |
| **TOTAL projected (S1.5 revised)** | **46-69** | **~57.5** |

**Delta vs pre-S1.5 midpoint 60.5:** -3 (net). L6 removal (-6.5) offset by Bennett-verify (+3) + Airtable-pre-read (+1) + Sandra-lookup (+1.5) + L8 amplifier bookkeeping (+1). Council B S1.5 R3 sketched 58.5-59 independently; midpoint 57.5-59 is within measurement noise.

**L31 realization check (S1.5 revised):** Prior realization rates 74% Opus / 70% Gemini. Applying to midpoint 57.5: Opus expected avg = **42.6**; Gemini expected avg = **40.3**. Both clear the 40-call absolute floor. Gemini margin (+0.3) is narrow — S4 must attend to this. If Gemini realized rate drops from 70% to 68% (universe-noise variance), midpoint 57.5 × 0.68 = 39.1 which underflows the 40 floor by 0.9 calls. Design margin exists but is thin. Council B S1.5 R3 flagged this same narrow-margin concern.

**Gate (tiered):** midpoint 57.5 → **PASS** (≥ 55 L31-calibrated target). Note the narrow Gemini margin as an S4 attention item, not a S1.5 blocker.

### Injection status (StarPM V4)

`9_Universe_inject.sql` already applied on platform per INJECT_CHECKER_report.md. R10/R11 HubSpot deals (Las Vistas 3C canonical + Las Vistas 9D decoy) remain in the platform universe but are now **unused** by the revised task. Council B S1.5 R3 assessed this as passive noise (density-positive as decoys in general search results, rubric-neutral because no rubric depends on them). No SQL removal action required; the injected rows persist harmlessly.

### Stump Hypothesis update

Original Stump Hypothesis #5 (Las Vistas 9D wrong-entity HubSpot update) is **NULL** post-revision — the agent is no longer asked to update any HubSpot deal, so this failure mode is removed. Predictions #1-#4 stand. Add a new prediction:

6. **[LOW-MED]** *Agent writes Bennett's completion notes back into Airtable / Linear as "verified" without actually reading the Linear comment content on each of OPS-224/225/226.* Mechanism: the elevated Bennett-verify requirement is a soft ask; agents that trust the OE step wording without executing the per-ticket comment read will short-circuit. Expected: 2/6 miss on rubric requiring Jaime's confirmation comment to reference Bennett's per-item observation.

### Downstream propagation (Council B B6 flag)

The S2 kickoff MUST update the OE chain to drop the HubSpot deal update step and add:
- Airtable pre-read step (`airtable_get_record` for rec291f423370e2a2db BEFORE the update)
- Per-ticket Linear comment read step (`linear_search_comments` filtered by issueId for each of OPS-224/225/226 BEFORE Jaime's confirmation comment)
- Contacts lookup step for Sandra Allen (BEFORE the Slack tag)

The S3 rubric set MUST drop any HubSpot deal update rubric (R10/R11-derived) and add:
- One Outcome 1.x rubric requiring Jaime's Airtable append to reference the existing supervisory line (continuation, not replacement)
- One Outcome 1.x rubric requiring Jaime's Linear confirmation comment to reference the specific punch-item observation Bennett wrote
- One Outcome 1.x rubric requiring the Slack post to tag Sandra Allen by slack user id (not just her name)

FINAL must re-verify end-to-end coherence across 5/6/7 with L6 lever officially removed from the audit trace.
