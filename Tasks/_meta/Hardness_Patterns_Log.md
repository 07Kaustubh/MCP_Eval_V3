# Hardness_Patterns_Log

Append-only. One entry per task — the lever-selection-vs-actual-failure calibration record.

## Schema

```
## Entry — Tasks/<TASK_DIR> — YYYY-MM-DD

**Persona / Business function:** <X / Y>

**Selected levers (from Hardness_Plan.md):**
- Lever <n> — <name>
- ...

**Actual failures (from S4 verifier-fails analysis):**
- Rubric <id or title>: <Bucket 3 — Legitimate AF / Bucket 2 — Judge error / Bucket 1 — Rubric invalid>

**Calibration:**
- Levers that fired as predicted: <list>
- Levers that did NOT fire: <list>
- Failures that came from un-predicted sources: <list>

**Lesson for next task:** <one line>
```

## Entries

## Entry — Tasks/24_6a36e84723508b4e3f391cfc — 2026-06-21

**Persona / Business function:** Lena Park (Procurement Officer, triage/escalate only, no approve/route authority) / AP-Vendor Operations — pending-approval queue triage across brookfield + northstar_legal + acme_cloud.

**Selected levers (from Hardness_Plan.md):**
- Lever 1 — Latching / authority-figure dismissal (Daniel Jones "routing patched last sprint" C010 thread reply vs post-patch invoices still null-approver)
- Lever 2 — Structured-DB skip (Acme scope = engagement_letter_addendum doc_eb7cb30c59bd4f03 + engagement_change_order doc_2d85ac5a698745c5; Northstar = engagement_letter doc_0036f5b991574808)
- Lever 7 — Multi-write diversification (Slack C010 + Linear comment on issue_378874... + email to Daniel cc Steven + 7-day reminder)
- Lever 8 — Multi-link per-vendor chain (SAP detail + Linear issue + email escalation per worst offender)
- Lever 9 — Universe-grounded gotcha (restricted scope docs with no Lena grant + 210000 vs 219000 account split + 320/320 null approver)

**FINAL-phase confirmation (pre-trajectory):** All 5 levers confirmed firing end-to-end by the cross-artifact Final Council (prompt sentence + OE step + rubric named for each). Integrated density mid ~47 (>= 40). VERDICT PASS after one REVISE round.

**Actual failures (from S4 verifier-fails analysis):** pending — 6 trajectories not yet run.

**Calibration:**
- Levers confirmed wired end-to-end: L1, L2, L7, L8, L9.
- FINAL caught a stale-candidate holdover the per-phase councils missed: the prior 60-day-SLA worst-offender BeaconPay (VEN-033-26339) was carried into the new compound (age x outstanding $) design, where it ranks only #10 (mid-dollar, ~8th by age, zero email/Slack/Linear trail). A rubric still rewarded naming it, which would have failed correct compound-ranking agents. Fixed: deleted the rubric and re-keyed OE 5 to the true compound top-5 (CivicSquare, VaultKey, Clearpoint, PensionBridge, AssurePath).

**Lesson for next task:** When a REDO changes the ranking metric (here SLA-age -> compound age x dollars), re-derive the worst-offender set from scratch and verify each named offender is still top-N under the NEW metric before it appears in any OE or rubric. Do not carry named offenders forward from the prior candidate.

**S4 post-trajectory update — 2026-06-21:**

- 6 trajectory runs evaluated. Density avg 68.7 tool calls (+28.7 above the 40 floor), pass@1 = 0/6, avg pass rate 64.6% (per-rubric). Both gates cleared with margin. **Verdict: SHIP.**

- **Levers that fired as predicted:**
  - L8 multi-link chain — 6 systematic AF rubrics (R2, R3, R9, R10, R15, R16) all failed 5/6 runs, each requiring SAP -> Linear -> email cross-reference per vendor. Exactly the predicted mechanism. The only run that escaped (Run 2) completed the full per-vendor chain.
  - L1 latching / Learnings-L9 authority dismissal — R22 routing-fix-did-not-hold conclusion failed 3/6 runs. Agents hedged ("could be normal routing lag"; "forward-looking patch isn't disproven"; "too few to call the fix broken") in the face of the Daniel-Jones Slack reply, exactly as predicted.

- **Levers that under-fired:**
  - L2 structured-DB skip on Acme scope — predicted HIGH, failed only 1/6 runs (Run 2). Explicit prompt language naming both "addendum" and "change order" prevented the keyword-narrow miss in 5/6 runs. The lever still works but the prompt-side defense is strong; expect HIGH-confidence Pred-2-shaped predictions to land at MED-low when the prompt cites the doc-kind variants.

- **Failures from un-predicted sources:**
  - R17 Pinecrest VEN-006-193120 active vendor dispute (4/6 fail). NEW mechanism: "small-dollar long-aged outlier under compound ranking." Pinecrest's $1,040.63 keeps it under the visual top-5 cut even though its 338-day age is highest-band. The compound (age x $) framing fixed the dollar-bias problem but introduced a different attention sink. **Add as Lever 12 to the playbook.**

- **Cross-task pattern worth tracking:** L8 (multi-link chain) remains the most reliable Opus-4.8 stump on Brookfield AP/scope tasks. Agents read the first system (SAP), find the surface signal (status=pending, approver=null), and stop. They do not pull the Linear + email cross-references that carry the actual root-cause classification. Every AF rubric on this task that demanded vendor-level root-cause naming failed 5/6 runs; every AF rubric that demanded only a surface-level write action passed 6/6 runs (R1, R5, R8, R11, R24). Future tasks should keep at least one L8 chain in the load-bearing set.

