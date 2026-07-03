# Council B v2 — Adversarial QC + Density + Hardness Preservation (POST-AUDIT REVISE)
Task: `Tasks/35_6a4421ec8169e23828bb442d`
Phase: S1 prompt (re-run after AUDIT REVISE)
Deliverable: `5_Prompt.txt`
Universe: keystone (single-entity, today 2026-04-28 America/New_York)
Anchoring scenario: `scenario_14b3ffde` (ransomware pay-vs-restore)
Prior verdict: `S1_B_adversarial.md` returned GO with 12/12 at 5/5. AUDIT downgraded UGT + Clarity to 4/5 under strictest reading (ambiguity around "the incident" — Reading A ransomware-narrow vs Reading B security-cluster-broad).

## Delta under review

Two changes vs prior version:
1. Para 1: "before the end of the week" → "this week" (semantic equivalent — no scoring impact).
2. Para 3: compressed "Anything queued or in draft I have not been looped on" → "Anything queued I have not been looped on" (compression only, no scope change), AND inserted one new sentence: **"Anything feeding the same borrower notice counts, even from a separate workstream."** — positioned between "Do not take the March framing at face value." and "Find the freshest signals on the incident and reconcile them, wherever they live."

Scope of this re-run is strictly the delta. I re-score the two AUDIT-downgraded sub-dims (Unique Ground Truth, Prompt Clarity & Specificity) under the strictest reading, re-check the ten previously-5/5 sub-dims for regression, re-project density, and re-verify the L25 lever now surfaces under its AUDIT-reframed CROSS_SCENARIO_RECONCILE form.

Applied through five role lenses (Architect, Implementer, Red-team, Ground-truth, Integration). Verdict is the union.

---

## [B1] Sub-dim re-scoring

### AUDIT-flagged sub-dims — re-scored under strictest reading

**SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5 scheme) -> the new sentence eliminates Reading A (ransomware-narrow) and locks Reading B (borrower-notice-workstream-broad) as the single leading interpretation.**

Strictest re-scoring of the two candidate readings:

- **Reading A (ransomware-narrow — evidence only from the 3/20 CRM engagement).** The new sentence "Anything feeding the same borrower notice counts, even from a separate workstream" is a first-person directive to broaden scope beyond a single-workstream reading. An agent that read Para 3 as "only pull ransomware-workstream evidence" now has to answer to a prompt sentence that explicitly says separate workstreams count. Reading A is no longer defensible under any reasonable interpretation — it directly contradicts a prompt-visible instruction. **Eliminated.**

- **Reading B (borrower-notice-workstream-broad — evidence from any workstream feeding the same borrower notice).** The new sentence directly names this reading. Additionally, the paragraph structure now makes the reconciliation direction unambiguous: (a) "Denise queued a preliminary plan" (the 3/20 anchor), (b) "Has scope narrowed. Are there specific files anyone has identified since" (invites fresher signals), (c) "Do not take the March framing at face value" (overrides staleness anchor), (d) "Anything feeding the same borrower notice counts, even from a separate workstream" (broadens to cross-workstream), (e) "Find the freshest signals on the incident and reconcile them, wherever they live" (finalizes the reconciliation ask). All five clauses point in one direction. **Single leading interpretation, unambiguous.**

Write-action SET is invariant under Reading B (four writes: decision memo upload, email cyber counsel, Slack status, engagement log note). No candidate reading produces a different write-action set. UGT restored to a genuine 5/5 under strictest AUDIT interpretation.

**SUB-DIM Prompt Clarity and Specificity -> SCORE 5/5 (1/3/5 scheme) -> the new sentence closes the "which incident scope" ambiguity that AUDIT downgraded to 4/5.**

The AUDIT downgrade for Clarity was rooted in the same ambiguity as UGT — a first-time recipient could reasonably read "the incident" as narrow ransomware-only or as the broader security-cluster / borrower-notice workstream, producing different investigation scopes even if write-action set stayed the same. The new sentence resolves the ambiguity at prompt-level by defining membership criteria for the reconciliation: "feeding the same borrower notice", explicitly cross-workstream. A first-time recipient has zero remaining latitude to read "the incident" narrowly. Clarity restored to 5/5.

