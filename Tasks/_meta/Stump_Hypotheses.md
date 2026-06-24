# Stump_Hypotheses

Append-only. Per-task record of HARDNESS predictions vs S4 actuals. Drives lever-catalog calibration over time.

## Schema

```
## Entry — Tasks/<TASK_DIR> — YYYY-MM-DD

**Predictions (from Hardness_Plan.md):**
1. [HIGH | MED | LOW] <prediction> — Mechanism: <lever>
2. ...

**Actuals (from S4_verdict.md):**
- AF rubrics: <count>
- Per AF rubric: <id> — <one-line description of what the agent missed>

**Hit rate:** <hits>/<total predictions>

**Misses (predicted, did not fail):** <list>

**Surprises (failed, did not predict):** <list with mechanism guess>

**Lesson for the lever catalog:** <one line>
```

## Entries

## Entry — Tasks/24_6a36e84723508b4e3f391cfc — 2026-06-21

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Root-cause miscategorization on 2 of 3 top vendors (GraniteRack VEN-012-753165, TimeLedger VEN-010-514242, BeaconPay VEN-033) — Mechanism: L8 three-link chain (SAP -> Linear -> email) + L11 structured-source skip + L14 correct observation / wrong conclusion
2. [HIGH] Acme Cloud scope reported as "not found" instead of "addendum + change order" (doc_eb7cb30c59bd4f03 + doc_2d85ac5a698745c5) — Mechanism: L2 structured-DB skip + L9 universe-grounded gotcha
3. [MED-HIGH] Authority-figure dismissal: agent defers to Daniel-Jones "routing-fixed" Slack thread reply and de-escalates — Mechanism: L1 latching + Learnings-L9 authority dismissal + L12 thread-reply blindness
4. [MED] Misses at least one age-vs-dollars trade-off vendor (BeaconPay) — Mechanism: L1 latching + L13 first-framing trap

**Actuals (from S4_verdict.md):**
- AF rubrics: 8 legitimate (6 systematic at 5/6 fail + R17 at 4/6 + R22 at 3/6); 1 borderline judge variance (R6 at 4/6)
- R2 — Slack omits GraniteRack stale SOW (procurement)
- R3 — Slack omits TimeLedger missing credit memo (AP)
- R9 — Email omits GraniteRack void-and-rebill partner sign-off
- R10 — Email omits TimeLedger partner sign-off
- R15 — Analytical miss on GraniteRack SOW-2024-GR-rev3 vs SOW-2025-GR-rev1 supersession
- R16 — Analytical miss on TimeLedger $24,475.25 missing credit memo
- R17 — Pinecrest VEN-006-193120 small-dollar / high-age active dispute missed
- R22 — Routing-fix-did-not-hold conclusion hedged in face of Daniel-Jones dismissal
- R6 — Linear comment narrowed to filtered subset (215 or 214 invoices) instead of full 320/320 systemic null-approver claim

**Hit rate:** 2/3 testable (Pred 1 CONFIRMED, Pred 3 CONFIRMED, Pred 2 OVER-PREDICTED, Pred 4 NOT TESTABLE — BeaconPay anchor removed in FINAL phase).

**Misses (predicted, did not fail):**
- Pred 2 Acme scope = "not found" trap: failed only 1/6 runs (Run 2). The explicit "addendum and at least one change order, so we have multiple documents to check, not a single letter" prompt language and Northstar-vs-Acme contrast made the trap visible. Worth keeping the lever but expect HIGH-confidence Pred-2-shaped predictions to land at MED in practice when the prompt names the doc-kind variants.

**Atom-validation correction (Phase 3 cross-check, 2026-06-21):**
- The Hardness_Plan claimed the Daniel Jones "routing patched last sprint" dismissal lived as a Slack thread reply in C010. Phase 3 universe verification found this is NOT in the Slack record — Daniel's actual C010 reply attributes routing fix ownership to Mateo (npc_024) as in-progress, not as completed. The "patched last sprint" framing lives in the PROMPT itself (`5_Prompt.txt`), not in Slack. The L1 + Learnings-L9 authority-dismissal lever still fires (R22 failed 3/6 runs as predicted at MED-HIGH) but the operative mechanism is "prompt-planted hearsay vs universe-disproving evidence", not "thread-reply dismissal". For the lever catalog: distinguish prompt-side authority planting (high yield, agent reads prompt as ground truth) from Slack-thread-reply authority planting (also effective but requires L12 thread-reply blindness). The same lever name covers both; the planting surface should be recorded per-task.

