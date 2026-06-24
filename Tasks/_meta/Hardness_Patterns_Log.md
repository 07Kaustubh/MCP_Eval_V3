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

- **Task 25_6a366bc27d66eaedcae82ab4 (FINAL PASS 2026-06-22):** Levers confirmed end-to-end — L1 latching (partial-feed framing across 6 surfaces), L2 structured-DB skip primary (`ogl_subledger_feed_runs`/run_e33ed2561f2c46) + secondary (`blackline_review_notes`/rn_564e65ce0d594f), L6 near-miss entity confusion (BL-75810CD0FEE4 vs blackline_bdbbea5db590), L8 multi-link chain (5-service A→E), L9 universe-grounded gotcha (restricted + AICPA_SQMS_7Y + account 119000 + open period). Integrated density ~48-50 (above 50 strict bar).


## Entry — Tasks/25_6a366bc27d66eaedcae82ab4 — 2026-06-22 (S4 trajectory actuals)

**Persona / Business function:** George McAdam (Accounts Senior) / Accounting Operations — May Brookfield WIP-to-revenue recognition close package.

**Selected levers (from Hardness_Plan.md):**
- Lever 1 — Latching (partial-feed narrative repeated across 5+ conversational surfaces)
- Lever 2 — Structured-DB skip (ogl_subledger_feed_runs primary; blackline_review_notes secondary)
- Lever 6 — Near-miss entity confusion (BL-75810CD0FEE4 vs blackline_bdbbea5db590 doppelganger)
- Lever 8 — Multi-link chain (Andrea email → BL recon → subledger feed runs → exception + Hannah reply → JE staging)
- Lever 9 — Universe-grounded gotcha (restricted doc_42c851aed8fb40ab; AICPA_SQMS_7Y retention; account 119000 brookfield-vs-northstar-vs-acme asymmetry; open period)

Authority-dismissal layer baked through Andrea (partner) + Hannah (tax counterpart) soft-verb instructions per Learnings L9 + L24.

**Actual failures (from S4 verifier-fails analysis):**

| Rubric | Pass count | Classification | Mechanism |
|---|---|---|---|
| R4 (stage $147,825 JE) | 0/6 | Bucket 3 AF | L13 existing-output anchor trap (NEW) |
| R8 (JE business justification) | 0/6 | Bucket 3 AF | R4 cascade |
| R12 (Slack notes staged for Daniel) | 0/6 | Bucket 3 AF | R4 cascade |
| R15 (doppelganger record) | 0/6 | Bucket 3 AF | L6 near-miss entity confusion |
| R16 (update exception disposition) | 0/6 | Bucket 3 AF | NEW soft-instruction over-compliance |
| R18 (vault upload restricted + linked) | 0/6 | Bucket 3 AF | L15 tool-variant trap (NEW) + R4 cascade |
| R19 (email staged $147,825) | 0/6 | Bucket 3 AF | R4 cascade |
| R20 (exception update refs) | 0/6 | Bucket 3 AF | R16 cascade |
| R9 (Slack thread_ts) | 1/6 | partial fail | L14 decoy parent thread (NEW) |
| R6 (email surfaces feed-run) | 1/6 | partial fail | L9 communication-surface attrition |
| R7 (email tool variant + CC) | 1/6 | partial fail | tool-variant + CC drop |
| R2 (email residual parked) | 2/6 | partial fail | email-not-sent / wrong content |
| R17 (variance entry preserved) | 3/6 | partial fail | recon over-progression in R4; array-overwrite in R6 |

**Density:** 73.3 avg total tool calls (+33.3 above the 40 floor). Per-run range 64-84. **Difficulty:** pass@1 = 0/6 (well under 40%). Both gates cleared with margin. **Verdict: SHIP.**

**Calibration:**

- **Levers that fired as predicted:**
  - L6 near-miss entity confusion — R15 0/6, exactly the predicted mechanism. The doppelganger record blackline_bdbbea5db590 shares identical entity/period/account/preparer/variance/balances with BL-75810CD0FEE4 and was never surfaced.
  - L8 multi-link chain — partially fired through R6, R7, R9: agents who completed the email step often dropped the feed-run finding from the email body, used wrong tool variants, or wrote to wrong thread.
  - L9 universe-grounded gotcha + R4 cascade — restricted-classification doc trapped agents into the tool-variant trap (R18).