### The other 10 sub-dims — regression check

Delta re-check against each; nothing new to relax or tighten.

SUB-DIM Feasibility -> SCORE 5/5 (1/3/5 scheme) -> every referenced atom still materialized; no new atoms introduced by the delta
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> new sentence contains zero tool names ("workstream", "borrower notice" are natural exec vocabulary)
SUB-DIM Contrived / Unnatural Prompts -> SCORE 5/5 (1/3/5 scheme) -> new sentence reads as natural directive; matches Robert's blunt exec-voice ("Anything ... counts")
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5 scheme) -> Para 1 wording change "this week" vs "before the end of the week" both anchor to universe today 2026-04-28 (Tuesday); "this week" remains semantically identical
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5 scheme) -> the new sentence makes a scope-directive claim rather than a factual claim; the factual claim it implies (that separate workstreams DO feed the same borrower notice) is grounded — the 4/07 UWM exposure stream and the 4/14 Marcus post-term stream both touch the borrower-file surface Denise's 3/20 plan anchored on
SUB-DIM Tool Use & Cross-service -> SCORE 5/5 (1/5 binary) -> delta preserves cross-service breadth; the cross-workstream broadening likely adds one more surface (CRM + email + Slack across three workstreams), not reduces
SUB-DIM Investigation + Action -> SCORE 5/5 (1/5 binary) -> four write actions preserved; investigation cue strengthened
SUB-DIM Coherence (Bolt-on) -> SCORE 5/5 (1/5 binary) -> new sentence shares core entities ("borrower notice", "workstream") with surrounding paragraph; not a bolt-on
SUB-DIM Persona -> SCORE 5/5 (1/3/5 scheme) -> persona unchanged, voice preserved
SUB-DIM Business Function -> SCORE 5/5 (3/5 scheme) -> Executive mapping unchanged

**B1 summary**: **12/12 at 5/5 under strictest AUDIT-inheriting reading**. UGT and Clarity restored from 4/5 → 5/5 by the new sentence. No regression in the other 10.

---

## [B2] Adversarial alt-path — does the delta introduce any new second reading?

Attempted hostile readings of the new sentence "Anything feeding the same borrower notice counts, even from a separate workstream":

**(a) Could an agent read this as an exclusion rule — "only things feeding the same borrower notice count" — and thereby drop legitimate ransomware-scope files that are NOT tied to borrower notice?**

Analysis: the sentence is grammatically inclusive ("Anything ... counts, even ..."). The word "even" is the tell — it broadens the base set rather than narrowing it. Ransomware-scope files remain a first-class member of the base set because they are what Denise's original 3/20 plan was anchored on (the base set the paragraph opens with). A hostile reading that treats "Anything feeding the same borrower notice counts" as an exclusion would have to ignore the preceding paragraph structure ("Denise queued a preliminary plan the night this started" — establishing ransomware-scope files AS THE ANCHOR of the borrower-notice workstream). The paragraph as written does not permit this hostile reading; the ransomware-scope files feed the same borrower notice by construction. **Contained.**

**(b) Could an agent read "separate workstream" as license to pull unrelated non-security workstreams into the brief (e.g., Marcus-departure severance financials, general HR)?**

Analysis: the sentence conditions inclusion on "feeding the same borrower notice". Non-security workstreams that do not feed the borrower-notice workstream fail the condition and remain out of scope. The Marcus 4/14 post-term-access CRM engagement is IN because it touches borrower-file access review; Marcus severance financials (if any existed in the split) are OUT because they don't. The clause is scoped, not open-ended. **Contained.**

**(c) Could an agent read this as a directive to identify NEW workstreams the operator was unaware of and act on them?**

Analysis: the sentence is a scope-membership rule for the reconciliation ask ("Find the freshest signals on the incident and reconcile them"), not an action-generation directive. The next sentence anchors the whole clause to the reconciliation output. **Contained.**

