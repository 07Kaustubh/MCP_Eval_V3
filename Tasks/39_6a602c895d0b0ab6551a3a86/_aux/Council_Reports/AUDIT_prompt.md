# AUDIT — Prompt (S1.5 Revision Pass)

**Scope note:** This audit is scoped to the **S1.5-revised prompt** and **post-dates** the platform linter block on the pre-revision (R5) prompt (see `_aux/Hardness_Plan.md` S1.5 REVISION UPDATE section, dated 2026-07-23). This report **supersedes** any prior `AUDIT_prompt.md`.

**Task:** 39_6a602c895d0b0ab6551a3a86 · Universe: StarPM (V4) · Today: 2026-07-01 (America/Chicago) · Audit date: 2026-07-23
**Deliverable audited:** `5_Prompt.txt` (356 words, 15 lines)
**Councils' verdict (S1.5 R3):** Council A GO · Council B GO
**Auditor mandate:** strictest possible interpretation — 5/5 only, density 50+, every soft convention binding, every "should" read as "must"

---

## VERDICT: **PASS (STRICT)**

- 0 BLOCKER · 0 MAJOR · 4 MINOR/informational (documented, non-blocking)
- Every applicable QC sub-dim = 5/5
- Every S1.5-revised lever traces end-to-end with cited universe evidence
- Density midpoint 57.5 clears 50+ strict design target (Gemini narrow-margin flag preserved)
- Injection cross-verified: 15/15 rows present in `3_UniverseDataForThisTask.json`
- Zero L6 (HubSpot / CRM / pipeline / deal) residue in prompt — clean removal
- Zero platform-linter-blocking patterns detected

---

## LENS 1 — Strict QC Scoring

Every prompt sub-dim from `Docs/7_QC_Spec_Doc1.json` + `Docs_starpm/13_QC_Companion.md`, under strictest interpretation:

| Sub-dim | Scheme | Score | Evidence |
|---|---|---|---|
| Coherence (Command List) | 1/5 binary | **5/5** | 5 narrative paragraphs with rationale ("that kind of surface tends to get lived-back-in fast"); zero bulleted drop. |
| Coherence (Bolt-on) | 1/5 binary | **5/5** | Remove-sentence test on line 9 "Leasing has been waiting on 3C to open showings...": removing weakens the WHY for the Carlos email (line 11) + Slack tag Sandra (line 13). Downstream asks reference "leasing" without motivation; line 9 anchors urgency. Load-bearing, not decorative. |
| Truthfulness / Groundedness | 1/3/5 | **5/5** | See per-atom evidence table below. |
| Alignment with Today's Date | 1/3/5 | **5/5** | "the 18th"→2026-06-18 (Thu), "Friday"→2026-07-03, "next Wednesday"→2026-07-08 — all resolve given today=2026-07-01 (Wed) per `_aux/Universe_Index/today_horizon.json` + `Fact_Ledger.dates`. |
| Unique Ground Truth | 1/3/5 | **5/5** | "formal side" unpacked by lines 5-15; two-reading test in Lens 5 finds no divergent write path. |
| Feasibility / Achievability | 1/3/5 | **5/5** | Every ask maps to Jaime-accessible StarPM V4 tool (`update_records_for_table`, `save_comment`+`save_issue`, `create_draft`, `slack_send_message`, `create_event`, `contacts_search_contacts`). |
| Explicit Tool Mention | 1/5 binary | **5/5** | No tool / service / API names. "#make-ready channel" is a channel-name reference, not a tool name. |
| Contrived / Unnatural | 1/3/5 | **5/5** | Terse, observation-first, methodical. Matches PersonaBrief Jaime (formality 0.55, verbosity 0.30). |
| Tool Use & Cross-Service | 1/5 binary | **5/5** | 6 detectable services: airtable, linear, contacts, slack, gmail, gcalendar. Above 2+ floor. |
| Investigation + Action | 1/5 binary | **5/5** | Investigation: Bennett per-ticket verify + Airtable pre-read + calendar range check. Action: 3×Linear comment + 3×Linear state flip + Airtable append + Gmail draft + Slack post + GCalendar reminder = 10 writes. |
| **Persona / Scope Fit** | 1/3/5 | **5/5** | See below — CRITICAL PASS given the linter block that triggered S1.5. |
| **Business Function Match** | 3/5 scheme | **5/5** | BF3 100% match; zero BF5 leakage. See below. |
| Length compliance | binary | **5/5** | 356 words < 500 cap. |
| Em-dash compliance | binary | **5/5** | Zero `—` / `–` in prompt (grep-verified). |
| "at least N" compliance | binary | **5/5** | Zero unmandated "at least N" (grep-verified). |

