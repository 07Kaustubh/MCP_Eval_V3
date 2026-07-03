# S3 Council B — Adversarial QC (heaviest pass)

**Task:** `Tasks/34_6a42ec7493b48d5ada4571bd` · Universe: MoveOps (V2.1 framework)
**Artifact under review:** `7_Rubrics.json` (22 outcome / 0 process)
**Validator:** PASS
**Council mode:** ultrabrain · read-only

Rubric indexing (1-based, matches JSON array order):

| # | One-line subject |
|---|---|
| R1 | Reply to Craig's email `email_email_1f1459bff84c` from blessing.okafor |
| R2 | Reply acknowledges KeyMove $1,200 rider processed |
| R3 | Reply directs Craig to HOLD formal claim pending client-side |
| R4 | Reply restates walkup-assessment / stairwell-turn-radius cause |
| R5 | David + Catalina email goes from blessing to both addresses |
| R6 | D+C email names vendor-side closure ($1,200 KeyMove rider per Marcus) |
| R7 | D+C email flags client-side scope as open and outside Blessing's authority |
| R8 | D+C email references walkup-assessment lesson |
| R9 | D+C email does NOT propose a specific client-side dollar figure |
| R10 | D+C email does NOT include Pam Kowalski as recipient |
| R11 | Airtable update on `recEmiliaCruzChicagoDenver` in `tblRelocations01` of `appMoveOpsOps001` |
| R12 | Airtable update PRESERVES existing Special Requirements content |
| R13 | Airtable update names vendor-side closure |
| R14 | Airtable update names client-side pending flag |
| R15 | Airtable update captures walkup-assessment lesson |
| R16 | Slack post on `#operations` channel `C006` |
| R17 | Slack post covers walkup-assessment lesson |
| R18 | Linear comment on `linear_issue_c8cdba4408f1` |
| R19 | Linear comment references vendor-side closure |
| R20 | Linear comment references client-side disposition flagged for D+C |
| R21 | Linear comment references walkup-assessment lesson |
| R22 | Calendar event/reminder dated 2026-04-27 (Monday) re Craig follow-up |

---

## B1 — QC sub-dim scoring (Docs/7_QC_Spec_Doc1.json Rubric dimension)

| Sub-dim | Score | Evidence |
|---|---|---|
| **Overall Rubric Quality** (atomicity, self-containment, justification quality) | **5/5** | Every rubric checks exactly one observable; every title is self-contained (states actor, action, and discriminating attribute); every `justification` ties to a prompt sentence AND names the load-bearing lever; every `evidence` field names the tool call, the parameter to inspect, and the binary observable. No rubric depends on reading another rubric to be understood. |
| **Rubric Category Balance** (outcome ≫ process) | **5/5** | 22 outcome / 0 process. The 4 V3-reference Brookfield tasks (Task11..14) also ship with 0 process. Three-condition process test does not fire: (a) no purely procedural ask the agent could fulfil with a wrong artifact, (b) no compliance/regulatory step that the prompt makes the agent the gatekeeper for, (c) no internal-control invariant whose violation cannot be caught at the Outcome layer. All process-flavoured concerns (no Pam leak R10, no client $-figure R9, channel C006 R16, Linear issue match R18) are atomically captured as Outcome guards. |
| **Process Rubric Justification** | **N/A** | 0 process rubrics — no scoring needed. The decision to ship zero process is itself justified above. |
| **Agent-Centric Phrasing** | **5/5** | All 22 titles begin "The Agent ..." Verb forms (replies, updates, posts, adds, creates, does not include, does not propose) are agent actions, not system states. No passive voice. No tool names in titles (per Hard Rule 7). |
| **Service Metadata Completeness** | **5/5** | Email rubrics: R1 names `email_email_1f1459bff84c` and `blessing.okafor@moveops.com`; R5 names both TO addresses; R10 names the specific address to exclude. Slack rubric: R16 names `C006` and the channel name `#operations`. Linear rubric: R18 names `linear_issue_c8cdba4408f1`. Airtable rubric: R11 names `base_id appMoveOpsOps001`, `table_id tblRelocations01`, `record_id recEmiliaCruzChicagoDenver`. Calendar rubric: R22 names date `2026-04-27` with explicit Monday qualifier. Content-only rubrics (R2-R4, R6-R9, R12-R15, R17, R19-R21) correctly point to a `content`, `payload`, `body`, or `Special Requirements` parameter; metadata travels via the paired write-action rubric. |

