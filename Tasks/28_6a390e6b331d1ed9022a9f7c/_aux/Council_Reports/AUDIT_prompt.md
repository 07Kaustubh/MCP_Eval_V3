# Strict Veteran AUDIT — PROMPT phase

**Task:** `28_6a390e6b331d1ed9022a9f7c`
**Deliverable audited:** `Tasks/28_6a390e6b331d1ed9022a9f7c/5_Prompt.txt` (403 words; revised once after Council A round 1; cleared Council A + Council B round 2)
**Date:** 2026-06-25
**Auditor stance:** STRICTEST possible QC interpretation — 5/5 only on every applicable sub-dim; every "should" read as "must"; density bar 50+; every soft convention binding; every WARN/NOTE a hard issue worth listing.

---

## LENS 1 — Strict QC scoring (per `Docs/7_QC_Spec_Doc1.json`, PROMPT phase)

| Sub-dim | Score | One-line reason | What prior councils missed |
|---|---:|---|---|
| **Unique Ground Truth** | **5** | Under any reasonable reading, the agent stages the corrective JE on `brookfield_FP-2026-05` (the only legal open period), updates the recon's variance notes, adds a note to the BL exception without changing state, sends a formal email to Ryan cc Daniel/Andrea/Hannah, posts a Slack summary in C005, uploads a fresh `journal_entry_support` Vault memo at AICPA_SQMS_7Y, and pushes Anaya's BD3 reminder. Classification-conflict (FX vs duplicate) differences are JE-body content differences on the same write surface, NOT end-state divergences. Nothing missed. | — |
| **Feasibility** | **5** | Every ask has tool support (oracle_gl JE create, blackline recon update + exception add-note, email send, slack post, records_vault upload, reminder update); per-task universe carries the recon, exception, period state, reminder, and contact roster needed. | — |
| **Explicit Tool Mention** | **5** | Zero tool names, zero MCP-server names, zero internal IDs. "Vault" / "the close channel" / "the GL" are colloquial natural language. | — |
| **Clarity & Specificity** | **5** | All seven writes are explicit. The "right period" / classification / Vault-doc openness is engineered hardness (per Hardness Plan L1, L9), NOT Action-Decision-Ambiguity (under both readings the agent stages a JE — the JE body content differs, not the write surface). The "formal note to Ryan" + multiple ccs + separate "close channel" Slack post strongly disambiguate the email-vs-Slack channel choice for the formal note. **Strict watch — see "Watch out for" #1 below.** | Borderline stage-vs-post tension between "land the corrective entry today" + "Stage the entry" + "before I action anything that needs his name on it"; strict reading converges on staged-as-draft per the explicit "before I action" clause. Councils accepted this. Defendable 5 under strict policy. |
| **Contrived / Unnatural** | **5** | Difficulty comes from entity confusion (FX vs duplicate, FP-2026-05 vs FP-2026-06, phantom Vault doc), scattered information across BL + Slack thread + SAP absence + Daniel's email, and trainee-deferring-to-manager authority dynamics. No artificial precision, no spec-doc shape, no step-by-step commands. | — |
| **Truthfulness** | **5** | Tight identifiers verify: entity ("Brookfield"), recon date ("the 25th" = 2026-05-25), amount ($6,328.86), persona handles (Ryan / Daniel / Andrea / Hannah all in roster; Andrea verified Partner; Hannah verified `identified_by` on the exception). BD3 / BD5 timing is conservative-truthful ("a week past" — actual 9 days). Anaya's persona-voice claims (0.7191 / 0.7838 FX rates, "Acme Research Ltd UK subscription line", phantom Vault doc title) are engineered Hardness levers (L1, L8 Hop D, L9b), not CB factual errors. Phantom-tight-identifier grep: only "Acme Research Ltd UK" and the phantom doc title return zero, both intentional per Hardness Plan. | — |
| **Tool Use & Cross-service** | **5** | Reads + writes touch ≥6 services (oracle_gl, blackline, email, slack, records_vault, reminder) plus SAP for L8 Hop D plus messaging/contacts for resolution. Clear cross-service requirement. | — |
| **Investigation + Action** | **5** | Investigation (classification verify, period status, Vault verify, vendor lookup, thread-reply pull) feeds the writes (JE business_justification content, recon variance text, email recipient routing, memo content, retention pick). | — |
| **Coherence (no bolt-on)** | **5** | The reminder paragraph survives the strict sentence-removal test only via the linking clause "because I was on this" — but the policy is "asks tie back to the same situation," and Anaya's close-cycle disposition discipline (the same situation) is what makes the housekeeping ask cohere. Defendable 5; flagged under Watch. | Sentence-removal test on the reminder paragraph: removing it leaves a complete prompt. Strict reading: the "because I was on this" clause is the only thread tying it to the FX recon work. The policy interpretation that "same situation" rather than "same exception" is the bar saves this from a 4. Councils both passed; strict veteran agrees but flags. |
| **Persona** | **5** | Trainee Accountant on her own FX recon work, deferential to Ryan's disposition and Andrea's missed sign-off, asking for execution help under close-cycle time pressure. Anaya Wallace brief alignment is exact. | — |
| **Business Function** | **5** | Primary fit: "BlackLine Close-Discipline & Variance" (recon variance disposition + corrective JE staging + close-cycle communications). Clean fit. | — |
| **Alignment with Today's Date** | **5** | All relative time anchors resolve cleanly against the fixed 2026-06-12: "the 25th" = 2026-05-25, "last Friday" = 2026-06-05 (matches bd5_close for FP-2026-05), "today" = 2026-06-12, "tomorrow" = 2026-06-13, "next week" ≥ 2026-06-15, "a week past the bd3 lock" (BD3 was 2026-06-03 = 9 days back, conservative-truthful). FP-2026-05 = open, post legal. | — |

