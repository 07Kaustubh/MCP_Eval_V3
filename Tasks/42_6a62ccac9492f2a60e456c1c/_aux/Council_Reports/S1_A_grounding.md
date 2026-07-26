# Council A — Grounding & Convention — S1 Prompt Review

**Task:** `Tasks/42_6a62ccac9492f2a60e456c1c` · **Phase:** prompt · **Universe:** starpm (V4)
**Deliverable:** `5_Prompt.txt` · **Universe today:** 2026-07-01 (America/Chicago)
**Verdict: GO**

## [A1 GROUNDING] — PASS (zero ungrounded claims)
Every concrete claim/named entity resolves to a materialized row in `Universe_Split/`:

| Claim / entity | Resolved to |
|---|---|
| Persona Brooke Phillips (p_000, brooke.phillips@starpm.com) | `contacts.contacts.json` → `c46d47256fd95ca6aca770c8dddda5eb`, Apartment Property Supervisor |
| Owner "Robert Finley" (Property Owner) | `contacts.contacts.json` → `677f79f79e1f5ebcb8d954e2efbda6f3`, robert.finley@gmail.com; also QB customer `proj-e59d4a436ed7` |
| "Pete Donovan" (contact) | `contacts.contacts.json` → `8628aa258df55e62a6d89f64897fce77`, **Exterior Painter** (QB **customer** `proj-f6f9edfeae5c`, not a vendor) — intentional latch |
| "Ridgeview" property + roof section repair | `airtable.airtable_records.json` → `rec8b679d92f30753` "Ridgeview - Roof Section (Common/Structural)"; QB bills below |
| Roof approved/discussed late May 2026 | `gmail.gmail_messages.json` → `4bcbe384bedfd26f` owner approval, internal_date 2026-05-28 (request `832b869d1db1f5e6` same day) |
| "Reserve" account for the owner | `quickbooks.quickbooks_entities.json` → account `64` "Owner Reserve (Trust)" (Bank/TrustAccounts); bill notes name "Ridgeview reserve account" |
| Owner-report tracking issue (Linear) | `linear.linear_issues.json` → **OPS-100** "May Monthly Owner Report - Finley Properties" (state In Progress, `state_OPS_2`) |
| #owner-relations Slack channel | `slack.slack_channels.json` → **C006** `#owner-relations` |
| Vendor payment / AP bill for roof | `quickbooks.quickbooks_entities.json` → bills `528539050604` (Doc 2026-481) + `301715729067` (Doc PD-2026-084), VendorRef Big Bend Restoration `203` |