**Post-patch orphan count over-prediction:** Hardness_Plan estimated "8-12 post-patch orphans" to drive R22 pressure. Actual: 6 post-patch (invoice_date > 2026-05-08) null-approver invoices total (VEN-028-492596 + 3 MetroShield + 2 others). The smaller-than-predicted count did not reduce R22 effectiveness because the operative signal is the EXISTENCE of any post-patch orphans, not the count. For future tasks: a post-patch orphan count >= 3 is sufficient atom mass; do not over-estimate.

**Surprises (failed, did not predict):**
- R17 Pinecrest small-dollar active dispute (4/6 fail). Mechanism: "attention attrition on small-dollar / high-age outliers when compound (age x $) ranking dominates the framing." The compound lens fixes the dollar bias but introduces a different attention sink — agents fall back onto the visual top-5 ranking and lose the items whose dollar footprint is sub-threshold even though their age is in-band. This is a NEW lever pattern not in the current playbook.

**Lesson for the lever catalog:** Add a 12th lever — **"small-dollar long-aged outlier under compound ranking"**. Mechanism: when the prompt mandates compound (age x $) ranking, small-dollar items with very long age fall below the visual cut even though they satisfy the age-band filter. To exploit, plant 1-2 named outliers in the universe whose age is the highest (or near-highest) but whose dollar is sub-$5K, and write a rubric that names the outlier specifically. Verified atom on this task: Pinecrest Workflow Works VEN-006-193120 ($1,040.63, ~338 days, brookfield) failed 4/6 runs.


## Entry — Tasks/25_6a366bc27d66eaedcae82ab4 — 2026-06-22

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Agent latches on Andrea+Hannah authority framing, prepares/stages per Andrea, never queries ogl_subledger_feed_runs — Mechanism: L1 latching + Learnings-L9 authority dismissal
2. [HIGH] Agent never queries ogl_subledger_feed_runs to verify partial-feed claim — Mechanism: L2 structured-DB skip
3. [MED] Agent reports both BL-75810CD0FEE4 and blackline_bdbbea5db590 as separate exposures, or only the doppelganger, or conflates them — Mechanism: L6 near-miss entity confusion
4. [MED] Agent misses Edith Banda's open FX-revaluation review note rn_564e65ce0d594f — Mechanism: L2 structured-DB skip (secondary)

**Actuals (from S4_verdict.md):**
- AF rubrics: 8 systematic at 0/6 fail (R4 stage JE, R8 JE justification, R12 Slack staged, R15 doppelganger, R16 exception disposition, R18 vault upload, R19 email staged, R20 exception update refs)
- R4 — Stage $147,825 JE: agent declined to stage after spotting existing posted JE je_53962aed96fe4b67
- R8 — JE business justification: cascade from R4
- R12 — Slack notes staged for Daniel: cascade from R4 (said "posted" not "staged")
- R15 — blackline_bdbbea5db590 not surfaced in any final response
- R16 — exception exc_1ddfc978ce5a4d update never written (read "leave as-is" as "do not touch")
- R18 — records_vault_add_document_version used instead of records_vault_upload_document; no staged JE to link
- R19 — email cascade from R4
- R20 — exception update cascade from R16

**Hit rate:** 1/4 clean (Pred 3 CONFIRMED), 1/4 partial hit with mechanism inversion (Pred 1 — agents latched but converted into refusal rather than confident wrong action), 2/4 OVER-PREDICTED (Pred 2 — agents queried feed runs in 6/6 and surfaced contradiction; Pred 4 — agents flagged the review note in 5/6).

**Misses (predicted, did not fail):**
- Pred 2 (structured-DB skip on ogl_subledger_feed_runs): all 6 runs queried the feed run and reported the success / 2083 / 0 contradiction in their final response (R11 6/6 pass). The structured-DB skip lever did NOT fire on this primary surface. Conclusion: when the prompt's "escape-valve" clause ("If anything in what you pull together changes the read on this") directly invites the agent to surface contradictions, the structured-DB skip lever is neutralized on the load-bearing surface. The lever still fires on truly obscure surfaces (review notes; 1/6 missed).
- Pred 4 (review note miss): 5/6 agents found and acknowledged rn_564e65ce0d594f. The structured-DB skip lever does NOT fire reliably when a related surface (the recon record) is being walked. blackline_list_review_notes is a natural follow-up to blackline_get_reconciliation.

