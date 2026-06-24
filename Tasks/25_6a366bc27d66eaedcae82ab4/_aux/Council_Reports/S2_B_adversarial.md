# Council B — S2 Oracle Events — Adversarial QC + Density + Hardness + Tool-leak

**Task:** Tasks/25_6a366bc27d66eaedcae82ab4
**Phase:** S2 (Oracle Events)
**Round:** 2 (post-AUDIT density REVISE [LOW])
**Council role:** B — Adversarial QC, Density Projection, Hardness Preservation, Tool-leak scan
**Deliverable under review:** `6_Oracle_Events.txt` (30 OEs, up from 28)

---

## Round 2 context

Round 1 closed GO across all sub-dims (5/5) with density midpoint **49.0**. AUDIT returned **REVISE [LOW]** on density (THIN-by-1 vs strict 50+ bar). Two new discovery OEs were inserted in the discovery zone:

- **NEW OE 12** — `messaging_search_conversations` + `messaging_get_conversation` to surface George's DM thread reinforcing the partial-feed narrative (L1 Latching reinforcement; anchors `msg_2022a15f5fbd` from `Hardness_Plan.md`).
- **NEW OE 16** — `oracle_gl_list_journal_entries` filtered by `period_id "brookfield_FP-2026-05"` with client-side narrow to account `119000` (sanity check before staging the $147,825 JE in OE 22).

Downstream OEs renumbered (old 12→13 … old 28→30). Total now 30 OEs.

Only the affected analyses are re-run: **[B1]** QC re-score, **[B3]** density re-projection, **[B4]** lever preservation, **[B5]** tool/ID/em-dash/en-dash scan on the new OEs and the renumber boundary. **[B6]** upstream propagation: none expected.

---

## [B1] QC sub-dim re-score (STRICT)

| Sub-dim | Verdict | Evidence |
|---|---|---|
| **OE Completeness** | **5/5** | OE 12 adds the messaging surface that Hardness_Plan L1 enumerates by ID (`messaging.messages:msg_2022a15f5fbd`); without it the latching surface count is 5 not 6. OE 16 adds the standard "no in-flight JE conflict" sanity that the write action in OE 22 implicitly relies on. No previously-required step was deleted; renumbering preserves every original step's text. |
| **Accuracy** | **5/5** | OE 12 cites the exact Hardness_Plan ID for the DM thread; tool names match `8_Server_Tools_Details.json` (`messaging_search_conversations`, `messaging_get_conversation`, optional `messaging_show_data`). OE 16 cites `oracle_gl_list_journal_entries` and pattern-matches the period/account combo with the same client-side narrow pattern used throughout (OE 8, OE 14, OE 18). No fabricated IDs. |
| **Scope** | **5/5** | Both new OEs sit strictly inside discovery. OE 12 is a read-only conversational lookup (Latching reinforcement). OE 16 is a read-only JE-surface scan (a precondition for the existing write in OE 22). Neither adds a write, neither expands prompt scope, neither introduces a new lever. |
| **Coverage Order** | **5/5** | OE 12 lands after OE 11 (Slack thread) — the natural place for the third conversational surface in the L1 reinforcement chain (recon variance_explanation → doppelgänger reviewer_comments → Andrea email → Hannah reply → Slack thread → messaging DM). OE 16 lands after OE 15 (subledger feed run sanity) and before OE 17 (account-role check), inside the pre-write structural block. Both insertions respect the discovery → structural → write progression. |
| **Realistic Agent Trajectory** | **5/5** | A diligent agent that has read the recon variance_explanation, the doppelgänger reviewer_comments, Andrea's email, Hannah's reply, and the Slack thread would naturally check messaging for any DM context before treating the partial-feed framing as canonical — OE 12 is what that diligence looks like. A diligent agent staging a manual JE on an open period would naturally scan the JE surface for any in-flight conflict on the same period+account — OE 16 is what that diligence looks like. Both extend the established pattern of paginated list + client-side narrow used elsewhere. |

**[B1] re-score: 5/5/5/5/5 — PASS (STRICT).**

---

## [B3] Density re-projection (STRICT 50+ bar)

Round 1 projected midpoint: **49.0** (THIN-by-1 vs the strict bar).

New OE call estimates:

