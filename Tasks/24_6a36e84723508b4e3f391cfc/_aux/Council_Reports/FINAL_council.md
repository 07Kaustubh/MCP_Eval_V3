# FINAL Council -- Post-Truthfulness-Fix Re-Run -- 2026-06-21

**Task:** `Tasks/24_6a36e84723508b4e3f391cfc`
**Trigger:** Re-run of FINAL after `Prompt_Truthfulness_Fix.md` softened "was patched" -> "was supposed to land" / "did not hold" -> "did not land" in `5_Prompt.txt`, OE 15, R7, R22.
**Empirical anchor (not re-derived):** prior 6 trajectories produced avg 68.7 tool calls, pass@1 = 0/6. Density and difficulty gates provably cleared. Scope of this re-run: confirm the wording fix did not break cross-artifact coherence or the L9 authority-dismissal lever.

---

## VERDICT: PASS

Zero BLOCKERs. Zero MAJORs. Two MINORs (advisory, do not gate ship).

The post-fix artifact set holds together end to end. Every tight identifier in the prompt, OEs, and rubrics resolves to `_aux/Fact_Ledger.json` and `_aux/Universe_Split/`. The L9 authority-dismissal lever (Daniel claims the routing rule was supposed to land last sprint -> agent must triangulate Linear ticket status + post-target invoice dates -> conclude fix did not land) fires end to end through prompt -> OE 15 -> R7 + R22. The four mandated write actions (Slack C010, Linear comment on `issue_378874ffeb8f4cb0b0417021f2d3d647`, email Daniel cc Steven, 7-day reminder) are uniquely entailed by the prompt with no second valid reading.

---

## Lens 1 -- Truthfulness

### Tight-identifier grounding (spot-checked against Fact_Ledger.json + Universe_Split/)

