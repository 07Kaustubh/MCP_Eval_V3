# AUDIT (Veteran QC) — Prompt Phase — STRICTEST Interpretation

**Task:** 41_6a61a86a3453b3714bdc72ef · **Phase:** prompt · **Universe:** starpm (confirmed via `_aux/Universe.txt` = `starpm`; `_aux/Universe_Index/today_horizon.json` = `2026-07-01`, America/Chicago). Dual-model (Opus 4.8 + Gemini).
**Deliverable:** `Tasks/41_6a61a86a3453b3714bdc72ef/5_Prompt.txt` (399 words, read-only for this audit).
**Prior councils:** A (grounding) GO, B (adversarial) GO. My job: catch what they missed under the strictest possible reading.

## VERDICT: PASS (STRICT)

Zero BLOCKER hits (answer-leakage sweep clean). Zero LENS-1 sub-dims < 5. All 5 selected levers trace to explicit prompt sentences. Per-model density >= 40 (Opus ~49, Gemini ~42). Two non-blocking items surfaced for the OE phase (neither a prompt-phase defect); listed below.

I re-derived every load-bearing atom from `_aux/Universe_Split/` rather than trusting prior phase outputs. All confirmed live.

---

## LENS 8 — Regression-anchor verification: 62/62 PASS
`python3 Validators/test_regression_anchors.py` => 62 passed / 0 failed out of 62 (as supplied this pass). Recorded.

---

## LENS 2 — Answer-leakage sweep (BLOCKER gate) — CLEAN

The derived answer is the net arrears (~$1,832 net / $2,132 stored) and the true eviction state (owner-approved, JP coordination, petition NOT filed). String-searched `5_Prompt.txt`:

| Token searched | Hits | Note |
|---|---|---|
| 2132 / 1832 / 1982 / 8173 / 8173.44 | 0 / 0 / 0 / 0 / 0 | no arrears figure |
| 150 / 847 / 925 / 210 / 1125 / 975 / 187.50 / 5885 / 5885.94 | 0 each | no charge line leaked |
| any digit `[0-9]` in whole prompt | **0** | prompt is numeric-free |
| `$` dollar sign | 0 | |
| 952690 / 232176 / 283231 / QR-2026 / OPS-32 / EVF-2026 | 0 each | no internal IDs |
| Castillo / Harris / Alamo / Sunset / Sunridge / Rimrock / "4B" / JP / "Unit 14" / "14" | 0 each | no entity/owner/unit leak |
| `rec` | 1 | substring inside "record" ("...y record f..."), NOT an ID |
| em-dash `—` / en-dash `–` | 0 / 0 | |

**2+ source synthesis is genuinely forced:** grep of `quickbooks.quickbooks_entities.json` returns **0** occurrences of `1832.0` or `1982.0` anywhere — the net figure is stored nowhere and MUST be derived. The only stored value is `2132.0` (x2: Balance + TotalAmt on the AP bill). The AP bill (`232176553533`/QR-2026-0441) carries `VendorRef` "Alamo HVAC Services" and **no CustomerRef**, so it is invisible to any customer/invoice query — no single tool read reveals the arrears. **No leakage. No BLOCKER.**

---

## LENS 1 — Strict QC scoring (bar = 5 is the ONLY pass)

