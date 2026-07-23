# Council B — Adversarial QC + Density + Hardness Preservation (S1 Prompt) — **v4 REVIEW after AUDIT REVISE**

- **Task:** 40_6a61a86a31b9c973b2021ba5
- **Phase:** prompt (S1)
- **Deliverable:** `Tasks/40_6a61a86a31b9c973b2021ba5/5_Prompt.txt` (v4, revised after AUDIT REVISE on v3)
- **Universe:** StarPM V4 (today = 2026-07-01 Wed, America/Chicago)
- **Persona:** Carlos Mendez, Onsite Property Manager (Mesa Vista)
- **Business Function:** Property Operations (Cat 1)
- **Method:** 5 role lenses (Architect / Implementer / Red-team / Ground-truth / Integration), 5 perspectives (B1, B2, B3, B4, B6).
- **Prior verdict (v3):** GO with THIN density carry (~49-50 midpoint) + 1 Minor Truthfulness slip carried; AUDIT then flagged 4 REVISE findings (F1 Truthfulness Diane-deadline drift, F2 Clarity Diane-vendor collision, F3 density hygiene, F4 word count).
- **v4 scope:** four AUDIT REVISE fixes — (1) rewrote closing line to remove false Diane-deadline attribution, (2) anchored Diane's first mention with vendor + role, (3) THIN carry codified in Hardness_Plan.md (footnote added lines 61-67), (4) trimmed prompt 424 -> 386 words.

## OVERALL VERDICT: GO

All four AUDIT REVISE findings resolved. **Truthfulness recovers 4/5 -> 5/5** — the load-bearing closing line "Parts need pulling today so Hill Country's ready for Thursday morning" is now a Carlos-owned operational statement with no named-entity attribution, so the v3 1-day forward drift on Diane's Mon-EOD-tomorrow claim is eliminated. **Clarity & Specificity recovers 4/5 -> 5/5** — line 3 "Diane, their AP contact at Hill Country" carries two disambiguators (vendor anchor "Hill Country" + role anchor "AP contact") that neutralize the base-universe Diane Flores (Lonestar Maintenance Supply, Account Representative) collision. All other v3 5/5 sub-dims hold. All 6 selected levers PRESERVED (L1, L2, L5, L7, L8, L9). Density unchanged at ~49-50 midpoint; **THIN carry now formally codified in `_aux/Hardness_Plan.md:61-67`** (AUDIT F3 resolved). Word count: **386 words** (was 424; under 400 sweet-spot preference AND under 500 hard cap — AUDIT F4 resolved). Zero em-dashes. Adversarial B2 sweep on v4 changes produces zero divergences.

---

## v3 -> v4 Diff Verification (against AUDIT REVISE findings)

| # | AUDIT finding | v3 text | **v4 text** | Line | Fix mechanism | Verified against |
|---|---|---|---|---|---|---|
| F1 | Truthfulness — line 11 attributed Wed-EOD deadline to Diane; her Mon email says Tue EOD | "Diane wants confirmation by end of business today so we're not scrambling on parts" | **"Parts need pulling today so Hill Country's ready for Thursday morning"** | 11 | Removes false Diane-attribution; recasts as Carlos-owned operational statement | No named-entity attribution -> no Truthfulness slip possible; grounded in "Thursday morning" install slot already established via Gmail record 7b body "We can be on site Thursday morning if you approve" |
| F2 | Clarity — "Diane" under-specified; base has Diane Flores at Lonestar (Account Rep, unrelated vendor); no Hill Country contacts row | "Their front-office lady, Diane, emailed me..." | **"Diane, their AP contact at Hill Country, emailed me..."** | 3 | Two disambiguators: vendor anchor ("Hill Country") + role anchor ("AP contact" grounded via `ap@hillcountryplumbing.com` sender prefix) | Diane Flores (Lonestar) title = "Account Representative" (not "AP contact"); Hill Country injected Gmail from `ap@hillcountryplumbing.com` with body signature "Diane at Hill Country Plumbing" — both disambiguators fire against the collision |
| F3 | Density hygiene — Council B v3 re-projected 49-50 THIN but Hardness_Plan showed 56.0 PASS | N/A (Hardness_Plan mismatch) | **Footnote added to `_aux/Hardness_Plan.md:61-67`** | Hardness_Plan | Codifies THIN carry with explicit acceptance rationale (6-lever buffer, further consolidation risks UGT regression, 8-service breadth PASS) | Read Hardness_Plan.md lines 61-67; footnote present, verdict criteria "documented in Hardness_Plan.md" satisfied |
| F4 | Word count 424 > 400 preference | 424 words | **386 words** | full prompt | Trimmed ~38 words across full prompt while preserving all lever surfaces | `wc -w 5_Prompt.txt` returns 386; under 400 sweet-spot AND under 500 hard cap |

