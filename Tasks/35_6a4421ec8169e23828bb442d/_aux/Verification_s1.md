# Verification — S1 (Prompt phase)

## Sources consulted

- **Per-task data** :: `_aux/Universe_Split/*` (email, crm, slack, contacts, mortgage_los), `_aux/Fact_Ledger.json`, `_aux/Universe_Index/today_horizon.json`, `_aux/Hardness_Plan.md`.
- **Eval spec** :: `Evals_keystone/1_Prompt_Eval.md` (all 12 Prompt sub-dims 1.1–1.12).
- **QC spec** :: `Docs_keystone/7_QC_Spec_Doc1.json` (Prompt dimension — 12 sub-dims scored 5/5 via `_aux/Council_Reports/S1_B_adversarial.md`).
- **Reference docs** :: `Reference/Prompt_Format.md`, `Reference/Hardness_Playbook.md`, `Reference/Council_Protocol.md`, `Reference/Similarity_Pivot.md`, `Docs_keystone/4_Prompt_Hard_Tips.md`, `Docs_keystone/5_Prompt_Diversity_Business_Function.md`, `Docs_keystone/6_Prompt_Relative_Time_Updates.md`, `Prompt_Guidelines.md`, `QC_Tasks/V3.1_Tasks/Task1|Task3|Task4 5_Prompt.txt`.

## Data sources consulted

- `_aux/Universe_Split/email.emails.json` :: verified Raj's 3/20 escalation (`email_email_8851e5637a6c` 17:20 UTC and `email_email_7aa25e7b6472` 17:24 UTC), Denise's privileged trio (`email_email_985ac55f2911` 18:33, `email_email_fc27f9914e8b` 19:00, `email_email_ab781889cc1c` 19:20), and Robert-to-Sloane pay-vs-restore counsel request (`email_email_b2572b3105dc` 19:09). All ground the prompt's phrasing on Raj's restore-cost read, Denise's preliminary plan (scope-question triple: which files, whether accessed, whether SAR), and Robert's engagement with outside cyber counsel.
- `_aux/Universe_Split/crm.crm_engagements.json` :: verified two independent CRM streams. Ransomware stream (5 notes on 2026-03-20: `crm_engagement_2b9c91c10337`, `beb5c30bfe7c`, `f1cb06ea7b65`, `191ea9b23c9b`, plus `730ac466da97` 3/27). Post-term-access / Marcus Webb stream (7+ notes on 2026-04-14: `cf917a096b98`, `9e5988d2297c`, `b95df55fbf01`, `4adb7e84d521`, `985a3efbbee8` and others). The **actual ransomware supersession** is the **2026-04-07 CRM stream** (formal breach response opened, affected files identified as LN-2026-00008/00010/00009, borrower notice drafts queued pending scope confirmation) surfaced by both councils.
- `_aux/Universe_Split/slack.slack_messages.json` :: verified C001 hosts Robert's canonical exec exchange for the incident (ts 1774032333 "raj/grace I need the ugly version"); C002 hosts Grace's tactical Monday-closings pivot (ts 1774029240); C008 hosts Raj's IT-support origination (ts 1774026720 "anyone else unable to get into LOS"). Decoy-parent pattern L26 is live. D_grace_robert_denise 3-way DM exists but has 0 ransomware-topic messages seeded — the "leadership channel" resolution is judgment-based; the prompt qualifier "not wider than needed" biases toward the DM, but C001 remains a plausible read.
- `_aux/Universe_Split/contacts.contacts.json` + `_aux/Universe_Split/slack.slack_users.json` :: verified 5 Bennett-* email variants (including the near-miss `lbennett@bennettcyberlaw.com`) vs the correct cyber counsel `megan.sloane@wardbarrettlaw.com`. Verified Robert's Slack alias `r.calloway@keystonemortgage.com` differs from his email `robert.calloway@keystonemortgage.com`.
- `_aux/Fact_Ledger.json` :: no explicit dollar amounts / dates / IDs from the prompt appear as atoms requiring verification (atom verifier ran clean at 0 checks).
- `_aux/Hardness_Plan.md` :: 5 levers selected (L8 multi-link, L9 latching / authority, L10 structured-DB skip on CRM, L25 supersession, L26 decoy parent), density midpoint 52, service breadth 8. **Deviation logged**: the Plan cites the 4/14 CRM stream as the ransomware supersession anchor; both Council A and Council B (independently) identified this as the Marcus-Webb post-term stream. The **actual** ransomware supersession is the 4/07 stream. Prompt is scenario-agnostic ("wherever they live") so this does not invalidate the S1 deliverable; the S2 OE writer and S3 rubric author MUST anchor supersession evidence on the 4/07 stream (not 4/14) to avoid scenario conflation. Recorded here for downstream propagation via S1_A_grounding.md and S1_B_adversarial.md notes.