**Answer-leak check (critical for S1): PASS.** The prompt contains none of the derived-answer tokens — no `8400/8,400`, `16800/16,800`, `Big Bend`, `Donovan Roofing`, doc numbers, "duplicate", or "hold". The three planted facts (vendor-of-record = Big Bend not Donovan; single $8,400 payable not $16,800; explicit reserve/duplicate HOLD) are correctly absent. The prompt names only "Pete Donovan" (the persona's mistaken belief / intended latch), which is allowed per task context.

## [A2 CONVENTION] — PASS
- Word count **320** (cap 500).
- No em-dash/en-dash (grep clean).
- No tool/function names; systems referred to naturally ("the books", "owner relations channel", "our tracker", "my calendar", "email Finley").
- No MCP-server names. No internal IDs / doc numbers / amounts.
- First-person, mid-thought natural voice; one coherent situation (Ridgeview roof CapEx close-out). No bolt-ons.

## [A3 NARRATIVE-STATE CONSISTENCY] — PASS (zero contradictions)
- STATE "Robert Finley gave his approval on the Ridgeview scope" → Gmail `4bcbe384bedfd26f` (finley→brooke, 2026-05-28 19:20 UTC): "You have my approval to proceed with the $8,400 roof section repair at Ridgeview." **GRANTED**, not pending/denied. ✓
- STATE "Pete Donovan's crew is confirmed" → Slack `a33ed…`/`7d94b…`, Airtable `rec8b679d92f30753` note, and Brooke→Pete email `0427cad50efd8219`. Grounded on the conversational surface (persona's belief/latch; the trap is vendor-of-record, not the confirmation itself). ✓
- STATE "I already posted that we were good to move" → Slack `a33ed9993702515c80b0be775da32e59` ("Roof repair at Ridgeview is approved…") and `7d94bdcbe1c75707baca974be1d83b0c` ("We're good to go."), both by Brooke (`U9741B657FE`) in C001, 2026-05-28. ✓
- STATE "sitting since late May" → owner approval 2026-05-28; bills TxnDate 2026-05-01 — both past relative to today 2026-07-01. ✓
- Observation (non-blocking, by design): Brooke's two Slack "approved/good to go" posts (19:15/19:16 UTC) predate the owner's written approval (19:20 UTC) by ~4 min. This is the planted L31 premature-approval defect for the agent to discover; it does not contradict the prompt's own claims. No BLOCK.

## [A4 ACTION-VS-UNIVERSE-PRESCRIPTION] — CONSISTENT; no authority gap
- Universe control: both roof bill PrivateNotes prescribe a pre-release control — "Teresa Wood to confirm reserve balance covers disbursement before payment is released" (`528539050604`) and "Confirm payment from Ridgeview reserve account before releasing funds" (`301715729067`). The prompt reinforces (not contradicts) this: "done by the book… bring it back to me first… do not just push it through." **CONSISTENT — accept.** No ACTION_DIVERGENCE.
- AUTHORITY: Brooke Phillips owns vendor-invoice approval, budget oversight, owner reporting, and the owner CapEx-approval flow, and routinely posts to `#vendors`/`#owner-relations`/`#budget-review`. She is authorized for every requested write. **No AUTHORITY_GAP.**

## [A7 CLARITY & SPECIFICITY] — PASS (no MAJOR gap)
Intended reading well-supported: investigate the true payable, hold if not clean, execute the write set (queue-but-do-not-release vendor payment; email Finley closing the pass-through; post to #owner-relations; comment on owner-report issue; set calendar reminder). Minor secondary reading (does "bring it back to me first" mean do zero writes and stop?) is resolved by paragraph 3, which enumerates the write set and gates only the release of funds. The two readings do not diverge into different write-action *sets*. **MINOR clarity note only — not MAJOR, no BLOCK.**

## [A10 BUSINESS FUNCTION] — match = true
Owner CapEx roof pass-through + vendor-payment coordination + owner reporting sits squarely in BF#2 "Portfolio Coordination & Owner Relations" — Brooke's signature scenario `owner_capex_approval_roof`.

## [A11 END-TO-END SOLVABILITY] — PASS (no solvability break)
Every link in the Hardness_Plan chain is materialized:
- Finley contact ✓ · Roof in Airtable ✓ `rec8b679d92f30753` · QB AP bills ✓ `528539050604` + `301715729067`
- Big Bend vendor of record ✓ vendor `203` (no "Donovan Roofing" vendor exists; "Pete Donovan Roofing" appears only as a decoy line-item description inside AR invoice `109367557444`)
- Duplicate bill ✓ two $8,400 bills, same TxnDate 2026-05-01, both Balance 8400, no LinkedTxn/payment
- Owner AR pass-through invoice ✓ `109367557444` (Doc 2026-494, CustomerRef Finley, note ties to 2026-481 only)
- Reserve/hold note ✓ (both bill PrivateNotes + account `64`) · #owner-relations ✓ C006 · owner-report Linear issue ✓ OPS-100

## Perspective roll-up
A1 pass · A2 pass · A3 pass · A4 consistent/authorized · A7 pass (minor note) · A10 true · A11 pass.

```json
{"phase":"prompt","council":"A","task_dir":"Tasks/42_6a62ccac9492f2a60e456c1c","verdict":"GO","perspectives":{"A1_grounding":"PASS","A2_convention":"PASS","A3_narrative_state":"PASS","A4_action_vs_prescription":"CONSISTENT","A4_authority":"NO_GAP","A7_clarity":"PASS_minor_note","A10_business_function":"true","A11_solvability":"PASS","answer_leak":"PASS_no_derived_facts_leaked"},"timestamp":"2026-07-25"}
```