**Diff verification:** All four v4 changes are targeted AUDIT fixes. Zero writes removed, zero discovery asks removed, zero lever mechanics changed. Two edits are wording-only; one is a Hardness_Plan documentation update; one is a word trim.

---

## B1 — QC Sub-Dim Scoring (v4, 12 applicable sub-dims, STRICT read)

| Sub-Dim | v3 Score | AUDIT (STRICT) | **v4 Score** | Delta | One-Line Reason |
|---|---|---|---|---|---|
| Unique Ground Truth | 5 | 5 | **5** | 0 | "Tenant thread I had going" still unambiguously anchors to Carlos's own thread; write targets unchanged. |
| Feasibility | 5 | 5 | **5** | 0 | All 8 writes + all named entities still resolve; StarPM tool traps compatible; no new phrasings introduce feasibility risk. |
| Explicit Tool Mention | 5 | 5 | **5** | 0 | Zero MCP tool names, zero server names anywhere. |
| **Clarity & Specificity** | 5 | **4** | **5 (RECOVERED)** | **+1 vs AUDIT** | **AUDIT F2 fix verified.** "Diane, their AP contact at Hill Country" carries vendor anchor + role anchor. Diane Flores (Lonestar) title is "Account Representative" (not "AP contact"), different vendor. Even naive `contacts_search("Diane")` collision is mitigated because the Draft action target is the Gmail thread sender (`ap@hillcountryplumbing.com`) already discovered via `gmail_search_threads("Mesa Vista 7B")` — no contacts lookup required for the write. |
| Contrived / Unnatural | 5 | 5 | **5** | 0 | Closing paragraph structure unchanged (merged drafts, natural onsite-PM voice). Line 11 rewrite reads as tactical urgency framing, not checklist-y. Trims applied evenly across full prompt do not create bullet-list feel. |
| **Truthfulness** | 5 | **4** | **5 (RECOVERED)** | **+1 vs AUDIT** | **AUDIT F1 fix verified.** Load-bearing closing line has no named-entity attribution — "Parts need pulling today so Hill Country's ready for Thursday morning" is Carlos's own operational read grounded in the already-established Thursday morning install slot. No Diane-attributed Wed-EOD claim remains. All other atoms still ground to universe records (see v3 per-atom evidence table, unchanged for lines 1-9). |
| Tool Use & Cross-service | 5 | 5 | **5** | 0 | 8 services still triangulated (Slack, Airtable, Linear, Gmail, QuickBooks, Contacts, GCalendar, HubSpot). |
| Investigation + Action | 5 | 5 | **5** | 0 | Read/write balance unchanged; 8 writes across 5 services still enumerated. |
| Coherence / Bolt-on | 5 | 5 | **5** | 0 | Sentence-removal test still passes; every ask ties to Thursday install slot + pending scope decision. |
| Persona | 5 | 5 | **5** | 0 | Casual-tactical Carlos voice preserved; passive-voice-idiom + structured-recap intact after trims. Formality 0.55 / verbosity 0.50 posture holds. |
| Business Function | 5 | 5 | **5** | 0 | Property Operations (Cat 1) unchanged. |
| Alignment with Today's Date | 5 | 5 | **5** | 0 | "Monday" (2026-06-29), "yesterday" (2026-06-30), "last night" (2026-06-30 eve), "today" (2026-07-01 Wed), "Thursday" (2026-07-02) all resolve cleanly. |