| OE | Calls | Midpoint | Notes |
|---|---|---|---|
| OE 12 (messaging) | `messaging_search_conversations` + `messaging_get_conversation` (+ optional `messaging_show_data`) | **2.0** | Search returns the DM thread, fetch returns the full message list; optional show_data adds 0.5 for agents that probe attachments. Matches the L1 reinforcement pattern in Hardness_Plan. |
| OE 16 (JE surface) | `oracle_gl_list_journal_entries` filtered by period (1 call, possibly paginated) | **1.5** | Single list with offset/limit; pagination adds 0.5 for an agent that walks more than one page on the high-traffic period. |

**Net delta: +3.5**

Round 2 midpoint: **49.0 + 3.5 = 52.5**

Range envelope updates from `40–62` to approximately **42–66** (each new OE adds ~1 floor and ~2 ceiling).

**Re-projection vs the strict 50+ bar:**

- **Midpoint 52.5 ≥ 50 → PASS** (2.5 above the bar, no longer THIN).
- Floor 42 is well above the absolute 40 floor.
- Two independent buffers remain available if a future audit tightens further: (a) the conversation-surface reinforcement reads (L1 surfaces 1–6 each plausibly re-touched on agent re-verification), and (b) cross-service triangulation buffer already booked at midpoint 6.5.

**[B3] verdict: density PASS at STRICT 50+ bar.** Round 2 midpoint **52.5**, range **~42–66**, margin **+2.5 over strict bar / +12.5 over absolute floor**.

---

## [B4] Hardness lever preservation

