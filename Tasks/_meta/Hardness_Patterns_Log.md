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

## Entry — Tasks/38_6a5edd95a6946f6c4d160b5a — 2026-07-22 (FINAL PASS, pre-trajectory)

**Persona / Business function:** Denise Morales (Onsite Property Manager, p_013) / Property Operations (StarPM universe)

**Selected levers (5) — confirmed end-to-end through FINAL_council.md:**
- L9 (Universe-grounded gotcha / authority-figure dismissal) — Tony Reyes (Lead Maintenance Technician) assessed Sunset Ridge 208B AC as dirty clogged filter via Slack, with Thursday fix; Alamo HVAC formal inspection email confirms compressor failure. Agent trusting Tony's authority misses the inspection result. Projected ~5/6 fail rate.
- L11 (Net-vs-gross framing) — Two QB vendor bills (2026-481 and PD-2026-084) each $8,400 for the same Big Bend Restoration roof job superficially read as $16,800 gross. PrivateNote on each bill (only in QB, not in email/Slack) confirms they are the same scope / AP-to-AR pass-through. Correct net = $8,400. Projected ~4/6 fail rate.
- L2 (Structured-DB skip) — Ridgeview reconciliation ground truth lives entirely in QB PrivateNote fields. Email + Slack anchor "$8,400 approved scope" but do not disclose the dual-bill structure or pass-through relationship. Correct answer not reachable without QB entity query.
- L8 (Multi-link chain, 5 hops) — Airtable tblMakeReady -> tblMaintenanceTickets MT-2026-047 -> QB bill 2026-481 -> QB bill PD-2026-084 (pass-through restatement) -> QB payment 972286822645 ($640 applied to separate vacancy invoice DocNumber 5848). Each hop in a different service.
- L6 (Near-miss entity confusion) — Seven Airtable "Unit 14"-flavored tblMakeReady records (Rio Bend variants, Sunset Ridge Unit 14, plain Unit 14 rows, Unit 14 Tanya Mitchell Eviction) mask Tanya Mitchell's actual unit Las Palmas 4B. Authoritative record rec769c9f03f0b85f and Slack C003 both confirm Las Palmas 4B. Projected ~3/6 fail rate.

**Additional lever active (not in original 5-lever selection):**
- L1 (Latching) — Tanya Mitchell has a parallel ESA reasonable-accommodation track (Slack C002) alongside the eviction/delinquency track (Slack C003 + Airtable). Agents latching on the first narrative found will miss the ESA track. Projected ~2/6 fail rate.

**Stump hypotheses (4) — projected failure modes:**
1. [HIGH] Agent reports 208B as "dirty filter / Tony Thursday fix" instead of "compressor failure" — L9.
2. [HIGH] Agent reports Ridgeview roof exposure as $16,800 (gross double-count) — L11 + L2.
3. [HIGH] Agent identifies Tanya Mitchell's unit as "Sunset Ridge Unit 14" or "Rio Bend Unit 14" — L6.
4. [MED] Agent omits Tanya Mitchell's ESA request from the Aurora brief — L1 latching on eviction track.

**FINAL verdict:** PASS. Validator 0 fails all phases. All 5 levers confirmed end-to-end (prompt sentence -> OE step -> rubric chain) in FINAL_council.md. 22 outcome / 0 process rubrics. THIN_DENSITY at ~43 midpoint (40-49 range), per-task justification carried (5 stump vectors + ESA lever). Lens 6: 0 HIGH Bucket 1 risk; 5 LOW-MEDIUM risk on AR/receivable terminology and bill-ID specificity — all below REVISE threshold.

**Pipeline note:** Prior FINAL blocked on OE21/OE22/OE25 referencing non-existent invoice 2026-494. Corrected: OEs now route owner-exposure path through QB bills 2026-481 + PD-2026-084 exclusively. Rubrics [7], [8], [9] use "AR receivable/balance" terminology while OEs use "billing exposure" — narrow terminology gap flagged as LOW-MEDIUM Bucket 1 risk; not changed since property management context treats them as synonymous and evidence fields have soft phrasing.