- **Levers that did NOT fire as predicted:**
  - L2 structured-DB skip on ogl_subledger_feed_runs — all 6 runs queried it and surfaced the contradiction in final response (R11 6/6 pass). The prompt's "If anything in what you pull together changes the read on this" escape-valve clause effectively neutralized the primary structured-DB skip lever. The lever DID fire on the secondary surface (blackline_review_notes) but only 1/6.
  - L1 latching on partial-feed narrative — did NOT cause "confidently writes wrong recognition" outcome. Instead converted into "declines to stage at all" (see L13 below).

- **Failures from un-predicted sources (NEW lever patterns):**
  - **L13 existing-output anchor trap** — R4 + R8 + R12 + R18 + R19 (5 of 8 AF rubrics cascaded from this). Agents found a previously posted JE je_53962aed96fe4b67 that superficially matches the $147,825 ask, read it as already satisfying the request, and refused to stage. This is the highest-yield novel stump observed.
  - **L14 decoy parent thread** — R9 5/6 fail. Agents posted to ts 1780230660.000000 instead of 1780248600.000000. The wrong thread exists on the same channel (C005) with overlapping keywords and a more recent timestamp; agents picked it as the "obvious" parent.
  - **Soft-instruction over-compliance** (R16 + R20) — agents read Hannah's "leave the underlying exception trail referenced as-is" as a blanket no-op on the exception record. The expected scoped read ("do not resolve, but do record the disposition") was the right model but no agent reached it.
  - **L15 tool-variant trap** (R18) — records_vault_add_document_version chosen over records_vault_upload_document because doc_42c851aed8fb40ab exists with the same title scope.

- **Hardness prediction hit rate this task:** 1/4 clean hit, 1/4 partial (mechanism inversion), 2/4 over-predicted.

**Lesson for next task:**

- **L13 (existing-output anchor trap) is now the single highest-yield Opus-4.8 stump in the catalog.** It cascaded into 5 of 8 AF rubrics on this task alone. Future Hardness_Plans should consider planting a "distractor existing artifact" (JE / doc / message / thread) that superficially matches the requested write but lacks one or two rubric-tested fields (per-line schedule, business justification, classification, related_resource_id, routing target). The agent's instinct to "not double-book" or "not duplicate work" is reliable, and the rubric can be built around the gap between the existing distractor and the spec'd write.

- **L14 (decoy parent thread) is a reliable secondary stump for Slack write rubrics.** When the canonical thread sits in a busy channel, plant another overlapping-topic thread with a similar or more-recent ts and require the canonical one in the OE. Yields ~80%+ fail rate on the thread_ts check.

- **L15 (tool-variant trap) is a clean Records Vault stump.** Plant a similar restricted doc and require a fresh upload tied to a new related_resource_id. Agents default to version-bump ~100% of the time.

- **Escape-valve prompt clauses neutralize structured-DB skip.** A prompt sentence like "If anything in what you pull together changes the read on this before I take it to Daniel, say so plainly" directly invites the agent to surface contradictions; the primary structured-DB skip lever does not fire. Future tasks that need L2 to fire should AVOID such clauses, or accept that L2 yield will collapse on the load-bearing surface.

- **Authority-instruction soft-verb tense matters at write granularity, not just truthfulness gates.** "Leave referenced as-is" got over-complied with (0/6 update wrote the exception). For future tasks where a soft instruction needs the agent to take a scoped action, the instruction must be more precise ("update the exception with the disposition but do not resolve it") or the authority figure must implicitly endorse the scoped write elsewhere. Otherwise expect 0/6 on the related rubric.

**Cross-task pattern reinforcement (vs Tasks/24):** L8 multi-link chain remains highly effective. R6 + R7 + R9 (the communication-write chain) failed 5/6 each, exactly mirroring the R2 + R3 + R9 + R10 pattern from Tasks/24. Agents reliably complete the analytical chain (R11, R14, R13 all 6/6 or 5/6) but drop the corresponding write to the communication surface. **Lesson:** if a task includes both an analytical surface (memo / response) and a communication surface (Slack / email) covering the same finding, the communication surface will fail 80%+ even when the analytical surface passes. Plant rubrics on the communication surface to harvest the asymmetry.

- **Task 26 (6a390e724c34487b95645dcc)** — FINAL PASS. Levers selected and confirmed end-to-end: L1 (Latching), L2 (Structured-DB skip), L8 (Multi-link chain), L9 (Universe-grounded gotcha), L10 (Reversal/supersession via L25 anchor). Density projection 44-55 (midpoint ~50). 23/23 outcome rubrics, 0 process. 0 BLOCKER / 0 MAJOR / 3 MINOR (all non-mandatory).