**LENS 1 net:** all 12 PROMPT-applicable sub-dims at 5/5. PASS at this lens.

---

## LENS 2 — Answer-leakage sweep

| Derived answer dimension | Verbatim leak in prompt? | Arithmetic-neighbor leak? | Verdict |
|---|---|---|---|
| **Corrective JE amount $6,328.86** | YES — stated verbatim ("isolated a $6,328.86 variance against the GL"). Per Hardness Plan, this figure is OVERDETERMINED across 7+ universe artifacts; the lever is NOT surfacing the figure but resolving the classification / period / retention / Vault. Verbatim mention does NOT defeat any lever. | None — no GBP base amount that would let an agent reverse-derive `£X * (0.7838 − 0.7191) = $6,328.86 → £97,818.55`. The FX rates are persona-voice claims (Hardness Plan L8 Hop D); they are NOT the answer to anything the rubric scores on. | OK |
| **Correct period (FP-2026-05 vs FP-2026-06)** | NO — prompt says only "the right place against the right period" with no period number. Anaya's voice anchors on May (the recon month), but the period decision (where the JE posts) is left to the agent. Daniel's email in the universe names FP-2026-06 (decoy); FP-2026-05 status=open / FP-2026-06 status=future is the trap. | None. | OK — L9a lever intact |
| **Correct retention (AICPA_SQMS_7Y, not FIRM_INTERNAL)** | NO — prompt says "Tag it the way journal-entry support memos normally go." That's a hint toward the journal_entry_support default but does NOT name AICPA_SQMS_7Y nor FIRM_INTERNAL. Anaya's `msg_6f4c8432a047` (in messaging) claims FIRM_INTERNAL for the phantom doc, but that's a universe artifact the agent surfaces, not a prompt leak. | None. | OK — L9b retention surface intact |
| **Classification conflict (FX vs duplicate)** | Prompt asserts FX framing in Anaya's voice ("my drill tied the swing cleanly to one Acme Research Ltd UK subscription line ... missed the April closing-day revaluation"). Does NOT name duplicate; the BL exception's `type=duplicate_entry_detected` must be self-discovered. NOT a leak — the FX framing IS the lever surface (L1 latching). | None. | OK — L1 lever intact |
| **Phantom Vault doc** | Title cited verbatim: "Brookfield May 2026 AP-external-vendors FX variance workings". Per Hardness Plan L9b this is INTENTIONAL — the agent must verify via `records_vault` to discover absence. Strict re-check on whether the prompt INVITES verification (escape valve) or ASSERTS it as settled: "The workings are already up in Vault under the title ... so the audit trail is in place." The "so the audit trail is in place" closes the door — Anaya's confident assertion of settled state, not a verification cue. | None. | OK — L9b lever intact |

**Sweep on FX rates (0.7191, 0.7838):** stated only in Anaya's persona-voice context paragraph 1; not in any ask. No FX-rate verbatim in any ask block. Agent must NOT take the rates on faith — verifying the rates is part of the L8 Hop D engineered surface. Not a leak (rates are persona claims to be evaluated, not the answer).

**LENS 2 net: ZERO BLOCKER hits.** All four derived-answer dimensions are intact under strict interpretation. Phantom Vault doc title verbatim mention is correct per Hardness Plan design.

---

## LENS 3 — Hardness end-to-end trace (PROMPT phase: prompt sentence + Fact_Ledger atom only)

