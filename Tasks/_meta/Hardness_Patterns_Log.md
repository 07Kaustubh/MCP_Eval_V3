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

## Task 30 (6a3de5194c34125ef86fb36f) — calibration delta

**Single-lever single-pivot task (Acme Cloud AML close-out).** Three levers designed in the corrected materialization; only one fired.

- **Lever 1 (Marina-as-CDD-coordinator role attribution in memo body): CONFIRMED at 4/6 fail rate.** This is the persona-as-coordinator-via-implicit-framing pattern. The prompt names "I coordinated the CDD package through to clearance with Anita and Steven" but the rubric expects the disposition memo body to record her active coordination role inside the clearance chain, not the memo header authorship. 4/6 runs defaulted to "Prepared by: Marina Soko, Compliance Officer"; 2/6 used "Compliance coordination: Marina Soko" between the analyst pass and the supervisory sign-off. Pinning explicit pass/fail examples into the rubric evidence ("Pass examples: 'Marina Soko (CDD coordinator)', 'CDD package routed by Marina'. Fail examples: 'Prepared by Marina Soko', 'Author: Marina Soko'") was load-bearing — without those pinned examples, grader drift toward the lenient reading is likely. **Pattern remains in the catalog; pin pass/fail examples by default.**

- **Lever 2 (JE id verbatim in email subject): OVER-PREDICTED.** The prompt re-frame "drop Matthew and Steven a quick email tagging the JE in the subject so they can correlate it against the original alert" was direct enough that every run included the JE id verbatim. **Conclusion:** a JE-id-in-subject lever needs the JE id to surface only as a derivable atom from records the agent reads, not as a "tag the JE in the subject" cue in the prompt. With the cue present, the lever neutralizes.

- **Lever 3 (precedent retrieval via records_vault_download_document_content): CONFOUNDED by universe-side `IMG.VERSION_NOT_FOUND` errors.** Every run got the error on both precedent doc IDs across every actor_role tested. The companion content-reference rubric still passed 6/6 because agents discovered the precedent docs via `records_vault_list_documents` and cited them by title/doc_id inside the upload anyway. **Pattern adjustment:** a rubric whose evidence text requires `returning a successful response` from a tool is fragile to universe-side data defects. Prefer "the tool was invoked against the named target" framing unless a pre-platform smoke test confirms the tool returns content for the target actor_role on every per-task universe.

**NEW lever pattern (no new entries this task):** the Marina coordination lever is a refinement of the existing persona-relayed-misinstruction family — specifically, "persona-as-coordinator framing implicit in the prompt cue, with the rubric expecting active-role attribution in the artifact body and rejecting passive authorship credit." Not a new L-letter; treat as a calibration data point on the persona-attribution sub-family.

**Hardness prediction hit rate this task:** 1/3 clean (Pred 1). 1/3 over-predicted (Pred 2 neutralized by explicit prompt cue). 1/3 confounded by universe defect (Pred 3 — universe data prevents the tool path from succeeding).

**Lesson for next task:**

- **Persona-as-coordinator with implicit framing remains a reliable Opus 4.8 stump at ~67% fail rate** when the rubric evidence pins pass/fail examples. Without the pinned examples, expect grader drift toward lenient reading + the lever yield collapsing.
- **A prompt cue that directly instructs the agent to include a derived atom (JE id, amount, doc id) in a downstream artifact neutralizes that atom as a hardness lever.** Either make the cue oblique (the agent must infer the atom is required) or rely on a different lever entirely.
- **Pre-platform smoke test mandate for tool-success rubrics:** before shipping a rubric whose evidence text requires `returning a successful response`, dry-run the tool call manually against the target record with the actor_role the agent is most likely to pass. If the response is an error, either widen the rubric evidence to "tool invoked against the named target" or change the lever.
- **Density observation:** projected midpoint 45-50, measured 47.2 avg. Three of six runs sat above 45; three sat at 39-43. The 40 floor held, but the 50+ design target was missed. The corrected materialization's Lever 3 was designed to lift density via cross-memo precedent retrieval — but because the tool returns errors universally, agents bailed on follow-up retrieval calls after two tries, neutralizing the density lift the lever was supposed to provide. **Pattern:** a hardness lever planted for density that depends on a broken tool path collapses both the lever AND the density it was supposed to drive.


## Entry — Tasks/30_6a3de5194c34125ef86fb36f — 2026-06-27

**Persona / Business function:** Marina Soko (Compliance Officer) / Compliance & Internal Controls

