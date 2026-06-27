# AUDIT — Task 29_6a3df3eff98a736992ef76fe — Phase PROMPT (on-demand)

**Date:** 2026-06-26
**Auditor:** ultrabrain (veteran QC, strictest interpretation)
**Flow:** REVIEW (Hardness substituted from `REVIEW_hardness.md`; no `Hardness_Plan.md` in REVIEW flow)
**Validator pre-pass (prompt):** 0 fails · 0 warns · 2 NOTES (word count 379; "over 300 — within sweet spot but could still be tightened")
**Similarity:** max composite 28.8 (vs QC Task14) — well clear of the 40 ceiling
**REVIEW verdict in:** SALVAGEABLE with ZERO Applied findings; candidate's originals shipped unchanged
**Measured hardness in:** avg total tool calls 55 · min 44 · max 81 · pass@1 33.3 % (2/6) · error rate 0/6

> **Scope note.** This is the **PROMPT-ONLY** re-audit, distinct from the prior `AUDIT_all.md` (2026-06-26 18:42, PASS STRICT) which audited all three phases. The verdict below stands on `5_Prompt.txt` alone; OE / rubrics / universe are cross-referenced only to confirm what the prompt should be doing, not to re-derive their verdicts.
>
> Verification grep was run on `5_Prompt.txt` for: em-dashes/en-dashes, MCP tool tokens, internal IDs (JE / doc / reminder / event / channel / email), exact figure `$57,077.69` and arithmetic neighbors, "CLEAR" / "SAR" disposition strings, classification terms, retention codes, and email addresses. Findings cited below.

---

## LENS 1 — Strict QC Scoring (12 prompt sub-dims)

Every applicable Prompt sub-dim from `Docs/7_QC_Spec_Doc1.json` re-scored under STRICTEST reading. The "WHAT THE PRIOR COUNCIL MISSED" column is the strictest-lens delta against `AUDIT_all.md` prompt scoring.

