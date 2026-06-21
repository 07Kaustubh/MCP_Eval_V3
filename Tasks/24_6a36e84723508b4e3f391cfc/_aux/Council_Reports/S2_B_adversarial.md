# Council B — S2 Oracle Events (Adversarial QC + Density + Hardness Preservation)

Task: `24_6a36e84723508b4e3f391cfc` (AP / Vendor Operations — Lena Park, Procurement Officer)
Deliverable: `6_Oracle_Events.txt` (22 OEs)
Universe today: 2026-06-12 (US/Eastern)
Method: five role lenses (Architect, Implementer, Red-team, Ground-truth, Integration). Every cited atom independently re-derived from `_aux/Universe_Split/` via Python (no reliance on Hardness_Plan or OE prose).

**VERDICT: GO** (Round 2, after fixes). Round 1 returned BLOCK on two Moderate issues; both are now resolved in the revised `6_Oracle_Events.txt` (see the Round 2 re-review section at the bottom of this report). The Round 1 analysis below is retained for the record.

> **Round 1 verdict (superseded): BLOCK** — two Moderate issues, both cheap to fix, neither fatal to solvability. The core reconciliation the S2 author performed (worst-offenders are acme_cloud orphans; differentiated-cause vendors are smaller-dollar and surface via the mandated cross-check; GraniteRack VEN-012-753165 sits on 219000 and is reached through the thread, not the backlog filter) is **faithful, fully grounded, and solvable** — I confirmed it independently. The block was on (1) an internally self-contradictory compound-ranking gloss in OE5 and (2) the OE3 "these 71 are employee reimbursements" characterization plus a count-robustness guard S3 must carry.

---

## Ground-truth verification ledger (what I re-derived myself)

All numbers below were computed directly from `sap_subledger.ap_invoices.json`, `oracle_gl.ogl_accounts.json`, `linear.linear_issues.json`, `email.emails.json`, `slack.slack_messages.json`, `records_vault.rv_documents.json`, `records_vault.rv_access_grants.json`, and `Brookfield_Base_Universe/8_Server_Tools_Details.json`.