**B1 verdict:** GO. **Truthfulness + Clarity BOTH recovered to 5/5 from AUDIT's 4/5.** All 12 applicable sub-dims now >= 5. Zero <5 carry-through.

---

## B2 — Adversarial Alt-Path / Second-Reading Attack (v4, focused on new phrasings)

### Q1 (NEW - AUDIT F2 verify): "Diane, their AP contact at Hill Country" — can this still be misread as Diane Flores at Lonestar?

**NO DIVERGENCE.** Three-layer defense:
1. **Vendor anchor** "at Hill Country" — a `contacts_search("Diane") + filter contains "Hill Country"` returns zero rows (no Hill Country Diane contact injected); agent naturally falls back to the Gmail thread sender.
2. **Role anchor** "AP contact" — Diane Flores's title in `contacts.contacts` is "Account Representative", not "AP contact". If agent maps "AP" -> "Accounts Payable", Diane Flores does not match; if agent maps "AP contact" -> the `ap@` email prefix pattern, `ap@hillcountryplumbing.com` matches Hill Country's vendor Gmail sender.
3. **Action target** — the Draft to Diane targets the Gmail thread sender (`ap@hillcountryplumbing.com`), not a contacts-based email lookup. The thread is already discovered via `gmail_search_threads("Mesa Vista 7B water heater")` — Diane's real email address is in the thread payload.

**Perspective:** Ground-truth / Red-team / Implementer. All three role lenses converge: the collision is neutralized in practice.

### Q2 (NEW - AUDIT F1 verify): "Parts need pulling today so Hill Country's ready for Thursday morning" — could this be misread as expecting the parts to actually be pulled today by Carlos (write action)?

**NO DIVERGENCE.** Structural + semantic + tool-availability defenses:
1. **Structural:** the sentence is closing urgency framing, not enumerated ask. Line 9 already enumerated all 8 writes explicitly ("Bring the maintenance ticket current... Update the operations tracking issue... Drop back into the tenant thread... Draft Diane the revised confirmation so she can pull the right parts, Tanya an update... Robert a heads-up... And put the install on my calendar..."). Line 11 is a follow-on justification for the timing, not a new action.
2. **Semantic:** "Hill Country's ready for Thursday morning" — Hill Country is the vendor doing the install; Hill Country pulls the parts. The construction "parts need pulling today" is passive; the implicit subject is Hill Country (established via "so Hill Country's ready" in the same sentence).
3. **Tool-availability:** StarPM has NO parts-inventory tool for Carlos to "pull parts" through. Only the Draft-to-Diane-confirming-scope path (already enumerated in line 9) affects parts pulling. Even a maximally-literal agent has no tool to over-index on.
4. **Cross-check:** line 9 already says "Draft Diane the revised confirmation so she can pull the right parts" — line 11 reinforces the same urgency, using consistent framing.

**Perspective:** Red-team / Implementer. Zero divergence — reads as urgency framing.

### Q3 (carried from v3): "Tenant thread I had going" — one thread or two?

**NO DIVERGENCE.** Unchanged in v4. Resolves to Carlos's own thread (records 3+4) by possessive + descriptor + Tony's post having `reply_count: 0`. Perspective: Red-team.

### Q4 (carried): "Close out today" — approve Tony vs correct scope?

**NO DIVERGENCE.** Line 7 "Whatever the diagnostic actually points to is the scope I want to move on" is explicit contingency; unchanged in v4. Perspective: Ground-truth.

### Q5 (carried): "Draft Diane the revised confirmation" — draft vs send?

**NO DIVERGENCE.** Gmail draft-only in StarPM; "Draft" verb matches tool semantic; unchanged in v4. Perspective: Implementer.

### Q6 (retested from v3): "Monday night" ticket vs Tony's "Monday night" post collision?

