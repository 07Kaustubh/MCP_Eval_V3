# AUDIT prompt (STRICTEST) — Task 37 (on-demand, fresh chat)

**Universe:** keystone · **Trigger:** `PIPELINE AUDIT --phase all` (pre-upload sanity gate)
**Artifact:** `5_Prompt.txt` (UNCHANGED from candidate submission)
**Baseline priors:** `AUDIT_prompt_original.md`, `REVIEW_FINAL.md`, `FINAL_materialize.md` all PASS (STRICT). Independently re-derived here.

## Programmatic floor (inherited)
- `validate.py --phase prompt` = **PASS** (0 fails · 3 warns [bolt-on candidates] · 6 notes)
- `calc_similarity.py` = 28.5 composite (< 40 ceiling)
- `verify_universe_atoms.py` = **PASS** (41/41 atoms grounded)
- `test_regression_anchors.py` = **48/48 PASS**
- Word count = 343 (< 500 cap) · em-dashes = 0 · tool names in prompt = 0

## LENS 1 — Strict QC scoring (Docs/7_QC_Spec_Doc1.json)

Per-atom evidence table (v18 mandate). Every prompt atom traced to universe source.

| # | Prompt atom | Universe source (file:record) | Verified |
|---|---|---|---|
| A1 | "Grace... wants a full status on every active file in my queue" (persona = Sofia's boss, deliverable request) | `mortgage_los.staff` → Grace Yamamoto is COO/manager (persona_briefs.md) | ✅ |
| A2 | "Camille... pulled her lock report and several of my files have lock issues" | `mortgage_los.staff` → Camille Foster = broker/lock-desk (persona_briefs.md); universe seeds 26 expired locks | ✅ |
| A3 | "every active loan assigned to me" (Sofia = processor, 26 files) | `mortgage_los.loans` filtered on `assigned_processor=los_staff_afc9caafae9d` AND active status → 26 rows | ✅ |
| A4 | "whether the lock is still good or expired" | `mortgage_los.loans.rate_lock_expiration` — every one of the 26 rows has date < 2026-04-28 | ✅ |
| A5 | "what conditions or documents are still outstanding" | `mortgage_los.conditions` (3 rows for LN-2026-00008, 2 outstanding) + `mortgage_los.document_checklist_items status=required` (26 items across 8 loans) | ✅ |
| A6 | "recent email threads or Slack discussions about them" | `email.emails` (39 emails across 7 loans) + `slack.slack_messages` (47 msgs across 9 loans in C002/C004) | ✅ |
| A7 | "Reach out to Carlos, Derek, Keisha, and any other LO with active files" | `mortgage_los.loans.assigned_lo` distinct → 8 active LOs (Carlos/Derek/Keisha/Amy/Marcus/Natasha/James/Priya) — 8 = "any other" fan-out probe | ✅ |
| A8 | "If any file is assigned to someone who's no longer with the company" | `mortgage_los.staff.is_active=False` × `assigned_lo` → 5 loans (Veronica Hayes ×4, Brian Mitchell ×1) | ✅ |
| A9 | "full lock status summary... every one of my files" | Same as A4 (26 rows) | ✅ |
| A10 | "broken down by loan status, assigned LO, and the main blocker" | Every loan record has `status`, `assigned_lo`, and discoverable blocker via conditions/docs/lock/email/Slack | ✅ |
| A11 | "processing channel" (Slack #loan-processing) | `slack.slack_channels` → C002 = #loan-processing (per Universe_Index/service_inventory) | ✅ |
| A12 | "log everything in the CRM" | `crm.crm_engagements` writable via `crm_create_engagement` (tool catalog) | ✅ |
| A13 | "If anything you find looks like it could be a compliance concern, flag it separately for Elena and Denise" | Denise Holloway = compliance authority (Slack C004 breach-response, ts=1775570820, verbatim); Elena Marchetti = senior processor with lender-coordination specialization (`mortgage_los.staff` role=processor, specialization="Doc collection, lender coordination"); 3 latent compliance findings surface (UWM/Keisha phishing scope; LN-2026-00613 TRID/30yr→15yr; terminated-LO accountability gap) | ✅ |

**Sub-dim scores (strictest 5/5-only bar):**

| Sub-dim | Score | Note |
|---|---|---|
| Coherence (no command-list / no bolt-on / no pre-solve) | **5** | Bolt-on validator WARN sentences re-tested via remove-sentence: all 3 load-bearing (see LENS 7) |
| Explicit tool mention | **5** | 0 tool tokens in the prompt (validator confirms) |
| Universe alignment | **5** | 13 atoms above all trace; 41/41 verify_universe_atoms PASS |
| Persona voice | **5** | First-person Sofia to internal-agent, matches persona brief (harried processor before Grace deadline) |
| Multi-step / density hint | **5** | 216.8 avg measured tool calls (well above 50+ design) |
| Unique-ground-truth (v18-merged from retired LENS 9) | **5** | Every "what to produce" claim traces to a single deterministic universe atom; no alt-answer escape hatch |
| Discoverability | **5** | Universe seeds discovery paths for each lever — cross-service (LOS + email + Slack + CRM + contacts) is required to surface all 8 |

**LENS 1 verdict: PASS (STRICT) — every applicable sub-dim = 5/5.**

## LENS 2 — Answer-leakage sweep (deeper than FINAL)

Prompt does NOT reveal any of the following (each independently probed):
- Count "26 active loans" — absent (`grep -Ei '26|twenty[- ]six' 5_Prompt.txt` = 0)
- Any loan number (LN-YYYY-NNNNN) — absent
- Any borrower name — absent
- Terminated-LO identity (Veronica Hayes / Brian Mitchell) — absent
- Rate-lock expiration dates — absent
- Document count "7" (LN-2026-00010) or "5" (LN-2026-00623) — absent
- Compliance-finding specifics (phishing/UWM/TRID/30yr→15yr) — absent
- Lender names (UWM, Homepoint, Caliber, Flagstar, Freedom, Pennymac, AmeriHome, Plaza) — absent

**LENS 2 verdict: PASS (STRICT). Zero leakage.**

## LENS 3 — Hardness end-to-end trace (from REVIEW_hardness.md 8 levers)

| # | Lever | Prompt anchor (line/phrase) | Present in prompt? |
|---|---|---|---|
| 1 | 26 active loans | "every active loan assigned to me in the system and for each one" | ✅ |
| 2 | All 26 locks expired | "whether the lock is still good or expired" | ✅ |
| 3 | 5 terminated-LO loans | "If any file is assigned to someone who's no longer with the company or if anything looks off about the assignment" | ✅ |
| 4 | 26 outstanding docs across 8 loans | "what conditions or documents are still outstanding" | ✅ |
| 5 | UWM/Keisha phishing scope | "If anything you find looks like it could be a compliance concern" (open-ended anchor; discoverable via Slack C004) | ✅ |
| 6 | LN-2026-00613 TRID redisclosure | same open-ended compliance anchor (discoverable via Slack C002) | ✅ |
| 7 | LN-2026-00623 CTC anomaly | "figure out exactly what's blocking progress on each one" | ✅ |
| 8 | LN-2026-00010 max-docs | same "conditions or documents outstanding" anchor | ✅ |

**LENS 3 verdict: PASS (STRICT). Every lever has an anchor line.**

## LENS 4 — Density projection (50+ bar)

Measured avg total tool calls = **216.8** (runs 89 / 85 / 338 / 256 / 226 / 307). Measured MCP-only avg = 194.7. Well above 50 design target and 40 floor.

Spot-check on 3 trajectories:
- Run 1: 89 tool_use events; 26× `mortgage_los_add_activity`; 15× `get_loan_by_id`; 11× `email_send_email`; iteration pattern is per-loan.
- Run 3: 338 tool_use events; 76× `email_search_emails`; 56× `slack_search_public_and_private`; 26× per-loan conditions/documents/rate_lock/activity — dense, cross-service probe.
- Run 5: 226 tool_use events; mixes aggregate (1× `get_pipeline_summary`, 1× `compliance_alerts`) with 26× per-loan iteration.

Aggregate tools (`get_compliance_alerts`, `get_pipeline`, `get_outstanding_documents`) appear as shortcuts in 4/6 runs but do NOT collapse density — measured density is 4× the strict bar.

**LENS 4 verdict: PASS (STRICT) with margin.**

## LENS 5 — Adversarial veteran review (pattern-match)

| Anti-pattern | Present? | Note |
|---|---|---|
| Rubrics Eval 2.7 method-lock | ❌ | "reach out", "give each of them", "make sure Camille gets", "post a heads up", "log everything in the CRM", "flag it separately" — method-agnostic language throughout |
| Persona-scope violation | ❌ | Sofia Reyes = processor (staff row confirmed active); Grace = boss; Camille = lock desk; all named personas map to real active `mortgage_los.staff` or slack.slack_users rows |
| Action-divergence | ❌ | Prompt actions all trace to universe write surface (email, Slack, CRM engagement, LOS activity) |
| Tool-name leaks | ❌ | validator PASS with 0 tool tokens |
| Entity drift | ❌ | Sofia / Grace / Camille / Elena / Denise / 8 LOs all confirmed in staff or slack.users |
| Em-dashes | ❌ | 0 |
| "At least N" | ❌ | Not present in prompt |
| Single-channel lock-in | ❌ | processing-channel mention is prompt-inherent (natural workplace phrasing); other channels method-agnostic |
| "(or similar)" near exact value | ❌ | Not present |
| Internal IDs | ❌ | No `los_staff_*` / `keystone_*` IDs in prompt |
| OE meta-tags | N/A | prompt phase |

**LENS 5 verdict: PASS (STRICT).**

## LENS 6 — RETIRED in v18 (merged into LENS 1 per-atom evidence table).

## LENS 7 — Anti-rationalization pass

Prior audit reasoning re-scrutinized for "I considered flagging X but decided it's fine because..." patterns:

1. **3 bolt-on WARNs (validator flagged sentences on terminated-LO, Camille lock summary, compliance escalation).** Re-tested via remove-sentence:
   - Remove "If any file is assigned to someone who's no longer with the company..." → rubric[20] and rubric[27] lose their prompt anchor; terminated-LO lever (#3) becomes ungrounded.
   - Remove "Make sure Camille gets a full lock status summary..." → rubrics [16], [17] lose their prompt anchor; Camille recipient method-agnostic still discoverable but the mandate is lost.
   - Remove "If anything you find looks like it could be a compliance concern..." → rubric[24] loses its prompt anchor; compliance-flag lever (#5, #6) loses its explicit trigger.
   All 3 are LOAD-BEARING. Validator flagged them as bolt-on candidates (heuristic); they are not actually bolt-on. Not rationalization — verified with mechanical removal test.

2. **Aggregate tools available (compliance_alerts, get_pipeline).** Under strictest lens, could aggregate tool availability be answer leakage via the tool catalog? Verified against measured trajectories: 216.8 avg total tool calls / 33.3% pass@1. The aggregate tools' EXISTENCE doesn't collapse hardness — they're one of many discovery paths, not the answer. Not rationalization.

3. **Persona attribution (Elena vs Denise).** The prompt names both by name. Elena is a senior processor per `mortgage_los.staff` (not compliance authority). Denise is the actual compliance authority per Slack C004. Both are appropriate escalation recipients (senior processor + compliance officer). Not persona-scope violation — matches real escalation chain.

**LENS 7 verdict: No suppressed findings.**

## LENS 8 — Regression anchor verification

`test_regression_anchors.py` → **48/48 PASS** (inherited from deterministic floor).

## LENS 9 — RETIRED in v18 (merged into LENS 1 unique-ground-truth sub-dim + LENS 5 adversarial).

## Final verdict

**PROMPT: PASS (STRICT)**

One-line summary: 13 universe atoms all trace, 0 leakage, all 8 hardness levers anchored, density 4× strict bar, 3 validator-WARN sentences confirmed load-bearing by mechanical removal test, no method-lock / persona-drift / tool-leak / em-dash / "at least N" anti-patterns.