**Composite Sub-Dim Score: 5/5 on every applicable dim.**

---

## B2 — Forward + reverse coverage map

### Forward (prompt ask → rubric coverage)

| Prompt ask (paraphrased) | Prompt anchor | Covering rubrics |
|---|---|---|
| 1. Reply to Craig at KeyMove on his Apr 11 email | "Craig at KeyMove emailed me on the 11th ... I owe him a direct reply" | R1 (write), R2 (rider ack), R3 (hold direction), R4 (walkup cause) |
| 2. Email David and Catalina a tight read on operational position + what is still moving | "Email David and Catalina a tight read on the operational position and what is still moving on their side" | R5 (write), R6 (vendor closed), R7 (client open), R8 (walkup lesson), R9 (no client $-figure), R10 (no Pam) |
| 3. Update Emilia's relocation record so it reflects both sides | "Update Emilia's relocation record so it reflects both sides of the disposition" | R11 (write), R12 (preserve), R13 (vendor), R14 (client), R15 (walkup) |
| 4. Drop the Emilia lesson in Slack where Chloe + ops team will see it | "Drop the Emilia lesson in Slack where Chloe and the ops team will see it" | R16 (write on C006), R17 (walkup content) |
| 5. Leave the operational facts on the existing Linear item for the wider NorthWind situation | "There is already a Linear item open ... leave the operational facts on that item" | R18 (write on existing issue), R19 (vendor), R20 (client), R21 (walkup) |
| 6. Remind me Monday to confirm Craig got his answer | "Remind me Monday to confirm Craig got his answer" | R22 (calendar 2026-04-27) |

All 6 explicit asks ≥ 1 rubric. ✔︎

### Reverse (rubric → prompt sentence)

Every rubric traces to a prompt sentence or to the prompt's load-bearing two-sided-disposition framing ("rider closes one ledger line; does not close out the rest of this" + "what is still moving on their side" + Mosaic-precedent shape "carrier exposure was one piece and the client-facing piece was a separate disposition with its own treatment ... process improvement section to the file"). Specifically:

- R10 (no Pam): supported by "Email David and Catalina" (scoped recipient list — Pam is third-party client and not in scope).
- R9 (no client $-figure): supported by "I do not have authority on the client facing piece. Surface what David and Catalina would need from us so they can package it cleanly" — Blessing has no authority to set the figure, so the rubric correctly forbids her inventing one.
- R12 (preserve Airtable content): supported by "Update Emilia's relocation record so it reflects both sides" — "update" not "replace"; the existing Special Requirements field is in the universe (OE11) and must be preserved.

No rubric goes BEYOND the prompt. ✔︎

---

## B3 — Density projection

Hardness Plan ships THIN_DENSITY at **midpoint 47, range 40-58**, with explicit per-task operator carry-forward (4-point justification including the genuine 6-write ceiling at Relocation-Coordinator scope, the 5-link L8 chain pushing upper bound to 51, and the intended L1+L9 short-circuit discrimination).

**Rubric-induced density projection (cross-check against the plan):**