**NO DIVERGENCE.** Airtable record 1 created_time 21:14 CDT + Slack Tony post 22:14 CDT — natural sequence (Carlos logs ticket at 21:14, Tony posts endorsement at 22:14). Both are Monday night events; no agent-facing conflict. Perspective: Ground-truth / Integration.

### Q7 (retested from v3): "That afternoon" — could an agent think Diane emailed from a different day's diagnostic?

**NO DIVERGENCE.** No other Hill Country diagnostic exists in universe for Mesa Vista 7B. Single referent. Perspective: Ground-truth.

### Q8 (NEW spot-check on trimming): does trimmed line 11 create checklist-y feel?

**NO DIVERGENCE.** Line 11 in v4 is a single sentence of urgency framing following an enumerated line 9. Read aloud, the prompt still flows as onsite-PM prose (trigger paragraph -> context recap -> due-diligence framing -> enumerated asks -> closing urgency). Not bullet-list, not command-list. Contrived remains 5/5. Perspective: Architect.

**B2 verdict:** GO. Zero adversarial divergences in v4. Two new phrasings (Diane anchor + operational closing line) both robust to second-reading attack; five carried alt-paths all still zero-divergence.

---

## B3 — Tool-Call Density Re-Projection (v4)

### Verification: does v4 touch density-relevant surface?

- **Write asks:** 8 writes unchanged (Airtable ticket update, Linear save_issue + save_comment, Slack thread reply, 3 Gmail drafts, GCalendar event).
- **Discovery asks:** unchanged. L2 push ("actually go through Diane's diagnostic write-up on the bill itself") unchanged. L5 forced thread-read ("tenant thread I had going") unchanged.
- **Lever mechanics:** unchanged. See B4 table.
- **Word trims:** ~38 words removed across full prompt without removing any lever-firing signal or discovery ask.

### Per-service breakdown (v4, same as v3)