**Actual failures (from S4_verdict.md — dual model: Opus 4.8 + Gemini 3.5-flash, 12 total runs):**

| Rubric | Pass count | Bucket | Mechanism |
|---|---|---|---|
| R9 Linear $640 not applied | 0/12 | Bucket 3 AF | L8 chain final hop never queried |
| R13 Gmail Las Palmas 4B | 0/12 | Bucket 3 AF | L6 near-miss entity confusion |
| R15 Gmail plan through July | 0/12 | Bucket 3 AF | Cascade from R13 |
| R18 FR $8,400 outstanding | 0/10 confirmed + 2 uncertain | Bucket 3 near-AF | L2 + L11 AR-qualifier omission |
| R19 FR $640 not applied | 0/12 | Bucket 3 AF | Cascade from R9 |
| R20 FR Las Palmas 4B | 0/12 | Bucket 3 AF | L6 cascade from R13 |
| R21 FR plan through July | 0/12 | Bucket 3 AF | Cascade from R20 |
| R6-R8 Linear Ridgeview (partial) | 2-8/12 fail | Bucket 3 partial | L2 + L8 QB reconciliation incomplete |
| R11 Gmail compressor | 4/12 fail | Bucket 3 partial | L9 fired on O1 + early-termination Gemini runs |
| R14 Gmail ESA | 8/12 fail | Bucket 3 partial | L1 latching on eviction track |
| R22 FR ESA | 10/12 fail | Bucket 3 partial | L1 latching cascade |

Bucket 1: 0. Bucket 2: 0. Bucket 3 AF: 7. Bucket 3 partial: 15.
All-Failing Rubrics sub-dim: 5/5 PASS (0/7 = 0% Bucket 1 ratio).
T2: pass@1 = 0/12 = 0% PASS. T3: 0/12 erroneous PASS. Density: avg 57.6 tool calls PASS.

**Calibration:**

- **L6 near-miss entity confusion (Tanya Mitchell / Las Palmas 4B):** CONFIRMED and EXCEEDED. Predicted ~3/6 Opus fail; actual 0/12 across both models. Seven Unit 14 decoys including "Unit 14 - Tanya Mitchell Eviction Track" anchored every run. The named-persona decoy variant is far stronger than a generic unit-number decoy pool. Reclassify L6 with named-persona decoys as HIGH-confidence in future Hardness_Plans.

- **L2 + L8 structured-DB skip + multi-link chain ($640 payment):** CONFIRMED and EXCEEDED. Predicted ~4/6 fail on gross/net framing; actual 0/12 on the payment attribution step and ~10/12 on the AR outstanding qualifier. The 5th hop (payment record lookup) was never reached in any run. The QB chain depth (5 hops) was sufficient to exhaust agent follow-through.

- **L1 latching (ESA omission):** CONFIRMED and EXCEEDED. Predicted ~2/6 fail; actual 8/12 (Gmail) and 10/12 (final response). The parallel ESA track in Slack C002 was systematically missed once agents established the eviction/delinquency narrative from Airtable and Slack C003.

- **L9 authority-figure dismissal (208B compressor):** OVER-PREDICTED. Predicted ~5/6 fail; actual 1/6 Opus fail (O1 only), 1/6 Gemini fail via early termination (G6), not L9 mechanism. Opus runs O2-O6 found the Alamo HVAC formal email. In a dual-model starPM setting the authoritative HVAC email is reachable via Gmail search and Gemini's broader exploration surfaces it before Opus's Tony-authority anchor takes hold. L9 fail rate in dual-model verification is ~1-2/6, not ~5/6.

- **L11 net-vs-gross:** CONFIRMED. R17/R18 partial and near-AF show the net vs outstanding AR distinction fails consistently. The single-job ($8,400) framing is grasped by agents but the AR-outstanding qualifier is dropped.

**Levers that fired as predicted:** L6 (EXCEEDED), L2 + L8 (EXCEEDED), L1 (EXCEEDED), L11 (CONFIRMED partial).

**Levers that did NOT fire:** L9 (over-predicted at ~5/6; actual ~1/6 Opus).

