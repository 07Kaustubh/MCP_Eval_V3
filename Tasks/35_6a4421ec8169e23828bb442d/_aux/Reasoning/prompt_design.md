# Prompt Design — S1 Final Report

**Task:** 35_6a4421ec8169e23828bb442d
**Universe:** keystone (Keystone Mortgage Partners)
**Persona:** Robert Calloway — Owner / Licensed Mortgage Broker
**Business Function:** Executive (10% KeyStone target)
**Anchoring scenario:** `scenario_14b3ffde` — 2 BTC ransomware / 72-hour cloud-backup decision (dated 2026-03-20, ~5.5 weeks stale vs universe today 2026-04-28)
**Final word count:** 397 / 500 cap
**Final iteration:** v2 (S1 REVISE round 1 of 3 applied)

## Levers engineered into the prompt

| # | Playbook Lever | Learnings tag | How the prompt surfaces it |
|---|---|---|---|
| 1 | L8 Multi-link chain (email → Slack → CRM) | §L8 | "Find the freshest signals on the incident and reconcile them, wherever they live" — pushes multi-service triangulation |
| 2 | L1 Latching (Raj authority framing on restore path) | §L9 + §L24 soft-verb | "Raj's read that night was that the restore path is expensive... So walk Raj's picture back to what the emails and records actually say... If restore is still a lift, I want the specific gaps and rebuild items as tradeoffs, not a foregone conclusion" |
| 3 | L2 Structured-DB skip (CRM engagement notes are load-bearing surrogate for Brookfield SAP skip) | §L10 | Implicit via "wherever they live" — pulls agent to CRM 3/20 + 4/07 + 4/14 stream |
| 4 | L10 Cross-scenario reconcile (reframed from supersession per AUDIT F1 fix) | §L25 | "Denise queued a preliminary plan the night this started... Do not take the March framing at face value. Anything feeding the same borrower notice counts, even from a separate workstream." — explicit scope broadening |
| 5 | L4 Decoy parent thread (C001 exec-general vs C002 loan-processing vs C008 IT-support vs D_grace_robert_denise DM) | §L26 | "Post a short status in the leadership channel so we are all reading the same room without pushing it wider than needed" — leaves channel resolution to agent, biased toward D_grace_robert_denise DM |

## Expected stump targets (Opus 4.8 failure predictions)