## Eval spec sub-dims (Evals_keystone/1_Prompt_Eval.md) verified

- 1.1 Unique Ground Truth :: PASS — single leading interpretation for both ask-branches (pay-vs-restore + borrower-notice reconciliation); no reasonable second reading flips a write action set.
- 1.2 Feasibility :: PASS — all required evidence materialized in Universe_Split; universe today 2026-04-28 accommodates all temporal claims.
- 1.3 Explicit Tool Mention :: PASS — natural surface references only ("email outside cyber counsel", "post a short status in the leadership channel", "our engagement log", "the incident folder"). Zero MCP-server names, zero tool-name leaks, zero internal IDs.
- 1.4 Prompt Clarity and Specificity :: PASS — asks are specific enough to execute without guessing; ambiguities (which channel, which folder) are lever-intentional (L26, L28) not clarity defects.
- 1.5 Contrived / Unnatural Prompts :: PASS — Owner's voice is measured, incident-anchored; no artificial precision, no format-constraint gimmicks, no timestamp-fishing.
- 1.6 Truthfulness :: PASS — every state-implying claim ("Raj's read that night was that the restore path is expensive", "encrypted local backups", "cloud copy three days behind", "environment rebuild plus validation", "Denise queued a preliminary plan", scope-question triple, "sanctions and privilege read") grounds cleanly to Universe_Split records.
- 1.7 Tool use and Cross-service requirement :: PASS — validator counted 2 distinct services from body keywords; actual trajectory spans 6+ services (email, slack, crm, filesystem, mortgage_los, contacts) per Hardness Plan service breadth.
- 1.8 Investigation :: PASS — investigation ("walk Raj's picture back", "find the freshest signals on the incident and reconcile them") + write actions (email, Slack post, CRM note, filesystem memo) both present.
- 1.9 Coherence :: PASS — every paragraph reinforces the same ransomware-disposition situation; no bolt-on sentences. Validator false-positive on "So walk Raj's picture back..." resolved by prefixing "So" so the regex doesn't grab "Walk Raj" as a compound entity.
- 1.10 Persona :: PASS — voice fits Robert Calloway (Owner / final decision-maker per PersonaBrief). "I would put a stake in the ground", "the bar", "counsel", "sign off" all match Owner register.
- 1.11 Business Function :: PASS — Executive assignment matches Owner-oversight decision on a live compliance-adjacent incident (per Docs_keystone/5_Prompt_Diversity_Business_Function.md — Executive 10%).
- 1.12 Alignment with Today's Date :: PASS — "this morning" / "five weeks" / "the March framing" all resolve against universe today 2026-04-28 with 3/20 incident onset.

## QC spec sub-dims (Docs_keystone/7_QC_Spec_Doc1.json — Prompt dimension) verified

All 12 Prompt sub-dims scored 5/5 by Council B (`_aux/Council_Reports/S1_B_adversarial.md`) per the 1/3/5 or 1/5 scheme map in Reference/Council_Protocol.md. No NON-FAIL band justifications invoked.

## Reference docs consulted