**Failures from un-predicted sources:**
- Payment attribution (DocNumber 5848 vs roof AR): the 5th hop in the reconciliation chain was never reached in any run. The chain depth itself is the stump mechanism -- not a new lever, but confirmation that 5-hop chains reliably lose agents at the final hop when prior hops return partial-but-satisfying data.

**Lesson for next task (StarPM):**
- L6 near-miss entity confusion with 7+ Unit 14 decoy records and at least one named-persona decoy row is the highest-confidence stump lever on StarPM property management tasks. It fires at ~100% in dual-model verification. Prioritize it in future Hardness_Plans.
- L9 authority-figure dismissal requires the authoritative evidence to be hard to surface (e.g., buried in a thread, not reachable by a direct Gmail search). When the authoritative email is discoverable via a keyword search in a distinct service, Opus often finds it. Pair L9 with an evidence-surfacing cost (L4 search-cap eviction or a non-obvious search term) for StarPM tasks.
- The "owner receivable" vs "billing exposure" terminology gap remains a risk: ensure QB AR invoice records exist in the universe if rubrics use "receivable" language, or align rubric terminology with OE language ("owner exposure" / "billing obligation").
- Task 38 (StarPM, Denise Morales/Onsite PM brief) — 5 levers preserved end-to-end after 2-round FINAL: L9 (Tony vs Alamo HVAC compressor authority-dismissal), L11 (Ridgeview roof $8,400 net vs $16,800 naive-sum trap), L2 (structured-DB skip / PrivateNote-only reconciliation), L8 (Airtable→MT→2×QB bill→payment 5-hop chain), L6 REFRAMED as record-freshness discriminator (Unit 14 canonical from 2026-07-01 record recc83c05d889b354; older Las Palmas 4B record rec769c9f03f0b85f is pre-breach/superseded). Density PASS ~52-54.
- **Task 39 (6a602c895d0b0ab6551a3a86)** :: StarPM V4 :: Jaime Salinas / QC :: L1 (latching on Airtable selReady) + L8 (multi-link chain 3× OPS-2XX closures across Airtable → Linear → Slack → Gmail) + L9 (StarPM parameter traps — message/body/team) + L25 (existing-output anchor trap — fldTurnStatus=selReady blocks write cascade) + L26 (decoy parent thread — 6/16 QC-FAIL vs 6/18 CLOSEOUT parents in Slack + Gmail). Density midpoint 50.5. FINAL PASS 0/0/6.


## Entry — Tasks/39_6a602c895d0b0ab6551a3a86 — 2026-07-22

**Persona / Business function:** Jaime Salinas (QC Coordinator, p_011) / Quality Control and Field Services (StarPM V4)

**Selected levers (from Hardness_Plan.md):**
- L1 (Latching) — Airtable unit already in selReady state; agent may anchor on existing state and skip the sign-off write
- L8 (Multi-link chain) — 3 Linear tickets × comment + close, Airtable update, Gmail draft-reply, Slack thread reply, calendar event
- L9 (Parameter traps) — StarPM Gmail uses body (not content); Slack uses message (not payload); Linear uses team (not teamId)
- L25 (Existing-output anchor) — selReady state blocks write cascade
- L26 (Decoy parent thread) — 6/16 QC-FAIL Slack thread and older Gmail fail chain compete with canonical CLOSEOUT threads

**Density projection:** 40-61 tool calls, midpoint 50.5

**Actual failures (from S4 verifier-fails analysis — dual model Opus + Gemini, 12 runs):**

