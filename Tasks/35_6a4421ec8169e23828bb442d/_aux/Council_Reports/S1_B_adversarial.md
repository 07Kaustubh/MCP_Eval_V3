# Council B — Adversarial QC + Density + Hardness Preservation
Task: `Tasks/35_6a4421ec8169e23828bb442d`
Phase: S1 prompt
Deliverable: `5_Prompt.txt`
Universe: keystone (single-entity, today 2026-04-28 America/New_York)
Anchoring scenario: `scenario_14b3ffde` (ransomware pay-vs-restore)

Applied through five role lenses (Architect, Implementer, Red-team, Ground-truth, Integration). Verdict is the union.

## Atom verification pre-work (Ground-truth lens floor)

Spot-queried `_aux/Universe_Split/*` before scoring:

- `email_email_b2572b3105dc` (2026-03-20 19:09) — Robert → Megan Sloane, subject "Need counsel on ransom payment vs restore path tonight". Body matches Raj framing referenced in prompt. **VERIFIED**.
- `email_email_985ac55f2911` (2026-03-20 18:33) — Denise → Megan, "Privileged: ransomware incident counsel needed today". **VERIFIED**.
- `email_email_fc27f9914e8b` (2026-03-20 19:00) — Denise → Robert, "Privileged: reporting obligations and borrower notice trigger". **VERIFIED**.
- `email_email_ab781889cc1c` (2026-03-20 19:20) — Denise → Megan + Robert, "Privileged: borrower notice drafts should be queued tonight". **VERIFIED**.
- `email_email_8851e5637a6c` (2026-03-20 17:20) — Raj → Grace/Robert, "Immediate escalation: ransomware impacting LOS and backups". **VERIFIED**.
- `crm_engagement_f1cb06ea7b65` (2026-03-20 16:17) — "Leadership weighing pay vs restore". Body "2 BTC demand. Local backups unusable, cloud copy ~72 hrs old". **VERIFIED**.
- `crm_engagement_b95df55fbf01` (2026-04-14 09:47) — "Owner escalation sent". Body "Escalated to Robert. 3 borrower files in **post-term access review**; borrower notice may be needed." **VERIFIED** with caveat below.
- Contact `megan.sloane@wardbarrettlaw.com` — Partner, Cyber Counsel, Ward Barrett LLP. **VERIFIED**.
- Contact `lbennett@bennettcyberlaw.com` — Laura Bennett, "Cyber Counsel" at Bennett Cyber Law. **VERIFIED live near-miss trap**.
- Slack C001=general (30 members, exec-visible), C002=loan-processing (334 msgs), C008=it-support (24 msgs), `D_grace_robert_denise` DM present. **VERIFIED**.

**Caveat surfaced by ground-truth lens**: the 4/14 CRM body uses the phrase "**post-term access** review". "Post-term access" is the canonical linguistic marker of the Marcus Webb departed-employee scenario (`scenario_7da8f37a`), not ransomware terminology. This is a scenario-crossover surface — the same borrower-file exposure workstream is being touched from two root-cause branches. See B6 for how the prompt's framing handles it.

---

## [B1] QC sub-dim scoring — all 12 Prompt sub-dims

SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5 scheme) -> two decisions (pay-vs-restore, borrower-notice posture) + 4 named write actions (memo, email cyber counsel, Slack status, engagement log note); write-action set is invariant across reasonable readings (see B2)
SUB-DIM Feasibility -> SCORE 5/5 (1/3/5 scheme) -> every referenced atom materialized (Raj/Denise/Sloane email chain, CRM engagements 3/20 + 4/14, C001 exec-general, D_grace_robert_denise DM, incident folder per PersonaBrief)
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> zero tool names in prompt body; "email", "leadership channel", "engagement log", "incident folder" are natural surface descriptions
SUB-DIM Prompt Clarity and Specificity -> SCORE 5/5 (1/3/5 scheme) -> Robert's voice specifies the two decisions, the four writes, and the reconciliation direction ("do not take the March framing at face value") explicitly
SUB-DIM Contrived / Unnatural Prompts -> SCORE 5/5 (1/3/5 scheme) -> reads as a natural exec voice-note ("five weeks of this hanging over the shop", "put a stake in the ground", "not going to have counsel or the bar find out I sat on it"); no framework-artifact phrasing
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5 scheme) -> "five weeks of this hanging over the shop" grounds cleanly to universe today 2026-04-28 vs incident 2026-03-20 (39 days); "Denise pinged me again this morning" implicitly anchors to today
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5 scheme) -> every factual claim ties to a verified universe atom; Raj's authority framing quoted per §L24 soft-verb convention ("Raj's read was that the restore path is expensive"), matching `email_email_8851e5637a6c` + `email_email_b2572b3105dc`
SUB-DIM Tool Use & Cross-service -> SCORE 5/5 (1/5 binary) -> spans email + slack + crm + filesystem + mortgage_los + contacts (six distinct services); breadth projection carries 8 services per Hardness Plan
SUB-DIM Investigation + Action -> SCORE 5/5 (1/5 binary) -> investigation ("walk Raj's picture back", "reconcile them, wherever they live") + explicit write actions (decision brief upload, email cyber counsel, Slack status, engagement log note)
SUB-DIM Coherence (Bolt-on) -> SCORE 5/5 (1/5 binary) -> every paragraph shares entities (Denise, Raj, Megan, borrower notice, incident record); no orphan sentence or subject drift
SUB-DIM Persona -> SCORE 5/5 (1/3/5 scheme) -> Owner/Broker Robert Calloway is the canonical decision authority for pay-vs-restore per PersonaBrief ("final decision-maker on every escalation"); voice matches (blunt, deadline-driven, accountability-conscious)
SUB-DIM Business Function -> SCORE 5/5 (3/5 scheme) -> Executive maps cleanly (KeyStone Executive 10% band per `Mortgage_Base_Universe/5_Task_Categories_Business_Functions.md`); strategic pay-vs-restore + borrower-notice decision is a canonical exec-tier task

**B1 summary**: 12/12 sub-dims at 5. No NON-FAIL bands invoked.

---

## [B2] Adversarial alt-path

Second-reading attacks attempted from Red-team lens:

**(a) Route counsel email to a Bennett-* variant instead of Megan Sloane.**
The near-miss trap is real — `lbennett@bennettcyberlaw.com` is a live contact with `job = "Cyber Counsel"` at Bennett Cyber Law. An agent that (i) shortcuts contact resolution by title-search ("cyber counsel") rather than reading Denise's 3/20 privileged email chain, and (ii) ignores the prompt's cue "confirm nothing has shifted on the legal side since **we asked** outside cyber counsel for the sanctions and privilege read" — could land on Bennett. **However**, the prompt anaphoric reference to counsel-already-engaged forces the agent to identify the counsel from prior correspondence, which grounds to Sloane. A competent agent following the prompt as written correctly resolves Sloane. **Write action set unchanged** (still one email to cyber counsel); recipient can drift. Contained: MODERATE risk on recipient field, not a write-action flip.