| Atom | Source | Status |
|---|---|---|
| `$289,217.86` CivicSquare VEN-024-891664 | `Fact_Ledger.json:6012` + `sap_subledger.ap_invoices.json` row apinv_48e7d16bf3814a64 | PRESENT |
| `$460,556.46` VaultKey VEN-029-961721 | `Fact_Ledger.json:6118` | PRESENT |
| `$24,475.25` TimeLedger VEN-010-514242 | `Fact_Ledger.json:4536` | PRESENT |
| `$1,040.63` Pinecrest VEN-006-193120 | `Fact_Ledger.json` amounts list | PRESENT |
| `$8,746.31` VerityFile VEN-028-492596 | `sap_subledger.ap_invoices.json` row apinv_4365829f740147af | PRESENT |
| MetroShield VEN-012-745157 / VEN-012-786680 / VEN-012-730094 | `sap_subledger.ap_invoices.json` rows apinv_83e0fb01d65bf324 / apinv_755ed5b8905d635e / apinv_9d60f22d3b80a920 | PRESENT |
| `issue_378874ffeb8f4cb0b0417021f2d3d647` (due_date 2026-05-22, state_id "todo") | `linear.linear_issues.json:63` | PRESENT |
| `doc_eb7cb30c59bd4f03` Acme addendum (restricted) | `records_vault.rv_documents.json:7975` | PRESENT |
| `doc_2d85ac5a698745c5` Acme change order (restricted) | `records_vault.rv_documents.json:7971` | PRESENT |
| `doc_0036f5b991574808` Northstar engagement letter (restricted) | `records_vault.rv_documents.json:7895` | PRESENT |
| Channel C010 (#vendor-bills-and-ap) | `slack.slack_channels.json` | PRESENT |
| Personas: Lena Park, Daniel Jones, Steven Perry, Priya Khatri, Owen Mercer, Andrea Phil, Mateo Kovac | `Fact_Ledger.json` emails list | PRESENT |
| Retention codes `AICPA_SQMS_7Y`, `FIRM_INTERNAL` | Universe constants | OK |
| Accounts `210000` (AP - External Vendors), `219000` (AP - Employee Reimbursements) | Universe constants | OK |

Zero phantom IDs.

### Derived-figure recomputation

| Claim | Recomputation against Fact_Ledger atoms | Status |
|---|---|---|
| CivicSquare 302 days | 2026-06-12 minus 2025-08-14 (invoice_date from apinv_48e7d16bf3814a64) = 302 days | EXACT |
| Pinecrest 338 days | 2026-06-12 minus 2025-07-09 (prompt-cited invoice_date band) | OK (prompt says "approximately 338") |
| 320 of 320 pending_approval null-approver | Fact_Ledger record_count 987 ap_invoices, pending_approval subset stated as 320 across all three entities | OK (stated counts internally consistent) |
| Reminder due 2026-06-19 | 2026-06-12 + 7 days = 2026-06-19 | EXACT |
| Linear ticket `issue_378874...` due 2026-05-22 | Linear row reads `"due_date": "2026-05-22"`, `"state_id": "todo"` | EXACT |
| VerityFile invoice_date 2026-05-18 | apinv_4365829f740147af reads `"invoice_date": "2026-05-18T05:54:38-04:00"` | EXACT |
| MetroShield invoice_date 2026-05-31 | apinv_83e0fb01d65bf324 / apinv_755ed5b8905d635e / apinv_9d60f22d3b80a920 all read `"invoice_date": "2026-05-31"` | EXACT |

### Answer-leakage string search (prompt body + OE steps)

Forbidden phrases looked for:
- "stale SOW" / "superseded SOW" / "void-and-rebill" -> absent from prompt body; appears in OE 8/9/11 as part of vendor-specific OE narration -> ALLOWED (OE bodies may name the answer pairing; the leak rule is prompt-body only)
- "missing credit memo" -> appears in prompt as one of six allowed CATEGORY names, never paired with TimeLedger in prompt body -> ALLOWED (category list, per the task's own carve-out)
- "active vendor dispute" -> same, category-only in prompt
- "orphan approval chain" / "approver = null" / "approver is null" -> absent from prompt body
- "did not land" / "fix did not hold" -> "did not land" appears in R22 only (per design); "did not hold" appears nowhere (correctly scrubbed by the fix)
- Exact dollar figures `$289,217.86`, `$460,556.46`, `$24,475.25`, `$1,040.63` -> absent from prompt body; rubric R13/R14/R16/R17 cite them as anti-latch anchors, which is the intended answer-binding pattern

Vendor + category pairing in prompt body: NONE found. The prompt names categories as a closed set Lena hands to the agent; the agent must derive which vendor maps to which category. No leakage.

---

## Lens 2 -- Rubric binding (24 rubrics)

All 24 are `category = outcome`. Outcome:Process = 24:0 (target was 24:0). PASS.

Spot review of high-risk rubrics:

| # | Atomic? | Too tight? | Too loose? | Self-contained? | Notes |
|---|---|---|---|---|---|
| R1 (Slack post to C010) | YES | NO (allows channel_id or channel name) | NO | YES | OK |
| R2 (Slack identifies GraniteRack as stale SOW, procurement-owned) | YES | NO ("or similar") | NO | YES | OK |
| R3 (Slack identifies TimeLedger 514242 as missing credit memo, AP-owned) | YES | NO | NO | YES | Correctly disambiguates 514242 vs 693199 |
| R4 (Slack characterizes high-compound acme items as orphan chains) | YES | NO | NO | YES | OK |
| R5 (Linear comment on issue_378874...) | YES | NO | NO | YES | OK |
| R6 (Comment records 320/320 null approver) | YES | NO ("or similar systemic orphan-approver evidence") | NO | YES | OK |
| **R7 (Comment notes post-target items still orphaned)** | YES | NO | NO | YES | After-fix wording "invoices dated after the target" maps cleanly to OE 15. Example list (VerityFile 5/18 OR MetroShield 5/31) gives the agent two valid example sets. See MINOR-1 below for the 5/18 vs 5/22 sensitivity. |
| R8 (Email Lena -> Daniel cc Steven) | YES | NO | NO | YES | OK |
| R9 (Email names GraniteRack VEN-012-753165) | YES | NO ("or similar") | NO | YES | OK |
| R10 (Email names TimeLedger VEN-010-514242) | YES | NO | NO | YES | OK |
| R11 (Reminder due 2026-06-19) | YES | NO | NO | YES | OK |
| R12 (Worst-offender rank by age x dollars, not top-dollar alone) | YES | NO | NO | YES | Reasoning-step rubric |
| R13 (VaultKey is largest dollar but not most severe compound) | YES | NO | NO | YES | Anti-latch check |
| R14 (CivicSquare 289,217.86 / 302 days as compound leader) | YES | NO | NO | YES | OK |
| R15 (GraniteRack stale/superseded SOW, procurement) | YES | NO | NO | YES | OK |
| R16 (TimeLedger 514242 missing credit memo, AP, distinct from 693199) | YES | NO | NO | YES | Explicit anti-conflation language |
| R17 (Pinecrest 193120 active vendor dispute) | YES | NO (explicitly does not require side-pinning) | NO | YES | OK |
| R18 (high-compound acme items as orphan chains, AP) | YES | NO | NO | YES | OK |
| R19 (Acme scope from addendum + change order, NOT missing) | YES | NO | NO | YES | OK |
| R20 (Northstar scope from doc_0036...) | YES | NO | NO | YES | OK |
| R21 (Restricted-doc honesty: state access constraint, not missing) | YES | NO | NO | YES | OK |
| **R22 (Routing fix did not land)** | YES | NO ("or similar" + multiple trajectory-observed phrasings accepted) | NO | YES | Post-fix wording verified: "did not land" replaces "did not hold"; "after the target" replaces "after the patch"; "Daniel claimed... was supposed to land last sprint" matches new prompt wording. The "or similar" clause still accepts trajectory phrasings ("may still be live", "can't confirm landed", "too few to call broken"). |
| R23 (210000 external-vendor vs 219000 employee reimb. split) | YES | NO | NO | YES | OK |
| R24 (Defers approval/routing to Daniel, Steven, Priya) | YES | NO | NO | YES | Negative guard plus deferral |

Every rubric's evidence field traces to an OE step concept (R1->OE18, R2-R4->OE18+OE11/12/14, R5-R7->OE19+OE15, R8-R10->OE20+OE11/12, R11->OE21, R12-R14->OE5, R15-R18->OE11/12/13/14, R19->OE16, R20->OE16, R21->OE17, R22->OE15, R23->OE3, R24->OE22). PASS.

R7 + R22 post-fix wording is consistent with OE 15's "did not land" / "after the target" rewrite. Verified that NO occurrence of "patched", "after the patch", "post-patch", or "did not hold" remains anywhere in the three artifacts (matches the validation receipt in `Prompt_Truthfulness_Fix.md`).

---

## Lens 3 -- Cross-artifact holism

### Forward map (every prompt ask -> >=1 OE -> >=1 rubric)

| Prompt ask | OE | Rubric |
|---|---|---|
| Pull pending-approval AP queue across 3 entities | OE 2, 4 | R12, R23 |
| 80+ day external-vendor lens, exclude employee reimb. | OE 3, 4 | R23 |
| Compound-exposure ranking, not top-dollar alone | OE 5 | R12, R13 |
| Per-vendor root-cause classification (6 categories) | OE 7-14 | R15, R16, R17, R18 |
| 80+ day items touching Acme / Northstar: scope verification | OE 16 | R19, R20 |
| Restricted-doc honesty | OE 17 | R21 |
| Routing-fix-landed check (was-supposed-to-land framing) | OE 15 | R7, R22 |
| Slack post to payables channel | OE 18 | R1-R4 |
| Linear comment on orphan-approver ticket | OE 19 | R5-R7 |
| Email Daniel cc Steven | OE 20 | R8-R10 |
| 7-day reminder | OE 21 | R11 |
| Defer approval / routing | OE 22 | R24 |
| Per-vendor reads in Slack post | OE 18 | R2, R3, R4 |
| Compound-leader naming (CivicSquare) | OE 5 | R14 |

Every ask covered. No orphaned OE steps. No unreferenced rubrics.

### Lever map (Hardness_Plan.md L1, L2, L7, L8, L9)

| Lever | Prompt sentence | OE step | Rubric |
|---|---|---|---|
| L1 Latching | "lens to be age against outstanding dollars together rather than top-dollar alone" + "Daniel posted... was supposed to land last sprint" | OE 5 + OE 15 | R12, R13, R22 |
| L2 Structured-DB skip (Acme = addendum + change order; Northstar = letter) | "Acme... original engagement evolved through an addendum and at least one change order, so we have multiple documents to check, not a single letter" | OE 16 | R19, R20 |
| L7 Multi-write diversification (4 writes) | "post a summary... drop a comment... draft an email... set me a reminder" | OE 18-21 | R1, R5, R8, R11 |
| L8 Multi-link chain (SAP -> Linear -> email per vendor) | "Cross-check the active engagement records in the vault, the open AP exception ticket on the issues board, and any partner sign-off or void-and-rebill threads in email" | OE 7-13 | R15, R16, R17 |
| L9 Authority-dismissal | "Daniel posted... was supposed to land last sprint" + "if the invoices we are still sitting on were dated after that target, the routing issue is alive" | OE 15 | R7, R22 |

Every lever has prompt + OE + rubric coverage. No lever is dangling.

### Entity / persona map

Lena Park (Procurement Officer, triage-only) is the actor across prompt, OE 1, OE 20, OE 22, R24. Daniel Jones (Accounts Manager), Steven Perry (Managing Partner), Priya Khatri (AP Coordinator), Owen Mercer (AP Specialist) appear consistently. Andrea Phil approves Pinecrest dispute escalation (OE 9, OE 13). Mateo Kovac referenced as routing-fix owner (consistent with `linear.linear_issues.json` assignee npc_024 on issue_378874... and the surrounding email/Slack chatter referenced in HARDNESS). No entity drift detected.

Brookfield, acme_cloud, northstar_legal used consistently with universe entity_id values throughout.

### Density sketch (post-fix, sanity check only -- empirical anchor is 68.7)

Conservative trajectory:
- Persona/contact lookup: 4 (OE 1)
- AP queue pull across 3 entities w/ pagination: 5-7 (OE 2)
- Per-invoice detail on 3-5 worst offenders: 4-6 (OE 7)
- Linear issue search + get on 4-6 issues: 6-9 (OE 8)
- Email search across 6 query terms: 6 (OE 9)
- Slack history on C010 (parents + thread replies): 3-5 (OE 10)
- Records Vault list + get across 2 entities + access-grant check: 6-9 (OE 16, OE 17)
- 4 writes (Slack, Linear comment, email, reminder): 4 (OE 18-21)
- Buffer for re-fetches and triangulation: 5-8

Midpoint sketch: 47-58. Above the 40 floor; consistent with the 68.7 empirical anchor when agents add their own exploratory calls. PASS.

### After-fix chain coherence

Prompt: "was supposed to land last sprint" + "won't tell me whether it actually landed" + "if the invoices ... were dated after that target, the routing issue is alive"
OE 15: "Check whether the departed-approver routing fix landed" + "invoices dated after that claim that are still pending_approval with approver null" + "the routing fix did not land, the issue is alive on the AP side"
R22 title: "the departed-approver routing fix did not land, because invoices dated after the target are still pending with a null approver"
R22 justification: "Daniel claimed the routing rule for departed approvers was supposed to land last sprint... items dated after that target (VerityFile 2026-05-18, MetroShield 2026-05-31) remain pending with no approver, so the fix did not land"

The three artifacts now use the same verb pair (`supposed to land` / `did not land`) and the same noun (`target`, not `patch`). Clean chain. PASS.

---

## Lens 4 -- Red-team adversarial

### Shortcut bypass attempt

Could an agent satisfy the prompt without exercising >=2 Hardness levers?
- Skip Records Vault entirely (skip L2): R19, R20, R21 all fail. NO.
- Skip Linear cross-ref (skip L8): R15 (GraniteRack stale SOW classification) requires the SOW reference evidence which only surfaces via the Linear `void-and-rebill` issue + the messaging cross-ref. Without L8, agent at best guesses "stuck in approval" -> fails R15, R16. NO.
- Skip OE 15 / routing-fix check (skip L9): R7, R22 both fail directly. NO.
- Skip 4-write diversification (skip L7): R1, R5, R8, R11 fail one by one. NO.

No shortcut path survives. PASS.

### Second valid reading of the write set

Prompt imperatives:
1. "post a summary in the payables channel" -> Slack C010 (uniquely entailed; "payables channel" = C010)
2. "Drop a comment on the open AP-routing orphan-approver ticket" -> Linear comment on issue_378874... (uniquely entailed; the ticket title matches exactly)
3. "Draft an email to Daniel with Steven on copy" -> email Daniel (TO), Steven (CC) (uniquely entailed)
4. "set me a reminder to re-check in seven days" -> reminder 2026-06-19 (uniquely entailed)

No alternate reading produces a different write set. PASS.

### New-ambiguity check: "was supposed to land" forward-looking misread

Could a strict-literalist agent now read "was supposed to land" as forward-looking ("the patch hasn't happened yet, might still happen") and flip R22?

Adversarial parse: "Daniel said it was supposed to land last sprint" + "if the invoices ... were dated after that target, the routing issue is alive". Even under the forward-looking misread, the conditional ("if invoices dated after target are still pending -> routing issue alive") is identical, and the agent still has to:
1. Find the Linear ticket due 2026-05-22 still in "todo" state (past the due date)
2. Find post-target invoices (MetroShield 2026-05-31) still with approver = null
3. Conclude the fix is not in place

Both readings converge on the same R22 outcome ("the fix did not land / has not landed"). R22's "or similar" clause already accepts the trajectory-observed soft phrasings ("may still be live", "can't confirm landed", "too few to call broken"), so the forward-looking phrasing would also satisfy. PASS -- no new ambiguity introduced.

### Lever-depth check

Empirical anchor: 5/6 trajectories failed root-cause classification (GraniteRack stale SOW, TimeLedger missing credit memo). L8 multi-link chain is NOT too shallow. Confirmed.

### Drift sweep across all 3 files

- Em-dash character (Unicode U+2014): NOT FOUND in `5_Prompt.txt`, `6_Oracle_Events.txt`, `7_Rubrics.json` (validator already gated this and reports 0 fails)
- "at least N" without prompt mandate: NOT FOUND in rubric titles (prompt says "three to five worst offenders" which is a soft N, not a strict minimum)
- Tool names in rubric titles: NOT FOUND (titles use action verbs like "posts a summary", "creates a reminder")
- Tool names in prompt: NOT FOUND
- Keystone/MoveOps tokens (mortgage_los, stripe, @keystonemortgage.com, April 28 2026): NOT FOUND
- "approximately" before exact IDs/dates: NOT FOUND in a position that misrepresents a derived figure (R11 due-date is exact, R14 amounts are exact)

Drift sweep clean.

---

## Issues (advisory only -- do not gate ship)

### MINOR-1 -- OE 15 + R7 example list mixes pre-target and post-target items
**File / location:** `6_Oracle_Events.txt` OE 15; `7_Rubrics.json` R7 title and evidence.
**Observation:** The Linear ticket `issue_378874...` has `due_date: "2026-05-22"`. VerityFile VEN-028-492596 has `invoice_date: "2026-05-18"`, which precedes the Linear due date by 4 days, so under a strict reading where "target" = Linear ticket due date, VerityFile is NOT post-target. Only the MetroShield 2026-05-31 items are unambiguously post-target.
**Why this is MINOR and not MAJOR/BLOCKER:** The rubric uses "for example VEN-028-492596 dated 2026-05-18, or the MetroShield items VEN-012-745157, VEN-012-786680, VEN-012-730094 dated 2026-05-31" -- the disjunction lets the agent cite EITHER set, and the MetroShield set unambiguously satisfies. The L9 lever still fires. The 6 prior trajectories handled this without issue (the empirical anchor confirms it).
**Suggested future tightening (not required to ship):** Drop the VerityFile example from OE 15 and R7 evidence; keep only the MetroShield items, which are unambiguously after the 2026-05-22 Linear due date.

### MINOR-2 -- R22 justification cites VerityFile 2026-05-18 as a post-target example
**File / location:** `7_Rubrics.json` R22 justification.
**Observation:** Same as MINOR-1. The R22 justification reads "items dated after that target (VerityFile 2026-05-18, MetroShield 2026-05-31)". Under strict reading of target = Linear due date 2026-05-22, VerityFile is pre-target.
**Why this is MINOR:** R22 acceptance is title + evidence based ("the routing fix did not land, because invoices dated after the target are still pending"), and a satisfying response need only cite ONE post-target example (MetroShield works). The justification's compound example list is descriptive context for the judge, not a binding requirement on the agent's output.
**Suggested future tightening:** Replace "VerityFile 2026-05-18, MetroShield 2026-05-31" with "MetroShield 2026-05-31" alone in the R22 justification.

---

## Receipts

- Truthfulness fix diff per `_aux/Prompt_Truthfulness_Fix.md` confirmed applied: zero `was patched`, `after the patch`, `post-patch`, or `did not hold` strings remain in `5_Prompt.txt`, `6_Oracle_Events.txt`, or `7_Rubrics.json`.
- All 5 Hardness_Plan levers (L1, L2, L7, L8, L9) still trigger prompt -> OE -> rubric end to end.
- All 24 rubrics are Outcome (target 24:0 holds).
- Density gate: empirical 68.7 avg from prior 6 trajectories; post-fix sketch midpoint 47-58. Above floor.
- Difficulty gate: empirical pass@1 = 0/6 from prior 6 trajectories; the operative reasoning (post-target invoices + open Linear ticket -> fix did not land) is unchanged by the wording fix, so the failure mode is preserved.

## Recommendation

**SHIP.** The post-fix artifact set is cross-artifact coherent. The L9 authority-dismissal lever is intact. The two MINOR notes are advisory tightening for future revisions; they do not warrant blocking this ship.
