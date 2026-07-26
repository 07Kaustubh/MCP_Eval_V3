# Council B — Adversarial QC + Density + Hardness Preservation (OE Phase)

**Task:** `Tasks/41_6a61a86a3453b3714bdc72ef` — Tanya Mitchell (Unit 14) delinquency/eviction, persona Patricia Nguyen (p_010, Onsite PM).
**Deliverable reviewed:** `6_Oracle_Events.txt` (18 OEs)
**Universe:** StarPM V4 · dual-model (Opus 4.8 + Gemini) · density bar per-model midpoint ≥40 PASS.
**Method:** Five role lenses (Architect, Implementer, Red-team, Ground-truth, Integration); verdict is the UNION. Every load-bearing OE claim was verified byte-for-byte against `_aux/Universe_Split/`.

---

## Ground-truth verification (Red-team + Ground-truth lenses)

Every dollar amount, ID, tool, parameter, and expected value in OE 1–18 was checked against the per-task universe. **All verified accurate.**

| Claim | OE | Universe value found | Match |
|---|---|---|---|
| Bill QR-2026-0441 = id 232176553533, VendorRef "Alamo HVAC Services", **no CustomerRef**, Balance 2132.0 | 4 | id 232176553533, VendorRef "Alamo HVAC Services", CustomerRef absent, Balance 2132.0 | ✅ |
| Bill lines 847 (May arrears) + 925 (June rent) + 210 (late fees) + 150 (credit) | 5 | lines exactly 847.0 / 925.0 / 210.0 / 150.0 | ✅ |
| Charges 1982 − 150 credit = **net 1832**; stored 2132 double-counts the credit | 5 | 847+925+210 = 1982; +150 stored = 2132; net 1832 | ✅ |
| Invoice 7214 = id 283231782926, TotalAmt 8173.44, **Balance 0.00**, CustomerRef Tanya proj-2e48c594aab7 | 3 | exact match; settled by payment 952690463873 (8173.44) | ✅ |
| Invoice charge lines 1125 / 975 / 187.50 differ from bill lines | 5,9 | 1125.0 / 975.0 / 187.5 / 5885.94 credit | ✅ |
| Bill 2026-EV-047 = id 146128608253, Balance 185.0, no CustomerRef (internal admin cost) | 4 | exact; VendorRef "Hill Country Plumbing", no CustomerRef | ✅ |
| Customer proj-2e48c594aab7 "Tanya Mitchell", no aggregate balance stored | 2 | DisplayName "Tanya Mitchell", Balance None | ✅ |
| Contacts: Tanya (tanya.mitchell@gmail.com); Linda Castillo job **"Property Owner"**; John Castillo job **"Water Delivery Representative"** | 1 | all three emails + both job titles exact | ✅ |
| Airtable base appPropertyOps → tblMakeReady ("Make-Ready Turns"), tblMaintenanceTickets ("Maintenance Tickets") | 6 | exact | ✅ |
| reca8230a8fd9ff51 fldUnit "Sunset Ridge Unit 14"; recc83c05d889b354 fldUnit "Unit 14", selSched, JP-coordination hold note, **last_modified 2026-07-01 11:18:57**; rec94e86a3007dd5e "Rio Bend - Unit 14" selReady | 7,8 | all exact incl. modified timestamp (reca8230a8 modified 2026-06-07) | ✅ |
| Supersession chain: rec769 (active plan/Las Palmas 4B) → rec8005 (Plan Breached, selProg) → rec915 (3-day notice) → rec378 (did not cure) → receee (awaiting sign-off) → recc83 (JP coordination, current) | 9 | all six records + note text verified | ✅ |
| DLQ-2026-0601 (recc0ecc885e9645e) selHigh, "Past Due - Grace Period Expired", **$75** late fee | 10 | exact | ✅ |
| EVF-2026-014 (rec922b9a2d1b9451) fldCompletionDate 2026-06-30, "Owner Approved - Ready to File", Linda Castillo auth, package staged | 10 | exact | ✅ |
| Gmail thread 621640f9e7aa6d46 "Eviction Filing Authorization. Tanya Mitchell. Unit 14" — Brooke request → Linda authorization reply | 11 | thread + both messages verified | ✅ |
| Slack C003 (#general) ts 1782673915 (plan breached), 1782673930 (3-day served), 1782881568 (owner-approved, JP coordination, flag if pays); superseded ts 1778696318/1778696320 (court stage / hearing) | 12 | all five messages verified in C003 | ✅ |
| Linear OPS-32 "Eviction Hearing - Mitchell, **Harris Property**", In Progress, priority 1, team_001; OPS-38, OPS-54 | 13 | all three titles/states/team exact | ✅ |
| Slack channels C003 #general, C004 #make-ready | 12,16 | exact | ✅ |
| All 21 referenced tools exist in catalog; params `issueId`/`body`, `channel_id`/`message`, `to`/`subject`/`body`, `baseId`/`tableId`/`records`, `team`/`query` all correct | 14–17 | verified against `7_Server_Tools_Details.json` | ✅ |

Zero ground-truth discrepancies found.

---

## [B1] QC sub-dim scoring

**SUB-DIM OE Completeness -> SCORE 5/5 (NON-FAIL scheme 3/4/5)** -> Full critical path present: identity resolution (OE1) → arrears discovery+derivation (OE2-5, incl. flagship AP-bill skip and net-vs-gross) → Airtable base/table resolution + make-ready read/disambiguation (OE6-8) → supersession trace (OE9) → ticket cross-ref + owner-auth confirmation (OE10-11) → Slack current status (OE12) → Linear ticket ID (OE13) → all four writes (OE14 update, OE15 note, OE16 Slack, OE17 draft) → content spec (OE18). No critical step missing.

**SUB-DIM OE Accuracy -> SCORE 5/5 (NON-FAIL scheme 3/4/5)** -> Every tool exists and maps to the correct service; every parameter name matches the catalog; every dollar figure, record ID, email, job title, ticket status, timestamp, and Slack ts was verified against the universe with zero discrepancies. Following the OEs literally produces a correct trajectory.

Minor, non-scoring observation: OE18 is a content-requirements/verification consolidation rather than a pure tool-call step. It is benign (drives Outcome 2.1/1.2 rubric content, all its facts accurate) and removes nothing from the critical path; does not lower either score.

---

## [B2] Adversarial alt-path

**(a) Second target for the "eviction ticket" note — ACCOMMODATED.** Two eviction-related tickets exist: Linear OPS-32 (Eviction Hearing) and Airtable EVF-2026-014 (Eviction Filing, rec922b9a2d1b9451). DLQ-2026-0601 is delinquency, not eviction. OE15 names Linear OPS-32 as primary (`save_comment`) **and explicitly states "The Airtable eviction record EVF-2026-014 … is an acceptable alternative surface for this note."** Same status content, different surface — a channel-of-delivery variation (QC 06/09 non-fail band). Divergence is acknowledged; no failure.

**(b) Alternative balance figures — CORRECTLY PINNED.** Candidates: $0 (paid-invoice decoy, wrong), $2,132 (stored, double-counts credit, wrong), $1,982 (charges only), $1,832 (net). The prompt explicitly asks to "walk it back to the underlying charges … not double-counting any credit or adjustment applied," which forces the credit to be applied and uniquely selects **$1,832**. OE5 derives it soundly (1982 charges − 150 credit) and OE17/18 report it. $1,982 is defensible only if one ignores the prompt's explicit credit instruction — the prompt language rules it out, so this is NOT a UGT split. Correctly pinned.

**(c) Make-ready channel — C004 correct.** Prompt: "Drop the **make-ready team** a heads-up in **our channel**." "make-ready team" + "our channel" anchors to #make-ready (C004), not #general (C003, where the eviction thread happens to live). OE16 names C004 #make-ready. Defensible and dominant; the eviction discussion living in C003 does not make C003 "the make-ready team's channel." No divergence the OE fails to accommodate.

No adversarial divergence the OE chain mislabels or leaves unaccommodated.

---

## [B3] Tool-call density projection (per model)

Independent trajectory sketch (competent agent), counting realistic reads incl. lever-driven dead-ends and cross-service triangulation:

- Identity: contacts ×2–3 (Tanya, Linda, disambiguate John) = ~3
- Arrears: search_customers + (catch-all 13-entity inspection / get_customer_balance) + search_invoices + read_invoice 7214 + search_bills + read QR-2026-0441/2026-EV-047 = ~7–9
- Airtable: list_bases + list_tables + search_records + individual reads of the 6-record supersession chain + Rio Bend exclusion + tickets search + DLQ/EVF reads = ~11–15
- Owner-auth: search_threads + get_thread = ~2
- Slack: search + read C003 (+C004) = ~2–3
- Linear: list_issues + get_issue OPS-32/38/54 = ~2–3
- Writes: update_records + save_comment + slack_send + create_draft = 4

**Opus 4.8 midpoint ≈ 48 → PASS (≥40).** Thorough Opus behavior on a 5-lever + stacked-near-miss task (flagship structured-DB skip forces the bills search after the invoice reads clean; three conflicting eviction narratives force reconciliation; 6-record chain + Rio Bend/Las Palmas/catch-all disambiguation) realistically lands 45–55.

**Gemini midpoint ≈ 43 → PASS (≥40).** ~0.85× leaner traversal (Task 40 empirical 33–47); this task's heavier lever stack keeps it at ~40–46. Tighter margin than Opus but clears the bar.

**Distinct-service breadth:** OEs actually exercise **6 services** — airtable (~30%), quickbooks (~20%), slack (~12%), gmail (~11%), linear (~10%), contacts (~6%) — **≥4 services each ≥5% → PASS**; max service ~30% (well under 60%, cross-correlation-heavy, not single-service). 

*Challenge to Hardness_Plan:* its breadth table lists 8 services incl. hubspot (~3) and gcalendar (~3), but the OE chain resolves identities via **contacts** (not hubspot) and does **not** invoke gcalendar. Actual breadth = 6 services. This does not affect the gate (6 ≥ 4, all dominant services ≥5%) and both models still clear ≥40, so the ~50 Opus / ~43 Gemini projection is validated in aggregate; the specific hubspot/gcalendar rows are optional corroboration, not critical path.

---

## [B4] Hardness preservation

| Lever | Exercised by | Status |
|---|---|---|
| **L2 structured-DB skip (flagship)** | OE3 ($0 paid-invoice decoy) + OE4 (AP bill QR-2026-0441, VendorRef, no CustomerRef → invisible to customer/invoice queries) + OE5 | ✅ preserved |
| **L10 reversal/supersession** | OE9 (6-record chain to JP-coordination current) + OE10 (EVF supersedes "awaiting sign-off") + OE12 (superseded Slack court-stage framing) | ✅ preserved |
| **L1 latching** | OE13 (Linear OPS-32 "Eviction Hearing / Harris Property" overstates progress + mis-attributes owner) + OE12 (older court-stage Slack) | ✅ preserved |
| **L11 net-vs-gross/sign** | OE5 ($150 credit stored as positive → 2132 vs net 1832) + OE17/18 (report 1832) | ✅ preserved |
| **L31 negative-directive omission (Gemini diff.)** | OE14 + OE16 + OE17 + OE18 all demand explicit "must NOT begin / must NOT market — possession not returned" | ✅ preserved (4×) |
| **L6 near-miss (stacked)** | OE7 (Rio Bend Unit 14 excluded) + OE1 (John vs Linda Castillo; catch-all) + OE9 (Las Palmas 4B dual designation) + OE5 (catch-all customer) | ✅ preserved |

All 5 selected levers + stacked L6 triggered. **No HARDNESS_REGRESSION.**

---

## [B6] Upstream propagation

**No PROPAGATE flags.** The prompt independently disambiguates each potential fork: the balance (explicit "not double-counting any credit" → $1,832), the owner ("the owner" = Linda Castillo, sole Property-Owner contact), the channel ("make-ready team … our channel" → #make-ready). The "eviction ticket" note has two valid surfaces (Linear OPS-32 / Airtable EVF-2026-014) but identical action + content, and OE15 accommodates it — a grading accommodation, not a prompt-ambiguity root cause (per OE Authority Rule, an OE "both valid" accommodation does not fail UGT). Every selected lever is genuinely visible to the agent under the prompt's reassuring framing. Nothing roots to S1 or the Hardness plan in a blocking way.

---

## [B8] OE Completeness semantic (dependency-chain walk)

| Required step | Covered? |
|---|---|
| Contact/owner resolution before owner draft | OE1 → OE17 ✅ |
| Customer lookup before invoice/bill reads | OE2 → OE3/4 ✅ |
| AP-bill discovery (flagship) | OE4 ✅ |
| Net derivation (1982 − 150 = 1832) | OE5 ✅ |
| Airtable base/table resolution before make-ready read+write | OE6 → OE7/8 → OE14 ✅ |
| Supersession trace | OE9 ✅ |
| Owner-auth confirmation | OE10 + OE11 ✅ |
| Slack current-status check | OE12 ✅ |
| Linear ticket identification | OE13 ✅ |
| Four write steps | OE14/15/16/17 ✅ |

**Zero OE_INCOMPLETE.**

---

## [B9] OE service mapping

Every OE's tool/service matches the data type: contacts→identities (OE1); quickbooks→customer/invoices/bills (OE2-5); airtable→bases/make-ready/tickets [SoR] (OE6-10,14); gmail→owner-auth thread + draft (OE11,17); slack→chat (OE12,16); linear→eviction mirror ticket + comment (OE13,15). Delinquency/eviction tickets DLQ/EVF correctly read from Airtable tblMaintenanceTickets (property-ops SoR), and the note is placed on Linear OPS-32 (secondary mirror) with Airtable EVF accepted. **Zero OE_SERVICE_MISMATCH.**

---

## Forward + Reverse coverage

**FORWARD (every actionable prompt sentence → ≥1 OE):** owe/walk-back-to-charges/no-double-count → OE2-5; eviction status/petition-filed?/owner-auth → OE8-13; clear-for-make-ready-or-hold → OE7/8/18; update make-ready record → OE6/7/14; note on eviction ticket → OE13/15; heads-up in make-ready channel → OE16; draft owner email (balance/status/unit) → OE1/17; correct stale assumptions ("mostly squared away", "at hearing stage") → OE18. **Full.**

**REVERSE (no scope creep):** every OE maps to a real ask; no OE exceeds prompt scope. **ESA/reasonable-accommodation correctly EXCLUDED** — this Patricia rent/eviction prompt never mentions the ESA thread (that was sibling Task 40's Lisa Smith scenario, legally independent per Hardness_Plan). Including it would be reverse-coverage creep; the OEs rightly keep it out and even flag it only as a near-miss to avoid conflation. No evidence in THIS prompt argues for ESA inclusion.

---

## VERDICT: GO

Both OE sub-dims score 5; no unaccommodated adversarial divergence; density ≥40 midpoint both models; all levers preserved; no PROPAGATE; zero OE_INCOMPLETE; zero OE_SERVICE_MISMATCH; full forward+reverse coverage.

```json
{"phase":"oe","council":"B","task_dir":"Tasks/41_6a61a86a3453b3714bdc72ef","verdict":"GO","perspectives":{"B1":"OE Completeness 5/5, OE Accuracy 5/5 — all claims verified against universe, zero discrepancies","B2":"alt-paths accommodated: eviction-ticket dual surface (OE15), balance uniquely $1,832 per prompt credit instruction, channel C004 correct","B3":"Opus midpoint ~48 PASS, Gemini ~43 PASS; breadth 6 services ≥4 at ≥5% PASS","B4":"5 selected levers + stacked L6 all preserved","B6":"no PROPAGATE — prompt independently disambiguates every fork","B8":"zero OE_INCOMPLETE — full dependency chain covered","B9":"zero OE_SERVICE_MISMATCH — all tools map to correct service","coverage":"full forward + reverse; ESA correctly excluded"},"scores":{"OE Completeness":{"score":5,"scheme":"3/4/5","reason":"Full critical path: identity+arrears discovery+net derivation+Airtable resolution+supersession+owner-auth+Slack status+Linear ID+all four writes"},"OE Accuracy":{"score":5,"scheme":"3/4/5","reason":"Every tool/service/parameter/expected value verified against per-task universe with zero discrepancies"}},"density_projection":{"midpoint":48,"band":"PASS","breadth_services":6,"breadth_band":"PASS","gemini_midpoint":43,"gemini_band":"PASS"},"lever_preservation":{"expected":5,"preserved":5,"missing":[]},"bucket_1_risk_pct":null,"iteration":0,"timestamp":"2026-07-24"}
```