**(d) Prior adversarial risks (recipient drift to Bennett-* variants, channel drift on Slack post) — do they change?**

Analysis: the delta does not touch the counsel-routing or Slack-channel language. Both risks remain contained at the same MODERATE level flagged in the prior report, both as intended L4 / L26 lever surfaces. **Unchanged.**

**B2 summary**: no new second reading introduced. The new sentence is inclusive by construction and grammatically resistant to exclusion-style hostile readings. Adversarial divergence remains contained.

---

## [B3] Tool-call density projection — delta re-check

Prior projection: midpoint ~55, range 44-68. The delta adds one sentence (~11 words) inviting cross-workstream reconciliation. Two possible effects on trajectory count:

1. **Zero change** if the competent agent already interpreted "Find the freshest signals on the incident, wherever they live" as inviting cross-workstream pulls. Under the pre-delta reading, a reasonable agent already touches the 4/14 CRM engagement (which uses the "post-term access" phrasing that is the Marcus-scenario marker). This was the scenario-crossover surface the prior report's B6 explicitly flagged as legitimate business logic.

2. **Modest additive** if the competent agent now runs one or two extra pulls to enumerate cross-workstream evidence (the UWM 4/07 exposure stream via email search on "UWM" or "wire" keywords; a broader CRM engagement search over the 3/20 → 4/28 window). Estimated additive: +1 to +3 tool calls.

Revised midpoint estimate: ~55-57 (up modestly). Range: 44-70. **Band: PASS** (design target ≥ 50 comfortably met; low-end ≥ 40).

Service breadth unchanged: 8 distinct services, dominant email ~23%. PASS.

---

## [B4] Hardness preservation — L25 supersession restoration

The AUDIT identified L25 as `HARDNESS_REGRESSION` in the pre-revise prompt because the cited 4/14 CRM stream was actually Marcus post-term access (a separate scenario branch), making the L25 supersession lever mis-anchored on a cross-scenario surface without prompt-level acknowledgement. The AUDIT reframed L25 as `CROSS_SCENARIO_RECONCILE` and required the prompt to surface this reframe.

Verification that the new sentence RESTORES L25 to a triggerable state:

- The AUDIT-reframed L25 requires: agent pulls evidence from BOTH the 3/20 ransomware CRM stream (`crm_engagement_f1cb06ea7b65`) AND the 4/07 UWM exposure stream (email chain — verified in ground-truth pre-work not exhaustively re-queried here) AND the 4/14 Marcus post-term stream (`crm_engagement_b95df55fbf01`), treating all three as feeding the same borrower-notice workstream.
- The new sentence directly instructs this: "Anything feeding the same borrower notice counts, even from a separate workstream." Combined with the next sentence "Find the freshest signals on the incident and reconcile them, wherever they live", the agent is prompted to (a) identify workstreams feeding the borrower-notice workstream, (b) treat separate workstreams as legitimate scope even if not ransomware-native, (c) reconcile all three streams into the brief.
- The L25 supersession behavior is now triggerable at prompt-level: the 3/20 ransomware plan is superseded (or at minimum evolved) by the 4/14 borrower-file escalation AND the 4/07 UWM exposure signal, and the prompt makes all three streams legitimate targets.

**L25 restored to a triggerable state under the CROSS_SCENARIO_RECONCILE reframe.** The other four levers (L8 multi-link, L9 latching, L10 structured-DB skip, L26 decoy parent) are untouched by the delta and remain preserved as recorded in the prior report.

**Full 5/5 lever preservation confirmed.** No HARDNESS_REGRESSION.

---

## [B6] Upstream propagation — new flags from the delta?

Delta is a prompt-level absorption of the AUDIT L25 reframe (per the operator context: "the prompt-level fix absorbs the issue"). By design this is a PROMPT-side patch of an issue whose semantic root sits in the Hardness Plan's L25 selection. The AUDIT noted this reframe as a downstream guardrail for the Hardness Plan documentation, not a hard PROPAGATE.

