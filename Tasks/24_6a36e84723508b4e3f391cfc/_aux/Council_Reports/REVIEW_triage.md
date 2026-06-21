# REVIEW Triage

Task: `24_6a36e84723508b4e3f391cfc`
Persona: Lena Park, Procurement Officer (NPC role in universe; assignment is internally consistent).
Business function: AP / Vendor Operations.

## QC scoresheet - per sub-dimension

Scores per `Docs/7_QC_Spec_Doc1.json` (5 = excellent / shippable, 1 = unsalvageable). Every < 5 must either be raised to 5 in-place or trigger REBUILD.

### Prompt (12 sub-dims)

| Sub-dim | Score | Reason (per-task universe) |
|---|---:|---|
| Unique Ground Truth | 3 | "Worst offenders" is fuzzy - many candidates would converge on top-dollar (VaultKey $460K, AssurePath $294K) and skip BeaconPay ($109K but 320d). Rubric expects BeaconPay too, so the prompt's "80-plus-day range" anchor under-specifies. |
| Feasibility | 4 | Data exists (320 pending_approval invoices, all six named in OE/rubric present in `sap_subledger.ap_invoices.json`). Reachable, just dense. |
| Persona / Business-function fit | 4 | Lena Park is `Procurement Officer` - adjacent to AP triage, not the natural owner. Daniel Jones (Accounts Manager) or Tariq Soto (AP Clerk) would be a tighter fit. Not a major mismatch, but cost-of-correctness lever. |
| Coherence (no bolt-on) | 4 | Records Vault scope-check + email/Slack prior-conversation check both fit the AP triage narrative naturally. |
| Contrived language | 5 | Reads naturally - vendor-calls anchor, two-or-three-vendor uncertainty, partner sign-off mention all sound like a real procurement officer. |
| Investigation pre-solved | 5 | Prompt does not name vendors / invoice IDs. Agent must discover. |
| Single-service tool use | 3 | Touches SAP + Records Vault + Email + Slack + (implicit) approver lookup - multi-service. But the OE / rubric only mandate one write action (Slack), which suppresses density. |
| Maximalism (density floor) | **1** | Measured 32.5 avg tool calls < 40 floor. Direct fail. |
| Word count / format | 4 | 220 words (well under 500 cap). Includes one relative-date phrase ("this week") that should anchor to 2026-06-12. |
| Strict-language conventions | **2** | Em-dashes at offsets 599 and 1146 (validator-blocking). |
| Tool / system name leakage | 4 | "SAP" appears in "pull the pending-approval queue in SAP" - system name, edge case. Not a tool name per `8_Server_Tools_Details.json`, but `Linter_Playbook` flags system-level naming as undesirable. |
| Truthfulness / lever fit | 3 | The "60-day SLA" anchor is fine. The "80-plus-day range -> disputed deliverable / missing credit memo / orphaned approval chain" forecast partially holds (most are orphaned with `approver=None`), but only 2-3 invoices show genuine disputed-deliverable / credit-memo trails. Most are pure orphans. The prompt over-promises the categorical mix. |

### Oracle Events (per `Docs/7_QC_Spec_Doc1.json` OE sub-dims)

| Sub-dim | Score | Reason |
|---|---:|---|
| Completeness vs prompt | 3 | OE1 (SAP query), OE2 (named-invoice identification), OE3 (Vault check), OE4 (email/Slack history), OE5 (root-cause categorization), OE6 (Slack post), OE7 (defer to Daniel/Steven). Maps to the prompt but doesn't decompose discovery into atomic verifiable steps. |
| OE count vs V3 range | **2** | 7 OEs; V3 reference range is 11-28. Sparse. |
| Action-verb openings | **2** | 0/7 begin with Search / Send / Call / Post. V3 references use action-first uniformly. |
| Atomicity | 3 | OE2 bundles "identify AssurePath VEN-005-84026 (~$294,270, ~130 days) AND Northloop VEN-015-500420 (~$168,054, ~123 days)" - two checks, one OE. Should split. |
| Truthfulness (atoms exist) | 4 | All six invoice IDs and three vendor names verified in `sap_subledger.ap_invoices.json`. Day-counts in OE are approximate (BeaconPay actually 320d, not implied 80-plus). |
| Strict-language conventions | **2** | Em-dashes at offsets 1459 and 1508 (validator-blocking). |