| Service | Discovery calls | Write calls | Subtotal | Delta vs v3 |
|---|---:|---:|---:|---|
| slack | 5-7 (channel list, search, thread-get x 2, latch check) | 1 (reply in Carlos's thread) | **8-10** | 0 |
| airtable | 5-7 (bases, tables, search, schema, record get) | 1 (ticket update) | **7-9** | 0 |
| linear | 5-7 (workflow states, teams, list_issues, get_issue) | 2 (save_issue + save_comment) | **7-9** | 0 |
| gmail | 3-5 (search_threads, get_thread) | 3 (drafts x 3) | **6-8** | 0 |
| quickbooks | 5-7 (list_entities VendorRef=201, get_entity x 2-3 for diagnostic bill) | 0 | **5-7** | 0 |
| contacts | 3-5 (search x 3-4) | 0 | **3-5** | 0 |
| gcalendar | 2-3 (list_calendars, optional list_events conflict check) | 1 (create_event) | **3-5** | 0 |
| hubspot | 1-3 (optional owner Robert Finley lookup) | 0 | **1-3** | 0 |

**Total projected: 40-56 calls, midpoint ~49-50** (unchanged from v3).

### Tier verdict

- **v4 re-projected midpoint: ~49-50** (unchanged from v3; no density-affecting surface touched).
- **Tier: THIN carry** (boundary at 50, midpoint 49-50).
- **AUDIT F3 resolution verified:** THIN carry now documented in `_aux/Hardness_Plan.md:61-67` per verdict criteria. Footnote captures re-projection rationale + explicit carry acceptance grounds (6-lever buffer, further consolidation risks UGT regression, 8-service breadth PASS). Verdict criteria "documented in Hardness_Plan.md" now SATISFIED.

**Service breadth:** 8 distinct services still >= 3 calls each (hubspot at 1-3 remains soft-optional). Breadth gate PASS.

---

## B4 — Hardness Preservation (6 selected levers, v4)

| Lever | v3 Status | AUDIT | **v4 Status** | Regression check evidence |
|---|---|---|---|---|
| **L1 Latching** (Unit 14 decoy) | PRESERVED | PRESERVED (STRONG) | **PRESERVED** | v4 does not touch Mesa Vista 7B specificity (line 1) or "older unit" broad-diligence framing (line 7). Any broadening still surfaces Tommy Reyes / Unit 14 records. NOT REGRESSED. |
| **L2 QB structured-DB skip** | PRESERVED / STRENGTHENED | PRESERVED (STRONG) | **PRESERVED / STRENGTHENED** | v4 does not touch line 7: "actually go through Diane's diagnostic write-up on the bill itself and check whether the detail she has captured lines up with the summary she and Tony are talking off of". Explicit L2 push toward QB `Line[0].Description` unchanged. NOT REGRESSED. |
| **L5 Thread-reply blindness** | PRESERVED | PRESERVED (STRONG) | **PRESERVED** | v4 does not touch line 5's "I dropped an update into the tenant thread I had going but I have not touched the actual maintenance ticket yet". Content-must-read mechanism intact. Escalation content still confined to Slack record 4. NOT REGRESSED. |
| **L7 Multi-write diversification** | PRESERVED | PRESERVED (STRONG) | **PRESERVED** | All 8 write asks (Airtable, Linear x 2, Slack reply, Gmail x 3, GCalendar) present and unchanged in line 9. Trim did not touch closing enumeration. NOT REGRESSED. |
| **L8 Multi-link chain** | PRESERVED | PRESERVED (STRONG) | **PRESERVED** | Slack thread -> Airtable ticket -> Linear issue -> QB bill line description chain still fully requested. NOT REGRESSED. |
| **L9 Authority dismissal** | PRESERVED | PRESERVED (STRONG) | **PRESERVED** | Tony's authority endorsement in line 3 ("Tony posted... endorsing that scope, said the tank held pressure on the hold test and it keeps us on Robert's June budget. He was going to sign off if nobody flagged it by end of business yesterday") unchanged. Carlos's neutral due-diligence framing ("Standard practice on an older unit") in line 7 unchanged. NOT REGRESSED. |

**B4 verdict:** GO. All 6 selected levers PRESERVED. v4 edits touched only closing-line operational framing + Diane's first-mention anchor + minor trim + Hardness_Plan documentation — none touched a lever-firing span. NO REGRESSION on any lever.

---

## B6 — Upstream Propagation

**No PROPAGATE flags raised.** v4 changes are all in-prompt textual edits + one Hardness_Plan documentation update.

- Hardness_Plan.md: **updated with THIN carry footnote** (AUDIT F3 resolution). No re-run of HARDNESS phase needed; the update is a documentation-only addendum recording an already-accepted density posture.
- Injection plan / actual injection: unchanged, no re-execution needed.
- S0 setup: unchanged.
- v4 does not affect OE or rubrics drafting surface — S2 / S3 will read the corrected prompt and the same universe data as v3.

---

## Anti-Pattern Sweep (v4 delta from v3)

| Anti-pattern | v3 Hit? | AUDIT | **v4 Hit?** | Delta rationale |
|---|---|---|---|---|
| Clone tonality | No | No | **No** | Neither v4 edit introduces "loop in" / "surface every" / "CC our CEO" phrasing. |
| Enumerated action list disguised as prose | No | No | **No** | Line 9 structure unchanged; line 11 trim didn't add bullet structure. |
| Over-signaling investigation | No | No | **No** | No generic "check our systems" phrasing added. |
| Formulaic closing | No | No | **No** | Line 11 closing rewrite reads as tactical urgency, not template. |
| Generic urgency | No | No | **No** | Specific urgency ("Thursday morning" install slot) preserved. |
| Em-dashes | No | No | **No** | `grep -c` on v4 prompt: 0 em-dashes. |
| Tool names in prompt | No | No | **No** | Both v4 edits use natural language. |
| Over-500-word cap | No (~424) | WARN (>400 pref) | **No (386)** | Word count trimmed from 424 to 386 — now under 400 sweet-spot AND under 500 hard cap. AUDIT F4 resolved. |
| Passive-voice ambiguity | No | No | **No** | Line 11 "Parts need pulling today" passive; implicit subject Hill Country is established via "so Hill Country's ready". No action-flip ambiguity possible. See B2 Q2. |
| Named-entity false attribution | (Truthfulness slip carried) | Truthfulness 4/5 | **CLEAN** | v4 closing line has zero named-entity attribution; Diane-Wed-EOD-attribution eliminated. |
| Under-specified named entity | (accepted, charitable) | Clarity 4/5 | **CLEAN** | v4 Diane anchor adds vendor + role disambiguators. |

**Sweep verdict:** All clean. **v4 improves anti-pattern posture on 3 axes vs AUDIT (word count, named-entity attribution, entity under-specification).**

---

## Per-Lens Verdict Roll-up (v4)

| Lens | v3 Verdict | AUDIT | **v4 Verdict** | Findings mapped |
|---|---|---|---|---|
| **Architect** | PASS | PASS | **PASS** | Three-movement structure intact after trim; edits are targeted line-level fixes. |
| **Implementer** | PASS | PASS | **PASS** | All 8 writes still resolvable; Diane Draft target unambiguous via Gmail thread sender. |
| **Red-team** | PASS | PASS with 2 sub-dim 4/5s | **PASS** | 8 adversarial readings tested (3 new + 5 carried); zero divergences. |
| **Ground-truth** | PASS with 1 minor slip carried | REVISE (Truthfulness 4/5, Clarity 4/5) | **PASS (CLEAN)** | All v4 edits verified against universe. Truthfulness + Clarity both recover to 5/5. |
| **Integration** | PASS with THIN carry | REVISE (THIN not codified) | **PASS with THIN carry (CODIFIED)** | Density posture unchanged; THIN carry now documented in Hardness_Plan.md. |

**Combined verdict:** GO. All lenses PASS; Ground-truth + Integration both upgraded from REVISE to PASS.

---

## Consolidated Findings (v4)

| # | Severity | Perspective | Issue | Status |
|---|---|---|---|---|
| 1 | **Advisory / THIN carry** | B3 | Density midpoint remains ~49-50, right at 50+ boundary. | **CODIFIED** in Hardness_Plan.md:61-67 per AUDIT F3 requirement. No further action. |

**No new findings.** All AUDIT REVISE findings (F1, F2, F3, F4) resolved. THIN density carry now properly documented per verdict criteria.

---

## OVERALL VERDICT: GO

**Truthfulness sub-dim RECOVERED from 4/5 (AUDIT) to 5/5** — v4 closing line has no named-entity attribution, eliminating the Diane-Wed-EOD forward drift. **Clarity & Specificity sub-dim RECOVERED from 4/5 (AUDIT) to 5/5** — v4 Diane anchor "AP contact at Hill Country" adds vendor + role disambiguators neutralizing the base-universe Diane Flores (Lonestar) collision, and the Draft action target resolves via the Gmail thread sender independently of contacts lookup. All 12 applicable QC sub-dims now >= 5. All 6 selected Hardness Plan levers PRESERVED (L1, L2, L5, L7, L8, L9 — none regressed by v4 edits, all still firing end-to-end). Adversarial B2 sweep produces zero divergences across 8 candidate alt-paths (3 new + 5 carried). Density unchanged at ~49-50 midpoint; **THIN carry now formally codified in `_aux/Hardness_Plan.md:61-67` per AUDIT F3 requirement** (verdict criteria "documented in Hardness_Plan.md" SATISFIED). Word count trimmed to **386 words** (was 424; under 400 sweet-spot preference AND under 500 hard cap — AUDIT F4 resolved). Zero em-dashes. No upstream propagation flags. No new anti-patterns introduced; three anti-pattern axes improved vs AUDIT (word count, named-entity attribution, entity under-specification).

Proceed to S1 AUDIT (strict-veteran re-verification of v4). On AUDIT PASS, proceed to S2 (Oracle Events drafting). No S1.5 linter round needed.
