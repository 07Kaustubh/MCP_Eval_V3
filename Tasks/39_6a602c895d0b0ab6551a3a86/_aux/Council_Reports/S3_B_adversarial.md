# S3 Council B — Adversarial QC (REDO)

## Verdict

**NO-GO** — 2 Moderate blockers (R18 Gmail threading lock-in, R21 Slack thread_ts lock-in). Both are lever-preserving (L26) but rest on threading discipline that the R5 prompt does not literally require. Iterate before AUDIT: preferred fix is **PROPAGATE TO S1** (add explicit threading language to the prompt so R18/R21 stop being over-specific); acceptable alternative is loosen R18/R21 (loses L26 discriminator, do not prefer). Absolute-count gates PASS (Major 0, Moderate 2, Minor 2 — all under thresholds), so this is a lever-vs-scope alignment escalation, not a rubric-quality collapse.

Density projection lands at **THIN_DENSITY midpoint ~48** — allowed under v21 policy with HARDNESS S1.5 justification (L6 dropped for linter; residual 5-lever set inherently supports 44-52), but the S2 mandatory-attention flag on Gemini realized density stands: if Gemini avg < 40 on the real 6-run, this task triggers another REDO cycle regardless of rubric verdict.

---

## B1. Overall Rubric Quality — 4/5

Rubric count = 26 (< 30, absolute-count gates apply per Reference/Rubric_Format.md line 148).

**Defect tally (per V4 July 2026 severity taxonomy):**

| Severity | Count | Rubrics | Rationale |
|---|---|---|---|
| Major | 0 | — | — |
| Moderate | 2 | R18, R21 | Overly Specific — thread lock-in fails a valid alt-path (fresh email / top-level Slack post with correct content), and the prompt does not explicitly mandate threading. Per V4: "Overly Specific" was promoted to Moderate July 2026 because "an over-specified rubric actively causes valid agent paths to fail." Both are lever-preserving (L26 decoy-parent) — the design tension is real. See B8+B9. |
| Minor | 2 | R11, R25 | R11: "attributes the entry to Jaime Salinas by name" has no `(or similar)`; an append signed "— Jaime" (first name only) is a realistic voice-consistent alt that fails the literal title. R25: 07:00-10:00 CT window is defensible for pre-tour logic but a 10:30 slot is arguably still "morning". |
| Non-Failing | 0 | — | — |

**Threshold check:**
- Major > 10% or absolute ≥ 3? Major = 0, absolute 0 → PASS
- (Major + Moderate) > 15% or absolute ≥ 5? 2/26 = 7.7%, absolute 2 → PASS
- (Major + Moderate + Minor) > 20% or absolute ≥ 8? 4/26 = 15.4%, absolute 4 → PASS
- No Major AND no Moderate AND < 5% Minor? FAILS (2 Moderate exists) → NON-FAIL bucket

Score = **4/5** (PASS on absolute gates, but the 2 Moderate findings prevent 5/5).

---

## B2. Rubric Category Balance — 5/5

Outcome = 26, Process = 0. Outcome > Process ✓. Process ≤ 50% ✓ (0%). Zero Outcome check ✓ (not zero).

**Borderline scan — no misfiled category:**

- No Outcome rubric should have been Process. All 26 test either a write-action result (1.1) or the specific content of a write action (1.2). None test ordering-between-actions or investigation-that-outcomes-cannot-cover (the two V3 Process legitimacy conditions).
- No Process rubric exists that should have been Outcome.

**Missing Process candidates (Phase 3.2 three-condition test):**

