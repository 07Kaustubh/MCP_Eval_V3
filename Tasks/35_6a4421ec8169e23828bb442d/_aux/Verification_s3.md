# Verification — S3 (Rubrics phase)

## Sources consulted

- **Per-task data** :: `_aux/Universe_Split/contacts.contacts.json` (Sloane at `contacts_contact_f5367b22340d` verified + 5 Bennett-* near-miss decoys), `_aux/Universe_Split/slack.slack_channels.json` (D_grace_robert_denise verified as 3-member mpim), `_aux/Universe_Split/slack.slack_users.json` (Robert/Grace/Denise/Raj personas), `_aux/Universe_Split/slack.slack_messages.json` (Raj C001 ts 1774447787 verified verbatim: "i can't promise los integrity till tested"), `_aux/Universe_Split/email.emails.json` (6 canonical emails: `_8851e5637a6c`, `_7aa25e7b6472`, `_985ac55f2911`, `_fc27f9914e8b`, `_ab781889cc1c`, `_b2572b3105dc` — all verbatim quotes verified), `_aux/Universe_Split/crm.crm_engagements.json` (22 CRM engagement IDs across 3/20 initial + 4/07 portal + 4/07 Raj audit + 4/14 Marcus Webb workstreams), `_aux/Universe_Split/mortgage_los.loans.json` (all 7 loan IDs LN-2026-00522, LN-2026-00008, LN-2026-00010, LN-2026-00009, LN-2025-00002, LN-2025-00007, LN-2025-00229 exist), `_aux/Fact_Ledger.json` (source-hash pinned).
- **Eval spec** :: `Evals_keystone/3_Rubrics_Eval.md` (Rubric Quality Evaluator — every phase 1-4 check applied).
- **QC spec** :: `Docs_keystone/7_QC_Spec_Doc1.json` (Rubric dimension — 5 sub-dims scored 5/5 by Council B + AUDIT strict re-verification).
- **Reference docs** :: `Reference/Rubric_Format.md` (flat schema + verb cheat sheet + phrasing patterns re-checked), `Reference/Strict_Convention_Inventory.json` (allowed phrasings + evidence-field shapes), `Reference/Council_Protocol.md`, `Reference/Sessions/AUDIT.md` (7 active lenses; LENS 6 + LENS 9 retired).
- **Framework docs** :: `Docs_keystone/2_Rubrics_V3_Guidelines.md` (V3 rubric spec — outcome-first workflow, three-condition test for process, atomic-per-item for multi-write actions, agent-centric phrasing, flexibility patterns, Common Mistakes 1-12), `Docs_keystone/12_Always_Failing_Rubrics.md` (AF patterns re-checked; zero AF risks in the deliverable), `Docs_keystone/8_QC_Spec_Doc2.md` (severity taxonomy Major/Moderate/Minor/Non-Failing).
- **Tool catalog** :: `Mortgage_Base_Universe/6_Server_Tools_Details.json` (KeyStone tool catalog — no tool names in rubric titles, verified).
- **Upstream cross-check** :: `_aux/Verification_s2.md` (6 PROPAGATE flags honored — 3-workstream borrower-notice reconciliation, D_grace_robert_denise channel pin, filesystem incident-folder path, at-risk-closings SOFT-OUTCOME, Sloane no-reply truthful gap, Bennett-cyber L4 trap).
- **Reference tasks** :: `QC_Tasks/V3.1_Tasks/Task4_6a30fe7ec1d692ab3ccad616/7_Rubrics.json` (voice/structure reference — method-agnostic "notifies" pattern), `QC_Tasks/V3.1_Tasks/Task1_6a26c29d5f5b7cf1ea90c0cc/7_Rubrics.json` (mixed 1.1/1.2/2.1 breakdown for content-rich briefs), `QC_Tasks/V3.1_Tasks/Task2_6a27b70a80b7729ca5d6d88d/7_Rubrics.json` (email-explicit prompt handling).

## Eval spec sub-dims (Evals_keystone/3_Rubrics_Eval.md) verified

- Overall Rubric Quality :: PASS — 0 Major, 0 Moderate, 0 Minor issues on the final deliverable (validator report notes: 0 fails, 0 warns).
- Rubric Category Balance :: PASS — 35 outcome, 0 process. Outcome > Process (V3 default).
- Process Rubrics :: PASS (N/A) — zero process rubrics. Three-condition test re-applied by AUDIT LENS 1: no missed process case where an outcome cannot capture.
- Agent-Centric Phrasing :: PASS — every title starts with "The Agent" or "The Agent's". No tool names in titles. No em-dashes anywhere. No "at least N" phrasing.

## QC spec sub-dims (Docs_keystone/7_QC_Spec_Doc1.json — Rubric dimension) verified