**(b) Post the Slack status to C002 (loan-processing) or C008 (it-support) instead of C001 or D_grace_robert_denise.**
Prompt says "leadership channel" — semantic pull toward C001 (general/exec-visible) or D_grace_robert_denise (the 3-way DM that has been the actual working channel per the ambient facts). A keyword-anchored agent latching on "Monday closings are at risk" (elsewhere in the incident's Slack chatter, not in this prompt) could post to C002; anchoring on "ransomware" could post to C008. Neither is genuinely a "leadership channel" — C002 is tactical processing, C008 is IT-tier. **Write action set unchanged** (still one Slack post); channel can drift. Contained: MODERATE risk on channel_id field. This is the L26 decoy-parent lever behaving exactly as designed.

**(c) Treat Raj's restore-cost framing as a foregone conclusion.**
Prompt says explicitly "**If restore is still a lift, I want the specific gaps and rebuild items as tradeoffs, not a foregone conclusion.**" The counter-frame is present in the prompt's own text. An agent that skips or misweights this clause could still latch. However, this is a reading-comprehension failure by the agent, not a prompt-side ambiguity. The prompt's language does NOT permit a second reading that materially favors payment without enumerating tradeoffs. Contained.

**(d) Latch on Denise's 3/20 preliminary plan without reconciling against fresher signals.**
Prompt says explicitly "**Do not take the March framing at face value. Find the freshest signals on the incident and reconcile them, wherever they live.**" L25 supersession is cleanly cued. An agent that ignores the "wherever they live" cue and confines its search to Denise's email thread could latch — but again this is an agent reading-comprehension failure, not a second reading the prompt itself allows. Contained.

**B2 summary**: No second reading flips the write-action SET. Recipient drift on (a) and channel drift on (b) are the intended lever-triggers (L4 near-miss, L26 decoy parent). Adversarial divergence is contained.

---

## [B3] Tool-call density projection

Projected trajectory for a competent Opus 4.8 agent (Implementer lens):

| Component | Reads/Calls |
|---|---:|
| Persona resolution + universe today lookup | 2 |
| Raj IT-escalation email chain pull (search + read) | 4 |
| Denise 3/20 privileged email chain pull | 4 |
| Robert's own 3/20 email to Sloane pull (already-engaged evidence) | 2 |
| Contact resolution: Megan Sloane vs Bennett-* variants | 3 |
| Slack ransomware chatter: C001 + C008 + D_grace_robert_denise | 6 |
| Slack channel resolution for the "leadership channel" write | 2 |
| CRM engagement pulls (3/20 `f1cb06ea7b65` + 4/14 `b95df55fbf01`) | 4 |
| Borrower-file cross-reference (mortgage_los.loans / conditions / document_checklist) | 5 |
| Ambient at-risk-closing loan status pull (LN-2026-00601 family) | 4 |
| §L9 latching validation (re-read Raj framing for tradeoff enumeration) | 3 |
| §L25 supersession comparison (3/20 preliminary vs 4/14 escalation reconciliation) | 3 |
| Write action 1: email to Megan Sloane at wardbarrettlaw.com + 3 supporting reads | 4 |
| Write action 2: Slack post to canonical leadership channel + 2 supporting reads | 3 |
| Write action 3: CRM engagement note append + 2 supporting reads | 3 |
| Write action 4: filesystem privileged decision memo upload + 2 supporting reads | 3 |

**Midpoint: ~55.** Range across pessimistic/optimistic corners: **44-68**.

Matches Hardness Plan projected midpoint 52 (range 41-63); the S1 prompt as written stays inside the projected envelope with slight upside from the borrower-file cross-reference layer that is explicit in the prompt's "any specific files anyone has identified since" ask.

**Band: PASS** (design target ≥ 50 met; low-end ≥ 40).

Service breadth (Implementer lens): email, slack, crm, mortgage_los, contacts, filesystem, quickbooks (ambient bill check on Ward Barrett retainer), stripe (ambient charge check) — 8 distinct services, dominant service email ~23%. PASS.

---

## [B4] Hardness preservation

Read the prompt against each selected lever from `_aux/Hardness_Plan.md`:

**§L8 (Multi-link chain, Playbook L8) → PRESERVED.**
Prompt quote: "find the freshest signals on the incident and reconcile them, **wherever they live**". This phrase mechanically pushes the agent across email + Slack + CRM. Additionally "walk Raj's picture back to what the emails and records actually say" enforces the multi-service reduction. Architect + Integration lenses concur.

**§L9 (Latching / authority dismissal, Playbook L1) → PRESERVED.**
Prompt quote: "Raj's read that night was that the restore path is expensive... So walk Raj's picture back... If restore is still a lift, I want the specific gaps and rebuild items as tradeoffs, **not a foregone conclusion**." The counter-frame is explicit and prompt-visible. §L24 soft-verb convention honored ("Raj's read was that... is expensive" — not "restore is impossible"). Red-team lens concurs the latching risk remains agent-side, not prompt-side.

**§L10 (Structured-DB skip on CRM, Playbook L2) → PRESERVED but soft.**
Prompt quote: "wherever they live" + "Anything queued or in draft I have not been looped on". "Wherever they live" invites structured surfaces; "queued or in draft" specifically implies non-email surfaces (CRM engagement notes, ticketing, etc.). The prompt doesn't literally name CRM — it doesn't have to, that would leak the lever. An agent that stops at Slack + email misses the CRM 3/20 and 4/14 engagements. Lever intact.

**§L25 (Reversal / supersession, Playbook L10) → PRESERVED.**
Prompt quote: "Denise queued a preliminary plan the night this started... What I need now is a plain read of where that plan stands. Has scope narrowed. Are there specific files anyone has identified since... **Do not take the March framing at face value.**" Directly invites reconciliation of Denise's 3/20 plan against fresher signals. Existing-output anchor plus explicit override cue. Integration lens concurs — this is the strongest surface lever in the prompt.

**§L26 (Decoy parent thread, Playbook L4) → PRESERVED.**
Prompt quote: "Post a short status in **the leadership channel** so we are all reading the same room without pushing it wider than needed." Deliberately soft on channel identity — leaves the agent to distinguish C001 (canonical exec-general) or D_grace_robert_denise (the actual 3-way exec DM) from C002 (loan-processing where "Monday closings" chatter lives) or C008 (it-support where the initial "anyone else unable to get into LOS" chatter lives). Miss-route surface is live.

**All 5 selected levers preserved. No HARDNESS_REGRESSION.**

---

## [B6] Upstream propagation

One concern to surface but NOT to propagate:

**Scenario-crossover on the 4/14 CRM engagement.** The Hardness Plan's L25 supersession selection uses `crm_engagement_b95df55fbf01` (2026-04-14 "3 borrower files in **post-term access review**") as the fresher signal that supersedes Denise's 3/20 preliminary ransomware plan. The 4/14 engagement's "post-term access" phrasing is the linguistic marker of scenario_7da8f37a (Marcus Webb departure), not ransomware terminology. This is a real cross-scenario surface, and the operator context already acknowledges it explicitly.

**Does the S1 prompt handle it cleanly?** Yes. The prompt's language is:
- "the incident" → ransomware (unambiguous anchor)
- "borrower notice" → scenario-agnostic (any exposure vector against the same borrower file set)
- "Find the freshest signals **on the incident** and reconcile them, wherever they live" → scoped to ransomware
- "Are there specific files anyone has identified since. Anything queued or in draft I have not been looped on" → scoped to the borrower-notice workstream, not to ransomware-only

Under this reading, the agent is asked to reconcile the borrower-notice workstream (any exposure vector) into the ransomware decision brief. Pulling both the 3/20 ransomware CRM engagement AND the 4/14 post-term-access CRM engagement is defensible business logic — whatever notice Keystone sends has to be comprehensive across all exposure vectors touching the same file set. The prompt does NOT hard-pin the 4/14 engagement as authoritative for the ransomware disposition.

**PROPAGATE TO S1: none.** The prompt as written is clean.

**Note for downstream S2/S3 writers** (not a B6 propagation, a guardrail): the OE and rubrics must test the RECONCILIATION BEHAVIOR (agent surfaced fresher signals about borrower-file exposure and folded them into the brief) rather than pin the 4/14 engagement as the mandatory ransomware citation. If the S2 writer bakes `crm_engagement_b95df55fbf01` into a hard OE step as "the current ransomware borrower-notice posture", THAT would embed the scenario conflation. The S1 prompt itself does not.

**No PROPAGATE flags raised.**

---

## Verdict

- Every applicable QC sub-dim: **12/12 at 5**.
- No adversarial alt-path flips a write action; recipient/channel drift risks are the intended lever surfaces.
- Projected tool-call density midpoint **~55** (range 44-68); Hardness Plan midpoint 52 corroborated.
- Every hardness lever preserved (L8, L9, L10, L25, L26).
- No PROPAGATE TO upstream flags.
- One downstream guardrail note passed to S2/S3 (do not hard-pin the 4/14 CRM engagement as the mandatory ransomware citation).

**GO.**

---

```json
{
  "phase": "prompt",
  "council": "B",
  "task_dir": "Tasks/35_6a4421ec8169e23828bb442d",
  "verdict": "GO",
  "perspectives": {
    "B1": {
      "status": "PASS",
      "findings": []
    },
    "B2": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "prompt:para3 (counsel email routing)",
          "issue": "lbennett@bennettcyberlaw.com is a live near-miss for Megan Sloane at wardbarrettlaw.com; write-action SET unchanged, recipient can drift",
          "fix": "no fix — intended L4 near-miss lever behavior; recipient resolution belongs in agent trajectory",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "prompt:para4 (Slack status)",
          "issue": "'the leadership channel' is deliberately soft; C001 vs D_grace_robert_denise vs C002/C008 decoy live",
          "fix": "no fix — intended L26 decoy-parent lever behavior",
          "propagate_to": null
        }
      ]
    },
    "B3": {
      "status": "PASS",
      "findings": []
    },
    "B4": {
      "status": "PASS",
      "findings": []
    },
    "B6": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "downstream S2/S3 guardrail (not a S1 issue)",
          "issue": "crm_engagement_b95df55fbf01 uses 'post-term access' phrasing (Marcus-scenario marker); OE/rubric must test reconciliation behavior, not hard-pin this engagement as the ransomware borrower-notice citation",
          "fix": "S2 writer: frame the OE around 'agent surfaces fresher borrower-notice signals and folds them into the brief'; do not require citing crm_engagement_b95df55fbf01 by ID as the ransomware-authoritative row",
          "propagate_to": null
        }
      ]
    }
  },
  "scores": {
    "unique_ground_truth": {"score": 5, "scheme": "1/3/5", "reason": "two decisions + 4 named writes; write-action set invariant across reasonable readings"},
    "feasibility": {"score": 5, "scheme": "1/3/5", "reason": "every referenced atom materialized in per-task universe"},
    "explicit_tool_mention": {"score": 5, "scheme": "1/5", "reason": "zero tool names in prompt body"},
    "prompt_clarity_and_specificity": {"score": 5, "scheme": "1/3/5", "reason": "two decisions, four writes, reconciliation direction all explicit"},
    "contrived_unnatural_prompts": {"score": 5, "scheme": "1/3/5", "reason": "natural exec voice-note; no framework-artifact phrasing"},
    "alignment_with_todays_date": {"score": 5, "scheme": "1/3/5", "reason": "'five weeks' matches universe today 2026-04-28 vs incident 2026-03-20"},
    "truthfulness": {"score": 5, "scheme": "1/3/5", "reason": "every factual claim ties to verified universe atom; L24 soft-verb honored"},
    "tool_use_and_cross_service": {"score": 5, "scheme": "1/5", "reason": "spans email+slack+crm+filesystem+mortgage_los+contacts (6+ services)"},
    "investigation_and_action": {"score": 5, "scheme": "1/5", "reason": "investigation cues + 4 explicit write actions"},
    "coherence_bolt_on": {"score": 5, "scheme": "1/5", "reason": "every paragraph shares incident entities; no orphan sentence"},
    "persona": {"score": 5, "scheme": "1/3/5", "reason": "Owner/Broker Robert Calloway is canonical pay-vs-restore decision authority per PersonaBrief"},
    "business_function": {"score": 5, "scheme": "3/5", "reason": "Executive maps cleanly to strategic pay-vs-restore + borrower-notice decision"}
  },
  "density_projection": {
    "midpoint": 55,
    "band": "PASS",
    "breadth_services": 8,
    "breadth_band": "PASS"
  },
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": []
  },
  "bucket_1_risk_pct": null,
  "iteration": 1,
  "timestamp": "2026-07-01T00:00:00Z"
}
```
