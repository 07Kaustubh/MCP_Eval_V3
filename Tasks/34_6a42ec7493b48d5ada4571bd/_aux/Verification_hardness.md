# Verification — HARDNESS

## Sources consulted

### Per-task data
- `_aux/Universe_Split/email.emails.json` (494 records) :: confirmed Marcus Thorne Apr 17 L9 email `email_email_99e10a978b48`; Pam Kowalski Apr 24 escalation `email_email_7168baed8438`; Craig Nguyen Apr 11 damage email with verbatim open question; Catalina Apr 14 commitment to Pam; Mosaic incident report Apr 16 with vendor liability cap + CM-2026-0415 reference
- `_aux/Universe_Split/slack.slack_messages.json` (354 records) :: confirmed 6 Slack hits anchoring $1,200 in KeyMove/Emilia context; verified Heartland Q1 leak (`c9a8c0f9deeef12b48f0c0a059f10e75` etc.) ruled out original anchor; confirmed C006 #operations is Blessing's home channel
- `_aux/Universe_Split/linear.linear_issues.json` (69 records) :: confirmed `linear_issue_c8cdba4408f1` "NorthWind retention response plan after April escalations"; confirmed `issue_heartland_q1_recon` description leaks "$4,800 overbilling" and "5 of 8 moves legitimate" (Heartland anchor killed); confirmed `issue_dot_docs_tanaka_mosaic` description leaks "placarding certificate — missing" (Tanaka anchor demoted to backup)
- `_aux/Universe_Split/airtable.records.json` (167 records) :: confirmed `recEmiliaCruzChicagoDenver` exists in `tblRelocations01` with Blessing Okafor as Assigned Coordinator, Status="In Progress" (stale — move was Apr 14-18), Special Requirements field populated with Steinway Model B detail
- `_aux/Universe_Split/airtable.tables.json` :: confirmed `tblRelocations01` schema has 9 fields including `Special Requirements` (multilineText) — the L25 write surface
- `_aux/Universe_Split/quickbooks.bills.json` (17 records) :: confirmed `BILL-KEYMOVE-2026-0417` (DocNumber=KM-44192-ICR, TotalAmt=$1,200, TxnDate=2026-04-17, line description verbatim: "Insurance claim rider for Emilia Cruz Steinway piano scratch during stairwell extraction") AND `bill_mosaic_damage_accrual_001` (TotalAmt=$90,000, line description verbatim references $50K vendor cap + $40K MoveOps exposure + CM-2026-0415 + INV-2026-0411)
- `_aux/Fact_Ledger.json` :: atom counts confirm $1,200, $4,800, $8,000, $50K, $90K, $60K all present in universe; Blessing Okafor in persona dict
- `_aux/Universe_Index/graph_report.md` :: confirmed Blessing density (19 mentions); channel densities (C002=94, C006=91 — operations is Blessing's home but #2 by raw count, behind water-cooler)
- `_aux/Universe_Index/service_inventory.md` :: confirmed 9 active services support the 5-service write target
- `PersonaBrief.txt` :: confirmed Blessing's admitted walkup-assessment miscalc as the operational anchor; confirmed her active threads include the Emilia Cruz NorthWind piano damage scenario

### Eval spec
- Implicit alignment with Phase 1.3 Coherence (anti-pattern: Command List / Bolt-on / Pre-Solving) :: HARDNESS plan reserves prompt-design choices for S1 but flags the L29 escape-valve risk in Marcus's email body that the prompt writer must NOT echo
- Trajectory dim Tool Call Count (floor ≥ 15; pipeline targets 50+ midpoint per AGENTS.md hard rule #11) :: projected midpoint 47 lands in THIN_DENSITY band (40-49), per-task justification documented in `## THIN density acceptance` subsection of Hardness_Plan.md

### QC spec
- Trajectory T1 Tool Call Count :: projected midpoint 47 (THIN), upper bound 58 (PASS) — operator accepted continuation with explicit Lever 8 traversal weighting note
- Trajectory T2 Service Breadth :: PASS with 7 services ≥ 5%, dominant service (email) at 27% well under 60% cap, distinct service count 8 (incl. reminders)
- Rubrics Anti-Pattern guards (no tool names in prompts; no Linear/Airtable/QB IDs in prompt) :: flagged for S1 enforcement in the Hardness Brief

## Verification statements
- [x] At least 3 levers selected; 5 chosen (Lever 1, 2, 7, 8, 11). Each cites a Learnings.md entry (L8/L9/L10/L11/L13/L14/L25).
- [x] Density midpoint projection 47 → falls in THIN band (40-49); operator continuation justified per `## THIN density acceptance` subsection.
- [x] Service breadth table populated (8 services, 7 ≥ 5%); PASS gate.
- [x] Heartland Q1 anchor rejected after verbatim leak verification (Linear issue + 5 Slack messages + Chloe email + Marcus email all stated "$4,800 overbilling" / "$8,000 verified"). Demoted to L1 confirm-already-done.
- [x] Tanaka DOT cert anchor demoted to backup after partial leak verification (Linear issue desc + Slack message state "cert missing"); only viable if L9 authority dismissal can override.
- [x] Marcus Webb Honda Civic anchor rejected (Blessing's Apr 23 admission email + Julian's owned service recovery pre-attribute the disposition).
- [x] Anchor A (Emilia Cruz piano damage) selected with full leak audit: zero verbatim "Emilia Cruz $X reimbursement" hits across email/Slack/Linear/Airtable/QB; the $1,200 vendor rider is NOT the customer-side answer.
- [x] L9 authority dismissal quote verified verbatim (Marcus Thorne Apr 17 email body).
- [x] L29 escape-valve risk surfaced in Marcus's email and mitigation prescribed in Hardness Brief (prompt must NOT echo Marcus's customer-side question + Lever 2 second-layer mitigation).
- [x] L15 implicit-prompt rule explicitly stated in Hardness Brief (no hint that the persona's $1,200 is wrong; no Pam-escalation / Friday-package mention).
- [x] L30 rubric-binding cascade flag forwarded to S3 (recipient names must match: Craig Nguyen + Catalina + David Chen; channel must be #operations C006; bill must be BILL-KEYMOVE-2026-0417; rec must be recEmiliaCruzChicagoDenver — but NONE of these IDs may appear in the prompt itself, only in OE evidence + rubric internals).

## Discrepancies surfaced
- **Two failed Oracle anchors before settling on Anchor A.** First Oracle pass picked Heartland Q1 ($12,800 → $8,000 derivation) which was fully leaked. Second Oracle pass (this one) picked Emilia Cruz after orchestrator surfaced the leak findings and ranked alternatives. The pipeline's `verify_universe_atoms.py` (run at MATERIALIZE) would not have caught the first anchor's leak — leak hygiene is a HARDNESS-phase responsibility that the runbook does not yet automate. Recommendation: forward to project to add `Hardness_Plan.md`-level leak check helper.
- **THIN_DENSITY (midpoint 47) accepted with documented justification.** Per AGENTS.md hard rule #11 the 50+ midpoint design target produces ~40+ tool calls in real platform runs. Midpoint 47 is below the design target. Operator continuation per the per-task justification documented in `## THIN density acceptance` subsection — Lever 8 upper-bound weighting (9 instead of 7) pushes midpoint to 51, and the breadth gate clears 8 services. Flag forwarded to S1 prompt writer to maximize Lever 8 traversal density (the multi-link chain Craig→Marcus→Pam→Linear→Catalina).
- **L29 escape-valve risk inside the universe (not the prompt).** Marcus Thorne's Apr 17 email body itself contains the customer-side flag ("paying the vendor rider before the customer even has a callback... not going to look great internally"). The prompt writer must NOT echo this clause AND the rubric writer must NOT phrase the customer-side rubric in a way that an agent who picked up the Marcus-flag echo passes trivially. The second-layer mitigation is Lever 2 (Mosaic precedent query) — an agent must STILL query `bill_mosaic_damage_accrual_001` to recognize the credit-memo + vendor-cap model even if they pick up Marcus's customer-side hint.
- **Marcus's email is addressed to David Chen, not Blessing.** Blessing's natural discovery path is QB bill → vendor name search → finds both Craig's Apr 11 and Marcus's Apr 17 emails. The prompt should anchor on QB-driven discovery, not "Marcus told me" — that preserves the L9 mechanism (agent finds Marcus's email mid-investigation and defers to its frame) without making Marcus the prompt's voice.

## Verdict
PASS — Hardness Plan complete with 5 selected levers, density midpoint 47 in THIN band with documented per-task continuation justification, service breadth gate PASS with 8 services, answer-leak audit clean. Anchor A (NorthWind / Emilia Cruz piano damage operational docket) holds. Two failed anchor candidates (Heartland Q1 fully leaked; Tanaka DOT partially leaked) ruled out and documented. STOP gate hit — wait for user to invoke `PIPELINE S1 — Tasks/34_6a42ec7493b48d5ada4571bd` in fresh chat.
