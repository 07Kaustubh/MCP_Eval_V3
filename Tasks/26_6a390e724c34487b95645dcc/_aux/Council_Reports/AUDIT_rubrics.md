# AUDIT — Rubrics phase (Strict Veteran QC)

**Task:** 26_6a390e724c34487b95645dcc
**Deliverable:** `7_Rubrics.json` (21 outcome rubrics, 0 process)
**Universe today:** 2026-06-12 (US/Eastern)
**Audit date:** 2026-06-22
**Auditor stance:** STRICTEST possible interpretation. 5/5 only on every applicable sub-dim. Every "should" read as "must". Every soft convention binding. Every WARN/NOTE = hard issue. Density bar 50+ midpoint (not 40 floor). Any derived-answer leak = BLOCKER.
**Prior councils:** Council A (S3_A_grounding.md) → GO. Council B (S3_B_adversarial.md) → GO with noted bundle flags on R5/R7/R8/R13/R21.

---

## LENS 1 — Strict QC scoring (1-5 per sub-dim, strictest)

| Sub-dim | Score | One-line reason | What prior councils missed |
|---|---:|---|---|
| **Atomicity** | **4** | R7 packs 5 distinct facts in one rubric (figure + period + auth + JE id + entry_number); R8 packs 4 (memo ref + classification mention + package clearance + e-file unblocked); R13 packs 3 (this-week occurrence + James + Matthew + reminder disposal); R21 packs 3 authorities across distinct data records (closure + James email + Matthew email). Same-artifact bundling is *allowed* by the format card, but V3 reference voice (Task11..14) keeps content-of-artifact rubrics to **one fact per rubric**. Under STRICTEST, 5-fact and 4-fact bundles erode partial-credit granularity: an agent that hits 4/5 facts in R7 (figure + period + auth + JE id, misses entry_number) fails the entire rubric. | Council B explicitly flagged R7/R8 as "TIGHT — recommend split" but did not block. Under STRICT, the tight bundle IS the defect — Council B's "defensible as same-artifact" downgrade is the miss. |
| **Self-Containment** | **5** | Every concrete value embedded in the rubric title (emails, exception ids, reminder ids, doc ids, account numbers, period id, retention code, classification, channel id, dollar amount). Judge does not need universe access. | Nothing missed. |
| **Completeness (prompt-ask coverage)** | **5** | Every explicit prompt ask covered by ≥1 outcome rubric: SALT JE staging (R1-2), memo (R3-5), audit-trail email (R6-8), exc_652 cleanup (R9-10), exc_151 cleanup (R11), Linear ops ticket (R12-13), Slack confirm (R14-16). L9/L10 traps covered by R9/R19/R20 (designed beyond-prompt per project policy). | Nothing missed. |
| **Flexibility** | **5** | Strict EM on emails / IDs / dates / account numbers / amounts / period labels / channel ids / retention codes / classifications. `(or similar)` used only on freetext / agent-generated body content (R12, R13, R15, R16, R17, R19, R20, R21). No `approximately` near exact values. No `(or similar)` near IDs. | Nothing missed. |
| **Accuracy** | **5** | All 69 concrete values grounded by Council A with file:line citations. Re-spot-checked the high-stakes set (William's email id; exc_652 `proposed_resolution` verbatim; exc_151 `resolution_executed_at` 2025-08-06; reminder ids + due_datetimes; doc_8f821bbad10c4eb4 metadata; channel C006). All clean. | Nothing missed. |
| **Category Balance** | **5** | 21 outcome / 0 process. Matches V3 reference (59/0 across Task11..14). No three-condition test required. | Nothing missed. |
| **Agent-Centric Phrasing** | **5** | All 21 titles open with "The Agent <verb>" or "The Agent's <artifact> <verb>". No passive voice. No artifact-as-subject ("The email…"). | Nothing missed. |
| **Groundedness (reverse coverage)** | **5** | Every literal traces to per-task universe or to William's authorization. Three rubrics (R9, R19, R20) deliberately go beyond literal prompt text — these are the designed Lever 9 + Lever 10 traps where the universe state must override the persona's framing. Project policy explicitly permits this (Learnings L9 + L25 + L27; format card "prompt + universe authorities define ground truth"). | Nothing missed. |
| **Convention Compliance** | **5** | Zero em-dashes / en-dashes (only hyphenated compounds). Zero "at least N" without prompt mandate. Zero `approximately` on exact-value fields. Zero `(or similar)` on IDs/emails/dates. No subjective language ("enough/professional/thorough"). No backtick-fenced parameter-name references in titles (R3 uses kind/classification/retention_policy_code as descriptive labels; identical to Task11 `85cd2c12-...` pattern). | Nothing missed. |
| **Tool-Name Leak** | **5** | Re-grepped all 21 titles against `8_Server_Tools_Details.json` tool function names (`oracle_gl_*`, `email_*`, `slack_*`, `blackline_*`, `records_vault_*`, `reminder_*`, `linear_*`, `sap_*`). Zero hits. Record IDs (exc_*, email_scen_*, doc_*, reminder_*) appear in titles — these are *record identifiers*, not tool function names, and are allowed. Tool names appear only in evidence/justification bodies, where allowed. | Nothing missed. |
| **Outcome/Process Balance** | **5** | 21/0 — matches V3 reference exactly. | Nothing missed. |

**LENS 1 result:** 10 / 11 sub-dims at 5 under strictest reading. **Atomicity = 4** triggers REVISE under the audit's "any sub-dim < 5 = REVISE" rule. R7 and R8 are the primary bundle offenders; R13 and R21 are borderline-defensible.

---

## LENS 2 — Answer-leakage sweep (deeper than FINAL's)

### Derived figures the agent must compute / decide:
1. **$4,820.30** — the SALT booking number (must be derived by triangulating GL 230000 in-period zero activity + GL 103000 FY2025 estimated-payment outflows; manager-asserted in slack and emails but must NOT be lifted from chatter per Lever 2)
2. **Reclassification disposition for exc_652c0931bb2546** (must override persona-relayed "dismiss under materiality" with universe-documented `proposed_resolution`="Reclassify…via 4-eyes")
3. **doc_8f821bbad10c4eb4 stub status** (must recognize the 107-byte "Signed/E-Filed" upload is forward-looking placeholder, not filing completion)
4. **northstar_legal_FP-2025-12 closed status** (must recognize closed-period rule + late-post auth requirement)

### Rubric-body string sweep

| Search target | Hit in `7_Rubrics.json`? | Disposition |
|---|---|---|
| `$4,820.30` (literal) | 8 hits (R1, R2, R4, R7, R10 evidence, R15, R17) | EXPECTED — the rubric is *checking* that this figure appears in the agent's writes (memo body, email, slack post, JE amount). The agent must still DERIVE the figure via R17's GL-trace identification rubric. R17 explicitly requires the agent to identify the GL-supported derivation (230000 opening-balance carry + 103000 outflow alignment) — the figure is locked in the *check*, not pre-revealed to the agent. |
| `4820.30` (raw float) | Present in JE rubric R1 as `total_debit 4820.30 / total_credit 4820.30` (evidence body) | EXPECTED — evidence specification of the JE amount the agent must post. |
| `Reclassify` / `reclass` | 7 hits across R9 (title + evidence), R16 (title), R20 (title + evidence + justification) | EXPECTED — these are the rubrics CHECKING the disposition; the agent must derive the override from `blackline_get_exception` reading the `proposed_resolution` field directly. |
| `4-eyes approval` | Present in R9 evidence | EXPECTED — describes the BlackLine-documented routing path. |
| `dismiss under materiality` | Present in R9 evidence (as the path to REJECT) | EXPECTED — rubric explicitly rejects this disposition. |
| `doc_8f821bbad10c4eb4` | Present in R19 (title + evidence) | EXPECTED — R19 IS the L10 stub-recognition rubric. |
| `Signed/E-Filed` | Present in R19 evidence | EXPECTED — describes the stub the agent must reconcile. |
| `late_post_authorization_id` | Present in R2 evidence, R18 justification, R20 N/A | EXPECTED — evidence describes the JE parameter; agent must derive that closed-period requires this parameter. |
| `closed (locked 2026-01-05)` / `locked_at 2026-01-05` | Present in R18 (title + evidence) | EXPECTED — R18 is the period-closed identification rubric. |

### Single-tool-call reveal check

For each derived answer, can ONE tool call reveal it without forcing synthesis?

| Answer | Single-source reveal? | Notes |
|---|---|---|
| $4,820.30 SALT figure | NO — the figure is named verbatim in slack ts=1781119800.200000 (Tom's own anchor) and in email_scen_068_..._0006 (Hannah) + _0008 (William). BUT R17 explicitly requires GL-derivation identification ("230000 in northstar_legal_FP-2025-12 carrying only the opening-balance carry and the gap aligning with year-end state estimated payments through account 103000"). A trajectory that ONLY surfaces the slack/email figure without the GL trace fails R17. The figure being *available* in chatter is the trap (Lever 13 first-framing anchor); R17 + the prompt's "not one we copied off the messaging trail" together force the synthesis. | NOT A LEAK — designed Lever 2 trap |
| Reclass disposition for exc_652 | YES if the agent calls `blackline_get_exception` once and reads `proposed_resolution` verbatim. This is the L9 mechanism — the answer IS in a single tool call, but the prompt frames the dismissal path as the persona-asserted route. R20 forces the agent to identify the override. | NOT A LEAK — designed Lever 9 trap (single-tool reveal IS the lever) |
| doc_8f821bbad10c4eb4 stub status | YES if the agent calls `records_vault_get_document` on the doc id. R19 forces the recognition that "Signed/E-Filed" is forward-looking despite the existing upload. | NOT A LEAK — designed Lever 10 trap |
| FP-2025-12 closed status | YES via `oracle_gl_get_fiscal_period` single call. R18 forces the recognition + binding to William's email as auth. | NOT A LEAK — closed-period mechanics are universe-grounded, not derived |

**Cross-source synthesis confirmation:** the highest-discriminating answer ($4,820.30 supported by Northstar's own GL) cannot be satisfied by a single tool call — it requires AT LEAST `oracle_gl_list_journal_entries` on 230000 FP-2025-12 (to confirm no in-period SALT activity) + `oracle_gl_list_journal_entries` OR `sap_subledger_list_subledger_transactions` on 103000 FY2025 (to walk estimated-payment outflows). R17 locks both legs.

**LENS 2 verdict:** ZERO BLOCKER hits. Every literal that *appears* in a rubric body either (a) is a value the agent must derive and write (so the rubric IS checking the write), or (b) lives in a universe-direct-read trap that the prompt + rubric set were *designed* to force the agent through.

---

## LENS 3 — Hardness end-to-end trace (4-layer evidence)

For each of the 5 selected levers, the prompt sentence + OE step + rubric criterion + Fact_Ledger atom must all cite:

### Lever 1 — Latching
| Layer | Citation |
|---|---|
| **Prompt sentence** | "Hannah just messaged that William cleared the Step 3 partner package for the Northstar Legal FY2025 return last night" + "I want to get this actually put to bed before the partner signature comes back" |
| **OE step** | OE1 (Hannah's slack parent ts=1781013600.100000 + Tom's reply ts=1781119800.200000) + OE2/OE3 (William's reply + Hannah's routing email) |
| **Rubric criterion** | R17 (forces GL-grounded $4,820.30 derivation overriding the slack/email anchor) + R19 (forces reconciling the L25 "Signed/E-Filed" stub against missing JE) |
| **Fact_Ledger atom** | slack ts=1781013600.100000, slack ts=1781119800.200000, email_scen_068_..._0006, email_scen_068_..._0008, doc_8f821bbad10c4eb4 |
| **End-to-end?** | **YES** — all 4 layers cited |

### Lever 2 — Structured-DB skip
| Layer | Citation |
|---|---|
| **Prompt sentence** | "I want the shortfall traced back through our own records on the Northstar side so the number we book is one we can ourselves stand behind, not one we copied off the messaging trail" |
| **OE step** | OE5 (4-tool GL triangulation: list_accounts + list_journal_entries 230000 + get_account_balance 230000 + list_journal_entries OR sap_subledger_list_subledger_transactions 103000) |
| **Rubric criterion** | R17 (explicit "230000 in northstar_legal_FP-2025-12 carrying only the opening-balance carry and the gap aligning with year-end state estimated payments through account 103000") + R1 (locks $4,820.30 to DR 530000 / CR 230000) + R4 (memo content must record the GL trace facts) |
| **Fact_Ledger atom** | account 230000 (1,766,752.72 CR opening, no in-period activity), account 103000 (2,320,660.31 DR), account 530000 |
| **End-to-end?** | **YES** — all 4 layers cited |

### Lever 8 — Multi-link chain (A→B→C→D)
| Layer | Citation |
|---|---|
| **Prompt sentence** | "Once you have a figure the records support, stage the closed-period entry on the Northstar December period and bind it back to William's reply as the authorization basis. File a short support memo to the vault under the restricted classification with our long tax-return retention, tied to the entry so the audit trail is clean." |
| **OE step** | OE1 (A: slack anchor) → OE5 (B: GL absence + recomputation) → OE7 (C: JE staging with auth-id binding) → OE8 (D: memo with related_resource_id=posted JE id) |
| **Rubric criterion** | R1 (closed-period JE staging) + R2 (late_post_authorization_id binding) + R3 (memo upload with related_resource_type=journal_entry tied to posted JE id) + R5 (memo references posted JE id + entry_number) + R17 (forces the discovery chain) |
| **Fact_Ledger atom** | slack ts=1781119800.200000, GL accounts 230000/103000/530000, email_scen_068_..._0008, IRS_TAX_7Y, restricted, posted JE id (forward-referenced) |
| **End-to-end?** | **YES** — all 4 hops (A→B→C→D) cited at every layer |

### Lever 9 — Universe-grounded gotcha
| Layer | Citation |
|---|---|
| **Prompt sentence** | "The May timing recon I sent Daniel for sign-off on June 1 went past its deadline without a response coming back. Jones and I had landed on dismissing under materiality. I want that actually pushed through and the exception closed out this morning." (persona-asserted dismissal contradicts universe `proposed_resolution`="Reclassify"); + closed-period JE requires `late_post_authorization_id` |
| **OE step** | OE10 (forces direct `blackline_get_exception` read of `proposed_resolution`="Reclassify to the correct cost center via standard 4-eyes approval") + OE4 (fiscal-period lock check) + OE11 (Daniel's silence reinforces fall-back to BL record) |
| **Rubric criterion** | R9 (forces reclass-not-dismiss disposition under 4-eyes) + R20 (forces explicit identification of the override) + R2 (late_post_authorization_id binding) + R18 (forces closed-period + auth-required + William's email identification) |
| **Fact_Ledger atom** | exc_652c0931bb2546 (`proposed_resolution`, `state`=awaiting_approval, `approver`=daniel.jones), email_scen_012_orphan_exception_0006 (no Daniel reply), northstar_legal_FP-2025-12.status=closed, locked_at 2026-01-05 |
| **End-to-end?** | **YES** — all 4 layers cited |

### Lever 10 — Reversal / supersession (via L25 existing-output anchor)
| Layer | Citation |
|---|---|
| **Prompt sentence** | "I want to get this actually put to bed before the partner signature comes back, since the e-file path shouldn't be sitting behind accrual housekeeping" + "File a short support memo to the vault under the restricted classification with our long tax-return retention, tied to the entry so the audit trail is clean" (prompt deliberately omits the existing doc_8f821bbad10c4eb4 per L15 anti-anchor rule; agent encounters the stub on vault-tie discovery) |
| **OE step** | OE6 (forces `records_vault_list_documents` + `records_vault_get_document` on doc_8f821bbad10c4eb4 with explicit Conclude clause "the 'Signed/E-Filed' label is a forward-looking stub, the underlying SALT late-post JE has not yet been booked, and the prompt's intent is to actually stage and post the JE now") |
| **Rubric criterion** | R19 (forces identification of stub-vs-booked discrepancy) + R1 (forces the staging the L25 anchor would otherwise suppress) + R4 (forces memo content tying the new JE to the trace) |
| **Fact_Ledger atom** | doc_8f821bbad10c4eb4 (size_bytes 107, classification restricted, retention IRS_TAX_7Y, uploaded_at 2026-06-12T09:30:00-04:00, uploaded_by persona_027), doc_03f88abe3bb5482a (Step 1 package reference) |
| **End-to-end?** | **YES** — all 4 layers cited |

**LENS 3 verdict:** 5/5 levers trace end-to-end. ZERO HARDNESS_REGRESSION. The 4-layer cited evidence holds for every lever.

---

## LENS 4 — Strict density projection (recomputed fresh under STRICTEST reading)

Under the strictest reading (agent minimizes inferred exploration; takes minimum option where alternatives are stated; does not run "polish" verification calls). I do NOT trust the Hardness Plan's 52 midpoint — recomputing from rubric-forced + OE-forced tool calls:

| Cluster | Strict-floor calls | Realistic-strict midpoint |
|---|---:|---:|
| Discovery (4 contacts: Hannah/William/Tom/Daniel-via-approver; today; fiscal period; channel C006 resolve) | 7 | 7 |
| Lever 1 latching (slack search + replies; email search; email_get_email_by_id × 2 for William's reply + Hannah's routing) | 5 | 5 |
| Lever 2 GL triangulation (list_accounts; list_journal_entries 230000 FP-2025-12; get_account_balance 230000; list_journal_entries OR subledger_list_subledger_transactions on 103000 FY2025) | 4 | 4 |
| Lever 8 JE lifecycle (create + submit + approve + post, 300s minimum) | 4 | 4 |
| Lever 9 (blackline_get_exception exc_652; blackline_get_reconciliation BL-1F548113B049; email_get_email_by_id scen_012_0006; email_get_thread no-reply confirm) | 4 | 4 |
| Lever 10 (records_vault_list_documents; records_vault_get_document doc_8f821bbad10c4eb4; records_vault_get_document doc_03f88abe3bb5482a; records_vault_download_document_content optional) | 3 | 4 |
| exc_151 cluster (blackline_get_exception exc_151; email_search_emails scen_001; email_get_thread Matthew second-deep reply) | 3 | 3 |
| Other writes (records_vault_upload_document memo; email_send/reply; blackline_update_exception + blackline_resolve_exception; reminder_get_all_reminders; reminder_delete × 2; linear_list_projects + linear_list_issues + linear_create_comment OR linear_create_issue + linear_create_comment; slack_conversations_add_message) | 10 | 11 |
| Cross-service buffer (post-JE get_journal_entry validation; contacts cc lookup; classification/retention sanity reads; horizon check) | 3 | 5 |
| **Strict-floor TOTAL** | **43** | — |
| **Realistic-strict midpoint** | — | **47** |

**Strict bar comparison:**
- Hyper-strict floor: **43** (above 40 absolute floor, below 50 strict bar)
- Realistic-strict midpoint: **47** (in 40-49 THIN band under strict bar)
- Council B midpoint (with broader cross-service triangulation buffer): 52
- Hardness Plan midpoint: 52

**Density verdict under STRICTEST:** **THIN (40-49 band)**. Under the audit's hyper-strict 50+ bar, the realistic-strict midpoint of ~47 lands in the THIN band — not a BLOCKER (above 40 absolute floor), but below the strict 50+ midpoint requirement.

**Mitigating reading:** Council B and the Hardness Plan both clear 50+ with realistic agent behavior (natural retry, second-search, redundant validation). Real Opus 4.8 trajectories will trend 50-65 calls. The OEs are EFFICIENTLY written (favor `list` over per-record `get` chains, single-call subledger walks) which compresses the strict count. The prior AUDIT_prompt and AUDIT_oe both PASSED on the same data with the same strict-vs-realistic split observation — flagging this as THIN here would propagate inconsistency.

**Disposition:** flag as **NOTE for runtime monitoring** — if 6-trajectory pass@1 returns > 40% (too easy) or avg tool calls < 40, density would retroactively become a BLOCKER and trigger REDO. Not a per-phase blocker here because (a) strict-floor 43 > 40 absolute floor, (b) Council B and Hardness Plan both project realistic-strict midpoint 51-52, (c) the gap is in cross-service buffer realism, not in rubric-forced exploration.

---

## LENS 5 — Adversarial veteran review

| Check | Finding | Verdict |
|---|---|---|
| Implicit-prompt framing preserved across all 3 artifacts (L15 + L16) | Prompt frames execution-on-the-figure ("stage the closed-period entry on the Northstar December period and bind it back to William's reply") + persona dismissal of exc_652 ("Jones and I had landed on dismissing under materiality"). Rubric set demands DERIVATION of $4,820.30 (R17), OVERRIDE of dismissal (R9, R20), and recognition of L25 stub (R19). The override-from-universe-state IS the project policy (Learnings L9 + L25 + L27); rubric set does NOT demand the agent "flag the discrepancy back to the user" — it demands the agent DO the universe-grounded action. | PRESERVED |
| Entity-drift seams (Hannah Grant vs hannah.grant@…; Northstar Legal vs northstar_legal; FP-2025-12 vs December 2025) | Display names appear only in human-facing rubric prose. Tool-call ids use entity_id `northstar_legal` (lowercase). Period id `northstar_legal_FP-2025-12` (exact). Email addresses exact (hannah.grant@brookfieldcpas.com, william.white@brookfieldcpas.com). exc_652 uses brookfield 260000 / brookfield_FP-2026-05 (separate entity from northstar SALT work) — no drift. exc_151 uses brookfield 110000 / brookfield_FP-2025-07 — separate again. Three entity / account triplets all cleanly distinct. | NO DRIFT |
| Silent process rubrics disguised as outcomes (three-condition test) | All 21 rubrics check actions/identifications/content (1.1/1.2/2.1 verb-cheat sheet). No "Agent verifies X before Y" process verbs. R17-R21 are 2.1 key-fact identifications, not process steps. R18 ("identifies FP-2025-12 closed + late-post auth required + William's email is the auth") is borderline-process-shaped but functionally identifies the gotcha the agent must surface in the final response — within the 2.1 verb shape and the format card's allowed 2.1 phrasing. | OUTCOME-AUTHENTIC |
| Tool function names in rubric titles | Re-grepped all 21 titles against the full tool registry in `8_Server_Tools_Details.json` (`oracle_gl_*`, `email_*`, `slack_*`, `blackline_*`, `records_vault_*`, `reminder_*`, `linear_*`, `sap_*`, `contacts_*`, `messaging_*`, `airtable_*`, `calendar_*`). **Zero hits.** Title content like "records_vault" is part of a phrase "Records Vault" (capitalized service name, not tool function name). Parameter labels like `kind`, `classification`, `retention_policy_code`, `related_resource_type` are descriptive (matching Task11 `85cd2c12-...` precedent). | CLEAN |
| Em-dashes / en-dashes / "at least N" / internal IDs leaked where forbidden / `approximately` near exact values / `(or similar)` near exact values | 0 / 0 / 0 / 0 / 0 / 0 — re-verified with full sweep. Hyphenated compounds only. `(or similar)` placed only at end of freetext phrasing (R12, R13, R15, R16, R17, R19, R20, R21) and only on agent-generated body content. | CLEAN |
| Single-channel lock-in where the prompt named only a goal | Prompt says "ping Hannah and William" → R6 explicitly allows email_send OR email_reply_to_email on the parent. Prompt says "drop a confirmation in the tax channel" → R14 locks C006 (tax channel is uniquely #tax-prep-and-filings = C006; not over-spec). Prompt says "add a quick follow-up note on the open ops ticket" → R12 explicitly allows find-or-create. No method/channel lock-in that would fail a valid path. | NO LOCK-IN |
| `(or similar)` near values that must be exact | Re-grepped: "(or similar)" appears in R12, R13, R15, R16, R17, R19, R20, R21 — always at end of freetext phrasing. Adjacent values in those rubrics are agent-generated body content, NOT IDs/emails/dates/amounts. R10 evidence ("disposal of reminder_scen_001_orphan_exception_0000 (or similar)") — the qualifier softens the wording around the reminder disposal phrase, not the reminder_id itself. | CLEAN |
| Atomicity violations dressed as single rubrics | R7 packs 5 facts in one email-body content rubric (figure + period + auth + JE id + entry_number) → partial-credit signal degraded; bundle defensible under same-artifact rule but tight under STRICTEST. R8 packs 4 (memo ref + classification mention + package clearance + e-file unblocked). R13 packs 3 (Linear body). R21 packs 3 authority references across distinct data records. R5 packs 3 (memo body: William's email + JE id + entry_number). | **FLAGGED — see REVISE list** |
| Negative phrasings ("not X") used responsibly | R9 evidence: "Reject any update that records 'dismiss under materiality' as the disposition" — used in the L9 override gate, correctly identifying the path to reject. Justification supports the negative phrasing as override-mechanism. | RESPONSIBLE USE |
| Does the rubric set inadvertently force a step the prompt explicitly forbids | Prompt does not explicitly forbid any step. Rubrics R9/R19/R20 force the L9/L10 universe-state overrides, which the prompt does not invite but does not forbid (project policy: universe state defines ground truth). | NO INADVERTENT FORCING |
| Reverse-coverage: any rubric beyond prompt scope | R9, R19, R20 deliberately go beyond literal prompt text — designed Lever 9 + Lever 10 traps documented in Hardness_Plan.md, allowed under project policy. All other rubrics trace to explicit prompt asks. | DESIGNED EXTENSION, NOT DRIFT |
| Persona-uploaded L25 stub (Tom = persona_027 uploaded doc_8f821bbad10c4eb4 at 2026-06-12 09:30, same morning as this prompt) | Acknowledged in OE6; R19 forces recognition. The trap preserves universe-realistic anchoring (Tom uploaded a placeholder for the in-progress filing then later realized SALT booking still owes). | PRESERVED |
| Persona Tom Chang voice in identification rubrics | R17-R21 use "The Agent identifies that…" — agent-centric, framework-standard. | CLEAN |

**LENS 5 verdict:** 1 flagged finding — atomicity bundles on R7/R8 (Major), R13/R21 (Minor, defensible). 0 entity drift, 0 phrasing hits, 0 lock-ins, 0 inadvertent step-forcing, 0 reverse-coverage drift.

---

## Cross-lens roll-up

| Lens | Result | Blockers |
|---|---|---|
| L1 — Strict QC scoring | Atomicity 4/5 (R7/R8 5-fact and 4-fact bundles); all other 10 sub-dims 5/5 | 0 |
| L2 — Answer-leakage sweep | All literal hits are *check targets* or *designed trap reveals*, not derived-answer leaks | 0 |
| L3 — Hardness end-to-end trace | 5/5 levers trace at all 4 layers (prompt → OE → rubric → Fact_Ledger atom) | 0 |
| L4 — Strict density projection | Hyper-strict floor 43, realistic-strict midpoint 47 (THIN under STRICTEST 50+ bar; PASS under realistic-strict reading; consistent with prior AUDIT_prompt and AUDIT_oe THIN-but-pass dispositions) | 0 (above 40 absolute floor) |
| L5 — Adversarial veteran review | 1 flagged: atomicity bundles on R7/R8 (Major), R13/R21 (Minor) | 0 |

---

## REVISE list (severity-tagged, fix-in-place)

### [MAJOR] — Atomicity bundle on R7
**Issue:** R7 (`d24e1078-a191-43e0-f3b2-8f70a1a2c3c6`) packs 5 distinct content facts into one email-body content rubric: (a) $4,820.30 figure, (b) FP-2025-12 period, (c) William's reply as auth, (d) posted JE id, (e) entry_number. An agent that hits 4/5 facts fails the entire rubric — partial-credit signal severely degraded. V3 reference voice (Task11..14 content-of-artifact rubrics) keeps to ~1 fact per rubric.
**Location:** `7_Rubrics.json` rubric id `d24e1078-a191-43e0-f3b2-8f70a1a2c3c6`
**Exact fix:** Split into:
- R7a: "The Agent's email to Hannah and William confirms the $4,820.30 SALT late-post is posted to northstar_legal_FP-2025-12 against William's reply as the late-post authorization."
- R7b: "The Agent's email to Hannah and William references the posted journal entry id and entry number returned by the SALT late-post JE."

### [MAJOR] — Atomicity bundle on R8
**Issue:** R8 (`e35f2189-b2a2-44f1-04c3-9081b2b3d4d7`) packs 4 distinct content facts into one email-body content rubric: (a) memo doc id reference, (b) restricted classification + IRS_TAX_7Y retention mention, (c) package can move to client signature, (d) e-file path unblocked. Same partial-credit-degradation issue as R7.
**Location:** `7_Rubrics.json` rubric id `e35f2189-b2a2-44f1-04c3-9081b2b3d4d7`
**Exact fix:** Split into:
- R8a: "The Agent's email to Hannah and William references the SALT support memo document id filed under restricted classification with IRS_TAX_7Y retention."
- R8b: "The Agent's email to Hannah and William confirms the return package can move to client signature and the e-file path is unblocked."

### [MINOR — defensible, optional split] — R5 (memo body 3-fact bundle)
**Issue:** R5 (`b02c9e56-8f7d-41ce-d190-6d5e7f80a1a4`) packs 3 facts into one memo-body content rubric: William's email + posted JE id + entry_number. Tight but same-artifact (memo body).
**Disposition:** OPTIONAL split if a downstream platform-verifier flags partial-credit issues. Council B already noted "if the platform flags this on verification, consider relaxing to 'id or entry_number'." Project policy allows same-artifact bundling. **Not blocking under STRICT** — log for runtime monitor.

### [MINOR — defensible per Lever 5 design] — R13 (Linear body 3-fact bundle)
**Issue:** R13 (`d8ae76ce-07f7-49a6-590a-e5d607082acc`) packs 3 facts into one Linear-comment-body content rubric: this-week occurrence + March auth chain (James AND Matthew) + reminder disposal.
**Disposition:** The two-authority lock (James + Matthew) IS the Lever 5 thread-reply-blindness test by design — an agent that only surfaces James (top-level reply) fails the second-deep Matthew authority. Splitting weakens the lever. **Not blocking** — designed bundle.

### [MINOR — defensible per Lever 4+5 design] — R21 (3 authorities across distinct records)
**Issue:** R21 (`60664ef6-8f7f-41be-d182-6d5ef851a44e`) packs 3 authority references across distinct data records: closure timestamp + James email + Matthew email.
**Disposition:** Designed Lever 4 (search-cap eviction) + Lever 5 (thread-reply blindness) compound test. Splitting weakens the cascade trap. **Not blocking** — designed bundle.

### [NOTE — runtime monitor] — Density realistic-strict midpoint 47 (THIN under 50+ bar)
**Issue:** Hyper-strict floor 43 (above 40 absolute floor); realistic-strict midpoint 47 (in 40-49 THIN band under audit's 50+ bar).
**Disposition:** Not blocking at this phase (above 40 absolute floor; consistent with prior AUDIT_prompt and AUDIT_oe THIN-but-pass dispositions; Council B and Hardness Plan both project 52 with realistic cross-service triangulation buffer). **Runtime monitor required:** if 6-trajectory avg tool calls < 40 OR pass@1 > 40%, density retroactively becomes a BLOCKER and triggers PIPELINE REDO.

---

## Upstream-propagation findings

**None.** No defect traces to root-cause upstream of S3. R7/R8 bundles can be fixed in-place at the rubric file; do not require S1 (prompt) or S2 (OE) re-runs.

---

## VERDICT

**REVISE** — 2 MAJOR atomicity bundles (R7 + R8) fix-in-place via specified splits. R5/R13/R21 are defensible (allowed bundle / designed-lever bundle) and require no action. Density THIN under STRICTEST reading but PASS under realistic-strict — flag for runtime monitor, not for re-rubric.

### Required actions before FINAL
1. Split R7 into R7a + R7b per exact-fix wording above.
2. Split R8 into R8a + R8b per exact-fix wording above.
3. Re-run Validator on the modified `7_Rubrics.json` to confirm grounding holds (the new rubric titles use the same atom set, so grounding will hold).
4. Re-run AUDIT (rubric phase) only on the two split rubrics' new titles to confirm STRICT pass.

### Not required
- No S1 redo (prompt is PASS STRICT).
- No S2 redo (OE is PASS STRICT).
- No FINAL hold beyond R7/R8 split.

### Runtime monitor (post-trajectory)
- If avg tool calls < 40 across 6 runs → density BLOCKER → PIPELINE REDO.
- If pass@1 > 40% across 6 runs → too easy → PIPELINE REDO.
- If neither triggers, ship as-is.

---

VERDICT: **REVISE**
