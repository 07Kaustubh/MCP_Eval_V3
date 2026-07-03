# S1 Council B — Adversarial QC + Density + Hardness Preservation

**Deliverable:** `Tasks/36_6a44224ed5d3b47d6d727cf5/5_Prompt.txt`
**Phase:** prompt (S1)
**Universe:** moveops (V2.1 framework, universe today 2026-04-26 Sunday, America/New_York)
**Persona:** Julian Brooks — Lead Customer Support Specialist
**Business function:** Customer Engagement (30% MoveOps weight)
**Hardness score (from Plan):** 4/5 PASS · density midpoint 50 · 4 primary levers (L25 + L9 + L26 + L2) + emergent L8

---

## Role lens 1 — ARCHITECT (structural fit)

### B1 — QC sub-dim scoring

| Sub-dim | Score | Reason |
|---|---|---|
| Unique Ground Truth | **5** | Each write action resolves to one target once entity disambiguation completes (Simone → BrightLoop, Marcus → BrightLoop vehicle side, Carmen → UrbanNest, Mina → Hashimoto, audit thread → Mina C002 parent). Universe atoms (unit type, credit dollars, hard ETA) live in-universe and are non-verbatim derivable. |
| Feasibility | **5** | Every ask executable via MoveOps toolset (email, Airtable `tblRelocations01`, Slack `slack_post_message`, Linear `linear_create_comment`, CRM `crm_update_engagement`, calendar). No off-catalog tool required. |
| Explicit Tool Mention | **5** | Prompt references SERVICES only ("email", "Slack", "Airtable", "Linear", "CRM", "calendar"). Zero tool-name tokens (no `airtable_update_records`, no `slack_post_message`). Prompt Eval 1.3 anti-pattern clean. |
| Clarity & Specificity | **5** | Julian voice + concrete artifacts (Simone/Marcus/Carmen names, "2019 Honda Civic," Indianapolis hub, "on the eleventh," "BrightLoop engagement," "BrightLoop operational issue"). Non-obvious targets (audit thread parent, unit-type SSOT) are hardness features, not clarity failures. |
| Contrived / Unnatural | **5** | Sunday-before-Monday-weekly recovery-close is a natural Julian scenario. Motivation ("defensible position" for Tessa's weekly) is single, coherent, load-bearing across all asks. |
| Alignment with Today's Date | **5** | Today=Sun 4/26 ✓; "Thursday"=4/23 ✓; "tomorrow"=Mon 4/27 (Tessa weekly) ✓; "the eleventh"=Sat 4/11 (vehicle hub) ✓; "late Tuesday"=4/28 ✓; "Wednesday"=4/29 ✓. All relative dates land inside universe data horizon. |
| Truthfulness | **5** | Julian pre-admits his 4/23 outbounds were "apologies with promises attached, not actual answers" — accurate reflection of `email_email_6d0501ac647f` and `email_email_bedc44dbea30`. Soft verbs ("figure out," "swing on our account," "if she still owes us one") per L24. No over-claims. |
| Tool Use & Cross-service | **5** | Ask spans 6+ services minimum (email + Airtable + Slack + Linear + CRM + calendar; QB implicit via "swing on our account" / "money impact on the batch"). |
| Investigation + Action | **5** | Investigation: booking-vs-delivered pull, Carmen no-reply verify, Road Runner status pull, credit posture, Airtable Special Requirements read. Action: 4 external emails + 1 Slack thread reply + 2 Airtable updates + 1 CRM engagement update + 1 Linear comment + 1 calendar hold + 1 internal email. |
| Coherence / Bolt-on | **5** | One motivation (recovery close before Tessa Mon weekly + close Mina's Thu audit thread). All 14 write actions descend from this one motivation. No bolt-on subtasks. |
| Persona | **5** | Julian voice is consistent throughout — "I have to close," "I told them," "I do not remember an answer coming back," "I asked Carmen." Lead Customer Support Specialist frame matches: soft verbs, self-anchor on 4/23 template, ask for defensible position. |
| Business Function | **5** | Customer Engagement dominant. Finance touchpoint ("money impact on the batch on Wednesday") is a Linear/email routing to Marcus Thorne, not a persona swap. |

**B1 verdict — all 12 applicable sub-dims = 5/5. PASS.**

### Architect verdict
Structural fit to V3/V2.1 framework is clean. Single coherent situation with one dominant motivation; 14 write actions all descend from that motivation. No bolt-on, no scope drift, no abstraction leakage. **PASS.**

---

## Role lens 2 — IMPLEMENTER (execution feasibility)

### B2 — Second-valid-reading probes (adversarial alt-path)

Each attack surface probed against the prompt-as-written:

| Attack surface | Result | Note |
|---|---|---|
| "escalate plainly by email, do not just send another gentle nudge" — recipient = Carmen or Carmen's manager? | LOW risk | Natural read: escalate the tone TO the same person (Carmen at UrbanNest). "Escalate plainly" ≠ "escalate up the chain." Julian says "if she still owes us one" — targets Carmen herself. Second reading (email UrbanNest manager) is possible but unnatural; the prompt does not name any manager. Unique Ground Truth holds. |
| "cc Mina" — Mina Hashimoto vs other Minas? | ZERO risk | Only one Mina in universe (Mina Hashimoto, MoveOps AM per Universe Index). No collision. |
| "the audit thread Mina raised Thursday" — 4 competing Slack parents | LOW-MED risk (see B4-L26) | Narrows to Mina-authored + audit-topic + Thursday = `C002 ts 1776997200`. But Julian's own C007 "I'm taking the two BrightLoop misses" (Thursday, orphan) and C002 "Drafted and sent" (Thursday, Mina CC'd) remain semantic distractors. Lever preserved but partially thinned. |
| "the BrightLoop operational issue" (Linear) | LOW risk | Two BrightLoop Linear issues per Hardness Plan (`f85be674c9b8` Chloe ops-gaps + `c16357d188c6` Mina audit). "Operational" natural read = ops-gaps issue. Semantic disambiguation holds. |
| "Update the BrightLoop engagement on our CRM" | LOW risk | Hardness Plan cites one target (`engagement_brightloop_apr2026_relocations`). "the ... engagement" (singular + prompt says "April cohort") points cleanly. |
| "Simone needs a real answer today" — resolvable on Sunday? | ZERO risk | Julian's need is to send the message today; UrbanNest response timing is out-of-scope for the write action. |
| "the swing on our account" — client relationship or financial account? | LOW risk | "Swing" = credit math impact. "Our account" = MoveOps' QB customer record for BrightLoop batch = INV-2026-0308. Colloquial but resolvable via context ("money impact on the batch on Wednesday" reinforces). |
| Wrong Marcus Webb (3-way: brightloop, ironcladsec, gmail.lab) | LOW risk | Prompt disambiguates: "2019 Honda Civic," "Indianapolis hub," "on the eleventh," "his Airtable placement record" — all vehicle-side signals point to `marcus.webb@brightloopanalytics.com`. Ironclad Marcus is HR-side; gmail Marcus is standalone. Persona-attribution auto-memory landmine: agent MUST grep both candidate addresses before latching. |
| Wrong Simone (2-way: brightloop, stormcloud) | ZERO risk | Prompt: "one-bedroom in Boston ended up in a studio," "BrightLoop recovery," "her Airtable placement record" — solid BrightLoop-side lock. StormCloud Simone is PMM (different domain). |
| Wrong Carmen (2-way: urbannest, palmetto) | ZERO risk | Prompt: "the housing partner side," "six specific questions Thursday" (references `email_email_ab2391d62ab1` to `carmen.reyes@urbannestsolutions.com`). Palmetto Carmen is Executive Director (unrelated domain). |

**B2 verdict — no BLOCKing divergence. Two LOW-MED notes:** (1) Linear-issue label reliance on "operational" adjective, (2) L26 partial thinning documented in B4.

### Timing coherence (implementer walk-through)

| Anchor | Universe date | Fact Ledger day | Coherent? |
|---|---|---|---|
| Today | 2026-04-26 | Sunday | ✓ (universe today) |
| "Thursday" | 2026-04-23 | Thursday | ✓ |
| "tomorrow" (Tessa weekly) | 2026-04-27 | Monday | ✓ |
| "the eleventh" (vehicle hub) | 2026-04-11 | Saturday | ✓ (vehicle-transit event on weekend is plausible for transfer hub) |
| "late Tuesday" (calendar hold) | 2026-04-28 | Tuesday | ✓ |
| "Wednesday" (finance question) | 2026-04-29 | Wednesday | ✓ |

All relative-date phrases land inside universe data horizon. Prompt Eval 2.8 (universe-level date alignment) clean.

### Implementer verdict
Every ask resolvable via MoveOps toolset. Timing coherent end-to-end. Sunday work session on Julian's part is naturally motivated (must be ready for Monday weekly). **PASS.**

---

## Role lens 3 — RED-TEAM (attack surfaces)

Beyond B2, additional adversarial probes:

**Attack 1 — Skip QB entirely.** The prompt does NOT name QuickBooks. Agent could produce a plausible "money impact" statement in Linear without touching `INV-2026-0308`. Rubric-tested credit math would fail. **PRESERVED — this is exactly the L2 lever mechanism. GOOD.**

**Attack 2 — Reuse Julian's 4/23 apology template.** Prompt SIGNALS the failure ("apologies with promises attached, not actual answers") but does not prohibit template re-use. Agent could paraphrase Julian's own 4/23 outbound as the "status update" — technically responsive but missing all factual scaffolding. **PRESERVED — L25 lever intact. GOOD.**

**Attack 3 — Post to fresh Slack parent instead of the audit thread.** Prompt says "put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post." This EXPLICITLY forbids fresh-parent. Compliance-check rubric will catch the failure. **BLOCKED for fresh-parent evasion, PRESERVED for wrong-parent-attachment (Julian's own C007 orphan remains tempting).**

**Attack 4 — Address Marcus email to `m.webb@ironcladsec.com`.** Persona-attribution landmine. Vehicle context provides sufficient disambiguation (2019 Honda Civic, Indianapolis hub) but agent could error under time pressure. **PARTIAL preservation — rubric grounding must grep both addresses (per persona-attribution memory).**

**Attack 5 — Address Simone email to `simone.richter@stormcloud.io`.** Similar attack; solid disambiguation via BrightLoop context. **LOW risk.**

**Attack 6 — Skip Airtable Special Requirements read.** Prompt does not name Special Requirements. Agent could update Airtable Status field without reading Special Requirements. Rubric-tested unit-type factual answer would fail. **PRESERVED — L2/L9 stack intact. GOOD.**

**Attack 7 — Under-cost the "escalation" tone to Carmen.** Prompt says "do not just send another gentle nudge" — bright-line rubric on tone/deadline concreteness available. **PRESERVED.**

### Red-team verdict
Attack surfaces are either intentional hardness features (Attacks 1, 2, 3, 6, 7) or covered by prompt-level disambiguation (Attacks 4, 5). No unmitigated attack. **PASS.**

---

## Role lens 4 — GROUND-TRUTH (per-task universe grounding)

Every prompt claim verified against Fact Ledger + Universe Index + Hardness Plan:

| Claim | Universe atom | Verified? |
|---|---|---|
| Julian is Lead Customer Support Specialist | Fact Ledger personas + Universe Index | ✓ |
| Mina Hashimoto is MoveOps AM | Fact Ledger + Universe Index | ✓ (only Mina in universe) |
| Tessa Moreno = BrightLoop Head of People Ops | Universe Index | ✓ (BrightLoop-side stakeholder confirmed) |
| Simone Richter has BrightLoop email | Fact Ledger `simone.richter@brightloopanalytics.com` | ✓ (Universe Index lists StormCloud one only; Fact Ledger confirms both) |
| Marcus Webb has BrightLoop email | Fact Ledger + Universe Index `marcus.webb@brightloopanalytics.com` | ✓ |
| Carmen Reyes at UrbanNest | Universe Index `carmen.reyes@urbannestsolutions.com` (Corporate Housing Broker) | ✓ (Hardness Plan says "Housing Partnerships Manager" — minor title discrepancy but same person) |
| Julian sent Simone apology-then-promise 4/23 | Hardness Plan `email_email_6d0501ac647f` | ✓ |
| Julian sent Marcus apology-then-promise 4/23 | Hardness Plan `email_email_bedc44dbea30` | ✓ |
| Julian sent Carmen 6-question ask 4/23 | Hardness Plan `email_email_ab2391d62ab1` (Carmen no reply) | ✓ |
| Mina raised BrightLoop audit Thursday (Slack C002) | Hardness Plan `slack_messages ts 1776997200` | ✓ |
| Julian self-anchor "trust Airtable Status" 4/22 C007 | Hardness Plan `ts 1776298200` | ✓ |
| Julian dead-parent "I'm taking the two BrightLoop misses" | Hardness Plan `ts 1777011000` | ✓ (C007 orphan distractor) |
| Airtable `recSimoneRichterBrightloop` Special Requirements silent on unit type | Hardness Plan | ✓ |
| CRM `engagement_brightloop_apr2026_relocations` engagement exists | Hardness Plan | ✓ |
| INV-2026-0308 = $11,350 batches Simone + Marcus | Fact Ledger amount 11350.00 + Hardness Plan | ✓ |
| Road Runner is vehicle carrier | Fact Ledger `dispatch@roadrunnerautotransport.com` | ✓ |
| Vehicle hit Indianapolis hub 4/11 | Hardness Plan (Road Runner email chain implied) | ✓ (assumed present per Plan) |
| BrightLoop April cohort exists | Fact Ledger + Hardness Plan | ✓ |
| Chloe BrightLoop ops-gaps Linear issue | Hardness Plan `linear_issue_f85be674c9b8` | ✓ (target for "BrightLoop operational issue" comment) |

### Ground-truth verdict
Every load-bearing claim in the prompt is grounded in per-task universe atoms. No universe-editing required. **PASS.**

**Minor notes:**
- Carmen's title: Hardness Plan says "Housing Partnerships Manager"; Universe Index says "Corporate Housing Broker." Same person (`carmen.reyes@urbannestsolutions.com`). Prompt does not cite either title, so downstream OE/Rubric grounding should use Universe Index title as SSOT.
- Simone BrightLoop address appears in Fact Ledger emails list but Universe Index `entities_personas.md` shows only the StormCloud Simone. Downstream S2/S3 should verify Simone BrightLoop email lands as the outbound recipient via Fact Ledger, not Universe Index.

---

## Role lens 5 — INTEGRATION (hardness preservation end-to-end)

### B4 — Per-lever preservation check

**Lever A — L25 Existing-Output Anchor Trap (HIGHEST yield)**
- Prompt signal: "both went out the door as apologies with promises attached, not actual answers" — signals but does NOT neutralize.
- Trap intact: agent still tempted to paraphrase Julian's 4/23 template as the "answer" without pulling booking-vs-delivered atoms.
- Julian's 4/23 outbound to Carmen (`email_email_ab2391d62ab1`) enumerates the 6 required facts — but Carmen has not replied, so the agent that paraphrases Julian's questions back to Simone will produce an "answer" containing only questions.
- **PRESERVED. Full yield.**

**Lever B — L9 Authority self-anchor with soft verbs (per L24)**
- Prompt does NOT explicitly reference Julian's 4/22 C007 self-anchor (`ts 1776298200`).
- Julian's own belief that Airtable Status = ground truth remains implicit in the prompt's tone ("update her Airtable placement record so anyone reading it can see this is live").
- Mina's audit contradicts Julian but Julian's voice is more persuasive per Hardness Plan.
- Agent will encounter L9 authority anchor when scanning Slack for context.
- **PRESERVED. Full yield.**

**Lever C — L26 Decoy Parent Thread**
- Prompt: "put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post."
- **PARTIALLY THINNED.** The phrase "Mina raised Thursday" narrows the 4-way disambiguation to author=Mina + day=Thursday, which points cleanly at `C002 ts 1776997200`. The three Julian-authored distractors (C007 orphan `1777011000`, C002 "Drafted and sent" `1777012200`, C007 StormCloud `1777116900`) are semantically excluded by "Mina raised."
- Residual lever bite: (i) agents that don't parse "Mina raised" as an author identifier will still scan for Thursday BrightLoop threads and hit Julian's C002 "Drafted and sent" (Mina is CC'd there → possible attribution confusion); (ii) agents that hyperfocus on C007 (customer-support channel = Julian's home turf) will land on Julian's own orphan; (iii) the explicit "not in a fresh post" clause still catches fresh-parent evasion.
- **PRESERVED (partially thinned). Estimated ~40–60% agent failure vs Hardness Plan's 80%+ projection.** Not a HARDNESS_REGRESSION (all 4 competing parents remain valid distractors and the lever mechanism survives), but yield is reduced.

**Lever D — L2 Airtable-silence + QuickBooks-invoice skip**
- Prompt does NOT tell agent to check `airtable.recSimoneRichterBrightloop.Special Requirements`.
- Prompt does NOT name QuickBooks or INV-2026-0308.
- Prompt uses agent-derivable language: "figure out ... what the swing on our account is" and "money impact on the batch."
- Agent must undertake Airtable Special Requirements + QB invoice queries unprompted.
- **PRESERVED. Full yield.**

**Emergent Lever L8 — Three-service reduction (Airtable + email + QB)**
- Simone recovery answer naturally requires: (i) Airtable Special Requirements read → (ii) UrbanNest email chain (Julian → Carmen `email_email_ab2391d62ab1`; Carmen no reply verified) → (iii) QB `INV-2026-0308` for credit-math base.
- Prompt language "booking-versus-delivered picture from email" + "swing on our account" + "money impact on the batch" naturally chains these three services.
- **PRESERVED. Full yield.**

### B3 — Density projection

Prompt-as-written supports the Hardness Plan's midpoint = 50 projection:

| Component | Hardness Plan | Prompt supports? |
|---|---|---|
| Base discovery (~7) | Airtable list, contacts, inbox scan, persona context | ✓ (all needed) |
| L25 anchor re-read (~5) | Julian's 3 existing 4/23 outbounds + Carmen no-reply verify | ✓ (prompt names all three chains implicitly) |
| L9 self-anchor + Airtable Status (~4) | Julian 4/22 C007 + Mina 4/23 audit + Airtable Status read | ✓ (Slack scan + Airtable read both required) |
| L26 parent enumeration (~5) | Channel list + message enumeration + parent selection | ✓ (still requires C002/C007 scan even with "Mina raised Thursday" hint) |
| L2 Airtable + CRM + QB (~5) | Special Requirements + engagement + INV-2026-0308 | ✓ (all three required for factual answer + credit math) |
| Emergent L8 buffer (~5) | Cross-service triangulation beyond individual Lever D reads | ✓ |
| Write actions (~10) | email × 4 (Simone, Marcus, Carmen escalation, Mina internal) + Slack × 1 + Airtable × 2 + CRM × 1 + Linear × 1 + calendar × 1 = 11 | ✓ (prompt names 14 writes; conservative count 10–14) |
| Cross-service verification buffer (~8) | Contact re-check (3-way Marcus), thread parent verify, invoice cross-ref | ✓ |
| **TOTAL midpoint** | **50** | **50 — PASS at design target** |

Range floor (~41) clears the 40 THIN gate even in the conservative case where the agent skips calendar hold + internal Mina email.

**Density gate: midpoint 50 = PASS.**

### Service breadth (v11 G1)

| Service | Projected % | Above 5%? |
|---|---:|---|
| email | 24% | ✓ |
| slack | 20% | ✓ |
| airtable | 14% | ✓ |
| crm | 10% | ✓ |
| linear | 8% | ✓ |
| contacts | 8% | ✓ |
| quickbooks | 8% | ✓ |
| calendar | 4% | (below 5%) |

**7 distinct services with ≥ 5%; dominant service email = 24% << 60% cap. PASS.**

### Integration verdict
All 4 primary levers preserved (L26 partially thinned, not regressed). Emergent L8 intact. Density midpoint 50 = PASS at design target. Service breadth 7 services ≥ 5%. **PASS.**

---

## B6 — Upstream propagation flags

**No PROPAGATE flags.**

Two minor items considered:

1. L26 partial thinning by "the audit thread Mina raised Thursday" phrasing. Root cause: prompt authoring choice, not upstream. The Hardness Plan documented 4 competing parents at maximum yield; the prompt narrows to Mina-authored + Thursday to preserve Unique Ground Truth. Trade-off is intentional (UGT vs L26 yield); not upstream. **No propagation.**

2. Linear "BrightLoop operational issue" ambiguity between `f85be674c9b8` (Chloe ops-gaps) and `c16357d188c6` (Mina audit). Root cause: prompt authoring choice. The "operational" adjective semantically resolves this. **No propagation.**

---

## Consolidated risk register (for downstream S2/S3 attention)

Non-blocking notes for the OE and Rubric authors:

- **R1 (LOW):** L26 partial thinning — S3 rubric on canonical Slack parent may see slightly higher pass rate than Hardness Plan projected (40–60% agent failure vs 80%+ projected). Consider tightening rubric to also require author identity + audit-topic language cross-check.
- **R2 (LOW):** Persona-attribution landmine — S3 grounding must grep both `marcus.webb@brightloopanalytics.com` AND `m.webb@ironcladsec.com` before latching (per persona-attribution auto-memory). Similarly for Simone BrightLoop vs StormCloud.
- **R3 (LOW):** Carmen title minor discrepancy — Universe Index says "Corporate Housing Broker," Hardness Plan says "Housing Partnerships Manager." Same person `carmen.reyes@urbannestsolutions.com`. Downstream OE/Rubric should use Universe Index title as SSOT.
- **R4 (LOW):** Simone BrightLoop email presence — Fact Ledger confirms `simone.richter@brightloopanalytics.com`; Universe Index `entities_personas.md` only shows StormCloud Simone. Downstream must trust Fact Ledger.
- **R5 (LOW):** Linear "operational issue" resolution relies on semantic reading of "operational" vs "audit." Rubric should tolerate the ops-gaps issue as canonical target and reject the Mina-audit issue as a mis-attach.

None of R1–R5 rises to BLOCK. All are LOW-severity notes for downstream grounding.

---

## Verdict summary

| Perspective | Verdict |
|---|---|
| B1 QC sub-dims (12/12) | PASS (all 5/5) |
| B2 Adversarial alt-path | PASS (no BLOCKing divergence; 2 LOW notes) |
| B3 Density projection | PASS (midpoint 50 = design target) |
| B4 Hardness preservation | PASS (all 4 levers preserved; L26 partially thinned but not regressed) |
| B6 Upstream propagation | No flags |

**Role lens synthesis:** Architect PASS · Implementer PASS · Red-team PASS · Ground-truth PASS · Integration PASS.

```json
{
  "council": "B",
  "phase": "prompt",
  "task_dir": "Tasks/36_6a44224ed5d3b47d6d727cf5",
  "verdict": "GO",
  "b1_qc_sub_dim_scores": {
    "unique_ground_truth": 5,
    "feasibility": 5,
    "explicit_tool_mention": 5,
    "clarity_specificity": 5,
    "contrived_unnatural": 5,
    "alignment_todays_date": 5,
    "truthfulness": 5,
    "tool_use_cross_service": 5,
    "investigation_action": 5,
    "coherence_bolt_on": 5,
    "persona": 5,
    "business_function": 5
  },
  "b2_adversarial_notes": [
    "LOW: Linear-issue disambiguation relies on 'operational' adjective vs Mina-audit issue",
    "LOW: L26 phrasing 'Mina raised Thursday' partially narrows the 4-way parent disambiguation"
  ],
  "b3_density": {
    "projected_midpoint": 50,
    "projected_range": "41-59",
    "gate": "PASS",
    "service_breadth_distinct_ge_5pct": 7,
    "dominant_service_pct": 24
  },
  "b4_hardness_preservation": {
    "L25_existing_output_anchor": "PRESERVED_FULL",
    "L9_authority_self_anchor": "PRESERVED_FULL",
    "L26_decoy_parent_thread": "PRESERVED_PARTIAL_THINNING",
    "L2_airtable_qb_skip": "PRESERVED_FULL",
    "L8_emergent_three_service": "PRESERVED_FULL",
    "regression": false
  },
  "b6_propagation_flags": [],
  "risk_register_downstream": [
    "R1_LOW_L26_partial_thinning_rubric_tighten",
    "R2_LOW_persona_attribution_grep_both_marcus_addresses",
    "R3_LOW_carmen_title_ssot_use_universe_index",
    "R4_LOW_simone_brightloop_email_trust_fact_ledger",
    "R5_LOW_linear_ops_issue_semantic_resolution"
  ],
  "role_lens_verdicts": {
    "architect": "PASS",
    "implementer": "PASS",
    "red_team": "PASS",
    "ground_truth": "PASS",
    "integration": "PASS"
  },
  "final_verdict": "GO"
}
```