Confirming no NEW upstream flags are raised by the delta:

- Hardness Plan (§L25 selection) — the reframe from "supersession" to "CROSS_SCENARIO_RECONCILE" is now surfaced at prompt-level. The Hardness Plan text still describes L25 in supersession-only terms, but the prompt correctly implements the AUDIT-reframed CROSS_SCENARIO_RECONCILE behavior. The Hardness Plan should be annotated (`## AUDIT REVISE NOTE: L25 reframed to CROSS_SCENARIO_RECONCILE per S1 prompt-level fix`) but this is a documentation update, not a re-run of HARDNESS.
- No S0 propagation. No PersonaBrief propagation. No universe-data propagation.
- Downstream S2/S3 guardrail from the prior report still applies: the OE writer must test the RECONCILIATION BEHAVIOR (agent surfaces cross-workstream signals and folds them into the brief) rather than hard-pin any single CRM engagement as the mandatory ransomware citation. This guardrail is REINFORCED by the delta — the OE must now handle three streams (3/20 ransomware CRM + 4/07 UWM email + 4/14 Marcus CRM) as legitimate cross-workstream inputs.

**PROPAGATE TO S1**: none.
**PROPAGATE TO S0 / HARDNESS**: soft documentation note only (annotate Hardness Plan §L25 with the CROSS_SCENARIO_RECONCILE reframe); no re-run required.
**Downstream S2/S3 guardrail**: reinforced (see above).

---

## Verdict