| Sub-dim | Score | One-line reason | What prior council missed |
|---|---|---|---|
| Unique Ground Truth | **5** | Single end-state per ask: balance = net-of-applied-credit ($1,832; prompt's "clean number... not double-counting any credit that got applied" uniquely selects net over stored $2,132 and over charges-only $1,982); eviction = owner-approved/JP-coordination/NOT-filed; unit = hold. Prompt asks to REPORT whether filed, never to file → no file-vs-defer divergence. | Nothing material. Confirmed the prompt's own disposition directive collapses the 3-way figure ambiguity to one GT. |
| Feasibility | **5** | Every ask actionable against the catalog: QB read/derive, Airtable `update_records_for_table`, Gmail `create_draft` (draft-only), Slack `slack_send_message`, Linear `save_comment`. "draft me an email... so I can look it over before it goes" = draft-only, matches capability. No conflicting instruction. | Verified all four write tools exist in `7_Server_Tools_Details.json` (councils asserted; I confirmed). |
| Explicit Tool Mention | **5** | No function/MCP/param names. "QuickBooks", "make-ready channel", "email", "re-lease" are permitted natural product/channel references. | — |
| Prompt Clarity & Specificity | **5** | Four writes determinate; balance/eviction/unit asks unambiguous; no write-vs-no-write / act-vs-defer. Only open point: which surface = "the eviction ticket" (Linear OPS-32 vs Airtable EVF-2026-014). Note content is byte-identical either way → spec's "channel-of-delivery to the same recipient / identical deliverable" carve-out (Clarity NON-FAIL band + UGT T11 precision guardrail) is a HARD exclusion, so it does not drop below 5. | Council B flagged this MINOR and deferred to OE. I confirm the hard exclusion (identical deliverable) and elevate it to a MANDATORY OE-phase pin (below) so no rubric hard-codes one surface. |
| Contrived / Unnatural | **5** | Natural warm-professional owner-brief message; no step list, no exact timestamps, no format constraints; difficulty is organic (stale memory + scattered/conflicting systems). | — |
| Truthfulness | **5** | Stale beliefs are explicitly HEDGED recollections to verify, not asserted facts; all entities grounded (per-atom table below). | — |
| Tool Use & Cross-service | **5** | Facts scattered across QB + Airtable + Gmail + Slack + Linear + gcalendar + hubspot + contacts; must be reconciled. | — |
| Investigation + Action | **5** | Investigation (balance derivation / eviction state / unit disposition) feeds four writes. "Confirm we have the owner's authorization on file" is a verification ask (truth = yes), NOT pre-solving — owner name/date not leaked. | Confirmed the owner-auth line is not a pre-solve: it names no owner and no date; Harris-vs-Castillo remains a discovery trap. |
| Coherence (Bolt-on) | **5** | Every ask funnels into the single Tanya owner-brief situation; the closing "if anything I've assumed is off, tell me plainly" ties to the hedged beliefs (self-correction), not a bolt-on. | — |
| Persona | **5** | Lisa Smith (Onsite PM, p_002) leads the Tanya scenario and drives make-ready; prepping a property-level owner brief (draft for her review) is in scope; warm-professional voice matches PersonaBrief. | — |
| Business Function | **5** | Tenant delinquency + eviction status + make-ready disposition + owner brief = core Property Operations (BF1). QuickBooks arrears is a sub-task in service of the ops brief, not a Finance reclass. | — |
| Alignment with Today's Date | **5** | Current state (owner approval 06-30, JP filing appt 07-01, SoR mod 07-01 11:18) aligns to universe today 2026-07-01; "today", "a few weeks stale", "last I tracked", "a while ago", "right now" all resolve cleanly; no future-event ask. | Validator NOTE (stale 2026-06-12 default) is a tooling artifact, not a prompt defect — see NOTE below. |
| Universe Data Exists | **5** | Every load-bearing record re-queried and present (AP bill, AR invoice, payment, supersession chain, EVF-2026-014, Linear Harris decoy, Slack #make-ready, Rio Bend near-miss). | — |
| Universe Cross-service Coherence | **5** | Harris-vs-Castillo / hearing-vs-JP / $0-vs-$2,132 are DESIGNED conflicts with a determinable truth (freshest Airtable SoR + semantic note-dates + AP filing-package ledger + Gmail 07-01) — not [Fail - Task Relies on Misaligned Data]. | — |

**All 14 applicable prompt sub-dims = 5. No sub-dim < 5.**

### Truthfulness — per-atom evidence table (required for the 5/5)

| Atom asserted in prompt | Universe query | Row excerpt | Verdict |
|---|---|---|---|
| Tenant "Tanya Mitchell" | contacts + QB CustomerRef | `contacts.contacts.json` tanya.mitchell@gmail.com; QB `283231782926` CustomerRef `proj-2e48c594aab7` "Tanya Mitchell" | TRUE |
| "the owner" (unnamed) | airtable EVF | `rec922b9a2d1b9451`: "Owner authorization received from Linda Castillo" | TRUE (unnamed in prompt; groundable) |
| "back rent had mostly been squared away" (HEDGED) | QB invoice 7214 | `283231782926` DocNumber 7214, **Balance 0.0**, TotalAmt 8173.44 (paid decoy) | TRUE as hedged recollection |
| "checked against what is actually in QuickBooks" | QB company | `quickbooks_company_info.json` present; arrears live in QB (AP bill + AR invoice) | TRUE |
| "for the filing package" | QB AP bill PrivateNote | `232176553533` PrivateNote: "Consolidated rent ledger compiled by Teresa Wood for Tanya Mitchell eviction filing package" | TRUE |
| "we were about at the hearing stage... a while ago" (HEDGED) | Linear OPS-32 + gcalendar | OPS-32 "Eviction Hearing - Mitchell, Harris Property... hearing date has been set"; gcal "Mitchell Eviction Court Hearing" 05-13 | TRUE as hedged recollection (superseded) |
| "confirm we have the owner's authorization on file" | airtable EVF | `rec922b9a2d1b9451` "Owner Approved - Ready to File", CompletionDate 06-30 | TRUE (verification ask; truth = yes) |
| "get her unit back into make-ready... or it has to hold" | airtable SoR | `recc83c05d889b354` "make-ready work on this unit cannot begin until the legal process concludes and possession is formally returned" | TRUE (open framing) |
| "our make-ready record for the unit" | airtable makeready | `recc83c05d889b354` fldUnit "Unit 14", tblMakeReady, last_modified 2026-07-01 | TRUE |
| "the eviction ticket" | airtable/linear | EVF-2026-014 `rec922b9a2d1b9451` (tblMaintenanceTickets) + Linear OPS-32 | TRUE (exists; surface pin = OE item) |
| "our make-ready channel" | slack channels | `slack.slack_channels.json` C004 `#make-ready` | TRUE |
| Author = Lisa Smith (implicit) | PersonaBrief + contacts | p_002 Onsite PM, lisa.smith@starpm.com | TRUE |

No false assertion; every stale belief is hedged. Empty-evidence forcing rule not triggered.

---

## LENS 3 — Hardness end-to-end trace (5 levers → prompt sentence → atom)

| Lever | Surfacing prompt sentence (verbatim) | Atom(s) the agent must touch |
|---|---|---|
| **L2 Structured-DB skip** (flagship) | "I was under the impression the back rent had mostly been squared away, but I am not putting a number in front of the owner that I haven't checked against what is actually in QuickBooks myself. Whatever the real outstanding figure is **for the filing package**, walk it back to the underlying charges" | AR invoice `283231782926` (Balance $0 decoy) → payment `952690463873` → AP bill `232176553533`/QR-2026-0441 (VendorRef Alamo HVAC, no CustomerRef, PrivateNote = the filing-package ledger). Confirmed live. |
| **L10 Reversal / supersession** | "where the eviction really stands **today**... last I tracked it we were about at the hearing stage, and that was a while ago... whether we have **truly filed yet or are still short of that**" | Supersession chain in Airtable → freshest `recc83c05d889b354` (JP coordination, NOT filed) supersedes `rec769c9f03f0b85f` "active payment plan" / `receee45491536859` "awaiting sign-off"; EVF `rec922b9a2d1b9451`. Confirmed. |
| **L1 Latching** | "last I tracked it we were about at the hearing stage" + "**confirm we have the owner's authorization on file** the way we should" | Older Linear OPS-32 "hearing date has been set... at one of Harry Harris's units" (owner mis-attribution) vs true owner Linda Castillo (EVF-2026-014). Confirmed OPS-32 text live. |
| **L11 Net-vs-gross / sign** | "walk it back to the underlying charges so I know it is **the clean number and we are not double-counting any credit or adjustment that got applied** along the way" | AP bill line 4 "Partial payment plan credit applied" Amount **150.0 stored POSITIVE** → net = 847+925+210-150 = 1832 vs stored 2132. Confirmed line-level. |
| **L31 Negative-directive omission** (Gemini differentiator) | "whether we are clear to get her unit back into make-ready and start lining up a re-lease, **or whether it has to hold. I don't want the crew mobilizing on a unit they can't touch yet, or us marketing something we can't actually deliver**" + owner email "covering... whether we can touch the unit yet" | SoR `recc83c05d889b354` prohibition ("make-ready cannot begin until... possession is formally returned") → deliverable must state the explicit NOT-begin / NOT-market directive. Confirmed. |

**All 5 levers surfaced by an explicit sentence. No HARDNESS_REGRESSION. No "implied-without-citation".** (Stacked support L6 near-miss confirmed: Rio Bend Unit 14 `rec94e86a3007dd5e` selReady carries zero Tanya linkage.)

---

## LENS 4 — Strict density projection PER MODEL (StarPM v4 bar: >=40 PASS / 15-39 THIN / <15 INSUFFICIENT)

Trajectory sketched under the reading that MINIMIZES inferred exploration; the four cross-service writes are mandatory and each needs ~2-3 reads for IDs/params.

**Opus 4.8:**
- contacts: Tanya + Linda Castillo (+ court clerk) — 2-3
- quickbooks: customer search (13-entity catch-all) → invoice 7214 → payment → bill search → AP bill QR-2026-0441 → inspect lines → credit-memo near-misses → net derivation — 8-10
- airtable: list Tanya/Unit 14 → supersession chain → EVF-2026-014 → Rio Bend near-miss check → **WRITE** SoR update — 10-12
- gmail: eviction-auth thread (request→Castillo reply) → 07-01 filing thread → accommodation thread (avoid conflation) → **WRITE** owner draft — 7-9
- slack: #general/#make-ready parents + thread replies → **WRITE** #make-ready post — 6-7
- linear: OPS-32/38/54 Harris reads → **WRITE** note — 4-5
- gcalendar: Harris hearing / cure deadline / JP filing 07-01 — 3
- hubspot: ESA tickets (avoid conflation) — 2-3

Opus band ≈ **42-56, midpoint ~49 → PASS**.

**Gemini (~0.85x leaner on lever traversal; Task 40 empirical 33-47):** projected **~36-48, midpoint ~42 → PASS**. Marginal (just above the floor) but the four independent levers (L2 discovery / L11 disposition / L1 anchor / L10 supersession) plus four cross-service writes keep even the leanest run above 40. Flagged marginal, not a blocker.

**Service breadth (~50-call baseline):** airtable ~22%, quickbooks ~18%, gmail ~17%, slack ~13%, linear ~9%, gcalendar ~6%, hubspot ~5%, contacts ~4%. **8 distinct services, 7 at >=5% → breadth PASS.** Max single service ~22% (no dominance). Cross-correlation-heavy, not a single-service deep trap.

---

## LENS 5 — Adversarial veteran review

- **Implicit-prompt framing preserved:** YES. No pre-solving; no "flag the discrepancy" leak. "If anything I've assumed here turns out to be off, tell me plainly" invites self-correction without naming WHAT is wrong (it does not point at the $0 decoy or the Harris over-statement). Clean.
- **Entity-drift seams:** none. Prompt names only "Tanya Mitchell"; unit is only "her unit"/"the unit" (never a bare "Unit 14"); owner is only "the owner".
- **Single-channel lock-in:** goals named (update record / note ticket / post channel / draft email), not tool paths. "Make-ready channel" is a natural channel reference, not a lock-in.
- **"approximately" / "(or similar)" near exact values:** none (prompt has zero numbers).
- **Tool-name / MCP / internal-ID leaks:** none.
- **Em/en dashes:** 0.
- **"at least N" without mandate:** none.
- **Accommodation-vs-eviction conflation risk:** the prompt does NOT mention the ESA accommodation at all — it is scoped to the rent eviction/arrears, so it introduces no conflation seam. The ESA-approved-and-closed status remains a universe near-miss the agent must not conflate, but the prompt neither leaks nor invites it. Correct handling.
- **"Tanya Mitchell" vs Rio Bend Unit 14 near-miss:** strong disambiguator. Re-verified `rec94e86a3007dd5e` = "Rio Bend - Unit 14", selReady, Victor Rios carpet, **zero Tanya linkage** — updating it satisfies none of the Tanya-bound asks. Designed trap, not a valid second reading.
- **Action-vs-prescription:** prompt respects the SoR "cannot begin" prescription ("I don't want the crew mobilizing on a unit they can't touch yet"); no ACTION_DIVERGENCE.

---

## LENS 7 — Anti-Rationalization sweep

Re-scanned my own reasoning for "I considered flagging X but decided it's fine because...":

1. **Eviction-ticket note surface (Linear vs Airtable).** Considered flagging as Clarity/UGT < 5. Promoted-check: does a HARD exclusion apply? YES — the QC spec's Clarity NON-FAIL band ("channel-of-delivery to the same recipient... only... non-action details vary") and the UGT T11 precision guardrail ("if the content of ALL deliverables is identical under both readings → the divergence is immaterial → NOT a UGT fail"). The note content (documenting current JP-coordination/not-filed/hold state) is byte-identical on either surface. Hard exclusion cited → stays 5, but recorded as a MANDATORY OE-phase pin (not a rationalization: it is a real open point routed to the correct phase). 
2. **Gemini density marginal (~42).** Considered flagging THIN. Hard exclusion: midpoint ~42 is >= the StarPM v4 PASS floor of 40; the band's low end (~36) is a tail, not the midpoint the gate scores. Not promoted — cites the explicit numeric bar.

No un-excused matched pattern remains.

---

## Non-blocking items (do NOT block the prompt; route to OE)

- **[LOW / OE-phase pin]** "Leave a short note on the eviction ticket" — surface is open between Linear eviction issue OPS-32 and Airtable EVF-2026-014 `rec922b9a2d1b9451`. Identical deliverable either way. **Fix (OE/rubric, not prompt):** pin the canonical target (Hardness_Plan projects Linear `save_comment` on the eviction issue) AND phrase the outcome rubric broadly ("Agent adds a note documenting the current eviction state — owner-approved, JP-coordination, petition not filed — to the eviction tracking record") so a valid run targeting either surface passes. No prompt change (adding a surface pin would over-specify and reduce naturalness).
- **[NOTE]** `_aux/Validator_Reports/prompt.md` (0 Fails / 0 Warns / 5 Notes) resolves relative "today" against the stale generic default `2026-06-12` per Fact_Ledger.lifecycle, whereas the authoritative per-task universe today is `2026-07-01` (`today_horizon.json`, task brief, V4). The prompt itself is correctly aligned to 07-01 (only solvable under 07-01 — owner approval 06-30 and JP filing 07-01 must be past). **Fix:** correct the validator's V4 date-anchor default; tooling-only, no prompt change, no S1 re-run.

---

## REBUILD check
0 of 5 levers untriggered. Not a REBUILD.

---

```json
{
  "phase": "prompt",
  "council": "AUDIT",
  "task_dir": "Tasks/41_6a61a86a3453b3714bdc72ef",
  "verdict": "PASS_STRICT",
  "universe": "starpm",
  "universe_today": "2026-07-01",
  "blockers": [],
  "leak_sweep": {"figures_hit": 0, "ids_hit": 0, "entities_hit": 0, "digits_in_prompt": 0, "dashes": 0, "net_figure_stored_in_qb": false, "result": "CLEAN"},
  "lens8_regression_anchors": "62/62 PASS",
  "scores": {
    "unique_ground_truth": 5,
    "feasibility": 5,
    "explicit_tool_mention": 5,
    "clarity_specificity": 5,
    "contrived_unnatural": 5,
    "truthfulness": 5,
    "tool_use_cross_service": 5,
    "investigation_action": 5,
    "coherence_bolt_on": 5,
    "persona": 5,
    "business_function": 5,
    "alignment_with_date": 5,
    "universe_data_exists": 5,
    "universe_cross_service_coherence": 5
  },
  "min_subdim_score": 5,
  "density_projection": {
    "opus_midpoint": 49,
    "opus_band": "PASS",
    "gemini_midpoint": 42,
    "gemini_band": "PASS",
    "gemini_note": "marginal, above the >=40 StarPM v4 floor",
    "breadth_services": 8,
    "breadth_services_ge_5pct": 7,
    "breadth_band": "PASS",
    "bar": "StarPM v4 per-model >=40 PASS / 15-39 THIN / <15 INSUFFICIENT (V3 50/40 NOT applied)"
  },
  "lever_preservation": {
    "expected": 5,
    "preserved": 5,
    "missing": [],
    "levers": {
      "L2_structured_db_skip": "TRIGGERED",
      "L10_reversal_supersession": "TRIGGERED",
      "L1_latching": "TRIGGERED",
      "L11_net_vs_gross_sign": "TRIGGERED",
      "L31_negative_directive_omission": "TRIGGERED"
    }
  },
  "non_blocking": [
    {"severity": "LOW", "location": "5_Prompt.txt para5 'Leave a short note on the eviction ticket'", "issue": "eviction-ticket note surface open (Linear OPS-32 vs Airtable EVF-2026-014); identical deliverable, spec-excluded from Clarity/UGT fail", "fix": "OE-phase: pin canonical target + phrase rubric broadly; no prompt change", "propagate_to": null},
    {"severity": "NOTE", "location": "_aux/Validator_Reports/prompt.md relative-date anchor", "issue": "validator resolves 'today' against stale 2026-06-12 (V3 default); authoritative is 2026-07-01; prompt correctly aligned to 07-01", "fix": "tooling-only: correct V4 date-anchor default; no prompt change", "propagate_to": null}
  ],
  "iteration": 0,
  "timestamp": "2026-07-24T12:30:00-05:00"
}
```