| Rubric block | Reads forced | Writes forced |
|---|---|---|
| R1-R4 (Craig reply) | OE1 (contacts ×6), OE6 (Craig Apr 11), OE3-5 (KeyMove bill + ACC-6185 + Marcus framing) — 8-10 reads to ground the 3 content checks | 1 reply_to_email |
| R5-R10 (D+C email) | OE7 (Pam Apr 24 + Catalina Apr 14 + Apr 13 backup), OE8 (Alejandro retention model for L6 leak-check), OE12 (Mosaic precedent) — 5-7 reads | 1 send_email |
| R11-R15 (Airtable) | OE10 (base + tables), OE11 (Emilia row read for L2 preserve discriminator) — 3 reads | 1 airtable_update_records |
| R16-R17 (Slack) | OE2 (channels_list), OE15 (operational context confirm) — 2-3 reads | 1 conversations_add_message |
| R18-R21 (Linear) | OE9 (issue read + comments) — 2 reads | 1 linear_create_comment |
| R22 (calendar) | — | 1 calendar_add_event |
| Base + L11 + L8 + L13 buffer | OE4 (ACC-6185), OE13-14 (NorthWind QB + CRM for credit-memo context), retention chain triangulation — 6-9 reads | — |
| **Total** | **26-34 reads** | **6 writes** |
| **Grand total midpoint** | **~46-50 calls** | |

**Verdict: THIN_DENSITY (carry-forward).** Rubric set does not pull density below the 40 floor, and aligns with the Hardness Plan projection within 1-3 calls. Per Hard Rule 11, operator can continue with explicit per-task justification — that justification is already on file in `_aux/Hardness_Plan.md` and remains valid post-S3. Flagged for re-evaluation after first trajectory cycle per Hardness Plan operator note.

**B3 result: THIN_DENSITY (acknowledged, not a blocker).**

---

## B4 — Lever coverage

