# Hardness Plan — Task 33 (Keystone / Loan Operations / Carlos Rivera)

## Persona and Business Function

- Carlos Rivera (Loan Officer — FHA + Conventional, bilingual Spanish) — `carlos.rivera@keystonemortgage.com`
- Business Function: Loan Operations
- Universe: Keystone Mortgage Partners (single entity). Universe today: 2026-06-12.

## Levers Available

| # | Lever | Status | Evidence (per-task universe citation) | Engineering plan (how S1 weaves it) | Learnings cite | Cost range |
|---|---|---|---|---|---|---:|
| 1 | Latching (cross-surface conflicting figures) | partial | `slack.slack_messages`: 10 msgs on LN-2026-00211 across C002+C005+D_denise_grace; `email.emails`: 6 emails on LN-2026-00211. `mortgage_los.loans`: LN-2026-00211 `status="withdrawn"`, updated 2026-03-28. Chatter treats trio as active; LOS contradicts. | Grace Slack DM (D_grace_robert exists, 21 msgs) framing the trio uniformly active; LOS row contradicts. | L13 first-framing trap | 5-8 |
| 2 | Structured-DB skip (`mortgage_los.conditions`) | YES | LN-2026-00009 has 3 OUTSTANDING conditions (`los_cond_74d7f24385f5`, `los_cond_739ecac87a02`, `los_cond_d7fdad61f9fa`) issued 2026-02-27 to 2026-03-03 with `cleared_date=None` (~100 days overdue). LN-2026-00184 has 0 conditions / 0 doc-checklist rows despite 9 Slack mentions and notes citing build delays + rate lock extensions. | Condition-overdue truth lives ONLY in `mortgage_los.conditions`; email + Slack chatter on LN-2026-00009 (4 emails + 8 Slack across C002/C004/C008) imply Carlos has it under control. Forces a `mortgage_los_list_conditions` call no chatter triggers. | L10 SAP-skip translated to mortgage = conditions skip | 4-7 |
| 3 | Missing reply / parent-only read | partial | `slack.slack_messages` has `reply_count` field; C002 (334 msgs) and C003 (23 msgs) on Carlos's loans show non-zero reply chains (e.g. LN-2026-00605 has 5 msgs in C003 #closings). | Plant canonical "Robert's review verdict" as Slack thread REPLY in D_grace_robert or C002 with parent stating wrong premise. | L12 thread-reply invisibility | 3-5 |
| 4 | Search-result-cap eviction | partial | C002 #loan-processing carries 334 of 573 total Slack msgs (58%). Older canonical msg can be buried under newer chatter. | Weak alone — only useful as multiplier. | L4 unreliable alone | 3-5 |
| 5 | Thread-reply blindness alone | partial | Same Slack data as L3. | Weak alone per Learnings. | L5 unreliable alone | 2-4 |
| 6 | Near-miss entity confusion | partial | LN-2026-00211 assigned to brian.mitchell (los_staff_6d606f7506a7) with processor sofia.reyes — Carlos-adjacent name pair Carlos could mis-credit. Marcus Webb (DEPARTED) is LO on LN-2026-00616 — natural confusion since LN-2026-00616 appears in Carlos's context. LN-2026-00622 actually assigned to todd.jennings (los_staff_0375f7c91014), not Carlos. | Soft lever — could mis-attribute trio loans to Carlos. | L4 unreliable alone | 3-5 |
| 7 | Multi-write diversification | YES | Natural Carlos writes: `email_send_email`, `slack_post_message` (C002 active), `mortgage_los_add_condition` (conditions table writable), `mortgage_los_update_loan`, `crm_create_engagement` (engagement_type=NOTE pattern at `crm_engagement_fc92d4a91195`). | Email to Grace summarising trio, Slack note in C002, CRM engagement update, condition/loan write. 4 writes × 3 supporting reads. | L5 — for density not stumping | 9-12 |
| 8 | Multi-link chain | YES | A (Grace Slack ask in D_grace_robert / C002) → B (loan + condition lookup in `mortgage_los`) → C (CRM engagement read for stale status; 472 engagement rows) → D (write reconciling). | "Pipeline review for Grace" frame naturally requires 4 hops. Stack reductions across mortgage_los + slack + crm. | L8 three reductions across three services | 6-9 |
| 9 | Authority dismissal | YES | Grace Yamamoto is in `slack.slack_users` (keystone_e304643b171b) and `email` surfaces but NOT in `mortgage_los.staff` (she is an org-level operations role, not an LOS-assignable resource). Robert Calloway IS in `mortgage_los.staff` as broker (los_staff_e85bc913c756 — oversight / escalations / compliance specialization). CORRECTED v2: Grace plant must live in `D-grace-yamamoto` MPIM (Grace + Carlos + Sofia + 1 other — Carlos has read access) OR in C002 #loan-processing as a Grace message tagging Carlos. `D-grace-robert` is Grace+Robert only, Carlos has no read access there. Authority candidates that Carlos can hear from: Grace (via D-grace-yamamoto or C002), Sofia (D-sofia-carlos exists), Robert (D-DENISE-ROBERT does not include Carlos either — Robert reaches Carlos via C002 or email). | Plant Grace Slack message in D-grace-yamamoto MPIM (Carlos-readable): "LN-2026-00211 is back in motion. Sofia got it un-stuck, just hold the line on the new appraisal." Plausible-but-wrong: LOS says withdrawn 2026-03-28. | L9 (~100% fail; HIGHEST yield) | 3-5 |
| 10 | Reversal / supersession | YES | LN-2026-00211 `status="withdrawn"`, `updated_at=2026-03-28T12:00:00+00:00`, but named in PersonaBrief as "pipeline review" loan. Slack chatter (10 msgs) treats it as active. 14 doc-checklist items in `received`/`required` (artifacts pretending it is still active). | Pipeline-review prompt names a trio; agent must check status per loan. Withdrawn one looks live in chatter. | L10-style reversal (mortgage variant) | 4-6 |
| 11 | Net-vs-gross framing | partial | `stripe.charges` has `amount_refunded` field on every row (1730 charges). Carlos-loan credit-report/appraisal fees could be planted with refund partials. | Could plant stripe refund on credit-report or appraisal fee for one of the trio; agent uses gross. | L11 net-vs-gross | 4-7 |