1. **[HIGH]** Agent stops at Denise's 3/20 preliminary plan and never reconciles across the 4/07 UWM broker-portal exposure and 4/14 Marcus post-term-access CRM streams. Mechanism: Learnings §L10 (structured-DB skip) + §L25 (existing-output anchor). Rubric outcome: fails the cross-scenario reconciliation rubric that requires the brief to enumerate specific borrower-notice-relevant file lists from all three streams.
2. **[HIGH]** Agent latches on Raj's technical-authority framing that restore is costly and materially misweights the pay-vs-restore analysis toward payment for Monday-closings urgency. Mechanism: Learnings §L9 (authority-figure dismissal). Rubric outcome: fails a decision-quality rubric that requires the brief to enumerate the specific restore-path tradeoffs as an itemized list rather than treat restore as a foregone conclusion.
3. **[MED]** Agent posts the Slack status to C001 (general/company-wide, 30 members) or C002 (loan-processing where Grace's Monday-closings tactical thread lives) or C008 (it-support) instead of the D_grace_robert_denise 3-way DM. Mechanism: Learnings §L26 (decoy parent thread). Rubric outcome: channel-pinned Slack-write rubric fails on `channel_id` check. Dependent on S2 OE writer pinning D_grace_robert_denise per AUDIT F2 downstream guidance.
4. **[MED]** Agent routes cyber-counsel email to a Bennett-* variant (5 candidates including `lbennett@bennettcyberlaw.com` which is a semantic near-miss for "cyber counsel") rather than `megan.sloane@wardbarrettlaw.com`. Mechanism: Learnings §L4 (near-miss entity — supporting only). Rubric outcome: contact-resolution rubric fails on `recipient` field for the counsel-outreach email write.

## Gate results

| Gate | Result | Notes |
|---|---|---|
| Validator `validate.py --phase prompt` | PASS — 0 fails / 0 warns / 6 notes | Word count 397 (sweet-spot), 2 distinct services (email + slack) counted, universe = keystone |
| Universe atom verifier | PASS — 0 fails / 0 warns / 0 atoms | Prompt has no explicit dollar/date/ID atoms requiring verification (deliberate — hardness comes from implicit references) |
| Council A v2 (Grounding + Convention) | GO | All 8 perspectives PASS. New sentence "Anything feeding the same borrower notice counts, even from a separate workstream" grounds against 3+ cross-scenario workstreams verified in `crm.crm_engagements.json` (3/20 ransomware stream, 4/07 UWM broker-portal exposure, 4/07 LOS export by Raj, 4/14 Marcus post-term) |
| Council B v2 (Adversarial QC + Density + Hardness) | GO | 12/12 Prompt sub-dims at 5/5. Density midpoint projected 56 (range 44-70). All 5 Hardness levers preserved. Zero PROPAGATE flags |
| Similarity gate `calc_similarity.py` | PASS | Max composite 28.4 vs QC_Tasks/V3_Tasks/Task14 (well under 40 pivot threshold) |
| Strict veteran AUDIT v2 (iteration 2 of 3) | PASS (STRICT) | F1 (L25 supersession → CROSS_SCENARIO_RECONCILE) resolved via 1-sentence prompt addition. F2 (leadership-channel ambiguity) carried as MINOR-downstream-fixable at S2 (OE writer pins `channel_id = D_grace_robert_denise`) |

## Iteration history

**v1** (initial draft): 4 councils passed but AUDIT (iteration 1) flagged F1 MAJOR — L25 supersession lever miscited in Hardness Plan (4/14 CRM is Marcus post-term stream, not ransomware supersession; there is no ransomware-specific supersession post-3/20). AUDIT recommended reframe to CROSS_SCENARIO_RECONCILE via 1-sentence prompt addition.

**v2** (post-AUDIT-revise, current): 3 changes applied — (a) para 1: "before the end of the week" → "this week" (compression); (b) para 3: compressed 2 phrases + inserted new sentence "Anything feeding the same borrower notice counts, even from a separate workstream." All gates re-run: Council A v2 GO, Council B v2 GO, AUDIT v2 PASS (STRICT). Net word count delta: 399 → 397.

## Downstream propagation notes (S2 OE writer + S3 rubric author)

1. **HARDNESS Plan §L25 reframe (housekeeping-only)**: annotate the Plan to reflect CROSS_SCENARIO_RECONCILE framing. The three ransomware-adjacent workstreams that feed the same borrower-notice obligation are:
   - **3/20 ransomware CRM stream** (5 notes): `crm_engagement_2b9c91c10337`, `beb5c30bfe7c`, `f1cb06ea7b65`, `191ea9b23c9b` + `730ac466da97` (3/27).
   - **4/07 UWM broker-portal exposure stream**: Amy's phishing / lender-portal exposure → affected files `LN-2026-00522`, `LN-2026-00008`, `LN-2026-00010`, `LN-2026-00009` (per Council A v2 grounding).
   - **4/14 Marcus Webb post-term-access stream** (7+ notes): `cf917a096b98`, `9e5988d2297c`, `b95df55fbf01`, `4adb7e84d521`, `985a3efbbee8`, `a33cc635ceed`, `1b81acccf98e` + affected files `LN-2025-00002`, `LN-2025-00007`, `LN-2025-00229`.

2. **F2 downstream pin (BLOCKING at S2)**: OE writer MUST pin the Slack channel target as `D_grace_robert_denise` (3-seat DM) per AUDIT's "reading the same room without pushing it wider" qualifier interpretation. Two-seat DMs (D_grace_robert, D_denise_robert) and C001 general channel are decoy candidates the prompt's language does not select for.

3. **Filesystem "incident folder" un-seeded** (from Council A NOTE-2 v1): filesystem has no seeded data. OE writer must specify a canonical path + content requirements atomically, or accept any reasonable folder path with content-requirement anchoring, to avoid the Learnings §L28 version-bump-vs-fresh-upload trap.

4. **Rubric authoring guardrail**: rubrics must grade cross-workstream reconcile BEHAVIOR (agent must surface at least one CRM engagement from each of the 3 streams — 3/20, 4/07, 4/14), NOT hard-pin any single CRM engagement ID as the ransomware-authoritative citation. Hard-pinning `crm_engagement_b95df55fbf01` as "the ransomware supersession" would be factually incorrect (that's a Marcus post-term engagement) and would inflate Bucket 1 rubric-invalid rate on verifier runs.

## Cross-task learnings surfaced (for `Tasks/_meta/`)

- **Hardness Plan factual-accuracy gap**: the HARDNESS phase can plausibly cite CRM engagement IDs as "supersession" evidence without verifying scenario-fit. The verification-hardness step should include a scenario-anchor check: for each supersession-lever citation, confirm the cited CRM engagement's `body` text uses language consistent with the anchoring scenario, not an adjacent scenario. Consider adding to `Tasks/_meta/Hardness_Patterns_Log.md`.
- **Bolt-on validator false-positive**: the NAMED_ENTITY_RE_PROMPT regex greedily captures multi-word capital sequences (e.g., "Walk Raj" captured as compound entity when "Walk" is sentence-start-capitalized), preventing single-token matching against the prior sentence's "Raj". Workaround: prefix with a discourse marker like "So" so the verb is lowercase. Consider filing a validator issue.
- **Validator universe-today mismatch**: `validate.py` reports universe today as `2026-06-12` (Brookfield fallback) instead of `2026-04-28` (KeyStone per `today_horizon.json`). Not blocking for this prompt but a note bug for the maintainer.