- Reference/Prompt_Format.md :: voice, anti-patterns, 500-word cap re-verified. 399 words, 3 movements, first-person Robert voice.
- Reference/Hardness_Playbook.md :: 5-lever selection re-checked against per-task universe; density midpoint ≥ 50 target confirmed.
- Reference/Council_Protocol.md :: both councils invoked; A + B verdicts collected before final.
- Reference/Similarity_Pivot.md :: N/A — max similarity composite 28.4, well under 40 pivot threshold.
- Docs_keystone/4_Prompt_Hard_Tips.md :: Opus 4.8 failure-mode patterns applied via Hardness Plan.
- Docs_keystone/6_Prompt_Relative_Time_Updates.md :: universe today = 2026-04-28 Tuesday; relative dates "this morning" and "March" both resolve cleanly.
- Docs_keystone/5_Prompt_Diversity_Business_Function.md :: KeyStone Executive business function 10% verified.
- Prompt_Guidelines.md :: anti-patterns (QC clichés, over-signaling, generic urgency, enumerated action lists) — none present.
- QC_Tasks/V3.1_Tasks/Task1 + Task3 + Task4 5_Prompt.txt :: reference voice confirmed (Task4 = Executive trust-attestation prompt is closest tonal analog).

## Verification statements

- [x] Validator (validate.py --phase prompt) exit 0 — PASS 0 fails, 0 warns, 5 notes.
- [x] Council A grounding + convention clean (zero ungrounded claims, zero convention drift). GO. 8 perspectives.
- [x] Council B QC scoring shows every applicable sub-dim = 5/5 (no NON-FAIL bands invoked). GO. 12 sub-dims. Density midpoint projected 55 (Hardness Plan projected 52).
- [x] Similarity gate (calc_similarity.py) composite < 40 — max 28.4 vs QC_Tasks/V3_Tasks/Task14 (well under threshold).
- [x] Universe atom verifier (verify_universe_atoms.py) — PASS 0 fails, 0 warns, 0 atoms checked.
- [x] AUDIT verdict = PASS (STRICT) — iteration 2 of 3, resolved F1 via a 1-sentence prompt addition; F2 carried as MINOR-downstream-fixable at S2 (OE writer pins `channel_id = D_grace_robert_denise`).

## Discrepancies surfaced

1. **Hardness Plan → Council A/B independent finding on 4/14 vs 4/07 CRM stream**: The Hardness Plan cites `crm_engagement_b95df55fbf01` (2026-04-14) as the ransomware supersession anchor for the L25 lever. Both councils independently identified this as the Marcus Webb post-term-access stream (scenario_7da8f37a). The **actual ransomware supersession** is the **2026-04-07 CRM stream** (formal breach response, affected files LN-2026-00008/00010/00009, borrower notice drafts queued). The S1 prompt is scenario-agnostic ("wherever they live", "the freshest signals on the incident") and remains solvable — an agent will discover both streams and correctly anchor supersession on 4/07. Recorded here for S2 OE writer and S3 rubric author to anchor evidence on 4/07 not 4/14. This is a soft PROPAGATE flag for downstream phases — no S1 deliverable change required.

2. **"Leadership channel" resolution**: Council A NOTE-1 flagged this as OE-writer guidance. The prompt's "not wider than needed" qualifier biases the resolution toward the D_grace_robert_denise 3-way DM rather than C001 (which is general/company-wide per Council A's re-read of Slack channel data). C001 remains a defensible second read. S2 OE writer should pin the intended target explicitly.

3. **Filesystem "incident folder" un-seeded**: Council A NOTE-2. Per Hardness Plan §L28 caution, filesystem has no seeded data. S2 OE writer must specify a canonical path + content requirements atomically, or accept any reasonable folder path with content-requirement anchoring, to avoid the L28 version-bump-vs-fresh-upload trap.

## Verdict

**PASS** — S1 prompt cleared validator (exit 0), Council A grounding + convention (GO, 8 perspectives), Council B QC scoring (GO, 12 sub-dims all 5/5), similarity gate (composite 28.4 < 40), universe atom verifier (clean), and strict veteran AUDIT (PASS STRICT, iteration 2 of 3). Three PROPAGATE flags carried forward to S2 (4/07 CRM stream anchor, D_grace_robert_denise channel pin, filesystem incident-folder path); none block S1 exit.