| Lever | Status pre-round-2 | Status post-round-2 | Change |
|---|---|---|---|
| **L1 — Latching** | 5 conversational surfaces (recon variance_explanation, doppelgänger reviewer_comments, Andrea email, George→Hannah self-quote, Slack thread) | **6 surfaces** — adds messaging DM thread via OE 12 | **STRENGTHENED** — exactly the 6th surface enumerated in Hardness_Plan Lever 1 evidence (`messaging.messages:msg_2022a15f5fbd`). Latching framing now repeats across recon + recon-doppelgänger + email + email-reply + Slack + DM, which is the strongest form of the lever the universe supports. |
| **L2 — Structured-DB skip (primary)** | `ogl_subledger_feed_runs` walk via OE 13–14 (was 12–13 pre-renumber); contradicts partial-feed narrative | OE 14–15 (post-renumber) unchanged in text and intent | **PRESERVED** — the load-bearing structural contradiction (`run_e33ed2561f2c46`, status success, 2083/2083 rows posted, 0 rejected) is intact. OE 12 cross-references it explicitly ("exactly the pattern the structural feed-run record will contradict in OE 14 to 15") — the renumber landed on the correct downstream OE numbers. |
| **L2 — Structured-DB skip (secondary)** | `blackline_review_notes` via OE 7 (Edith's `rn_564e65ce0d594f`) | OE 7 unchanged | **PRESERVED.** |
| **L6 — Near-miss entity confusion** | OE 3–5 (canonical recon vs doppelgänger; account 119000 entity-role asymmetry in OE 15→17) | OE 3–5 unchanged; account-role check now at OE 17 | **PRESERVED.** Renumber correctly moves the account-role check from old 15 to new 17. |
| **L8 — Multi-link chain** | Andrea email → BL recon → feed-run verification → exception + Hannah reply → JE staging | Unchanged hops, same 4-service families | **PRESERVED.** OE 16 adds a JE-surface pre-write read inside the chain but does not break the A→B→C→D→E shape. |
| **L9 — Universe-grounded gotcha** | OE 16–18 (RV restricted doc + retention codes + open-period note) | OE 18–20 (post-renumber) unchanged in text | **PRESERVED.** |
| **Authority-dismissal layer (Learnings L9)** | Andrea + Hannah soft-verb anchors via OE 2 and OE 10 | Unchanged | **PRESERVED.** |

**[B4] verdict: every selected lever preserved. L1 strengthened (5→6 surfaces). No lever cost re-balancing required.**

---

## [B5] Tool / ID / em-dash / en-dash re-scan

Scope: full text of OE 12 and OE 16, plus the renumber boundary (OE 11→12→13 and OE 15→16→17) for cross-reference integrity.

### Tool names (allowed only in OE bodies, not in prompt or rubric titles)
- OE 12: `messaging_search_conversations`, `messaging_get_conversation`, `messaging_show_data` — all present in `8_Server_Tools_Details.json`, all in OE body only. **OK.**
- OE 16: `oracle_gl_list_journal_entries` — present in tools file, in OE body only. **OK.**

### Parameter names
- OE 12: `query`, `conversation` (implicit from messaging family) — consistent with Brookfield universe constants section in `AGENTS.md` (messaging uses `content`, not `body`; no body param invoked here, so no trap hit).
- OE 16: `period_id`, `offset`, `limit`, `account_id` — match the JE list signature. **OK.**

### IDs / values
- OE 12: `BL-75810CD0FEE4`, `exc_1ddfc978ce5a4d`, `msg_2022a15f5fbd` — all match Hardness_Plan and Universe_Index records.
- OE 16: `brookfield_FP-2026-05`, `119000`, `$147,825` — match Universe_Index, Andrea's email anchor figure, and the chart-of-accounts role on Brookfield.

### Em-dash / en-dash scan
- OE 12 body: hyphens only in compound modifiers (`partial-feed`, `engagement-hours`, `May close`); no `—` (U+2014), no `–` (U+2013). **CLEAN.**
- OE 16 body: hyphens only (`client-side`, `WIP-to-revenue`, `in-flight`); no em-dash, no en-dash. **CLEAN.**

### Renumber-boundary cross-reference integrity
- OE 12 references "OE 14 to 15" for the structural feed-run contradiction. Post-renumber, OE 14 = `oracle_gl_list_subledger_feed_runs` walk, OE 15 = `oracle_gl_get_subledger_feed_run` confirmation. **Correct.**
- OE 22 (write JE) is referenced by OE 25 (RV upload) as "the staged JE entry_id from OE 22" and by OE 27 (email reply) implicitly. Post-renumber, OE 22 is the JE write action. **Correct.**
- OE 25 references "engagement-stage backup" linkage to `doc_42c851aed8fb40ab` from OE 18. Post-renumber, OE 18 is the records_vault_list_documents discovery for the support memo. **Correct.**
- OE 28 (`reminder_delete_reminder`) targets `reminder_scen_010_orphan_exception_0000` found in OE 21. Post-renumber, OE 21 is the reminder discovery. **Correct.**
- OE 30 references items (a)–(g) anchored on writes in OE 22–29. All anchor numbers consistent.

### Convention checks against `Strict_Convention_Inventory.json` / `OE_Convention_Inventory.json`
- No tool names appear in the prompt (`5_Prompt.txt` re-confirmed clean by spot-check on the request body; no new prompt edits anyway).
- No "at least N" phrasing introduced.
- No reference to guides / specs / frameworks.

**[B5] verdict: CLEAN.** No tool leak into prompt, no ID drift, no em-dash, no en-dash, all cross-references post-renumber land on the correct downstream OE numbers.

---

## [B6] Upstream propagation

No prompt revision is implied by adding two discovery OEs. The prompt language ("Pull the May engagement-stage support, confirm the recognition figure ties out across our records, and walk the reconciliation end to end. I want the actual state, the evidence attached, anything else opened or reviewed against it that I have not seen") already implicitly authorizes both:

- The messaging DM check (OE 12) — covered by "anything else opened or reviewed against it that I have not seen" reading.
- The JE surface sanity (OE 16) — covered by the standard "stage the recognition entry … queued for Daniel's review through the normal close path" precondition.

**[B6] verdict: no upstream propagation required. Prompt unchanged.**

---

## Summary

| Check | Round 1 | Round 2 |
|---|---|---|
| QC sub-dims | 5/5/5/5/5 | 5/5/5/5/5 |
| Density midpoint | 49.0 (THIN-by-1 vs strict 50+ bar) | **52.5** (PASS, +2.5 over strict bar) |
| Lever preservation | All 5 levers intact | All 5 intact; **L1 strengthened (5→6 surfaces)** |
| Tool / ID / em-dash / en-dash | Clean | Clean |
| Upstream propagation | n/a | None required |

The two inserted OEs are minimum-touch, lever-aligned, discovery-zone-correct, and recover the strict density margin with headroom. The renumber landed without breaking any internal cross-reference. L1 latching is meaningfully stronger now that the 6th conversational surface enumerated in `Hardness_Plan.md` is on-trajectory rather than left implicit.

---

## VERDICT: GO