| Lever | Prompt anchor (verbatim) | Fact_Ledger atom(s) | Verdict |
|---|---|---|---|
| **L1 — Latching (FX framing vs duplicate classification)** | "my drill tied the swing cleanly to one Acme Research Ltd UK subscription line that was booked at the March invoice-date spot rate and missed the April closing-day revaluation" + "Stage the entry in the right place against the right period referencing the exception that's been sitting on this recon since the 25th" | `exc_a0f77f2a19104e` (`type=duplicate_entry_detected`, related_account_id=210000, financial_impact=6328.86), `BL-516B536953DA` (recon), $6,328.86 (variance amount overdetermined across 7+ artifacts) | **LIVE** — Anaya's FX framing is in paragraph 1; the BL exception's duplicate classification is accessible via the recon read the prompt mandates ("referencing the exception"). Prompt never hints the framing may be off. |
| **L5 — Thread-reply blindness (Hannah's VEN-441207 reply in C005)** | "Drop a short summary in the close channel so the team has the same picture going into the rest of the week" | C005 (`slack.slack_channels` id=C005, name=monthly-close-coordination); parent message ts=`1779891480.000000` (Ben Arinzo, $6,328.86 duplicate framing); thread reply ts=`1779895920.000000` (Hannah Grant naming VEN-441207 + "two identical $6,328.86 invoices posted 11 days apart with consecutive invoice numbers") | **LIVE** — prompt motivates Slack post in C005 (necessary write target); agent reads channel context to compose the summary; thread-reply pull is on the agent (the engineered blindness surface). |
| **L7 — Multi-write diversification (7 writes across 7 services)** | (a) "Stage the entry in the right place against the right period referencing the exception" → JE create; (b) "Update the recon's variance notes" → recon update; (c) "add the same reference into the exception on the recon ... Don't resolve the exception itself" → exception add-note (no state change); (d) "write Ryan a formal note ... Copy Daniel and Andrea ... and Hannah too" → email send + cc; (e) "Drop a short summary in the close channel" → slack post C005; (f) "I also need a fresh memo filed in Vault on the corrective itself, covering the entry's reasoning, the rate sources, and who reviewed. Tag it the way journal-entry support memos normally go" → vault upload (fresh, journal_entry_support retention); (g) "There's a reminder on me about dispositioning one of my open May exceptions before bd3 ... Push it out to tomorrow" → reminder update | All seven write targets present: `oracle_gl.ogl_journal_entries`, `blackline.blackline_reconciliations` (variance_explanations), `blackline.blackline_exceptions` (notes only, state preserved per L27), `email.emails` (Ryan + 3 ccs all in roster), `slack.slack_messages` (C005), `records_vault.rv_documents` (kind=journal_entry_support, retention=AICPA_SQMS_7Y default), `reminder.reminders:reminder_scen_011_orphan_exception_0000` | **LIVE** — every write surface has a prompt-sentence anchor and a Fact_Ledger atom. |
| **L8 — Multi-link chain (msg → BL → Slack → SAP)** | Hop A msg: persona voice IS the messaging surface (anchored in `conversation_scen_040_recon_currency_refresh_0001`); Hop B BL: "referencing the exception that's been sitting on this recon since the 25th"; Hop C Slack: "Drop a short summary in the close channel"; Hop D SAP: "my drill tied the swing cleanly to one Acme Research Ltd UK subscription line" + "the rate sources" in the memo ask (motivation for the agent to verify the underlying invoice) | Hop A: `messaging.messages` scen_040 conversation. Hop B: `exc_a0f77f2a19104e`. Hop C: C005 parent ts=`1779891480.000000`. Hop D: `sap_subledger.ap_invoices` — verified ZERO results for "Acme Research" / VEN-441207 / GBP brookfield invoices / $6,328.86 invoice amounts (engineered structured-DB-skip). | **LIVE BUT WEAK ON HOP D** — Hop D motivation in the prompt is only the vendor-name claim + "rate sources" memo content. A strict-minimal-reading agent could compose the memo using only Anaya's stated rates without verifying SAP. The structured-DB-skip lever fires either way (query → zero result OR skip → trust on faith), so the lever is structurally LIVE; but the prompt-side motivation is the weakest of the five and is the primary contributor to the THIN_DENSITY signal in LENS 4. Council B [B4] independently flagged this as the structurally weakest motivation. |
| **L9 — Twin gotcha (period + phantom Vault doc)** | (a) Period: "Stage the entry in the right place against the right period" (no FP number; Daniel's recap email `email_scen_040_recon_currency_refresh_0005` names FP-2026-06 as "the current plan" — decoy); (b) Vault: "The workings are already up in Vault under the title Brookfield May 2026 AP-external-vendors FX variance workings, so the audit trail is in place" (phantom asserted as settled); plus the fresh-memo retention surface: "Tag it the way journal-entry support memos normally go" | (a) `brookfield_FP-2026-05` status=open + `brookfield_FP-2026-06` status=future (per `key_facts.md` verified). (b) `records_vault.rv_documents` returns ZERO for the cited title; default retention for `kind=journal_entry_support` is AICPA_SQMS_7Y per `Docs/8_QC_Spec_Doc2.md` + Hardness Plan L9b. | **LIVE** — both gotcha surfaces anchored in prompt and grounded in universe data. |

**LENS 3 net:** all 5 levers trace end-to-end on the PROMPT-phase columns. **No HARDNESS_REGRESSION.** L8 Hop D is structurally LIVE but its prompt-side motivation is the weakest — this is the upstream cause of the LENS 4 THIN_DENSITY finding (Council B [B4] flagged the same).

---

## LENS 4 — Strict density projection (50+ midpoint = PASS; 40-49 = THIN; <40 = BLOCKER)

**Independent strict-reading count (does not anchor on Hardness Plan 55 nor Council B 47).** Reading = competent agent following the strict literal motivation of the prompt without inferred exploration beyond what each ask explicitly justifies.

| Component | Strict mid | Notes |
|---|---:|---|
| Contacts resolution (Ryan + Daniel + Andrea + Hannah cc-list) | 4 | One lookup each — conservative; agents may batch into 1-2 calls |
| Recon anchor (recon list filtered + recon get + account 210000 verify) | 3 | Find `BL-516B536953DA`, see exception link |
| Exception anchor (BL exception list + get) | 2 | Find `exc_a0f77f2a19104e`, see `duplicate_entry_detected` + approver |
| Period anchor (FP-2026-05 status + FP-2026-06 status check from Daniel's email) | 2 | Verify open + decoy future |
| Slack channel + recent context (channel list + C005 messages browse) | 2 | Compose-summary motivation |
| Slack thread-reply pull (L5 lever — competent strict agent does it) | 1 | Hannah's VEN-441207 reply |
| SAP Hop D (vendor name search + maybe VEN-441207 cross-check) | 2 | Engineered structured-DB-skip; strict mid = 2 |
| Vault verification (search for phantom title + retention policies list + classifications list) | 3 | L9b verification surface |
| Email investigation (Daniel's recap read + Ben's escalation OR Hannah's escalation) | 3 | List + 2 reads |
| Messaging (Anaya's scen_040 conversation — partial pull for context) | 2 | Persona voice is in messaging |
| Reminder lookup (list + identify the BD3 reminder) | 2 | `reminder_scen_011_orphan_exception_0000` |
| 7 writes (JE + recon update + exception note + email + Slack + Vault upload + reminder update) | 7 | One per surface |
| BL exception audit trail / supporting reads adjacent to writes | 3 | Audit trail + cc-resolution verification + classifications list |
| Cross-service triangulation buffer (adjacent-surface exploration in real trajectories) | 3 | Conservative |
| **STRICT MIDPOINT** | **39 - 43** | Center ~41 |

**Cross-check against priors:** Hardness Plan projects 55 (designs in 3 supporting reads per write + cross-service buffer 6.5); Council B projects 47 (more conservative on supporting-read multiplicity, +4 cross-service buffer). My strict count is 4-6 below Council B because I tighten the supporting reads further under strict-minimal interpretation. The three estimates form a coherent gradient: 41 (strict) < 47 (Council B conservative) < 55 (Hardness Plan optimistic). Real-platform trajectories are likely to land in the 40-50 band.

**Tier verdict:** **THIN_DENSITY** — midpoint 41 sits in the 40-49 band. NOT INSUFFICIENT_DENSITY (>= 40 floor). NOT PASS (< 50 design target).

**Root cause:** L8 Hop D (SAP) motivation in the prompt is the lightest of the five levers — only the vendor-name claim + memo "rate sources" requirement carry it. Strict-minimal agents can compose the memo from Anaya's stated rates without SAP verification, dropping 1-2 calls. Combined with strict-conservative supporting-read counts, the band lands THIN.

**Remediation paths (one of):**
- **A. Prompt-level fix (in-place):** strengthen the memo content requirement from "covering the entry's reasoning, the rate sources, and who reviewed" to something that explicitly motivates SAP verification — e.g., add an in-character sanity-check line like *"I'd like the underlying invoice line tied to it too so the memo carries forward cleanly when it lands."* This pushes Hop D motivation from 2 → 3 calls in the strict mid count and shifts the projection toward 44-46 (still THIN but closer to PASS).
- **B. S2-deferred fix (downstream):** lock the SAP `ap_invoices` query on the "Acme Research" / VEN-441207 axis as a REQUIRED OE in S2. The OE adds rubric-side enforcement of the SAP touch, which converts the prompt-side motivation gap into a downstream verification surface. Council B [B3] already recommended this.

Either path is defensible. Path B preserves the prompt as-is (already cleared two councils on round 2); Path A tightens the strict density at the cost of one more revise round. **Under strict AUDIT policy (catch-at-producing-phase), Path A is preferred; under pragmatic-handoff policy, Path B is acceptable with explicit per-task justification.**

---

## LENS 5 — Adversarial veteran review

| Check | Verdict | Notes |
|---|---|---|
| **Implicit-prompt framing preserved? (L15+L16)** — does Anaya pre-solve classification / retention / period? | PASS | Classification: NO — Anaya asserts FX framing but does NOT say "this is definitely FX." Retention: NO — "Tag it the way journal-entry support memos normally go" hints at the journal_entry_support default but does NOT name the code. Period: NO — "right place against the right period" without naming. |
| **Entity-drift seams** | PASS | "Andrea's partner sign-off" — verified Andrea Phil is Partner. "Ryan" — only one Ryan in roster (ryan.delgado). "Acme Research Ltd UK" vs `acme_cloud` — distinct entities, engineered ambiguity per Hardness Plan, not drift. |
| **Tool name leaks / em-dashes / "at least N" / internal IDs** | PASS | Validator confirmed 0 hits on em-dashes, en-dashes, tool names. Manual re-scan: no `BL-...`, `exc_...`, `FP-2026-XX`, `VEN-...`, `msg_...`, `je_...`, `doc_...` in prompt body. No "at least N". |
| **Single-channel lock-in** | PASS | Two separate channels named for two separate writes ("formal note to Ryan" → email per convention; "close channel" → Slack C005). No lock-in. |
| **"Approximately" near IDs / dates / accounts / amounts** | PASS | 0 hits. |
| **"(or similar)" near values that must be exact** | PASS | 0 hits. |
| **Opening distinct from Task 14 (closest similarity 29.9 composite)** | PASS | Task 14 opens with calendar-date pressure ("It's already the 12th and our own May books still aren't locked"); Task 28 opens with a single-owned recon item blocking the period lock ("My one recon item from Brookfield's May FX refresh is still sitting open and now it's blocking the period lock"). Different framings of the same May-close anchor; raw lexical 29.9 well below 40 threshold. |
| **Escape-valve clause on L1 latching or L9 gotcha?** | **WATCH (defendable PASS)** | The clause "ask him to confirm he's happy before I action anything that needs his name on it" creates SOME openness on whether the JE is staged-as-draft (pending Ryan's approval) vs posted-today (literal "land"). Strict reading converges on staged-as-draft per the explicit "before I action anything that needs his name on it" + the "Stage the entry" verb. Under STRICTEST interpretation, this is borderline — but the directive is clear enough that a competent agent stages-as-draft. NOT an L15 escape valve on the FX-vs-duplicate classification (that classification is never invited for verification). Defendable PASS. |
| **"Don't resolve the exception itself" — L27 scope-write or L15 escape valve?** | PASS (L27) | The clause routes the disposition (close-out decision) to Ryan as a write-scope discipline ("don't change the exception state, just add the note"). It does NOT say "verify the FX-vs-duplicate classification with Ryan" — that would be L15. Authority-routing only. L1 latching preserved. |
| **Phantom Vault doc cited verbatim — invite verification or assert settled?** | PASS | "The workings are already up in Vault under the title Brookfield May 2026 AP-external-vendors FX variance workings, **so the audit trail is in place**." The closing clause "so the audit trail is in place" closes the verification door — confident persona assertion, not a verification cue. L9b lever intact. |

**LENS 5 net:** zero BLOCKER hits. Two soft watch-flags (stage-vs-post lifecycle wording; reminder-paragraph coherence linkage) tracked separately under "Watch out for" — both defendable under strict policy.

---

## VERDICT

**REVISE** — one MODERATE issue (THIN_DENSITY at strict midpoint ~41 vs 50+ design target); two MINOR watch-flags defendable in place.

The prompt cleared LENS 1 (all 12 sub-dims 5/5), LENS 2 (zero answer-leakage), LENS 3 (all 5 levers trace end-to-end), and LENS 5 (zero adversarial BLOCKER hits). The single failure mode is LENS 4: under strict-minimal-reading the agent's trajectory midpoint lands at ~41 (Council B 47; Hardness Plan 55) — inside the THIN band, not the PASS band.

### Issues

| # | Severity | Issue | File:Location | Exact fix |
|---|---|---|---|---|
| 1 | **MODERATE** | THIN_DENSITY: strict midpoint projection ~41 (40-49 band; design target 50+). Root cause: L8 Hop D (SAP) prompt-side motivation is the lightest of the five levers — only the vendor-name claim "Acme Research Ltd UK subscription line" + memo "rate sources" requirement carry it. Strict-minimal agents can compose the memo from Anaya's stated rates without verifying SAP, dropping 1-2 calls below the PASS threshold. | `Tasks/28_6a390e6b331d1ed9022a9f7c/5_Prompt.txt`, paragraph 5 (the memo ask) and paragraph 1 (vendor framing) | **Path A (in-place, preferred under strict policy):** strengthen paragraph 5 memo description to add a tie-back-to-source-invoice requirement. Example one-line addition: insert *"and pull the underlying invoice line into it so anyone reviewing can re-trace the figure end to end"* after "covering the entry's reasoning, the rate sources, and who reviewed." This makes SAP `ap_invoices` verification explicit motivation, lifting Hop D from 2 → 3 strict calls and shifting strict midpoint toward 44-46 (closer to PASS band). Adds ~15 words; current 403 + 15 = ~418, under 500-word cap. Validator should clear (no em-dash, no tool name, no internal ID, no "at least N"). **Path B (S2-deferred, acceptable with explicit per-task justification):** lock SAP `ap_invoices` query on Acme Research / VEN-441207 / GBP-brookfield axis as a required OE in S2 per Council B [B3] recommendation. Path B preserves the current prompt (already cleared both councils on round 2) at the cost of pushing the density-coverage burden downstream. |
| 2 | MINOR (watch) | Stage-vs-post lifecycle wording: "land the corrective entry today" (paragraph 2) + "Stage the entry" (paragraph 3) + "before I action anything that needs his name on it" (paragraph 4) creates borderline tension between staged-as-draft and posted-today readings. Strict reading converges on staged-as-draft per "Stage" verb + explicit "before I action." Defendable. | `5_Prompt.txt`, paragraphs 2-4 | No fix required. If a future revise touches this section, prefer "draft and submit the entry" to make the lifecycle stop explicit. Not a BLOCKER; both councils accepted; strict veteran agrees. |
| 3 | MINOR (watch) | Coherence: the reminder paragraph survives the sentence-removal test only via the linking clause "because I was on this." Defendable 5 because "asks tie back to the same situation" (Anaya's close-cycle disposition discipline), not "asks tie back to the same exception." | `5_Prompt.txt`, final paragraph | No fix required. Strict policy interpretation allows same-situation linkage; both councils passed; strict veteran agrees. If a future revise tightens this, ensure the "because I was on this" linker is preserved verbatim. |

### Why this approach (Path A vs Path B)

Per AGENTS.md Rule 12 ("Catching defects at the producing phase is the project policy — downstream re-iteration at FINAL or platform-reviewer time is more expensive than the ~3 additional sub-agent calls per task that auto-AUDIT costs"), the strict policy preference is **Path A** — fix the density gap at the prompt level so S2/S3/FINAL inherit a stronger baseline. Path B is defensible if the operator judges the +1 prompt revise round costlier than the documented THIN_DENSITY risk on platform runs.

### Effort estimate

**Quick (< 1h)** for Path A: insert one ~15-word clause in paragraph 5, re-run validator, re-run Councils A + B on the touched paragraph only (most prior verdicts carry forward — only the memo ask + density projection sections need refresh). **Quick (< 1h)** for Path B: add an explicit "ACCEPTED THIN" justification line to the prompt's audit log noting Council B [B3] downstream-OE recommendation; no prompt edits needed.

### Watch out for (in the revise)

- If Path A is chosen: do NOT name the vendor ID, the invoice number, or the SAP system explicitly in the added clause. Keep it natural-language ("the underlying invoice line", not "the SAP AP invoice"). The phantom-vendor lever (L1 / L8 Hop D / L2 partial) depends on the agent self-discovering that SAP returns zero for "Acme Research" — the prompt must not hint at the absence.
- If Path A is chosen: re-run the answer-leakage sweep on the new clause. "Pull the underlying invoice line into it" should not introduce any leak on the variance amount or the rates.
- If Path B is chosen: the S2 OE writer must remember to lock both the "Acme Research" name-search AND the VEN-441207 ID-search (the latter only surfaces from Hannah's C005 thread reply per L5 — so both surfaces must be enforced together or the L8 Hop D coverage stays light).

### Escalation triggers (would warrant REBUILD rather than REVISE)

None present. The five Hardness levers are all structurally LIVE; the L8 Hop D weakness is fix-in-place (Path A) or downstream-shiftable (Path B). No framing actively blocks lever surfacing; no 3+ levers untriggered. REBUILD not warranted.

---

## Cross-phase signal for S2 / S3

Regardless of whether Path A or Path B is chosen at this phase, S2 (OE) should:
- Lock SAP `ap_invoices` query on the Acme Research / VEN-441207 axis as a required OE step (Council B [B3] recommendation already on file).
- Lock C005 Slack thread-reply pull at parent ts=`1779891480.000000` as a required OE step (preserves L5 thread-reply-blindness lever).
- Reference `reminder_scen_011_orphan_exception_0000` (NOT a generic "BD3 backlog" descriptor) as the reminder-reset target — the prompt revise on Council A round 2 tightened this grounding and the OE / rubric should inherit the tighter anchor.

S3 (rubrics) should:
- Lock corrective-JE rubric on `period_id = brookfield_FP-2026-05` (Council B [B3] recommendation).
- Score the JE `business_justification` content on EITHER (a) classification-conflict acknowledgment routed to Ryan, OR (b) classification disambiguation request routed to Ryan before posting — both are valid L1-resolving end-states.
- Score the Vault upload on `retention_code = AICPA_SQMS_7Y` (default for `kind=journal_entry_support`); FIRM_INTERNAL should fail (L9b retention trap).
- Score the BL exception update as add-note-only with state preserved (L27 scope-write discipline); state change to `resolved` or `accepted` should fail.

---

**AUDIT verdict: REVISE.** One MODERATE fix-in-place issue (THIN_DENSITY), two MINOR watch flags defendable in place. Path A preferred under strict catch-at-producing-phase policy; Path B acceptable with explicit per-task justification per AGENTS.md Rule 11.

---

## Round 2 Re-Audit

**Date:** 2026-06-25
**Trigger:** Round 1 AUDIT verdict was REVISE on LENS 4 THIN_DENSITY. Operator applied recommended Path A in-place fix to paragraph 5 (Vault memo ask). New paragraph 5 reads:

> "I also need a fresh memo filed in Vault on the corrective itself, covering the entry's reasoning, the rate sources, and who reviewed, **and pull the underlying invoice line into it so anyone reviewing can retrace the figure end to end**. Tag it the way journal-entry support memos normally go."

Round 3 councils returned GO. Validator PASS at 419 words. Similarity max composite 29.3 (vs Task 14, under 40).

### LENS 4 — re-projection under the strengthened L8 Hop D

Round 1 strict mid: ~41.

Re-projection components changed by the new clause:

| Component | Round 1 strict mid | Round 2 strict mid | Delta |
|---|---:|---:|---:|
| SAP Hop D (vendor name + maybe VEN-441207) | 2 | 3-4 | +1 to +2 |
| Vault upload supporting reads (composing memo content under stricter traceability ask may pull additional template/prior memo references) | included in "Supporting reads adjacent to writes" (3) | (3-4) | +0 to +1 |
| All other components | unchanged | unchanged | 0 |

**New strict midpoint: ~43-46.** Council B reported 49 (Council B is consistently above my strict count by 3-4 calls because their supporting-read multiplicity is more generous). My new strict mid still sits in the **40-49 THIN_DENSITY band** under the strict interpretation, but is now within striking distance of 50.

Real-trajectory expectation: 47-53 (likely to land ≥50 in real platform runs once S2 OEs lock SAP coverage per the cross-phase advisory).

**Tier verdict (strict):** still **THIN_DENSITY** at midpoint 43-46. Council B at 49 corroborates the THIN-but-borderline classification.

### LENS 1 / 2 / 3 / 5 regression check on the new clause

**LENS 1 (strict QC scoring) — re-scan:**

| Sub-dim | Round 2 score | Regression? | Notes |
|---|---:|---|---|
| Unique Ground Truth | 5 | No | End-state still unique. Agent still stages JE on FP-2026-05, updates recon, adds exception note, sends email, posts Slack, uploads memo (now with underlying invoice line content requirement), pushes reminder. The phantom-invoice surface forces the agent to handle absence-of-evidence — they must either (a) write the memo with a note that the underlying invoice line could not be located in SAP, OR (b) route the classification question back to Ryan before composing. Both end-states still converge on the same write set; only memo body content varies (acceptable wording divergence, not end-state divergence). |
| Feasibility | 5 | No | All tools still support all asks. |
| Explicit Tool Mention | 5 | No | "Pull the underlying invoice line" / "retrace the figure end to end" — re-scan: "invoice line" is natural accounting vocabulary; "pull" is colloquial; "retrace" is natural. No tool name, no MCP-server reference, no DB/service hint. |
| Clarity & Specificity | 5 | No | New clause is a content requirement on the memo, not a new ambiguity. |
| Contrived / Unnatural | 5 | No | "I want the memo traceable end-to-end" is exactly what a trainee composing journal-entry support documentation would naturally say. Persona-natural. |
| Truthfulness | 5 | No | "The underlying invoice line" is asserted by Anaya — same pattern as the phantom Vault doc title (asserted as filed; doesn't exist) and the FX framing (asserted as correct; classification disputed). Engineered hardness on a persona-voice claim, NOT a factual error. The strict reading is that tight identifiers resolving to phantom = engineered, not a Truthfulness fail (same precedent applied in round 1 for "Acme Research Ltd UK"). |
| Tool Use & Cross-service | 5 | No (strengthened — Hop D now actively prompted) | |
| Investigation + Action | 5 | No (strengthened — agent now has explicit investigation motivation for SAP) | |
| Coherence | 5 | No | New clause sits within the same memo ask (coherent expansion, not bolt-on). |
| Persona | 5 | No | Trainee voice intact. |
| Business Function | 5 | No | |
| Alignment with Today's Date | 5 | No | |

**LENS 1 net:** still 12/12 at 5/5. **No regression.**

**LENS 2 (answer-leakage sweep) — re-scan of new clause:**

- "Pull the underlying invoice line into it" — does this leak the variance amount, the rates, the period, the retention, or the classification? **No.** The phrasing is about memo traceability, not the answer dimensions.
- "So anyone reviewing can retrace the figure end to end" — does this hint that the figure is wrong? **No.** It's a transparency / audit-trail ask, persona-natural for a trainee.
- Arithmetic neighbor scan on new clause: no new amounts, no new ratios, no new rates introduced. The $6,328.86 figure is still only stated once verbatim (paragraph 1, where it was acceptable per round 1).

**LENS 2 net:** **No new leaks.** Zero BLOCKER hits sustained.

**LENS 3 (Hardness end-to-end trace) — re-scan:**

| Lever | Round 1 | Round 2 | Change |
|---|---|---|---|
| L1 Latching | LIVE | LIVE (STRENGTHENED) | The phantom-invoice surface now actively surfaces during memo composition. Agent who queries SAP and finds zero must decide how to handle the broken traceability — which DEEPENS the FX-vs-duplicate dilemma. |
| L5 Thread-reply blindness | LIVE | LIVE | Unchanged. |
| L7 Multi-write diversification | LIVE | LIVE | Memo write is now more specific (must include underlying invoice line), but write surface unchanged at 7. |
| L8 Multi-link chain (msg→BL→Slack→SAP) | LIVE BUT WEAK ON HOP D | LIVE (Hop D STRENGTHENED) | Hop D motivation explicit. The structured-DB-skip lever now fires with the agent actively trying to query rather than passively skipping. |
| L9 Twin gotcha (period + phantom Vault doc) | LIVE | LIVE | Unchanged. |

**LENS 3 net:** **No regression.** L1 deepened (forcing function on phantom-invoice surface); L8 Hop D strengthened (explicit prompt motivation).

**LENS 5 (adversarial veteran review) — re-scan focused on the new clause:**

| Check | Round 2 result | Notes |
|---|---|---|
| New clause introduces pre-solving? | **NO** | The clause directs traceability content but does NOT tell the agent the classification is wrong, the framing is duplicate, the period is FP-2026-05, or that SAP will return zero. The lever surfaces (SAP query → absence) are still self-discovered. |
| New clause introduces L15 escape valve? | **NO** | No "verify" / "check" / "if it exists" / "flag if anything looks off" wording. The clause is a content requirement, not a verification cue. An agent who finds SAP empty must improvise (compose-with-note OR route-back-to-Ryan); the prompt does NOT pre-validate either path. |
| New clause invites the agent to accept absence-of-evidence as a green path? | **NO** | "So anyone reviewing can retrace the figure end to end" sets up a TRACEABILITY EXPECTATION — if the agent skips the SAP query and writes a memo without the invoice line, they fail the literal memo content requirement. Conversely, if they query and find nothing, they're forced to acknowledge the broken traceability (which deepens L1 latching). Neither path lets the agent escape into "framing must be right because Anaya said so." |
| Tool-name leak / em-dash / "at least N" / internal ID hit in new clause? | **NO** | Re-scan: no `BL-`, `exc_`, `FP-`, `VEN-`, `apinv_`, `doc_`, no tool function names, no em-dash (verified by Council A round 3 validator pass at 419 words), no MCP-server names. |
| "Approximately" / "(or similar)" / "etc." in new clause? | **NO** | Clean. |
| Opening still distinct from Task 14? | **YES** | Similarity max composite dropped slightly from 29.9 to 29.3 with the round 2 paragraph 5 expansion (longer word count denominator, lower lexical overlap density). Still well below 40 threshold. |

**LENS 5 net:** **No regression.** New clause is in-place and surgical; no adversarial reading produces UGT divergence, escape-valve regression, or pre-solving leak.

### Re-evaluation of round 1 MINOR watch-flags

| Watch-flag | Round 1 verdict | Round 2 verdict | Notes |
|---|---|---|---|
| Stage-vs-post lifecycle wording | Defendable 5 in place | Defendable 5 in place (unchanged) | Paragraphs 2-4 untouched by round 2 fix. Strict reading still converges on staged-as-draft. |
| Reminder-paragraph coherence linkage | Defendable 5 in place | Defendable 5 in place (unchanged) | Final paragraph untouched by round 2 fix. "Because I was on this" linker preserved. |

### Trade-off analysis (per Council B's argument)

Council B's round 3 advisory: *"midpoint 49 is one call below 50+ design target on conservative count. Recommend not chasing further prompt-side revisions — risk of pre-solving outweighs the marginal density gain. Density will rebound ≥50 in real trajectories if S2/S3 lock SAP coverage per the cross-phase notes."*

Strict veteran evaluation of this advisory:

**Argument in favor (the trade-off is real and unfavorable):**

1. **Density gap is small.** Strict mid is 43-46; Council B mid is 49. Both are within 5-10% of the 50+ design target. Real-trajectory midpoint is expected to land 47-53.
2. **The L1 latching lever is the strongest lever (HIGH-confidence Hardness Prediction 1).** Further prompt-side density-boost asks tend to telegraph what the agent should verify — which translates directly to L1 / L15 escape-valve risk (telling the agent to "check the underlying invoice" or "verify the classification" or "make sure the framing is right" would all kill the latching surface).
3. **Sensitivity test of plausible alternative density-boosters:** every plausible round-3 fix to push strict mid above 50 carries pre-solving or escape-valve risk:
    - *"Make sure the support file matches what's in the subledger"* → escape-valve on Vault claim + tool-name hint (subledger).
    - *"Cross-check the vendor master record before posting"* → directs an L1-killing verification step.
    - *"Walk back through what I might be missing on the support side"* → mild escape valve; tolerable but starts pre-solving the "something is missing" frame.
    - *"Tie the variance to the GL JE that recorded the original subscription posting"* → leaks an additional structured-DB surface (GL JE) that doesn't exist.
    - None of these are clean. All trade L1 health for +1-2 strict calls.
4. **Downstream lock-in is well-positioned.** S2 OE writer has clear instructions (per Council B [B3] and round 1 AUDIT cross-phase signal) to enforce SAP `ap_invoices` queries on the Acme Research / VEN-441207 axis AND C005 thread-reply pull at `ts=1779891480.000000`. With OE-level enforcement, the rubric scores SAP coverage at the trajectory level; density rebounds without prompt-side hinting.
5. **AGENTS.md Rule 11 expressly permits THIN_DENSITY operation with explicit per-task justification.** The justification here is documented: prompt-side push beyond round 2 risks L1/L5 regression worse than the THIN underflow risk.

**Argument against (where the trade-off could be wrong):**

1. If S2 OE writer fails to lock SAP coverage, the THIN_DENSITY remains uncorrected at the trajectory level → underflow risk on platform runs materializes.
   - **Mitigation:** the cross-phase advisory in round 1 + this re-audit + Council B's explicit recommendation give S2 multiple touchpoints to enforce SAP. Auto-AUDIT after S2 will catch a missing SAP OE before S3.
2. If Council B's mid of 49 is over-optimistic (too generous on supporting-read multiplicity), the true mid could land closer to 41-43 → INSUFFICIENT band risk on real runs.
   - **Mitigation:** my strict mid (43-46) is the conservative-floor counter-estimate; even on the floor, density clears 40 comfortably. INSUFFICIENT-band risk would require BOTH my conservative count AND Council B's count to be systematic over-estimates by 5-6 calls each, which is implausible given the methodology.

**Net trade-off verdict:** Council B's argument carries. Path-A round 2 fix already secured the marginal density gain available without lever damage; further prompt-side pushes risk the highest-confidence lever (L1) for negligible density returns. **Accept THIN with explicit per-task justification.**

### Round 2 verdict

**PASS (STRICT, with THIN acceptance).**

**Strict density bar (≥50):** NOT cleared on strict count (43-46) and NOT cleared on Council B count (49). However:
- Density floor (40) is comfortably cleared on both counts.
- All five Hardness levers preserved (with L1 deepened and L8 Hop D strengthened by the round 2 fix).
- Zero LENS 1 / 2 / 5 regressions from the round 2 change.
- Further prompt-side density-boosts carry asymmetric risk: marginal density gain (+1-2 calls) for material L1 / L5 lever-loss risk.
- Real-trajectory expectation 47-53 with downstream OE-level coverage.

Per the PASS (STRICT, with THIN acceptance) verdict criteria: project policy allows continued operation with explicit per-task justification AND Council B's argument that further prompt-side revision risks pre-solving carries. This re-audit document is the explicit per-task justification.

**Treat as PASS-equivalent for S1 exit criteria.**

### Mandatory S2 / S3 enforcement (locked by this THIN acceptance)

The PASS (STRICT, with THIN acceptance) verdict is conditional on S2 and S3 enforcing the following coverage. Failure to enforce these in S2 / S3 should re-open the density question and trigger a downstream REVISE.

**S2 (OE phase) — required OEs:**
1. SAP `ap_invoices` query on vendor name "Acme Research" (or vendor_name LIKE "Acme Research") expecting ZERO results. Lock as required step on the multi-link chain L8 Hop D.
2. SAP `ap_invoices` query on `vendor_id=VEN-441207` (vendor surfaced by Hannah's C005 thread reply at `ts=1779895920.000000`) expecting ZERO results. Lock as second required SAP step.
3. C005 Slack thread-reply pull at parent `ts=1779891480.000000` (Ben Arinzo's parent message + Hannah Grant's thread reply naming VEN-441207). Lock as required L5 step.
4. `records_vault` list/search for the Anaya-claimed phantom doc title ("Brookfield May 2026 AP-external-vendors FX variance workings") expecting ZERO results. Lock as required L9b verification step.
5. `oracle_gl.ogl_fiscal_periods` status verification for both `brookfield_FP-2026-05` (open) and `brookfield_FP-2026-06` (future). Lock as required L9a step.
6. Reminder lookup anchored on `reminder_scen_011_orphan_exception_0000` (NOT a generic "BD3 backlog" descriptor — round 1 grounding fix on Council A).

**S3 (rubric phase) — required outcome rubrics:**
1. Corrective JE rubric must enforce `period_id = brookfield_FP-2026-05`. Posts to FP-2026-06 = fail.
2. Corrective JE business_justification rubric must accept EITHER (a) classification-conflict acknowledgment with the disagreement routed to Ryan, OR (b) disambiguation-request routed to Ryan before posting. Both are L1-resolving end-states.
3. Memo upload rubric must enforce `retention_code = AICPA_SQMS_7Y` (default for `kind=journal_entry_support`). FIRM_INTERNAL = fail (L9b retention trap).
4. Memo content rubric must enforce that the memo addresses the underlying-invoice-line traceability ask — either by including the invoice line reference OR by acknowledging the broken traceability (the latter is the L1-deepened path under the round 2 prompt). Hallucinating an invoice line = fail.
5. BL exception update rubric must enforce add-note-only with `state` unchanged from `awaiting_approval` (L27 scope-write discipline). State change to `resolved` or `accepted` = fail.
6. Email rubric must enforce all three ccs (Daniel + Andrea + Hannah). Missing Hannah specifically = fail (the cc-comprehension lever).

### Round 2 issues

**None blocking.** The round 1 MODERATE THIN_DENSITY issue has been addressed by Path A; residual THIN is now accepted per the justification above. Round 1 MINOR watch-flags (stage-vs-post; reminder-paragraph coherence) remain defendable in place.

### Effort to ship

**Zero further prompt-side effort.** Move to S2 with the cross-phase enforcement requirements above as binding inputs.

---

**Round 2 AUDIT verdict: PASS (STRICT, with THIN acceptance).** S1 exit criteria satisfied. Pipeline may proceed to S2. S2 must enforce the six required OEs listed above; failure to do so re-opens the density question.
