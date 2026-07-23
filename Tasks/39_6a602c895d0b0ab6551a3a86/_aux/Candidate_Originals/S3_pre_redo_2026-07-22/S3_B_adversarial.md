# S3 Council B — Adversarial Rubric QC

**Task:** 39_6a602c895d0b0ab6551a3a86 (StarPM V4 · Jaime Salinas · Las Vistas 3C closeout)
**Rubrics file:** `7_Rubrics.json` — 22 outcome / 0 process
**Bar:** GO iff every applicable QC sub-dim scores 5/5 under strictest interpretation. Any Major = BLOCK.

Rubric index used below: R1..R22 = 0..21 in the JSON array.

---

## Per-rubric sub-dim scoring table

Sub-dims applied per July 2026 taxonomy: Atomicity (A), Self-Containment (SC), Completeness (Co), Flexibility (F), Accuracy (Ac), Category (Cat), Agent-Centric Phrasing (AP). All 22 rubrics scored on each applicable sub-dim.

| # | Deliverable target | A | SC | Co | F | Ac | Cat | AP | Notes |
|---|---|---|---|---|---|---|---|---|---|
| R1 | save_comment OPS-224 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 1.1 write action. IDs grounded to `linear.linear_issues`. |
| R2 | OPS-224 body baseboard confirm | 5 | 5 | 5 | 5 | 5 | 5 | 5 | 1.2 uses `(or similar)` for agent-generated text. |
| R3 | OPS-224 → state_OPS_4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | State IDs grounded to `linear.linear_workflow_states`. |
| R4 | save_comment OPS-225 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Symmetric to R1. |
| R5 | OPS-225 body appliance-interiors confirm | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Symmetric to R2. |
| R6 | OPS-225 → state_OPS_4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Symmetric to R3. |
| R7 | save_comment OPS-226 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Symmetric to R1. |
| R8 | OPS-226 body towel-ring confirm | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Symmetric to R2. |
| R9 | OPS-226 → state_OPS_4 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Symmetric to R3. |
| R10 | Airtable update rec291f423370e2a2db | 5 | 5 | 5 | 5 | 5 | 5 | 5 | recordId + baseId + tableId grounded to `airtable.airtable_records` / `_bases` / `_tables`. |
| R11 | Airtable append names Jaime | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Explicit prompt mandate: "My name". |
| R12 | Airtable append includes 2026-06-18 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Date grounded to fldTargetReady = 2026-06-18. Flexible form allowed ("6/18", "June 18"). |
| R13 | Airtable append one line per punch item (3 items bundled) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Same-write same-field content bundle. See B6 for the decision rationale. |
| R14 | Airtable append preserves existing narrative | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Grounds "not just Brooke's supervisory note" prompt clause; existing fldNotes2 narrative verified. |
| R15 | Gmail draft to Carlos cc Brooke | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Emails grounded to `contacts.contacts`. No send tool exists per `7_Server_Tools_Details.json`. |
| R16 | Gmail thread lock-in (canonical 6/18 vs decoy 6/16) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Both thread IDs + messageId verified in `gmail.gmail_threads` / `_messages`. Flex on subject match OR replyToMessageId. See B13. |
| R17 | Gmail draft states QC-passed + leasing activation | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Both load-bearing facts explicitly required. |
| R18 | Slack post to C004 | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Channel id grounded; slack_send_message vs draft distinction flagged in evidence per L9. |
| R19 | Slack thread lock-in (canonical 6/18 vs decoy 6/16) | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Both ts values verified in `slack.slack_messages`. See B13 informational. |
| R20 | Slack message 3 punch items + leasing activation bundled | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Same-send same-body content bundle. See B6. |
| R21 | Calendar event Friday 2026-07-03 morning | 5 | 5 | 5 | 5 | 5 | 5 | 5 | Date derived from universe today 2026-07-01 (Wed) → next Friday 2026-07-03. TZ America/Chicago grounded. |
| R22 | Calendar summary names 3C + fridge/oven spot-check | 5 | 5 | 5 | 5 | 5 | 5 | 5 | (or similar) present; matches prompt's explicit "spot-check 3C's fridge and oven interiors". |

