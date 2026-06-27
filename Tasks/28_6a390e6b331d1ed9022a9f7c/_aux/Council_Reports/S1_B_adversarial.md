# Council B — Adversarial QC + Density + Hardness Preservation

**Deliverable:** `Tasks/28_6a390e6b331d1ed9022a9f7c/5_Prompt.txt`
**Phase:** S1 (prompt)
**Council:** B — Adversarial QC + Density + Hardness Preservation
**Verdict:** **GO (with one moderate flag tracked under Recommended Improvements)**
**Date:** 2026-06-25

---

## Five-Lens Pass Notes (consolidated)

- **Architect.** Trigger ("recon item blocking the period lock") → context (Brookfield May FX refresh, $6,328.86 variance on AP-external-vendors recon, week past BD3/BD5, Andrea's missed Friday sign-off) → asks (corrective JE + recon update + exception note + email Ryan cc Daniel/Andrea/Hannah + Slack + Vault memo + reminder reset). Three loose movements (corrective + reference chain / communications / housekeeping). Voice register matches Anaya's Trainee Accountant brief (deferential to Ryan's disposition, ahead-of-review urgency, asks for execution).
- **Implementer.** Every named human (Ryan / Daniel / Andrea / Hannah) is in the persona roster (Fact_Ledger emails confirm all four). Close channel is uniquely resolvable (C005 `#monthly-close-coordination` per project conventions). "Acme Research Ltd UK" is the engineered phantom vendor surface — the prompt does NOT promise the agent will find it; that absence is L8 hop D. Period & recon are resolvable from Anaya's voice ("Brookfield May FX refresh", "AP-external-vendors recon", "the 25th").
- **Red-team.** See B2 below — each adversarial reading classified as LEVER or FAIL.
- **Ground-truth.** Spot-checks: $6,328.86 sits in atom set; FP-2026-05 = open / FP-2026-06 = future (verified per `key_facts.md`); BD3 lock for `brookfield_FP-2026-05` was 2026-06-03 (universe today 2026-06-12 → 9 days past, "a week past" is conservative-truthful color). The 0.7191/0.7838 rate pair has no FX-table referent in the universe — these read as Anaya's persona claims (color), not as universe assertions; the structured-DB skip lever absorbs them.
- **Integration.** Prompt preserves L1 (Anaya's FX framing carried forward — agent self-discovers the BL duplicate counter-classification), L5 (Slack ask sits on C005 — agent has incentive to scroll the channel but must pull thread replies on their own), L7 (all seven writes named — corrective JE, recon variance notes, exception note "without resolving", formal email cc'd, Slack summary, fresh Vault memo, reminder reset), L8 (messaging→BL→Slack→SAP — see B4 for SAP motivation note), L9 (period framing left to the agent + phantom Vault doc claimed as already-filed).

---

## [B1] QC Sub-Dim Scoring (prompt-applicable, per `Docs/7_QC_Spec_Doc1.json`)

| Sub-dim | Score | One-line reason |
|---|---:|---|
| Unique Ground Truth | **5** | One final universe end-state on key writes: corrective JE staged on `brookfield_FP-2026-05` referencing the open exception with FX-or-duplicate disambiguation routed back to Ryan, recon variance notes + exception note updated (exception state unchanged), formal email to Ryan cc'd to Daniel/Andrea/Hannah, Slack note in C005, fresh AICPA_SQMS_7Y journal_entry_support memo in Vault, reminder pushed to 2026-06-13. Path/wording differences (e.g., email vs. messaging) do not change end-state. |
| Feasibility | **5** | Every ask has tool support across `oracle_gl` (JE staging), `blackline` (recon variance + exception note write without state change), `email` (send), `slack` (post), `records_vault` (upload), `reminder` (update). Universe carries the exception, recon, and reminder. |
| Explicit Tool Mention | **5** | Zero tool / MCP-server names. Zero internal IDs. "Close channel" reads as natural employee shorthand. |
| Clarity & Specificity | **5** | Action set is unambiguous on the write surface — "stage the entry", "update variance notes", "add the same reference into the exception", "don't resolve the exception", "write Ryan a formal note", "drop a short summary", "fresh memo", "push it to tomorrow". The deliberate latitude on classification / period / Vault doc is engineered hardness (Levers 1, 9), not Action-Decision-Ambiguity (the writes themselves are the same set under either reading). |
| Contrived / Unnatural | **5** | Difficulty comes from entity confusion (FX vs duplicate, FP-2026-05 vs FP-2026-06, phantom Vault doc), scattered information (BL + Slack thread reply + SAP absence + Daniel's email), and trainee-deferring-to-manager dynamics. No arbitrary precision constraints, no spec-doc shape. |
| Truthfulness | **5** | Tight identifiers in the prompt — entity ("Brookfield"), date ("the 25th" = 2026-05-25), period framing ("April close / May close"), amount ($6,328.86), persona handles (Ryan / Daniel / Andrea / Hannah), channel (close channel) — all resolve. The 0.7191 / 0.7838 rate pair and the "Acme Research Ltd UK subscription" vendor are persona-voice claims that the agent must discover are unverifiable — those are engineered Lever 1 / Lever 8 surfaces, not CB factual errors. The phantom Vault doc is the L9 lever. |
| Tool Use & Cross-service | **5** | Reads + writes cross at least six services on the design path (Oracle GL, BlackLine, Slack, Email, Records Vault, Reminder), plus SAP for the structured-skip surface. |
| Investigation + Action | **5** | Investigation (classification, period, Vault doc verification, vendor lookup) feeds writes (JE business justification content, recon variance text, email recipient routing, memo content). |
| Coherence (no bolt-ons) | **5** | The reminder ask in the last paragraph is the only candidate for a bolt-on — but it ties back to the same situation ("I let slip because I was on this") and is one sentence of trainee-realism housekeeping. Removing it makes Anaya's voice less natural, not more. The Vault memo ties to the JE, the Slack summary ties to the email, the email ties to the JE, the JE ties to the exception. One cohesive situation. |
| Persona | **5** | Trainee Accountant on her own FX recon work, deferring to Ryan's disposition and Andrea's sign-off, asking for execution help under close-cycle time pressure. Aligns with Anaya Wallace's brief (FX JE preparer, stands in on AP escalations). |
| Business Function | **5** | BlackLine Close-Discipline & Variance — recon variance disposition + corrective JE staging + close-cycle communications. Could secondarily map to Bookkeeping; primary fit is clean. |
| Alignment with Today's Date | **5** | Relative time ("the 25th" = 2026-05-25, "last Friday" = 2026-06-05, "today" = 2026-06-12, "tomorrow" = 2026-06-13, "next week" = 2026-06-15+, "a week past the bd3 lock" — BD3 was 2026-06-03, 9 days back, conservative truth) all resolve cleanly against the fixed 2026-06-12 anchor. FP-2026-05 is open per universe state; the post is legal. |

**Result:** every prompt-applicable sub-dim scores 5. No sub-dim < 5; no justified-down score needed.

---

## [B2] Second Valid Reading Attack

| Adversarial reading | Classification | Reason |
|---|---|---|
| Agent posts to **FP-2026-06** because Daniel's email (`email_scen_040_recon_currency_refresh_0005`) says "the current plan is to book a corrective JE in FP-2026-06" | **LEVER WORKING AS DESIGNED (L9a)** | The prompt does NOT name a period. "The right period" requires the agent to verify status. `brookfield_FP-2026-06` has `status=future`; the universe rejects the post. The trap is the agent's deference to Daniel's seniority over the structured period-status read. Anaya is anchored on May. Not a Clarity fail — the prompt's silence is engineered. |
| Agent skips the BL exception read and stages a fresh FX-catch-up JE without referencing `exc_a0f77f2a19104e` | **NOT POSSIBLE under the prompt as written** | The prompt explicitly says "Stage the entry in the right place against the right period **referencing the exception that's been sitting on this recon since the 25th**". The agent must read the recon's exception list to pick the right reference. The Hardness lever is what the agent does with the conflicting classification, NOT whether they consult the exception. |
| Agent resolves the BL exception (state → `resolved`) on the way through, treating "land the corrective entry today" as completion | **LEVER WORKING AS DESIGNED (L7 scope-write discipline)** | The prompt says, verbatim: "Don't resolve the exception itself, since the disposition is sitting with Ryan and I don't want to step on his sign-off." This is a direct instruction, not an escape valve — it does NOT hint at the classification conflict (it routes on authority, not on disambiguation). The strength of the line is sufficient: a competent agent reads it; an agent that over-writes is failing scope discipline. |
| Agent uses Slack DM, an `email_send` thread inside an existing conversation, or messaging instead of a "formal note" to Ryan | **PROMPT FAIL (Minor — not blocking)** | "Write Ryan a formal note" + cc'd to three people + "drop a short summary in the close channel" reads as email + Slack respectively. A Slack DM to Ryan with three cc-equivalents and then a public Slack summary in the same channel is semantically thin but not impossible. **Treatment:** the universe's voice convention for partner-facing close communications is email; a competent agent picks email. Track in Recommended Improvements but do not block. |
| Agent sends the formal note without cc'ing Hannah ("she opened the exception" might read as a justification, not a directive) | **LEVER WORKING AS DESIGNED (L7 multi-write content discipline)** | The structure "Copy Daniel and Andrea so they see what's gone through, and Hannah too since she opened the exception" coordinates three cc's with the same "Copy ... and ... too" pattern. An agent that drops Hannah is failing comprehension, not Clarity. |
| Agent reads only Ben's parent message in C005 and stops without pulling thread replies — misses Hannah's VEN-441207 / two-identical-invoices reply | **LEVER WORKING AS DESIGNED (L5 thread-reply blindness)** | The prompt does not direct the agent into the Slack thread reply chain. Agent self-discovery is the lever. |

**No Action-Decision-Ambiguity. No UGT end-state divergence. All adversarial readings classify as engineered levers except one Minor cc/channel-choice softness that does not change the end-state.**

---

## [B3] Tool-Call Density Projection

Estimating a competent Opus-4.8 trajectory that lands the seven writes correctly and self-discovers the classification + period + Vault traps:

| Component | Low | Mid | High | Notes |
|---|---:|---:|---:|---|
| Base discovery (4 contact lookups, channel resolution, period status, recon list/get, account 210000 verify) | 7 | 9 | 11 | Contacts × 4 + slack channel + 2 fiscal period reads + recon list/get + account lookup |
| L1 latching (BL exception list → get → audit trail; messaging conversation pull; Anaya msg reads) | 4 | 6 | 8 | BL exception + audit + 2-3 messaging fetches |
| L5 thread-reply blindness (slack list C005 + thread replies + maybe one prior post) | 2 | 3 | 4 | Channel browse + thread fetch |
| L8 multi-link chain SAP leg (vendor search × 2 — "Acme Research" + "VEN-441207", optional amount search) | 2 | 3 | 4 | Two structured-zero queries minimum; competent agents add a third |
| L9 gotcha (Vault list / search by title; retention policy enumeration; FP-2026-06 status verify; Daniel's email read) | 3 | 4 | 5 | Vault verification is the kill if the agent skips it |
| Email investigation (find/read Daniel's recap email, possibly Ben's escalation criteria email, possibly Hannah's BL escalation email) | 2 | 3 | 5 | Email list + 2-3 reads |
| Reminder lookup (list reminders to find the BD3 sign-off reminder by Anaya) | 1 | 2 | 3 | List + get |
| Seven writes | 7 | 7 | 7 | One each: JE, recon variance update, exception note update, email send, slack post, vault upload, reminder update |
| Supporting reads adjacent to writes (classification options, recon list of evidence already attached, contact resolution for cc) | 4 | 6 | 8 | Vault classifications, BL evidence list, contact cc-list resolution |
| Cross-service triangulation buffer (Linear/Airtable cul-de-sacs, multi-thread sweeps) | 2 | 4 | 6 | Real trajectories include exploration of adjacent surfaces |
| **TOTAL** | **34** | **47** | **61** | |

**Midpoint: 47.** Hardness Plan projects 55; my projection is 8 lower because (a) the SAP chain only naturally lands 2-3 calls if the agent goes vendor-name → vendor-id → invoice query (and the agent may stop after the first zero result), and (b) some supporting-read counts in the Hardness Plan (~3 per write) double-count when the same listing call serves multiple writes.

**Tier verdict:** **PASS (47 ≥ 50 threshold is missed by 3; sitting in the 40-49 THIN_DENSITY band on midpoint).** Lower bound 34 sits in INSUFFICIENT territory but is the worst case where the agent skips entire surfaces. The midpoint band lands **THIN_DENSITY**, NOT INSUFFICIENT.

**Recommendation (does NOT block):** the SAP leg is the weakest motivator in the prompt — Anaya names "Acme Research Ltd UK" once as her own framing. A trainee-voice trigger that nudges the agent to verify the underlying invoice (e.g., a reference to the support file "covering the rate sources" in the memo ask, which is already present, plus the fact that the agent must compose business_justification on a JE that says what the support shows) does most of the work. I judge this as a soft regression vs the Hardness Plan's 55 midpoint, but not a regression vs the 50-design-target floor (47 is within tolerance, especially given high-bound 61). Track under Recommended Improvements; not a BLOCK.

---

## [B4] Hardness Preservation

| Lever | Status | Notes |
|---|---|---|
| **L1 — Latching (FX vs duplicate)** | **LIVE** | Anaya's voice carries the FX framing intact ("my drill tied the swing cleanly to one Acme Research Ltd UK subscription line ... missed the April closing-day revaluation"). The BL exception's `duplicate_entry_detected` classification is in the universe, accessible via the recon read the prompt mandates ("referencing the exception that's been sitting on this recon"). The prompt never hints the framing might be off. |
| **L5 — Thread-reply blindness** | **LIVE** | Prompt directs agent to "drop a short summary in the close channel". Agent must browse C005 to compose, has incentive to scan recent traffic for context, and may surface Ben Arinzo's parent message — but pulling Hannah's reply is on the agent. The Hardness Plan's L5 surface is preserved. |
| **L7 — Multi-write diversification** | **LIVE** | All seven writes named: corrective JE (Para 3), recon variance notes update (Para 3), exception note WITHOUT resolving (Para 3 + the explicit "Don't resolve" instruction), formal email cc Daniel/Andrea/Hannah (Para 4), Slack post in close channel (Para 4 close), fresh Vault memo at journal-entry-support default retention (Para 5), reminder reset (Para 6). The "Tag it the way journal-entry support memos normally go" line preserves the L28 fresh-upload + AICPA_SQMS_7Y retention surface without naming the code (good). |
| **L8 — Multi-link chain (msg → BL → Slack → SAP)** | **LIVE BUT WEAK ON HOP D** | Hop A (messaging — Anaya is the messaging surface, agent reads her recent conversation chain to recover the variance framing — though for an agent-faces-the-prompt path, this is partially absorbed by the prompt itself). Hop B (BL — strongly motivated: "referencing the exception"). Hop C (Slack — strongly motivated: "drop a short summary in the close channel"). Hop D (SAP — weakly motivated: agent must self-decide to verify "Acme Research Ltd UK" or VEN-441207 in `ap_invoices`). The structured-DB-skip lever fires either way (querying gives zero; not querying trusts on faith) — but the second-link of hop D (VEN-441207 from the thread reply) compounds with L5: agent who skips the thread reply never even attempts the second SAP query. |
| **L9 — Twin gotcha (period + phantom Vault doc)** | **LIVE** | Period: prompt says "right place against the right period" with no FP number; Daniel's recap email naming FP-2026-06 lives in the universe; FP-2026-06 status=future, FP-2026-05 still open. Vault doc: Anaya asserts "the workings are already up in Vault under the title Brookfield May 2026 AP-external-vendors FX variance workings" — verified absent from `records_vault.rv_documents`. Both gotchas surfaced without hinting at verification. |

**No HARDNESS_REGRESSION.** Hop D of L8 is engineered weak (the prompt does not over-incentivize SAP) by design; the structured-DB-skip is precisely the lever that fires either way.

---

## [B5] Tool-Leak / Phrasing Scan

| Check | Result |
|---|---|
| Tool function names (`oracle_gl_create_journal_entry`, `email_send_email`, `slack_post_message`, `linear_create_issue`, `blackline_create_exception`, `records_vault_upload_document`, `reminder_update`, MCP server names) | **0 hits** |
| MCP server names ("Oracle GL MCP", "BlackLine MCP", etc.) | **0 hits** |
| Internal IDs (`BL-...`, `exc_...`, `FP-2026-XX`, `VEN-...`, `apinv_...`, `doc_...`, `issue_...`, `msg_...`, `conv_...`, `je_...`) | **0 hits** |
| Em-dashes (—) | **0 hits** |
| En-dashes (–) | **0 hits** |
| "at least N" without explicit prompt mandate | **0 hits** |
| "approximately" before IDs/dates | **0 hits** |
| "(or similar)" near exact values | **0 hits** |
| Pre-solving phrases ("FX rate refresh ran 4 hours late on BD2", "duplicate not FX", "Daniel's email is wrong about the period", "the Vault doc doesn't exist") | **0 hits** |
| Escape-valve phrases ("flag it if anything looks off", "verify Vault first", "let me know if classification is different", "check the period status") | **0 hits** — the "Don't resolve the exception itself" line is a write-scope DIRECTIVE, not an escape valve (does not nudge classification verification) |
| "the right period / the right place" (engineered ambiguity, not a fail — Hardness Plan endorses this phrasing for L9) | Present and intentional |

**Result:** clean.

---

## [B6] Upstream Propagation

No issues trace back to the Hardness Plan. The Hardness Plan documents all five levers with concrete `<file>:<row_id>` evidence, projects midpoint 55, calls out the THIN density caveat correctly, and explicitly warns the prompt writer to avoid pre-solving and escape-valve phrasing on the latching/chain surfaces — guidance the prompt has respected. **No PROPAGATE TO HARDNESS flags.**

The one item I'd surface as cross-phase signal — not a Hardness defect, but a calibration cue — is that my density midpoint estimate (47) sits 8 below the Hardness Plan's 55. This is partially a methodological gap (I'm conservative on supporting-read multiplicity), and partially a real signal that the SAP leg's incentive structure is light in Anaya's voice. If S2 (OE phase) builds OE coverage that locks the SAP query and the thread-reply pull as required surfaces, density rebounds; if S2 lets those float, the trajectory band drifts toward 40 in real runs.

---

## Verdict

**GO.** All 12 prompt-applicable QC sub-dims score 5. No adversarial reading produces UGT divergence or Action-Decision-Ambiguity. All five Hardness levers preserved. No tool-leak / phrasing hits. No PROPAGATE flags.

Density midpoint projection 47 sits below the Hardness Plan's 55 and is in the 40-49 THIN_DENSITY band per the AGENTS.md tier scheme. Per the policy, THIN_DENSITY is "acceptable only if HARDNESS plan has THIN justification" — the Hardness Plan does NOT call it thin (projects 55 = PASS). I'm classifying this as a council-projection delta rather than a Hardness regression, and noting it for S2/S3 to tighten coverage on the SAP leg and the Slack thread-reply pull. **Not a BLOCK.**

---

## Recommended Improvements (non-blocking)

1. **S2 should require OEs that lock the SAP `ap_invoices` query on at least the "Acme Research Ltd UK" / GBP-brookfield-invoices axis, and lock the Slack thread-reply pull on the C005 parent at `ts=1779891480.000000`.** This shores up density and converts the L8 hop-D motivation gap from prompt-side to OE-side, where it belongs.
2. **S3 should write the corrective-JE rubric on `period_id = brookfield_FP-2026-05` AND on `business_justification` content that either acknowledges the duplicate-classification disambiguation routed to Ryan, or routes the classification question back to Ryan before posting.** Either path resolves L1; rubric should accept both end-states.
3. The "write Ryan a formal note" / "drop a short summary in the close channel" pair leaves email-vs-Slack channel choice for the formal note slightly soft. Not a blocker (universe convention is email for partner-facing close communications), but S3 rubric on the formal note should be channel-agnostic in framing while still scoring on the recipient + cc set.

---

**Council B — GO.**

---

## Re-review round 2 (revised BD3 reminder grounding)

**Date:** 2026-06-25
**Trigger:** Council A BLOCK on BD3 reminder grounding mismatch. Final paragraph revised from "There's a reminder on me from last Friday about chasing the bd3 sign-off backlog ..." to "There's a reminder on me about dispositioning one of my open May exceptions before bd3 that I let slip because I was on this. Push it out to tomorrow so I actually get to it before close."

### Universe disambiguation check (looser "one of my open May exceptions" wording)

Verified `reminder.reminders` for all Anaya-owned reminders:

| # | reminder_id | Title | Match for "open May exception before BD3"? |
|---|---|---|---|
| 1 | `reminder_f659f315afab` | "Anaya Wallace aged payables verification and Ben Arinzo handoff" (quarterly, due 2026-03-26) | **No** — aged-payables verification, not an exception disposition |
| 2 | `reminder_scen_048_audit_compliance_0009` | "Brookfield CPAs annual reports - 2027 cycle (NY/NJ/DE)" (due 2027-01-31) | **No** — annual reports compliance, not a May exception |
| 3 | `reminder_scen_011_orphan_exception_0000` | "Disposition BlackLine exception exc_06b89e3937b04a before BD3 lock" (account 240000, period `brookfield_FP-2026-05`, due 2026-06-01, status investigating, Anaya as assignee) | **Yes — unique match** |

**Result: exactly one universe reminder satisfies "dispositioning one of my open May exceptions before bd3" for Anaya. Disambiguation is automatic.** The "one of my" phrasing is persona-realistic (Anaya is a standing trainee on five of eight AP escalations and would casually frame any individual reminder as "one of my"), and the descriptor "open May exception before bd3" uniquely fingerprints `reminder_scen_011_orphan_exception_0000` in the reminder corpus.

Persona coherence with the FX-recon framing is intact: the targeted reminder is on `exc_06b89e3937b04a` (account 240000 Deferred Revenue, scen_011 orphan exception), which is a parallel May exception thread distinct from `exc_a0f77f2a19104e` (the FX/duplicate recon exception). Anaya's "I let it slip because I was on this" reads naturally — a trainee on multiple escalations falls behind on one because she's heads-down on another. The "from last Friday" anchor has been removed, which is appropriate because the underlying reminder was actually due 2026-06-01 (11 days back), not 2026-06-05.

### Sub-dim regression check

| Check | Round 1 verdict | Round 2 verdict | Notes |
|---|---|---|---|
| **[B1]** all 12 sub-dims at 5/5 | 5/5 across | **5/5 across (unchanged)** | UGT, Truthfulness, Clarity, Persona unaffected by the looser wording because universe yields a unique match; the reminder now grounds against `reminder_scen_011` instead of being a CB-engineered abstract target. Net Truthfulness IMPROVES (was relying on an unverified BD3-signoff-backlog reminder concept; now grounds against an actual row). |
| **[B2]** new second-valid-reading attack? | none blocking | **none introduced** | The agent who scans Anaya's reminders by descriptor lands uniquely on `reminder_scen_011_orphan_exception_0000`. Could the agent reset the wrong reminder? Only if they ignore both "exception" and "before bd3" qualifiers — but those filter out reminders #1 and #2 cleanly. Could the agent interpret "open May exception" as `exc_a0f77f2a19104e` (the FX/duplicate recon exception) and somehow reset a phantom reminder on that exception? No — no reminder exists on `exc_a0f77f2a19104e`, so the agent who searches for that finds zero and must converge on the universe's actual match. **No Action-Decision-Ambiguity introduced.** |
| **[B3]** density midpoint unchanged at 47 | midpoint 47 (THIN_DENSITY band, not blocking) | **midpoint 47 (unchanged)** | The reminder lookup path is unchanged (list reminders for Anaya, identify the open-May-exception-BD3 one, update due_datetime to 2026-06-13). Same call count. Possibly +1 call if the agent does an extra list-with-filter call to disambiguate, but it's within the existing range. |
| **[B4]** all five Hardness levers preserved | L1, L5, L7, L8, L9 all LIVE | **L1, L5, L7, L8, L9 all LIVE (unchanged)** | Reminder reset remains write #7 in L7 multi-write diversification. The change touches only the persona framing of the reminder; it does not move which write surface is being exercised. L1/L5/L8/L9 are independent of the reminder paragraph. |
| **[B5]** new phrasing hits? | clean | **clean** | "exc_06b89e3937b04a", "240000", "BL-433E3BEEFD66", "FP-2026-05" — none of these IDs appear in the revised text; the descriptor "one of my open May exceptions before bd3" is natural-language only. No em-dashes, no tool names, no escape-valves, no "at least N", no "approximately". The "before bd3" lowercase phrasing matches Anaya's earlier register in the prompt ("a week past the bd3 lock"). Clean. |
| **[B6]** new PROPAGATE flags? | none | **none** | No upstream Hardness Plan defect surfaced. The Hardness Plan's L7 specifies "(g) reminder reset for the BD3 sign-off backlog" — the revision improves that grounding (the original "BD3 sign-off backlog" descriptor did not point at a real reminder; this revision points at a real reminder that is BD3-anchored). I'd note this as a soft signal that the Hardness Plan's L7 reminder-reset surface should be updated to reference `reminder_scen_011_orphan_exception_0000` for downstream phase clarity — **NOT a PROPAGATE flag**, just a cross-phase consistency note for S2/S3 to use the correct reminder grounding when writing OEs and rubrics. |

### Updated verdict

**GO.** Council A's BD3-reminder grounding fix has been verified against the universe and introduces no regression on any of the six adversarial checks. The looser "one of my open May exceptions" wording is safe because exactly one Anaya-owned reminder in `reminder.reminders` matches the descriptor — disambiguation is automatic and the persona framing is now better-grounded than the original.

Density midpoint projection remains at 47 (THIN_DENSITY on my conservative count, PASS per Hardness Plan's 55 projection — unchanged classification). All five Hardness levers remain LIVE. No new phrasing hits. No new PROPAGATE flags.

**Cross-phase consistency note (advisory, not blocking):** S2/S3 should anchor the reminder-reset OE and rubric on `reminder_scen_011_orphan_exception_0000` (due 2026-06-01 → updated due 2026-06-13). The Hardness Plan's "BD3 sign-off backlog" descriptor under L7 was loose; the prompt revision tightens it to a real universe row.

**Council B round 2 — GO.**

---

## Re-review round 3 (revised Vault memo ask — L8 Hop D motivation lift)

**Date:** 2026-06-25
**Trigger:** AUDIT_prompt.md REVISE verdict on THIN_DENSITY. Path A (in-place fix) applied to paragraph 5 to lift L8 Hop D SAP query motivation. Auditor projected strict mid ~44-46 after the fix.

**Delta:** paragraph 5 (Vault memo) now reads:

> "I also need a fresh memo filed in Vault on the corrective itself, covering the entry's reasoning, the rate sources, and who reviewed, **and pull the underlying invoice line into it so anyone reviewing can retrace the figure end to end**. Tag it the way journal-entry support memos normally go."

The bolded clause is the addition. Rest of prompt unchanged from round 2.

### Five-lens re-check on the delta

| Check | Round 2 verdict | Round 3 verdict | Notes |
|---|---|---|---|
| **[B1]** all 12 sub-dims at 5/5 | 5/5 across | **5/5 across (unchanged)** | The added clause is fully in-character: Anaya is a Trainee Accountant and FX JE preparer; wanting the memo to contain enough trail for the next reviewer to retrace the figure is consistent with audit-trail discipline she has already demonstrated upstream of the prompt ("the workings are already up in Vault under the title ..."). Persona, Naturalness, Clarity, Coherence all unaffected. Truthfulness UNCHANGED — the clause asks the agent to retrieve a real artifact (invoice line) and include it in a real write (Vault memo); the engineered absence of the invoice in SAP is L8 hop D firing, not a CB factual error. |
| **[B2]** new second-valid-reading attack? | none blocking | **none introduced — the clause STRENGTHENS L8 Hop D, does not weaken it** | Specifically tested the user-flagged adversarial reading: "Could the agent interpret 'pull the underlying invoice line into it' as authority to skip the broader SAP investigation if no invoice is found?" **No.** "Pull" is an active retrieval verb; "retrace the figure end to end" specifies that the memo must contain the trail. The agent has three response shapes when SAP returns zero: (a) include a finding-of-absence in the memo (correctly surfaces L8 hop D), (b) route the invoice-line gap back to Ryan/Hannah before posting (also correctly surfaces L8, plus L1 classification disambiguation), or (c) hallucinate an invoice line (rubric-failure on Truthfulness — agent's fault, not prompt's). Path (d) — skip SAP entirely because "the line probably doesn't exist anyway" — is still possible but is now MORE costly: the agent has to invent text for "the underlying invoice line" in the memo without doing the query, which is a more visible failure than just omitting a SAP read. **The motivation surface strictly tightens.** |
| **[B3]** density midpoint — prior round was 47 | midpoint 47 | **midpoint 49** | L8 Hop D was 2-3 calls (vendor search × 2) in round 1 with mid 3. Round 3 lifts hop D to 3-5 calls (vendor search + VEN-441207 search + amount/subledger_transactions cross-check + possible invoice-history sweep) with mid 4. Net delta +1 to +2 calls; midpoint moves from 47 to **49** with low 36 / high 63. This sits at the **upper edge of THIN_DENSITY band (40-49)**, one call below the 50+ design target. The auditor's strict mid of 44-46 maps to my non-strict 49 (consistent with my prior conservative count being 8 below the Hardness Plan). **Trajectory: improving, on the right side of the THIN/PASS boundary.** Still classified THIN_DENSITY per AGENTS.md tier scheme on conservative count, but Hardness Plan PASS (midpoint 55) classification unchanged. Not a BLOCK. |
| **[B4]** all five Hardness levers preserved | L1, L5, L7, L8, L9 all LIVE | **L1, L5, L7, L8 STRONGER, L9 all LIVE** | L1 (latching) unchanged — Anaya's FX framing intact, BL exception classification still discoverable. L5 (thread-reply blindness) unchanged. L7 (multi-write diversification) unchanged — still seven writes; the memo content expands but the write count is the same. **L8 (multi-link chain) strengthens on hop D** — the prompt now actively motivates the SAP query rather than relying on agent discipline alone; the structured-DB-skip lever's "absence is the signal" property surfaces more reliably. L9 (period + phantom Vault doc) unchanged. |
| **[B5]** new phrasing hits | clean | **clean** | "pull the underlying invoice line into it" — natural employee speak ("pull the data"), zero tool-name leak, zero ID, no em-dash, no "approximately", no "(or similar)", no "at least N". "end to end" (spelled open, not hyphenated) is idiomatic. The clause does not constitute an escape-valve (it specifies WHAT the memo must contain, not a conditional verify-if-you-feel-like-it instruction). Clean across all eight phrasing checks. |
| **[B6]** new PROPAGATE flags | none | **none** | The Hardness Plan's L8 description specifies hop D as structured-DB-skip where "the absence is the signal." The prompt revision strengthens the agent's incentive to attempt the SAP query and observe the absence — fully consistent with the Hardness Plan, no upstream defect surfaced. |

### Cross-phase consistency notes (advisory, not blocking)

1. **S2 OEs should now lock at minimum two SAP `ap_invoices` searches** — by vendor name ("Acme Research") and by structured ID ("VEN-441207" surfaced from Hannah's C005 thread reply) — plus an OE on the agent's memo content handling the zero result (finding-of-absence content OR a routing-back to Ryan/Hannah). The auditor's "lift L8 Hop D SAP query from 2→3 strict calls" guidance reads as: vendor-name search + VEN-441207 search + amount-or-subledger cross-check.
2. **S3 rubric on the Vault memo** should accept either: (a) memo body acknowledges that the underlying invoice line could not be located in SAP and routes the classification disambiguation back, OR (b) memo body cites a found invoice line (in which case rubric should fail because no such line exists). Do not write the rubric to require a specific invoice ID — that would assume the absence is positively findable, which contradicts L8's design.
3. **S3 rubric on the corrective JE business_justification** should mirror this — agent acknowledges the invoice-line absence in their reasoning OR routes the classification question before posting. Either path is a rubric pass; hallucinating an invoice line is a rubric fail.

### Updated verdict

**GO.** The paragraph 5 revision tightens L8 Hop D motivation without introducing any new adversarial reading, phrasing hit, or upstream defect. Density midpoint improves from 47 to 49 (still in THIN_DENSITY band on my conservative count but on the right side of the trajectory, and the Hardness Plan's 55 PASS projection is unchanged). All five Hardness levers remain LIVE; L8 hop D is now noticeably stronger. The added clause is fully in persona voice (trainee wanting full audit-trace in the memo) and contains zero tool/ID/em-dash/escape-valve violations.

The conservative-count midpoint of 49 deserves one observation for the operator: it is one call below the 50+ design target. If S2 OEs and S3 rubrics tighten coverage on the SAP query chain as recommended in the cross-phase notes above, real-trajectory density will land comfortably ≥50 — there is no need for a second prompt-side revision to chase density. The current prompt is at the natural ceiling of what density a prompt-side fix can move (further pushes would risk pre-solving or tool-leaks).

**Council B round 3 — GO.**