| Candidate | Cond 1 (required by every path) | Cond 2 (Outcome can't cover) | Cond 3 (behavioral, not tool trace) | Verdict |
|---|---|---|---|---|
| Bennett per-ticket verify before comment | Yes — prompt L5 explicit | Partial — R2/R5/R8 per-item content proves item is KNOWN, but not that Bennett's comment was READ (agent could infer from ticket title) | Yes | Borderline. Outcome R2/R5/R8 is strong enough per "tighten Outcome first". Do not add. |
| Airtable pre-read before append | Yes — prompt L7 explicit | No — R13 (preserves existing narrative) cannot be satisfied without pre-read | Yes | Do not add — R13 already covers. |
| Calendar-window check before reminder | Yes — prompt L15 explicit | Yes — the check is null-tolerant (OE28) so no Outcome captures the pure read | Yes | Genuinely qualifies. See PROPAGATE section. |

Verdict: **zero process is CORRECT** for the current write-action coverage. Optional Process rubric for the calendar-window read is a defensible addition but not required (R25's 07:00-10:00 pre-tour window implicitly encodes the "before earliest tour" logic).

Score = **5/5**.

---

## B3. Tool-Call Density Projection

**Independent trajectory sketch (Opus 4.8 on R5 against the 26 rubrics):**

| Phase | Calls | Count | Range |
|---|---|---|---|
| Contacts (Brooke, Carlos, Bennett, Sandra) | 4 | 4 | 4-5 |
| Airtable metadata (list_bases, list_tables_for_base, get_table_schema) | 3 | 3 | 3-4 |
| Airtable record read (search_records "Las Vistas 3C") | 1 | 1 | 1-2 |
| Linear team backlog orient (list_issues broad + narrowed) | 2 | 2 | 1-3 |
| Linear per-ticket get (OPS-224/225/226) | 3 | 3 | 3-3 |
| Linear per-ticket list_comments (Bennett verify amplifier) | 3 | 3 | 3-6 (pagination) |
| Linear list_issue_statuses | 1 | 1 | 1-2 |
| Gmail search_threads canonical | 1 | 1 | 1-2 |
| Gmail get_thread canonical + 2 decoys | 3 | 3 | 2-4 |
| Slack list channels + slack_read_channel C004 | 2 | 2 | 1-3 |
| Calendar list_events window | 1 | 1 | 1-2 |
| **Reads subtotal** | — | **24** | **21-36** |
| L9 gotcha retry loops (Slack payload→message, Gmail content→body, Airtable snake→camel) | ~3 | 3 | 2-5 |
| Cross-service triangulation buffer | ~4 | 4 | 3-6 |
| **Writes** (3 Linear comments + 3 Linear state flips + 1 Airtable + 1 Gmail + 1 Slack + 1 Calendar) | 10 | 10 | 10-10 |
| **PROJECTED TOTAL** | — | **~41-57** | midpoint ~48 |

**Tier: THIN_DENSITY** (midpoint 48, band 40-49).

**Comparison to HARDNESS S1.5 midpoint 57.5:** my independent projection is ~9 calls below HARDNESS's optimistic count. Gap sources: HARDNESS budgets aggressive L1/L25 re-reads (6.5 + 6) that Opus 4.8 does not consistently perform — agents that latch on selReady tend to reduce, not multiply, verification calls. Verification_s2 independently landed at ~44-49 midpoint; my ~48 is consistent.

**L31 realization check applied to midpoint 48:**
- Opus expected avg: 48 × 0.74 = 35.5 — **UNDERFLOWS 40 floor**
- Gemini expected avg: 48 × 0.70 = 33.6 — **UNDERFLOWS 40 floor**

**Realization rates were derived from THIS TASK's prior REDO cycle** (Opus 37.5/Gemini 35.5 realized against a projected 50.5 midpoint), so they are highly load-bearing here. If applied to HARDNESS's optimistic 57.5: Opus 42.6 / Gemini 40.3 — both clear 40 with narrow margins. If applied to my ~48: both underflow. **The truth is likely between.** S2 policy escape hatch is the correct call for this REDO band, but the risk is real and mandatory S4 attention on realized Gemini avg is non-negotiable.

**Per-lever call breakdown:**

| Lever | Calls attributable | Notes |
|---|---|---|
| L1 Latching | 4 (search_records + list_issues x2 + Airtable field read) | Amplifier: R13 preservation forces Airtable pre-read |
| L8 Multi-link chain + Bennett verify | 15 (3 get_issue + 3 list_comments + 3 save_comment + 3 save_issue state flip + Airtable + Slack + Gmail chain hooks) | Largest lever contribution |
| L9 Parameter gotcha | 3 (retry loops per StarPM param traps) | Only fires on wrong-first-try |
| L25 Existing-output anchor | Overlaps L1 — 2 extra Airtable re-reads | |
| L26 Decoy parent thread | 4 (Gmail get_thread canonical + 2 decoys + Slack read_channel) | R18/R21 rubric coverage |
| Base discovery | 4 (contacts x4) | Sandra lookup amplifier |

**Structural support for 50+ midpoint:** the rubric set supports up to ~57 tool calls IF Opus consistently performs the L1/L25 verification pattern (Airtable re-read after latching). It does not; realized behavior clusters around 40-49. Structural PASS in theory; empirical THIN in practice.

**Verdict:** THIN_DENSITY, allowed per v21 policy with S1.5 HARDNESS justification (L6 dropped, residual 5-lever set inherently supports 44-52). NOT a Council B blocker. Mandatory S4 attention flag on Gemini density realization carries forward.

---

## B4. Hardness Lever Coverage

| Lever | Covering rubric(s) | Rationale |
|---|---|---|
| **L1 Latching (Airtable selReady anchor)** | R10, R11, R12, R13, R14, R15, R16 | Agent that latches on "selReady = nothing to do" fails the full Airtable append cluster. R13 (preservation) specifically requires pre-read, breaking the latching short-circuit. |
| **L8 Multi-link chain (3 Linear + Airtable + Slack + Gmail + Calendar)** | R1-R9 (Linear), R10-R16 (Airtable), R17-R19 (Gmail), R20-R23 (Slack), R24-R26 (Calendar) | Every link of the chain has ≥ 1 write-action rubric. Skipping any tool leaves at least one 1.1 failing. |
| **L9 StarPM parameter gotcha** | R10 (Airtable camelCase), R17 (Gmail draft-only, `body` not `content`), R20 (Slack `message` not `payload` — write must have succeeded), R1/R4/R7 (Linear `save_comment(issueId, body)`) | Wrong param shape → tool call errors → no successful write → 1.1 rubric fails at the tool-call layer. |
| **L25 Existing-output anchor (selReady pre-declares Ready)** | R10, R13 in particular | R13's "preserves existing narrative" claim is unsatisfiable without pre-read + append; the anchor trap fails at R10 (no write at all) OR at R13 (overwrote existing). |
| **L26 Decoy parent thread (6/16 FAIL vs 6/18 CLOSEOUT parents in both Slack and Gmail)** | R18 (Gmail thread b8e4d0a3f2c5b9e7 via replyToMessageId d0e6f2c5b4a70b19), R21 (Slack thread_ts 1781788320.000202) | Direct thread-anchor rubrics with explicit fail-if-decoy language in evidence field. These are the two Moderate-flagged rubrics in B1 — the tension is intended-discrimination vs prompt-literal-scope. |

**All 5 preserved levers have Outcome rubric coverage.** L6 correctly absent (post-S1.5 removal).

---

## B5. Forward + reverse coverage map

### Forward (prompt sentence → OE step → rubric)

| Prompt ask | OE step | Rubric(s) | Status |
|---|---|---|---|
| "get each ticket moved through my sign and out of my queue" | OE17-22 | R1, R3, R4, R6, R7, R9 | ✓ |
| "with the pass called out for each item, not a blanket close" | OE17, OE19, OE21 | R2, R5, R8 | ✓ |
| "Pull his note off each ticket ... item he's writing up actually matches" | OE13-15 (Bennett verify) | Implicit in R2/R5/R8 (per-item content requires knowing Bennett's item) | Soft coverage — L8 amplifier; strengthens L8 chain via prompt-visible discipline. Acceptable per "tighten Outcome first" — Bennett-verify's payoff is that R2/R5/R8 content correctness requires having read his comment. |
| "Pull the make-ready record on 3C and get my second-pass sign-off written into it" | OE23 | R10 | ✓ |
| "My name" | OE23 | R11 | ✓ |
| "the re-inspection date" | OE23 | R12 | ✓ |
| "one line per punch item" | OE23 | R14, R15, R16 | ✓ (three atomic 1.2s) |
| "Read what's already sitting in the notes so my sign-off reads as a continuation" | OE8 + OE23 | R13 | ✓ |
| "Carlos needs an email from us that 3C is clear" | OE25 | R17 (to Carlos), R19 (body) | ✓ |
| "Copy Brooke" | OE25 | R17 (cc Brooke) | ✓ |
| "Keep it short, hand-off not a report" | OE25 | Implicit in R19 "(or similar hand-off phrasing)" | ✓ (soft) |
| "Post in the #make-ready channel" | OE27 | R20 | ✓ |
| "the formal close is done and 3C is live for showings" | OE27 | R23 | ✓ |
| "tag Sandra so leasing sees it" | OE27 | R22 | ✓ |
| "Check the calendar for any 3C showings booked between now and next Wednesday" | OE28 | **NO RUBRIC** (null-tolerant read; folded implicitly into R25 pre-tour timing) | Acceptable gap — check is instrumental, not deliverable. Optional Process candidate (see PROPAGATE). |
| "set me a reminder for Friday morning to spot-check 3C's fridge and oven interiors" | OE29 | R24, R25, R26 | ✓ |
| "before whichever tour hits earliest" | OE29 | Implicit in R25 (07:00-10:00 CT window) | ✓ (soft) |

**Forward gaps:** none blocking. Calendar-window check has no direct rubric but is null-tolerant and folded into R25 timing.

### Reverse (rubric → prompt sentence)

| Rubric | Traces to prompt | Status |
|---|---|---|
| R1-R9 | L5 "get each ticket moved through my sign ... pass called out for each item" | ✓ |
| R10 | L7 "Pull the make-ready record on 3C and get my second-pass sign-off written into it" | ✓ |
| R11 | L7 "My name" | ✓ |
| R12 | L7 "the re-inspection date" | ✓ |
| R13 | L7 "Read what's already sitting in the notes so my sign-off reads as a continuation" | ✓ |
| R14, R15, R16 | L7 "one line per punch item" | ✓ |
| R17 | L11 "Carlos needs an email from us ... Copy Brooke" | ✓ |
| **R18 (Gmail threading exact IDs)** | L1 "Brooke's followed up since" + L11 "loop closed" (implicit continuation, NOT literal threading ask) | **Reverse surplus / weak** — see B9 |
| R19 | L11 "3C is clear so leasing can start today ... hand-off, not a report" | ✓ |
| R20 | L13 "Post in the #make-ready channel" | ✓ |
| **R21 (Slack thread_ts exact)** | L1 "Brooke's followed up since" (implicit only; L13 says only "Post in the #make-ready channel") | **Reverse surplus / weakest** — see B9 |
| R22 | L13 "tag Sandra so leasing sees it" | ✓ (tag semantics = @-mention with user id) |
| R23 | L13 "the formal close is done and 3C is live for showings" | ✓ |
| R24 | L15 "set me a reminder" ("me" = Jaime) | ✓ |
| R25 | L15 "Friday morning ... before whichever tour hits earliest" | ✓ |
| R26 | L15 "spot-check 3C's fridge and oven interiors" | ✓ |

**Reverse surplus:**
- R18 (Gmail threading): prompt has implicit-continuation support but no literal threading ask. Marginal.
- R21 (Slack threading): prompt has NO explicit or implicit threading ask; L13 is purely open ("Post in the #make-ready channel"). Weakest reverse trace of the set.

Both are lever-preserving (L26). See B8 + B9 for adversarial-alt-path analysis.

---

## B6. Process re-test

**Missing Process candidates:**

| Candidate | Three-condition test | Verdict |
|---|---|---|
| Bennett per-ticket verify before comment | Cond 1 ✓, Cond 2 partial (R2/R5/R8 give strong-but-not-airtight signal), Cond 3 ✓ | **Do not add** — Outcome R2/R5/R8 sufficient; "tighten Outcome first" rule applies. |
| Airtable pre-read before append | Cond 1 ✓, Cond 2 ✗ (R13 preservation cannot be satisfied without pre-read), Cond 3 ✓ | **Do not add** — R13 already forces the pre-read. |
| Calendar-window check before reminder | Cond 1 ✓, Cond 2 ✓ (null-tolerant read; no Outcome captures a null check), Cond 3 ✓ | **Optionally add** — genuinely three-condition-qualifying; adding "The Agent checks Jaime's calendar for 3C showings between 2026-07-01 and 2026-07-08 before creating the Friday reminder" would strengthen coverage. NOT a blocker — R25 morning window folds in the pre-tour timing intent. See PROPAGATE section. |

**Verdict: zero process is CORRECT** for the two blocked candidates (Bennett-verify, Airtable-preread). Calendar-window is a defensible optional add, flagged as PROPAGATE-TO-S3 not-blocking.

---

## B7. Cross-artifact consistency

Per-rubric verification against OEs + universe atoms (Verification_s2 attests atoms are grounded in Universe_Split):

| Rubric | OE alignment | Universe atom check | Prompt-vs-Rubric action alignment | Verdict |
|---|---|---|---|---|
| R1 | OE17 (issueId OPS-224, `save_comment`) | ✓ | Agent action, correct actor | ✓ |
| R2 | OE17 "must reference the baseboard specifically" | ✓ | ✓ | ✓ |
| R3 | OE18 (state_OPS_4 Done) | ✓ state_OPS_4 confirmed in OE16 | ✓ | ✓ |
| R4 | OE19 (OPS-225) | ✓ | ✓ | ✓ |
| R5 | OE19 "appliance interiors specifically" | ✓ | ✓ | ✓ |
| R6 | OE20 (state_OPS_4) | ✓ | ✓ | ✓ |
| R7 | OE21 (OPS-226) | ✓ | ✓ | ✓ |
| R8 | OE21 "towel ring specifically" | ✓ | ✓ | ✓ |
| R9 | OE22 (state_OPS_4) | ✓ | ✓ | ✓ |
| R10 | OE23 (baseId appPropertyOps, tableId tblMakeReady, recordId rec291f423370e2a2db, fldNotes2) | ✓ | ✓ | ✓ |
| R11 | OE23 "naming Jaime Salinas" | ✓ Jaime = persona | ✓ | ✓ (see B8 for Minor over-strict flag) |
| R12 | OE23 "2026-06-18" | ✓ | ✓ | ✓ |
| R13 | OE23 "existing narrative ... plus a new second-pass signoff line" + "preserve the existing supervisory line" | ✓ | ✓ | ✓ |
| R14, R15, R16 | OE23 "one confirmation line per punch item" | ✓ | ✓ | ✓ |
| R17 | OE25 (to carlos.mendez, cc brooke.phillips) | ✓ contact atoms confirmed | ✓ (agent drafts on Jaime's behalf) | ✓ |
| R18 | OE25 (replyToMessageId d0e6f2c5b4a70b19, thread b8e4d0a3f2c5b9e7) | ✓ | ✓ | ✓ structurally; over-specific per B8/B9 |
| R19 | OE25 "QC-passed as of 6/18 and leasing can activate showings today" | ✓ | ✓ | ✓ |
| R20 | OE27 (channel_id C004) | ✓ C004 = #make-ready confirmed | ✓ | ✓ |
| R21 | OE27 (thread_ts 1781788320.000202) | ✓ | ✓ | ✓ structurally; over-specific per B8/B9 |
| R22 | OE27 ("<@UADB2B4E045>") | ✓ Sandra's Slack id confirmed | ✓ | ✓ |
| R23 | OE27 "formal close is done ... unit is live for showings" | ✓ | ✓ | ✓ |
| R24 | OE29 (calendarId jaime.salinas@starpm.com) | ✓ | ✓ ("me" = Jaime = persona) | ✓ |
| R25 | OE29 "Friday morning 2026-07-03 ... morning slot" | ✓ 2026-07-03 = Friday, universe today 2026-07-01 Wed | ✓ | ✓ structurally; 07:00-10:00 window is Minor tight (see B8) |
| R26 | OE29 "summary that names Las Vistas 3C and the fridge and oven interior spot-check" | ✓ | ✓ | ✓ |

**Zero cross-artifact mismatches.** All 26 rubric literals ground back to OE + universe atoms. All 10 write actions correctly attributed to the Agent (no user-action misattribution per Evals_starpm 3_Rubrics_Eval Prompt-vs-Rubric hard gate).

---

## B8. Adversarial alt-path (per-flagged-rubric)

**R18 — Gmail threading exact IDs (Moderate — Overly Specific)**

Verbatim: *"The Agent's Gmail draft to Carlos threads under Brooke's 6/18 closeout package thread (Gmail thread b8e4d0a3f2c5b9e7 via replyToMessageId d0e6f2c5b4a70b19)."*

Valid alt-path that fails R18: Agent drafts a NEW email to `carlos.mendez@starpm.com` (cc `brooke.phillips@starpm.com`) with subject "Las Vistas 3C — QC clear, leasing can activate" and body matching R19. This satisfies prompt L11 literally ("Carlos needs an email from us that 3C is clear ... Copy Brooke") but fails R18 because no `replyToMessageId` is set. Per V4 severity taxonomy, "Overly Specific" is Moderate July 2026: the rubric fails a valid alternative solution path. The prompt's continuation cues ("Brooke's followed up since", "loop closed") are implicit, not literal.

**R21 — Slack thread_ts exact value (Moderate — Overly Specific)**

Verbatim: *"The Agent's Slack post in #make-ready is threaded under Brooke's 6/18 closeout-request parent (thread_ts 1781788320.000202)."*

Valid alt-path that fails R21: Agent posts a top-level message in `#make-ready` (channel_id C004) tagging `<@UADB2B4E045>` with body matching R23. This satisfies prompt L13 literally ("Post in the #make-ready channel that the formal close is done and 3C is live for showings, and tag Sandra"). Prompt L13 has NO threading ask, explicit or implicit. R21 is the weakest-grounded rubric in the set.

**R11 — Jaime Salinas by name (Minor)**

Verbatim: *"The Agent's Airtable second-pass signoff on rec291f423370e2a2db attributes the entry to Jaime Salinas by name."*

Alt-path: an append signed "— Jaime" (first name only, matching voice profile formality 0.55 / verbosity 0.30) fails literal "Jaime Salinas by name". Recommend adding "(or similar first-name attribution)" OR leaving as-is if strict full-name attribution is intentional for post-append record readability.

**R25 — Friday 07:00-10:00 CT window (Minor)**

Verbatim: *"The Agent's calendar reminder lands on Friday 2026-07-03 in the morning window (between 07:00 and 10:00 America/Chicago)."*

Alt-path: agent schedules 10:30 CT — arguably still "morning" per common usage; fails hard cutoff at 10:00. Defensible for pre-tour logic (showings typically start 10 AM+), but 10:00 upper bound is slightly tight. Minor.

**R22 — Sandra tag `<@UADB2B4E045>` (NO ALT-PATH — exact-match justified)**

Structured field, correct-value semantics. Slack `@mention` notification routing requires user-id wrapper; plain-text "Sandra" or "@Sandra" does NOT ping her. Prompt L13 "tag Sandra so leasing sees it" — the "so leasing sees it" is dispositive: notification routing is the ask, and only `<@USER_ID>` achieves it. Exact-match is aligned with the prompt's outcome ask.

**R17, R20, R24 — Structured recipients / channel / calendar (NO ALT-PATH — exact-match justified)**

Emails, channel_id, calendar_id are single-correct-value structured fields per V4 spec. Exact match required.

---

## B9. Adversarial reverse-coverage

Only two rubrics fail the strict reverse-trace check (rubric → literal prompt ask):

**R18 (Gmail threading):** prompt L1 "Brooke's followed up since" + L11 "loop closed" provide IMPLICIT continuation context, but no literal ask for `replyToMessageId`. Marginal reverse trace. Moderate.

**R21 (Slack threading):** prompt L13 is fully open ("Post in the #make-ready channel"). NO literal or implicit threading ask. Weakest reverse trace of the 26. Moderate.

All other 24 rubrics have direct literal or clear implicit prompt traces (see B5 forward+reverse table).

**Design tension:** R18 and R21 exist to enforce the L26 decoy-parent-thread lever, which is one of the 5 preserved hardness levers post-S1.5 revision. Loosening either loses L26 discrimination on that comms channel. This is not a rubric-quality defect per se — it is a prompt-vs-rubric alignment gap that must be resolved at S1 (add threading language) OR accepted as lever-preservation-with-Moderate-risk. Preferred fix: PROPAGATE-TO-S1.

---

## B10. Adversarial atomicity

| Rubric | Distinct claims | Same tool call? | Verdict | Notes |
|---|---|---|---|---|
| R1 | 1 (comment posted on OPS-224) | — | Atomic ✓ | |
| R2 | 1 (baseboard reference) | — | Atomic ✓ | |
| R3 | 1 (state = state_OPS_4) | — | Atomic ✓ | |
| R4-R9 | Mirror R1-R3 | — | Atomic ✓ | |
| R10 | 1 (Airtable update to fldNotes2) | — | Atomic ✓ | |
| R11 | 1 (Jaime name attribution) | — | Atomic ✓ | |
| R12 | 1 (2026-06-18 date) | — | Atomic ✓ | |
| R13 | 1 (preservation of existing narrative) | — | Atomic ✓ | |
| R14 | 1 (baseboard line) | — | Atomic ✓ | |
| R15 | 1 (appliance interiors line) | — | Atomic ✓ | |
| R16 | 1 (towel ring line) | — | Atomic ✓ | |
| R17 | 2 bundled (to Carlos, cc Brooke) | Same `create_draft` call — allowed per V4 July 2026 rule ("email sent to A, B, C" is send-atomic per send action; a single draft with multiple recipients IS a single send) + Reference/Rubric_Format.md line 30 | Atomic ✓ | S2 PROPAGATE flag honored — do NOT split cc into separate 1.1 |
| R18 | 1 (threading atom — thread_id + replyToMessageId are the same threading concept) | Same `create_draft` call | Atomic ✓ | |
| R19 | 2 bundled (QC-cleared + leasing activate today) | Same email body | Atomic ✓ | Prompt L11 bundles both in one sentence; content-atomic |
| R20 | 1 (post in C004) | — | Atomic ✓ | |
| R21 | 1 (thread_ts value) | — | Atomic ✓ | |
| R22 | 1 (Sandra `<@UADB2B4E045>` tag) | — | Atomic ✓ | |
| R23 | 2 bundled (formal close done + live for showings) | Same message body | Atomic ✓ | Prompt L13 bundles both in one sentence; content-atomic |
| R24 | 1 (event on Jaime's calendar) | — | Atomic ✓ | |
| R25 | 2 bundled (Friday 2026-07-03 + 07:00-10:00 CT) | Same event startTime/endTime | Atomic ✓ | Time-atomic |
| R26 | 2 bundled (Las Vistas 3C + fridge/oven) | Same summary/description | Atomic ✓ | Reminder-self-explanation-atomic |

**S2 PROPAGATE-TO-S3 flags honored (all 4):**
- (a) Multi-atomic 1.2s on Airtable: R11 + R12 + R13 + R14 + R15 + R16 = **6 atomic pieces** ✓
- (b) Multi-atomic 1.2s on Slack: R21 + R22 + R23 = **3 atomic pieces** ✓
- (c) NO cc-recipient split on Gmail: R17 = **single 1.1 covers both to+cc** ✓
- (d) Friday-morning window (R25 = 07:00-10:00 CT, not exact clock time): ✓

Zero atomicity violations.

---

## B11. Adversarial entity-swap (O4)

For every rubric that names a specific person alongside a workstream label, checked whether a DIFFERENT person in the universe could plausibly be attributed:

**R11 (Jaime Salinas attribution on Airtable append):**
- Brooke Phillips: her retrospective supervisory sign-off is ALREADY the pre-existing narrative in fldNotes2 (OE8 confirms). Jaime's second-pass ACTIVE signoff is distinct — prompt L7 explicitly separates them ("not just Brooke's supervisory note"). Distinctness verified in universe.
- James Bennett: maintenance tech doing rework, NOT the QC signoff (persona role separation per StarPM personas).
- Only Jaime is the QC Inspector persona. **Not ambiguous.** ✓

**R17 (Carlos primary + Brooke cc on Gmail):**
- Denise Morales: appears in Brooke's canonical Gmail body as the leasing-side requester ("Denise is asking whether leasing can activate showings") — she is the DEMAND signal, not the OPERATIONAL hand-off recipient. Prompt L11 explicit: "Carlos needs an email from us".
- Sandra Allen: leasing agent, handled via Slack tag (R22), not Gmail cc.
- Carlos = Onsite Property Manager per contacts + persona briefs. Correct operational hand-off recipient. **Not ambiguous.** ✓

**R22 (Sandra Allen Slack tag):**
- Prompt L13 explicit: "tag Sandra". Named directly.
- Other Leasing Agents in the universe (Kevin Okafor, Alicia Vega, Maria Lopez, per HARDNESS L6 note where Kevin is referenced) — none named in prompt; Sandra is the only person named. Sandra's Slack user id UADB2B4E045 confirmed in Universe_Split.
- **Not ambiguous.** ✓

**R24 (Jaime's calendar for reminder):**
- Prompt L15 "set me a reminder" — "me" = Jaime (persona voice, first-person). Not ambiguous with any other calendar owner. ✓

All person-linked rubrics correctly attributed. Zero O4 (entity-swap) ambiguities.

---

## Blocking issues (Major + Moderate)

1. **R21 (Moderate — Overly Specific) — Slack thread_ts lock-in.**
   - Verbatim: *"The Agent's Slack post in #make-ready is threaded under Brooke's 6/18 closeout-request parent (thread_ts 1781788320.000202)."*
   - Prompt L13 is fully open on the Slack side ("Post in the #make-ready channel"). NO literal or implicit threading ask. Fails a valid alt-path (top-level tagged post with correct content).
   - Lever-preservation tension: this rubric is the entire L26 discriminator for the Slack channel.
   - Preferred fix: PROPAGATE-TO-S1 — add threading language to prompt (e.g., "under Brooke's morning ping"). Alternative: loosen R21 to accept correct-audience-routed post, but this deletes L26 Slack coverage.

2. **R18 (Moderate — Overly Specific) — Gmail thread lock-in.**
   - Verbatim: *"The Agent's Gmail draft to Carlos threads under Brooke's 6/18 closeout package thread (Gmail thread b8e4d0a3f2c5b9e7 via replyToMessageId d0e6f2c5b4a70b19)."*
   - Prompt L1 + L11 give implicit continuation context ("Brooke's followed up since", "loop closed") but no literal `replyToMessageId` ask. Fails a valid alt-path (fresh email to Carlos+Brooke with correct content).
   - Marginal — implicit prompt support is stronger than R21's.
   - Preferred fix: PROPAGATE-TO-S1 — same fix as R21. Add threading language.

---

## Non-blocking observations (Minor)

1. **R11 — "Jaime Salinas by name" has no `(or similar)` qualifier.** An append signed "— Jaime" (first-name-only, consistent with Jaime's voice profile) would fail literal reading. Consider adding "(or similar first-name attribution)" if operator wants voice-consistent alt-paths preserved. Not blocking.

2. **R25 — 07:00-10:00 CT window is slightly tight.** A 10:30 slot is arguably still "morning". Upper cutoff at 10:00 is defensible for pre-tour logic (showings typically 10 AM+) but rubric wording could accept up to 11:00 without losing discriminative value. Not blocking.

3. **Calendar-window read (OE28) has no direct rubric.** Null-tolerant instrumental check; folded into R25 morning-window Outcome. Genuinely three-condition-qualifying Process candidate exists; not required. See PROPAGATE.

4. **B3 THIN_DENSITY midpoint ~48 with narrow Gemini realized-margin.** Not a rubric defect — it is a HARDNESS-level structural ceiling on the post-S1.5 5-lever set. S4 attention mandatory on Gemini realized avg; if < 40, PIPELINE REDO triggers.

---

## PROPAGATE-TO-S1 or PROPAGATE-TO-S2 flags

**PROPAGATE-TO-S1 (preferred fix for the 2 Moderate blockers):**

Add explicit threading language to the R5 prompt so R18 and R21 stop being reverse-surplus:

- Gmail (near prompt L11): add "reply on Brooke's closeout thread" or "on Brooke's follow-up email" so the threading discipline becomes a literal ask.
- Slack (near prompt L13): add "under Brooke's morning ping" or "on the closeout thread Brooke opened" so the threading discipline becomes a literal ask.

Estimated impact: prompt gets +6-10 words (well under the 500-word cap). Post-S1 re-run cost: full S1 → S1.5 (linter re-check) → S2 (OE alignment re-check — likely minimal since OE24/25/26/27 already encode threading) → S3 (rubric re-check — R18/R21 become fully-aligned, Moderate downgrades to non-fail).

**Alternative (not preferred):** loosen R18/R21 to accept correct-audience-routed alternatives. This deletes L26 discrimination on that comms channel; task loses hardness on the Slack/Gmail decoy-parent lever.

**PROPAGATE-TO-S3 (optional, non-blocking):**

Consider adding one Process rubric for the calendar-window read to close the soft coverage gap on prompt L15 "Check the calendar for any 3C showings between now and next Wednesday":

- Suggested: *"The Agent checks Jaime's calendar for 3C showings between 2026-07-01 and 2026-07-08 before creating the Friday morning reminder."*
- Three-condition test: all three PASS (required by every valid path, no Outcome captures null-tolerant read, behavioral not tool-trace).
- This would break the "zero process rubrics" pattern currently held across all 4 V3 reference tasks and this task. Defensible either way. Non-blocking.

**PROPAGATE-TO-S2:** none.

**PROPAGATE-TO-HARDNESS:** none. HARDNESS S1.5 revision is stable; the density projection tension is honest structural ceiling on the residual 5-lever set post-L6 removal, and S2 has already invoked the THIN_DENSITY policy escape correctly.