## Entry — Tasks/26_6a390e724c34487b95645dcc — 2026-06-22

**Density:** 79.8 avg total tool calls (+39.8 above the 40 floor). Per-run range 67–98. **Difficulty:** pass@1 = 0/6 (0% — well under 40%). Both gates cleared with margin. **Verdict: SHIP.**

**Calibration:**

- **Levers that fired as predicted:**
  - L9 + L27 (authority dismissal + soft-instruction over-compliance) — R11 + R22 both 0/6, exactly the predicted mechanism. The persona-relayed "Jones and I had landed on dismissing under materiality" dominated the decision in every run despite the BlackLine record's documented proposed_resolution. Highest-yield clean prediction this task.
  - L25 (existing-output anchor / reversal-supersession) — R21 0/6 on the doc_8f821bbad10c4eb4 "Signed/E-Filed" stub. No run discovered the 107-byte placeholder via the standard records_vault_list_documents path scoped to kind='tax_return'. The L25 anchor fired hardest as a RECOGNITION gap, not as a write-refusal gap (see mechanism inversion below).
  - L8 (multi-link chain) — fired through R1 → R2 → R7 → R8 → R17 cascade. Agents who tripped the late_post_authorization_id parameter contract (L17 below) cascaded the failure through every downstream confirmation surface.

- **Levers that did NOT fire as predicted:**
  - L4 (search-result-cap eviction) — predicted to bury the scen_001 dismissal chain under 60+ in-flight mentions of exc_151b0bee7e374e. Actual: 5/6 agents found the James Randall + Matthew Li reply pair via direct email_search scoped to the exception id keyword. The eviction set shared the same keyword as the canonical pair, so the search cap did not evict the authority pair. **Conclusion:** L4 needs the canonical evidence to NOT carry the keyword the eviction set carries; otherwise direct grep beats the cap.
  - L13 first-framing (figure quoting) — predicted to make agents copy $4,820.30 verbatim without verification. Actual: all six quoted the figure correctly, but the lever fired on the VERIFICATION DEPTH step instead (R19 split 3/6 — half traced 230000+103000 and confirmed support, half traced 230000 alone and concluded "not supported"). The L11 net-vs-gross lever lives at the verification step, not the quoting step.

- **NEW lever patterns (failures from un-predicted sources):**
  - **L16 tool-enum specificity drift** — when a tool's enum has a "support" / "specific-purpose" variant that lexically matches the noun in the prompt ("support memo" → kind='journal_entry_support'), agents pick the more-specific variant over the canonical generic ('memo') specified by convention. **R3 0/6 on this task** (every successful upload used 'journal_entry_support'). Cascades to memo content rubrics because the wrong kind means the memo does not appear in the canonical lookup. To exploit: define a tool enum with a "support" variant adjacent to the canonical generic, and write the rubric on the generic. Yield: ~100% on the kind check.
  - **L17 free-text shelter** — agents satisfy a structured-parameter binding requirement in narrative free-text fields (business_justification, body, content) rather than as the parameter itself, even when the parameter is in the tool spec. **R2 0/6 on this task** (every JE create call put email_scen_068 in business_justification but omitted late_post_authorization_id). The PERIOD_CLOSED tool errors in 3/6 runs confirmed the parameter was the gate. Cascades through every downstream "JE is posted" rubric (R1, R7, R8, R17). To exploit: require a structured parameter binding that the tool spec gates on (late_post_authorization_id, related_resource_id, parent_thread_ts) and is also semantically capturable in a free-text field. Yield: ~100% on the parameter check, plus full cascade.
  - **L18 two-step write reduction** — when a service exposes both a "create with description" call and a "create comment / version / annotation" follow-on, agents collapse the two-step workflow into the single create call with the comment content baked into the description / body. **R14 + R15 0/6 on this task** (Run 5 opened CAO-3116 with follow-up content in the issue description but never called linear_create_comment). The R15 cascade is automatic because the comment vehicle is absent. To exploit: write OE and rubric pairs that require the second step (linear_create_comment, records_vault_add_document_version on top of upload, slack_conversations_add_reaction after a post). Yield: ~80% on the second-step check.

- **Hardness prediction hit rate this task:** 2/4 clean (Pred 1, Pred 2). 1/4 confirmed with mechanism refinement (Pred 3 fires on verification depth, not figure quoting). 1/4 over-predicted (Pred 4 — L4 neutralized by shared search keyword).

**Lesson for next task:**

