# S2 Council B — Adversarial QC Review

**Task:** Tasks/38_6a5edd95a6946f6c4d160b5a
**Persona:** Denise Morales (Onsite Property Manager, p_013)
**Universe:** StarPM · Today = 2026-07-01 (America/Chicago)
**Artifacts reviewed:** `5_Prompt.txt` · `6_Oracle_Events.txt` (OE1-OE25) · `_aux/Hardness_Plan.md`
**Reference specs:** `Docs_starpm/7_QC_Spec_Doc1.json` · `Evals_starpm/2_OE_Eval.md`

---

## B1 — FORWARD COVERAGE (Prompt → OE)

Every explicit and implicit ask in `5_Prompt.txt` mapped to ≥1 OE step.

| # | Prompt ask | Covering OEs | Verdict |
|---|---|---|---|
| 1a | Check Sunset Ridge 208B AC **true status** | OE3 (Airtable ticket MT-2026-063), OE4 (Tony Slack), OE5 (Gmail search), OE6 (Tony email), OE7 (Alamo HVAC compressor-failure email) | COVERED |
| 1b | **Update the maintenance record** with true status | OE8 (update_records_for_table on rec7f6e5d4c3b2a1e) | COVERED |
| 1c | **Post to #maintenance** so team works from correct info | OE9 (slack_send_message channel_id: "C001") | COVERED |
| 2a | Figure out **real Ridgeview roof owner exposure** | OE10 (MT-2026-047), OE11 (make-ready rec8b679d92f30753), OE12 (4 Ridgeview threads), OE13 (Finley approval), OE14 (coordination chain), OE15 (search_bills), OE16 (bill 2026-481 PrivateNote), OE17 (bill PD-2026-084 PrivateNote), OE18 (AR invoice 2026-494), OE19 (payment 972286822645) | COVERED |
| 2b | **Update the Linear issue** with current status | OE20 (list_issues discovers no existing issue) → OE21 (save_issue creates new) | COVERED (with minor prompt-vs-universe caveat, see Findings below) |
| 3a | Look up **Tanya Mitchell status** | OE22 (Airtable make-ready Las Palmas 4B), OE24 (Slack ESA request) | COVERED |
| 3b | **Confirm which unit she is in** | OE22 (rec769c9f03f0b85f Las Palmas 4B), OE23 (Slack C003 confirmation) | COVERED |
| 4a | **Draft Gmail to Aurora with full update** | OE1 (Aurora contact lookup for recipient email), OE25 (create_draft) | COVERED |

**Implicit asks** — the four write actions (Airtable update, Slack post, Linear issue, Gmail draft) plus the contact resolution needed for the Gmail recipient are all covered.

**B1 verdict: PASS** — no uncovered prompt asks.

---

## B2 — REVERSE COVERAGE (OE → Prompt)

Every OE step traceable to a real prompt need.

| OE | Traces to | Notes |
|---|---|---|
| OE1 (Aurora contact) | Ask 4 (Gmail recipient) | Required for create_draft |
| OE2 (Tony contact) | Ask 1 context | **Minor flag** — Tony is named in prompt but role is not required to verify. Low-value but defensible as authority-context establishment for L9 justification. Not scope creep, borderline. |
| OE3-OE7 (208B discovery chain) | Ask 1a | Direct |
| OE8 (Airtable update) | Ask 1b | Direct |
| OE9 (Slack post) | Ask 1c | Direct |
| OE10-OE19 (Ridgeview discovery + billing chain) | Ask 2a | Direct — full 5-hop chain per L8 |
| OE20-OE21 (Linear check + create) | Ask 2b | Direct |
| OE22 (Tanya Airtable) | Ask 3a/3b | Direct |
| OE23 (Slack unit confirmation) | Ask 3b | Direct — cross-validation via L6 defeat |
| OE24 (ESA request) | **Implicit — status completeness** | Prompt asks for "current status." ESA request is part of current status per Hardness Plan Stump Hypothesis 4 (Fair Housing risk if omitted). Defensible — not scope creep. |
| OE25 (Gmail draft) | Ask 4 | Direct |

**B2 verdict: PASS** — no scope creep. OE2 is the only borderline call and is justified as L9 authority-context anchoring.

---

## B3 — DENSITY PROJECTION

### Per-OE tool-call count (minimum path)

