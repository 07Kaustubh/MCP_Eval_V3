# Council B — Adversarial QC + Density + Hardness Preservation (S1 Prompt)

- **Phase:** prompt
- **Council:** B
- **Task:** Tasks/34_6a42ec7493b48d5ada4571bd
- **Deliverable:** `5_Prompt.txt`
- **Universe:** moveops (V2.1 framework — using `Docs_moveops/7_QC_Spec_Doc1.json` + `Evals_moveops/1_Prompt_Eval.md`)
- **Upstream:** `_aux/Hardness_Plan.md` (Anchor A — Blessing Okafor / Operations / Emilia Cruz damage docket; 5 levers L1/L2/L7/L8/L11; 47-midpoint THIN_DENSITY accepted per operator note)
- **Iteration:** 1

---

## Universe Verification (programmatic floor before LLM lenses)

Confirmed against `_aux/Universe_Split/`:

| Lever anchor | Universe record | Confirmed |
|---|---|---|
| KeyMove rider $1,200 / DueDate 2026-04-24 / Steinway scratch line description | `quickbooks.bills.json` → `BILL-KEYMOVE-2026-0417` (TxnDate 2026-04-17, AccountRef ACC-6185 "Claims & Remediation Expense", VendorRef VEND-KEYMOVE-001) | YES |
| Craig Nguyen Apr 11 damage email to Blessing | `email.emails.json` → `email_email_1f1459bff84c` 2026-04-11T23:42 — subject "Emilia Cruz Steinway damage photos and extraction notes" | YES |
| Marcus Thorne Apr 17 L9 framing email | `email.emails.json` → `email_email_99e10a978b48` 2026-04-17T17:14 — subject "KeyMove added $1,200 insurance rider for Emilia Cruz claim", to David Chen | YES |
| Catalina Apr 14 NorthWind "by end of week" commitment | `email.emails.json` → `email_email_ab22f67eeeb0` 2026-04-14T17:18 — subject "NorthWind service recovery plan by end of week", to Pam Kowalski | YES |
| Slack channels (C006 operations, C002 customer-engagement, C005 finance) | `slack.slack_channels.json` — C006 operations, C002 customer-engagement, C005 finance | YES |
| Universe today | Fact_Ledger dates list closes 2026-04-26 Sunday; S0 confirms `2026-04-26` | YES |

Relative-date resolution under universe today = 2026-04-26 (Sun): "this morning" → Apr 26 Sun; "the 11th" → Apr 11 (Craig email — CONFIRMED); "Monday" → Apr 27 — all resolve to records present in universe. The validator-reported `2026-06-12` lifecycle date is stale Brookfield default; MoveOps S0 Setup Report names 2026-04-26 as authoritative, and every relative reference in the prompt resolves against that anchor.

---

## Role-Lens Reading (5 passes)

| Lens | Headline finding |
|---|---|
| **Architect** | Prompt structure is clean V2.1 first-person Operations voice (Blessing). Anchors: Chloe's verbal ask + KeyMove rider arrival + Catalina's NorthWind side. No abstractions broken. PASS. |
| **Implementer** | Every action is implementable: email send to Craig (`craig.nguyen@keymove-specialty.com` resolvable in contacts), email send to David + Catalina (resolvable), `airtable_update_records` on Emilia row, slack post, linear comment, reminder. No invented IDs. PASS. |
| **Red-team** | Three alt-paths tested below (B2). All resolve to INTENDED_HARDNESS — the prompt's framing is the designed stump, not a clarity fail. PASS. |
| **Ground-truth** | Every concrete claim resolves to per-task universe (table above). The "Mosaic case last quarter" reference is a HINT not a pre-solving leak — the prompt does NOT name the bill_id, the credit-memo number, the vendor cap, or the Section 6 process-improvement template. Agent must query QB + Airtable to recover the model. PASS. |
| **Integration** | L1/L2/L7/L8/L11 all preserved (B4 below). Hardness Plan's hard-rule list cross-checked: NO Pam-escalation mention, NO Friday-EOD-package mention, NO $60K-account-risk mention, NO escape-valve clause ("if anything looks off, say so plainly"), NO tool names, NO IDs, NO em-dashes, NO "at least N", NO service names. All clean. PASS. |