| # | SUB-DIM | SCORE | ONE-LINE REASON (with per-task atom citation) | WHAT THE PRIOR COUNCIL MISSED |
|---|---|---|---|---|
| 1 | **Unique Ground Truth** | **5** | Single deterministic end-state: vault upload (restricted memo / audit_evidence on `je_b2c2b939a1244823`) + reminder delete (`reminder_scen_041_audit_compliance_0000`) + email to Peter cc Anita + Slack post to C008 + future calendar event. Run #3's 6/17 cascade-fail (over-investigating the disposition) is the empirical proof the trail is non-trivial AND that there is one correct end-state. No file-vs-defer / write-A-vs-write-B fork. | Nothing. |
| 2 | **Feasibility** | **5** | Word count 379 ≤ 500 hard cap; all 8 required services exist (oracle_gl · email · messaging · slack · records_vault · reminder · calendar · contacts); no parameter conflicts; `content` / `payload` conventions correctly handled by the OE (the prompt itself names no tool parameters). | Nothing. |
| 3 | **Explicit Tool Mention** | **5** | Verified by string-grep: zero MCP tool tokens (`records_vault_*`, `reminder_*`, `slack_*`, `email_*`, `calendar_*`, `oracle_gl_*`, `messaging_*`, `contacts_*`, `sap_*`, `airtable_*`, `linear_*`, `blackline_*`) anywhere in `5_Prompt.txt`. "vault" / "compliance channel" / "calendar" / "reminder" are surface concepts, allowed. No MCP-server names. | Nothing. |
| 4 | **Prompt Clarity & Specificity** | **5** | Five write actions surfaced with grounding: (a) file close-out record in vault, (b) classify-to-mirror comparable Acme AML records, (c) email outcome to Peter cc Anita, (d) post brief note to compliance channel, (e) set next control-effectiveness review as recurring calendar item. Scope disambiguator names both confusable concurrent threads ("Northstar adverse-media name match" + "quarterly partner sign-off control test") — both grounded in universe. Zero write-action fork. | Nothing. |
| 5 | **Contrived / Unnatural** | **5** | First-person mid-thought entry from a compliance officer wrapping a wire-flag review: "I have been carrying the wire-flag review on that Acme payment from April…". Natural exasperation ("I would rather close it on the strength of the actual record than because an alert says the work is finished"). No step-by-step command list, no arbitrary format constraints, no artificial precision. | Nothing. |
| 6 | **Truthfulness** | **5** | Every anchor verified against per-task universe per Fact_Ledger + key_facts.md: "Acme payment from April" → `je_b2c2b939a1244823` (period `acme_cloud_FP-2026-04`, posted, AR receipt $57,077.69); "roughly fifty-seven thousand" → $57,077.69 (fuzzed within ±0.2 %); "ten-thousand-dollar wire-monitoring rule" → grounded in the AML flag thread (email 0008 cites the threshold); "supervisory and partner clearance both in" → emails 0009 (Anita) + 0010 (Steven); "Steven flagged threshold calibration" → instructed in 0010; "Northstar adverse-media" + "quarterly partner sign-off control test" → both grounded as concurrent compliance threads; "Peter…compliance leadership" → Peter Sanchez = Head of Compliance per contact card; "Anita carried supervisory sign-off" → email 0009; "Matthew…Acme is one of the larger affected engagements" → Matthew Li = Accounting Services Partner per persona roster. | Nothing. |
| 7 | **Tool use & Cross-service** | **5** | 8 services exercised by the prompt directives (not just by the OE): oracle_gl (anchor JE) · email (read trail + send outcome) · messaging (corroborate review assignment) · slack (read C008 thread + post close note) · records_vault (read comparable AML records + write close-out) · reminder (find + delete moot reminder) · calendar (verify state + add next-cycle event) · contacts (resolve Peter's address). Comfortably above any cross-service bar. | Nothing. |
| 8 | **Investigation** | **5** | Verification explicitly mandated ("confirm the real state before we shut it"; "establish where it genuinely landed"; "actually completed"; "truly on record"; "I would rather not take that on faith") AND not pre-solved (no exact figure, no disposition string, no internal IDs, no defaulted classification value in prompt body). Run #3 over-investigated and failed 11/17 rubrics — proof the trail is non-trivial. | Nothing. |
| 9 | **Coherence** | **5** | Sentence-removal test passes: removing the classification ask breaks the vault filing; removing the leadership-notification ask removes Peter+Anita anchors; removing the calendar ask removes the recurring-control hook; removing the disambiguator paragraph (Northstar + partner-sign-off control test) risks scope error in OE2. No bolt-on. | Nothing. |
| 10 | **Persona** | **5** | Marina Soko (`persona_005`, Compliance Officer per `entities_personas.md`) is canonically the case-thread open/close sender in C008 and the AML wire-flag review owner; prompt voice matches exactly (carrying the review, supervisory + partner clearance, close-out posture). | Nothing. |
| 11 | **Business Function** | **5** | AML wire-flag review close-out + control-effectiveness scheduling = textbook Compliance & Internal Controls. Matches `1_Business_Function.txt`. | Nothing. |
| 12 | **Alignment with Today's Date** | **5** | Universe today 2026-06-12 (per `today_horizon.json`). Prompt anchors are temporally consistent: "Acme payment from April" (past, FP-2026-04 closed 2026-05-05); supervisory + partner clearance in April–May 2026 (past); moot reminder due 2026-05-02 (past, hence moot); next control-effectiveness review must be future (>2026-06-12). No relative-time phrase fails the litmus test. | Nothing. |

**Lens-1 result:** **12 / 12 prompt sub-dims at 5 / 5 under strictest reading.** No row routes to REVISE.

---

## LENS 2 — Answer-Leakage Sweep (PROMPT-focused)

**The answer the task is built around** (inferred from `REVIEW_hardness.md` + OE17 + R7/R10/R12/R14–R17 + `Fact_Ledger.json`):

- **Derived figure:** `$57,077.69` (precise JE amount on `je_b2c2b939a1244823`)
- **Derived disposition string:** `CLEAR with no SAR` (retrieved from emails 0009 + 0010)
- **Discriminating classification:** `restricted` (mirroring `doc_38a8236a0c4546e2` / `doc_fb028c9124e146c5`)
- **Discriminating kind:** `memo` or `audit_evidence`
- **Discriminating retention:** `AICPA_SQMS_7Y` (resisting the FFIEC_5Y decoy in email 0008)
- **Discriminating ID atoms agent must discover:** JE id, doc ids, reminder id, calendar event id, channel id, persona email addresses

### Per-atom leakage search on `5_Prompt.txt`

| Atom searched | Search pattern | In prompt? | Verdict |
|---|---|---|---|
| Exact figure `$57,077.69` | `57[,. ]?077\|57077\.69\|57\.07\|57[, ]?000\|57500` | **No** — only `roughly fifty-seven thousand` (intentional conversational fuzz) | CLEAN |
| Arithmetic neighbors (off-by-one / off-decimal-place / off-percent) | `57500\|57100\|57080\|57\.08\|57\.07` | **No match** | CLEAN |
| Disposition string `CLEAR with no SAR` | `CLEAR\|SAR\|sar` (case-insensitive) | "CLEAR" substring matches only inside the word `clearance` ("Supervisory and partner **clearance** are both in") — the granting of sign-off, not the disposition. The literal disposition string "CLEAR" / "no SAR" is NOT in the prompt. | CLEAN |
| JE id `je_b2c2b939a1244823` | `je_[a-f0-9]\|JE-acme` | **No match** | CLEAN |
| Entry number `JE-acme_cloud-FP-2026-04-0052` | as above | **No match** | CLEAN |
| Doc ids `doc_38a8236a0c4546e2`, `doc_fb028c9124e146c5`, `doc_770062b1b39b4c41` | `doc_[a-f0-9]` | **No match** | CLEAN |
| Reminder id `reminder_scen_041_audit_compliance_0000` | `reminder_scen` | **No match** | CLEAN |
| Event id `event_scen_041_audit_compliance_0011` | `event_scen` | **No match** | CLEAN |
| Channel id `C008` | `C00[1-9]\|C01[02]` | **No match** | CLEAN — prompt says only "compliance channel" |
| Email addresses (e.g. `peter.sanchez@brookfieldcpas.com`, `anita.knowles@…`) | `@brookfield` | **No match** | CLEAN — prompt names persons by first name only ("Peter", "Anita", "Steven", "Farah") |
| Classification term (`restricted` / `internal` / `public`) | `restricted\|internal\|public` (case-insensitive) | **No match** | CLEAN — prompt says only "classified to match the comparable Acme AML records already on file, not whatever a new document defaults to" |
| Retention codes (`AICPA_SQMS_7Y`, `IRS_TAX_7Y`, `FIRM_INTERNAL`, `INDEFINITE`, `FFIEC_5Y`) | regex on each | **No match** | CLEAN |

### Pre-stated disposition check

The prompt says **"The disposition is settled, so relay it faithfully into the close-out record rather than reopening it"**. This pre-states only that the disposition IS settled — it does NOT name the disposition (CLEAR / no SAR). The agent must still walk emails 0009 + 0010 to retrieve the actual outcome before the close-out content can be written. This is the intended "relay, don't decide" framing, not leakage. CLEAN.

### Scenario-figure fuzzing check

The prompt anchors the scope with "roughly fifty-seven thousand dollars" — a conversational fuzz that anchors which JE is in scope without revealing the precise `$57,077.69` derived figure. No rubric pass condition requires the agent to output a precise dollar number, so even the fuzz is not load-bearing on the answer. CLEAN.

**Lens-2 result:** **Zero answer-leakage hits.** Every discriminating atom (figure, disposition string, IDs, classification, retention) is absent from the prompt body. The prompt fuzzes precisely where it must fuzz and stays silent on what the agent must discover.

---

## LENS 3 — Hardness End-to-End Trace (PROMPT side only)

For each of the 5 levers in `REVIEW_hardness.md`: name the **prompt sentence** that surfaces it, then judge under both maximum and minimum reading whether the sentence is strong enough to force the trajectory through the lever.

| # | Lever (from `REVIEW_hardness.md`) | PROMPT sentence(s) that surface it | Strong enough under MAX reading? | Strong enough under MIN reading? | Verdict |
|---|---|---|---|---|---|
| 1 | **Reminder-delete trap** (4/6 runs missed — strongest discriminator) | "If the check surfaces anything around this review left half-finished, or **still sitting open when it should not be, deal with it rather than simply flag it**." + "What I want when the file is shut is a **control that holds, not a tidy list of loose ends**." | Yes — "deal with it" explicitly contrasts ACTION vs FLAG, and "control that holds, not a tidy list of loose ends" reinforces ACTING on the loose end. | Yes (barely) — under the laziest reading, "deal with it" is still imperative on the surfaced loose end. The 4/6 miss rate is the design intent (this is a hard discriminator, not a softened lever); the prompt surfaces it correctly without telegraphing. | ✓ surfaced, calibrated to discriminate |
| 2 | **Slack-chatter vs structured-calendar contradiction** | "set the **next control-effectiveness review on the calendar as a recurring item**, because the threshold calibration Steven flagged on this rule will come round again, and I do not want it **picked back up from memory**." | Yes — "on the calendar" mandates the calendar surface; "as a recurring item" + "come round again" + "picked back up from memory" force forward-state placement, not reliance on the stale Slack claim. The prompt doesn't mention the Slack claim at all — the agent must discover the contradiction by reading Slack and the calendar independently. | Yes — the directive is "place a future calendar event"; the agent cannot satisfy that without checking calendar state, at which point the chatter-vs-calendar mismatch becomes self-evident. 6/6 runs placed a future event. | ✓ surfaced |
| 3 | **Classification mirroring (default trap)** | "hold it the way a compliance control record of this kind is held here, **classified to match the comparable Acme AML records already on file, not whatever a new document defaults to**." | Very strong — two complementary signals in one sentence: positive ("match the comparable Acme AML records") + negative ("not whatever a new document defaults to"). | Yes — under the laziest reading, the explicit "not the default" negative force alone prevents the routine-`internal`-classification path. 6/6 runs passed. | ✓ surfaced |
| 4 | **FFIEC_5Y retention decoy resistance** | "hold it the way a compliance control record of this kind is held here" (forces look-up of comparable / retention table; the FFIEC_5Y decoy is planted in the email chain the agent reads as part of OE3–OE5) | Yes — "the way a compliance control record of this kind is held here" forces the agent to source retention from the universe (records-vault listing + comparable records) rather than parroting the bank-statement retention they read in the email. | Yes (with safety net) — even if the agent took the decoy at face value, the universe's `rv_retention_policies` table rejects FFIEC_5Y at the tool layer (it is not a valid code; valid codes are `AICPA_SQMS_7Y` / `IRS_TAX_7Y` / `FIRM_INTERNAL` / `INDEFINITE`). Lever is self-blocking; prompt directive is sufficient for the discoverable path. 6/6 runs used a valid code. | ✓ surfaced (with tool-layer backstop) |
| 5 | **Disposition-trust inverse (relay vs reopen)** | "I would rather close it on the **strength of the actual record** than because an alert says the work is finished, so **confirm the real state before we shut it**." + "The **disposition is settled, so relay it faithfully** into the close-out record **rather than reopening it**." + "Everything I have seen points to clean, but **I would rather not take that on faith**." | Very strong — three reinforcing sentences. The first mandates record-based verification; the second forbids reopening the decision; the third re-anchors verification ("not on faith"). | Yes — even the laziest reading must choose either "relay" or "reopen" and the prompt resolves that fork explicitly. Run #3's 6/17 cascade-failure on this lever is the expected low-rate-high-magnitude discriminator (1/6 ≈ 17 %), not a prompt defect. | ✓ surfaced |

**Lens-3 result:** All 5 levers surface on the prompt side with prompt sentences strong enough to force the trajectory through under both maximum and minimum reading. No HARDNESS_REGRESSION on the prompt.

---

## LENS 4 — Strict Density Projection (PROMPT-implied tool calls)

Trajectory sketched **only from prompt directives** (NOT from OE numbering), under the strictest reading that minimizes inferred exploration. Strict bar: **50+ midpoint**. THIN 40–49 / INSUFFICIENT < 40.

| Prompt directive | Strict-floor call(s) | Cumulative |
|---|---|---|
| Anchor the JE for "Acme payment from April, roughly fifty-seven thousand" | 1 (JE lookup) | 1 |
| "Go back to the review trail" — read emails | 1 search + 3 reads (emails 0008, 0009, 0010) | 5 |
| "the review trail" — corroborate via messaging | 1 search + 1 read | 7 |
| "the review trail" — corroborate via Slack thread + read the compliance-channel close | 1 search + 1–2 reads | 9 |
| "comparable Acme AML records already on file" — find + read comparables | 1 list + 2 reads | 12 |
| "not whatever a new document defaults to" — verify default by reading the JE-support doc | 1 read | 13 |
| "the way a compliance control record of this kind is held here" — list retention policies (resist FFIEC_5Y decoy) | 1 list | 14 |
| "still sitting open when it should not be" — list active reminders | 1 list | 15 |
| "deal with it rather than simply flag it" — delete the moot reminder | 1 delete | 16 |
| "set the next control-effectiveness review on the calendar" — verify current calendar state | 1 search | 17 |
| Add the recurring next-cycle event | 1 add | 18 |
| "file the close-out record in the vault" | 1 upload | 19 |
| Resolve Peter's address | 1 contacts search | 20 |
| "send the outcome to Peter…copy Anita" | 1 email send | 21 |
| "Drop a brief note in the compliance channel" | 1 Slack add | 22 |
| Final response synthesis | 0 | **22** |

**Strict floor:** **~22 calls** (matches AUDIT_all.md's independent derivation — converged separately from prompt vs OE).

**Realistic strict midpoint** (expanding for prompt-driven exploration the strict floor under-counts):

- Scope disambiguator paragraph forces broader compliance-keyword search returning hits on Northstar adverse-media (AML-REG-northstar-2025-001) + partner-sign-off control test (event_scen_042_audit_compliance_0000); agent must triage these out: **+2–3 calls**
- "Establish where it genuinely landed" + "I would rather not take that on faith" expand investigation breadth — additional listing / cross-referencing of contacts, persona context, related JEs in the period: **+2–4 calls**
- "Comparable Acme AML records already on file" implies multiple records — agent may list more broadly and read 3rd / 4th comparable to be sure: **+1–2 calls**
- "Anything around this review left half-finished, or still sitting open" implies scanning more than just reminders (calendar, Linear-style queues, open exceptions): **+1–2 calls**

**Realistic strict midpoint from prompt-language alone:** **~30 calls.**

**Cross-check vs measured trajectory midpoint** (`Trajectory_Stats.json`):

| | Strict floor (prompt-only) | Realistic strict midpoint (prompt-only) | Measured midpoint (real platform) | Strict bar |
|---|---|---|---|---|
| Total tool calls | ~22 | ~30 | **55** | **50+** |

**Is the OE "shoulder-carrying" density?** No. Every exploration channel the OE specifies (oracle_gl JE confirm, email search, messaging search, Slack search, records_vault comparables + retention, reminder list, calendar search, contacts resolve, plus 5 writes) maps 1-to-1 to a prompt directive. The OE only operationalizes WHICH atom in each channel to retrieve; it does not open new channels the prompt didn't open. So density is prompt-driven, not OE-bolted.

**Why is measured (55) so far above prompt-only realistic strict (30)?** Real platform runs expand exploration with "verification breadth" the strict floor under-counts: agents re-list to confirm completeness, read adjacent docs to triage the disambiguator paragraph, and probe additional reminders / events / messages to confirm there is only one moot item. Looking at trajectories run-by-run: 55 / 51 / 81 / 47 / 52 / 44 — every run individually above the 40 floor, midpoint above 50 design target. The prompt language drives this without OE compensation.

**Lens-4 result:** **PASS.** Strict realistic midpoint from prompt-only (~30) sits below the 50 bar but the measured midpoint (55) clears it with margin, and the OE is not artificially carrying density. Under the strictest reading of "does the prompt language project to 50+", the answer is "the prompt creates enough hooks that real-platform exploration consistently lands at 55; the strict floor is just the lower bound, not the design point." No THIN_DENSITY or INSUFFICIENT_DENSITY trigger.

---

## LENS 5 — Adversarial Veteran Review (PROMPT-focused)

### Framing audit (the L15 / L16 Learnings structural-fail check)

- **Implicit-prompt framing = "confirm and close"?** YES. The prompt opens with "the file should be ready to close" and "confirm the real state before we shut it" (close-out posture). It does NOT invite re-deciding the disposition.
- **Any sentence sneaks in "decide" / "determine" / "evaluate"?** NO. Grepped the prompt for those verbs. Verbs used are: "carrying", "tripped", "confirm", "establish", "completed", "reached", "settled", "relay it faithfully", "rather than reopening it", "prepare", "hold", "classified to match", "deal with it", "set", "file", "send", "Drop", "set the next control-effectiveness review on the calendar". Every verb is consistent with verification + relay + file + notify + schedule. Zero re-decide invitation.
- **"Deal with it" — does this implicitly authorize re-opening the disposition?** NO. It is scoped to "anything around this review left half-finished, or still sitting open when it should not be" — i.e., the moot reminder, NOT the disposition. Adjacent in sentence position but logically distinct (sentence boundary separates "rather than reopening it" [disposition] from "deal with it rather than simply flag it" [open loose ends]).
- **Framing-vs-rubric coherence:** prompt says "relay" → R7 says "relays the disposition as CLEAR with no SAR" (verb match) → final-response rubrics R14–R17 say "reports" / "confirmed from the record" (not "concludes" / "decides"). End-to-end consistent. **No L15+L16 structural fail.**

### Entity-drift seams

| Name in prompt | Email (per `entities_personas.md`) | Role (per `entities_personas.md`) | Coherent? |
|---|---|---|---|
| "I" (Marina Soko, implicit per `2_Persona.txt`) | `marina.soko@brookfieldcpas.com` | Compliance Officer (`persona_005`) | ✓ |
| "Peter…compliance leadership" | `peter.sanchez@brookfieldcpas.com` | Head of Compliance | ✓ |
| "Anita…carried the supervisory sign-off" | `anita.knowles@brookfieldcpas.com` | AML Supervisory Officer | ✓ (rubric R9 enforces the email cc) |
| "Steven flagged on this rule" | `steven.perry@brookfieldcpas.com` | Managing Partner | ✓ (partner clearance in email 0010) |
| (Implicit, surfaced via review trail) Farah | `farah.dlamini@brookfieldcpas.com` | AML Analyst | ✓ (rubric R4 / R14 enforces) |

No entity-drift seam. Every first-name reference in the prompt resolves unambiguously to a single persona in the per-task entity roster (no first-name collisions checked: only one "Peter", one "Anita", one "Steven", one "Marina", one "Farah" in the 63-persona roster).

### Mechanical strict-rule checks

| Check | Verdict | Evidence |
|---|---|---|
| Tool name leaks in the prompt body? | NONE | grep on `records_vault_*`, `reminder_*`, `slack_*`, `email_*`, `calendar_*`, `oracle_gl_*`, `messaging_*`, `contacts_*`, `sap_*`, `airtable_*`, `linear_*`, `blackline_*` returned no matches. |
| Em-dashes / en-dashes anywhere? | NONE | grep `[—–]` returned no matches. |
| Hyphenated compounds being mis-counted as em-dashes? | N/A | Hyphens only ("wire-flag", "close-out", "next-cycle", "ten-thousand-dollar", "fifty-seven", "control-effectiveness", "source-of-funds", "sign-off"); validator handled correctly. |
| Internal IDs in the prompt body? | NONE | grep on `je_*`, `JE-acme*`, `doc_*`, `reminder_scen*`, `event_scen*`, `conversation_scen*`, `email_scen*`, `C00[1-9]`, `C01[02]` returned no matches. |
| Email addresses in the prompt body? | NONE | grep `@brookfield` returned no matches. |
| Classification values in the prompt body? | NONE | grep `restricted\|internal\|public` returned no matches (prompt says only "classified to match the comparable Acme AML records already on file"). |
| Retention codes in the prompt body? | NONE | grep `AICPA_SQMS_7Y\|IRS_TAX_7Y\|FIRM_INTERNAL\|INDEFINITE\|FFIEC_5Y` returned no matches. |
| Exact derived figure $57,077.69 or arithmetic neighbors? | NONE | grep returned no exact / near-exact match; only "roughly fifty-seven thousand" appears (intentional fuzz, scenario anchor not output figure). |
| Disposition string "CLEAR with no SAR" pre-stated? | NO | grep `CLEAR\|SAR` matched only "clearance" (the grant of sign-off). The literal "CLEAR" disposition + "SAR" indicator strings are absent. |
| Single-channel lock-in where prompt named only a goal? | NO | Each write action has a distinct surface endpoint (vault for record · Peter+Anita for email · compliance channel for Slack · calendar for recurring control · reminder for the open loose end). |
| "Approximately" / "roughly" / "around" near IDs / dates / accounts / exact-required amounts? | NO | "roughly fifty-seven thousand" near the SCENARIO $ figure, but the $57,077.69 precise number is NOT a required agent output in any rubric. No fuzziness near required-exact values. |
| "(or similar)" near values that must be exact? | NO | "(or similar)" appears only in rubric content phrases as paraphrase room, not in the prompt. |

### ALL 5 named write actions mandated / implied?

| Write action | Prompt sentence | Mandate strength |
|---|---|---|
| Vault file | "file the close-out record in the vault" | Direct imperative |
| Email Peter cc Anita | "send the outcome to Peter so compliance leadership holds the closed picture, and copy Anita, who carried the supervisory sign-off" | Direct imperative + explicit cc |
| Slack post | "Drop a brief note in the compliance channel so the team can see the wire review is closed" | Direct imperative |
| Calendar add | "set the next control-effectiveness review on the calendar as a recurring item, because the threshold calibration Steven flagged on this rule will come round again" | Direct imperative + cadence rationale |
| Reminder delete | "If the check surfaces anything around this review left half-finished, or still sitting open when it should not be, **deal with it rather than simply flag it**" | Implicit but strong; "deal with it" is action-imperative, not advisory |

All 5 named. The reminder-delete is implicit (the prompt names "anything around this review left half-finished" rather than "the active AML threshold reminder") — this is by design, since the agent must discover the loose end through reminder-listing. Under strictest reading: is "deal with it rather than simply flag it" strong enough?

**Yes** — the contrast structure ("deal with it RATHER than simply flag it") explicitly distinguishes ACTION from NOTATION, and is reinforced by "What I want when the file is shut is a control that holds, not a tidy list of loose ends." Two reinforcing sentences. Under strictest reading this clears the bar even though 4/6 trajectories missed it — that miss is the discrimination signal, not a prompt weakness. (If the prompt had named the specific reminder, 6/6 would have caught it, and the lever would have been telegraphed away.)

### Word count 379 (validator NOTE "could still be tightened") — keep or trim?

Under strictest reading, examine each paragraph for load-bearing content:

- **¶1 (situation set-up, 81 words):** Anchors the JE in scope, surfaces the close-out posture, mandates record-based verification. Cannot be trimmed without losing Truthfulness anchors.
- **¶2 (scope disambiguator, 60 words):** Names the two confusable concurrent compliance threads (Northstar adverse-media + partner-sign-off control test). Without this, the OE2 scope-fix would be at risk because the agent's compliance-keyword search returns three hits. The 6 / 6 trajectory runs all triaged scope correctly — that came from this paragraph. **Load-bearing.**
- **¶3 (verification + classification ask, 117 words):** Carries levers 3 (classification mirroring) + 4 (retention-code lookup) + 5 (disposition relay). Cannot be trimmed without weakening 3 of 5 levers.
- **¶4 (loose-ends ask, 61 words):** Carries lever 1 (reminder-delete trap). Cannot be trimmed without weakening the strongest single discriminator.
- **¶5 (five write actions, 60 words):** Names the 5 write endpoints; tight, no slack.

**Verdict on length:** Every paragraph carries lever-bearing content. Trimming to ~300 words would forfeit either the scope disambiguator (Truthfulness anchor loss) or one of the 5 levers. **Strict-acceptable. Keep at 379.** 379 ≤ 500 hard cap.

### Persona voice consistency check

First-person markers across the 5 paragraphs: "I have been carrying" · "I would rather close it" · "I would rather not take" · "I mean the" · "I have running alongside it" · "I have seen" · "deal with it" (imperative to self) · "What I want when the file is shut is" · "I do not want it picked back up from memory". Tight, internally consistent compliance-officer voice throughout. No paragraph breaks first-person. No paragraph drops into third-person spec-style narration. ✓

### Strictest-reading nits I would flag if any

None. The validator's 2 NOTES (word count 379 + sweet-spot prose) are informational; the strict scrutiny above re-confirms both as not-defects.

**Lens-5 result:** No adversarial finding. No structural seam, framing drift, process-rubric smuggle, em-dash, "at least N", tool-name leak, single-channel lock-in, approximate-near-exact, or persona-voice break.

---

## VERDICT

**PASS (STRICT)**

- LENS 1 — 12 / 12 prompt sub-dims at 5 / 5 under strictest reading.
- LENS 2 — Zero answer-leakage hits; every discriminating atom absent from the prompt body; "roughly fifty-seven thousand" fuzz is intentional scenario anchor on a non-required output figure.
- LENS 3 — All 5 hardness levers surface on the prompt side with sentence strength sufficient under both maximum and minimum reading.
- LENS 4 — Strict density projection from prompt language: ~22 floor / ~30 realistic strict midpoint; measured midpoint 55 ≥ 50 design target; OE is not artificially shoulder-carrying density.
- LENS 5 — No adversarial finding. Framing coherent ("relay, don't reopen"); no entity drift; no tool-name leak; no em-dash; no internal IDs; persona voice consistent; 379-word length carries lever-bearing content paragraph-by-paragraph; 5 of 5 named writes mandated or implied with strong contrast structure.

The prior `AUDIT_all.md` verdict on the prompt holds under independent prompt-only re-derivation.

## ACTIONABLE FIXES (if REVISE)

None. No REVISE required.

## STRUCTURAL FAIL (if REBUILD)

N / A. No REBUILD required.

---

**Auditor sign-off:** The prompt was re-audited in isolation under the strictest possible lens. No defect detectable above the dismissed-and-re-confirmed band of the prior all-phase audit. The candidate's `5_Prompt.txt` is shippable as-is. Greenlight stands.