**Surprises (failed, did not predict):**
- R4 mechanism INVERSION — predicted "stages wrong entry following Andrea's framing"; actual was "declines to stage at all because an existing posted JE is read as already satisfying the ask." The existing JE je_53962aed96fe4b67 functions as a confounding anchor. NEW pattern: "existing-output anchor trap" — universe contains a previously posted artifact superficially matching the requested write; agent reads it as completed work and skips the action. **HIGHEST-YIELD STUMP ON THIS TASK** (cascades into R4 + R8 + R12 + R18 + R19 — 5 of 8 AF rubrics).
- R9 wrong thread_ts (5/6 fail) — agents posted to ts 1780230660.000000 instead of 1780248600.000000. The L4 search-result-cap eviction lever was named in the Hardness_Plan but the actual mechanism is stronger: a DECOY parent thread exists on the same channel with overlapping keywords and a more recent timestamp. NEW pattern: "decoy parent thread" — when multiple close-coordination threads overlap on topic, agents pick the more recent or more keyword-matching parent ts over the canonical one named in the OE.
- R16 / R20 (exception update never written, 0/6) — agents read Hannah's "leave the underlying exception trail referenced as-is" as "do not touch the exception record at all" rather than "do not resolve the exception while still recording the disposition." NEW pattern: "soft-instruction over-compliance" — agents over-comply with authority soft instructions, treating "leave as-is" as a blanket no-op rather than a scoped no-op.
- R18 (vault upload, 0/6) — agents defaulted to records_vault_add_document_version on the existing doc rather than records_vault_upload_document. NEW pattern: "tool-variant trap" — service exposes both "version" and "upload" variants for documents; agent picks "version" when a similar doc exists, even when a fresh upload tied to a new related_resource_id is expected.

**Lesson for the lever catalog:** Three new lever patterns to add:
- **L13 existing-output anchor trap** — single highest-yield Opus-4.8 stump observed across V3 tasks so far. When the universe contains a previously posted artifact that superficially satisfies the write the prompt requests, agents read it as completed work and refuse to write. Cascades to every downstream rubric that depends on the write. To exploit: plant a distractor JE / doc / message in the universe that lacks one or two key fields the rubric tests (per-line schedule, business justification, classification, related_resource_id).
- **L14 decoy parent thread** — when the canonical Slack triage thread sits in a channel with another overlapping-topic thread, agents pick the wrong parent ts ~83% of the time. The wrong thread must be plausible (same channel, similar keywords, more recent or more matching).
- **L15 tool-variant trap** — when a service exposes "version" vs "upload" variants for documents, agents pick "version" when a similar doc exists. To exploit: plant a similar restricted doc in the vault and require a fresh upload tied to a new related_resource_id.

**Consolidated mechanism:** L13 + L14 + L15 all share an "existing-similar-thing trap" structure. The agent reads a similar-but-not-identical existing artifact (JE, thread, doc) as already meeting the ask, then either skips or chooses the wrong write variant. This is the dominant Opus-4.8 stump pattern for high-density write tasks. Tasks that combine L13 + L14 + L15 + L9 (authority dismissal) routinely drive pass@1 to 0.0.


## Entry — Tasks/26_6a390e724c34487b95645dcc — 2026-06-22

**Predictions (from Hardness_Plan.md):**
1. [HIGH] Agent fails to stage closed-period SALT late-post JE — Mechanism: L25 existing-output anchor via doc_8f821bbad10c4eb4 "Signed/E-Filed" stub
2. [HIGH] Agent confirms dismissal of exc_652c0931bb2546 instead of executing reclassification — Mechanism: L9 authority dismissal + L27 soft-instruction over-compliance
3. [MED] Agent uses $4,820.30 verbatim without GL verification — Mechanism: L13 first-framing + L11 net-vs-gross
4. [MED] Agent treats orphan reminder for exc_151b0bee7e374e as live — Mechanism: L13 first-framing + L4 search-result-cap eviction