| OE | Tool calls | Notes |
|---|---|---|
| OE1 | 1 | contacts_search_contacts |
| OE2 | 1 | contacts_search_contacts |
| OE3 | **3** | list_bases + list_tables_for_base + search_records |
| OE4 | 1 | slack_search_public_and_private |
| OE5 | 1 | search_threads |
| OE6 | 1 | get_thread |
| OE7 | 1 | get_thread |
| OE8 | 1 | update_records_for_table |
| OE9 | 1 | slack_send_message |
| OE10 | 1 | search_records |
| OE11 | 1 | search_records |
| OE12 | 1 | search_threads |
| OE13 | 1 | get_thread |
| OE14 | **2** | two get_thread calls |
| OE15 | 1 | search_bills |
| OE16 | 1 | get-bill |
| OE17 | 1 | get-bill |
| OE18 | 1 | search_invoices |
| OE19 | 1 | search_payments |
| OE20 | 1 | list_issues |
| OE21 | 1 | save_issue |
| OE22 | 1 | search_records |
| OE23 | 1 | slack_search_public_and_private |
| OE24 | 1 | slack_search_public_and_private |
| OE25 | 1 | create_draft |
| **TOTAL MIN** | **27** | Strict shortest path |

### Upper bound (agent behavior with lever-driven exploration)

| Contributor | Extra calls |
|---|---|
| L6 (7 Unit 14 decoys) — agent retrieves individual records to disambiguate | +5-7 |
| L8 (4 Ridgeview Gmail threads) — walk beyond the 2 explicit get_thread calls | +2-3 |
| L9 (Tony vs Alamo) — cross-verification, extra Slack/Gmail searches | +2-3 |
| L11 (net-vs-gross) — agent pulls credit memos, additional invoices, customer records | +3-4 |
| Airtable base/table exploration (list_bases likely returns multiple bases) | +2-3 |
| Contacts lookups for other personas (Finley, Donovan, Phillips, Mitchell) | +3-4 |
| HubSpot owner lookup for Finley | +1-2 |
| QB customer/vendor entity lookups | +1-2 |
| Retries, dead-end searches, wrong-first-guess parameters | +3-5 |
| **Upper bound extra** | **+22-33** |

**Upper bound total: 49-60** (median 55)

### Projection

- **Lower bound:** 27
- **Upper bound (median of range):** 55
- **Midpoint:** (27 + 55) / 2 = **41.0**

### Verdict

**B3 verdict: THIN_DENSITY** (midpoint 41, in 40-49 band).

- The Hardness Plan projects 50.0 midpoint via a per-component breakdown that overlaps write-action costs with per-lever costs. A cleaner min-vs-max midpoint calculation lands at ~41.
- **Not a BLOCKER** (above 40 floor). Operator should note this task is at moderate risk of underflowing 40+ average tool calls on real platform runs. Consider whether the write-action buffer or a cross-service triangulation OE can be lightly padded — but no BLOCK finding.
- If S3 rubric writing adds explicit rubric-worthy discovery beats (e.g., "Agent verifies the ESA context is on file" as an Outcome that requires an additional Slack search), the effective density will climb.

---

## B4 — HARDNESS LEVERS

All 5 selected levers from `_aux/Hardness_Plan.md` are exercised.

| Lever | Required coverage | OEs that exercise it | Verdict |
|---|---|---|---|
| **L9** (Authority dismissal) | OE4 + OE6 + OE7 | OE4 (Tony Slack casual assessment), OE6 (Tony email repeating same claim), OE7 (Alamo HVAC compressor-failure override) | PASS |
| **L11** (Net-vs-gross) | OE15 + OE16 + OE17 | OE15 (two QB bills surface, naive $16,800), OE16 (PrivateNote leg-1 pass-through), OE17 (PrivateNote leg-2 itemized restatement of same job → $8,400 true) | PASS |
| **L2** (Structured-DB skip) | OE3/OE10/OE11/OE22 | OE3 (Airtable is primary source for 208B ticket), OE10-11 (Airtable is primary source for Ridgeview MT and MR), OE22 (Airtable is primary source for Tanya, not Slack) | PASS |
| **L8** (Multi-link chain) | OE12 + OE13 + OE14 | OE12 (4 Ridgeview threads listed), OE13 (Finley formal approval), OE14 (Brooke/Pete/Finley coordination walk). Full 5-hop reconciliation also covered by OE10 → OE11 → OE15 → OE16/17 → OE18 → OE19. | PASS |
| **L6** (Near-miss entity) | OE22 + OE23 | OE22 (7 Unit 14 decoy records returned alongside authoritative Las Palmas 4B), OE23 (Slack C003 cross-check with 2 additional Unit 14 decoy messages) | PASS |

