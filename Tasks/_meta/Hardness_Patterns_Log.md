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

## Entry — Tasks/42_6a4fc1d98bf6758607609d35 — 2026-07-09

**Persona / Business function:** Lena Bjorkstrom (Software Engineer, MoveOps) / Engineering — incident response + multi-write coordination (ticket comment + Slack post + email to manager) after a billing mismatch caused by an invoice attachment safeguard she had deferred.

**Universe:** MoveOps (V2.1 framework). REVIEW task — 6 original trajectories present at intake.

**Selected levers (from REVIEW_hardness.md):**
- L1 — State resolution (ticket backlog state + assignee-field vs narrative-unassigned discrepancy + 5-comment thread with pre- and post-incident phases)
- L2 — Thread-depth email surfacing (Samira's April 15 email to Marcus + David, CC Lena — agent must find it in Sent/CC folder, not inbox)
- L3 — Cross-service Airtable Account-Manager discovery (Emeka's full book of business — Active+Onboarding filter on tblClientAccts01 yields 5 accounts, not just the 2 invoiced clients)
- L4 — Correction discovery (Emeka's April 22 correction emails already sent; agent must surface that remediation is in progress but not confirmed)
- L5 — Multi-write coordination (3 required write actions in the correct sequence: ticket comment establishing ownership BEFORE Slack announcement that ticket has new owner)

**FINAL-phase confirmation (post-MATERIALIZE, iteration 2):** All 5 levers confirmed firing end-to-end by cross-artifact Final Council after 3 FINAL iterations (REVISE -> REVISE -> PASS). Measured density 59.3 avg (6 real runs, PASS). VERDICT: PASS after iteration-2 blockers cleared.

**Actual failures (from REVIEW S4 bucket classification):**
- Rubric 1 (comment attribution to Lena): Bucket 1 (Rubric Invalid) — 5/6 runs. Platform Linear MCP overwrites author_id to authenticated account (moveops_alejandro_fuentes) regardless of user parameter passed. Rubric graded the tool-returned field; only Run 4 passed via body-signature "- Lena". FIXED at MATERIALIZE: rubric rewritten to grade body-text signature only.
- Rubric 10 (Emeka's 4 accounts): Bucket 1 (Rubric Invalid) — 6/6 runs. Prompt paragraph 4 pronoun-bound "those accounts" to Sunbelt+Palmetto only; rubric expected {Sunbelt, Palmetto, GreenStack, Mosaic} which no agent discovered. FIXED at MATERIALIZE: prompt widened to explicit "active and onboarding client relationships from the account records"; rubric rewritten to the 5-account Active+Onboarding set {Sunbelt, Palmetto, GreenStack, Tideway, Mosaic}.
- Rubric 11 (Samira April 15 email): Bucket 3 (Legit AF) — 1/6 runs. Agent legitimately missed the email due to narrow inbox-search filter.
- Rubric 15 (corrected client comms): Bucket 3 (Legit AF) — 2/6 runs. Agents legitimately missed Emeka's April 22 correction emails due to narrow Sent-folder search.

**Calibration:**
- Levers confirmed end-to-end (post-MATERIALIZE): L1, L2, L3 (repaired), L4, L5.
- Levers that did NOT fire on original artifacts: L3 — under-triggered by prompt paragraph 4 pronoun binding; 0/6 agents made the Airtable Account-Manager discovery. FIXED by widening prompt.
- Failures from un-predicted sources: Platform Linear MCP author_id overwrite (structural platform constraint invisible at design time). Not a rubric design error per se — but surfaces when rubric grades tool-returned metadata rather than message content.

**Lesson for next task:** (1) Platform Linear MCP overwrites `linear_create_comment` author_id to the authenticated account regardless of the `user` parameter — always grade comment attribution from body-text signature, never the tool-returned author_id field. (2) When widening a prompt to expose a lever, verify the rubric's expected entity set matches an actual derivable filter BEFORE committing to a numeral in the prompt — the "four accounts" count leaked in the prompt and simultaneously mismatched the universe's Active+Onboarding partition (which yields 5, not 4).

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


## Entry — Tasks/38_6a4e9f9a28328f89d031fd66 — 2026-07-09

**Persona / Business function:** Sofia Reyes (Senior Processor, Title/Insurance/Compliance) / Loan Operations. Keystone universe.

**Persona-swap context:** Task 38 was originally scoped to James Thornton (FHA/USDA Loan Officer). Initial HARDNESS run STOPPED at INSUFFICIENT_LEVERS (0/5) + INSUFFICIENT_DENSITY (23.5/40 realistic). James has no named scenarios (per PersonaBrief, "stable baseline"), 0 sent emails, 0 sent Slack, no CRM structured presence — every Learnings-validated failing lever starved. Operator swapped persona to Sofia Reyes (same business function, Loan Operations) per v1 plan's `## Persona swap recommendation` section. Universe unchanged. v1 plan archived at `_aux/Hardness_Plan_v1_james_STOP.md`.

**Selected levers (5) — from v2 Hardness_Plan.md:**
- Lever 1 — Latching (Learnings L13): PersonaBrief anchors Sofia on 9 loans; Slack chatter (C002) + email subject clusters reinforce
- Lever 2 — Structured-DB skip (Learnings L10 mechanism generalized; L11 skip-vs-conversation trade): `mortgage_los.loans.assigned_processor` filter reveals only 1 of 9 brief-named LNs is actually Sofia's (LN-2026-00613); load-bearing target is her actual 2 outstanding conditions on LN-2026-00008
- Lever 7 — Multi-write diversification (Learnings L5, density-only): 5+ writes across 5 services (email + Slack + LOS condition update + CRM engagement + calendar); task-adjusted range 12-15
- Lever 8 — Multi-link chain (Learnings L14): Grace DM re LN-2026-00619 -> LOS assigned_processor lookup (contradicts Slack framing) -> CRM engagement trail (`crm_engagement_9c1b4dd91ef8`) -> outstanding conditions on LN-2026-00008
- Lever 9 — Authority-figure dismissal (Learnings L9 ~100% fail, single most effective; L24 soft-verb caveat): Grace-voiced (128 msgs, `keystone_e304643b171b`) or Camille-voiced directive

**Density:** projected midpoint 50.0 (at PASS floor). PASS band contingent on S1 drafting 5+ writes to hold L7 at 12-15 range. If only 3 writes: midpoint collapses to 47 (THIN).

**Service breadth (v11 G1):** 5 distinct services >= 5% (mortgage_los 34%, email 24%, slack 18%, crm 12%, contacts 8%). Dominant mortgage_los well below 60% ceiling. PASS.

**Load-bearing stump surface:** PersonaBrief-vs-LOS-ledger contradiction. Sofia is anchored on 9 loans in brief, only 1 in LOS truth (`assigned_processor` filter). Universe-authored discrepancy — S1 must preserve without editing. Learnings L29 escape-valve caveat: do NOT include "if what you find changes the read, tell me" clause in S1 — it neutralizes the L2 skip on the load-bearing surface.

**Actual failures (from S4 verifier-fails analysis):** pending — trajectories not yet run.

**Interim lesson (pre-trajectory):** Persona swap within the same business function unlocked 0 -> 5 levers on the same universe (Loan Operations, Keystone). Calibration signal for future thin-persona tasks: when INSUFFICIENT_LEVERS fires on a persona explicitly authored as "stable baseline / no named scenario involvement", the persona-swap fallback (documented in the v1 plan's swap-recommendation section) reliably surfaces a viable alternative persona within the same business function without editing the universe. Cross-task pattern to track: does the swap consistently unlock >= 3 Learnings-validated failing levers when the swap target has >= 500 graph-report mentions and >= 5 named scenarios?


## Entry — Tasks/38_6a4e9f9a28328f89d031fd66 — 2026-07-09 — FINAL PASS

**FINAL Council verdict:** PASS. All 6 lenses clean (Truthfulness / Rubric Binding / Cross-Artifact Holism / Red-team / Narrative-State + Action-Prescription / Verifier-Fails-Spec). All 12 hard rules PASS. 0 answer leakage. 0% Lens 6 Bucket_1_Risk.

**Levers confirmed end-to-end (prompt -> OE -> rubric):**
- L1 Latching — prompt paras 1-2 anchor Sofia on brief-named LN-2026-00619 (Grace) + LN-2026-00610 (Destiny Pham via Camille speakerphone); OE 5 verifies both against LOS `assigned_processor` (neither is Sofia); rubrics [8]/[9]/[14] score the LOS-authoritative path (LN-2026-00008)
- L2 Structured-DB skip — prompt para 2 "the real state, not the impression"; OE 6 pulls Sofia's 143-loan pipeline via `mortgage_los_get_pipeline(assigned_to=los_staff_afc9caafae9d)`; rubrics [8]/[14] score the 26-open-loan count
- L7 Multi-write diversification — 5 writes across 4 services (email OE 11, LOS condition updates OE 12+13, CRM engagement OE 14, LOS activity OE 15, Slack post OE 16); density midpoint 50 at PASS floor
- L8 Multi-link chain — Grace DM + Camille speakerphone (OE 2/3) -> LOS assigned_processor lookup (OE 5) -> Sofia's actual pipeline (OE 6) -> outstanding conditions on LN-2026-00008 (OE 7-8) -> borrower outreach (OE 11)
- L9 Authority-figure dismissal — Grace + Camille voice in prompt para 1 with soft verbs ("watching 00619", "got Carlos and me on speakerphone"); prompt para 2 counters with "not the impression from what people are messaging me about"; rubrics reward LOS-authoritative path, not authority-implied path

**Density confirmed:** integrated midpoint 50 (Hardness_Plan target; PASS floor per Reference/Council_Protocol.md B3 SSOT).
**Service breadth confirmed:** 5 services >=5% (mortgage_los 34%, email 24%, slack 18%, crm 12%, contacts 8%). Dominant mortgage_los well below 60% ceiling.

Task cleared for platform upload. Awaiting 6-run trajectories for S4 verifier-fails classification.

## Entry — Tasks/38_6a4e9f9a28328f89d031fd66 — 2026-07-09 — S4 CALIBRATION

**Levers actually engaged (across trajectories):**

- **L1 Latching — partial engagement.** Fired via a DIFFERENT sub-mechanism than predicted: not brief-named-loan latching but "dead files" heuristic latching. Agents anchored on the "closed and dead files don't count" prompt phrase and imputed dead status to open-status 2024-2025 loans.
- **L2 Structured-DB skip — partial engagement.** Fired in the form of conflating document_checklist_items with LOS conditions (Rubrics 8 + 10, 5/6 fail each). Agents broadened "outstanding items" to include any doc/HOI item on the file instead of narrowing to the LOS conditions filter.
- **L7 Multi-write diversification — density delivered.** 91.2 avg tool calls, +82% over the 50 target. Density plan hit and exceeded.
- **L8 Multi-link chain — engaged but survived.** All agents traversed the Grace/Camille -> LOS -> conditions chain correctly on the identity/borrower/condition-id side. The chain did NOT trip anyone up in the way L8 typically operates.
- **L9 Authority-figure dismissal — did not fire.** Agents did not defer to Grace/Camille voice on write scope. L9 was over-weighted in the plan.

**Levers NOT in the Hardness_Plan that dominated:**

- **L-industry-native-suppression (new).** Appraisal condition treated as internal by every agent (R3, R5, R12 partial). Real-world mortgage-industry lifecycle (appraisal ordered by lender) overrode the LOS condition status. Highest hit rate of any lever on this task (6/6 fails on 2 rubrics + partial on a third).
- **L-industry-native-status-override (new).** Dead-file heuristic override on LOS `status` field (R9 all-fail + R14 partial). Prompt phrasing "Closed and dead files don't count" gave the soft cue; agents took it as license to drop 2024-2025 open-status loans.

**Density verdict:** projected 50 midpoint, actual 91.2 avg. Density model UNDER-projected by 82%. Loan-Ops tasks with 5+ writes across 5+ services routinely produce 80+ tool calls in practice. Consider raising density projections for similar future tasks.

**Rubric quality verdict:** 5/5 All-Failing sub-dim. Zero rubric-invalid classifications. Trajectory-diagnosed failures are all legitimate model reasoning gaps.

**Cross-task pattern to track:** on the next 3 Loan-Ops tasks, explicitly enumerate industry-native reasoning shortcuts (appraisal-as-internal, HOI-as-internal, title-as-internal, dead-file heuristic, aged-file relative-time compression) as first-class stump hypotheses alongside the classical Learnings-catalog levers. If they consistently outperform L1/L2 in raw fail-rate, formalize them as L-industry-native-* levers in the Hardness_Playbook.

## Entry — Tasks/38_6a4e9f9a28328f89d031fd66 — 2026-07-09 — S4 CALIBRATION (post-fix rerun)

**Post-fix rerun of the same task after prompt + rubric fixes were applied.**

Rubric count now 13 (was 14; R5-old appraisal condition update was deleted). Fixes applied:
- Prompt §3: "outstanding items" narrowed to "outstanding condition on the borrower's side"
- Prompt §7: pipeline bound to five open LOS statuses (closed / denied / withdrawn excluded)
- R3 (email appraisal FYI): $291K anchor no longer required in the email body
- R8 (Slack 26-loan roster): 26-loan enumeration moved to evidence + tolerance widened to +/- 2 days
- R9 (final sole-outstanding): reshaped
- OE 15: `follow_up_reminder / reminder_set / or similar` -> `follow_up_scheduled`

**What the fixes resolved (previously all-failing, now resolved):**

- **Slack 26-loan roster:** was 0/6 pre-fix (all-failing), now 6/6. Moving the enumeration to evidence with +/- 2 day tolerance fully resolved the dead-files heuristic override.
- **26-count in final response:** was 3/6 pass pre-fix, now 6/6. Binding the pipeline definition to the five open statuses removed the ambiguity that let the dead-files heuristic drop 2024-2025 loans.
- **Appraisal condition update:** was 0/6 pre-fix (all-failing), now removed from the rubric set.
- **Appraisal FYI in email:** was 0/6 pre-fix (all-failing), now 1/6 (passes Run 3). No longer AF. Softened FYI framing is passable.

**Novel stump surfaces first observed on the rerun (not in original Hardness_Plan):**

- **Compliance-hold hallucination (Runs 2 and 6).** Agents invent a "compliance review hold" or "breach-response communications hold" on LN-2026-00008 with no supporting universe artifact. Origin: KeyStone universe has a Slack C003 spoofed-wire incident on LN-2026-00605 (unrelated file). Agents generalize the incident into a per-loan comms hold and withhold outreach to Yuki Wilson. Drove all fails in R1, R2, R4 for those runs and cascaded into R5, R6, R7, R9.
- **Cron-syntax two-day confusion (Runs 2, 3, 5).** Agents encode the two-day follow-up as `day-of-month=11, month=7` (July 11) instead of `day-of-month=30, month=4` (April 30). Not a domain reasoning error — a raw cron-syntax bug. Runs 1 and 4 got it right (`3 9 30 4 *` and `47 8 30 4 *`).

**Confirmed on the rerun (already known from pre-fix):**

- **Appraisal-as-internal industry bias.** Even with the softened R3, agents still substitute HOI binder for appraisal in 4 of 6 emails and in 4 of 6 final responses. Only Run 3 correctly surfaced the appraisal as an FYI. Loan-Ops tasks reliably surface this bias.
- **document_checklist_items vs LOS conditions conflation.** Drove 8-file broadening in Runs 1, 4, 5 on R7 and R9. Even with the prompt qualifier "borrower's side", agents give equal weight to the checklist table and the conditions table.

**Hypotheses that MISSED again on the rerun:**

- **H1 (assigned-processor contradiction miss):** MISS on second run too. Every agent correctly ran the LOS filter. This lever is functionally dead on this task — the LOS query is too natural.
- **H2 (authority-figure deferral on write scope):** MISS. No agent mis-scoped a write to brief-named 00619 / 00610.
- **H3 (missing-reply / thread-hidden disposition):** NOT OBSERVED.

**Density verdict (rerun):** avg 92.3 tool calls (target 50+). Density remained ~2x the projection. Loan-Ops tasks with 5+ writes across 5+ services consistently produce 80+ tool calls.

**Rubric quality verdict:** 5/5 All-Failing sub-dim. Zero Bucket 1 classifications. Every failing rubric passes in at least one run.

**Cross-task pattern to formalize:** compliance-hold hallucination is a distinct stump surface from generic authority-figure deferral (L9). Agent picks up a real universe-authored incident on File X and generalizes it into a policy constraint on unrelated File Y. Worth adding to the lever catalog as **L-incident-generalization**: when the universe carries a real incident with a communications restriction on one loan, agents generalize the restriction to any loan that "feels similar" without checking whether the restriction actually applies. In this task, the LN-2026-00605 spoofed-wire incident generalized to LN-2026-00008 despite zero overlap (different borrower, different lender, different loan status, different incident).


## Task 38 (Sofia Reyes, KeyStone Mortgage) — post-fix S4 rerun — 2026-07-09

Post-fix trajectory pass: 6 runs, avg 92.3 tool calls, pass@1 = 0/6 = 0.0%. All 10 failing rubrics classified Bucket 3.

### Pattern: appraisal-as-internal industry bias (confirmed, robust across fix)

Even after the R3 evidence was softened to allow FYI framing without a $291K anchor in the email body, agents still substitute an HOI-binder ask for the appraisal contingency in 4 of 6 runs. Root cause is real-world mortgage practice — appraisals are lender-ordered so the agent's "borrower-provided item" instinct fills the slot with the next thing they know borrowers provide (HOI). Only Run 3 surfaced the appraisal FYI correctly. Drove R3 (5 fails) and R11 (4 fails) on this run.

**Carry-forward.** Any Loan-Ops task that requires the agent to surface both a borrower-provided and a lender-ordered condition in the same outreach faces this bias. Rubric-side mitigations available: (a) split the two items into separate atomic rubrics so partial credit is preserved, (b) soften evidence to accept any appraisal-adjacent mention including "we're finalizing on our end", (c) escalate to prompt-side by explicitly listing "the appraisal contingency is one of the two items" — but this crosses into pre-solving.

### Pattern: document_checklist_items vs conditions conflation (confirmed, robust)

Agents read `mortgage_los.document_checklist_items` (per-loan checklist rows) and treat any row marked "outstanding" or "missing" as a borrower-side outstanding item, broadening the LN-2026-00008 sole-outstanding claim to 8 files. Only Run 2 (correctly narrow) and Run 3 (correctly narrow) navigate the distinction. Drove R7 (5 fails) and R9 (4 fails).

**Carry-forward.** The KeyStone data model has two overlapping tables for "what's missing on this file" (`conditions` = underwriter-authoritative, `document_checklist_items` = processor-workflow). Future prompts on this universe should call out the specific table when the rubric is table-specific.

### Novel pattern: compliance-hold hallucination (first observed)

Runs 2 and 6 invented a compliance / breach-response communications hold on LN-2026-00008 with no supporting universe artifact. Root cause is generalization from a real Slack C003 incident-mode discussion of a spoofed-wire email on LN-2026-00605 — the agent extrapolates a per-loan comms hold policy that does not exist. Drove all R1 / R2 / R4 fails and cascaded into R5 / R6 / R7 in both runs.

**Carry-forward.** Any KeyStone task where the prompt tacitly asks the agent to send borrower email risks this hallucination when the universe contains ANY incident-mode Slack chatter (spoofed wire, TCPA complaint, breach alert). Consider either (a) removing incident-mode chatter from universes for outreach-heavy tasks, or (b) accepting the outreach-withheld path as a valid rubric alternative when incident chatter is present — but option (b) undermines the outreach-focused task design.

### Novel pattern: cron-syntax two-day confusion (first observed)

Runs 2, 3, 5 encode a two-day follow-up from 2026-04-28 as `day-of-month=11, month=7` (July 11) instead of `day-of-month=30, month=4` (April 30). This is a raw cron-syntax bug where the agent puts the "day" and "month" values in the wrong cron field positions. Runs 1, 4 hit the correct April 30 cron. Drove 3 of the 4 R6 fails.

**Carry-forward.** When the KeyStone tool catalog exposes a generic `CronCreate` scheduler alongside domain tools, agents default to the scheduler and hit this bug. Route reminder-style tasks to the domain tool (`mortgage_los_add_activity` with `follow_up_scheduled`) — the OE 15 fix already codified this as the KeyStone-native fit.


## Entry — Tasks/40_6a4f56f2a17df14b36807b01 — 2026-07-09

**Persona / Business function:** Reshma Patel (Firm Operations Coordinator) / HR & Operations Administration — Brookfield HR guidance close-out (settled vs open items on employee file handling + new starter access checklist).

**Selected levers (from `_aux/Council_Reports/REVIEW_hardness.md` — REVIEW-flow task, no `Hardness_Plan.md`):**
- Airtable-record discovery under non-HR-labeled base (record `airtable_ddadfe58b867` in `Client Access and Onboarding Admin` base; not HR-named)
- Cross-service investigation depth (8 services: email, Slack, Airtable, Records Vault, Linear, Reminders, Calendar, Contacts)
- Settled-vs-open discrimination across Yusuf / Rachel / Clint / Peter / Marina messages
- Anti-external-send anti-pattern (floor)

**Actual failures (from `_aux/Council_Reports/S4_verdict.md`):**

| Rubric surface | Fails / 6 | Classification | Mechanism |
|---|---|---|---|
| Stale HR-only policy reminder replaced | 3/6 (Runs 2, 3, 4) | Bucket 3 | reminders-service discovery gap (NEW — under-predicted) |
| Email states HR admin tracking was updated | 3/6 (Runs 4, 5, 6) | Bucket 3 | meta-confirmation sentence attrition (NEW — under-predicted) |
| HR files not in shared or team folders — tracking | 2/6 (Runs 4, 5) | Bucket 3 | phrase-specificity: agents wrote "restricted storage" without the shared-folder exclusion |
| HR files not in shared or team folders — email | 2/6 (Runs 4, 5) | Bucket 3 | same as above on email artifact |
| Standard access day-one gating — email | 2/6 (Runs 1, 4) | Bucket 3 | two-tier content completeness (NEW — under-predicted); half the split failed |
| Standard access day-one gating — tracking | 1/6 (Run 4) | Bucket 3 | same |
| Elevated access separate manager approval — email | 1/6 (Run 4) | Bucket 3 | two-tier content completeness (other half of split) |
| Elevated access separate manager approval — tracking | 1/6 (Run 4) | Bucket 3 | same |
| Airtable tracking title exact-match | 1/6 (Run 1) | Bucket 3 | Airtable-record discovery gap (predicted) — Run 1 substituted a Reminders record |
| Intake / exception approval routing unresolved — tracking | 1/6 (Run 1) | Bucket 3 | settled-vs-open misclassification (predicted) — Run 1 placed routing in Settled section |
| Stray-copies removal / containment — tracking | 1/6 (Run 4) | Bucket 3 | compound-AND preemptive split (fix #7); agent stated misrouted rule but skipped stray-copy rule |
| Packet-scope unresolved — email | 1/6 (Run 5) | Bucket 3 | settled-vs-open (predicted) |
| Packet-scope unresolved — tracking | 1/6 (Run 5) | Bucket 3 | settled-vs-open (predicted) |
| Legacy shared-drive cleanup unresolved — email | 1/6 (Run 6) | Bucket 3 | settled-vs-open (predicted) |
| Legacy shared-drive cleanup unresolved — tracking | 1/6 (Run 6) | Bucket 3 | settled-vs-open (predicted) |

**Density:** 46.3 avg total tool calls (range 39-55). Above the 40 floor, below the 50+ design target. THIN_DENSITY band. **Difficulty:** pass@1 = 0% on the 33-rubric expanded verifier-evaluated set (33.3% on the 22-rubric parsed reference set). Both hard gates PASS. **Verdict: SHIP if operator accepts THIN_DENSITY; otherwise consider a density-margin patch before re-upload.**

**Calibration:**

- **Levers that fired as predicted:**
  - Settled-vs-open discrimination — 5 fail instances across Runs 1, 5, 6 tracked exactly to the predicted mechanism.
  - Airtable-record discovery — Run 1 fired the title-match rubric; Runs 5 and 6 found the record but produced downstream content omissions (partial hit).
  - Anti-external-send floor — 0 violations across all 6 runs.

- **Levers under-predicted (add to catalog):**
  - **L-adjacent-service-discovery-gap** — the reminders-service replacement rubric failed 3/6 despite the Airtable-record-discovery lever being the named primary. Two similar-purpose services in one task systematically triggers a discovery gap on the secondary one.
  - **L-two-tier-content-completeness** — post-materialize atomicity splits on standard-vs-elevated access surfaced this as a discrete lever; Run 4 dropped one of the two tiers on both artifacts.
  - **L-meta-confirmation-attrition** — "email states tracking was updated" failed 3/6 despite runs producing clean summary bodies. Related to the L-final-response-depth-anchor pattern cataloged for Task 37 but on the email artifact.

- **Density:** projected 50+ (per REVIEW density-lift OE hardening fixes #9-#11), actual 46.3 (THIN band). Under-projected by ~4 tool calls. The explicit base/table discovery OE addition (fix #11) has not yet been platform-verified; expect a modest lift on the next trajectory cycle.

- **Bucket 1 collapse post-materialize.** The pre-materialize REVIEW walk found 5 Bucket 1 instances across 3 compound rubrics (rubrics 3, 13, 14 in the parsed set). MATERIALIZE atomicity splits eliminated all 5. Post-materialize the same 22 fail instances all classify Bucket 3. **This is a strong empirical proof point** that per-phase auto-AUDIT catching atomicity defects at the producing phase (as the pipeline hard rule 12 mandates) is materially cheaper than downstream S4 re-classification — the atomicity fixes were mechanical once identified, but classifying compound-AND fails against per-run trajectories is expensive.

**Lesson for next task:**

- **Adjacent-service-discovery** is a real Brookfield/KeyStone stumping mechanism when a task has both an Airtable admin tracking item AND a stale Reminders record. Two similar-purpose services in one task create predictable under-coverage on the secondary. Whenever a task's OE chain names both, ensure the OE prescribes the discovery walk for the less-obvious service explicitly.
- **Meta-confirmation sentences** in downstream artifacts are attrition-vulnerable. When the rubric requires "email states X was updated" or "final response confirms Y was filed", phrase the rubric evidence unambiguously and pin an atomic evidence example.
- **THIN_DENSITY operator-acceptance pattern reproduced.** REVIEW-mode tasks with density fixes applied at MATERIALIZE tend to land ~4 calls below the projected 50+ target. Consider prescribing an extra verification-read call in the OE post-materialize when the REVIEW density projection is between 44-49.

## Entry — Tasks/42_6a4fc1d98bf6758607609d35 — 2026-07-10 (S4 post-trajectory update)

**S4 run context:** New runs after REVIEW + MATERIALIZE fixes (prompt widened to Emeka's full book, CRM rubric expanded to 5 accounts, attribution rubric rewritten to body-text grading, JSON defect fixed).

**Actual failures (S4 new runs — post-MATERIALIZE):**
- R16 (5-account CRM+Airtable check): Bucket 3 (Legit AF) — 5/6 runs. Agents searched CRM by name (Sunbelt, Palmetto, Mosaic, Axiom, Tideway) but made zero Airtable calls. GreenStack Energy (recAcct000000003, Active) and Tideway Hospitality Tech (recAcct000000069, Active) never queried. Only Run 6 made the Airtable account-manager discovery step and passed.
- R15 (corrected comms - Emeka April 22 emails): Bucket 3 (Legit AF) — 1/6 runs (Run 3). Agent searched inbox + Sent at limit 30; Sent cutoff excluded April 22 corrections. 5/6 runs found them.
- R12 (Samira April 15 email): Bucket 3 (Legit AF) — 1/6 runs (Run 3). Agent searched "Samira" in inbox, did not identify the specific April 15 email among results. 5/6 runs found it.

**Calibration (post-MATERIALIZE):**
- L3 (Airtable AM discovery): CONFIRMED HIGH — fires 5/6 runs. Most reliable stumper on the task. Prompt widening preserved the lever; agents still do not perform the Airtable filter step without explicit column-level instruction.
- L4 (correction discovery): LOW-YIELD — fires 1/6 runs only. Most agents search broadly enough to find the April 22 emails after MATERIALIZE.
- L2 (email surfacing): LOW-YIELD — fires 1/6 runs only. Samira April 15 email easily found on "Samira" inbox search in 5/6 runs.
- L1, L5: did not fire (0/6) on new runs.

**Pass@1:** 16.7% (1/6 runs pass all rubrics). Difficulty gate: PASS. Density avg 59.3 total / 50.8 MCP: PASS.

**Lesson for next task:** When designing a cross-service account-discovery task in MoveOps, L3 (Airtable AM filter) is load-bearing and survives prompt widening. L4 (correction emails) and L2 (thread-depth email surfacing) are low-yield after prompt fixes because they are findable with standard inbox-search patterns. Reserve L4 and L2 as secondary levers and keep at least one L3-type cross-service discovery step as the primary stumper.

## Entry — Tasks/43_6a4f191dbdbe492d7e70af2d — 2026-07-10

**Persona / Business function:** Marcus Knell (Billing Coordinator) / Engagement Mgmt & Client Operations. Brookfield universe. New v47 seat; natural authoring seats Cat 1.4 (WIP-to-revenue) + Cat 8 (quarterly AR aging).

**Selected levers (5) — from Hardness_Plan.md:**
- Lever 1 — Latching (Learnings L13 + L9 authority-dismissal): George McAdam (1,407 universe artifact mentions, BlackLine exception identifier) voices the latching directive -- "the $4,390.62 is a BD3 feed-timing artifact, don't hold billing for it." Agent must self-discover the exception is NOT a timing artifact and net the figure correctly.
- Lever 2 — Structured-DB skip (Learnings L10): two approved-not-posted WIP JEs (`je_01de85923ce744ba` + `je_46e6033b6aa946e7`) on account 119000 (brookfield_FP-2026-05). Status=approved is NOT posted; agent must transition both before computing net billable WIP.
- Lever 7 — Multi-write diversification (density): 8 write actions across 7 services (oracle_gl JE post x2, blackline corrective JE, blackline update, records_vault upload, email Daniel Jones, slack C005, reminder).
- Lever 9 — Universe-grounded gotcha (Learnings L18 figure-is-the-rubric): correct net billable WIP = $29,454.31 (gross $33,844.93 minus $4,390.62 exception); George frames the gross as authoritative.
- Lever 11 — Net-vs-gross framing: gross WIP ($33,844.93) vs correct net billable WIP ($29,454.31). Load-bearing figure is the rubric.

**Density projection:** range 45-71, midpoint 58. PASS (>=50 design target).

**Service breadth:** 7 services >=5% (oracle_gl, sap_subledger, blackline, records_vault, email, slack, contacts). PASS.

**Actual failures (from S4 verifier-fails analysis):** pending -- trajectories not yet run.

## Entry — Tasks/43_6a4f191dbdbe492d7e70af2d — 2026-07-10

**Persona / Business function:** Marcus Knell (Billing Coordinator) / Engagement Mgmt & Client Operations. Brookfield universe. Scenario seat: May close billing-cycle owner deriving May WIP billing basis for Daniel Jones's June invoice batch.

**Selected levers (5) — from Hardness_Plan.md:**
- Lever 1 — Latching (L9 authority-dismissal): Marcus paraphrases George McAdam's steer that the submitted audit AR entry (je_1f83fec3cf0346db, $43,950.76) "covers the full billing cycle and is just waiting on the approver click." Agent must override via GL status check.
- Lever 2 — Structured-DB skip (L10 SAP invisibility): SAP subledger has zero mirrors for je_1f83fec3cf0346db (submitted, never cleared approval workflow). Two approved WIP JEs have 2 mirrors each. Absence-of-mirror is the second structural discriminator.
- Lever 7 — Multi-write diversification (L5 density): 5 writes across 5 services (email Daniel, Records Vault memo, Slack C005 post, calendar hold, reminder).
- Lever 8 — Multi-link chain (L8 analogue): 4-step derivation: George steer → GL status=submitted (blocked) → SAP absence-of-mirror → aggregate two approved 119000 WIP JEs → $33,844.93.
- Lever 9 — Universe-grounded gotcha (3 sub-traps): (a) JE lifecycle rule (submitted not billing-eligible); (b) account-role trap (wrong JE debits 110000 AR not 119000 WIP); (c) entity filter (northstar draft WIP chatter in C005 must be excluded).

**Density projection:** range 40-60, midpoint 50. THIN_DENSITY under strict-minimum reading (~42 realistic per AUDIT_prompt iter3b); operator accepted with per-task justification. OE-normal exploration hits 45-55.

**Service breadth:** 8 distinct services (oracle_gl, sap_subledger, contacts, email, records_vault, slack, calendar, reminder). PASS.

**Stump hypotheses:**
1. [HIGH] Agent emails $43,950.76 (trusts George's steer without GL status check) — Lever 1 + L9.
2. [HIGH] Agent never queries SAP subledger for submitted JE absence — Lever 2 + L10.
3. [MED] Agent treats status=submitted as effectively-approved — Lever 9a.
4. [MED] Agent sums revenue credits (401000+403000) instead of WIP debits (119000) — Lever 9b.

**Remediation history:** Previous attempt built around BlackLine exception exc_1ddfc978ce5a4d was poisoned — partner-approved disposition email (Hannah Grant) created a valid Reading A destroying the net-vs-gross discriminator. All 7 non-closed brookfield BlackLine exceptions had email/Slack approval threads. Replaced with submitted-vs-approved JE discriminator (B6 propagation).

**FINAL Council findings (pre-ship):**
- 0 BLOCKERs
- 2 MAJORs fixed: R9 attendee lock-in (softened: Daniel removed as hard evidence requirement); R11 AND-bundle (softened: individual amounts not required if sum + JE IDs stated)
- THIN_DENSITY carry-forward (accepted)

**Actual failures (from S4 verifier-fails analysis):** pending -- trajectories not yet run.

## Entry — Tasks/43_6a4f191dbdbe492d7e70af2d — 2026-07-10

**Persona / Business function:** Marcus Knell (Billing Coordinator) / Engagement Mgmt & Client Operations — May close billing basis derivation for June invoice batch

**Universe:** Brookfield CPAs (V3). CB creation task.

**Selected levers (from Hardness_Plan.md):**
- Lever 1 — Latching (Marcus paraphrases George's authority steer about submitted advisory+audit entry)
- Lever 2 — Structured-DB skip (SAP subledger absence-of-mirror for submitted JE)
- Lever 7 — Multi-write diversification (5 writes: email Daniel, Slack C005, Records Vault upload, calendar hold, reminder)
- Lever 8 — Multi-link chain (4-link: George steer → GL status check → SAP subledger absence → 119000 WIP aggregation → $33,844.93)
- Lever 9 — Universe-grounded gotcha (JE lifecycle, account-role trap 110000 vs 119000, entity discipline)

**Actual failures (from S4 verifier-fails analysis):**
- R#14 SAP subledger check: Bucket 3 — 6/6 fail (true AF). Zero sap_subledger tool_use calls in any run. Lever 2 achieved 100% predicted fail rate.
- R#2 Email figure: Bucket 3 — 5/6 fail (Runs 1, 3, 4, 5, 6 sent $89,425; Run 2 recovered and sent $33,844.93)
- R#5 Memo related_resource_id: Bucket 3 — 5/6 fail (Runs 1, 3, 4, 5, 6 tied to je_53962aed96fe4b67; Run 2 tied to je_46e6033b6aa946e7)
- R#6 Memo figure: Bucket 3 — 5/6 fail (same cascade as R#2)
- R#8 C005 figure: Bucket 3 — 5/6 fail (same cascade as R#2)
- R#11 Identifies correct derivation: Bucket 3 — 5/6 fail. Runs 1, 3, 4, 5, 6 computed $89,425 or explicitly excluded 119000 WIP JEs as "approved-but-unposted"; Run 2 correctly derived $33,844.93 from both JE IDs.
- R#13 Account-role identification: Bucket 3 — 4/6 fail. Runs 1, 3, 4, 5 stopped at submitted-status exclusion without naming 110000 vs 119000; Runs 2 and 6 explicitly cited the AR / 110000 characterization.
- R#4 Retention code: Bucket 3 — 1/6 fail (Run 3 only). Run 3 used FIRM_INTERNAL instead of AICPA_SQMS_7Y.
- R#12 Submitted status identification: Bucket 3 — 1/6 fail (Run 3 only). Run 3 misidentified George's entry as je_53962aed96fe4b67 (posted); never surfaced je_1f83fec3cf0346db submitted status. All other runs passed.
- R#9 Calendar date: PASS 6/6. Every run placed the hold at 2026-06-30 (confirmed by direct tool_use trajectory inspection).

**Calibration:**
- Levers that fired as predicted: Lever 2 (100% SAP skip on R#14), Lever 7 (density delivered 40.2 avg, THIN_DENSITY band), Lever 9 account-role trap (R1, 3, 4, 5 failed R#13).
- Levers that did NOT fire as predicted: Lever 1 did not cause agents to use the submitted JE as billing basis — 5/6 correctly rejected it and then latched on a different wrong entry (adjacent posted revenue-recognition entry je_53962aed96fe4b67).
- Failures from un-predicted sources: "Adjacent-posted-entry anchor" — agents correctly excluded submitted JE on status, found je_53962aed96fe4b67 (posted, $147,825 total), extracted its AR debit leg ($89,425) as the billing basis. Account-type discrimination (WIP 119000 vs AR 110000) was insufficient to deter this anchoring in 5/6 runs. Run 2 recovered by summing the 119000 debits.
- Recovery observation: The task has one clean-recovery run (Run 2 passed 13/14, missing only R#14 SAP subledger). The stump is not deterministic — a correct WIP-side aggregation path exists and one Opus 4.8 run followed it.

**Lesson for next task:** When a submitted-JE stump coexists with a large posted revenue-recognition entry in the same period, agents will reject the submitted JE correctly and then anchor on the posted entry ~83% of the time. The posted entry must be clearly non-billing-eligible on its own terms (e.g., wrong entity, prior-period, different cost center), or the correct billing basis must be the only entry touching the target account in the period. Account-type discrimination (WIP vs AR) alone does not deter anchoring on posted entries. Note: an SAP-subledger absence-of-mirror rubric (Lever 2 shape) is the highest-yield single mechanism observed on this task — 6/6 zero-tool-call rate — and is worth keeping in the catalog for future JE-eligibility tasks.

## Entry — Tasks/44_6a4f19235611212ea6b60a62 — 2026-07-10

**Persona / Business function:** Anaya Wallace (Trainee Accountant, Brookfield CPAs & Advisors, AP-escalation family) / Business Function 7 (BlackLine Close-Discipline & Variance).

**Selected levers (from Hardness_Plan.md, 5 chosen):**
- L8 multi-link chain (3 services) — BL review-notes → SAP subledger AR/AP + feed_runs → Oracle GL JE history on acct 119000 for FP-2026-05.
- L9 authority-figure dismissal — soft-verb dismissal cover from Harry Marks (materialized universe reroutes to George's C005 parent thread + Hannah Grant's accept-timing disposition email trail; documented Lens 5 narrative-fiction gap kept under trap-design latitude).
- L10 SAP subledger invisibility — true root cause sits on `brookfield_tax_engagement_trust_feed` partial_failure `run_e0365372e21545` (ten rejected rows), NOT the AP feed the prompt describes.
- L25 existing-output anchor trap — three FP-2026-05 candidate JEs on account 119000 (je_01de85923ce744ba $18,621.37 AR approved, je_46e6033b6aa946e7 $15,223.56 AR approved, je_53962aed96fe4b67 $147,825 manual posted with doubled-prefix entry_number quirk); none match the residual on amount / purpose / exc reference.
- L26 decoy parent Slack thread — C005 George McAdam parent ts 1780248600.000000 is the correct authority thread carrying the review-note pointer + Edith's vault-sweep confirmation; more-recent George parent ts 1780327320 (BD1 close-entries announcement) is the decoy.

**Predicted stump hypotheses (from Hardness_Plan.md, awaiting S4 confirmation):**
- [HIGH] Opus accepts Harry's soft-verb dismissal and closes exc_1ddfc978ce5a4d without derivation.
- [HIGH] Opus never opens `sap_subledger.subledger_transactions` / `ogl_subledger_feed_runs` on 119000 for May, missing the L10 anchor.
- [MED] Opus mistakes je_46e6033b6aa946e7 or a peer for prior handling and refuses to draft the NEW correcting JE.
- [MED] Opus posts to the decoy Slack parent 1780327320 instead of authority parent 1780248600.000000.

**Density projection:** Hardness_Plan midpoint 55.5 (range 44-67); FINAL integrated projection 45-50 (THIN-band-at-risk NOTE; Verification_s3.md carries AUDIT inherited THIN band 43 from OE audit). Passes Council_Protocol B3 tiered gate with per-task justification. Watch S4 for platform-density underflow (< 40 floor).

**Novel Brookfield anchors documented for future tasks:**
- L25 existing-output anchor with three plausibly-similar approved+posted FP-05 JEs on the same account.
- L26 decoy parent thread via C005 (829-msg density enables plausible more-recent decoy).
- Doubled-entity-prefix entry_number quirk on je_53962aed96fe4b67 (`JE-brookfield-brookfield_FP-2026-05-0057`) — noted in OE 14 as universe-stored form; future tasks using ogl_journal_entries on brookfield should expect this shape on some rows.
- Account 119000 `verify_universe_atoms.py` schema-shape false-positive (nested `row_data`) — worth reporting to Validators maintainer separately.

**Actual failures (from S4_verdict.md, 2026-07-10; corrected 2026-07-10 from stale trajectory files):**
- pass@1 = 0.0% (0/6 runs passed all criteria). Per-run pass counts: 5/4/3/3/3/10 = 28/120 = 23.3%.
- 7 all-failing criteria + 11 partial-fail + 2 perfect-pass (Slack thread_ts 1780248600.000000; $4,390.62 variance walk).
- Bucket 1 = 0, Bucket 2 = 0, Bucket 3 = 18. All-Failing Rubrics sub-dim = 5/5 PASS.
- Density 45.8 avg total, 35.8 avg MCP. Above 40 floor, below 50 design target — trust-feed skip shaved 5-8 discovery calls per run.

**Calibration (3 of 4 predictions hit):**
- **HIT** L9 authority-figure dismissal — 5/6 runs cited Hannah's accept-timing or Harry's soft close-out as reason to refuse the corrective JE and the exception update. Highest-yield single mechanism on this task.
- **HIT (strong)** L10 SAP subledger invisibility — 0/6 runs discovered `run_e0365372e21545` or `brookfield_tax_engagement_trust_feed`. Runs 4 and 5 saw partial_failure in the feeds-list response but never followed up with a get-run call. Cascades into three all-failing criteria (exception root_cause, vault memo derivation, corrective JE business_justification).
- **BLOCKED-BY-L9** L25 existing-output anchor — not observed as a distinct failure. The L9 authority-dismissal refusal fired upstream and short-circuited the JE-history check that would have exposed the anchor. Not a task defect; a design lesson.
- **MISS (over-predicted)** L26 decoy Slack thread — 6/6 runs used the correct thread_ts 1780248600.000000. The BD1 close-entries decoy at 1780327320 was too topically distinguishable from the target exception thread to fire.

**New sub-mode named — status-glance-only skip:** Runs 4 and 5 observed `partial_failure` status in the feed-list response and did NOT follow up with a get-run call. This is a distinct sub-mode of L10 SAP invisibility (status-visible + detail-invisible). Future L10 designs can lean on this by making the partial_failure status visible in the list response but the identifying run_id only reachable through the get-run call the agent skips.

**Lesson for next task:**
- L9 remains the strongest single stump on Brookfield authority-anchor scenarios. Design should budget for L9 to dominate — either accept that downstream levers may not fire, or split L9 across a subset of writes so other levers can be independently measured.
- L10 cascades into multiple derived criteria (root_cause, memo derivation, JE business_justification) without artificial multiplication. A single L10 anchor efficiently produces three or more all-failing rubrics.
- L26 needs stronger decoy similarity to fire against Opus 4.8. Future L26 designs should share subject-line keywords, account references, or timestamps within an hour or two of the target thread. Pure topical distinguishability is insufficient.
- Density at 45.8 avg total sits above the 40 floor despite the trust-feed skip shaving 5-8 discovery calls per run. The 50+ design target provided the necessary buffer — without it the task would have landed near or below the 40 floor. If a task's L10 anchor is a "not-attempted" surface (agent should touch it but does not), the density projection should assume the calls will not be made and pad the base discovery accordingly. *(Corrected 2026-07-10: prior entry cited 41.3 from stale trajectory files.)*

## Entry — Tasks/44_6a4f19235611212ea6b60a62 — 2026-07-11

**Persona / Business function:** Anaya Wallace (Trainee Accountant, npc) / BlackLine Close-Discipline & Variance

**Selected levers (from Hardness_Plan.md):**
- Lever 1 — Latching (Slack C005 partial-feed narrative vs BlackLine proposed_resolution corrective JE with source_module=manual)
- Lever 3 — Missing reply (rn_564e65ce0d594f on BL-75810CD0FEE4: state=open, response=null, SLA 2026-06-02 — 10 days overdue)
- Lever 5 — Thread-reply blindness (ts=1780248600.000000 in high-traffic C005; resolution context in replies, not top-level post)
- Lever 6 — Near-miss entity confusion (account 119000: brookfield=WIP-Unbilled Services vs northstar_legal=WIP-Unbilled Time)
- Lever 7 — Multi-write diversification (5 write surfaces: oracle_gl JE x2, blackline exception update x2, records_vault upload x2, slack post, email)
- Lever 8 — Multi-link chain (exception -> related_reconciliation_id BL-75810CD0FEE4 -> blackline_list_review_notes -> null-response check; 4-hop chain)
- Lever 9 — Universe-grounded gotcha (two past-SLA exceptions same assignee same period; agent likely resolves only the larger first-returned one)

**All 7 levers confirmed end-to-end by FINAL Council (VERDICT: PASS, 0 BLOCKER, 0 MAJOR, 3 MINOR).**

**Actual failures (from S4 verifier-fails analysis):**
- Rubrics 8, 9, 10, 11 (exception status updates): Bucket 1 — Rubric Invalid. EX.SLA_OVERDUE hard-blocks all state transitions; no escalation tool in catalog; both exceptions already escalated=true in universe. Rubrics required success responses that the system architecture prevents. FIXED: rewritten to test attempt + call parameters instead of stored outcome.
- Rubrics 12, 13 (vault uploads kind=journal_entry_support): Bucket 3 — Legitimate AF. All 4 runs that attempted uploads used kind='reconciliation_support'. Agents defaulted to workflow context (reconciliation exception) rather than document type (JE support memo). Lever 7 (multi-write) partially covered this surface; the specific kind-parameter trap was not predicted.
- Rubrics 1, 2, 5, 6 (JE creation): Bucket 3 partial fail — R4 cited invented manager directive; R5 cited invented SOX blocker. Novel latching variants not in stump hypothesis.
- Rubrics 3, 7 (JE post): Bucket 3 partial fail — R3 submitted but did not post after receiving nonstandard_manager_required=true flag; did not know to call oracle_gl_approve_journal_entry to handle the flag.
- Rubric 4 (BL variance update): Bucket 3 partial fail — R3 used blackline_attach_evidence instead of blackline_update_reconciliation_variances (wrong tool for the re-run-recon step).
- Rubrics 14, 16 (Slack + email execution): Bucket 3 partial fail — R5 and R6 drafted output but did not call the send tools.
- Rubric 19 (Edith's review note): Passed all 6 runs. Lever 3/8 chain did not stump any run.

**Calibration:**
- Levers that fired: Lever 1 (latching, partial — novel variants in R4/R5), Lever 7 (multi-write, partial — kind-parameter gap exposed), Lever 9 (gotcha, partial — R4/R5 missed both exceptions)
- Levers that did NOT fire: Lever 3 (missing reply — 6/6 found Edith's note), Lever 6 (entity confusion — 0 mismatches among runs that engaged), Lever 8 (multi-link chain — 6/6 traversed correctly)
- Failures from un-predicted sources: EX.SLA_OVERDUE rubric design flaw (most impactful — caused 4 of 6 AF rubrics to be Bucket 1); kind='reconciliation_support' vault default; nonstandard_manager_required handling gap in R3

**Lesson for next task:** Before writing exception-update rubrics, verify universe `sla_due_at` vs universe today and confirm an escalation tool exists if the SLA has passed. If no escalation tool is available and SLA is overdue, rewrite the rubric to test the attempt + call parameters, not the stored outcome. Add this check to S3 rubric QC.

## Entry — Tasks/44_6a4f19235611212ea6b60a62 — 2026-07-11 (Post-fix re-run correction)

Corrects the 2026-07-11 entry above. Bucket 1 fixes applied to 7_Rubrics.json; verifier re-ran
against the fixed rubric set. T1 density confirmed from actual trajectory files.

**Corrected calibration (post re-run):**
- Bucket 1: 0 rubrics (rubrics 8-11 absorbed into fixed criteria that now pass in R1/R2/R3/R6).
- Bucket 3: 2 rubrics (12, 13 — vault kind parameter, both legitimate AF).
- All-Failing Rubrics sub-dim: 5/5 PASS (0/2 = 0%). Corrected from 1/5 FAIL (4/6 = 67% in prior run).
- Density: 65.8 avg total, 55.3 avg MCP — PASS at 50 design target (prior 2026-07-11 entry cited
  stale pre-trajectory values).

**Confirmed replicable failure — kind='reconciliation_support' vault default:**
4/4 runs that attempted vault uploads (R1, R2, R3, R6) used kind='reconciliation_support' instead
of kind='journal_entry_support'. This is a stable model gap: agents categorize vault documents by
the workflow that produced them (exception resolution = reconciliation) rather than the document's
content type (JE support memo). Future tasks using records_vault_upload_document with a
kind=journal_entry_support rubric should plan for an AF justification on this parameter.

**Lesson update:** Core lesson unchanged. Additional lesson confirmed: when testing vault upload kind
parameters, the reconciliation-vs-JE-support distinction is a reliable stumping surface. Budget for
it as a legitimate AF rather than treating it as a rubric design issue.

## Entry — Tasks/45_6a5edd95a6946f6c4d160b5a — 2026-07-21

**Persona / Business function:** Denise Morales, Onsite Property Manager / Property Operations

**Selected levers (from Hardness_Plan.md):**
- L9 — HVAC life-safety gotcha + authority-figure dismissal (Tony Reyes Slack + Gmail reply)
- L2 — QB credit memo skip ($1,840 gross vs $1,550 net, CM-2026-SR208)
- L8 — Multi-link chain: Gmail tenant report → Airtable ticket → Linear issue → QB bill
- L12 — Document cross-reference: Alamo HVAC inspection report (Gmail) vs Airtable structured field
- L7 — Multi-write: 5 write actions across 5 services

**Actual failures (from S4 verifier-fails analysis):**
- TBD — pending platform run and S4 verifier-fails paste

**Calibration:**
- Levers that fired as predicted: TBD
- Levers that did NOT fire: TBD
- Failures that came from un-predicted sources: TBD

**Lesson for next task:** TBD — update after S4.