Union verdict: GO.

---

## [B1] QC Sub-Dim Scoring (12 dims for prompt phase)

```
SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5 scheme) -> 6-write action set converges across reasonable readings; vendor-vs-customer disposition split is the intended derivation, not an alt path.
SUB-DIM Feasibility -> SCORE 5/5 (1/3/5 scheme) -> every action implementable in moveops tool surface; recipients resolvable in contacts.contacts; Airtable Emilia row + Linear NorthWind issue exist.
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> no tool names, no service names, no API verbs in the prompt body (grep clean).
SUB-DIM Clarity & Specificity -> SCORE 5/5 (1/3/5 scheme) -> L9 framing on the vendor line is INTENDED (per Hardness_Plan + calibration note); prompt explicitly says "The rider closes one ledger line. It does not close out the rest of this" — second-reading attack on rider-approval closed by "I am not going to relitigate the rider with him. That part is in his lane."
SUB-DIM Contrived/Unnatural -> SCORE 5/5 (1/3/5 scheme) -> first-person reflective voice on a same-day operational catch-up reads natural; Sunday after-deadline catch-up is plausible given Apr 24 KeyMove DueDate already lapsed and NorthWind crisis context.
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5 scheme) -> "the 11th" resolves to Apr 11 Craig email (confirmed); "Monday" resolves to Apr 27 (Apr 26 Sun + 1); "this morning" resolves to Apr 26 Sun. Every relative reference resolves to a universe record. (Validator's 2026-06-12 reading is stale Brookfield lifecycle default; S0 Setup Report names 2026-04-26 as authoritative.)
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5 scheme) -> every factual claim verified against universe: Craig Apr 11 ✓, Marcus's process-as-submitted read ✓ (verbatim language matches Apr 17 email), Catalina assembling NorthWind side ✓ (Apr 14 commitment), Mosaic case last quarter ✓ (Q1 2026 precedent, "last quarter" relative to Apr 26 reads correctly), Linear item open for NorthWind ✓ (retention issue per Hardness_Plan), walkup-assessment admission ✓ (Blessing's persona-brief field admission). Zero ungrounded claims.
SUB-DIM Tool Use & Cross-service -> SCORE 5/5 (1/5 binary) -> 5+ services minimum (email Craig, email David+Catalina, airtable update Emilia row, slack post, linear comment, reminder); breadth gate passes.
SUB-DIM Investigation + Action -> SCORE 5/5 (1/5 binary) -> multiple investigations required (Mosaic precedent query, Emilia Airtable state, Marcus's email read, Craig's open question, Catalina's NorthWind track, Linear NorthWind issue lookup) + 6 distinct write actions across 5 services.
SUB-DIM Coherence (Bolt-on) -> SCORE 5/5 (1/5 binary) -> every entity (Emilia, NorthWind, Catalina, David, Chloe, Marcus, Craig, KeyMove, Mosaic precedent, Linear NorthWind item, Monday Craig follow-up) coheres around the Emilia operational docket. Nothing bolt-on.
SUB-DIM Persona -> SCORE 5/5 (1/3/5 scheme) -> Relocation Coordinator voice: operational not financial ("I am not going to relitigate the rider with him. That part is in his lane"), field-facts owner ("the walkup assessment underestimated that stairwell turn radius"), defers customer-comm scope ("I do not have authority on the client facing piece"). Perfectly scoped.
SUB-DIM Business Function -> SCORE 5/5 (3/5 scheme) -> Operations: closing out an operational damage docket, owning the field-facts lesson, coordinating the operational position to the customer-engagement track. Not Finance (Marcus owns the rider), not Customer Engagement (David/Catalina own the retention package). Clean Operations fit.
```