**B4 verdict: PASS** — every lever has ≥1 OE that materially exercises it.

---

## B8 — RUBRIC FORWARD-MAP

Every write-action OE has a plausible rubric coverage point.

| Write OE | Action | Outcome 1.1 (action result) | Outcome 1.2 (content) |
|---|---|---|---|
| OE8 | update_records_for_table on MT-2026-063 | "Agent updates Sunset Ridge 208B maintenance ticket to reflect Alamo HVAC compressor-failure finding, superseding Tony Reyes's dirty-filter assessment." | Optional 1.2 for updated notes/status field content — likely rolled into 1.1 |
| OE9 | slack_send_message to #maintenance (C001) | "Agent posts a correction note in #maintenance..." | 1.2: "message identifies compressor failure (not dirty filter), references MT-2026-063 update" |
| OE21 | save_issue create in Linear OPS team | "Agent creates a new Linear issue tracking Ridgeview roof owner billing status." | 1.2: "issue body states $8,400 vendor cost (single Big Bend job), notes 2026-481 + PD-2026-084 are same-scope, AR invoice 2026-494 outstanding at $8,400, $640 payment applied to a separate vacancy invoice" |
| OE25 | create_draft Gmail to Aurora | "Agent drafts email to aurora.winona@starpm.com." | 1.2: three parallel content requirements — (i) 208B compressor failure; (ii) Ridgeview $8,400 real exposure with dual-bill and payment-misapplication clarification; (iii) Tanya at Las Palmas 4B with payment plan + ESA context |

**B8 verdict: PASS** — every write-action OE has clear Outcome 1.1 hooks and 1.2 content hooks where required. OE25 in particular has strong 1.2 material for a multi-part content rubric (per Hardness Plan Stump Hypotheses 1-4).

---

## B9 — OE ACCURACY SCORE

Per `Docs_starpm/7_QC_Spec_Doc1.json`, OE Accuracy grading:

**Verification checkpoints:**

| Check | Result |
|---|---|
| StarPM parameter conventions per root AGENTS.md | ✓ OE9 uses `channel_id` + `message` (correct StarPM param, not `payload`). ✓ OE25 uses `to[]` + `subject` + `body` (correct — not `content`). ✓ OE21 uses `team` (correct — not `teamId`). ✓ OE3/OE8/OE10/OE11/OE22 use camelCase `baseId`/`tableId` (correct). |
| Tool-name plausibility for StarPM Airtable server | `list_bases`, `list_tables_for_base`, `search_records`, `update_records_for_table` — consistent StarPM naming pattern. **Suggest AUDIT verify against `StarPM_Base_Universe/7_Server_Tools_Details.json`** — accuracy score assumes correct. |
| Universe fact cross-check via Hardness Plan citations | Tony Reyes (Lead Maintenance Technician), Aurora Winona (President), Robert Finley (owner), Alamo HVAC (compressor-failure email), bills 2026-481 + PD-2026-084 ($8,400 each, same job), AR invoice 2026-494 ($8,400), payment 972286822645 ($640 applied to separate invoice), 7 Unit 14 decoys + Las Palmas 4B — all present in Hardness Plan evidence. |
| Record IDs and thread IDs | OE-cited IDs (rec7f6e5d4c3b2a1e, rec769c9f03f0b85f, thread b2f4e9a3c71d0856, thread 0133155c8a154ab1, bill 528539050604, bill 301715729067, payment 972286822645, Slack msg c7e3a2f5b4d1e9a8b3c2f7e4d5a1b9c8, etc.) — specific, consistent with a real universe extract. **Suggest AUDIT spot-check 3-5 of these against `3_UniverseDataForThisTask.json`.** |
| Date/time consistency | OE4 timestamp 1782914700 = 2026-07-01 07:25:00 UTC — within active window. OE21 references OPS-10 (Mid-Year Owner Portfolio Reviews) and OPS-100 (May Monthly Owner Report Finley Properties) — plausible for July timing. |