**Bonus (newer Learnings):**
- **L25 Existing-output anchor**: stale CRM engagement NOTE on the LN-2026-00211 deal saying "lock extended, on track". `crm.crm_deals` 80 rows; `crm.crm_engagements` 472 with engagement_type=NOTE pattern. Anchored agent reads existing engagement instead of LOS status. **Cost 4-6 → midpoint 5.0.**

## Selected Levers (3 to 5)

- **L10 Reversal/supersession on LN-2026-00211** — withdrawn loan framed by PersonaBrief as active "pipeline review trio" member. LOS status is the binary truth; 10 Slack msgs + 6 emails create chatter that pretends it is in motion. — projected cost midpoint **5.0**.
- **L2 Structured-DB skip on `mortgage_los.conditions`** — LN-2026-00009 has 3 outstanding conditions overdue ~100 days; load-bearing truth lives ONLY in conditions table. — projected cost midpoint **5.5**.
- **L1 First-framing trap + L25 Existing-output anchor (Carlos's own quoted over-promise)** — replaces L9 v2. CORRECTED v3 after AUDIT round 1 finding: Grace cannot plausibly be the authority-dismissal sender on LN-2026-00211 because Grace's own 2026-03-25 emails to Marcus identified 211 as a spouse-conflict fraud-investigation file (loan withdrawn 2026-03-28). Any Grace plant saying "211 is back in motion" contradicts her documented investigative role. RESOLUTION: the "211 was back in motion because Sofia had it unstuck" claim is now Carlos's OWN self-quoted over-promise to Grace (per PersonaBrief: "He tends to over-promise timelines"). This is universe-consistent with Carlos's persona and shifts the carrier from L9 (Grace's authority dismissal) to L1 first-framing (Carlos's confident wrong premise that the agent inherits) + L25 existing-output anchor (Carlos's prior statement is the anchor). The L10 reversal trap (211 actually withdrawn) is still triggered. — projected cost midpoint **4.0**.
- **L8 Multi-link chain across mortgage_los + slack + crm + email** — Grace ask → LOS loan + condition lookup → CRM engagement history → reconciling write. Three reductions across three services. — projected cost midpoint **7.5**.
- **L25 Existing-output anchor** — stale CRM engagement NOTE on LN-2026-00211 deal saying "lock extended, on track". Anchored agent reads CRM instead of LOS status. (Highest-yield novel stump per Learnings.) — projected cost midpoint **5.0**.

## Tool-Call Density Projection

| Component | Range | Midpoint |
|---|---|---:|
| Base discovery (Carlos contact + 16 open loans + channel directory + 17 staff + conditions table) | 5-8 | 6.5 |
| L10 Reversal (status check + history for LN-2026-00211) | 4-6 | 5.0 |
| L2 Structured-DB skip (conditions + document_checklist_items queries on the trio) | 4-7 | 5.5 |
| L9 Authority dismissal (read Grace DM + cross-check) | 3-5 | 4.0 |
| L8 Multi-link chain (slack → LOS → CRM → email reconciliation) | 6-9 | 7.5 |
| L25 Existing-output anchor (read existing CRM engagement + stale Slack thread) | 4-6 | 5.0 |
| Write actions (4 writes × ~3 supporting reads: email to Grace, Slack in C002, CRM engagement, condition update) | 9-12 | 10.5 |
| Cross-service triangulation buffer | 5-8 | 6.5 |
| **TOTAL projected** | **40-61** | **50.5** |

**Gate verdict:** midpoint 50.5 ≥ 50 → **PASS (design target met).**

## Service Breadth (v11 G1)

| Service | Projected calls | % of 50.5 |
|---|---:|---:|
| `mortgage_los` (loans, conditions, document_checklist_items, staff, borrowers) | 16 | 32% |
| `slack` (channels list, messages search, thread fetch, post_message) | 10 | 20% |
| `email` (search threads, list emails, send_email) | 8 | 16% |
| `crm` (engagements list, deals list, create engagement) | 7 | 14% |
| `contacts` (contact lookup for Grace / Sofia) | 4 | 8% |
| `quickbooks` OR `filesystem` (fee context OR PDF reference for new construction) | 3 | 6% |
| `stripe` (optional credit-report fee on one loan) | 2.5 | 5% |
| **Distinct services** | **7** | — |

**Breadth gate:** ≥ 4 distinct services with each ≥ 5%; dominant share 32% (well under 60%) → **PASS (breadth).** No false-positive single-service density pattern.

## Stump Hypothesis (2 to 4 predictions)

1. **[HIGH]** Agent reports LN-2026-00211 as part of the "active" pipeline trio. Mechanism: L10 reversal + L9 authority dismissal. Reasoning: LOS row has been `withdrawn` since 2026-03-28; Grace's DM and 10 Slack msgs frame it in-motion. Agent trusts chatter over `mortgage_los_get_loan` status check, especially when Grace appears to confirm.
2. **[HIGH]** Agent's write to Grace omits the 3 overdue conditions on LN-2026-00009 (`los_cond_74d7f24385f5`, `los_cond_739ecac87a02`, `los_cond_d7fdad61f9fa`). Mechanism: L2 structured-DB skip. Reasoning: outstanding conditions live ONLY in `mortgage_los.conditions`; no Slack/email message restates them; agent that skips `mortgage_los_list_conditions` reports the loan as conditionally-approved-and-progressing.
3. **[MED]** Agent picks stale CRM engagement / decoy Slack thread as ground truth. Mechanism: L25 existing-output anchor + L26 decoy parent thread. Reasoning: with 472 CRM engagements and 334 messages in C002, plausible decoy artifacts on the trio loans will look more "current" than the LOS row.
4. **[MED]** Write artifacts mis-attribute LN-2026-00622 to Carlos. Mechanism: L6 near-miss entity / first-framing trap. Reasoning: LN-2026-00622 is actually assigned to todd.jennings (los_staff_0375f7c91014); PersonaBrief and Grace's framing imply Carlos. Agent that copies trio into the write without verifying `assigned_lo` cascades the wrong scope.

## Hardness Score

**4/5 — PASS**

Levers L10 + L2 + L9 + L8 + L25 are individually verified in the per-task universe with concrete row citations; density midpoint 50.5 meets the design target; service breadth across 7 services is healthy. Not 5/5 because L25 anchor and L9 dismissal both depend on planted artifacts that the S1 prompt-writer must phrase carefully to keep the dismissal plausible-but-wrong without leaking the answer. **Robert is NOT in `mortgage_los.staff` — only Grace + Sofia + Camille + Denise can voice an authority dismissal without fabrication risk.**

## Hardness Brief for the Prompt Writer (v3)

Frame the task as Carlos asking the agent (Carlos's assistant) to put together a pipeline-review packet for Grace covering the trio Grace flagged: LN-2026-00009, LN-2026-00211, LN-2026-00622. CORRECTED v3 (after AUDIT round 1): the L9 authority-dismissal-from-Grace mechanism was replaced by L1 first-framing + L25 anchor via Carlos's own quoted over-promise. Reason: Grace cannot plausibly say "Sofia got 211 unstuck" because her own 2026-03-25 emails identify 211 as a Marcus-Webb spouse-conflict fraud-investigation file (loan withdrawn 3 days later). Instead, the prompt has Carlos self-quote: "I told her 211 was back in motion because I thought Sofia had it unstuck" — Carlos's wishful self-talk per his over-promise persona. The agent inherits Carlos's wrong premise (L1 first-framing) and Carlos's prior claim is the existing-output anchor (L25). The prompt MUST believe all three are active and progressing — never hint that LN-2026-00211 has been withdrawn (L10 trap), never restate the overdue conditions on LN-2026-00009 in any email/Slack body (L2 structured-DB skip on `mortgage_los.conditions`). Grace's universe presence in S2 is a low-spec ping (no specific claims about 211 status) consistent with her org-level operations role; the plant lives in `D-grace-yamamoto` MPIM (Grace + Carlos + Sofia + 1 other; Carlos-readable) or in C002 #loan-processing. Originally proposed D-grace-robert (corrected v2 — Carlos not a member); then proposed Grace authority dismissal (corrected v3 — contradicts her March investigation emails). The agent's required writes — short Grace email, C002 surface note, CRM engagement update, and a condition/loan write reflecting actual status — give a 4-write surface yielding ~50 tool calls across mortgage_los + slack + email + crm + contacts + quickbooks/filesystem + stripe (7 services). Anchor rubrics on (a) LN-2026-00211 being correctly flagged as withdrawn-not-active, (b) the three overdue conditions on LN-2026-00009 being surfaced by ID, and (c) LN-2026-00622 not being attributed to Carlos. Target pass@1 ≤ 40%; expected dominant failure mode is L10 + L9 cascade missing the withdrawn-status flip.