All 12 dims at 5/5. Zero NON-FAIL bands invoked.

---

## [B2] Adversarial Alt-Path

Three alt-readings tested per the brief:

**(a) "Process it as submitted" + "I am not going to relitigate" → agent attempts QB rider approval.**

Verdict: **INTENDED_HARDNESS_NOT_CLARITY_FAIL.**

The prompt's framing is unambiguous on persona authority: "His read is we process it as submitted ... I am not going to relitigate the rider with him. That part is in his lane" — Marcus is the actor on the bill; Blessing is reporting Marcus's read, not adopting it as her own write action. A competent Opus 4.8 agent reading "Marcus already weighed in on the finance side" + "his lane" should not invoke QB write tools on Blessing's behalf. Even if the agent mis-attributes authority and tries `quickbooks_update_bill` or similar, the persona-scope validator (Council A A6) catches it. The prompt itself does not direct a QB write — the latching is on Marcus's framing, which is what L1 is designed to do: anchor on the vendor-line conclusion so the agent stops investigating the customer-side disposition. This is L1 + L9 working as intended.

**(b) "Drop the Emilia lesson in Slack where Chloe and the ops team will see it" → agent posts in #customer-engagement (C002) or #finance (C005).**

Verdict: **INTENDED_HARDNESS_NOT_CLARITY_FAIL.**

The Hardness Plan flagged channel-lock-in as a MED-priority stump (Lever 9 universe-grounded persona-channel gotcha). The prompt's framing names two natural signposts — "Chloe" (Operations Manager) and "the ops team" — both pointing at #operations (C006). The phrasing "where ... will see it" cues the agent to query Slack channels and pick the one Chloe + the ops team inhabit. A literal agent who runs `slack_get_users` on Chloe + co. and `slack_get_channel_members` on the candidate channels will resolve to C006. An agent that short-circuits on topical adjacency (NorthWind = customer-engagement, $1,200 = finance) and skips the channel-member query will mispost — which IS the designed L9 stump. The prompt deliberately does NOT name C006 (per Hardness_Plan hard-rule "phrase persona ask as 'drop the ops lesson where it belongs' rather than naming #operations"); the rephrasing in the actual prompt ("where Chloe and the ops team will see it") is functionally the same hint.

**(c) "Remind me Monday to confirm Craig got his answer" → agent sends Craig a Monday follow-up email.**

Verdict: **INTENDED_HARDNESS_NOT_CLARITY_FAIL.**

The prompt cleanly separates two threads:
- "I owe him a direct reply" → today's email to Craig (active outgoing, answering Apr 11 formal-claim question).
- "Remind me Monday to confirm Craig got his answer" → a Monday personal reminder/task for Blessing to follow up internally.

"Remind me" is an unambiguous personal-reminder verb in moveops phrasing (matches the calendar/reminder pattern from prior V3 tasks). The semantic distinction (today: send a reply; Monday: check the reply landed) is reinforced by "to confirm Craig got his answer" — confirmation of receipt, not a new outgoing. An agent that writes a Monday-scheduled email to Craig instead of a Monday reminder will fail the reminder Outcome rubric at S3 and is a clean L7 multi-write discriminator. No clarity fail at the prompt phase.

No alt-paths produce a different VALID write set. All three converge on the intended action surface.

---

## [B3] Tool-Call Density Projection

Re-projected for the prompt as written (cross-checked against Hardness_Plan):