| Rubric | Pass count | Bucket | Mechanism |
|---|---|---|---|
| R16 Carlos draft threading | Opus 6/6 B3; Gemini 2/6 B3; Gemini 4/6 pass | B3 | All models draft to Carlos (correct to/cc) but fresh subject, no replyToMessageId d0e6f2c5b4a70b19 -- fails threading step. Gemini Runs 2/3/4/6 pass by using replyToMessageId; Opus all runs and Gemini Runs 1+5 fail. |
| R20 Slack closeout reply in Brooke's thread | 0/6 both models | Bucket 3 AF | thread_ts extraction failure: ts 1781788320.000202 visible in slack_search_public results on all 12 runs but never passed as thread_ts parameter. Top-level channel post produced instead. |
| R23 Calendar event (Opus Run 4) | FAIL 1 run | Bucket 3 | CronCreate (system cron scheduler) used instead of create_event; no calendar event created |
| R23 Calendar event (Opus Run 5) | FAIL 1 run | Bucket 2 | Judge error: create_event without calendarId — same omission as Run 6 which passed |
| R24 Calendar summary (Opus Run 4) | FAIL 1 run | Bucket 3 | Cascade from R23 Run 4 — no event created, no summary to evaluate |
| All Linear R1-R9 | 6/6 both | PASS | L1+L25 did not fire |
| All Airtable R10-R14 | 6/6 both | PASS | L25 did not fire |
| Gmail non-threading R15, R17, R18 | 6/6 both | PASS | L9 parameter traps did not fire |