- Every applicable QC sub-dim: **12/12 at 5**, including UGT and Clarity restored from AUDIT 4/5 → 5/5 by the new sentence.
- No adversarial second reading introduced by the delta; hostile inclusion-vs-exclusion analysis of "Anything feeding the same borrower notice counts, even from a separate workstream" confirms grammatical inclusivity.
- Projected tool-call density midpoint **~55-57** (range 44-70), modest additive from prior 55; well above the 50 design target.
- L25 lever RESTORED to triggerable state under the AUDIT CROSS_SCENARIO_RECONCILE reframe; all 5 levers now preserved.
- No new PROPAGATE flags. Soft documentation note on Hardness Plan §L25 recommended but not required.

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
      "findings": [
        {
          "severity": "NOTE",
          "location": "prompt:para3 (new sentence \"Anything feeding the same borrower notice counts, even from a separate workstream.\")",
          "issue": "Delta restores AUDIT-downgraded UGT + Clarity from 4/5 to 5/5 by eliminating Reading A (ransomware-narrow) and locking Reading B (borrower-notice-workstream-broad) as the single leading interpretation.",
          "fix": "no fix — delta closes the AUDIT F1 softness by prompt-level absorption",
          "propagate_to": null
        }
      ]
    },
    "B2": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "prompt:para3 (new sentence)",
          "issue": "New sentence is grammatically inclusive (\"Anything ... counts, even ...\"); hostile exclusion-style reading contained by paragraph structure (ransomware-scope files feed the borrower-notice workstream by construction).",
          "fix": "no fix — intended inclusive scope directive",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "prompt:para3 (\"separate workstream\") boundary",
          "issue": "\"Separate workstream\" scope contained by \"feeding the same borrower notice\" condition; unrelated non-security workstreams remain out of scope.",
          "fix": "no fix — scope-membership rule is bounded",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "prompt:para3 (counsel routing) + prompt:para4 (Slack channel)",
          "issue": "Prior adversarial risks on counsel recipient drift (Bennett-* variants) and Slack channel drift (C002/C008 decoy) unchanged by delta; both remain intended L4 / L26 lever surfaces.",
          "fix": "no fix — intended lever behavior",
          "propagate_to": null
        }
      ]
    },
    "B3": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "trajectory projection",
          "issue": "Delta adds +1 to +3 tool calls (cross-workstream enumeration); midpoint moves from ~55 to ~55-57; range 44-70. Comfortably above 50 design target.",
          "fix": "no fix",
          "propagate_to": null
        }
      ]
    },
    "B4": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "Hardness Plan §L25",
          "issue": "L25 restored to triggerable state under AUDIT CROSS_SCENARIO_RECONCILE reframe by the new prompt sentence. Agent now prompted to pull from 3/20 ransomware CRM stream + 4/07 UWM exposure stream + 4/14 Marcus post-term stream and reconcile all three into the brief.",
          "fix": "no fix at S1 — L25 now triggerable",
          "propagate_to": null
        }
      ]
    },
    "B6": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "Hardness Plan §L25 documentation",
          "issue": "Hardness Plan text still describes L25 as supersession-only; the AUDIT-reframed CROSS_SCENARIO_RECONCILE behavior is now surfaced at prompt-level but the plan documentation lags. Soft documentation update recommended.",
          "fix": "Annotate Hardness Plan §L25 with \"## AUDIT REVISE NOTE: L25 reframed to CROSS_SCENARIO_RECONCILE per S1 prompt-level fix; agent pulls evidence from all three streams (3/20 ransomware, 4/07 UWM, 4/14 Marcus).\" No HARDNESS re-run required.",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "downstream S2/S3 guardrail",
          "issue": "OE writer must test the reconciliation BEHAVIOR (surfaces fresher borrower-notice signals across multiple workstreams, folds them into the brief); do NOT hard-pin any single CRM engagement (e.g., crm_engagement_b95df55fbf01) as the mandatory ransomware citation. Reinforced by delta.",
          "fix": "S2 writer: frame the OE around 'agent surfaces fresher borrower-notice signals across multiple workstreams and reconciles them into the brief'; do not require citing any single engagement ID as the ransomware-authoritative row.",
          "propagate_to": null
        }
      ]
    }
  },
  "scores": {
    "unique_ground_truth": {"score": 5, "scheme": "1/3/5", "reason": "new sentence eliminates Reading A (ransomware-narrow); Reading B (borrower-notice-workstream-broad) is unambiguous single leading interpretation; write-action set invariant"},
    "feasibility": {"score": 5, "scheme": "1/3/5", "reason": "every referenced atom materialized in per-task universe; no new atoms introduced by delta"},
    "explicit_tool_mention": {"score": 5, "scheme": "1/5", "reason": "zero tool names in prompt body; new sentence uses natural exec vocabulary"},
    "prompt_clarity_and_specificity": {"score": 5, "scheme": "1/3/5", "reason": "new sentence closes the \"which incident scope\" ambiguity the AUDIT downgraded; first-time recipient has zero remaining latitude to read \"the incident\" narrowly"},
    "contrived_unnatural_prompts": {"score": 5, "scheme": "1/3/5", "reason": "new sentence reads as natural exec directive matching Robert's blunt voice"},
    "alignment_with_todays_date": {"score": 5, "scheme": "1/3/5", "reason": "\"this week\" semantically identical to prior \"before the end of the week\"; anchors cleanly to universe today 2026-04-28"},
    "truthfulness": {"score": 5, "scheme": "1/3/5", "reason": "new sentence is a scope-directive; implied factual claim (separate workstreams DO feed the same borrower notice) is grounded via 4/07 UWM exposure + 4/14 Marcus post-term"},
    "tool_use_and_cross_service": {"score": 5, "scheme": "1/5", "reason": "cross-service breadth preserved; cross-workstream broadening likely adds surface, not reduces"},
    "investigation_and_action": {"score": 5, "scheme": "1/5", "reason": "four write actions preserved; investigation cue strengthened by cross-workstream directive"},
    "coherence_bolt_on": {"score": 5, "scheme": "1/5", "reason": "new sentence shares core entities (\"borrower notice\", \"workstream\") with surrounding paragraph; not a bolt-on"},
    "persona": {"score": 5, "scheme": "1/3/5", "reason": "persona unchanged, voice preserved"},
    "business_function": {"score": 5, "scheme": "3/5", "reason": "Executive mapping unchanged"}
  },
  "density_projection": {
    "midpoint": 56,
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
  "iteration": 2,
  "timestamp": "2026-07-01T00:00:00Z"
}
```