| Component | Range | Midpoint | Verified against prompt |
|---|---|---|---|
| Base discovery (contacts.contacts on Craig + David + Catalina + Chloe, slack channel enumeration, vendor + bill lookup, Airtable schema, NorthWind CRM, Mosaic precedent context) | 6-9 | 7 | Prompt names Craig + David + Catalina + Chloe + Marcus by first name only → contact resolution needed for each |
| Lever 1 reads (KeyMove bill, Marcus's Apr 17 email, surrounding $1,200 anchors in Slack/email) | 4-6 | 5 | Prompt does not name $1,200 → agent must query QB to discover the figure |
| Lever 2 reads (Airtable schema + Emilia row pull + QB Mosaic bill + retention engagement context) | 4-6 | 5 | Prompt's "Mosaic case last quarter ... that is the shape I want us to mirror" → agent must query the precedent |
| Lever 8 reads (Craig Apr 11, Marcus Apr 17, Pam Apr 24, Catalina Apr 14, Linear NorthWind issue + comments, Julian customer-side context) | 6-9 | 7 | Prompt surfaces 4 of 5 chain links; Pam Apr 24 is the chain link the agent must derive |
| Lever 11 reads (QB ACC-6185 schema, NorthWind QB customer + invoices for credit-memo precedent, Alejandro retention model context) | 4-6 | 5 | Prompt "It does not close out the rest of this" → net-vs-gross derivation requires the read trail |
| Lever 7 write actions (email Craig, email David+Catalina, airtable update Emilia row, slack post C006, linear comment NorthWind issue, Monday reminder) + supporting reads | 11-14 | 12 | Prompt explicitly enumerates 6 writes ("Housekeeping" paragraph + Craig reply + Monday reminder) |
| Cross-service triangulation buffer | 5-8 | 6 | Multi-link chain across email + Linear + Airtable + QB |
| **TOTAL projected** | **40-58** | **47** | Matches Hardness_Plan exactly |

**Band: THIN_DENSITY (midpoint 47, range 40-58).**

Accepted per Hardness_Plan operator continuation note. The prompt as written preserves every density driver from the Hardness Plan — no scope shrinkage between HARDNESS → S1. Real platform runs traversing the L2 + L8 chains will land 50+; agents short-circuiting at L1+L9 will land lower 40s, which is the intended discrimination. The THIN band IS the expected projection on L9-anchored stumps.

**Verdict: PASS (THIN_DENSITY accepted).**

---

## [B4] Hardness Lever Preservation

| Lever | Mechanism preserved in prompt? | Evidence |
|---|---|---|
| **L1 Latching** ($1,200 + Marcus L9 frame) | YES | Prompt anchors the rider as "already weighed in on the finance side. His read is we process it as submitted because the vendor paperwork lines up with the field report, and there is no clean argument to dispute it on the vendor line. Fine. I am not going to relitigate the rider with him. That part is in his lane." — textbook L9 dismissal in domain-correct language. The $1,200 figure is not in the prompt body (intentional: agent must surface it via QB query, which is exactly the L1 latching trap — once the agent reads the bill, the figure latches). Surface count for the rider anchor IN the prompt: 5 ("the KeyMove insurance rider for the Steinway scratch", "Marcus already weighed in", "His read is we process it as submitted", "the vendor paperwork lines up", "I am not going to relitigate the rider"). All five point at the same vendor-line conclusion. Lever firing as designed. |
| **L2 Structured-DB Skip** (Airtable Emilia row + QB Mosaic precedent) | YES | "I keep thinking about how we structured the Mosaic case last quarter, where the carrier exposure was one piece and the client facing piece was a separate disposition with its own treatment, and we attached a process improvement section to the file afterward. That is the shape I want us to mirror on Emilia" — names the precedent without naming the bill_id, the credit-memo number, the vendor cap, or the Section 6 template. Agent must query QB Bills to find the Mosaic precedent and Airtable to find Emilia's row state. Pre-solving check: prompt says "that is the shape I want us to mirror" — direction, not a copy-paste of the model. PASS. |
| **L7 Multi-Write Diversification** (6 writes / 5 services + reminder) | YES | All six writes explicitly enumerated in the prompt's "Housekeeping" paragraph + earlier: (1) email Craig (Apr 11 formal-claim question), (2) email David+Catalina (operational position summary), (3) Airtable update on Emilia's relocation record, (4) Slack post (operations lesson), (5) Linear comment on the NorthWind item, (6) Monday reminder. 5 services + reminders. Service breadth distribution from Hardness_Plan preserved. |
| **L8 Multi-Link Chain** (Craig Apr 11 → Marcus Apr 17 → Pam Apr 24 → Linear retention → Catalina Apr 14) | YES (4 of 5 surfaced, 1 to derive) | Prompt explicitly surfaces 4 chain links: Craig Apr 11 ("emailed me on the 11th"), Marcus Apr 17 ("Marcus already weighed in on the finance side ... his read"), Linear NorthWind issue ("There is already a Linear item open for the wider NorthWind situation"), Catalina Apr 14 commitment ("Catalina is pulling something together on the NorthWind side"). The Pam Apr 24 link is intentionally unstated (per Hardness_Plan stump design: agent must traverse the chain via email search to find Pam's formal escalation — which is the L8 chain extension). Chain integrity preserved. |
| **L11 Net-vs-Gross** (vendor rider ≠ customer-side reimbursement) | YES | "The rider closes one ledger line. It does not close out the rest of this" — explicit gross-vs-net framing. Reinforced by "Surface what David and Catalina would need from us so they can package it cleanly" and "the operational position and what is still moving on their side." Lever firing cleanly. |

**No HARDNESS_REGRESSION. All 5 levers preserved.**

Additional Hardness-Plan hard-rule cross-check:
- NO Pam-escalation mention ✓
- NO Friday-EOD-package mention ✓
- NO $60K-account-risk mention ✓
- NO escape-valve clauses ("if anything looks off, say so plainly", "let me know if I am missing something") ✓
- NO em-dashes ✓
- NO "at least N" ✓
- NO tool names ✓
- NO service names ✓
- NO Linear issue IDs ✓
- NO Airtable record IDs ✓
- NO QB bill numbers ✓
- NO specific customer-side reimbursement $-figure ✓ (none exists in universe — L6 audit confirmed)
- Channel-lockin handling: phrasing "where Chloe and the ops team will see it" is the rephrased "drop the ops lesson where it belongs" pattern Hardness_Plan called for ✓
- ≤500 words: 332 words ✓

---

## [B6] Upstream Propagation

No upstream propagation flags. The prompt's framing implements the Hardness Plan exactly:
- Anchor A (Blessing / Operations / Emilia damage docket) — preserved.
- Stump-design intent (L1 latching + L9 authority dismissal + L11 net-vs-gross) — preserved.
- Hard-rule list — fully respected.
- 47-midpoint THIN_DENSITY — preserved with operator continuation already documented.

No `PROPAGATE TO HARDNESS` or `PROPAGATE TO S0` flags.

---

## Verdict

**GO.**

- Every applicable QC sub-dim scores 5/5 (zero NON-FAIL bands invoked, all per-task universe-verified).
- B2 returned three INTENDED_HARDNESS classifications, zero ACTUAL_CLARITY_FAIL or AMBIGUOUS_WRITE.
- B3 projected midpoint 47 — THIN_DENSITY band, accepted per Hardness_Plan operator continuation note (already documented in upstream).
- B4: all 5 levers (L1/L2/L7/L8/L11) preserved with no regression.
- B6: no PROPAGATE flags.

Operator should monitor first trajectory cycle for L8 chain traversal (Hardness_Plan flagged for re-evaluation after first run); if midpoint comes in <45 on real runs, the Hardness Plan's pre-approved rescope path (add `tblClientAccts01` NorthWind ARR-context read + Friday-EOD calendar event create) is available.

---

```json
{
  "phase": "prompt",
  "council": "B",
  "task_dir": "Tasks/34_6a42ec7493b48d5ada4571bd",
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
          "location": "prompt:para3 \"process it as submitted ... I am not going to relitigate the rider with him\"",
          "issue": "Alt-path (a): agent attempts QB rider approval despite being out of finance authority",
          "fix": "INTENDED_HARDNESS — prompt explicitly puts the rider in Marcus's lane; Council A A6 persona-scope catches any QB-write attempt",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "prompt:para5 \"Drop the Emilia lesson in Slack where Chloe and the ops team will see it\"",
          "issue": "Alt-path (b): agent posts in #customer-engagement (C002) or #finance (C005) instead of #operations (C006)",
          "fix": "INTENDED_HARDNESS — L9 universe-grounded channel-lockin stump per Hardness_Plan; phrasing hints at C006 via Chloe + ops-team signposts without naming the channel",
          "propagate_to": null
        },
        {
          "severity": "NOTE",
          "location": "prompt:para6 \"Remind me Monday to confirm Craig got his answer\"",
          "issue": "Alt-path (c): agent sends Craig a Monday-scheduled email instead of setting a personal reminder",
          "fix": "INTENDED_HARDNESS — prompt cleanly separates today's outgoing reply (\"I owe him a direct reply\") from Monday's confirmation reminder (\"to confirm Craig got his answer\")",
          "propagate_to": null
        }
      ]
    },
    "B3": {
      "status": "PASS",
      "findings": [
        {
          "severity": "NOTE",
          "location": "Hardness_Plan.md density section",
          "issue": "Midpoint 47 (THIN_DENSITY band)",
          "fix": "Accepted per Hardness_Plan operator continuation note (4 per-task justifications documented). Monitor first trajectory cycle for L8 traversal.",
          "propagate_to": null
        }
      ]
    },
    "B4": {
      "status": "PASS",
      "findings": []
    },
    "B6": {
      "status": "PASS",
      "findings": []
    }
  },
  "scores": {
    "unique_ground_truth": {"score": 5, "scheme": "1/3/5", "reason": "6-write action set converges across reasonable readings; vendor-vs-customer split is intended derivation."},
    "feasibility": {"score": 5, "scheme": "1/3/5", "reason": "Every action implementable in moveops tool surface; recipients resolvable in contacts.contacts."},
    "explicit_tool_mention": {"score": 5, "scheme": "1/5", "reason": "No tool/service names in prompt body."},
    "clarity_and_specificity": {"score": 5, "scheme": "1/3/5", "reason": "L9 framing is intended hardness; explicit 'rider closes one ledger line. It does not close out the rest of this' resolves second-reading attack."},
    "contrived_unnatural": {"score": 5, "scheme": "1/3/5", "reason": "First-person reflective Operations-Coordinator voice on Sunday after-deadline catch-up reads natural."},
    "alignment_with_todays_date": {"score": 5, "scheme": "1/3/5", "reason": "'the 11th' = Apr 11 Craig email confirmed; 'Monday' = Apr 27; 'this morning' = Apr 26 Sun. Every relative ref resolves to universe records."},
    "truthfulness": {"score": 5, "scheme": "1/3/5", "reason": "Craig Apr 11 ✓, Marcus's process-as-submitted ✓, Catalina's NorthWind track ✓, Mosaic precedent (Q1 2026) ✓, Linear NorthWind item ✓, walkup-assessment admission ✓. Zero ungrounded claims."},
    "tool_use_cross_service": {"score": 5, "scheme": "1/5", "reason": "5+ services (email × 2, airtable, slack, linear, reminders)."},
    "investigation_and_action": {"score": 5, "scheme": "1/5", "reason": "Multi-source investigation (Mosaic precedent, Emilia state, Marcus email, Craig open Q, Catalina track, Linear NorthWind) + 6 distinct writes."},
    "coherence_bolt_on": {"score": 5, "scheme": "1/5", "reason": "Every entity coheres around the Emilia operational docket. No bolt-on."},
    "persona": {"score": 5, "scheme": "1/3/5", "reason": "Relocation Coordinator voice: operational, defers finance to Marcus, defers customer-comm to David/Catalina, owns field facts."},
    "business_function": {"score": 5, "scheme": "3/5", "reason": "Operations: closing operational damage docket, owning field-facts lesson, coordinating ops position to CE track."}
  },
  "density_projection": {
    "midpoint": 47,
    "band": "THIN",
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
  "timestamp": "2026-06-30T00:00:00Z"
}
```