**Calibration:**
- **Levers that fired as predicted:** L26 (partial HIT — Slack threading failure confirmed; actual mechanism is thread_ts extraction failure, not decoy-thread keyword competition; Brooke's ts was discoverable in search results in all 12 runs)
- **Levers that did NOT fire:** L1 (over-predicted; agents read completion comments and executed writes), L9 (over-predicted; correct parameters used throughout), L25 (over-predicted; selReady state not read as completed work)
- **Failures from un-predicted sources:** R16 two-action notification split (channel post + Carlos individual notification) stumped both models unpredicted. R20 thread_ts extraction failure is model-intrinsic — independent of whether a decoy thread exists.

**Hardness prediction hit rate:** 1/4 (25%)

**Lesson for next task:**

- **The Gmail thread-reply requirement (replyToMessageId to a specific canonical parent thread) is a HIGH-confidence stump for both models.** All models draft to Carlos correctly (content and to/cc); the failure is at the thread-find + replyToMessageId propagation step. Opus fails 6/6; Gemini fails 2/6 (B3) with 4/6 passing. Design guidance: requiring a thread reply to a specific discoverable parent is a dual-model stumping surface -- stronger against Opus but also catches Gemini on ~33% of runs.

- **Thread_ts extraction from Slack search results is a persistent Opus 4.8 failure mode that does not require a window constraint.** Agents retrieve the parent thread via slack_search_public, see the ts in the output, but do not propagate it as thread_ts in the send call. The WINDOW-CONSTRAINT THEORY IS DISPROVED for this task: Brooke's ts appeared in search results on all 12 runs. The actual gap is the ts-to-parameter propagation step. Design guidance: requiring a Slack thread reply to a discoverable parent thread (not necessarily buried by window depth) is sufficient to stump both models reliably.

- **L1 and L25 require ambiguous or missing completion signals to fire on StarPM tasks.** When a Linear issue has active named-person completion comments and an Airtable record has a clear action field, agents correctly interpret the status as "needs action." Future L25 deployments should pair the existing-output anchor with either no completion comments, a status label that reads as final (e.g., Resolved, Verified), or a prior write-action that partially satisfies the request.

- **L9 parameter traps (StarPM body/message/team distinctions) are not stumping surfaces in isolation.** Agents follow the tool catalog correctly when the task is otherwise clear. Pair L9 with a tool-variant trap (two tools for the same action, only one correct) to produce reliable failures.


## Entry — Tasks/39_6a602c895d0b0ab6551a3a86 — 2026-07-23 (FINAL v2 refresh)

**Follow-up to 2026-07-22 entry.** FINAL was re-run against updated `7_Rubrics.json` (26 rubrics vs prior 22; rubric edits landed 2026-07-23 03:13). Refreshed VERDICT and lever anchors below supersede the prior 0/0/6 summary line.

**Selected levers preserved end-to-end (unchanged from prior FINAL):**
- L1 (Latching on Airtable `fldTurnStatus=selReady`)
- L8 (Multi-link chain: 3 × OPS-2XX Linear comments + state flips + Airtable append + Gmail draft-reply + Slack thread reply + calendar event)
- L9 (StarPM parameter traps: `message` vs `payload`, `body` vs `content`, `team` vs `teamId`, `slack_send_message` vs `slack_send_message_draft`)
- L25 (Existing-output anchor: `selReady` + `fldNotes2` blanket "passed all items ... supervisory sign-off from Brooke Phillips" phrase composes the anchor)
- L26 (Decoy parent thread: 6/16 QC-FAIL parents in Slack + Gmail vs 6/18 CLOSEOUT canonical parent)

**Density:** midpoint 57.5 (Hardness_Plan.md). Realization-adjusted averages Opus 42.6 / Gemini 40.3 both above 40-call floor; Gemini margin thin, flagged for S4 monitor.

**FINAL Council verdict:** PASS (0 BLOCKER, 2 MAJOR, 1 MODERATE, 4 MINOR).
- MAJOR: rubric 18 Gmail thread lock-in + rubric 21 Slack thread lock-in. Both are intentional L26 discriminators; softening kills the lever. Held strict.
- MODERATE: rubric 25 Friday morning 07:00-11:00 CT window is over-specific vs prompt "Friday morning." Cheap widening to 07:00-12:00 available if any REVISE round is triggered.
- MINOR: Universe_Index timezone bug (America/New_York should be America/Chicago; non-artifact); rubric evidence without `Per OE#` citations (aligned with V4 spec that treats OEs as internal planning docs); Bennett-verify cross-check partial coverage (implicit via per-item scope references); thin Gemini density margin.
- Lens 6 Bucket_1_Risk: 3/26 = 11.5% (well below 20% threshold).

**Ship-eligible.** SUBMISSION_GATE is the next hard gate. Prior `SUBMISSION_GATE_report.md` in Council_Reports also predates the rubric refresh and should be re-run in a fresh chat.

## Task 39 (6a602c895d0b0ab6551a3a86) — StarPM V4 — 2026-07-23 FINAL PASS
Persona: Jaime Salinas (QC Inspector). Post-S1.5 lever set confirmed end-to-end through FINAL council: L1 (Airtable selReady latching anchor) + L8 (multi-link chain across Airtable + 3x Linear + Slack + Gmail + GCalendar) + L9 (StarPM parameter traps — `message` not payload, `body` not content, camelCase Airtable, no send-tool) + L25 (existing-output anchor via fldNotes2 supervisory retrospective) + L26 (decoy parent threads in both Slack #make-ready 6/16 QC-FAIL vs 6/18 CLOSEOUT-REQUEST, and Gmail 6/16 fail-notification vs 6/18 canonical closeout-package). L6 (HubSpot near-miss entity) REMOVED at S1.5 in response to platform linter cross-persona-scope block; density recovered via Bennett-per-ticket-verification amplifier + Airtable-pre-read amplifier + Sandra-contact-lookup soft levers. Density midpoint 57.5 (design target ≥ 50); Gemini realization margin +0.3 above 40-call floor documented as S4 attention item.

## Entry — Tasks/39_6a602c895d0b0ab6551a3a86 — 2026-07-23 (second REDO — density fail again)

**Persona / Business function:** Jaime Salinas (Quality Control Inspector) / Quality Control & Field Services — single-cycle QC closeout on Las Vistas 3C (Linear per-ticket signoffs + Airtable append + Gmail hand-off + Slack post + Google Calendar reminder).

**Selected levers (from Hardness_Plan.md post-S1.5 revision):**
- L1 — Latching (Airtable selReady anchor already contradicts Linear In Review tickets)
- L8 — Multi-link chain (3x Linear + Airtable + Slack + Gmail; HubSpot dropped in S1.5)
- L9 — Universe-grounded gotcha (StarPM param traps: Slack `message`, Gmail `body` + draft-only, Linear `save_comment`, Airtable camelCase)
- L25 — Existing-output anchor trap (Airtable Ready blocks write cascade)
- L26 — Decoy parent thread (Slack 6/16 QC-FAIL vs 6/18 CLOSEOUT-REQUEST; Gmail parallel decoy)

**Actual failures (from S4_verdict.md):**
- R20 (Gmail thread under Brooke 6/18) — Bucket 3 Opus 6/6; Gemini R1/R3/R5 Bucket 3; Gemini R2/R4/R6 pass. Model-divergence.
- R24 (Slack thread_ts under Brooke 6/18) — Bucket 3 both models 12/12. L26 landed at 100% failure rate.
- R28 (Calendar on jaime.salinas@starpm.com) — Bucket 2 Opus R1/R4 (judge inconsistency with Gemini's implicit-primary reasoning); Bucket 3 Opus R2/R3/R5/R6 (CronCreate wrong-tool selection).
- R29-R32 (Calendar detail rubrics) — Bucket 3 Opus R2/R3/R5/R6 cascade fail from CronCreate root cause.

**Calibration:**
- Levers that fired as predicted: L26 (Slack thread lever — hit at 100% both models; strongest lever in the batch)
- Levers that did NOT fire: L1 (agents did read the Linear tickets and acted on them despite Airtable Ready), L9 (create_draft, save_comment, slack_send_message all used correctly with right param names), L25 (Airtable update happened on every run despite Ready state)
- Failures that came from un-predicted sources: (a) Gmail replyToMessageId thread-find failure for Opus specifically — novel model-capability divergence. (b) Calendar-vs-cron tool-family confusion on Opus (CronCreate used in 4/6 runs instead of create_event) — novel Opus 4.8 stump not in the pre-registered predictions.

**Density outcome:**
- Projected midpoint (S1.5 revised): 57.5
- Actual: Opus 39.7 / Gemini 38.0 — BOTH below 40-call floor → SECOND consecutive density fail on this task
- L31 realization: 69% Opus / 66% Gemini — 5-4 percentage points below the calibration baseline (74% / 70%)
- Prior REDO batch was Opus 37.5 / Gemini 35.5; this REDO lifted envelope by +2.2 Opus / +2.5 Gemini but still underflows floor

**Lesson for next task:**
- The single-cycle QC closeout scenario is structurally thin on tool-call surface. Two REDO cycles have failed density in a row despite reasonable lever composition. Next REDO must materially expand the write surface (add a service + a discovery leg) OR escalate for scope reconsideration.
- **Calendar-vs-cron tool-family confusion** for reminder-adjacent Opus 4.8 asks is a NEW STUMPING PATTERN worth cataloging (add as lever candidate L37 or similar). When CronCreate and create_event are both in scope, Opus routes ~67% of runs through the system cron primitive instead of the personal calendar tool; a single wrong tool selection cascades to 5 rubric fails (R28 + R29 + R30 + R31 + R32). Not applicable to Gemini.
- **thread_ts extraction from search-result output** is a robust cross-model failure mode (100% fail both frontier models); worth elevating L26 to strong-recommend for tasks with multi-thread channel context.
- L1 + L25 (latching + existing-output anchor) need a stronger no-op cue than a status-field enum value to trigger. A superficially-final state field alone is insufficient; add natural-language "already handled" text in a visible artifact (Slack message, email) to trigger the no-op instinct.

## Entry — Tasks/40_6a61a86a31b9c973b2021ba5 — 2026-07-23

**Persona / Business function:** Carlos Mendez (Onsite Property Manager, p_009) / Property Operations (Cat 1)

**Selected levers (from Hardness_Plan.md):**
- Lever 1 — Latching (resolved Tommy Reyes / Linda Castillo Unit 14 water heater incident 5/15-5/27 as free L1 decoy — no injection)
- Lever 2 — Structured-DB skip on QuickBooks (bill 195836274018 Line[0].Description carries the load-bearing scope truth "Full unit replacement recommended, approx 1850 dollars"; totals view shows only $185.00 diagnostic charge)
- Lever 5 — Thread-reply blindness (Carlos-relayed parent ts 1782824160.000302 frames "small drip, no rush"; evening reply ts 1782863220.000303 flips to "no hot water, water pooling")
- Lever 7 — Multi-write diversification (8 writes across 5 services: Airtable update + Linear save_issue + Linear save_comment + Slack thread reply + 3 Gmail drafts + GCalendar create_event; expanded from playbook default 3 writes)
- Lever 8 — Multi-link chain (Slack tenant-relay → Airtable ticket → Linear issue → QB bill Line[0].Description; 4-hop cross-service triangulation)
- Lever 9 — Authority-figure dismissal (Tony Reyes Lead Maintenance Tech authority parent ts 1782789240.000301 endorses narrow scope "exchanger swap only, about 310 dollars, keeps us on Robert's June budget")

**Cleared end-to-end at FINAL:** All 6 levers preserved through Prompt + OE + Rubric artifact set per FINAL Lens 3 lever map; zero answer-leakage on "1850" / "full unit" / "Ruud" / "corrosion" / "burner assembly" / "cracked heat exchanger" across prompt body + injected Slack + injected Gmail (verified via grep).

**Actual failures (S4 verifier-fails analysis):** PENDING — platform 6-run trajectories not yet returned. To be back-filled after `PIPELINE S4`.

**Calibration:** PENDING — to be back-filled after `PIPELINE S4`.

**Density prediction:**
- Projected midpoint (Hardness_Plan generous): 56.0 (44-68 range)
- Projected midpoint (Council B v3 strictest): ~49-50 (THIN band 40-49)
- Projected midpoint (FINAL Lens 3 strictest per-service accounting): ~28-30
- Selected 6 levers (over default 4-5) specifically to buffer L31 real-run underflow pattern (Task 39 landed 35-37 despite 50.5 projected). L31 pattern is a real risk on this task.

**Lesson pre-registered for next task:** This is the third StarPM CB task in a row where strictest-lens density projection underflows the 40-call floor, despite generous accounting comfortably clearing 50. If Task 40 6-run avg lands below 40, the pattern becomes a STANDING PROJECT SIGNAL — StarPM CB scope surfaces need mandatory expansion beyond default 4-5 levers, and possibly a project-wide floor bump from 40 to 45 to reflect real-run underflow envelope. Escalation route on density fail: `PIPELINE REDO` with mandate to add a 7th lever (L3 missing-reply or L12 document-cross-reference StarPM adaptation).

## Entry — Tasks/40_6a61a86a31b9c973b2021ba5 — 2026-07-23 (S4 back-fill: platform 6-run trajectories returned)

**Follow-up to the 2026-07-23 entry above; back-fills the PENDING sections.**

**Actual failures (from S4_verdict.md):**
- 5 all-failing rubrics: Opus R23/R24/R25/R26 (Slack #maintenance thread post cluster, 6/6 each); Gemini R5 (Airtable description "active leak with occupants at home", 6/6).
- 8 partial-failing rubrics: Opus R4/R5/R20/R21 (1/6 each Run 1 thin-description slip); Opus R47 (2/6 Robert draft drops RS75); Opus R9/R10/R11/R12 (1-2/6 Linear write attrition); Gemini R21 (~3-4/6 same "occupants at home" atom drop); Gemini R9/R10/R11/R12 (2/6 Runs 4 & 6 no save_issue); Gemini R2/R39 (Run 4 attrition).
- Cross-model AF divergence: no rubric fails 6/6 on BOTH models. Opus AF cluster and Gemini AF are on different surfaces.
- Bucket 1 count: 0 hard defects (2 soft atomicity refinement suggestions on R5/R21 "leak with occupants" bundling, non-blocking).
- Bucket 2 count: 0 judge errors; all 59 verifier decisions matched independent trajectory walks.
- Bucket 3 count: all failing rubrics classify as legitimate model failures.

**All-Failing Rubrics sub-dim score:** 0/5 Bucket 1 ratio = 0% → 5/5 PASS.

**Density calibration (actual vs projected):**
- Opus avg 46.5 (min 37 max 57): THIN tier (40-49), above 40 floor. Prediction: Hardness_Plan generous 56.0 was OVER by 9.5; Council B v3 strictest ~49-50 was CLOSER (within 3); FINAL Lens 3 strictest ~28-30 UNDER by 16.5. The V3 THIN carry note was accurate to within a few calls.
- Gemini avg 32.3 (min 25 max 43): below 40 pipeline floor but above 15 QC floor. Treated as INFORMATIONAL parallel to Gemini pass@1 codification (commit `a342b8c`).
- Density did NOT block S4 completion; STOP was reversed after cross-check against QC criteria.
- Actual density lands at the strict-Council-B midpoint band, confirming the L31 real-run underflow pattern predicted for the third StarPM CB in a row.

**Difficulty calibration (actual vs 40% Opus gate):**
- Opus pass@1 = 0/6 = 0.0 → well below 40% gate. Gemini pass@1 = 0/6 = 0.0 (informational). Task strongly discriminates.
- Predicted 3 HIGH + 1 MED stump mechanisms; actual outcome: all 4 predictions OVER-PREDICTED on the specific mechanism, but 1 lever (L9 authority dismissal) shifted MODE from content-level to tool-target-level.

**Lever-by-lever calibration:**
- L1 Latching: OVER-PREDICTED. Both models correctly identified the resolved Unit 14 decoy as resolved and moved on. Closable decoys (with obvious closure metadata) are weak L1 anchors.
- L2 QB structured-DB skip: OVER-PREDICTED. Both models read the Line[0].Description field. Recent Opus 4.8 trained toward reading line-level fields on vendor bills.
- L5 Thread-reply blindness: OVER-PREDICTED. Both models called slack_read_thread on the tenant-relay parent and consumed the evening reply, lifting priority correctly.
- L7 Multi-write diversification: PARTIAL HIT. Multi-write attrition surfaced on Linear description writes for both models (R9-R12 partial fails). Not the AF driver but real friction.
- L8 Multi-link chain: HIT with SHIFT. Predicted the READ chain would break; the WRITE chain broke instead — Opus reads the whole chain correctly but then fails to write the reply back into the tenant-relay Slack thread.
- L9 Authority dismissal: HIT with MODE SHIFT. Predicted the agent would ACCEPT Tony's narrow-scope recommendation; instead the agent OVERRODE Tony's scope (content correct) but then failed to POST the correction back into the maintenance thread where Tony would see it. Opus specifically shows this Slack-thread-anchor stumble pattern: 4 runs skip the post, 1 run posts top-level (no thread_ts), 1 run posts to the wrong thread ts (the evening-reply ts, not the parent-tenant-relay ts).

**Novel findings for the lever catalog:**
- **L9 payoff can shift from CONTENT to TOOL-TARGET.** When an agent overrides an authority figure's recommendation on scope, the post-solve back-communication to that authority (posting into their thread) is where the lever can still pay off. Worth codifying as a variant: "L9-write" or "L9-thread-anchor".
- **Cross-model AF DIVERGENCE is a positive discrimination signal.** Opus AF cluster on Slack post; Gemini AF on Airtable safety atom. When both models fail 6/6 on non-overlapping rubrics, the task tests multiple discriminating axes rather than a single narrow one. Add to hardness playbook as a target pattern.
- **Gemini systematic atom-drop pattern.** When a rubric bundles two safety atoms ("leak with occupants at home"), Gemini reliably drops the secondary atom across the entire batch, on both Airtable and Linear surfaces. This is a persistent Gemini generation-style feature. Either split bundled rubrics or accept the systematic failure as Gemini-specific.

**Lesson updates for the standing project signals:**
- The "L31 StarPM CB density underflow" standing signal now has THREE data points: Task 39 REDO landed 35-37; Task 39 second REDO landed 39.7 Opus / 38.0 Gemini; Task 40 lands Opus 46.5 Gemini 32.3. Opus finally cleared 40 on Task 40 with 6 selected levers; Gemini stayed below 40. Pipeline maintenance follow-up: consider codifying Gemini density as INFORMATIONAL project-wide (parallel to Gemini pass@1), which is what this S4 applied.
- Runbook-wording follow-up: `Reference/Sessions/S4.md` opening paragraph needs update to reflect Gemini density is informational, not a REDO trigger. Current runbook literal reading conflicts with the Gemini-informational codification.