**FINAL Council re-run after Truthfulness fix — 2026-06-21:**

- After applying the prompt verb swap (`was patched last sprint` -> `was supposed to land last sprint`) and the cascading wording updates in OE 15 + R7 + R22, the Final Council was re-run holistically across all 3 artifacts. **VERDICT: PASS.** Zero BLOCKERs, zero MAJORs, two MINORs (advisory only).
- All 5 selected levers (L1, L2, L7, L8, L9) confirmed firing end-to-end through prompt -> OE -> rubric chain. L9 authority-dismissal remains active despite the softer verb; R22 still requires the agent to triangulate Linear ticket status (still `todo` past 2026-05-22 due date) + post-target null-approver invoices to reach the conclusion. No shortcut path exists; second-reading ambiguity check clean.
- Two MINORs flagged for awareness, not blocking: VerityFile VEN-028-492596 (dated 2026-05-18) appears in OE 15 + R7 + R22 as a "post-target" example, but the Linear ticket's 2026-05-22 due date and Daniel's ~2026-05-19 C010 post both predate it slightly. Under strict reading only the MetroShield 2026-05-31 items are unambiguously post-target. The rubric's "for example X or Y" disjunction lets agents satisfy by citing MetroShield alone, and empirical trajectories confirm the rubric works (Run 4 cited VerityFile, judge passed it; Runs 2/3/6 cited MetroShield, judge passed). Cosmetic cleanup is available (drop VerityFile from the 3 example lists) but does not gate ship.

**Lesson for the lever catalog:** L9 authority dismissal can be operated through the PROMPT (persona's stated belief about a third party) instead of through Slack (third party's literal post). When the prompt-side placement is used, the verb tense matters for the Truthfulness gate: `was patched` (completed-action assertion that the universe contradicts) carries QC risk; `was supposed to land` (target-action assertion that the universe still allows the agent to verify) carries no QC risk and the lever fires identically. Future tasks using prompt-side L9 should default to the softer verb framing.

**Second S4 cycle (post-Truthfulness-fix trajectories) — 2026-06-21:**

After re-uploading the fixed prompt + OE + rubrics and running 6 fresh trajectories, we have an empirical comparison of the same task on the same universe with only the L9 verb tense changed.

- **Density attrition observed.** Mean total tool calls dropped from 68.7 to 60 (-8.7, still well above the 40 floor). Distribution tightened (was 13-22 / 24, now 12-20 / 24). Per-rubric avg pass rate up 4.2pp (64.6% -> 68.8%). Pass@1 still 0/6.

- **L9 yield sensitivity to verb tense:** R22 ("routing fix did not land") fail rate moved from 3/6 to 2/6 (-17pp). The softer verb made the prompt slightly less assertive but did not break the lever. Calibration: prompt-side L9 with the soft verb yields ~33% fail rate; with the hard verb (Truthfulness-risky), yields ~50%. Use the soft verb unless the difficulty target needs the harder bite AND the QC reviewer is permissive about persona-relayed assertions.

- **L8 yield IMPROVED at lower density.** R9 (Email GraniteRack) and R10 (Email TimeLedger) both went from 1/6 to **0/6** — every agent across both cycles dropped these vendors from the email body. Root cause: agents anchor email on a dollar-threshold filter ($50K+) that excludes the partner-sign-off items by amount. This is a structural stump pattern stronger than predicted. Add as confirmed: **"dollar-threshold filter blindness" — when agents are asked to surface specific named items in an email, they fall back to a generic $50K cutoff that misses sub-threshold items even when the prompt names them.**

- **L2 yield IMPROVED at lower density.** R19 (Acme scope) and R21 (restricted framing) both went from 1/6 to 3/6 fail rate. The lower-density agents skipped the multi-doc-kind search (engagement_letter vs engagement_letter_addendum vs engagement_change_order) and fell into the "no plain engagement letter so it's missing" trap. Confirms: L2 yield is sensitive to density attrition; agents who run thorough Records Vault searches avoid the trap, agents who skim fall into it.

- **L1 + L12 (small-dollar attention sink, added in prior cycle):** Pinecrest R17 stable at 3/6 across both cycles. Lever is reliable.

- **Hardness prediction hit rate this cycle:** 3/4 (improved from prior 2/3).

**Lesson for the lever catalog (consolidated across both cycles):**

| Lever | Yield (pre-fix / post-fix) | Sensitivity to | Action |
|---|---|---|---|
| L1 latching + L9 authority dismissal (R22) | 50% / 33% | prompt verb tense | use soft verb by default; switch to hard verb only for difficulty headroom |
| L2 structured-DB skip (R19, R21) | 17% / 50% | trajectory density | yields more at lower density; reliable in either regime |
| L7 multi-write diversification (R8, R11) | 100% / 100% pass | n/a | density floor only, no stumping |
| L8 multi-link chain — Slack/analytical surface (R2, R3, R15, R16) | 70-83% / 50-67% | density and surface attention | reliable across density bands |
| L8 multi-link chain — email surface (R9, R10) | 83% / 100% | dollar-threshold filter blindness | strongest AF pattern in the catalog; always include named sub-threshold items in tasks that mandate an email write |
| L12 small-dollar attention sink (R17) | 67% / 50% | compound ranking dominance | reliable when paired with a named outlier that falls below visual top-N |