- Overall Rubric Quality :: PASS (Council B: 5/5; AUDIT strict: 5/5).
- Rubric Category Balance :: PASS (Council B: 5/5; AUDIT strict: 5/5).
- Process Rubrics :: PASS (Council B: 5/5 N/A; AUDIT strict: 5/5).
- Agent-Centric Phrasing :: PASS (Council B: 5/5; AUDIT strict: 5/5).
- All-Failing Rubrics :: PASS (Council B: 5/5; AUDIT strict: 5/5).

## Verification statements

- [x] Validator (validate.py --phase rubrics) exit 0 — final run: 0 fails, 0 warns, 5 notes; Overall Rubric Quality 0% Major / 0% Moderate+ / 0% any-issue.
- [x] Every concrete literal in every rubric title and evidence field verified against `_aux/Universe_Split/*` by Council A (35/35 rubrics grounded; verdict GO).
- [x] Every rubric title starts with `The Agent` or `The Agent's` per V3 agent-centric phrasing rule.
- [x] Zero tool names in rubric titles. Tool names appear only in evidence/justification where they cite specific artifacts.
- [x] Flat schema {title, category, justification, evidence} used for all 35 rubrics (no legacy nested shape, no `id`, no `annotations` wrapper).
- [x] Outcome > Process (35 vs 0). Process three-condition test re-applied by AUDIT LENS 1; zero missed process cases.
- [x] Every OE with a write action or a tell-me signal has ≥1 covering rubric (Council B B9 forward map complete; AUDIT LENS 3 confirms).
- [x] Every prompt "reports/identifies/lists" ask has a 2.1 rubric covering it.
- [x] All 5 Hardness levers (§L8 multi-service chain, §L9 authority dismissal / soft-verb, §L10 structured-DB skip on CRM engagements, §L25 existing-output anchor / supersession, §L26 decoy parent thread) trace end-to-end through prompt sentence → OE step → rubric criterion → Fact_Ledger atom (AUDIT LENS 3 verified).
- [x] Density projection: Council B B3 midpoint 52 ≥ 50 target; AUDIT LENS 4 strictest-read midpoint 52; matches Hardness_Plan projection.
- [x] Council A returned GO (35/35 grounded; only 2 non-blocking sanity flags on address forms and mpim ambiguity, both correctly resolved in the deliverable).
- [x] Council B returned GO (5/5 all QC dims; B1-B9 checks clean; no adversarial hits).
- [x] AUDIT verdict = PASS (STRICT) — all 7 active lenses cleared under strictest interpretation; regression anchor suite 48/48 PASS.
- [x] 6 PROPAGATE flags from Verification_s2.md all honored: (1) 3-workstream borrower-notice reconciliation via rubrics R8/R9/R10/R11/R14/R15/R16/R17/R18/R19/R22/R23/R31/R33/R34 covering portal breach + Raj audit + Marcus Webb; (2) D_grace_robert_denise channel pin via R1 (write action) + R12/R13/R14/R15 (content); (3) filesystem incident-folder path via R3 (semantic incident-folder path, not exact string); (4) at-risk-closings SOFT-OUTCOME honored (no rubric enforces at-risk-closings reads); (5) Sloane no-reply truthful gap honored (no rubric requires finding a Sloane reply; R30 requires reporting the gap); (6) Bennett-cyber L4 trap honored (R0 pins Sloane at wardbarrettlaw.com; R26 identifies Sloane in final response).

## Discrepancies surfaced

1. **Robert Calloway address form** — Slack profile carries `r.calloway@keystonemortgage.com` while the email-system sender is `robert.calloway@keystonemortgage.com`. Rubric R0 uses the email-system form for the send_email action, which is correct. No fix needed; Council A flagged as non-blocking. Downstream FINAL / trajectory eval will confirm the agent used the correct form per surface.

2. **Council B soft observation (7 rubrics bundle content within a single write action)** — R4/R12/R13/R14/R16/R20/R25 bundle multiple content elements per V3 Required-Elements pattern within a single artifact. AUDIT LENS 1 re-scored these under strictest read and confirmed the bundling is per-artifact (same write action, tightly coupled facts) — acceptable per V3 atomicity rules. No fix needed.

3. **AUDIT LENS 7 note-level tweaks applied post-audit** — R14 title and R32 title originally used `approximately seven` for the count of specific borrower files. Per Rubric_Format.md the `approximately` qualifier is banned on discrete counts (7 = exact 4+3). Applied two one-word edits to remove `approximately` from both title and evidence on R14 and R32. Validator re-run confirms clean PASS. AUDIT counter-lock (R8/R10/R18/R23 enforce exact 7-file enumeration) preserved.

## Verdict

**PASS** — S3 Rubrics cleared validator (exit 0, 0 warns), Council A grounding (GO, 35/35 grounded), Council B adversarial (GO, QC 5/5 all 5 sub-dims, density midpoint 52, 5/5 hardness levers preserved), and strict veteran AUDIT (PASS STRICT, all 7 active lenses passed, regression anchors 48/48). Two AUDIT NOTE-level tweaks applied inline (R14 + R32 discrete-count `approximately` removal). Deliverable is ready for PIPELINE FINAL.