**B9 verdict: 5** (all tools/services/parameters/expected data match universe as documented in the Hardness Plan). Caveat: direct universe-JSON verification is deferred to AUDIT; if AUDIT finds any specific record ID or tool name mismatch, downgrade to 4.

---

## B10 — OE COMPLETENESS SCORE

Per `Docs_starpm/7_QC_Spec_Doc1.json`, OE Completeness grading (5 = full critical path).

**Critical path checklist:**

| Category | Coverage |
|---|---|
| **Discovery** — 208B AC | OE1 (Aurora), OE2 (Tony), OE3 (Airtable ticket), OE4 (Slack), OE5-7 (Gmail chain: search + Tony email + Alamo HVAC) — ✓ full |
| **Discovery** — Ridgeview roof scope | OE10 (MT), OE11 (MR), OE12 (Gmail thread list), OE13 (Finley approval), OE14 (coordination walk) — ✓ full |
| **Discovery** — Ridgeview billing reconciliation | OE15 (bill list), OE16-17 (per-bill PrivateNote reads), OE18 (AR invoice), OE19 (payment) — ✓ full 5-hop chain |
| **Discovery** — Tanya Mitchell | OE22 (Airtable MR + decoys), OE23 (Slack unit confirmation), OE24 (ESA request) — ✓ full |
| **Dependency chain** — 208B | Tony Slack → Tony email → Alamo email (agent reconciles authority vs professional inspection) ✓ |
| **Dependency chain** — Ridgeview | MR row → MT ticket → 2 QB bills → AR invoice → payment ✓ |
| **Dependency chain** — Linear | OE20 (check existing) → OE21 (create new) ✓ |
| **Write actions** | OE8 (Airtable), OE9 (Slack), OE21 (Linear), OE25 (Gmail) — ✓ all 4 covered |

**B10 verdict: 5** — full critical path covered including discovery, dependency chains, and all four required write actions.

---

## FINDINGS SUMMARY

### Non-blocking flags (do not gate AUDIT)

1. **[MINOR] OE2 low-value context lookup** (B2). Contacts search for Tony Reyes is not strictly required — his identity is given in the prompt. Defensible as L9 authority-context anchoring; keep. No fix needed.

2. **[MINOR] Prompt-vs-universe interpretation on Linear issue** (B1 asks 2b). Prompt says "update the Linear issue" implying one exists; OE20 discovers none exists so OE21 creates. The OE handles it correctly, but this is a prompt/universe interpretation gap that S4 (rubric evaluation vs verifier runs) should watch. The rubric writer at S3 should either:
   - phrase Outcome 1.1 as "Agent tracks the Ridgeview roof billing status in Linear (creating a new issue if none exists, or updating the closest related issue)" — accommodating both paths, OR
   - accept that the OE-defined create path is the single valid interpretation.
   Not a B2 BLOCK — flag for S3 attention.

3. **[THIN_DENSITY] B3 midpoint 41** (B3). Above the 40 BLOCKER floor but below the 50 design target. The Hardness Plan's 50 midpoint uses per-lever component sums; a straight min-vs-max midpoint calculation lands at 41. Task is at moderate risk of underflowing 40+ average tool calls on real platform runs. Operator should:
   - accept and continue, OR
   - if S3 rubric writing surfaces natural additional discovery beats (e.g., "Agent verifies ESA request is on file" as an Outcome sub-check), let those pad density organically.
   No BLOCK finding, but note in AUDIT for a strict second look.

### No BLOCK findings.

---

## FINAL VERDICT

**GO** (all sub-checks pass; one THIN_DENSITY flag on B3 does not block per rules).

| Sub-check | Verdict |
|---|---|
| B1 (Forward coverage) | PASS |
| B2 (Reverse coverage) | PASS |
| B3 (Density projection, midpoint 41) | THIN_DENSITY — flag, no block |
| B4 (Hardness levers) | PASS |
| B8 (Rubric forward-map) | PASS |
| B9 (OE Accuracy) | 5 (with universe spot-check deferred to AUDIT) |
| B10 (OE Completeness) | 5 |

**Recommended next step:** AUDIT auto-fire. AUDIT should (a) spot-check 3-5 of the specific record IDs / thread IDs / bill IDs cited in OEs against `3_UniverseDataForThisTask.json`, and (b) apply the strictest possible reading on B3 density — if AUDIT's strict reading lands below 40, this becomes a BLOCKER and returns to S2 for OE expansion.