### Rubrics

| Sub-dim | Score | Reason |
|---|---:|---|
| Atomicity | 4 | 10 rubrics, mostly atomic. R1 bundles three vendor names (AssurePath / Northloop / BeaconPay) as one rubric - should be three. |
| Self-containment | 5 | Each rubric carries its own evidence pointer. |
| Outcome-process balance | 5 | 9 outcome + 1 process. Process rubric is justified (ordering check, can't be inferred from outcome alone). |
| Binding to prompt | 4 | Most rubrics derive from prompt asks. R4 ("Agent retrieves a document from Records Vault related to the Acme Cloud engagement scope") binds to "pull the relevant SOW or engagement letter from Records Vault so we can check whether the amounts are in scope" - but ground truth disagrees (see below). |
| **Truthfulness against ground truth** | **1** | **R4 is keyed to a finding that does not exist in the per-task universe.** `records_vault.rv_documents.json` contains 0 engagement_letter, 0 master_services_agreement, 0 sow records for `entity_id = acme_cloud`. The only engagement_letter in the whole vault is for Northstar Legal. Acme Cloud has 565 vault docs (mostly journal_entry_support / reconciliation_support), but nothing tagged as engagement scope. Agents that strictly looked for engagement-scope docs correctly reported "none found" - and were penalized. Agents that loosened the rubric to "any Acme document" got Pass. This is a rubric design defect, not an agent failure. |
| Title hygiene | 5 | No "at least N" tags. No tool names in titles. |
| No tool names in titles | 5 | Clean. |

## Measured trajectory hardness

See `REVIEW_hardness.md`. Density verdict: **FAIL** (32.5 < 40). Difficulty verdict: OK (pass@1 = 16.7%).

## Verdict

**REBUILD.** Triggered by **two** independent rows of the REVIEW decision table:

1. **Hardness fail row** - measured `avg_tool_calls_total = 32.5 < 40`. Density cannot be patched by OE/rubric tweaks; needs new lever combination.
2. **FAIL-band row** - Rubric Truthfulness sub-dim scored 1 (R4 keyed to nonexistent ground truth). Prompt Maximalism sub-dim scored 1 (measured density fail). Two sub-dims in the 1-2 FAIL band.

Per runbook: **do NOT emit `14_Updated_Oracle_Events.txt` or `15_Updated_Rubrics.json`.** Patching OE/rubric on top of a scenario that needs structural redesign would ship a half-fixed task.

Next action for the user: `PIPELINE REDO - Tasks/24_6a36e84723508b4e3f391cfc`.

## Sub-dims requiring fixes if salvageable (FOR REFERENCE - not actionable under REBUILD)

If this had been SALVAGEABLE, the following would have been required to raise every sub-dim to 5:

- Prompt: strip em-dashes; anchor "this week" to "since 2026-06-08"; specify what "worst offenders" means (oldest-by-age, not largest-by-dollar) so BeaconPay surfaces naturally; replace "in SAP" with a system-agnostic phrasing.
- OE: strip em-dashes; expand from 7 to ~14 OEs by decomposing OE2 (per-invoice rather than bundled), OE3 (per-entity vault check), OE5 (per-category root cause), OE6 (draft + post + confirmation). Open each line with Search / Identify / Verify / Post / Defer.
- Rubric R1: split AssurePath / Northloop / BeaconPay into three separate rubrics.
- Rubric R4: re-key to "Agent searches Records Vault for Acme Cloud engagement-scope documents and reports the finding (no engagement letter / SOW present in vault for Acme Cloud)" - i.e. invert the rubric to match actual ground truth (the universe has no such doc).

These would be applied in a SALVAGEABLE pass. They are NOT being applied here because the verdict is REBUILD.