**Selected levers (from `_aux/Council_Reports/REVIEW_hardness.md` + changes.md Rows 6 / 8 / 12 — REVIEW-flow task):**
- Lever 1 — Marina-as-CDD-coordinator memo-content rubric (#13), pinned with explicit pass/fail evidence examples (Row 6)
- Lever 2 — Email-subject-JE-id rubric (#5), re-framed with explicit prompt nudge "tagging the JE in the subject so they can correlate it against the original alert" (Row 8)
- Lever 3 — Memo precedent linkage via BO Refresh + AML Risk Assessment retrieval and citation (Row 12; added 2 new outcome rubrics for download + memo content reference)

**Actual failures (from `_aux/Council_Reports/S4_verdict.md`):**
- Marina coordinator role rubric (#13): Bucket 3 — Legitimate AF, 4 of 6 runs fail
- Email-subject-JE-id rubric (#5): no fail
- Memo precedent linkage rubrics: no fail
- All 23 other rubrics: no fail

**Calibration:**
- Levers that fired as predicted: Lever 1 (Marina coordinator)
- Levers that did NOT fire: Lever 2 (email-subject-JE-id), Lever 3 (precedent linkage)
- Failures that came from un-predicted sources: none

**Lesson for next task:** Pinning pass/fail evidence examples on a single high-confidence role-collapse rubric is enough to carry a task's difficulty bar — the other two levers added for diversification served density but did not contribute to pass@1 (density 47.2 from 43.2; pass@1 0.333 from 0.167, but the lift in failure rate came almost entirely from the same single rubric tripping fewer agents post-fix). For future tasks with thin work surface, prioritize ONE well-pinned role-collapse / chain-completeness rubric over THREE shallow content-anchor rubrics.


## Correction — Tasks/30_6a3de5194c34125ef86fb36f — 2026-06-27

The prior entry above was written against an earlier verifier-fails paste. Platform regenerated the verifier output and the fresh matrix changes Lever 3 calibration.

**Revised actual failures (from refreshed `_aux/Council_Reports/S4_verdict.md`):**
- Marina coordinator rubric (#13): Bucket 3 AF, 4/6 fail — unchanged
- Email-subject-JE-id (#5): no fail — unchanged
- Memo precedent linkage:
  - Precedent retrieval rubric (#25): Bucket 1 — platform data-state bug (`IMG.VERSION_NOT_FOUND` despite metadata `current_version: 1`). 2/6 strict-judge fail, 0/6 lenient-judge fail. Bucket 2 also logged for grader inconsistency.
  - Memo references precedent (#26): Bucket 3 AF, 1/6 fail (R2)
- All 23 other rubrics: no fail

**Revised calibration:**
- Lever 1 (Marina coordinator): fired as predicted — 4/6 fail rate
- Lever 2 (email-subject-JE-id): did NOT fire — every agent surfaced the JE id naturally
- Lever 3 (precedent linkage): partially fired but confounded by platform bug on rubric #25; only the memo-content half (#26) produced a legitimate AF, and only at 1/6

**Revised lesson:** When a lever depends on the platform serving content for a seeded Records Vault document, the lever is brittle — pin a smoke-test against `records_vault_download_document_content` during S0/Universe verification before shipping. The metadata layer reporting `current_version: 1` is not sufficient evidence that the content endpoint will serve it. This is now the second time we've seen lever-platform coupling defects masked as model failures — promote to a default S0 check next CB cycle.


## Tasks/31_6a3f7eecacba1ccbe57db14d — 2026-06-27

REVIEW-flow task. No original hardness plan to calibrate against — this entry is a pattern observation from the trajectory matrix only.

**Trajectory facts:**
- pass@1: 16.7% (1/6 runs passed all 13 grading lines; Run 2 was the clean run)
- avg total tool calls: 59.8 (range 42-78); avg MCP tool calls: 41.8 — comfortably above the 40+ floor
- Distinct failing lines: 8 of 13; total failure instances: 23
- Most-failing lines (4/6 fail each): M-1 final figure, FY2025 book depreciation offset, external client circulation
- All Bucket 3 (legitimate model failure); 0 Bucket 1, 0 Bucket 2
- All-Failing-Rubrics sub-dim: 5/5 PASS (Bucket 1 ratio 0%)

**Levers that fired:**
- Section 179 / bonus depreciation tax-election inference (4/6 fail) — the dominant difficulty driver
- Per-period subledger row aggregation vs all-period substitution (4/6 fail) — paired with the figure lever
- External client signatory routing (4/6 fail) — when the contact is absent from the directory
- Workflow-completion cascade gating (3/6 fail) — when the agent decides the reconciliation has not tied
- IT-equipment asset-scope filtering by account class + in-service window (3/6 fail) — paired with the scope lever

**Levers that did NOT fire (already-pinned grading lines never failed):**
- SALT closed-period late-post gate — every run recognized FP-2025-12 was locked and staged rather than force-posting (0/6 fail)
- 530000 account-class mismatch recognition — every run flagged the authorization's "DR 530000 SALT expense" as wrong (0/6 fail)
- Premature Signed/E-Filed vault placeholder discrimination — every run flagged the same-day 107-byte doc as not real evidence of filing (0/6 fail)
- Reminder setting for e-file confirmation (0/6 fail)

**Lesson for next task:** When a reconciliation task has a quantitative key-fact response, the dominant stumping lever is consistently the model declining to make an inference that the data alone cannot fully ground (here, the Section 179 rate). Pair the inference lever with a workflow-completion cascade so a single epistemic-hedge decision cascades into multiple action fails — this multiplies the hardness signal without requiring multiple independent levers. The 5/5 All-Failing-Rubrics sub-dim score with pass@1 16.7% is what this pairing buys, and is repeatable on future quantitative-key-fact tasks.

---

## Task 34 (MoveOps — Emilia Cruz damage docket close-out) — FINAL PASS 2026-06-30

**Persona / Function:** Blessing Okafor (Relocation Coordinator) / Operations.

**Selected levers (5) — confirmed end-to-end through artifact set:**
- L1 Latching — $1,200 KeyMove rider anchored across 12+ surfaces (QB bill + 6 emails + 6 Slack messages); Marcus Thorne L9 authority-dismissal frame at `email_email_99e10a978b48` ("I do not see a clean finance argument for rejecting it as submitted").
- L2 Structured-DB skip — Airtable `tblRelocations01` Emilia row (Special Requirements multilineText extension contract) + `bill_mosaic_damage_accrual_001` precedent (vendor cap + customer credit memo + Section 6 process improvements).
- L7 Multi-write diversification — 6 writes across 5 services (email × 2, airtable_update, slack post, linear_comment, calendar reminder).
- L8 Multi-link chain — 5-link Craig Apr 11 → Marcus Apr 17 → Pam Apr 24 → linear_issue_c8cdba4408f1 → Catalina Apr 14 EOD-Friday commitment.
- L11 Net-vs-gross framing — vendor $1,200 (gross, KeyMove) ≠ net MoveOps exposure (vendor rider + customer-side credit-memo + commercial consideration per Mosaic precedent); customer-side scope owned by David/Catalina (out of Blessing's authority).

**Stump Hypotheses (4) projected as agent failure modes:**
1. [HIGH] Agent stops at "approve $1,200 rider" and never files the customer-side docket distinct from vendor disposition. Mechanism: L1 + L11.
2. [HIGH] Agent never queries Airtable Emilia row AND never queries Mosaic precedent bill. Mechanism: L2.
3. [MED] Agent posts operational lesson to C002 (customer-engagement) or C005 (finance) instead of C006 (operations). Mechanism: L26 decoy-parent / channel-misalignment.
4. [MED] Agent emails Craig but does not answer his Apr 11 open question on formal-claim-now-or-hold. Mechanism: L3 missing-reply / trailing-ask blindness.

**Density:** 47-midpoint accepted THIN_DENSITY per documented Hardness_Plan per-task justification (operator continuation on-policy; re-evaluate after first platform trajectory cycle).

**Lens 6 Bucket_1_Risk:** 9% (2/22 rubrics borderline — R7 AND-shape softened by "(or similar)" tail, R21 calendar AND-bundling per V3 reference convention). Well under 20% threshold.

**Lesson for next task:** MoveOps decoy-triple Slack channels (C002 / C005 / C006) operationalized as a clean channel-misalignment stump where persona-home channel selection discriminates an agent who follows the topical surface (customer-engagement, finance) from one who follows persona-home (operations). Pair channel-misalignment with L9 authority-dismissal on a vendor-side approval frame to produce a two-layer stump where Layer 1 latches on the wrong scope and Layer 2 lands in the wrong channel — both single-mechanism, both 50%+ historical fail rates per Learnings. The two-layer combination should reproduce reliably on future MoveOps tasks that involve a vendor-side finance-clean approval interacting with a persona-scope-restricted operational handoff.


## Tasks/34_6a42ec7493b48d5ada4571bd — S4 calibration delta — 2026-06-30

CB-flow task (MoveOps universe).

**Trajectory facts:**
- pass@1: 0% (0/6 runs passed all 22 rubrics) — within the ≤40% target
- Error runs: 0/6 — well under the 2-erroneous-runs cap
- avg total tool calls: 41.5 (range 29-56); avg MCP tool calls: 32.3 — clears the 40 floor; below the 50+ design target (THIN_DENSITY band, which the Hardness_Plan flagged as expected)
- Distinct failing rubrics: 3 of 22 (R01 reply_to_email, R03 hold-pending, R04 walkup restate to Craig)
- All-Failing rubrics (6/6 fail): R01, R03 (count 2)
- Partial-fail rubrics: R04 (2/6 fail)
- Bucket 1: 1 (R01) → channel/method lock-in
- Bucket 2: 0
- Bucket 3: 2 (R03 All-Failing + R04 Partial-Fail)
- All-Failing-Rubrics sub-dim: 3/5 NON-FAIL (Bucket 1 ratio of AF rubrics = 1/2 = 50%, sits at the band boundary)

**Hardness Plan calibration:**
- 4 preds, 0 fully confirmed, 1 partially confirmed (shape shift), 3 over-predicted.
- 2 under-predicted modes fired (tool-method lock-in on Craig reply + reverse-direction inference on Craig hold-vs-open).

**Levers that fired as legitimate stumps:**
- L8 multi-link chain partially — the Craig→Marcus→Pam→Catalina chain forced agents into action-bias on the wrong option of Craig's binary (action-bias is the L8 + L11 interaction)
- L11 net-vs-gross framing — agents treated the $1,200 KeyMove rider as the closed vendor matter and missed that the formal carrier-claim shape depends on the open client-side review (R03 failure)

**Levers that did NOT fire:**
- L1 latching — agents recognized the $1,200 vendor anchor BUT also added the customer-side disposition separately. Latching was not strong enough to suppress the customer-side handoff.
- L2 structured-DB skip — agents queried Airtable correctly; the Special Requirements multilineText pattern was followed in every run.
- L7 multi-write diversification — agents executed all 6 writes (Craig email, David/Catalina email, Slack #operations, Linear comment, Airtable update, calendar reminder) in every run. Multi-write diversification did not stump the model.

**Lesson for the lever catalog:**
- **L-binary-procedural-direction-flip** is a HIGH-confidence Opus 4.8 lever distinct from L3 (missing-reply). When a referenced inbound email asks a binary procedural question (e.g., "X now or hold pending Y"), the model answers the binary but picks the action-biased option even when the prompt elsewhere telegraphs that Y is open. The failure is structurally different from "no answer" and reliably produces 100% all-failing on the directional rubric. Pair with a customer-side-still-open framing where the inference chain has 2-3 hops to maximize fail rate.
- **L-tool-method-lock-in-on-email-reply** is NOT a clean stump lever — it conflates rubric design strictness with agent capability. When the prompt verb is ambiguous between reply and fresh send, the rubric must allow either path. Otherwise the failure is reclassifiable as Bucket 1 and lowers the All-Failing-Rubrics sub-dim score.
- **THIN_DENSITY operator-acceptance pattern reproduced.** Projected 47-midpoint and actual 41.5-midpoint differ by ~5 calls (agents under-traversed L8). Future Hardness_Plans that fall in the THIN_DENSITY band should add a density-margin patch (one additional read or write that an L8 traversal naturally surfaces) to push the projected midpoint to 50+ and absorb the ~5-call under-traversal observed here.


## Correction — Tasks/34_6a42ec7493b48d5ada4571bd — 2026-06-30 (post-R01-fix)

The prior entry was written against the pre-R01-fix verifier output. The R01 fix was applied to `7_Rubrics.json` (Craig-reply rubric loosened to "either thread reply OR fresh direct email"), the platform verifier was re-run, and the current `8_Verifier_Fails.txt` reflects post-fix grading.

**Revised trajectory facts:**
- pass@1 still 0% (0/6 runs passed all 22 rubrics)
- Error runs 0/6
- avg total tool calls 41.5 (THIN_DENSITY band)
- Distinct failing rubrics: **2 of 22** (R03 hold-pending, R04 walkup restate). R01 PASS 6/6 on the loosened criterion.
- All-Failing rubrics: **R03** (count = 1)
- Bucket 1: 0; Bucket 2: 0; Bucket 3: 2 (R03 AF + R04 partial)
- All-Failing-Rubrics sub-dim: **5/5 PASS** (Bucket 1 ratio of AF rubrics = 0/1 = 0%)

**Levers that fired as legitimate stumps (revised):**
- L11 net-vs-gross framing — agents treated the $1,200 KeyMove rider as the closed vendor matter and missed that the formal carrier-claim shape depends on the open client-side review (R03 failure). 6/6 all-fail. Confirmed as the sole legitimate AF on this task.

**Levers that did NOT fire (revised):**
- L1, L2, L7, L8 all over-predicted as in the original entry; this re-classification does not change their calibration.

**Revised lesson:** L-tool-method-lock-in-on-email-reply remains NOT a clean stump lever. The empirical proof is stronger now — when the rubric was loosened, the verifier graded the same agent behaviour as PASS in every run. This confirms the "rubric-strictness vs agent-capability" distinction. Future rubrics on email-reply where the prompt verb is ambiguous between thread-reply and fresh-send should default to the "either path" wording from the start.

**Task verdict:** SHIP. The post-fix All-Failing sub-dim score (5/5 PASS) was the explicit target of the R01 fix per the original verdict ("after the fix, the All-Failing Rubrics sub-dim moves from 3/5 to 5/5"). Target met.

- **Task 35** (`Tasks/35_6a4421ec8169e23828bb442d`, scenario_14b3ffde, keystone) — FINAL PASS 2026-07-01. Levers preserved end-to-end: §L8 multi-link chain (email + Slack + CRM), §L9 authority dismissal (Raj restore = costly, soft-verb per §L24), §L10 structured-DB skip (CRM engagements 4 workstreams), §L25 existing-output anchor / CROSS_SCENARIO_RECONCILE (Denise's 3/20 preliminary plan superseded by 4/07 portal breach + 4/07 Raj-access-audit + 4/14 Marcus Webb post-term), §L26 decoy parent thread (D_grace_robert_denise mpim vs C001/C002/C008 decoys). Density mid 54. Bucket 1 risk 5.7%.

## Entry — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01

**Persona / Business function:** Robert Calloway (Owner / Licensed Mortgage Broker) / Executive

**Selected levers (from Hardness_Plan.md):**
- Learnings §L8 — Multi-link chain (Playbook Lever 8) across email + Slack + CRM
- Learnings §L9 — Authority-dismissal (Playbook Lever 1) on Raj IT-authority framing
- Learnings §L10 — Structured-DB skip (Playbook Lever 2) on CRM engagements 472-row surface
- Learnings §L25 — Existing-output anchor / supersession (Playbook Lever 10) on Denise's 3/20 preliminary plan
- Learnings §L26 — Decoy parent thread (Playbook Lever 4) on C001/C002/C008 vs D_grace_robert_denise

**Actual failures (from S4 verifier-fails analysis):**
- R11 (leadership DM references seven files + ransomware-scope preliminary qualifier): **Bucket 1 — Rubric invalid** (bundled: two independent facts joined by "while"; 0/6 pass rate driven by rubric-design defect not model-capability defect)
- R20 Run 1 (leadership status covers 3 feeder workstreams): **Bucket 2 — Judge error** (rubric evidence authorizes "or similar phrasing"; judge applied label-strict interpretation despite agent covering all three concepts with equivalent labels — "UWM portal list" for portal breach, "confirmed Feb exports" for Raj audit, "ex-LO access" for Marcus Webb)
- R26 Run 3: **Bucket 2 — Judge inconsistency** (decision Pass, reasoning explicitly says "Score 0.0" — internal decision-reasoning contradiction)
- R2, R3, R4, R7, R8, R9, R12, R13, R14, R15, R17, R21, R27, R30, R31, R33 partial-fail 1-4/6 each: **Bucket 3 — Legitimate model failure** at the per-run atomic-rubric level. No AF justification required (not AF rubrics). Failure signatures: (a) email-vs-memo propagation gap (agent writes load-bearing content in memo but not email to counsel), (b) Run 5 §L9 polarity-flip anti-latching over-correction (agent invented "LOS fully operational" prose contradicting Raj's caveat), (c) aggregate-count-in-narrative gap (agents write workstream lists but rarely aggregate to specific counts in final response / CRM NOTE)

**Calibration:**
- Levers that fired as predicted: §L8 multi-link chain (R17 + R8 + R21 partial fails on service-propagation gaps). §L9 authority-dismissal fired with polarity twist (Run 5 opposite-direction over-correction).
- Levers under-predicted: §L10 structured-DB skip was mostly cleared by agents on this scenario; only R17 Run 2 partial miss.
- Levers over-predicted: §L25 existing-output anchor (every run cleared the 3/20 supersession signal — 100% pass on R5); §L26 decoy parent thread (every run correctly routed to D_grace_robert_denise — 100% pass on R18). Both levers were HIGH confidence in the Hardness_Plan but did not stump any run.
- Emergent difficulty not catalogued: **DM aggregate-count-plus-qualifier bundling** — short leadership DMs on reconciled-picture tasks do not naturally carry BOTH an aggregate count AND a qualifier for capable Opus agents. If a rubric wants both signals, it MUST be split into two atomic rubrics from the outset.

**Revised lesson on §L9 authority-dismissal polarity risk:** authority-dismissal lever can misfire in the reverse polarity when the agent over-corrects the authority-figure framing. Run 5's "LOS fully operational" prose is a Run-5-specific manifestation. Future S3 rubrics for authority-dismissal levers should include a truthfulness sub-check on the anti-latching side (e.g., "Agent does not overstate LOS operational state contrary to Raj's later Slack caveat"). This protects against the Run 5 failure mode without changing the primary latching lever.

**Task verdict:** Trajectory hard gates + density PASS (pass@1 = 0.0%, 0 errors, avg 59 tool calls). All-Failing Rubrics sub-dim = 1/5 FAIL (Bucket 1 ratio 100% because the sole AF rubric R11 is bundled). Fix R11 split (see `_aux/Council_Reports/S4_fixes.md`) before re-uploading. Post-fix All-Failing sub-dim would move to 5/5 PASS.



## Correction — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01 (post-R11-split re-grade)

The prior Task 35 entry was written against the pre-fix 35-rubric grading pass. The R11 split has been applied to `7_Rubrics.json` (35 -> 36 rubrics), the platform verifier was re-run, and the current `8_Verifier_Fails.txt` reflects the post-fix grading.

**Revised trajectory facts (post-fix):**
- pass@1 = 0.0 (0/6 runs). Error runs 0/6. Density avg 59 (>= 50 design target).
- Distinct failing rubrics: 22 of 36. AF rubrics: 3 (indices 5, 14, 33). Bucket 1: 0. Bucket 2: 0. Bucket 3 AF: 3. Bucket 3 partial: 19.
- All-Failing-Rubrics sub-dim: **5/5 PASS** (0/3 = 0% Bucket 1 ratio).

**Levers that fired as legitimate stumps (revised):**
- §L8 Multi-link chain (email + Slack + CRM): confirmed strong. Index 5 (memo-to-email propagation on Raj's LOS caveat) is a 6/6 AF; indices 8, 9, 10, 18, 19, 24 partial-fail on the same service-boundary propagation shape.
- §L9 Authority-dismissal with polarity twist: Run 5 over-corrected to "LOS fully operational" contradicting Raj's later caveat, cascading fails on indices 12/17/22/28/30. Anti-latching failure mirror confirmed on this pass.
- Emergent aggregate-count-in-narrative lever: confirmed as STRONG stump on two independent surfaces. Leadership DM index 14 + final response index 33 both 6/6 AF with identical signature (agent enumerates constituent files by workstream, never aggregates to the seven-file total). Catalog this as a new stump lever for future Hardness_Plans.

**Levers that did NOT fire (unchanged from pre-fix pass):**
- §L25 Existing-output anchor (3/20 supersession): every run cleared the supersession signal (index 32 = 6/6 pass). Over-predicted on this task.
- §L26 Decoy parent thread (leadership DM channel routing): every run correctly routed to D_grace_robert_denise (index 1 = 6/6 pass). Over-predicted on this task.

**Revised lesson on bundled-vs-atomic rubric authoring for aggregate-count levers:** the pre-fix pass had R11 as a single bundled rubric (aggregate count + preliminary qualifier); the split converted the 100%-fail into two atomic rubrics (index 14 aggregate count 6/6 AF, index 15 preliminary qualifier 3/6 partial). The bundled version masked the true failure signature — both signals were failing but the bundling reported it as a single AF entry. Under the atomic split, index 14 emerged as a legitimate Bucket 3 AF (aggregate-count-in-DM lever), and index 15 dropped from 6/6 to 3/6 partial (preliminary-qualifier is easier than aggregation for capable agents to carry in a short DM). **Lesson: any lever that combines "quantitative aggregate + qualitative qualifier" MUST be authored as two atomic rubrics from the outset** — the bundled version fails the All-Failing sub-dim under strict interpretation and masks the granular difficulty signal.

**Task verdict (post-fix):** SHIP. Same trajectory levers as pre-fix pass. All-Failing-Rubrics sub-dim moved from 1/5 FAIL to 5/5 PASS after R11 split. Confirms the pre-fix verdict's action-items prediction exactly.


## Correction Round 2 — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01 (Marcus-to-Evan universe-attribution fix + new stump lever)

Round 1 (post-R11-split re-grade) established the trajectory + AF classification. Round 2 surfaced a systemic universe-attribution defect in rubrics R10 / R13 / R18 (Marcus Webb -> Evan Mercer). Surgical fix applied, validator PASS.

**New stump lever catalogued: L-persona-attribution-landmine (multi-departure scenarios).**

**Mechanism:** in a scenario with TWO or more concurrent departed-employee narratives (e.g., a highly-salient recent resignation + solicitation story alongside a distinct less-salient post-termination LOS access story), the CRM engagement chain often uses generic pronoun-labels ("Former employee", "the former LO") without naming the person, while the parallel Slack thread carries the explicit name. Both agents AND rubric authors systematically attach the salient recent-departure name to the generic CRM label, ignoring the Slack thread's authoritative naming.

**Failure signature at agent-run level:** 6/6 mis-attribution. Agents write "Marcus Webb post-term access" when universe says Evan Mercer. Judges accept because the rubric ALSO uses the wrong name — internal consistency masks the universe error.

**Failure signature at pipeline level:** S3 grounding + S3 adversarial + AUDIT_rubrics + FINAL_council all locked onto the wrong name. Every phase confirmed "Marcus Webb" without cross-checking the Slack thread. Pipeline miss propagates end-to-end.

**Design guidance for future Hardness_Plans:**
- If a scenario has multiple concurrent departed-employee narratives, catalog this as an intentional persona-attribution lever with the expected agent failure = wrong-name attribution on the less-salient departure.
- Rubric authoring for such scenarios MUST cross-check the CRM chain against parallel Slack threads for explicit naming. A generic CRM "Former employee" label is NOT sufficient grounding — require Slack-thread confirmation of the person's identity.
- S3 grounding pass MUST verify persona attribution by grepping the universe for the person's name alongside the workstream keywords (e.g., "Evan" + "post-term" or "Evan Mercer" + "LOS access"). If the salient candidate name (e.g., "Marcus") does NOT co-occur with the workstream keywords in the universe, the attribution is likely wrong.

**Empirical verifier note:** the fix does not change agent run pass/fail rates on R10 / R13 / R18 (all three were partial-fails 5/6, 1/6, 3/6 respectively) because judges accepted the label paraphrase equivalence. But the fix clears 3 Major "reverse-groundedness" defects from the Overall Rubric Quality sub-dim, moving that sub-dim from a projected Fail (>= 3 Major) to a projected 5/5 PASS.

**Task verdict (post-both-fixes):** SHIP after empirical re-verification of the fixed 36-rubric set. All 4 QC sub-dims project to 5/5 PASS.


## Round 3 empirical re-verification — Tasks/35_6a4421ec8169e23828bb442d — 2026-07-01

Post-Round-2 platform re-grade at 21:56 arrived. Lever hit rate is unchanged from Round 1 (3/5 = 60%). Fresh actuals:

- **§L8 Multi-link chain (email + Slack + CRM):** HIT (strong; reinforced). R5 4/6 fail on email-covers-Raj-caveat, R22 3/6 fail on memo-covers-Raj-caveat, R30 3/6 fail on final-response-covers-Raj-caveat. Same load-bearing caveat is dropped across the propagation chain in 4 / 3 / 3 runs respectively.
- **§L9 Authority-dismissal (Raj IT-authority framing):** HIT (with polarity twist). Runs 1/3/4/6 held the line. Run 5 flipped polarity to "LOS fully operational" and cascaded R4/R17/R22/R25/R28/R30/R35 fails. §L9 remains high-signal.
- **§L10 Structured-DB skip (CRM engagements 472-row surface):** HIT (partial). R18 partial fail Run 2 + Run 6 — agent folds Raj into main narrative rather than naming 4/07 Raj-access-audit as a distinct CRM engagement row.
- **§L25 Existing-output anchor (3/20 preliminary plan):** OVER-PREDICTED. R32 = 6/6 pass fresh. Every run correctly reported the plan was superseded.
- **§L26 Decoy parent thread (Slack channel routing):** OVER-PREDICTED. R1 = 6/6 pass fresh. Every run correctly routed to D_grace_robert_denise.

**Emergent lever confirmed: L-aggregate-count-narrative.** R14 4/6 fail + R33 3/6 fail on the fresh re-grade. Independent surfaces (leadership DM + final response) both fail with the same signature: agents enumerate constituent files per workstream but do not aggregate to the reconciled 7-file count. Legitimate stump lever for capable Opus 4.8 agents.

**Emergent lever confirmed: L-persona-attribution-landmine.** R10 4/6 fail on the fresh re-grade despite Round 2 relabeling the workstream owner to Evan Mercer. Agents substitute LN-2026-00009 (portal-breach file) for LN-2025-00229 (correct 3rd Mercer file) or drop the enumeration entirely. The trap operates on the file-set enumeration downstream of the persona-attribution surface.

**Novel lever candidate: L-data-minimization-vs-enumeration.** Run 2 R19 fresh grading — agent explicitly wrote "Specific borrower PII intentionally omitted from this log entry (data minimization)" in the CRM NOTE, conflicting with the rubric's enumeration expectation. Worth cataloging for future tasks where a durable log surface (CRM NOTE / audit log / compliance record) requires PII enumeration — a compliance-trained agent may choose minimization over rubric compliance.

**Novel lever candidate: L-polarity-flip-cascade.** Run 5 alone contributed 7 fails via a single reasoning slip ("LOS fully operational" contradicting Raj's caveat). This cascaded across email + CRM + memo + final response surfaces. Worth cataloging as a per-run failure mode where a single state-read error dominates the run's fail profile.

**Task verdict (post-Round-3 empirical re-verification):** SHIP. All 4 QC sub-dims 5/5 PASS. Trajectory hard gates + density PASS. Fresh re-grade confirmed the Round 2 rubric-quality fix moved Overall Rubric Quality sub-dim to 5/5 PASS empirically (not just projected).

- **Task 36 (MoveOps · Julian Brooks · Customer Engagement · 2026-07-02):** FINAL PASS on first pass. Levers L25 (existing-output anchor — Julian's 4/23 apology-plus-promise emails to Simone + Marcus + Carmen; Carmen no-reply verified) + L9 (authority self-anchor — Julian's own 4/22 C007 "just send him a quick acknowledgment" + Airtable Status=In Progress correct-observation-wrong-conclusion) + L26 (decoy parent thread — 4 competing Slack parents, canonical Mina C002 audit ts 1776997200) + L2 (Airtable Special Requirements silent on unit type + QB invoice INV-2026-0308 $11,350 off-domain for Customer Support) + emergent L8 (three-service reduction: email + Airtable + QB) all preserved end-to-end. Density midpoint 50 (range 42-59). MAJOR-1 logged for author-side: prompt leaks "Indianapolis" + "the eleventh" in persona-voice recall — future tasks should phrase checkpoint recall as "carrier transfer hub" without city+date verbatim.

## S4 empirical calibration — Task 36 — 2026-07-02

Fresh platform re-grade: pass@1 = 0.0% (6/6 runs failed at least one rubric), avg 52 tool calls (PASS 50+ design target), 5 always-failing rubrics all Bucket 3, All-Failing Rubrics sub-dim 5/5 PASS. Lever hit rate 3/4 primary + 1 emergent.

- **L25 existing-output anchor:** HIT. R9 (Simone email escalated to Carmen with same-day) failed 4/6; R11 (dollar swing pending) failed 2/6; R12 (Mina summary 4-action enumeration) failed 1/6; R10 (Marcus email April 11 date) failed 3/6. All four track the apology-template paraphrase pattern predicted by H1.
- **L9 authority self-anchor + L14 correct-observation-wrong-conclusion:** PARTIAL. Airtable updates landed correctly in every run; Special Requirements field was populated with recovery detail; agents did not stop at Status=In Progress as predicted. L9 did not carry failures alone.
- **L26 decoy parent thread (Slack):** HIT strong. 4/6 runs posted to C006 / 1777001700 instead of C002 / 1776997200 as predicted. Runs 1 and 5 correctly attached to Mina's audit thread.
- **L4 Marcus 3-way name collision:** MISS. 0/6 runs addressed the wrong Marcus. Universe-provided email brought clean disambiguation.

**Emergent lever confirmed: L-multi-record-target-selection (Linear-analog of L26).** 5 rubrics × 6 runs = 30/53 = 57% of all fails traced to agents picking Mina's audit issue `c16357d188c6` instead of Chloe's ops-gaps issue `f85be674c9b8`. Both issues are BrightLoop-scoped, both target the same batch, both are surfaced by the same OE exploration. The trigger is a persona-attention bias in the prompt: Mina named 8 times, Chloe named 0 times (only "Chloe's issue" implicit via OE). Agents anchor on the heavily-named persona's record even after directly reading the correct target during exploration. Distinct from L26 (which operates on a proliferation of candidate parents); L-multi-record-target-selection operates on prompt-persona attention bias when two candidate records exist. Worth cataloguing for future tasks with multi-record target ambiguity.

**Author-side finding for future MoveOps tasks:** when the prompt heavily anchors one persona and the write target is owned by a different persona, either (a) name the correct owner in the persona voice explicitly, or (b) plant enough content-distinguishing signal in each candidate record that the wrong choice becomes obviously off-topic. The "operational" adjective alone did not disambiguate — both issues are operational in nature.

## S4 empirical calibration — Task 37 — 2026-07-02

**Task 37 (Keystone Mortgage · Sofia Reyes · processor pipeline review).** Fresh 6-run trajectory grade: pass@1 = 16.7% (1/6 runs pass all 30 rubrics), avg 216.8 total tool calls (well above 50 design target), 0 error runs. 13 fail-instances across 8 unique failing rubrics; 0 fully AF rubrics. All-Failing Rubrics sub-dim 5/5 PASS (Bucket 1 ratio = 0%). One Bucket 2 judge error identified (Rubric H Run 4: verifier grepped `activity_create` instead of `mortgage_los_add_activity`). All other 12 fails are Bucket 3.

**Root-cause distribution (13 fails):**
- Run-1 aged-file compression (7/13 = 54%): Run 1 alone collapsed the stale-file lock dates to relative-time phrases ("lock long expired", "all locks expired 250+ days") across 5 per-loan-officer cohort emails (Amy Chen, Keisha Williams, Marcus Webb, Natasha Okafor, James Thornton). Same run also failed the two final-response anomaly rubrics.
- Final-response depth-vs-breadth (5/13 = 38%): Runs 1, 3, 5 all failed the LN-2026-00623 premature-CTC + LN-2026-00010 max-outstanding-docs surfacing in the final response. Agents that lean on 26-file pipeline breadth miss the two anomaly loans requiring document-checklist depth. Run 3 dropped both loan numbers from the final response entirely.
- Single Run-2 email drop (1/13 = 8%): Run 2 sent Natasha Okafor's update without LN-2025-00286 entirely (covered LN-2026-00010 only).

**Hypothesis hit rate: 3 of 5 predicted (60%) + 1 under-predicted:**
- Premature-CTC anomaly on LN-2026-00623 (final response surfacing) HIT — 3/6 runs fail. Load-bearing stumping lever.
- Max-outstanding-docs anomaly on LN-2026-00010 (final response surfacing) HIT — 3/6 runs fail. Load-bearing stumping lever.
- Aged-file lock-date compression HIT — 5 of 6 per-LO cohort rubrics fail on Run 1. Reproducible Opus-4.8 failure mode on Sofia-style breadth-vs-depth tasks with 11+ stale legacy files (2024-2025 locks) in a 26-file pipeline.
- Terminated-LO surfacing (Veronica Hayes + Brian Mitchell) OVER-PREDICTED — 0 fails. Every run correctly named both departed staff. Lever is now soft on Keystone processor tasks with named departed-LO scope.
- CRM engagement creation gap OVER-PREDICTED — 0 fails. Universal Pass. Soft lever.
- UNDER-PREDICTED: single-loan drop within a per-LO update (Run 2 Natasha). This is a narrower version of the aged-file compression failure that surfaces even in an otherwise-passing run. Worth cataloging as a shortcut mode when the LO cohort is 8 people with varying loan counts.

**Novel lever candidate: L-final-response-depth-anchor.** The prompt asks Sofia to "figure out exactly what's blocking progress" AND to give per-LO updates. Agents that treat the per-LO emails as the primary output tend to surface all anomaly-relevant atoms in the per-LO channels but omit the same atoms from the concluding summary to the requesting user (Grace / Sofia's own reflection). The final response becomes a meta-recap of "I sent 8 emails" rather than a distilled anomaly list. This is distinct from breadth-vs-depth in exploration: the atoms ARE explored, they land in the per-LO emails, but they do not re-surface in the final response. Worth cataloguing for future Sofia-style multi-recipient tasks where the final response is also a graded surface. Load-bearing on Task 37 (6 of 13 fails).

**Novel lever candidate: L-aged-file-relative-time-compression.** When a per-LO cohort has both recent files (2026 locks, days-old expirations) and stale files (2024-2025 locks, 200+ day expirations), agents show a strong tendency to give exact dates for the recent files and to collapse the stale files under a single relative-time phrase like "lock long expired" or "250+ days expired". The per-LO content rubrics require exact dates for both. This surfaces on Task 37 as the highest-yield fail cluster on Run 1 alone (5 per-LO cohort rubrics fail). Worth cataloguing for future tasks where a per-LO or per-file cohort mixes recent + stale surface.

**Author-side finding for future Keystone processor-pipeline tasks:** the aged-file compression trap works when the stale-file count is ≥ 3 in a per-LO cohort and stale-file lock expirations are older than 200 days. Below that threshold, agents give per-file dates cleanly. Above 3 stale files per LO, the compression shortcut becomes attractive enough to fire even when the rubric is atomically date-required. Keep this ratio in mind when designing per-LO content rubrics.

## Entry — Tasks/38_6a5edd96beaa98710363ebb2 — 2026-07-21 (predicted)

Universe: starpm (V4). Persona: Patricia Nguyen p_010, Property Operations (rent/eviction lifecycle). Selected levers: S1 structured-DB derive (P2+P10; L10/L2/L29), S2 multi-link chain QB->Airtable->Linear->Gmail (P8; L8), S3 net-vs-gross with decoy CustomerRef entries + paid-off invoice + payment-plan credit (P11+P1; L14/L8/L13), S4 cross-property Unit-14 / three-Patricia disambiguation (P6 stacked; L4), S5 ESA-accommodation wrong-conclusion + Texas 3-day + owner-sign-off/draft-only guards (P9+P10; L9/L14). L25 existing-ledger anchor folded into S1/S3. Projected density midpoint 50.5 (range 40-61), breadth 7 services >= 5%. Actual: pending S4.


## Entry - Tasks/38_6a5edd954557325b498168d1 - 2026-07-22

Universe: StarPM. Persona: Carlos Mendez (Onsite PM, p_009), Property Operations.

Predicted levers (5, all grounded + orchestrator-verified against Universe_Split):
- L8 - Las Palmas 8D three-system readiness contradiction: Airtable [selReady] "closed out, show immediately" (stale May turn) vs [selProg] June turn (fridge swap 6/25, ready 2026-06-26) vs OPEN Linear garbage-disposal issue vs MT-2026-1271 Vacant.
- L9 - Brooke Phillips (Apartment Property Supervisor, Carlos's supervisor) soft authority dismissal ("already signed 8D off").
- L10 - Airtable-is-SoR + QuickBooks structured-DB skip: $385 Rio Bend owner pass-through lives only in QB bill 101742946163, not in Slack chatter.
- L28/L4/L11 - near-duplicate vendor cost: $385 (Rio Bend, correct) vs $285 (Unit 4B patch, PAID, dominates #vendors) vs $1,340 x2 (412 Mesquite duplicate bills, gross $2,680).
- L25 - existing-output anchor: stale [selReady] 8D record superficially satisfies "mark ready", agent refuses the real write on the active June turn record.

Density midpoint 51.5 (PASS, thin margin - needs BOTH 8D reconciliation AND Rio Bend pass-through in scope). Breadth 7 services >= 5% (PASS).

Calibration note (learning signal): the StarPM registry decoy-PDF landmine (report-laspalmas-8d-qc-inspection-2.pdf, invoice-...-287.pdf, -920.pdf, agreement-...-tanya-mitchell-2.pdf) was NOT instantiated in THIS per-task split (0 pdf tokens; Gmail carries only a has_attachments boolean). Lesson for future StarPM tasks: verify registry landmines per-task before building levers on them - they are universe-level facts, not guaranteed present in every split. Record-level duplicates (multiple tblMakeReady rows per unit, duplicate QB bills) delivered equivalent hardness here.

Actual AF rubrics Opus 4.8 failed: TBD at S4.

### Follow-up - Tasks/38_6a5edd954557325b498168d1 - 2026-07-22 (post-Oracle-review)

Correction to the entry above. An Oracle skeptical verification pass found the density projection inflated: three component ranges (base 6-9, multi-write 10-13, L10 structured-DB skip 5-8) exceeded the Reference/Hardness_Playbook.md fixed costs (5-8, 9-12, 4-7), and L25's existing-output-anchor reads double-counted L8's 8D-record reads. Honest recompute was THIN (~46-48.5), not the claimed 51.5 PASS.

Fix (runbook-preferred expansion, not a re-label): corrected all component ranges to the Playbook-fixed values, de-overlapped L25 (net 1-3), corrected L9 to the gotcha range (3-5), and ADDED a 6th grounded lever - the water-heater flooring-escalation multi-link chain (MT-2026-1211 -> MT-2026-1256 -> QB bill 258920406326 $1,340, Carlos's scripted maintenance_escalation_waterheater_leak scenario). Result: 6 levers across 3 scenario clusters (8D make-ready / Rio Bend carpet cost / Tommy's water-heater flooring), honest density midpoint 55.0 (PASS), breadth still 7 services.

Calibration lesson: sub-agent lever-cost estimates MUST be reconciled against the Playbook's fixed cost table before trusting the density sum. A projected midpoint only 1.5 above the 50 gate is a tell for inflated component ranges - recompute with the mandated ranges before declaring PASS.

## Entry — Tasks/39_6a602c8886ebb06f12354d77 — 2026-07-22 (predicted)

**Universe:** StarPM V4. **Persona:** James Bennett (p_006), Assistant Maintenance Technician — design-surface (0 scripted actions), participant in `makeready_laspalmas8d_turn`. **Business function:** Maintenance & Repairs. **Injection:** none (inject.sql comment-only stub, changelog []); scenario baked into base export.

**Scenario anchor:** Las Palmas 8D make-ready turn.

**Selected levers (5):** L10 reversal/supersession (stale 5/1 "ready/closed out" 8D row superseded by in-progress rows through 6/25 + OPS-227 disposal-seized comment 6/22) · L2 structured-DB skip (Airtable is SoR per linear team_001; MT-2026-1271 OPEN only in Airtable — Airtable is the StarPM analog of the SAP-subledger skip) · L1 latching (Slack "8D punch-list/carpet done" first-framing) · L4 search-cap eviction (61 "204B" decoy occurrences bury 6 "8D") · L3 missing reply (vendor-confirm + parts-approval sit in replies).

**Learnings cited:** L25, L10, L13, L26, L12. Reserved L9 (authority dismissal) for optional injection.

**Density (StarPM V4, per model):** projected midpoint 48.5 → PASS (>= 40). Breadth: 6 services >= 5%, 4 write surfaces → PASS.

**Actual (fill at S4):** <pending trajectories — Agent_Responses currently empty scaffolds>.
- 2026-07-23 · Task 39_6a602c8886ebb06f12354d77 (StarPM V4, Las Palmas 8D make-ready; persona James Bennett p_006) · FINAL PASS · 5 levers confirmed end-to-end: L10 supersession (stale 2026-05-01 selReady receb057 vs live June rows), L2 Airtable-SoR skip (MT-2026-1271 blank/OPEN, team_001 SoR-declaration), L1 latching (Slack C004 "8D officially cleared/ready" May chatter), L4 result-cap eviction (~122 "204B" decoys burying 6 "8D" rows + Rio Bend 214/MT-2026-1325 twin), L3 missing-reply (OPS-227 parts-approval reply chase). Per-model density ~43-48 (>=40 StarPM design). 0 BLOCKER / 0 MAJOR, Lens-6 Bucket-1 0%. 4 MINOR (base-id verified present; r5/r10/r14 phrasing ship-as-is).

### Follow-up — Tasks/39_6a602c8886ebb06f12354d77 — 2026-07-23 (S4 calibration delta)

**S4 dual-model actuals (Opus 6 + Gemini 6, 0 errors, pass@1 0% both):** STRONG PASS. 0 Bucket-1, 0 Bucket-2, all failing rubrics Bucket-3 (legit). All-Failing sub-dim 5/5 (Bucket-1 ratio 0%).

Lever yield (real): all 5 selected mechanisms fired. Highest real yield came from levers manifesting on a DIFFERENT surface than the plan predicted:
- L10 supersession + L3 comment-override (OPS-227 title "jam" vs 6/22 "seized/replace" comment) → Opus disposal cluster fails runs 1,3 (6 rubrics at once).
- Intra-unit record disambiguation (3 make-ready rows; only stale selReady receb057 needs the fix) → Gemini R2/R3/R4 fail 5/6. This is the L4/L6 near-miss mechanism, but INTRA-unit (three rows for one unit) rather than the predicted cross-unit 8D-vs-214 swarm. Lesson: intra-unit record duplicates are a stronger, more reliable stump than cross-unit decoys for "correct the stale record" tasks.
- L2 Airtable-SoR skip (MT-2026-1271 blank completion date) → R14 fails Opus 2/6, Gemini 3/6.

NEW pattern (Gemini-specific, dual-model): a rubric demanding an explicit NEGATIVE directive ("not ready, do not show/market") is a near-100% Gemini stump (R6 6/6 fail) while trivial for Opus (6/6 pass) — see Stump_Hypotheses.md follow-up. Log as a dual-model differentiator lever.

Density calibration: projected 48.5/model; actual Opus 43.5 (good), Gemini 33.0 (over by ~15). Per-model density spread is real; do not assume one midpoint covers both models. NOTE: parse_trajectories.py currently reports Gemini=0 (flat tool_use schema unhandled) — Gemini figures here were hand-counted; flagged for a parser patch (not applied in S4).


## Entry — Tasks/40_6a614767cd5b60ad96902fb4 — 2026-07-23 (HARDNESS predicted)
- **Universe/persona:** StarPM V4 (dual-model Opus+Gemini) · Lisa Smith (p_002, Onsite PM) · Property Operations. Fresh CB build.
- **Spine:** Tanya Mitchell dual live track as of 2026-07-01 — OPEN+approved Fair Housing ESA accommodation (HubSpot ticket_8faab56c663352cfb8d61c994b2bae88) coexists with an in-progress nonpayment eviction (Unit 14). Lisa assembles the Unit 14 turnover-readiness + account-status package believing the eviction is settled.
- **Selected levers (5):** S1 negative-directive / possession-not-returned (catalog #9 + L31 — Gemini stump); S2 delinquency-state supersession/latching (#1/#8/#10, L8/L13 — both); S3 structured-DB skip HubSpot ESA (#2, L10 — Opus stump); S4 near-miss Unit 14 cross-property Rio Bend vs Sunset Ridge (catalog #6, Learnings L4 — both); S5 authority-relayed 'owner approved / ready to file' anchor (L9, prompt-side — Opus).
- **Density:** midpoint 48 (range 38-59) → StarPM PASS (≥40 per model). 8 services touched, airtable dominant ≈26% (<60%). No PDF-decoy lever (0 .pdf in data). Avoid Las Palmas 8D shape (Task 39 similarity).
- **Actual Opus/Gemini fails:** TBD — fill from S4 after 6+6 trajectories.

## Entry — Tasks/40_6a614767cd5b60ad96902fb4 — 2026-07-23

**Persona / Business function:** Lisa Smith (lisa.smith@starpm.com, StarPM property manager) / Property Operations — Tanya Mitchell Sunset Ridge Unit 14 make-ready turn + account/eviction reconciliation.

**Selected levers (from Hardness_Plan.md):**
- S1 — Possession-not-returned negative-directive (L31): prompt "ready to re-rent" push vs make-ready hold note (recc83c05d889b354 fldNotes2); turn must stay selSched.
- S2 — Delinquency supersession / latching: prompt "nonpayment side is cleared" vs breached plan + active eviction; books-vs-notes decoy (invoice 7214 Balance 0 but PrivateNote "delinquent, no cure"; QR-2026-0441 $2,132 arrears).
- S3 — HubSpot ESA structured-DB skip (L10): approved reasonable-accommodation reachable only via HubSpot ticket_8faab... + gmail thread 9f2b3cd..., no conversational cue.
- S4 — Near-miss cross-property Unit 14 (L4): Rio Bend Unit 14 (rec94e86a3007dd5e, rent-ready decoy) vs Tanya's Sunset Ridge Unit 14.
- S5 — Authority-relayed "owner signed off / filing squared away" (L9): EVF-2026-014 owner-approved but still in JP coordination, possession not returned.

**FINAL-phase confirmation (pre-trajectory):** All 5 levers confirmed firing end-to-end by the cross-artifact Final Council (prompt sentence + OE step + rubric named for each). Integrated density ~44 per model (>= StarPM 40+ target). Injection difficulty 4.3/5 (>= 3.5; injection is comment-only, scenario native to base universe). Lens-6 Bucket-1 risk 0/16. Answer-leakage clean ($2,132 + full conclusion distributed across airtable + slack + quickbooks + hubspot + gmail, never pre-stated). VERDICT PASS, no REVISE round. Dual-model (Opus 4.8 + Gemini) verification expected downstream.

**Pipeline note:** submission_gate surfaced 5 deterministic FALSE-positives (F4 money-format, F2 calendar future-date) on a CORRECT rubric set; root-caused + fixed at Validators/v4_gates.py (Decimal money-normalization both sides; triple-gated calendar-create date exemption emitting a COUNCIL note), Oracle-blessed, regression-clean (anchors 62/62, reports 21/21, verdicts 7/7, qc_verdict 128/128). Future StarPM tasks with >= $1,000 comma amounts or calendar-reminder rubrics no longer false-fail.

**Lesson for next task:** StarPM calendar-reminder rubrics legitimately carry near-term future ISO dates, and >= $1,000 rubric amounts written "$X,XXX.XX" are grounded against bare-float universe storage. Both are now handled by the gate — never vague-ify a correct rubric to dodge a deterministic check; fix the check.
## Task 40 (StarPM V4) calibration delta - 2026-07-23
Predicted 5 levers: 3 produced genuine stumps (arrears-source, HubSpot-ESA-skip, near-miss-record), 2 acted as guardrails that behaved as designed rather than stumping (possession-hold negative-directive, authority-relayed false owner sign-off - agents correctly held true state, R2/R3/R6/R11/R9 pass).
Over-predicted: near-miss cross-record for Gemini (disambiguated 6/6; only Opus fell for it).
Under-predicted: R15/R16 OPS-32 comment omission in Opus low-call runs 5,6 (agent listed issues then skipped the comment entirely). Density-tail effect - the runs with fewest tool calls drop the last write action. Not a designed lever.
Robustness ranking observed: mis-filed-authoritative-figure (symmetric) > structured-store-skip (Gemini-selective) > near-miss-record (Opus-selective) > content-clause-omission (JP coordination, ESA phrasing; partial, high variance).


## Entry — Tasks/40_6a614767cd5b60ad96902fb4 — 2026-07-23 (S4 Gemini re-verify closure)
The R12 split was re-verified on Gemini (post-split 8b, 17 criteria) and matches Opus: R12a 6/6 pass, R12b 6/6 pass. The rubric-atomicity fix is now dual-model-validated. Difficulty levers unchanged and confirmed model-symmetric where predicted: R10 arrears-in-an-AP-bill 0/12 (both models never query the bills ledger); R13 ESA carry-through 6/6 Gemini + 4/6 Opus (retrieved then omitted). R1 near-miss cross-record Unit 14 stays Opus-only (5/6 Opus, 0/6 Gemini). No new levers; the atomicity fix does not move pass@1 (still 0% both models).

## Entry — Tasks/41_6a61a86a3453b3714bdc72ef — 2026-07-24 (FINAL pre-upload, lever end-to-end confirmation)

**Persona / Business function:** Patricia Nguyen (Onsite Property Manager, reassigned from Lisa Smith at S1.5) / Property Operations (BF1). StarPM V4 dual-model (Opus 4.8 + Gemini).

**Selected levers (from Hardness_Plan.md):**
- Lever 2 — Structured-DB skip (flagship): authoritative arrears in vendor-linked AP bill QR-2026-0441 (no CustomerRef), invisible to customer/invoice queries; AR invoice 7214 Balance $0 is the paid decoy.
- Lever 10 — Reversal / supersession: JP-coordination current state supersedes active-plan / awaiting-sign-off frames (Airtable SoR chain rec769→…→recc83).
- Lever 1 — Latching: older Linear "Eviction Hearing – Mitchell, Harris Property" (OPS-32) overstates progress + mis-names owner (real owner Linda Castillo, EVF-2026-014).
- Lever 11 — Net-vs-gross / sign: $150 "credit applied" stored as a positive → $2,132 stored vs $1,832 net (derived-only).
- Lever 31 — Negative-directive omission (Gemini differentiator): explicit prohibition "make-ready must NOT begin / do not market — possession not returned" (+ "not current despite paid invoice").

**End-to-end confirmation (FINAL Council, _aux/Council_Reports/FINAL_council.md):**
- All 5 levers (+ stacked L6 near-miss) trace prompt → OE → rubric → Fact_Ledger atom; zero lever regression.
- L2 → R1/R2 (walk-back to $1,832 net / $1,982 gross); L10 → R3/R10/R16; L1 → R4/R11/R17; L11 → R1; L31 → R5/R7/R8/R13/R18 (the explicit-hold / do-not-market rubrics).
- Answer-leakage clean (net $1,832 never stored in prompt or agent-readable universe content; independently re-greped).
- Density projection: Opus ~47 / Gemini ~42 — both clear StarPM v4 ≥40 (Gemini margin tight, watch first run).

**Actual failures (from S4 verifier-fails analysis):** DEFERRED — trajectories not yet run (0-byte pre-upload). To be recorded at PIPELINE S4.

**Calibration:** Pending S4. FINAL predicts: L2 arrears-in-AP-bill symmetric Bucket-3 (0/12 both models on sibling Task 40); L31 explicit-prohibition rubrics Gemini-asymmetric Bucket-3 (legitimate model gap, not invalid AF); rubric #2 ($1,982 walk-back composition) is the single atomicity watch-item.

**Lesson for next task:** StarPM FINAL phase-readiness will STOP on an upstream `Verification_s3.md` that follows the S3.md runbook template literally — the runbook Step-0.5 templates (`Data sources consulted` / no Verdict) are out of sync with `check_verification.py` (`Sources consulted` + `Verdict` + Per-task/Eval/QC categories). Also: never write the literal string `## Verdict` in the prose of a Verification file — the linter's first-match regex captures the inline mention and false-fails the real header.

## Entry — Tasks/41_6a61a86a3453b3714bdc72ef — 2026-07-24 (S4 calibration delta vs FINAL prediction)

Actuals now filled (FINAL entry above left "DEFERRED"). pass@1 0/6 both models, 0 errored, density Opus 48.0 / Gemini 38.8 (projection Opus ~47 / Gemini ~42 — Opus dead-on, Gemini ~4 under).

Lever calibration (predicted → actual):
- **L2 structured-DB skip (flagship) → HIT, symmetric, strong.** Arrears rubrics 0/12; both models stopped at paid invoice 7214, never opened vendor-linked bill QR-2026-0441. Confirmed for the 2nd StarPM task running. KEEP verbatim.
- **L31 negative-directive omission → HIT, Gemini-asymmetric, exact.** Channel "do not market" failed Gemini 3/6, Opus 0/6. 3rd confirmation (Tasks 39/40/41).
- **L1 latching (owner) → HIT but Opus-asymmetric (predicted symmetric).** Owner-mis-attribution fired Opus-only (3/6), Gemini 0/6. Correct the model-symmetry assumption: latching onto a mis-named owner is Opus-selective when the disambiguating record is a single auth record and both candidates share the owner role.
- **L10 reversal/supersession → HIT, Opus-asymmetric, manifested as make-ready record-pick (not the eviction-state report).** Opus 3/6 wrote to superseded records; Gemini 0/6. The eviction-STATE report (petition not filed) did NOT fail — supersession bit at the write target, not the read/report.
- **L11 net-vs-gross → DISPLACED (masked by L2).** Never observed: no agent reached the bill, so the $150-credit disposition step never ran. Pair L11 with an easier discovery path next time or it stays invisible behind L2.
- **L6 near-miss (Rio Bend / catch-all) → over-predicted, no fire.**

Over-predicted: eviction-state progress-overstatement (H2 half) — 12/12 pass; near-miss unit (H5) — 0 fires.
Under-predicted: none material. The owner-latch cascaded into 4 rubrics (broader blast radius than the single-rubric FINAL mapping implied).
Robustness ranking observed (StarPM dual-model, 2 tasks): vendor-linked-AP-bill arrears (symmetric, 0/12 twice) > negative-directive omission (Gemini-selective) ~ owner-latching / reversal-record-pick (Opus-selective) > net-vs-gross (only visible once discovery is easy) > near-miss unit (weak).

## Entry — Tasks/41_6a61a86a3453b3714bdc72ef — 2026-07-24 (S4 post-fix re-grade delta)

Re-grade after the R6/OE-14 reconciliation + $2,287.50 fail-list additions. Append-only; prior "S4 calibration delta" entry left intact.

- **R6 fix CONFIRMED EFFECTIVE, difficulty unchanged.** R6 now passes 6/6 Opus (was 3/6 fail pre-fix); identical Tanya-Unit-14 writes that flip-flopped now grade consistently. pass@1 stayed 0/6 both models — the fix removed a rubric-invalidity false-fail, not a lever. **Correction to the prior delta:** L10 did NOT manifest as a legitimate make-ready-record stump; the pre-fix R6 fails were over-strict-rubric artifacts. L10's genuine contribution is the eviction-state supersession chain (reads), which the deliverables handled correctly (petition-not-filed rubrics 3/10/17 passed 12/12).
- **Surviving lever ranking (StarPM dual-model, unchanged by the fix):** vendor-linked-AP-bill arrears (SYMMETRIC, 0/12 — flagship) > negative-directive omission (Gemini-selective, R14 3/6) ~ owner-latching (Opus-selective, R4/R11/R15/R18 3/6) > net-vs-gross L11 (masked by L2, never observed) > near-miss unit (no fire).
- **Zero Bucket 1 / zero Bucket 2 this run** — task is ship-clean; no rubric fix outstanding. AF justifications (R1/R2/R16) voice-gate clean.

**Lesson for next task:** when an S4 fix broadens an over-strict rubric, re-run and confirm pass@1 is unchanged before crediting the removed fails as a difficulty lever in the calibration ledger. A false-fail eliminated is not a lever lost.

## Entry — Tasks/43_6a62ccaf5853030245ac9d53 — 2026-07-25 (FINAL council PASS, pre-upload)

StarPM V4 dual-model, Carlos Mendez / Property Operations. Spine: **Mesa Vista 4C make-ready owner cost pass-through reconciliation** ($1,622 believed vs $1,812 derived; decoys $1,897 / $1,727 / $1,810).

- **Levers selected and confirmed end-to-end at FINAL (4):** **L2 structured-DB skip** (the $1,340 repaint exists ONLY on AP bill `696089964235`; absent from invoice 2026-534, the summary email body, and Slack) · **L10 supersession** (the stale AR draft is the mirror; AP bills supersede) · **L6 near-miss** (10-bill $1,340 cluster + $1,140/$1,340 + twin $85 + Linda/Pete owner decoy + the 385/387 Rio Bend deep-clean trap) · **L11 net-vs-gross** (exclude the internal $85 condition walk, keep the $85 closet trim). Each maps to a prompt sentence + OE step + rubric; no lever orphaned.
- **New pattern that graded well — "twin-amount discrimination".** Two $85 third-party bills on the same unit, both opening with the identical `"Internal labor charge for <StarPM person>"` template, one owner-billable and one not. The template phrase appears on exactly 2 records universe-wide, so the obvious textual discriminator separates nothing and the agent must fall back on work-kind + account coding + the note's operative instruction. Cheap to build, forces real reading, and produces two clean decoy totals in opposite directions.
- **MAJOR carried into S4 (yield caveat, not a defect):** the prompt must state the reconciliation ask ("go back to what each vendor charged us"), which is the `Learnings.md` **L29 escape-valve** shape and will blunt L2's predicted ~0/12 sweep. Removing it would cost Feasibility/Clarity, so it stays. **Expected sweep re-attributed to L6/L11**; if runs reach the AP bills but land on $1,897 or $1,727, score that as L6/L11 firing, not L2 failing.
- **Density:** Opus ~45 PASS; Gemini ~36 THIN (accepted with the Hardness_Plan justification; 4 writes / 4 services delivered as the promised mitigation). Watch the first Gemini run's call count at S4.
- **Gate history:** `submission_gate` caught 4 real F5 NEEDS_TOOL_OUTPUT defects that S3's own gates did not surface ("confirm the tool returned a success response" in write-rubric evidence). **Lesson: any write rubric whose evidence asks the judge to confirm a call succeeded is an automatic Evals_starpm/5 F5 FAIL — write write-rubric evidence against call ARGUMENTS from the start.**

## Entry — Tasks/43_6a62ccaf5853030245ac9d53 — 2026-07-25 (S4 calibration delta, dual-model actuals)

Measured against the pre-registered Hardness_Plan + the FINAL-council carry-forward. pass@1 0/6 both models, 0 errored runs, 0 Bucket 1.

**Hit rate: 1 of 4 predictions confirmed as written; 1 more confirmed by the FINAL re-attribution; 2 over-predicted.**

| Lever | Predicted | Measured | Delta |
|---|---|---|---|
| L2 structured-DB skip | HIGH, symmetric, ~0/12 | **0/12 fired** (all runs reached the AP bills) | over-predicted; the L29 escape-valve sentence neutralised it, exactly as FINAL MAJOR-1 warned |
| L6 near-miss entity | MED-HIGH, Opus-selective | **0/12 fired** | over-predicted; cluster/owner/385-387 decoys all missed |
| L11 net-vs-gross | MED, Gemini-leaning, "margin item not the engine" | **12/12, SYMMETRIC, 9 of 15 failing rubrics** | under-predicted in magnitude AND mis-attributed by model |
| L9 duplicate write | LOW-MED | **0/12 fired** | over-predicted; keep as a cheap guard |
| Dual-row record pick (unbudgeted) | not a named lever | **3/12, both models** | new observation |

**Density:** projected Opus ~45 / Gemini ~36 → measured **41.7 / 36.8**. Gemini projection accurate to 1 call; Opus 3 calls optimistic. The FINAL watch-item (abort if the first Gemini run < 30) was **not triggered** (min 34). The THIN-density acceptance held: the 4-write / 4-service OE executed on all 12 runs and carried Gemini to 36.8, comfortably clear of the 15 fail floor.

**New pattern, promoted from the FINAL-phase "twin-amount discrimination" note to a first-class lever: PROSE-VS-STRUCTURED-FIELD CONTRADICTION ON ONE RECORD.**

Recipe, in the order that made it work:
1. Put the **misleading** claim first in a free-text field on the authoritative record ("Internal labor charge for Tony Reyes...").
2. Name a person the agent can verify is internal (`tony.reyes@starpm.com`, Lead Maintenance Technician) so the wrong reading survives a contacts lookup.
3. **Corroborate the wrong reading from a second service** (Slack C004: "Tony got it done today"). This is what lifts it from a coin-flip to a 0/12 sweep.
4. Put the resolving evidence in a **structured field on the same record** (`VendorRef.name` = the outside vendor) plus an operative clause later in the same note ("Pass-through to owner").
5. Give it a symmetric twin that goes the other way (the Alamo HVAC $85 condition walk, genuinely internal) so the discriminator cannot be a keyword.

Blast radius: 9 atomic rubrics from one classification call. Highest of any StarPM lever measured so far.

**Robustness ranking updated (StarPM dual-model, 3 tasks):** prose-vs-structured-field contradiction (symmetric, 0/12, 9-rubric radius) > vendor-linked-AP-bill arrears (symmetric, 0/12 twice, 3-rubric radius) > negative-directive omission (Gemini-selective) ~ owner-latching (Opus-selective) > dual-row record pick (weak, both models, 3/12) > near-miss entity cluster (no fire this task) > duplicate-write guard (no fire, keep anyway).

**Cost note for the next plan:** the two levers that fired cost ~5 projected calls each and delivered the entire sweep. The two that did not fire (L6 near-miss at cost 4, L2 skip at cost 6) still bought real density, because forcing disambiguation reads produces calls whether or not the agent falls for the decoy. Do not delete a non-firing near-miss lever from the density budget on the strength of one task.

## Entry — Tasks/44_6a62ccba8cad60844b8364b9 — 2026-07-26 (HARDNESS, pre-registered)

StarPM V4 dual-model. Persona **Jaime Salinas** (Quality Control Inspector, `p_007`, BF3 Quality Control & Field Services). Scenario: **close out the QC side of the portfolio-wide Preventive Maintenance Push** (Brooke Phillips's HVAC / plumbing / electrical audit, kicked off 2026-05-07, target close "before end of June"; universe today is 2026-07-01, so the deadline has passed).

**Hardness 5/5 PASS.** Levers 1 (latching), 2 (structured-DB skip), 5 (thread-reply blindness), 8 (multi-link chain), 9 (authority dismissal, persona-self variant). Lever 7 multi-write engineered in and scored in the Write-actions row. Levers 3, 4, 6, 10 carried as corroboration/noise with no rubric dependency; Lever 11 dropped for lack of backing data.

**Density:** projected midpoint **55.5** (range 44-67) against the StarPM 40 design target, per model. Breadth 6 services at >= 5%, dominant service linear at 34%.

**The load-bearing lever is a structural variant of Task 43's flagship — prose-vs-structured-field contradiction — moved from a QuickBooks money field to the Linear workflow-state column.** It hits all five steps of the Task 43 recipe without any injection:
1. Misleading claim first in free text: OPS-87 description "moved both from In Review to Done", OPS-96 "Moving this to In Review", OPS-98 "I'm moving both cluster issues to Done", plus Jaime's own two OPS-98 comments and her OPS-96 comment restating it.
2. Named person verifiable as internal: the claim is authored by **the persona herself**, a real `@starpm.com` Quality Control Inspector, so the wrong reading survives any contacts lookup and additionally recruits Lever 9.
3. Corroborated from a second service: Slack C001 `1779308446.000005` / `1779308447.000006`, Elias Navarro "all three clusters are done. Every unit serviced" / "Summer HVAC push is a wrap... 34 units total serviced".
4. Resolving evidence in a structured field on the same record: `state_id` = `state_OPS_1` (Todo) on OPS-87 and OPS-96, `state_OPS_2` (In Progress) on OPS-98 and OPS-97, `state_OPS_0` (Backlog) on OPS-108 and OPS-44. **Not one push QC issue sits in Done.** Decoding requires a second call to `list_issue_statuses`, since the raw values are opaque ids.
5. Symmetric twin going the other way so the discriminator cannot be a keyword: **OPS-91** carries `state_OPS_4` (Done) while its own description says "Moving this issue to In Progress". Near-duplicate titles in opposing states give two more: OPS-99 (In Progress) vs OPS-108 (Backlog), OPS-51 (In Review) vs OPS-71 (Backlog).

**Second novel pattern this task banks: the persona's own field note contradicts the persona's own sign-off, one day apart.** Slack C001 `1779562423.000092`, 2026-05-23, Jaime: "north Cluster walk-throughs done. Two units need HVAC looked at right away, flagged on the Linear issue with coil, plumbing, and panel notes." Her OPS-87 (5/24) and OPS-98 (5/25) then say "everything came back clean across the board" and "No issues to flag on either side". No follow-up issue for those two units exists anywhere in the 230-issue corpus. This is L9 authority dismissal with the authority collapsed onto the persona, which removes the usual seam an agent can use to distrust the framing — there is no third party to be sceptical of.

**Coverage-gap sub-lever (new shape).** Jaime's three QC issues cover South, North and portfolio filters; East is covered via OPS-99 / OPS-108. The push also has a **West cluster** (OPS-35, Lisa Smith onsite lead) that she never walked, and OPS-186 dated 2026-06-17 states "the West Cluster work still underway". The cluster set is genuinely inconsistent across services — Elias's scope issues OPS-16 / OPS-17 / OPS-18 name only three clusters — so an agent anchored on the HVAC scope reads three-of-three as portfolio-wide coverage. Note the discipline this forced: no rubric may assert a cluster count, only that **her own three issues never cover West**.

**Prompt-side constraints pre-registered, carried from prior-task scars.** No escape-valve clause (L29 / Task 43 MAJOR-1 — an invitation to surface contradictions would neutralise Lever 2 on the exact column the task turns on). Soft verbs on the authority anchor (L24). F7 is the live gate risk: Jaime owns **three** interchangeable QC issues, so prefer writes unique by construction (new Linear issue, new Airtable ticket, new Calendar event, Gmail draft to a named recipient, Slack post) over any rubric that pins an issue id. F9 swept clean — 9 unique future confirmed events, none touching the push, the clusters or Jaime — with two adjacent watch items (2026-07-15 Mesa Vista 4C QC inspection, 2026-07-23 Q3 make-ready budget review) that forbid any "her QC queue is otherwise clear" or "budget question settled" claim.

**QuickBooks deliberately excluded from the lever set, which is also the similarity pivot.** Three reasons: `VendorRef.name` is unreliable noise in this universe (bills attributed to "Alamo HVAC Services" carry landscaping, legal-review and Tanya Mitchell arrears lines — the Task 43 item-19 failure mode); the only push-relevant QuickBooks fact would be an **absence** (no bill or PO for the 20x25 filter restock or the Lone Star bulk order), which L7 forbids as a load-bearing answer; and Tasks 41, 42 and 43 all resolved to a QuickBooks dollar figure, so keeping this answer non-monetary is the main defence of the 40% similarity ceiling. Near-miss vendor pair noted for future use: **Lone Star Maintenance Supply** vs **Lone Star Electric**.

**Density-shape note for future StarPM plans.** This is the first StarPM task whose primary store is Linear rather than QuickBooks. Roughly 20 push-adjacent issues each needing a state read plus a comment walk is structurally more call-hungry than the 41/42/43 money-figure shape, which is why the projection sits at 55.5 against measured 41.7 / 36.8 on Task 43. Stated risk: a strong agent can pull state for many issues in one `list_issues` page instead of iterating `get_issue`, which would compress the Lever 2 row toward its low end. The row was budgeted at 5.5 rather than the Playbook maximum for that reason, and the total clears 40 even if it collapses to 1.

**Wording constraint that nearly slipped, recorded because it is the Task 39 overclaim shape.** Two push issues ARE in Done: OPS-40 "Preventive Maintenance Push - North Cluster Properties" and OPS-91 "HVAC condenser cleaning and filter replacements - West Cluster". So "nothing on the push is closed" is falsifiable and must never be written. The verified claim is scoped: **none of Jaime's three QC issues is in a completed state** (OPS-87 Todo, OPS-96 Todo, OPS-98 In Progress), with OPS-97, OPS-108 and OPS-44 showing the same prose-versus-state pattern. Caught by asserting the claim against the data with an explicit issue list rather than trusting the prose summary of the scan — worth doing on every prose-vs-structured-field lever, since the lever's whole premise is that prose summaries are unreliable.

**FINAL (2026-07-26) — all 5 levers confirmed end-to-end; PASS.** Task 44 cleared the cross-artifact council with 0 BLOCKER. Levers confirmed firing prompt -> OE -> rubric: **Lever 2** structured-DB skip on Linear `state_id` (idx 54, the symmetric stump), **Lever 9** authority dismissal in its persona-self variant (idx 52/53 plus the three notes at idx 24/25/26), **Lever 1** latching on the crew's wrap (idx 55/56), **Lever 8** multi-link chain off Jaime's own field note (idx 1), **Lever 5** thread-reply blindness (idx 8/11). Density PASS per model on the StarPM V4 band: Opus midpoint 54, Gemini midpoint 49. Bucket_1_Risk 3.1% post-fix.

**New pattern worth banking: the "either-destination" asymmetry defect.** When a prompt carries an explicit routing rule ("X belongs in A rather than B"), every criterion covering an item of class X must grant the same destination latitude. Task 44 shipped past S3 and AUDIT with idx 16 accepting either destination for the water heaters while idx 17 pinned the hose bibs to a tracking item, and idx 11 accepting either for the South access unit while idx 12 pinned the North pair. Both items in each pair come from the same source comment and are the same class of work. An agent that applies the prompt's own routing rule *consistently* passes one and fails the other, which is a pure Bucket-1 false-fail invisible to per-phase review because each criterion reads fine alone. **Check: for every prompt routing rule, list the items of that class and diff their accept-sets across the rubric set.** Fixed by widening the narrower criterion and extending the matching OE's accommodation clause so the artifacts agree.

**Second pattern: a graded fact whose OE quotation was truncated one sentence short.** idx 61 graded OPS-186's electrical-completion statement, but OE 20 quoted that description starting at the *second* sentence, so the graded fact had no oracle designation anywhere in 38 OE steps. `grep -c` on the criterion's own subject term across the OE file is a cheap detector (it returned 2 here, both unrelated). Compounded by the justification asserting the completion as settled fact while the record sits in Todo, in a rubric set that otherwise trains distrust of exactly that pattern. **Check: for each rubric, grep its distinguishing noun in the OE file; and any criterion that asks the agent to credit prose in a non-completed record must carry the grades-what-the-record-states hedge.**

**S4 (2026-07-26) — Opus actuals; calibration deltas. Gemini half blocked on an unsaved verifier file.**

Opus pass@1 **0/6**, density **62.5** (projection 55.5, so the projection under-counted), 0 errored runs. Gemini density **79.8**. 44 of 60 criteria failed at least once; Bucket 1 = 3, Bucket 2 = 1, Bucket 3 = 40; All-Failing sub-dim **5/5**. No REDO.

**Correction that invalidates a lever on this universe: Lever 5 (thread-reply blindness) is INERT on StarPM.** Zero of 12 runs across both models ever called `slack_read_thread`, and it did not matter: `slack_read_channel(channel_id="C001", limit=100)` returns thread replies inline as flat top-level messages. Brooke's stock-count ask at ts `1779569323.000012`, John's parent post at `1779567943.000011` and the South-cluster reschedule replies at `1779308444.000003` all appear in the **first channel-read result of all 12 runs**. Verified by grepping every trajectory for the reply timestamps and for "Lone Star" / "bulk order": present in 12/12. Consequences for future StarPM plans: (a) do not select Lever 5 as an independent lever here, (b) do not budget the 2-4 `slack_read_thread` calls the density row assigns it, (c) any StarPM hardness claim of the form "this fact lives only in a thread reply" must be falsified against an actual channel-read result before it is banked. Whether the same flattening holds on Brookfield / KeyStone / MoveOps is **unverified** and should be checked the same way before reusing L12 there.

The lever the plan credited did not exist; the difficulty it produced was real but came from a different mechanism. The filter run still swept 0/6 because the agents **read** "restock before I can finish the run" and then closed the filter spot-check as a clean pass anyway. That is a reasoning failure, not a retrieval failure, and it is the more durable of the two.

**Promote Lever 6 out of "flavor".** The plan carried near-miss entity confusion as noise with no rubric dependency, citing L4. Two of the three strongest discriminators in the shipped set were exactly that shape: the two North pairs (deficient-flagged vs access-pending, 6/6 on the criterion that separates them) and OPS-99 vs OPS-108 (identical title, opposing states, 6/6). The working recipe is **same cluster, same count, same noun, different reason for being open** — three runs even retrieved both East records and called them duplicates without ever comparing their states. Retrieval is not the gate; the comparison is.

**A structured-DB-skip lever discriminates on records but does not gate the verdict when a conversational path to the same verdict survives.** Criteria 49, 50, 54 and 60 (the headline: sign-off does not hold, not closeable, flagged units still open, cannot close out) all passed **6/6** while the state-column criteria failed 3/6 to 6/6. Jaime's own 5/23 field note (Lever 8) was sufficient to reach the right top-line answer without ever decoding `state_id`. If a future plan needs the verdict itself gated on the structured field, the conversational path has to be removed or made insufficient on its own; otherwise budget the structured-DB lever as a *criterion-level* discriminator and let the multi-link chain carry the headline.

**Surfacing a gap and acting on it are separately gradeable, and the action is roughly twice as hard.** West coverage gap: 4/6 runs named it in narrative, 2/6 raised the tracking item. Build both criteria, expect the narrative one to be the weak discriminator.

**The "either-destination" asymmetry defect survived the FINAL fix at the container level.** FINAL caught and widened the *item-level* pairs (water heaters vs hose bibs, South access unit vs North pair). It did not catch that the two *container* criteria above them still read "raises a tracking item" and pin Linear. Criterion 15 false-failed four runs that routed the plumbing findings to the ticket log exactly as OE 32 permits; criterion 11 false-failed three runs that had already passed its own content and owner criteria on the strength of the same Airtable ticket. **Extend the check: when a routing rule is widened on the content criteria, widen the container criterion in the same pass, or the accept-sets diverge in the one place a per-criterion read cannot see.**

**A criterion that grades a state can collide with an OE that permits changing that state.** Criterion 51 asks the agent to report that none of OPS-87 / OPS-96 / OPS-98 is in a completed state; OE 15 says an agent that flips one of them "is not wrong". Three runs flipped OPS-96 to Done and were failed on the criterion. **Check: any criterion grading a field the agent is also permitted to write must be anchored to the as-found value, not the present tense.**

**Positive-completion criteria are judge-fragile.** Criterion 58 (report that the South electrical panel inspections are recorded as finished) failed 6/6, and three of those six said it plainly in their final-response cluster table ("Electrical done", "South HVAC + electrical Done, Patricia", "electrical confirmed (Patricia)"). The criterion's own evidence field authorised exactly that, and the judge still required a dedicated sentence. When a criterion asks the agent to report what IS finished inside a deliverable that is otherwise a list of what is NOT, carry `(or similar)` and say explicitly that a table row or list entry satisfies it.

**S4 CORRECTION (2026-07-26) — dual-model actuals. Supersedes the "Opus actuals; Gemini half blocked" block above.**

The Opus block above was computed from a verifier export that did not match the Opus trajectories on disk. Both files were re-exported against the shipped 60-criterion set and the loop was re-run on both models. Corrected: Opus pass@1 **0/6** (31/36/45/27/30/47), Gemini pass@1 **0/6** (17/10/25/16/15/18), density 62.5 / 79.8, 0 errored runs. 52 criteria fail at least once. **Bucket 1 = 1, Bucket 2 = 6, Bucket 3 = 45. All-Failing sub-dim 5/5 (1.9%).** No REDO.

**Retract the "Lever 5 is INERT on StarPM" claim as stated; the corrected version is narrower.** Re-measured against the trajectories on disk: **Opus called `slack_read_thread` 0 times across all 6 runs; Gemini called it 9 times across 4 of 6 runs.** The lever is a retrieval barrier on Opus only. What survives unchanged is the part that actually matters: `slack_read_channel(channel_id="C001", limit=100)` returns thread replies inline as flat messages, so the reply content sat in every run's context on both models regardless of whether the thread tool was called. The practical guidance is unchanged (do not select thread-reply blindness as an independent StarPM lever, do not budget its calls on Opus) but the evidence for it is "the replies are flattened into the channel read", not "no model opens threads". **Method note: the earlier claim was asserted from a trajectory grep whose input set was correct but whose conclusion was never re-checked after the verifier export changed. Re-measure tool-usage claims against the same artifacts the grading was computed from.**

**Correct the "positive-completion criteria are judge-fragile" entry, and strengthen it.** The South-electrical criterion does not fail 6/6; it fails **4/6 on Opus and 4/6 on Gemini**, and **four of those eight cells are judge errors** against responses that state it in the plainest available form ("Electrical panel inspections (Patricia) and HVAC run (Elias) are finished"; "electrical panel inspections (OPS-186) are complete and marked Done"). The criterion's evidence already authorises exactly that. The failure mode is sharper than first recorded: the judge reads **"are recorded as finished"** as demanding a meta-claim about the record rather than a claim about the work, and withholds latitude the evidence grants. **The trap is that the obvious fix is wrong**: dropping the recorded-as hedge would assert as verified fact a completion that lives in a record still sitting in Todo, which is the overclaim the hedge exists to prevent. Bank the shape rather than a fix: **a criterion that must grade what a record claims, in a set that otherwise trains distrust of what records claim, is inherently judge-fragile in both directions and should be expected to draw appeals.**

**New pattern: first-person accept-sets.** A criterion listing named people as the acceptable holder of a piece of work can false-fail a correct answer when the holder is the persona writing the deliverable, because the natural business phrasing is "owned by me" in a signed email rather than the person's own name. One Opus cell failed exactly this way. **Check: for every accept-set that includes the persona, state in the evidence that a first-person self-reference by the sender counts as naming them.** Cheap to add, invisible until a run writes in the voice the prompt asked for.

**Judge-error rate, measured.** 22 of 403 fail cells (5.5%) are contested after a full trajectory walk, 19 of them on Gemini. The dominant shape is **scope drift**: the criterion scopes itself to the draft body or the channel post, and the judge grades the agent's Linear writes instead. One Gemini justification applies a different criterion's accept-set outright. Useful baseline for future tasks: expect roughly 1 in 20 fail cells to be contestable, skewed toward the weaker model, and budget the S4 trajectory walk accordingly rather than trusting the verifier text.

**A conversational path to the verdict makes the structured-DB lever model-selective rather than symmetric.** Refined from the Opus-only reading. On Opus the field-note path carried the headline verdict and the state-column criteria discriminated only at the record level. On Gemini both the records and the verdict fell. So the same lever is a criterion-level discriminator on the stronger model and a verdict-level one on the weaker model. If a plan needs the verdict gated on both, the conversational path has to be removed or made insufficient on its own.

**S4 PASS-3 REGRADE (2026-07-26). Supersedes the correction block above on every number; the mechanism findings in it stand.**

Both verifier files were re-exported a third time after six evidence-field clarifications. Trajectories unchanged. Corrected: Opus pass@1 **0/6** (34/33/44/26/30/46), Gemini pass@1 **0/6** (20/19/22/19/20/21), density 62.5 / 79.8, 0 errored runs. 48 criteria fail at least once. **Bucket 1 = 0, Bucket 2 = 0 at criterion level, Bucket 3 = 48, 10 contested run-cells. All-Failing sub-dim 5/5 (0.0%).** No REDO.

**Measured grader non-determinism: 8.5% of decision cells, on unchanged text.** 67 of 720 cells changed between two gradings of byte-identical trajectories. Only 6 fall on the six criteria whose evidence was edited between the exports; **61 are decision changes on criteria whose text did not move by a character.** Direction is model-asymmetric: Gemini gained 20 criteria-passed across six runs, Opus lost 3. Largest single-run swing was 9 points (Gemini run 2, 10 to 19). This is the single most important number in the entry, because it bounds what any per-cell claim is worth.

**What survives the variance and what does not.**
- **Gates are unaffected.** pass@1 was 0/6 on both models under both exports, error runs 0 under both, and density is a trajectory property grading cannot touch. A task whose difficulty margin is wide survives regrading; one sitting near a threshold does not. **Design for margin, not for a passing number.**
- **Per-cell appeals are worth filing only where the artifact text is verbatim decisive.** Pass 2 filed 22 contested cells; the regrade vacated 11 of them unprompted, including every cell on four criteria that are now clean 12/12. Pass 3 files 10, scoped to that standard, and three of those are cases where the judge's sentence is contradicted word-for-word by the artifact.
- **Revised judge-error baseline: ~2.6% of fail cells after a strict walk** (down from the 5.5% recorded under the pass-2 export), but the *cell-level instability* is 8.5%. Those are different quantities and the second is the one to plan around.

**Criterion shape predicts grading stability. This is the actionable finding.**
- Criteria grading **a created artifact and its contents** (ticket created, item raised, calendar slot booked, message posted, draft addressed) moved **0 of 96 cells** across both gradings.
- Criteria grading **the agent's characterisation of a pre-existing record's claim** ("X is recorded as finished", "the crew recorded Y as complete", "the latest dated status says Z") absorbed most of the movement and account for **6 of the 10 contested cells** in this pass.
- **Rule: when a lever can be carried on either shape, carry it on the artifact.** Reserve record-characterisation criteria for levers that genuinely require them, and expect them to draw appeals in both directions.

**Correction to the "positive-completion criteria are judge-fragile" entry.** The South-electrical criterion is not 6/6 and not 4/6-and-4/6. Under the current grading it is **4/6 Opus and 3/6 Gemini, with 3 of those 7 cells contested.** The failure mode recorded earlier is confirmed and unchanged: the judge reads "are recorded as finished" as demanding a meta-claim about the record rather than a claim about the work, and withholds latitude the evidence field explicitly grants. The trap also stands: dropping the recorded-as hedge would assert as verified fact a completion living in a record still sitting in Todo. **Method note: this criterion's numbers have now been restated three times off three exports. Never restate a per-cell count without re-deriving it from the export in hand.**

**The first-person accept-set fix is verified, not just proposed.** The evidence-field amendment stating that a first-person self-reference by the sender counts as naming the persona flipped exactly the cell it targeted (`Opus run 2`) from Fail to Pass, and a second contested cell with it. **Confirmed cheap and effective. Apply it at S3 to every accept-set that includes the persona, rather than waiting for S4 to find it.**

**New: a judge can fail a cell with a claim the artifact refutes verbatim.** Three cells in this pass carry judge text contradicted word-for-word by the write payload, the clearest being an item description containing the literal string "Owner: Lisa Smith (cluster lead)" failed with "the description text does not confirm Lisa Smith". All three passed under the previous grading. **Consequence for S4 method: the trajectory walk is not optional verification of the verifier text, it is the only thing standing between a false fail and an AF justification that blames the model for the judge's error.**

---

## Task 44 — pass-4 regrade block (2026-07-26, third grading of identical trajectories)

Basis: `8a` (16:18) + `8b` (16:19), rubric text as edited at 14:42 (13 criteria widened). Trajectories
unchanged. 74 of 720 cells moved from the pass-3 grading; 62 of those on text that did not change.

### Two new judge failure classes, both distinct from the ones already logged

**Class 3: the judge cannot resolve an internal record id, and then accuses the run of misreporting itself.**
`Opus run 4` addressed six Linear comments by internal record uuid rather than by issue identifier. The judge
resolved five and mis-resolved the sixth as a different issue, concluded that no comment was written on the
required record, and wrote that the run's final response "claims a note was left on OPS-87, but this is
contradicted by the actual trajectory." The comment exists, the uuid resolves to OPS-87 from the identifier and
uuid pair returned in that same run's tool results, and the criterion's evidence field explicitly accepts the
internal id form. **Method consequence: build a uuid-to-identifier map from the tool results across all runs
before classifying any comment-target criterion.** On this task 257 uuids resolved from the trajectories alone.
Without that map, this cell would have been written up as a legitimate model failure and the AF batch would have
blamed the model for the judge's resolution error.

**Class 4: the judge reasons from the run's own summary rather than from the sent payload.** Three cells carry
judge text of the form "the response summary does not show this framing in the posted Slack message" where the
posted payload carries the required statement verbatim, in one case as the message's opening sentence. This is
distinct from over-strict reading: the judge is grading the wrong artifact. **Method consequence: for every
channel or draft criterion, read the write payload, never the run's description of it.** Worth flagging to the
platform separately from ordinary appeals, because it is a harness-level problem rather than a judgment call.

### Confirmation: the "recorded-as" criterion shape is judge-fragile, third data point

The two as-found criteria (South electrical recorded finished, crew recorded East service complete) produced
**7 of the 21 contested cells this pass**, on both models. Both carry evidence text stating that naming the
record identifier is not required, and the East criterion states a single FAIL condition that none of the
contested cells meets. The grader required record attribution anyway, on four cells for one criterion and three
for the other. The trap itself remains sound and must not be dropped: removing the "recorded as" hedge would
assert as verified fact a completion that lives in a record still sitting in a non-completed state. **The fix,
if the misreading recurs, is to lift the "identifier not required" clause out of the evidence field and into the
title, which changes no accept-set and costs no criterion slot.** Not applied this pass, to keep the grading
comparable.

### Confirmation: accept-set widening is cheap, effective, and measurable inside one regrade

The 14:42 edits widened thirteen criteria. Measured effect on Opus: the note-on-a-QC-record criterion moved
**0 of 6 to 4 of 6** once any correct reason was accepted; three filter-run criteria each moved **0 of 6 to 1 of
6** once a comment on an existing open record was accepted beside a new tracking item; the plumbing escalation
criterion moved 4 of 6 to 5 of 6 once the maintenance ticket was accepted as a destination. Two widened criteria
drifted one cell against the agent, inside the documented variance and not attributable to edits that only added
locations. **Apply this at S3: enumerate every reasonable destination in the evidence field at authoring time.**

### Confirmation: criterion shape predicts grading stability, now across three gradings

Criteria grading a created artifact and its contents moved **0 of 120 cells** between the last two gradings,
having moved 0 of 96 between the previous pair. The persona's-own-field-note carriers moved **0 of 48**. All the
movement continues to concentrate on criteria grading the agent's characterisation of a pre-existing record's
claim. This is now a rule rather than an observation, and it should drive lever carrier selection at S3.

### Method note on counts

Per-run and per-cell counts on this task have now been restated across three exports (best Opus run: 47, then
46, then 43). **Never carry a per-cell count forward between passes. Re-derive it from the export in hand.**


## 2026-07-27 - Task 45 (StarPM V4) FINAL PASS: Mesa Vista 4C QC hold

Levers selected and confirmed end-to-end by the Final Council (prompt + OE + rubric each named):
**L2 structured-DB skip (SYMMETRIC)** the not-ready truth lives only in the tblMakeReady selProg row recbd087a4abd605b; maintenance tickets + prior selReady turn + Slack chatter all say done -> R1/R2/R3.
**L1 latching + L10 supersession (OPUS-SELECTIVE)** the decoy selReady row recc8534 was created LATER (5/29 vs 5/22), baiting a latest-row heuristic; two done-flavored maintenance tickets reinforce -> R1 evidence + R2.
**L31 explicit negative directive (GEMINI-SELECTIVE)** correct output is a kick-back: do NOT mark Ready, do NOT release for listing -> R2/R15. This is the banked StarPM dual-model 0/6 triad (Learnings item 11): one symmetric + two complementary asymmetric stumps.
Supporting: **L7 multi-write** (6 distinct writes across Airtable / Slack C004 / Linear issue+comment / Gmail draft to Carlos / Brooke notification) and **L9 universe-grounded future-event gotcha** (confirmed 2026-07-15 QC re-inspection + past-due 6/30 target) -> R8/R19.

**Density is THIN (accepted):** per-model competent projection Opus ~40-43 / Gemini ~38-41; empirical StarPM anchor 33-38. Clears the 15 fail-floor but leans on the 40 design target. Mandatory S4 gate: real-run per-model avg < 40 -> PIPELINE REDO.

### Standing gate added this pass: F2 negation-awareness (rule 18)

The submission_gate F2 date net false-failed rubrics #8/#19 for citing the real confirmed future event 2026-07-15 with future-acknowledging language ("has not yet occurred"). Evals_starpm/5 P2 (~L146) defines the F2 defect as future-AS-PAST (treating a not-yet-happened event as already analyzed); asserting an event is still pending is the spec-correct opposite, and is exactly what the F9 net rewards. Fixed the gate (not the rubrics) per rules 18-20: added _FUTURE_ACK_RE to v4_gates.py so a post-window future date co-occurring with "not yet occurred / still pending / yet to occur / upcoming" routes to a COUNCIL NOTE, not a FAIL. Regression clean (anchors 62/62, reports 21/21, verdicts 7/7; 0/21 hashes moved). The future-date-plus-negation construction is this task's novel pattern; no snapshot carried it. Reject the Path-A workaround (adding "calendar" to trip the calendar-create exemption) as gate-gaming.

### S4 ACTUAL (2026-07-27) — the FINAL-pass prediction was REFUTED empirically

The FINAL council named all three levers end-to-end and predicted the banked StarPM 0/6 triad. The 12-run dual-model verifier says otherwise: **Opus pass@1 = 100% (6/6 x 20/20), Gemini 50% (3/6), overall 75%.** Machine verdict `REBUILD_CANDIDATE_DIFFICULTY`. Zero all-failing rubrics. The only fails are Gemini-only and inconsistent (crit 1+3 Airtable write skipped Runs 1-2; crit 5-7/17-19 dollar-figure or In-Progress/past-due dropped Runs 2,4). Density corroborates: Opus 37.0 avg (sub-40, tripping the plan's own mitigation #2).

**Every predicted lever missed 0/4**, and the mechanism is identical for all four: `5_Prompt.txt` names the discriminator each lever was built to withhold. L2 is handed away by "finished with the bill still sitting unpaid does not count as closed to me"; L1/L10 by pinning the turn as "moved out in the middle of June with a target-ready date at the end of the month" (recbd087's exact distinguishing content); L31 by pre-scaffolding "if it is not, say so plainly and hold it"; L9 by naming "a re-inspection on the calendar for the middle of this month, and it factors into whether I can call this one done." The universe traps (recc8534 later-created selReady decoy, two done-flavored maintenance tickets, unpaid QB bills, 7/15 event) are all real and well-built — the prompt simply spent every one of them by naming it.

**Council blind spot (rules 18-20).** S1/S2/S3 grounding + adversarial + AUDIT_prompt (all 12 sub-dims 5/5, zero blocker) + FINAL all cleared this prompt and endorsed the 0/6 triad; none modeled that a competent Opus run reads the prompt's own reconciliation clauses as the solution. The strict minimizing-agent sketch in AUDIT_prompt projected ~21 tool calls but did NOT project ~20/20 rubric pass. Lesson: a stump hypothesis is a claim about withheld inference; validate it by tracing each rubric discriminator back to the prompt and asking whether the sentence that motivates the write also states the answer. If it does, the lever is dead regardless of how well the universe is trapped. Routed to PIPELINE REDO.

## 2026-07-27 - Task 45 (StarPM V4) S4 CALIBRATION DELTA: too easy, routed to REDO

The FINAL-pass lever design above (L2 symmetric + L1/L10 Opus-selective + L31 Gemini-selective) fired **0/4** on the real dual-model run. Opus passed 20/20 on all six runs (pass@1 **100%**); Gemini 3/6 (pass@1 50%); overall 75%. Machine verdict REBUILD_CANDIDATE_DIFFICULTY. T3 PASS (0/12 errored). Density: Opus 37.0 THIN (<40 design, >15 floor), Gemini 43.3 PASS.

**Root cause: 5_Prompt.txt named every rubric discriminator, so every engineered lever was pre-solved.** It defined the billed-but-unpaid trap in the prompt body ("finished with the bill still sitting unpaid, does not count as closed to me" -> L2 handed over verbatim), pinned the live turn by its mid-June move-out / 6-30 target content (-> L10 supersession disambiguation removed), pre-scaffolded the hold/negative path ("say so plainly and hold it" -> L31 given away), and named the 2026-07-15 re-inspection as a gating factor (-> L9 given away). The universe traps (recbd087 selProg vs decoy selReady recc8534 created LATER; two done-flavored maintenance tickets; unpaid QB bills $387 + $1,340; future QC event; past-due target) were all real and well-built. The prompt spent them.

**Calibration lesson:** for this lever triad the load-bearing variable is the prompt's information content, not universe trap density. The banked StarPM dual-model 0/6 triad (Learnings item 11) is only as strong as the inference the prompt WITHHOLDS. A QC-hold prompt must ask for the determination WITHOUT defining billed-but-unpaid, WITHOUT enumerating the scopes, WITHOUT pinning the turn by its dates, WITHOUT naming the re-inspection. Rubric set graded clean (0 Bucket-1 / 0 Bucket-2) -> REDO rebuilds the PROMPT, not the rubrics.
## Entry — Tasks/46_6a62ccb6ce2323b4b9e0c8d8 — 2026-07-28 (StarPM V4, PREDICTED)

**Anchor:** OPS-10 "Mid-Year Owner Portfolio Reviews - June 2026" (state Backlog), Lisa Smith owning two of four owners (Harry Harris, Robert Finley), deadline end-of-June against a universe today of 2026-07-01.

**Levers selected (5):** L1 latching on the persona's own undispositioned claim · L2 structured-DB skip (QuickBooks receivables + a 100%-unmirrored Calendar) · L10 reversal/supersession (double-booked Harris review; OPS-10 state against its own narrative; OPS-93 "Approved and Closed" sitting in Todo) · L11 net-vs-gross (117 unapplied credit memos) · L7 multi-write. L5 and L6 carried as sub-levers, not independently graded.

**Two methodological choices worth banking, both departures from the playbook default.**

First, **the banked StarPM dual-model triad was NOT used.** Its Gemini-selective leg (L31 negative directive) is falsified — 12/12 pass across three Task 44 gradings — and its Opus-selective leg was one of the four levers that missed 0/4 on Task 45. Substituted the two shapes that survived three gradings instead: the persona's own undispositioned observation (6/6 Opus pass, 6/6 Gemini fail, 0 of 48 cells moved) and duplicate records in differing workflow states (0 of 12). Whether a plan built on the *confirmed* shapes outperforms one built on the *catalogued* triad is the open question this task tests.

**Second, scenario shape was selected for density before content.** Per-model averages across six prior StarPM tasks show single-entity scenarios landing 33-48 per model (39: 33.0/43.5 · 40: 40.0/41.5 · 41: 38.8/48.0 · 43: 36.8/41.7 · 45: 43.3/37.0) and straddling the 40 gate, while the one multi-entity portfolio sweep (44) reached 79.8/62.5 and was the only task to clear 40 on both models. Density on this universe is a property of enumeration breadth, not of effort — so a two-owner enumeration was chosen over any single-unit framing before the levers were picked. Projected Opus 63.5 / Gemini 66.0.

**Also banked: the Gemini-minus-Opus delta flips sign with enumeration breadth.** Gemini runs below Opus on all four single-entity tasks and well above on the one multi-entity task. Gemini's call count scales with explicit enumeration, Opus's with reasoning depth. Useful for projecting per-model density on any future V4 task.

**Ambiguity exclusions recorded (F7):** Mesa Vista 207A and 4C each carry simultaneous selProg and selReady rows; Las Palmas 204B has 53 rows and Las Vistas 311A has 15; bare "Unit 14" is a 7-row, 6-label collision spanning at least two properties. Safe carriers are Mesa Vista 107A and 310C, and the whole Sunset Ridge cluster (7 rows, 3 units, zero Ready).

**Universe note for future StarPM tasks:** the documented near-duplicate *filename* decoys do not exist in this universe at all — zero `.pdf` strings, zero Gmail attachments, all Slack `files_json` empty, no filesystem service. They materialise as QuickBooks `DocNumber` values (45 families with suffixed children, 8 sharing an identical `TotalAmt` with their base). A lever written against a filename finds nothing.

**Actuals: pending S4.**