| OE claim | Verified value | Match |
|---|---|---|
| 320 pending_approval (bf 127 / acme 106 / ns 87) | 320 (127 / 106 / 87) | ✅ exact |
| 249 on header 210000, 71 on 219000 | 249 / 71 | ✅ exact |
| 214 of 249 external-vendor pending over 80d | 214 | ✅ exact |
| approver null on 320/320 | 320/320 null | ✅ exact |
| 210000 = "Accounts Payable - External Vendors", 219000 = "Accounts Payable - Employee Reimbursements" (all 3 entities) | confirmed in chart of accounts | ✅ exact |
| OE5 six worst-offenders (id, $, age, entity, acct, status, approver) | all six exact (CivicSquare apinv_48e7d16bf3814a64 $289,217.86/302d; BeaconPay apinv_cfc3542208f14055 $108,826.27/320d; Clearpoint apinv_99aa0bf007864353 $224,863.67/242d; PensionBridge apinv_3188f63412744768 $185,872.57/259d; AssurePath apinv_7385e55ca9dc4612 $294,270.04/139d; VaultKey apinv_0f7b328f3be04a9c $460,556.46/137d) | ✅ exact |
| GraniteRack VEN-012-753165 on 219000 (excluded by 210000 filter) | apinv_6131b7c637aa4b6e, acct **219000**, $39,090.56, 97d, acme_cloud | ✅ exact |
| GraniteRack 210000 siblings VEN-012-259787 ($15,888.94/318d), VEN-012-697263 ($38,990.41/141d) | both on 210000, exact | ✅ exact |
| TimeLedger VEN-010-514242 ($24,475.25/99d/210000/acme); split $17,825.00 undisputed + $6,650.25 disputed; credit memo; Phase-3 | all confirmed in email body | ✅ exact |
| Separate TimeLedger VEN-010-693199 ($21,777.01) = expired-W-9 hold | confirmed (W-9 escalation email exists) | ✅ exact |
| Pinecrest VEN-006-193120 ($1,040.63/338d/210000/brookfield) = vendor dispute; 5 seats, telemetry held at 5, no 2025 grant; Andrea Phil approved | confirmed in email body | ✅ exact |
| LatticeHill VEN-033-86573 (apinv_5e09decd035d4443, brookfield, $887.04) ≠ BeaconPay VEN-033-26339 (acme) | vendor_id **VEN-033-B** vs **VEN-033** — genuinely different vendors | ✅ exact |
| Post-fix-date orphans: VerityFile VEN-028-492596 (2026-05-18), MetroShield VEN-012-745157/786680/730094 (2026-05-31) | all pending, approver null, brookfield, 210000 | ✅ exact |
| 6 Linear issue IDs (OE8) + titles | all present, titles match | ✅ exact |
| 6 email subjects/senders/dates (OE9) | all present (owen 5/18 & 5/15 & 5/18, daniel 5/21 & 5/21, andrea 5/21) | ✅ exact |
| Owen 2026-05-15 weekly-exception parents for the 4 apinv IDs; Jones Harrison 2026-03-09 parent; Edith Banda routing-problem reply | all confirmed (Owen posts are top-level parents; Edith's is a reply to Jones Harrison) | ✅ exact |
| Daniel Jones C010 thread reply 2026-05-19: "Mateo owns the routing fix and brookfield-wide pending_approval sweep, and the Linear ticket is already open for follow-up" | confirmed, is a thread reply | ✅ exact |
| RV docs: doc_eb7cb30c59bd4f03 (acme addendum), doc_2d85ac5a698745c5 (acme change_order), doc_0036f5b991574808 (ns engagement_letter); all restricted; no Acme plain engagement_letter | confirmed exactly | ✅ exact |
| Access grants: 184 total, 0 on the 3 docs, 0 for Lena, all "viewer" | confirmed exactly | ✅ exact |
| All 15 tools + param traps (payload not text; content not body; issueId+body; list_ap_invoices has no invoice_date filter) | confirmed in 8_Server_Tools_Details.json | ✅ exact |

This is an unusually high-fidelity OE: every hard identifier, amount, age, date, account, and address checks out. The defects below are confined to two reasoning/scoping clauses.

---

## [B1] QC sub-dimension scoring

Format: SUB-DIM -> SCORE -> reason. Bar is 5.

- **OE Completeness -> 5** -> Full critical path. Discovery (OE1 contacts, OE2 paginated AP pull, OE3 account split, OE4 age band, OE5 compound rank, OE6 null-approver signal, OE7 per-invoice get, OE8 Linear, OE9 email, OE10 Slack, OE15 post-fix-date check, OE16 RV scope, OE17 access grants) + all four mandated writes (OE18 Slack, OE19 Linear comment, OE20 email, OE21 reminder) + final response (OE22). Every actionable ask in `5_Prompt.txt` maps to ≥1 OE; the four writes and the vault/Linear/email cross-check are all present.
- **OE Accuracy -> 4** -> Every data atom is exact (ledger above), but OE5's *conclusion clause* is factually self-contradictory against the universe (see Issue 1). Per the QC band this is a "minor imprecision" (following the OEs still yields a correct trajectory), so 4, not 3 — but it is **not** justified by universe state (it is contradicted by it), so it cannot sit at 5.
- **Unique Ground Truth / solvability -> 4** -> The dominant reading is clear and the four writes (channel C010, issue_378874…, recipient Daniel + cc Steven, 7-day reminder) are invariant across every reasonable reading. The one soft spot is the reported external-vendor backlog count (249), which a substance-over-form agent could render as ~320 by including the 219000 vendor bills (see Issue 2). Writes/worst-offenders converge, so this is a count-emphasis ambiguity, not a write-A-vs-write-B fail — hence 4 with an S3 guard, not a 1-2 unique-GT failure.
- **Universe Feasibility (data exists) -> 5** -> Every referenced entity/record verified present and tool-retrievable.
- **Tool/Cross-service requirement -> 5** -> Spans SAP Subledger, Oracle GL (account roles), Linear, Email, Slack, Records Vault, Contacts, Reminder. Cannot be solved in one service.
- **Investigation (not pre-solved) -> 5** -> Root-cause classification per vendor requires genuine SAP→Linear→email→Slack triangulation; nothing is handed to the agent.

---

## [B2] Adversarial alt-path / second-reading analysis

I probed for a valid path the OEs miss, or a second reading that flips a **write action, recipient, or final-state**.

1. **"External-vendor activity" = account 210000 vs = bills from external vendors (the 219000 trap).** The 71 pending items on 219000 ("Employee Reimbursements") are in fact external-**vendor** bills miscoded to that account: 30 vendor names appear on **both** 210000 and 219000 (BeaconPay, AssurePath, GraniteRack, Fieldstone, CrownPeak…), and the 219000 line coding is ordinary expense (515000 salaries-indirect, 521000 software, 560000 insurance, 550000 lease, 610000 supplies) — no employee reimbursements at all. A substance-over-form agent could therefore *include* them and report a ~320 backlog. **Does this flip the final state? No.** I recomputed the compound ranking with 219000 included: the top-8 by age×$ are byte-for-byte identical to the 210000-only ranking (the best 219000 item, CivisCode at compound 10.3M, sits far below the #8 210000 item at 39.7M). Every write (Slack/Linear/email/reminder), every recipient, and the worst-offender diagnosis are unchanged. The prompt's explicit "employee reimbursements run through a different account family and are not ours" steers the dominant reading to exclude-by-account (=249). So this is **not** a B2 divergence; it is a reported-count robustness issue (Issue 2 / handled in B1 and for S3).

2. **"Worst offenders" = top-compound set vs the differentiated-cause vendors.** The top 3-5 by compound are all big acme_cloud orphans; the SOW/credit-memo/dispute vendors (GraniteRack, TimeLedger-514242, Pinecrest) are smaller-dollar and would not crack the compound top-5. An agent could reasonably label *either* group "the worst offenders." **Does this flip the final state? No.** Both readings surface the same vendors (compound rank → acme orphans; mandated cross-check → the three differentiated vendors) and converge on the same four writes and the same per-vendor ownership map. The OE correctly does per-vendor reads on both groups (OE11-14). Converges; not a divergence.

3. **Vendor-dispute ownership (Pinecrest).** The prompt lists six root-cause categories but assigns ownership for only five ("first three [SOW / change-order / out-of-scope] are procurement's… last two [credit-memo / orphan] are AP's"), leaving **"active vendor dispute" unassigned**. OE18/OE22 mirror this by naming "Pinecrest active vendor dispute" without forcing a side. Faithful to the prompt; **flagged for S3** so no rubric hard-pins Pinecrest to procurement or AP.

4. **Write-target uniqueness (checked, clean).** `issue_378874ffeb8f4cb0b0417021f2d3d647` is the unique open ("todo") orphan-approver routing ticket; competing Linear items are vendor-specific (GraniteRack/TimeLedger/Pinecrest/CrownPeak) or the W-9 sweep, none of which match "open AP-routing orphan-approver ticket." Email recipient (Daniel) + cc (Steven), Slack channel (C010 payables), and reminder horizon (2026-06-19 = +7d) are all unambiguous.

**Conclusion:** no second reading flips a write, recipient, or end-state. The only residual is the reported backlog count (Issue 2).

---

## [B3] Tool-call density projection (6-run average)

Realistic competent-Opus-4.8 trajectory that satisfies this OE list:

| Phase | OEs | Calls (typical) | Why hard to compress |
|---|---|---:|---|
| Contact + channel resolution | OE1 | 3-4 | 4 named people (Daniel/Steven/Priya/Owen) |
| Pull pending AP across 3 entities, paginate | OE2 | 4-9 | 320 rows; "do not stop at first page"; post-fix-date brookfield items live in the tail (needed for OE15) |
| Re-filter / per-invoice inspection | OE3, OE7 | 6-12 | `get_ap_invoice` on ~8 worst offenders + siblings |
| Linear cross-check | OE8 | 6-8 | list + `get_issue` on ~6 issues |
| Email cross-check | OE9 | 4-7 | multi-query search (GraniteRack/TimeLedger/Pinecrest/W-9/void-and-rebill) |
| Slack cross-check | OE10, OE15 | 5-8 | search + C010 history + locate the Daniel-Jones thread reply |
| RV scope (2 entities × 3 kinds) + gets | OE16 | 5-9 | addendum + change_order + engagement_letter across kinds |
| Access-grant check | OE17 | 3-4 | 3 docs + grantee=Lena |
| Writes | OE18-21 | 4 | Slack + Linear + email + reminder |

Low ≈ 40, high ≈ 60, **mid ≈ 46-48**. This sits squarely on the Hardness_Plan midpoint (47; low 37 / high 57) and clears the 40 floor. The non-compressible drivers — mandatory pagination of 320 rows, per-invoice `get` on the worst offenders, a 3-link chain across Linear+email+Slack for the differentiated vendors, the 2-entity × 3-kind RV sweep plus access-grant checks, and four writes — make a sub-40 *average* unlikely. A single fast-and-loose run could dip to ~37, but the 6-run mean holds above 40. **Density gate: PASS. No INSUFFICIENT_DENSITY flag.**

---

## [B4] Hardness preservation (each selected lever must be exercised)

- **L1 Latching (dollar-bias anchor + Daniel-Jones "already fixed" dismissal) -> TRIGGERED.** Dollar-bias counter-anchor in OE5 (compound vs top-dollar). Authority dismissal in OE15: the real C010 thread reply (Daniel Jones, 2026-05-19) says "Mateo owns the routing fix and brookfield-wide pending_approval sweep, and the Linear ticket is already open for follow-up." Agent must reconcile against VerityFile (2026-05-18) and MetroShield (2026-05-31) still sitting with approver null. *Note (not a regression):* the in-data dismissal is "fix owned/ticket open" rather than a hard "already patched last sprint," so the latch leans on the prompt's framing; still firmly triggered.
- **L2 Structured-DB skip / scope verification -> TRIGGERED.** OE16 forces 2 entities × 3 doc kinds; Acme has **no** plain `engagement_letter` (only addendum + change_order), Northstar has the engagement_letter — exactly the "don't report Acme as missing" trap. Verified in data.
- **L7 Multi-write diversification -> TRIGGERED.** Four writes across four services (OE18 Slack C010, OE19 Linear comment, OE20 email Daniel+cc Steven, OE21 reminder). Tools + param traps correct.
- **L8 Multi-link chain -> TRIGGERED.** Per-vendor SAP (OE7) → Linear (OE8) → email (OE9) for GraniteRack/TimeLedger/Pinecrest, synthesized in OE11-13; orphan cluster in OE14. The three named chains all resolve in data.
- **L9 Universe-grounded gotcha -> TRIGGERED.** Restricted-doc access constraint (OE17: 3 restricted docs, 0 grants, none for Lena), 210000-vs-219000 split (OE3), null-approver fingerprint 320/320 (OE6). All three verified.

No HARDNESS_REGRESSION. All five levers intact.

---

## [B5] Tool-leak / phrasing scan

- Em-dash / en-dash / figure-dash / minus-sign: **0** occurrences (programmatic scan of the OE file).
- "at least N": **0**.
- "approximately" before ids/dates: **0**.
- "(or similar)": **2**, both correctly attached to **search-query term lists** in OE9 and OE10 (the sanctioned discovery-phrasing pattern from `Reference/OE_Format.md`), not next to an exact value. Not a violation.
- Tool name in wrong position: none — all tool names sit in discovery/action step bodies, where OEs require them.

**B5: CLEAN. No phrasing hits.**

---

## Numbered issue list (Major / Moderate)

**Issue 1 — MODERATE — [B1 OE Accuracy] — OE5 compound-ranking conclusion is self-contradictory and data-contradicted.**
OE5 concludes: "VaultKey … is the single largest dollar item but at 137 days it ranks below **several** older mid-dollar items on compound exposure, so a top-dollar-only read would miss high-age items like **CivicSquare** and BeaconPay." Verified ranking (pending 210000 >80d, age×$): VaultKey is **#2** on compound (behind only CivicSquare), not "below several"; and CivicSquare ($289,217.86) is the **#3 dollar** item, so a top-dollar read would **not** miss it — the same OE names CivicSquare as the #1 compound item two sentences earlier. The hard atoms are all correct; only this gloss is wrong, but it would propagate a false "CivicSquare is buried by top-dollar" claim into rubric writing.
**Fix:** reword to, e.g., "VaultKey is the single largest dollar item ($460,556.46) but at 137 days ranks #2 on compound exposure behind CivicSquare (302 days); the compound lens elevates high-age items such as BeaconPay ($108,826.27, 320 days) that a top-5 dollar sort would bury." (Use BeaconPay as the "missed by top-dollar" exemplar; drop CivicSquare from that clause.)

**Issue 2 — MODERATE — [B1 Unique-GT / OE Accuracy] — OE3 asserts the 71 items on 219000 are "employee reimbursements"; they are external-vendor bills miscoded to that account, and the reported 249 backlog count is not robust.**
The chart-of-accounts label is correct (219000 = "Accounts Payable - Employee Reimbursements"), and excluding 219000 is the prompt-faithful reading ("a different account family and are not ours"). But the 71 pending 219000 rows are vendor bills (30 vendors appear on both 210000 and 219000; line coding is ordinary expense), so OE3's stated reason — "because employee reimbursements are … out of scope" — mischaracterizes the underlying items. A substance-over-form agent could include them and report ~320. Worst-offenders and all four writes are invariant (verified), so this is not a solvability failure, but it is a latent rubric trap.
**Fix:** (a) reword OE3 to scope by *account family* rather than asserting the items are employee reimbursements (e.g., "exclude the 71 coded to the employee-reimbursement account 219000, which the prompt places out of scope, even though some are vendor bills coded there"); (b) carry an explicit instruction into S3 that the external-vendor backlog count be treated as "~249 on account 210000" and that an agent flagging the 219000 miscoding (or reporting ~320) must not be failed — only the per-vendor diagnosis and the four writes are load-bearing.

### Minor notes (non-blocking, optional polish)
- **OE15 / OE19 "VEN-012 MetroShield":** MetroShield's vendor_id is `VEN-012-B` (GraniteRack is the real `VEN-012`). The full invoice numbers used (VEN-012-745157/786680/730094) are correct and unambiguous, so this is only a labeling nuance; consider "the MetroShield items (VEN-012-745157, …)" to avoid implying they belong to GraniteRack's vendor_id.
- **OE15 post-fix-date example:** VerityFile (invoice_date 2026-05-18) is ~1 day before Daniel's 2026-05-19 post; the MetroShield items (2026-05-31) are the cleaner "dated after the patch" exemplars. The patch was claimed for a prior sprint so 5/18 is still defensibly post-effective, but leading with MetroShield (and noting the sprint timing) tightens the signal.

---

## Final judgment on the author's reconciliation (per the S2 brief)

Independently verified: the S2 author's handling is **(a) faithful** to the prompt as written (exclude the reimbursement account family; rank by compound; surface differentiated causes via the mandated vault/Linear/email cross-check; defer all approval/routing), **(b) fully grounded** (every atom re-derived from the split, including the GraniteRack-753165-on-219000 detail and the LatticeHill-vs-BeaconPay VEN-033 / VEN-033-B distinction the Hardness_Plan had backwards), and **(c) solvable** with invariant writes. It is **not** a Completeness defect and **not** a defect in the 219000/worst-offender reconciliation itself. The BLOCK rests solely on the OE5 reasoning gloss (Issue 1) and the OE3 wording + S3 count-robustness guard (Issue 2).

**Round 1 verdict (superseded): BLOCK** (2 Moderate, both quick fixes). See Round 2 below for the resolution and final verdict.

---

## ROUND 2 RE-REVIEW (after author fixes)

Re-read the revised `6_Oracle_Events.txt` and re-checked both Moderate issues against the same verified atoms. Density, hardness levers, and phrasing were re-scanned.

### Issue 1 (OE5 compound-rank gloss) — RESOLVED ✅
Revised Conclude clause reads: "VaultKey … ($460,556.46) is the single largest dollar item and stays near the top on compound exposure, but the age weighting promotes the oldest items so CivicSquare ($289,217.86 at 302 days) leads on compound, and a top-dollar-only read would underweight a high-age mid-dollar item like BeaconPay ($108,826.27 at 320 days)."
Checked against verified compound ranking (pending 210000 >80d, age×$):
- VaultKey = #1 by dollar ($460,556.46) and #2 by compound (63.1M) → "single largest dollar item … stays near the top on compound" is **accurate**.
- CivicSquare = #1 by compound (87.3M), 302 days, $289,217.86 → "age weighting … CivicSquare leads on compound" is **accurate**.
- BeaconPay = $108,826.27 / 320 days, #10 by compound and **not** in the top-8 by dollar → "a top-dollar-only read would underweight a high-age mid-dollar item like BeaconPay" is **accurate and the correct exemplar**.
The self-contradiction is gone: CivicSquare is now correctly the compound leader (not the "missed by top-dollar" example), and BeaconPay is the underweighted-by-dollar item. Internally consistent and data-accurate.

### Issue 2 (OE3 219000 / count hard-pin / substance-over-form) — RESOLVED ✅
Revised OE3 now: (a) says "about 249" / "about 71" (OE4 says "about 214") — count no longer hard-pinned; (b) scopes the backlog to the 210000 external-vendor family and sets aside the 219000 family "per the prompt," framed as "employee reimbursements are a different account family and are not procurement's queue" rather than asserting all 71 rows are employee reimbursements; (c) explicitly calls the account-family split "the scoping lens rather than a strict vendor-versus-employee guarantee"; (d) notes "a few genuine vendor obligations are accrued to 219000 (for example the GraniteRack void-and-rebill item in OE 11), which the mandated cross-check still surfaces."
This matches the verified data exactly (30 vendors appear on both 210000 and 219000; GraniteRack VEN-012-753165 is on 219000 and is reached via the void-and-rebill thread, not the backlog filter). The substance-over-form mischaracterization is removed, the count is robust, and the S3 guard is now baked into the OE prose itself. The earlier-recommended rubric guidance (don't fail an agent who flags the 219000 miscoding or reports a broader count) is now self-evident from OE3.

### B3 density — UNCHANGED (PASS) ✅
The edits are wording-only on OE3/OE4/OE5: no steps added or removed, no tool calls changed. Projection holds at **~46-48 (>= 40)**.

### B4 hardness levers — ALL FIVE STILL TRIGGERED ✅
L1 (OE5 dollar-vs-compound anchor + OE15 Daniel-Jones dismissal), L2 (OE16 2-entity × 3-kind scope), L7 (OE18-21 four writes), L8 (OE7/8/9 → OE11-14 per-vendor chain) — all untouched. L9 (210000-vs-219000 split + restricted docs + null approver) is, if anything, **richer**: OE3's "scoping lens, not a strict guarantee" framing plus the explicit note that genuine vendor obligations sit on 219000 deepens the account-split gotcha rather than weakening it. No HARDNESS_REGRESSION.

### B5 phrasing — CLEAN, no new issues ✅
Re-scanned the full file: em-dash / en-dash / figure-dash / minus-sign = **0**; "at least N" = **0**; "approximately" = **0**. The three new "about" hedges sit before **counts** (249 / 71 / 214), not before ids or dates, so they are valid robustness language, not an "approximately before an id/date" violation.

### Minor note (non-blocking, optional)
OE18 still describes the Slack-post content as "(249 items on account 210000, 214 over 80 days, employee-reimbursement items on 219000 excluded)." Both figures are exact-correct, so this is not an error, but for full consistency with the reworded OE3 it could mirror the "set aside the 219000 employee-reimbursement account family" framing and the "about" hedge. Purely cosmetic; does not affect the verdict.

### Round 2 scoring delta
- OE Accuracy: 4 → **5** (OE5 gloss corrected; all atoms exact).
- Unique Ground Truth / solvability: 4 → **5** (count robustness + scoping-lens framing remove the residual ambiguity; writes remain invariant).
- OE Completeness: **5** (unchanged). Universe Feasibility / Cross-service / Investigation: **5** (unchanged).

**VERDICT: GO.** Both Round 1 Moderate issues are resolved, every applicable QC sub-dim is now 5, no adversarial divergence, projected tool calls ~46-48 (>= 40), all five hardness levers preserved, and the phrasing scan is clean. Clear to proceed to S3.