### Persona Scope Fit — critical pass (linter block resolution verified)

Per StarPM `2_StarPM_PERSONA BRIEFS.md`, Jaime Salinas (QC Inspector, BF3) documented systems: Airtable Make-Ready · Slack #make-ready · Linear (QC tickets) · Gmail (Onsite PM notifications). Every write ask in the revised prompt maps to that set:

| Line | Ask | Service | In-scope for Jaime BF3? |
|---|---|---|---|
| 5 | "get each ticket moved through my sign...pass called out for each item" | Linear per-ticket comment + Done | YES (QC gate ownership) |
| 5 | "Pull his note off each ticket and make sure the item he's writing up actually matches" | Linear read (Bennett comment content) | YES (verification pre-write is QC discipline) |
| 7 | "Pull the make-ready record on 3C and get my second-pass sign-off written into it" | Airtable Make-Ready append | YES (Airtable = named QC system) |
| 7 | "Read what's already sitting in the notes so my sign-off reads as a continuation" | Airtable pre-read | YES |
| 11 | "Carlos needs an email from us...Copy Brooke" | Gmail draft to Onsite PM + supervisor cc | YES (Gmail = named Onsite PM notification path) |
| 13 | "Post in the #make-ready channel...and tag Sandra so leasing sees it" | Slack top-level post + user mention | YES (#make-ready = Jaime's named channel; @-mention is Slack, not HubSpot) |
| 15 | "set me a reminder for Friday morning" | GCalendar personal reminder | YES (personal QC follow-up) |

**HubSpot residue scan (post-linter):** grep of `5_Prompt.txt` for `hubspot`, `HubSpot`, `CRM`, `deal`, `pipeline`, `deal stage`, `dealstage`, `advance`, `activate the deal`, `crm`, `pipeline advance` — **zero hits**. The R5-blocked "get the 3C leasing deal updated in the pipeline" phrasing is fully removed. The line 9 "Leasing has been waiting on 3C to open showings, so they'll want the heads-up from us before they can move on their end" retains only the LEASING CONTEXT (not the CRM write ask), which is required to motivate the Slack tag + Carlos email hand-offs downstream. Clean L6 removal. **PASS.**

### Business Function Match

BF3 (Quality Control & Field Services) requires: QC sign-off / punch-item closure / rework verification / make-ready state ownership. Every prompt ask is a BF3 activity or a BF3→peer hand-off (email to Onsite PM, Slack tag to Leasing). No BF5 (Leasing & Applicant Intake) write asks — the Sandra tag is a **notification hand-off in the Slack channel** (Jaime's domain), not a HubSpot write. **BF3 = 100%, PASS.**

### Truthfulness — per-atom evidence table (grounding proof)

| Prompt claim | Universe atom (per-task) | Verified |
|---|---|---|
| "Got the QC pass posted for Las Vistas 3C back on the 18th" | Airtable `rec291f423370e2a2db.fldTargetReady=2026-06-18`; `fldTurnStatus=selReady`; `fldNotes2` supervisory line references 6/18 second-pass | ✅ |
| "Brooke" (follow-up sender) | `contacts.contacts` + `hubspot.hubspot_owners.owner_brooke_phillips` + Slack msg `03e5b7c4a9fb5d803c7e1b4a52d69f7c` from Brooke on 2026-06-18T13:12:00+00:00 | ✅ |
| "Bennett dropped a completion note on each of the three 3C punch items around the time I re-inspected" | Linear comments `comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02` (OPS-224 · 2026-06-17T16:44), `comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13` (OPS-225 · 2026-06-17T11:19), `comment_c3e69a4f5bad63a8d1f43e1b6c709d24` (OPS-226 · 2026-06-16T15:34) — all authored by `user_8cd13ca90bca5494ab86e300c4b7829b` (James Bennett) | ✅ |
| "three 3C punch items" (baseboard, appliance interiors, towel ring) | Linear OPS-224 (baseboard) + OPS-225 (appliance interiors) + OPS-226 (towel ring), all `state_id=state_OPS_3`, `completed_at=NULL` | ✅ |
| "make-ready record on 3C" (fldNotes2 continuation) | `airtable.airtable_records.rec291f423370e2a2db.fldNotes2` currently ends "...cleared for marketing with supervisory sign-off from Brooke Phillips" — third-person Brooke narrative; Jaime-first-person signoff is NOT present | ✅ |
| "Brooke's supervisory note" | fldNotes2 tail ends with "supervisory sign-off from Brooke Phillips" | ✅ |
| "Carlos" (email recipient) | `contacts.contacts` Carlos Mendez (Onsite PM, `carlos.mendez@starpm.com`) | ✅ |
| "#make-ready channel" | `slack.slack_channels.C004.name=#make-ready` | ✅ |
| "Sandra" (Slack tag) | `slack.slack_users.UADB2B4E045.name=sandra.allen`, real_name=Sandra Allen; also `contacts.contacts` (Leasing Agent per Fact_Ledger.personas); also `hubspot.hubspot_owners.owner_sandra_allen` | ✅ |
| "any 3C showings booked between now and next Wednesday" | Zero 3C events in gcalendar.gcalendar_events window 2026-07-01 through 2026-07-08 (agent's expected null-result path) | ✅ |
| "Friday morning" | 2026-07-03 (Friday) per Fact_Ledger.dates + universe today = 2026-07-01 Wed | ✅ |

**Truthfulness = 5/5. All per-atom evidence traces to per-task `3_UniverseDataForThisTask.json`.**

### StarPM V4 injection cross-verification (MANDATORY per audit mandate)

Every `INSERT` / `UPDATE` row in `9_Universe_inject.sql` cross-checked against `3_UniverseDataForThisTask.json`:

| SQL row | ID / target | Present in 3_Universe? | Correct state? |
|---|---|---|---|
| R2 UPDATE | linear_issues.OPS-224 → state_OPS_3, completed_at=NULL | ✅ | state_id=state_OPS_3, completed_at=None, updated_at=2026-06-17T16:45 ✅ |
| R3 UPDATE | linear_issues.OPS-225 → state_OPS_3, completed_at=NULL | ✅ | state_id=state_OPS_3, completed_at=None, updated_at=2026-06-17T11:20 ✅ |
| R4 UPDATE | linear_issues.OPS-226 → state_OPS_3, completed_at=NULL | ✅ | state_id=state_OPS_3, completed_at=None, updated_at=2026-06-16T15:35 ✅ |
| R2 INSERT | linear_comments.comment_a1c47e2d3f8b41e6b9d21c9f4a5e7b02 | ✅ | present |
| R3 INSERT | linear_comments.comment_b2d58f3e4a9c52f7c0e32d0a5b6f8c13 | ✅ | present |
| R4 INSERT | linear_comments.comment_c3e69a4f5bad63a8d1f43e1b6c709d24 | ✅ | present |
| R5 INSERT | slack_messages.01c3f5a2e7d94b681a5c9f2e30b47d5a (6/16 decoy) | ✅ | present |
| R6 INSERT | slack_messages.02d4a6b3f8ea4c792b6d0a3f41c58e6b (Bennett reply) | ✅ | present |
| R7 INSERT | slack_messages.03e5b7c4a9fb5d803c7e1b4a52d69f7c (6/18 canonical) | ✅ | present |
| R8 INSERT | gmail_threads.a7f3c92e1b4d8e56 (fail decoy) | ✅ | present |
| R8 INSERT | gmail_messages.c9d5e1b4a3f6c0a8 | ✅ | present |
| R9 INSERT | gmail_threads.b8e4d0a3f2c5b9e7 (canonical closeout) | ✅ | present |
| R9 INSERT | gmail_messages.d0e6f2c5b4a70b19 | ✅ | present |
| R10 INSERT | hubspot_objects.deal_c3a1b2e4f5d67890ab12cd34ef56789a (3C canonical) | ✅ | dealstage=qualifiedtobuy, hs_lastmodifieddate=2026-06-11 (older) ✅ |
| R11 INSERT | hubspot_objects.deal_d4b2c3e5f6a78901bc23de45fa6b7c8d (9D decoy) | ✅ | dealstage=qualifiedtobuy, hs_lastmodifieddate=2026-06-20 (newer) ✅ |

**Injection integrity: 15/15 rows present with correct state. PASS.** R10/R11 HubSpot deals are unused by the revised prompt but remain in the platform universe as passive noise (Council B B6 assessment: density-positive, rubric-neutral once S3 confirms no HubSpot rubrics).

### Landmine self-check (per audit mandate)

- **Slack param trap:** prompt says "Post in the #make-ready channel" — no bias toward wrong `payload`/`text` params; agent will pick `message`. `slack_send_message_draft` disqualification is a rubric-time concern, not a prompt-time concern. PASS.
- **Gmail send trap:** prompt says "Carlos needs an email from us" — Gmail is draft-only in StarPM V4 (no send tool). Prompt's "email from us" reads naturally as a `create_draft` action. No bias toward a non-existent send. PASS.
- **Airtable camelCase:** implicit; rubric-level enforcement. PASS.
- **Linear `team` vs `teamId`:** implicit; not triggered by prompt. PASS.

### LENS 1 sub-verdict: **PASS.** All applicable sub-dims = 5/5. No REVISE issues.

---

## LENS 2 — Answer-Leakage Sweep

Derived answer surface (per `_aux/Hardness_Plan.md` stump hypotheses + rubrics-to-be):
1. Jaime's second-pass QC PASS conclusion per punch item (baseboard, appliance interiors, towel ring)
2. Correct Slack thread target (canonical 6/18 vs decoy 6/16)
3. Correct Gmail thread target (canonical 6/18 vs decoy 6/16)
4. Correct 3 Linear tickets moved to Done (not "one blanket close")
5. Airtable fldNotes2 continuation (append, not overwrite)

**Verbatim-answer string-search on `5_Prompt.txt`:**

| Candidate leak | Present in prompt? | Verdict |
|---|---|---|
| "second-pass passed" / per-item PASS verbatim | Prompt IS Jaime's first-person narrative stating punch items cleared — this is EXPECTED persona reporting (per FINAL council Lens 1 rule). Not leakage — the prompt is the persona's opening frame. | ✅ non-leakage |
| Slack thread_ts / ts values | absent | ✅ |
| Gmail message-id / thread-id | absent | ✅ |
| Linear comment IDs | absent | ✅ |
| Airtable record ID / fldNotes2 verbatim | absent | ✅ |
| Deal IDs | absent | ✅ |
| "state_OPS_4" / "Done" state IDs | absent | ✅ |

**Arithmetic-neighbor check:** no derived amounts, no derived counts beyond "three punch items" (which is a stated fact, not a derived answer). PASS.

**LENS 2 sub-verdict: PASS.** No answer-leakage BLOCKER.

---

## LENS 3 — Hardness End-to-End Trace

For each S1.5-revised lever, cite the exact prompt sentence + Fact_Ledger / Universe_Split atom(s):

### L1 Latching — Airtable selReady anchor
- **Prompt trigger (line 7):** "Pull the make-ready record on 3C and get my second-pass sign-off written into it."
- **Universe atoms:** `airtable.airtable_records.rec291f423370e2a2db` — `fldTurnStatus=selReady`, `fldTargetReady=2026-06-18`, `fldNotes2` third-person retrospective ending with Brooke supervisory line.
- **Trap:** agent reads Airtable state, sees "already Ready", latches, skips downstream write cascade.
- **Trace:** ✅

### L8 Multi-link chain — 3 Linear closures + Airtable + Slack + Gmail (HubSpot leg dropped)
- **Prompt trigger (line 5):** "Then get each ticket moved through my sign and out of my queue with the pass called out for each item, not a blanket close."
- **Universe atoms:** Linear `OPS-224/225/226`, all `state_id=state_OPS_3` (In Review), Bennett rework-complete comments planted per ticket.
- **Chain:** Airtable read → 3× Linear read + comment + state flip → Slack post → Gmail draft → GCalendar reminder. Bennett-verify amplifier expands the Linear leg by +3 (one comment read per ticket).
- **Trace:** ✅

### L9 Universe-grounded gotcha — StarPM parameter traps
- **Prompt trigger:** implicit (agent-executed writes will fire the trap).
- **Universe atoms:** StarPM tool catalog `7_Server_Tools_Details.json` — Slack `slack_send_message(channel_id, message)`; Gmail `create_draft(to[], body, subject)` draft-only; Linear `save_comment(issueId, body)`; Airtable `update_records_for_table(baseId, tableId, records[])` camelCase; `slack_send_message_draft` exists but does NOT send.
- **Trap fires:** first write attempt with wrong param name (`payload`/`text`/`content`/`teamId`/snake_case).
- **Trace:** ✅

### L25 Existing-output anchor trap — Airtable already selReady blocks write cascade
- **Prompt trigger (line 7):** "Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement. Anyone pulling 3C up after this should read the second-pass sign-off and not just Brooke's supervisory note."
- **Universe atoms:** `fldNotes2` narrative currently ends "...cleared for marketing with supervisory sign-off from Brooke Phillips" — no Jaime-first-person signoff, no per-item confirmation.
- **Trap:** existing narrative superficially "closes" the record; agent's no-op instinct kills the cascade.
- **Amplifier:** the "Read what's already sitting in the notes" clause is the L25 amplifier — forces the existing-state read that L25 traps against (Council B B4 confirmed semantically visible to agent).
- **Trace:** ✅

### L26 Decoy parent thread — 6/16 FAIL vs 6/18 CLOSEOUT in both Slack + Gmail
- **Prompt trigger:** implicit (line 11 Carlos email + line 13 Slack post must land on canonical 6/18 thread pair, not decoy 6/16).
- **Universe atoms:** 
  - Slack: `01c3f5a2e7d94b681a5c9f2e30b47d5a` (6/16 decoy FAIL parent, keyword-rich) vs `03e5b7c4a9fb5d803c7e1b4a52d69f7c` (6/18 canonical CLOSEOUT parent from Brooke)
  - Gmail: `a7f3c92e1b4d8e56` (6/16 decoy FAIL thread) vs `b8e4d0a3f2c5b9e7` (6/18 canonical CLOSEOUT thread from Brooke)
- **Trap:** older FAIL thread has richer keyword footprint (baseboard + appliance + towel ring); agent that keyword-searches picks wrong parent.
- **Trace:** ✅

### Bennett per-ticket verification (L8 amplifier, new soft-lever)
- **Prompt trigger (line 5):** "Pull his note off each ticket and make sure the item he's writing up actually matches what the ticket is about before I sign off."
- **Universe atoms:** the three Bennett Linear comments (see L8 above) — each references a distinct punch item that must match the ticket title (OPS-224 baseboard, OPS-225 appliances, OPS-226 towel ring).
- **Density contribution:** +3 (1 linear_search_comments / linear_get_comments call per ticket).
- **Trace:** ✅

### Airtable pre-read discipline (L25 amplifier, new soft-lever)
- **Prompt trigger (line 7):** "Read what's already sitting in the notes so my sign-off reads as a continuation of the supervisory line, not a replacement."
- **Universe atoms:** `fldNotes2` current content — Brooke's supervisory sign-off narrative.
- **Density contribution:** +1 (airtable_get_record on rec291f423370e2a2db BEFORE update).
- **Trace:** ✅

### Sandra hand-off contact lookup (new soft-lever)
- **Prompt trigger (line 13):** "tag Sandra so leasing sees it and can pick it up on their end."
- **Universe atoms:** Sandra Allen grounded across `contacts.contacts` (sandra.allen@starpm.com), `slack.slack_users.UADB2B4E045` (name=sandra.allen, real_name=Sandra Allen), `linear.linear_users.user_02f411243d8f550daf3f13d46eb13979`, `hubspot.hubspot_owners.owner_sandra_allen`, `airtable.airtable_users.usr_sandra_allen`, `gcalendar.gcalendar_calendars.sandra.allen@starpm.com`. Leasing Agent title per contacts.
- **Density contribution:** +1 (contacts_search_contacts + optional slack_users resolve for `<@UADB2B4E045>` mention format).
- **KS-9 persona-attribution reverse-groundedness:** Sandra Allen is universe-documented Leasing Agent (per Fact_Ledger.personas: "Leasing Agent") — co-occurs with the leasing workstream domain. Per Hardness_Plan.md line 410 "BF5 (Leasing & Applicant Intake) owns it (Sandra Allen / Kevin Okafor)" — Sandra is explicitly named as one of two leasing owners. **Reverse-grounded**, not name-only.
- **Trace:** ✅

### L6 residue check (removal verification)
- Prompt grep for: `hubspot`, `HubSpot`, `CRM`, `crm`, `deal`, `pipeline`, `dealstage`, `9D`, `Las Vistas 9`, `activate the deal`, `advance to`, `pipeline advance`, `stage move`, `owner_denise`, `owner_brooke` — **ZERO hits**.
- Line 9 "Leasing has been waiting on 3C to open showings, so they'll want the heads-up from us before they can move on their end" retains ONLY the leasing-context motivation (which triggers the Slack tag + Carlos email hand-offs). Does NOT name HubSpot, deals, pipeline, or any CRM entity.
- **L6 removal: CLEAN.** ✅

### LENS 3 sub-verdict: **PASS.** All 5 preserved levers + 3 new soft-lever elevations trace end-to-end with universe evidence. L6 cleanly removed.

---

## LENS 4 — Strict Density Projection

Strict interpretation minimizes inferred exploration. Sketch essentials-only path:

| Component | Essentials | Notes |
|---|---|---|
| Base discovery (universe today, 3 contact lookups, channel/thread resolve) | 6-9 | midpoint 7.5 |
| L1 Latching (Airtable get_record + Linear list_issues + re-read to confirm state) | 5-8 | midpoint 6.5 |
| L8 multi-link chain (3× list_comments Bennett verify + 3× save_comment + 3× save_issue state flip) | 10-13 | midpoint 11.5 |
| L9 param retries (Slack message vs payload; Gmail body vs content; Airtable camelCase) | 2-4 | midpoint 3 |
| L25 existing-output anchor (extra fldNotes2 re-reads before append) | 5-7 | midpoint 6 |
| L26 decoy disambiguation (Slack #make-ready history + Gmail thread search + subject-match) | 4-6 | midpoint 5 |
| Sandra contact lookup (contacts + slack_users for mention format) | 1-2 | midpoint 1.5 |
| Writes (Airtable update + 3× Linear comment + 3× Linear state flip + Slack post + Gmail draft + GCalendar create_event) | 10-14 | midpoint 12 |
| Cross-service triangulation buffer | 3-6 | midpoint 4.5 |
| **Total strict midpoint** | **46-69** | **~57.5** |

**Classification: PASS (STRICT).** Midpoint 57.5 clears 50+ design target. No THIN_DENSITY.

### Gemini narrow-margin evaluation (per audit mandate)

Applying L31 realization rates:
- Opus 74% × 57.5 = **42.6** expected avg (clears 40 floor with 2.6-call margin).
- Gemini 70% × 57.5 = **40.25** expected avg (clears 40 floor with **0.25-call margin**).

Under strictest interpretation, the Gemini margin is thin: a real-world realization rate of 68% (2 pts below baseline, plausible universe-noise variance per L31 evidence) yields 57.5 × 0.68 = 39.1, which underflows the 40 floor by 0.9 calls.

**Verdict:** Non-blocker at the prompt phase — midpoint math is sound and clears the 50+ strict design target. Council B S1.5 R3 independently flagged the same narrow margin. **Flagged for S4 attention** — if Gemini avg lands 38-40 in real runs, root cause is density-margin (not lever design), and REDO would be a candidate. Document as MINOR informational.

### LENS 4 sub-verdict: **PASS** with documented narrow-margin note.

---

## LENS 5 — Adversarial Veteran Review

Pattern recognition from cross-task history + `Tasks/_meta/Learnings.md`:

| Adversarial check | Status | Notes |
|---|---|---|
| Implicit-prompt framing (L15+L16) | **PRESERVED** | Persona believes the QC pass is done; agent's job is "wrap the formal side". No hint that any step is missing. |
| Entity drift (Sandra Allen ↔ "leasing", Brooke ↔ "Brooke", Bennett ↔ "James Bennett") | **CLEAN** | Sandra = Leasing Agent (Fact_Ledger + contacts + slack_users). "Brooke" = Brooke Phillips (Apartment Property Supervisor). "Bennett" = James Bennett (Assistant Maintenance Technician). No first-name collision (no second Bennett/Brooke/Sandra/James in universe personas). |
| Silent process rubric candidate (three-condition test) | **BORDERLINE INFORMATIONAL** | Line 5 "make sure the item he's writing up actually matches what the ticket is about before I sign off" is a verification-before-write instruction. Three-condition test: (1) required by every valid path? YES; (2) outcome can't cover it? NO — outcome rubric can require Jaime's confirmation comment to reference Bennett's per-item observation (that IS the write); (3) evaluates verification not execution? Only if authored as a process rubric — the outcome-only framing (Council B B6: "Jaime's Linear confirmation comment to reference the specific punch-item observation") sidesteps this. **S3 authoring must resist the silent-process-rubric temptation.** Flag as MINOR — depends on S3 discipline. |
| Tool name leaks in prompt | **CLEAN** | Zero tool/service/API names (grep-verified). |
| Em-dashes | **CLEAN** | Zero `—` / `–` (grep-verified). |
| "at least N" without mandate | **CLEAN** | Zero occurrences. |
| Internal IDs in prompt | **CLEAN** | No OPS-XXX, no rec_, no C004, no thread_ts, no deal_ ids. |
| OE meta-tags in prompt | **CLEAN** | No `[OE-N]`, no `SETUP_STEP`, no `INVESTIGATION_STEP` tags. |
| Single-channel lock-in on goal-only asks | **CLEAN** | Line 11 explicitly names "email", line 13 explicitly names "#make-ready channel", line 15 explicitly names "reminder". All channels named by prompt (agent-locked correctly at rubric time). |
| KS-9 persona-attribution reverse-groundedness (Sandra) | **PASS** | Sandra Allen co-occurs with leasing/BF5 in universe personas + hardness plan explicitly cites her as leasing owner. Not a name-only mention. |
| StarPM param-trap bias check (Slack `message`/Gmail `body`) | **PASS** | Prompt uses natural language ("Post in the channel...", "Carlos needs an email"); no biasing toward `payload`/`text`/`content` shape. |
| StarPM Gmail send vs draft | **PASS** | Prompt "email from us" reads as `create_draft`; no bias toward a non-existent send tool. |
| StarPM slack_send_message_draft trap | **PASS** | Prompt "Post in the #make-ready channel that the formal close is done" reads as a send action (not draft). Rubric-time disqualifier per Council A/B. |
| Bolt-on sentence check (remove-sentence test on every sentence) | **PASS** | Every line contributes: line 1 (frame), line 3 (per-item observations grounding), line 5 (Linear + Bennett verify), line 7 (Airtable + L25 amplifier), line 9 (WHY for lines 11+13), line 11 (Gmail hand-off), line 13 (Slack post + Sandra tag), line 15 (calendar check + reminder). Line 9 remove-test: removing it strips the "why act today" urgency; downstream asks reference "leasing" without motivation. Non-bolt-on. |

### LENS 5 sub-verdict: **PASS** with 1 MINOR informational note (S3 process-rubric discipline for line 5 Bennett-verify wording).

---

## LENS 7 — Anti-Rationalization Scan

Re-scanning my Lens 1-5 reasoning for "considered flagging X but decided it's fine because..." rationalization patterns:

1. **Line 9 bolt-on:** I said "borderline defensible" then scored 5/5. Re-check: under strictest reading, "borderline" would push to 3/5 or REVISE. **HONEST DEFENSE:** the remove-sentence test says removing line 9 severs the WHY for the Carlos email + Slack tag. Both downstream asks contain "leasing" without motivation absent line 9. That IS load-bearing motivation, not bolt-on decoration. NOT promoted to REVISE. Documented for transparency.

2. **Gemini narrow-margin +0.25:** I scored density PASS at 57.5 midpoint. Under strictest reading, 57.5 clears the 50+ design target. Gemini narrow-margin is real but is an S4 concern, not a S1.5 prompt-phase concern. NOT promoted to REVISE. Flagged as MINOR for S4.

3. **Bennett-verify soft process push:** I flagged as MINOR informational. Under strictest reading, this is a genuine risk that only materializes at S3 authoring time. The prompt phase cannot fix it; S3 must resist authoring a process rubric. NOT promoted to REVISE — proper venue is S3, not S1.5. Documented for downstream propagation.

4. **Sandra vs Kevin Okafor for leasing tag:** I flagged as MINOR ambiguity, then noted "prompt says Sandra explicitly, so agent's action unambiguous". Re-check: prompt saying "Sandra" makes agent's action deterministic regardless of whether Kevin would also be valid. Non-ambiguity for the agent. NOT promoted to REVISE.

**Zero rationalization findings promoted to REVISE.** All 4 candidates checked under strictest interpretation remain defensible or belong to a different phase.

---

## LENS 8 — Regression Anchor Verification

Operator-run `python3 Validators/test_regression_anchors.py` result: **not pasted inline by operator**. Reserved for operator note — if not run, the audit does NOT block on this lens (per audit mandate the operator would paste result inline if applicable).

**LENS 8 status:** N/A (operator did not paste result). Recommend: operator run `python3 Validators/test_regression_anchors.py` before final ship if the pipeline has been touched since last regression pass.

---

## Summary of Findings

| # | Severity | Lens | Location | Finding |
|---|---|---|---|---|
| 1 | MINOR (informational) | 4 | Density projection (Gemini) | Gemini expected avg 40.25 clears 40 floor by only 0.25 calls. Real-world variance could underflow. S4 must attend; not a prompt-phase blocker. |
| 2 | MINOR (informational) | 5 | Line 5 Bennett-verify wording | Verification-before-write language flirts with a silent process rubric candidate. S3 authoring must use outcome-only framing (Jaime's comment references Bennett's per-item observation). Council B B6 already flagged this for S3 kickoff. |
| 3 | MINOR (informational) | 1 | Fact_Ledger.meta timezone | `today_horizon.json` says `universe_timezone=America/New_York` but AGENTS.md StarPM registry says `America/Chicago`. Fact_Ledger indexer artifact. Non-blocking for prompt (Jaime's calendar record is authoritative). |
| 4 | MINOR (informational) | 3 | R10/R11 HubSpot deals | Injected under R2 lever plan; unused by S1.5-revised prompt. Council B B6 assessment stands: passive noise, density-positive, rubric-neutral (S3 must NOT include HubSpot rubrics). |

**BLOCKER count: 0**
**MAJOR count: 0**
**MINOR / informational: 4** (all documented, all non-blocking)

---

## VERDICT: **PASS (STRICT)**

Every applicable QC sub-dim = 5/5. Every S1.5-revised lever traces end-to-end with cited universe evidence. Density midpoint 57.5 clears 50+ strict design target. All 15 injected rows verified in per-task `3_UniverseDataForThisTask.json`. Zero HubSpot / CRM / pipeline / deal residue in prompt — clean L6 removal. Zero platform-linter-blocking patterns. Persona scope fit rescored honestly at 5/5 post-linter: every write in Jaime's documented BF3 systems.

The S1.5 revision fully resolves the platform linter block. Prompt is ready to progress to S2 (Oracle Events). Council B B6 propagation flags stand for S2 kickoff:

- S2 must NOT carry HubSpot OE steps forward from any prior draft.
- S3 must NOT include HubSpot deal update rubrics.
- S3 must resist silent-process-rubric authoring on the Bennett-verify line (Council B B6 gave the outcome-only rubric shape: "Jaime's Linear confirmation comment references Bennett's per-item observation").
- S4 must attend to the Gemini narrow-margin density risk.

---

**Audit provenance:** S1.5 auto-fire per `Reference/Sessions/S1.5.md` step 8 + `Reference/Sessions/AUDIT.md` conditionality table. Supersedes prior S1 audit report on this task. Date: 2026-07-23.