| Lever | Mechanism | Covering rubric (the value of the rubric DEPENDS on traversing this lever) |
|---|---|---|
| **L1 Latching ($1,200)** | Agent locks on the $1,200 KeyMove vendor rider as the whole disposition (Marcus L9 dismissal frame) | **R2** (Craig reply must specifically acknowledge the $1,200 rider processed) + **R6** (D+C email must name the $1,200 vendor closure per Marcus) — both explicitly anchor the load-bearing dollar figure, which forces the agent to surface the latch AND then escape it via L11 (see below) |
| **L2 Structured-DB skip (Airtable + Mosaic)** | Agent skips `tblRelocations01` Emilia row + `bill_mosaic_damage_accrual_001` Mosaic precedent | **R12** (preserves existing piano/three-vendor/lease-overlap content — only attainable if agent reads the row first) + **R14** (names client-side scope using Mosaic-precedent credit-memo language — only attainable if agent queries the Mosaic bill) |
| **L7 Multi-write diversification** | 6 writes across 5 services + 1 reminder | **R1, R5, R11, R16, R18, R22** — the six write-action rubrics, each binding a distinct service (email reply, email send, airtable, slack, linear, calendar). All six must hit for full credit, which forces breadth |
| **L8 Multi-link chain** | 5-link Craig → Marcus → Pam → Linear → Catalina-commitment | **R3** (Craig HOLD direction — only correct if agent has read Catalina's EOD package context, i.e. traversed link 5) + **R7** (handoff to D+C with client-side scope — only correct if agent has chained Marcus's vendor framing to Pam's escalation to the Linear retention issue) + **R20** (Linear comment scoped to operational facts that feed the retention package — only correct if agent has resolved the issue is the consolidator) |
| **L11 Net-vs-gross framing** | Vendor gross ≠ customer net | **R6 + R7** paired (vendor closed AND client open) + **R9** (no client $-figure — explicit gross-vs-net guard) + **R13 + R14** paired on Airtable + **R19 + R20** paired on Linear. The 6-pair structure across 3 surfaces is the strongest L11 enforcement in the rubric set. |

All 5 selected levers have ≥ 1 covering rubric whose value depends on lever traversal. ✔︎

---

## B5 — Adversarial alt-path (over-specificity check)

Walked every Outcome rubric. Flexible-language escape valves ("or similar", "or approved", "or accepted", "or comparable") are present on every content rubric where the universe genuinely admits multiple phrasings. Specific findings:

| Rubric | Alt-path stress test | Verdict |
|---|---|---|
| R1 | Agent uses `send_email` (new email) instead of `reply_to_email` on the thread, but still addresses Craig | **DISCRIMINATES CORRECTLY.** Prompt is explicit "I owe him a direct reply" → continuity on Craig's existing thread is the prompt-intent and the operationally-correct behaviour. Lock to `reply_to_email` + `email_id` is the right discrimination. Not over-specific. |
| R3 | Agent acknowledges Craig but does not address the formal-claim question | Rubric correctly FAILS this trajectory. This IS the stump-hypothesis #4 enforcement. Not over-specific. |
| R5 | Agent sends two separate emails (one to David, one to Catalina) covering all content | Prompt says "Email David and Catalina a tight read" — singular "an email" and the same docket framing across both. Rubric specifies "same outbound." Reasonable. ✔︎ |
| R7 | Agent names "client-side disposition is open and outside Blessing's authority" but does NOT enumerate credit-memo AND commercial-consideration scopes | **POTENTIAL ATOMICITY/OVER-SPEC.** Rubric primary requires BOTH a credit-memo/reimbursement scope AND a commercial-consideration scope. The escape valve "or similar statement that these scopes are outside Blessing's authority" mitigates by accepting a single broad statement. After re-reading: escape valve is broad enough that "the client-side scope is open and rests with you both" passes. Not a blocker, but flagged as a borderline candidate for split if a future revision wants to be safer (split into "names handoff" + "names commercial-consideration scope"). |
| R9 | Agent quotes the Mosaic CM-2026-0415 $40K direct exposure figure as a "precedent reference, not a recommendation" | Rubric language: "must not contain a specific client-side dollar figure ... attached to Emilia Cruz or the client-side disposition." The Mosaic figure is attached to MOSAIC, not Emilia. Borderline — could be argued either way. Mitigation: rubric explicitly says "attached to Emilia Cruz or the client-side disposition," which excludes the Mosaic precedent figure. ✔︎ |
| R12 | Agent appends NEW content but trims a few words of the existing "Special Requirements" prose (e.g. compresses three-vendor coordination into "vendor coordination") | Rubric language: "preserve content from the existing field (e.g., references to the piano, specialty piano movers, three-vendor coordination, lease overlap, or similar existing content)." "Or similar" provides flexibility. ✔︎ |
| R18 | Agent creates a NEW Linear issue rather than commenting on `linear_issue_c8cdba4408f1` | Rubric correctly fails. Prompt is explicit "There is already a Linear item open ... leave the operational facts on that item" — new-issue is the wrong behaviour. ✔︎ |
| R22 | Agent sets reminder for Tue Apr 28 (one business day after the Friday EOD) | Rubric specifies Monday 2026-04-27. Prompt says "Remind me Monday." Lock to Monday is correct. ✔︎ |

**One borderline finding (R7) — escape-valve mitigation holds. Not a blocker. No surgical fixes required.**

---

## B6 — Adversarial reverse-coverage (rubric → prompt sentence)

Walked every rubric in reverse. Every rubric maps to a prompt sentence or to the prompt's load-bearing Mosaic-precedent two-sided framing.

Special cases:

- **R9 (no client $-figure):** Prompt does NOT explicitly say "do not propose a dollar figure." This rubric is enforced from the conjunction of (a) "I do not have authority on the client facing piece" (prompt explicit) + (b) the L6 leak-check (no Emilia-specific reimbursement figure exists in universe). This is the standard "anti-hallucination" Outcome guard pattern and is supported by the prompt's authority scoping.
- **R10 (no Pam):** Prompt does NOT explicitly say "do not cc Pam." Enforced from (a) "Email David and Catalina" (scoped recipients) + (b) Hardness Plan L29 escape-valve mitigation (operator-required to prevent leakage of the formal-escalation context into the internal handoff). Supported.
- **R12 (preserve existing Airtable content):** Prompt says "Update Emilia's relocation record." "Update" semantically preserves existing data. Supported by OE11 explicit framing.

No rubric goes BEYOND the prompt scope. ✔︎

---

## B7 — Cross-artifact consistency (fabrication scan)

Walked every concrete value in rubric titles/justifications/evidence. Verified each appears in prompt OR OE OR universe split.

| Value | Source verified |
|---|---|
| `email_email_1f1459bff84c` (Craig Apr 11) | OE6, OE16 |
| `email_email_99e10a978b48` referenced via "Marcus Thorne's review" | OE5 (Marcus Apr 17) |
| `blessing.okafor@moveops.com` | Persona + OE1 |
| `david.chen@moveops.com`, `catalina.dubois@moveops.com` | OE1, OE17 |
| `pam.kowalski@northwindtech.com` | OE7 (Pam Apr 24) — rubric R10 accepts "any pam.kowalski address" so domain variance is tolerated |
| `$1,200` KeyMove rider | OE3 (QB bill), OE5 (Marcus framing), Hardness Plan L1 anchor count: 6+ surfaces |
| `appMoveOpsOps001`, `tblRelocations01`, `recEmiliaCruzChicagoDenver` | OE10, OE11, OE18 |
| Piano specialty / three-vendor coordination / lease-overlap (existing Special Requirements content) | OE11 explicit |
| `Marcus Thorne` | OE1, OE5 |
| `C006` `#operations` | OE2, OE19; MoveOps registry constant |
| `linear_issue_c8cdba4408f1` | OE9, OE20 |
| Walkup assessment / stairwell turn radius | Prompt verbatim |
| Credit-memo / client-side reimbursement / commercial consideration framing | OE12 (Mosaic precedent CM-2026-0415 model) |
| Mosaic precedent two-sided structure | OE12 + Hardness Plan |
| `2026-04-27` (Monday) | OE21; Universe today = 2026-04-26 (Friday) per universe constant |

**Zero fabrications detected.** Every concrete value in every rubric is anchored in either the prompt, an OE, or the per-task universe split.

Per the auto-memory note `[discovery_prompts_vs_groundedness.md]`, also cross-checked: rubric IDs (`linear_issue_c8cdba4408f1`, `recEmiliaCruzChicagoDenver`, `email_email_1f1459bff84c`) all appear in OE — these are NOT discovery-only IDs that would trigger B7 fabrication flags. ✔︎

---

## B8 — Atomicity check (single-failure-reason per rubric)

| # | Single-failure-reason? | Note |
|---|---|---|
| R1 | ✔︎ | Reply-to-email call present with correct email_id + sender |
| R2 | ✔︎ | $1,200 rider acknowledgement in content |
| R3 | ✔︎ | Hold-direction in content |
| R4 | ✔︎ | Walkup cause in content |
| R5 | ✔︎ | Both recipients on one outbound |
| R6 | ✔︎ | Vendor-side closure in content |
| R7 | ⚠ borderline | Primary "AND" requires BOTH a reimbursement-scope AND a commercial-consideration scope. Escape valve "or similar statement that these scopes are outside Blessing's authority" makes this single-concept (client-side open and out of authority). After re-read: escape valve carries the load — atomic via fallback. **Mitigation present; not flagged for revise.** |
| R8 | ✔︎ | Walkup lesson in content |
| R9 | ✔︎ | Negative atomic — no client-side $-figure |
| R10 | ✔︎ | Negative atomic — no Pam recipient |
| R11 | ✔︎ | Airtable update call with correct ids |
| R12 | ✔︎ | Preserves existing content (single discriminator) |
| R13 | ✔︎ | Vendor-side closure in Special Requirements |
| R14 | ✔︎ | Client-side pending flag in Special Requirements |
| R15 | ✔︎ | Walkup lesson in Special Requirements |
| R16 | ✔︎ | Slack post on C006 |
| R17 | ✔︎ | Walkup lesson in payload |
| R18 | ✔︎ | Linear comment on correct issue |
| R19 | ✔︎ | Vendor closure in body |
| R20 | ✔︎ | Client-side flag in body |
| R21 | ✔︎ | Walkup lesson in body |
| R22 | ✔︎ | Calendar event on 2026-04-27 |

**21/22 cleanly atomic. R7 borderline but escape-valve carries — not a blocker.**

---

## B10 — OE write-action map (every OE write has a 1.1 Outcome rubric)

| OE write | Service | Covering 1.1 Outcome rubric |
|---|---|---|
| OE16 `reply_to_email` to Craig | email | **R1** |
| OE17 `send_email` to David + Catalina | email | **R5** |
| OE18 `airtable_update_records` on Emilia row | airtable | **R11** |
| OE19 `conversations_add_message` to C006 | slack | **R16** |
| OE20 `linear_create_comment` on retention issue | linear | **R18** |
| OE21 `calendar_add_calendar_event` for Monday | calendar | **R22** |

All 6 OE write-actions have a paired 1.1 Outcome rubric. ✔︎

---

## B11 — Prompt "tell me" cue map

Walked every prompt sentence for direct-answer / "tell me" / "let me know" cues.

| Prompt cue | Type | 2.1 rubric needed? |
|---|---|---|
| "I owe him a direct reply" | Write action (reply email) | No — covered by R1-R4 (1.1 Outcome) |
| "Surface what David and Catalina would need from us" | Write action (email D+C) | No — covered by R5-R10 (1.1 Outcome) |
| "Update Emilia's relocation record" | Write action (airtable) | No — covered by R11-R15 (1.1 Outcome) |
| "Email David and Catalina a tight read" | Write action (email) | No — covered by R5-R10 (1.1 Outcome) |
| "Drop the Emilia lesson in Slack" | Write action (slack) | No — covered by R16-R17 (1.1 Outcome) |
| "leave the operational facts on that item" | Write action (linear) | No — covered by R18-R21 (1.1 Outcome) |
| "Remind me Monday to confirm Craig got his answer" | Write action (calendar/reminder) | No — covered by R22 (1.1 Outcome) |

**Result: All prompt asks are write-actions. No 2.1 (direct-answer to user) rubric needed.** Zero "tell me" / "let me know" / "explain" / "summarise to me" cues in the prompt. Pure operational-handoff task — every ask routes to a downstream surface. ✔︎

---

## Sub-dim score summary

| Sub-dim | Score |
|---|---|
| Overall Rubric Quality | 5/5 |
| Rubric Category Balance | 5/5 |
| Process Rubric Justification | N/A (0 process) |
| Agent-Centric Phrasing | 5/5 |
| Service Metadata Completeness | 5/5 |

**All applicable sub-dims at 5/5.**

## Perspective-level summary

| Perspective | Status |
|---|---|
| B1 sub-dim scoring | 5/5 across the board |
| B2 forward + reverse coverage | All 6 prompt asks covered; all 22 rubrics trace to prompt |
| B3 density projection | THIN_DENSITY (mid 47, plan-aligned, operator carry-forward valid) |
| B4 lever coverage | All 5 selected levers covered |
| B5 alt-path | No over-specificity issues (R7 escape valve holds) |
| B6 reverse-coverage | No rubric beyond prompt scope |
| B7 cross-artifact consistency | Zero fabrications |
| B8 atomicity | 21/22 cleanly atomic; R7 borderline mitigated by escape valve |
| B10 OE write-action map | All 6 OE writes paired with 1.1 Outcome |
| B11 "tell me" cues | None — all asks are writes; no 2.1 rubric needed |

## Optional surgical notes (not blockers, not required for GO)

For a future polish pass (not now), R7 could be split into two atomic rubrics:
- R7a: "names handoff of the client-side scope to David and Catalina as outside Blessing's authority"
- R7b: "names a commercial-consideration / goodwill / credit-memo scope as part of what D+C must decide"

The current escape valve makes this optional; the rubric IS atomically scorable today.

---

VERDICT: GO