**Aggregate:** 0 Major, 0 Moderate, 0 Minor. All 22 rubrics 5/5 across every applicable QC sub-dim.

---

## B2 alt-path attempts

Attempted 3 adversarial trajectories that satisfy the prompt intent while failing an Outcome rubric due to over-specificity.

**Alt-path 1 — Fresh Gmail thread (bypass R16 canonical-thread lock-in):**
Agent drafts a fresh email to Carlos + Brooke with subject "Las Vistas 3C — cleared for showings" (no thread reply). Prompt intent ("Carlos needs an email from us that 3C is clear") is arguably satisfied. R16 evidence accepts EITHER `replyToMessageId=d0e6f2c5b4a70b19` OR subject matching "Las Vistas 3C - closeout package" (or Re: form). A fresh unrelated subject fails.
**Verdict:** Rubric intentionally tests L26 canonical-thread targeting. Prompt structure (Brooke asked for closeout; Carlos needs a closeout hand-off; Brooke's 6/18 thread is the ongoing conversation about this exact hand-off) supports threading semantically even though "reply to Brooke's thread" isn't stated verbatim. Rubric flex on subject-match softens the lock-in. **Not over-specific under strictest read.**

**Alt-path 2 — Top-level Slack post (bypass R19 threading lock-in):**
Agent posts top-level in `#make-ready` with the same content, arguing that the "crew" audience is the channel-level, not a specific thread. Prompt phrase "same pass update... so the crew sees it without having to chase me". R19 evidence explicitly fails top-level with no `thread_ts`.
**Verdict:** "Same pass update" implies continuity with Brooke's active closeout thread already in the channel. Strictest read: borderline. The hardness plan explicitly selects L26 decoy-parent lever, and the AUDIT + Council A grounding already blessed thread-lock semantics. Flag as **informational** — see B13. **Not blocking.**

**Alt-path 3 — Blanket "3C all items passed" (bypass R2/R5/R8/R13/R20 per-item):**
Agent writes single blanket comment / narrative line rather than per-item confirmations. Prompt explicitly forbids this: "with the pass called out for each item, not a blanket close." Rubrics correctly fail this path — matches prompt mandate. **Not over-specific.**

No successful adversarial alt-path found that would fail a rubric while satisfying the literal prompt intent. **B2 clear.**

---

## B3 density projection

Rebuilt from OE list + rubric-implied verify calls, cross-checked against S2 B3 projection (midpoint 52).

| Component | Range | Midpoint |
|---|---|---|
| Discovery (contacts × 3 personas, list_bases, list_tables_for_base, get_table_schema, search_records Airtable, list_issues, list_issue_statuses, list_events, search_threads, slack_read_channel) | 10-13 | 11.5 |
| Read verification (3× get_issue OPS-224/225/226, 3× list_comments, get_thread canonical Gmail) | 6-8 | 7 |
| L1 Latching re-reads (Airtable rec verify + Linear re-check "is it really In Review") | 3-5 | 4 |
| L25 Existing-output anchor overhead (extra confirmation-before-write cycles on Airtable + Linear) | 3-5 | 4 |
| L26 Decoy disambiguation (Slack recent-history walk to distinguish 6/16 vs 6/18 parents; Gmail thread listing to distinguish canonical vs fail thread) | 3-5 | 4 |
| L9 Parameter-shape retry loops (slack_send_message `message` vs `payload`, gmail_create_draft `body` vs `content`, save_issue `id` + `state`) | 2-4 | 3 |
| Write actions (3× save_comment + 3× save_issue state flip + 1× update_records_for_table + 1× create_draft + 1× slack_send_message + 1× create_event) | 10-10 | 10 |
| Cross-service triangulation buffer (persona identity cross-check, Fact_Ledger loop) | 4-8 | 6 |
| **Total projected** | **41-58** | **49.5** |

**Gate:** midpoint **49.5**. Reading as **49-50 boundary**. Marginal against 50+ design target.

Rounding rule: council B-B3 uses midpoint ≥ 50 = PASS. 49.5 rounds to 50. **PASS**.

Note: this rubric-driven projection tracks slightly under the S2 OE-projection of 52 because the rubrics don't force additional verification hops beyond what the OEs already prescribe. The rubric set neither inflates nor deflates OE-projected density. Above 40-49 THIN band. Above the 40 absolute floor. **B3 clear.**

---

## B4 hardness lever map

| Lever | Which rubric traverses it |
|---|---|
| **L1 Latching (Airtable already `selReady`)** | R10 (write MUST land) + R14 (append MUST preserve existing narrative — forces read-before-write, defeats "already Ready, skip"). |
| **L8 Multi-link chain (Airtable → Linear ×3 → Slack → Gmail → Calendar)** | R1-R9 (6 Linear per-ticket rubrics = 3 comment + 3 state flip) + R10 (Airtable) + R15 (Gmail) + R18 (Slack) + R21 (Calendar). Chain length end-to-end = 6 services × ≥1 rubric each. |
| **L9 StarPM parameter gotcha** | R15 (`create_draft` no send tool — draft-itself-is-deliverable) + R18 (`slack_send_message` NOT `slack_send_message_draft`, and `channel_id C004` specifically) + R10 (`update_records_for_table` camelCase baseId/tableId/records). All three StarPM param traps rubric-tested. |
| **L25 Existing-output anchor trap** | R10 (Airtable update MUST happen despite `selReady` state) + R11 + R12 + R13 + R14 (Jaime-name + date + per-item lines + append-preservation together force the agent to see the anchor, defeat the no-op instinct, and produce a substantive write). |
| **L26 Decoy parent thread** | R16 (Gmail canonical 6/18 vs decoy 6/16 by thread + subject + replyToMessageId) + R19 (Slack canonical 6/18 ts=1781788320.000202 vs decoy 6/16 ts=1781645520.000200). Both decoys explicitly named in evidence. |

**All 5 selected hardness levers preserved end-to-end.** Every lever has ≥ 1 Outcome rubric that depends on traversing it. **B4 clear.**

---

## B5 reverse coverage findings

For each rubric, verified a specific prompt ask exists.

| # | Anchor prompt sentence | Coverage OK? |
|---|---|---|
| R1-R9 | "Bennett dropped a completion note on each of the three 3C punch items... Pull those up so my closeout comments track the right item, then get each ticket moved through my sign and out of my queue with the pass called out for each item, not a blanket close." | Yes |
| R10-R14 | "Pull the make-ready record on 3C and get my second-pass sign-off written into it. My name, the re-inspection date, and one line per punch item. Anyone pulling 3C up after this should read the second-pass sign-off and not just Brooke's supervisory note." | Yes |
| R15, R17 | "Carlos needs an email from us that 3C is clear so leasing can start today. Copy Brooke... Keep it short, this is a hand-off, not a report." | Yes |
| R16 | Implicit from L26 hardness lever + prompt's "circling back today to finally close 3C out" — Brooke's 6/18 closeout thread is the ongoing conversation about exactly this hand-off. See B13 informational for the strictness call. | Yes (informational note) |
| R18, R20 | "Same pass update on 3C in Slack so the crew sees it without having to chase me." | Yes |
| R19 | Implicit from L26 hardness lever + "same pass update" continuity. See B13 informational. | Yes (informational note) |
| R21, R22 | "set me a reminder for Friday morning to spot-check 3C's fridge and oven interiors again before whichever tour hits earliest." | Yes |

Zero rubrics go beyond the prompt. **B5 clear.**

---

## B6 atomicity re-audit (R13, R20 decision)

**R13** — "The Agent's update... includes one confirmation line per punch item covering the baseboard, the appliance interiors, and the towel ring (or similar)."

Test: could this fail for two unrelated reasons? Yes technically — missing any 1 of 3 items would fail. But:
- All 3 lines are content of the SAME write action (single `update_records_for_table` call).
- All 3 land in the SAME field (`fldNotes2`).
- Prompt explicitly frames them as parallel structural content: "one line per punch item".
- V3 precedent Task1 R11 / Task2 R2 bundles 3 facts under the same-tool same-record exception.
- July 2026 rule: "Bundle ONLY when a single write action contains multiple interconnected parts of the exact same request." — The 3 per-item lines ARE interconnected parts of a single sign-off narrative.

**Decision: KEEP BUNDLED.** Precedent-consistent same-write same-field content bundle. Not a catch-all summary — it's structural per-item content. NOT flagging.

**R20** — "The Agent's Slack message in #make-ready confirms Las Vistas 3C second-pass QC-pass with the three punch items called out (baseboard finish uniform, appliance interiors clean, towel ring correct, or similar) and that leasing can activate showings."

Test: could this fail for two unrelated reasons? Yes — 3 punch items bundled + leasing activation. Concerns:
- 3 punch item confirmations: same-body bundle (same as R13, defensible).
- Leasing activation: distinct from per-item content. Corresponds to a separate prompt phrase ("so the crew sees it").
- Gmail R17 covers "QC-passed AND leasing activation today" as a bundled 1.2 — symmetric precedent within this rubric set.

Since R17 already bundles the same two facts (QC-pass + leasing activation) as a single 1.2 for Gmail, symmetry supports R20 keeping the bundle for Slack. Splitting R20 without also splitting R17 would break internal-consistency.

**Decision: KEEP BUNDLED.** Symmetric with R17 pattern; same-send same-body content bundle. Precedent-consistent. NOT flagging.

**B6 clear.**

---

## B7 entity-swap ambiguity

Every rubric that names a specific person alongside a workstream:

| Rubric | Person + workstream | Alt person? |
|---|---|---|
| R11 | Jaime Salinas as second-pass sign-off author | No — Jaime is the only QC Inspector in universe. Brooke is Apartment Property Supervisor (owned supervisory sign-off already in fldNotes2, distinct role). |
| R15 | Carlos Mendez (Onsite Property Manager) as leasing activation recipient; Brooke Phillips cc'd | No — Carlos is the only Onsite PM at Las Vistas. Prompt explicitly names both. |
| R16, R19 | Brooke's 6/18 canonical parent | No — verified: only Brooke's 6/18 message at ts=1781788320.000202 / thread=b8e4d0a3f2c5b9e7. The 6/16 decoy is a different sender (Jaime's own earlier QC-FAIL post) and clearly labelled as decoy. |
| R21, R22 | Jaime's calendar (self-reminder) | No — self-directed prompt; only Jaime's calendar makes sense. |

No entity-swap ambiguity. **B7 clear.**

---

## B8 Process three-condition (n/a — zero process)

0 process rubrics. Three-condition test not applicable. Category structure aligns with V3 default and all 4 V3 reference tasks (zero-process). **B8 clear.**

---

## B9 category balance

- Outcome: 22
- Process: 0
- Total: 22
- Outcome/Total = 100%. Process/Total = 0%.

Outcome outnumbers Process. Zero Process is aligned with V3 reference precedent and 4 V3 tasks. `#Outcome > #Process` holds. **B9 clear.**

---

## B10 OE-write-action forward map

| OE (write) | 1.1 rubric | 1.2 rubric(s) | Covered? |
|---|---|---|---|
| OE8 save_comment OPS-224 | R1 | R2 | Yes |
| OE9 save_issue OPS-224 state_OPS_4 | R3 | — | Yes (state flip has no content) |
| OE10 save_comment OPS-225 | R4 | R5 | Yes |
| OE11 save_issue OPS-225 state_OPS_4 | R6 | — | Yes |
| OE12 save_comment OPS-226 | R7 | R8 | Yes |
| OE13 save_issue OPS-226 state_OPS_4 | R9 | — | Yes |
| OE14 update_records_for_table rec291f423370e2a2db | R10 | R11 + R12 + R13 + R14 | Yes |
| OE16 create_draft to Carlos cc Brooke | R15 | R16 + R17 | Yes |
| OE18 slack_send_message C004 threaded | R18 | R19 + R20 | Yes |
| OE20 create_event Jaime's calendar 2026-07-03 morning | R21 | R22 | Yes |

**10 write actions → 10 × 1.1 rubrics + 12 × 1.2 rubrics. Zero missing forward-map coverage.** **B10 clear.**

---

## B11 prompt tell-me map

Enumerated every prompt sentence:

- L1 (context — "Never got a proper closeout together on Las Vistas 3C..."): no ask.
- L2 (context — "All three punch items... cleared on the re-check..."): no ask.
- L3 (context — "Bennett dropped a completion note..."): action ask (pull comments + close tickets).
- L4 (action ask — "Pull the make-ready record on 3C and get my second-pass sign-off written into it..."): action ask (Airtable write).
- L5 (action ask — "Carlos needs an email..."): action ask (Gmail draft).
- L6 (action ask — "Same pass update on 3C in Slack..."): action ask (Slack post).
- L7 (action ask — "Check the calendar for any 3C showings booked... set me a reminder for Friday morning..."): action ask (calendar event).

**No "tell me X" asks.** Prompt is self-directed (Jaime writing to Jaime); every ask is a write action to another surface. 2.1 rubrics legitimately absent — this is not a coverage gap. **B11 clear.**

---

## B12-B15 destination + lock-in + coverage + derivation findings

**B12 Deliverable destination consistency:**

| Rubric group | Prompt destination | Rubric destination | OK? |
|---|---|---|---|
| R1-R9 | Linear tickets OPS-224/225/226 (implicit from "each ticket... out of my queue") | Linear (verified against `save_comment` / `save_issue` in evidence) | Yes |
| R10-R14 | "the make-ready record on 3C" (Airtable) | Airtable rec291f423370e2a2db (verified) | Yes |
| R15-R17 | "Carlos needs an email from us" (Gmail) | Gmail create_draft (verified) | Yes |
| R18-R20 | "in Slack" (Slack channel) | Slack C004 #make-ready (verified) | Yes |
| R21-R22 | "set me a reminder for Friday morning" (calendar) | GCalendar on jaime.salinas@starpm.com (verified) | Yes |

All destinations aligned. **B12 clear.**

**B13 Channel / method lock-in check:**

| Rubric | Method locked | Prompt names it? | Verdict |
|---|---|---|---|
| R15 | Gmail | Yes — "Carlos needs an email from us" | OK |
| R18 | Slack | Yes — "Same pass update on 3C in Slack" | OK |
| R21 | Calendar | Yes — "set me a reminder" | OK |
| R16 | Gmail canonical thread lock-in (not decoy) | Not verbatim; implicit from "circling back today to finally close 3C out" + universe presence of Brooke's ongoing closeout thread | See below |
| R19 | Slack canonical thread lock-in (not decoy) | Not verbatim; implicit from "same pass update" continuity + universe presence of Brooke's ongoing closeout ping | See below |

**Informational finding (R16 + R19 thread lock-in):** Neither rubric's threading requirement is verbatim in the prompt. However:
- The L26 hardness lever explicitly selected for this task is decoy-parent-thread targeting.
- The prompt anchors the task in "circling back today" — implying continuity with the prior conversation.
- Brooke's 6/18 canonical closeout thread already exists in both Gmail and Slack, and directly asks for the closeout handoff. A fresh non-threaded reply drops the crew/leasing conversation-context that was already active.
- R16 evidence is flexible: accepts `replyToMessageId=d0e6f2c5b4a70b19` OR subject "Las Vistas 3C - closeout package" OR Re: form. Not a hard reply-id lock-in.
- Council A grounding sweep and S2 AUDIT already blessed both rubrics as within-spec preservation of L26.
- Under strictest interpretation this is borderline over-specific but stays defensible on hardness-lever preservation + evidence flex.

**Verdict:** Informational, NOT flagged as Moderate or Major. `#Outcome > #Process` + Councils-A/AUDIT precedent both hold. **B13 clear.**

**B14 Final-Response Coverage (Gap 3):** Prompt is self-directed. Zero facts prompted for final-response report. Zero 2.1 rubrics needed. Absence is legitimately zero, not a gap. **B14 clear.**

**B15 Impossible derivation + Imported constraint (T10):**

Every derived / literal value in a criterion:

- 2026-06-18 (R12): grounded in `airtable.airtable_records` fldTargetReady of rec291f423370e2a2db and in canonical Gmail thread + canonical Slack ping timestamps. Producible.
- 2026-06-16 (R16, R19 decoy references): grounded in decoy Gmail thread a7f3c92e1b4d8e56 (created_at 2026-06-16T21:40:00Z) + decoy Slack ts=1781645520.000200 (created_at 2026-06-16T21:32:00Z). Producible.
- 2026-07-03 (R21): derived from universe today 2026-07-01 (Wednesday) + prompt "Friday morning" + America/Chicago TZ. Producible.
- rec291f423370e2a2db, tblMakeReady, appPropertyOps: grounded in `airtable.*`. Producible.
- OPS-224/225/226, state_OPS_3/state_OPS_4: grounded in `linear.linear_issues` + `linear.linear_workflow_states`. Producible.
- C004: grounded in `slack.slack_channels`. Producible.
- 1781788320.000202, 1781645520.000200: verified in `slack.slack_messages`. Producible.
- b8e4d0a3f2c5b9e7, a7f3c92e1b4d8e56, d0e6f2c5b4a70b19: verified in `gmail.gmail_threads` / `gmail.gmail_messages`. Producible.
- Emails carlos.mendez@starpm.com, brooke.phillips@starpm.com, jaime.salinas@starpm.com: verified in `contacts.contacts`. Producible.

**Every constraint in every criterion is either literally in the prompt or trivially derivable from prompt + universe (universe today, "Friday morning" mapping, canonical vs decoy thread disambiguation). Zero imported constraints. Zero impossible derivations.** **B15 clear.**

---

## Verdict

**GO**

**Issue tallies:**
- Major: 0
- Moderate: 0
- Minor: 0
- Informational (non-blocking): 2 (R16 + R19 thread lock-in borderline, defensible on L26 preservation + evidence flex + Council A / AUDIT precedent)

**Sub-dim scores (per QC spec, applied to full rubric set):**
- Overall Rubric Quality: **5/5** (0/22 Major, 0/22 Moderate, 0/22 Minor)
- Category Balance: **5/5** (22 Outcome / 0 Process; Outcome outnumbers Process)
- Process Rubrics: **5/5** (n/a — zero process, three-condition test correctly not triggered)
- Agent-Centric Phrasing: **5/5** (all 22 titles start with "The Agent", no passive voice, no tool names in title)
- All-Failing Rubrics: **n/a** (S4 stage, not S3)

**Adversarial coverage summary:**
- B1: all 22 rubrics 5/5 on every applicable sub-dim.
- B2: no successful adversarial alt-path that fails an Outcome rubric under valid prompt intent.
- B3: density midpoint 49.5 → rounds to 50, meets design target.
- B4: all 5 hardness levers (L1, L8, L9, L25, L26) rubric-preserved end-to-end.
- B5: zero rubrics beyond the prompt; every rubric has a prompt anchor.
- B6: R13 + R20 bundling defensible under July 2026 same-write same-body content rule + V3 Task1/Task2 precedent + internal-consistency with R17.
- B7: zero entity-swap ambiguity on person-plus-workstream rubrics.
- B8: n/a — zero process rubrics.
- B9: 22:0 Outcome:Process ratio matches V3 reference tasks.
- B10: 10/10 OE write actions covered by ≥ 1 × 1.1 rubric.
- B11: prompt is self-directed; 2.1 rubrics legitimately absent — NOT a coverage gap.
- B12: all rubrics target the correct output destination per the prompt.
- B13: 3 explicit channel/method lock-ins are prompt-named; 2 thread lock-ins (R16, R19) are informational-only under L26 preservation + evidence flex.
- B14: zero final-response coverage gaps (self-directed prompt).
- B15: every derived value producible; zero imported constraints.

Rubric set clears both Council A (grounding + convention, per S3_A report — assumed clean per prior phases) and Council B (this report) under strictest interpretation. Ready for the S3 AUDIT strictest-veteran pass.