- **L17 (free-text shelter) is the single highest-yield novel stump observed on this task** and the dominant Opus-4.8 cascade trigger. Five of fourteen AF rubrics (R1, R2, R7, R8, R17) all collapse to a single parameter-contract failure on late_post_authorization_id. Future Hardness_Plans should consider planting a structured-parameter requirement that is also lexically capturable in a free-text adjacent field, with the tool spec gating on the parameter. The agent's instinct to "explain in narrative" beats the agent's instinct to "use the documented parameter slot" with very high reliability.

- **L16 (tool-enum specificity drift) is the clean Records Vault / similar-enum stump.** Plant a "specific-purpose" enum variant adjacent to the canonical generic and require the generic. Combine with a similar related_resource_type / classification trap for cascading effect.

- **L18 (two-step write reduction) is the clean Linear / multi-step write stump.** When the running-record convention requires a create-then-comment two-step (or upload-then-add-version, etc.), agents collapse to a single call ~80%+ of the time. Plant the second-step rubric explicitly.

- **L4 (search-result-cap eviction) requires the canonical evidence to NOT carry the searchable keyword the eviction set carries.** If the canonical pair and the eviction set both index on the same exception id / keyword, agents grep directly on the keyword and bypass the cap. To make L4 fire, vary the canonical evidence's searchable terms so direct grep misses it.

- **L9 + L27 (authority-relayed misinstruction + documented-control override) remains the strongest persona stump in the catalog.** R11 + R22 both 0/6 on this task, matching the dismissal-vs-reclass mechanism predicted exactly. The authority-relayed framing dominates even when the BlackLine record explicitly shows the override. This combo is now a reliable repeat-pattern for persona-relayed misinstruction tasks.

- **L25 (existing-output anchor) fires harder as a RECOGNITION gap than as a write-refusal gap on Opus-4.8.** R21 0/6 on doc_8f821bbad10c4eb4. Agents did not refuse to write — they tried to write and tripped the parameter contract (L17). Future predictions should split L25 into two sub-mechanisms: (a) L25-recognition (stub-discovery rubrics, high yield), (b) L25-refusal (write-skip rubrics, medium yield on Opus-4.8 — easier to overcome than predicted).

**Cross-task pattern reinforcement (vs Task 25):** L13 existing-output anchor / Task 25's "previously posted JE je_53962aed96fe4b67" pattern morphed into a different mechanism here. On Task 25 the anchor caused write-refusal (0/6 stage); on Task 26 the anchor caused recognition-skip (0/6 stub discovery) but agents still attempted the write and tripped L17. Pattern: **the same existing-output anchor mechanism produces different downstream cascades depending on whether the existing artifact is a NEAR-MATCH of the requested write (Task 25, refusal) versus a FORWARD-LOOKING STUB that does not lexically match the request (Task 26, missed recognition).** For future tasks: choose the anchor type intentionally to drive either refusal or recognition-skip.

- **Task 26 (6a390e724c34487b95645dcc)** — S4 PASS. 14 AF rubrics, 0 Bucket 1, 0 Bucket 2. AF justifications all clean under voice gate. Density 79.8 avg, pass@1 = 0/6. **SHIP.**

- **Task 27 (6a39fd19048f9213281ec7b)** — FINAL PASS. Confirmed levers end-to-end: **P1 (latching, 3-service: Slack thread 1780147500.000000 + Blue↔Daniel email + Blue↔Ryan messaging) + P2 (structured-DB skip via blackline_evidence → records_vault double-chase on evid_6cbb5c1605904b/_6969ca2fd0a345 → doc_01b7c6e1cbe94529/_b3633a2899a04e9e mislabel) + P7 (4 writes: vault + Slack thread reply + George email + reminder) + P8 (load-bearing multi-link precedent dig: George's FP-2025-11/$42/feed-drop claim → blackline_list_exceptions filtered brookfield/102000 → exc_d8fc13aa2cc742 in FP-2025-12, unrecorded_invoice, -$617.63, resolution_summary "Corrective JE posted", related_recon BL-782A2EC69343) + P9 (USD-cash → no FX revaluation principle) + L9-overlay (5-way authority alignment: Ryan/George/Hannah/Daniel/Blue all on accept-timing, demonstrably wrong vs records)**. Density projected 44, baseline trajectory was 53. Zero answer-leakage in the prompt or any artifact the agent reads (correct precedent atoms appear only in the universe records the agent must dig for). 24 outcome / 0 process rubrics, all four-pillar refutation atomized across vault + email + final response. **Cleared for platform upload.**