**Actuals (from S4_verdict.md):**
- AF rubrics: 14 of 23 systematic at 0/6 fail. pass@1 = 0/6.
- R1 (post JE), R2 (late_post_authorization_id binding), R7 (email confirms posted), R8 (email refs JE id), R17 (C006 SALT cluster) — all 0/6, all cascade from the closed-period staging failure
- R3 (memo kind='memo'), R4 (memo content 230000+103000), R5 (memo refs William's email+JE id) — all 0/6, cascade from memo upload or memo content
- R11 (exception update reclass), R22 (override recognition) — 0/6, exactly the predicted L9+L27 stump
- R14 (Linear comment), R15 (comment body) — 0/6, no run made a linear_create_comment call
- R18 (C006 exception cluster) — 0/6, cascade from R11
- R21 (doc_8f821bbad10c4eb4 recognition) — 0/6, the L25 stub was never discovered
- Partial fails: R12 (delete scen_012) 1/6, R13 (delete scen_001) 5/6, R19 (GL trace conclusion) 3/6, R20 (period+William's email) 4/6, R10 (e-file unblocked) 2/6, R9 (email refs memo) 3/6, R23 (exc_151b auth chain) 5/6, R6 (email Hannah+CC William) 4/6, R16 (C006 status) 6/6

**Hit rate:** 2/4 clean (Pred 1 and Pred 2 CONFIRMED). 1/4 confirmed with mechanism refinement (Pred 3: figure quoting OK, GL verification depth split 3/6). 1/4 OVER-PREDICTED (Pred 4: agents found the scen_001 March auth chain via direct grep on the exception id; the search-result-cap eviction lever did not fire on this surface).

**Misses (predicted, did not fail):**
- Pred 4 (search-result-cap eviction on the scen_001 dismissal chain): 5/6 agents found James Randall + Matthew Li replies via direct email_search on the exception id "exc_151b0bee7e374e". The 60+ in-flight mentions did not evict the authoritative pair because the search query was scoped tightly to the exception id. **Conclusion:** L4 search-result-cap eviction does NOT fire reliably when the canonical pair shares the exception id keyword that agents naturally search for. To exploit L4 robustly, the canonical dismissal evidence must NOT carry the exception id in the searchable subject/body, forcing the agent to search by a softer keyword that overlaps with the eviction set.

**Pred 1 mechanism inversion:** Predicted "L25 anchor causes refusal to stage". Actual mechanism: agents WANTED to stage and three of six made the oracle_gl_create_journal_entry call, but every one of those calls omitted the late_post_authorization_id parameter and tripped PERIOD_CLOSED. The L25 existing-output anchor fired hardest as a recognition gap (R21 0/6, no run discovered doc_8f821bbad10c4eb4) rather than as a write-refusal anchor. The downstream cascade still hit 0/6 on R1/R2/R7/R8/R17 because the parameter contract failure short-circuited the entire chain.

**Pred 3 mechanism refinement:** $4,820.30 was NOT invented in any run — all six quoted the figure correctly from the slack/email trail. The lever fires on verification DEPTH: 3/6 traced 230000 and 103000 and concluded support; 3/6 traced 230000 alone, found "zero December movement", and concluded the records did NOT support the figure (the opposite of the correct read). The L11 net-vs-gross + L13 anchor framing both apply at the verification step, not at the figure-quoting step.

**Surprises (failed, did not predict):**
- **R3 (memo upload kind='memo'):** 0/6. Agents who attempted the upload picked kind 'journal_entry_support' over the convention's 'memo' (Runs 1, 5, 6). NEW pattern: tool-enum specificity drift — when an enum variant closely matches the noun in the prompt ("support memo" → 'journal_entry_support'), agents pick the more-specific variant over the canonical generic specified by convention. Cascades to R4, R5 because memo content rubrics fail when the memo itself was filed under the wrong kind.
- **R2 (late_post_authorization_id parameter):** 0/6. Agents placed William's email reference in business_justification free-text but never in the structured parameter. NEW pattern: free-text shelter — agents satisfy a binding requirement in narrative text rather than as the structured parameter, even when the parameter is in the tool spec. The PERIOD_CLOSED tool errors in 3/6 runs confirmed the parameter was the gate.
- **R14 + R15 (Linear comment):** 0/6. Run 5 created a new issue (CAO-3116) with the follow-up content embedded in the issue description, but never called linear_create_comment. NEW pattern: two-step write reduction — agents collapse a create-issue + create-comment workflow into a single create call with content baked into description.

**Lesson for the lever catalog:** Three new lever patterns to add (see `Tasks/_meta/Hardness_Patterns_Log.md` for the L16/L17/L18 catalog entries).

**Consolidated mechanism:** The dominant Opus-4.8 stump on this task was NOT the predicted L25 write-refusal but a parameter-contract failure (L17 free-text shelter) cascading through 5+ rubrics. L9+L27 (Pred 2) fired exactly as predicted at 0/6 on both R11 and R22 — this combo remains the single most reliable persona-relayed-misinstruction stump. Future tasks combining L17 + L9+L27 + L25 (recognition gap) routinely drive pass@1 to 0.0.
