# S1.5 Linter Decision — Tasks/41_6a61a86a3453b3714bdc72ef

**Round:** 1 · **Linter class:** A (Misalignment — persona mismatch) · **Linter return value:** FALSE · **Decision:** ACCEPT (linter right) → revise deliverable via persona reassignment.

## Linter finding (persona-consistency check)
The prompt was authored in **Lisa Smith**'s voice (Onsite PM, p_002), but the work described — verifying the QuickBooks balance for the eviction **filing package**, tracking eviction status, confirming **owner authorization** on file, and drafting an **owner-facing email** — falls outside an Onsite PM's turnover/tenant-coordination lane. The linter attributed the eviction/delinquency lifecycle to **Patricia Nguyen** and owner reporting to **Brooke Phillips**, and returned FALSE.

## Re-check verdict: linter substantially RIGHT
Verified every claim against the source of truth (`StarPM_Base_Universe/2_StarPM_PERSONA BRIEFS.md`, `4_StarPM_SCENARIO STORYLINES.md`) and this task's own `Hardness_Plan.md`.

| Linter issue | Verdict | Grounding |
|---|---|---|
| 1. QuickBooks balance verification for the filing package | **VALID** | Rent/eviction ledger + filing packet is Patricia's (`eviction_filing_prep`: Teresa pulls the consolidated QuickBooks rent ledger, Patricia assembles the packet). Lisa touches no QuickBooks. |
| 2. Owner brief + owner-facing email draft | **VALID** | Owner reporting is Brooke's; in `owner_monthly_report_review` Lisa *submits property data to Brooke*. She feeds Brooke, she does not draft owner comms. |
| 3. Eviction status tracking + owner-authorization confirmation | **VALID** | Patricia's anchored territory (`eviction_filing_prep`/`eviction_court_coordination`; obtains Linda Castillo authorization; coordinates with Court Clerk Patricia Lowe). Lisa has zero eviction footprint. |
| 4. Make-ready record update + `#make-ready` channel ping | **INVALID** | These *are* Lisa's lane (Airtable Make-Ready Turns, `#make-ready` C004). The linter conceded this itself. Rendered moot by the fix. |
| 5. Scope of authority (finance + legal + owner + field simultaneously) | **VALID** | Summary of 1–3. |

**Root cause (how this passed S1):** Council A's A6 (persona scope) PASS quoted *"PersonaBrief and Hardness_Plan both state Lisa leads the Tanya Mitchell scenario"* — silently dropping the **"ESA accommodation"** qualifier. Lisa leads exactly one Tanya Mitchell scenario, `fair_housing_reasonable_accommodation`, which `Hardness_Plan.md:84` itself flags as *"legally independent of the rent eviction… must NOT be conflated with the delinquency."* The prompt conflated precisely that. `S1_A_grounding.md` A1/A6 annotated with a supersession pointer to this file.

## Resolution — persona reassignment (not push-back)
Reassigned **p_002 Lisa Smith → p_010 Patricia Nguyen** (chosen over the linter's Brooke suggestion because Brooke is BF2, which would flip the task off its assigned **BF1 Property Operations**; Patricia is also an Onsite PM in BF1 and actually owns the QuickBooks ledger, filing package, eviction lifecycle, and Linda Castillo owner-authorization thread). Low cost — Oracle Events (6) and Rubrics (7) are still empty (pre-S2), so no downstream rework.

**Deliverables changed:** `2_Persona.txt`, `PersonaBrief.txt`, `5_Prompt.txt` (rewritten in Patricia's firm/factual register; stale belief now grounded in the payment plan she herself set up in `rent_delinquency_payment_plan`). All 5 hardness levers (L2 QuickBooks skip / L11 net-vs-gross / L1 latching / L10 supersession / L31 negative-directive) preserved verbatim and now land on the persona who owns the workstream. The 4-write cluster is *more* grounded under Patricia (the eviction Linear ticket is literally her creation in `eviction_court_coordination`).

## Gate re-run (post-reassignment)
- `validate.py --phase prompt` → **PASS · 0 fails / 0 warns / 5 notes** · 397 words · 0 dashes / 0 dollar-figures / 0 internal-IDs.
- Similarity → max composite **28.6** (< 40 ceiling; top match V3 Task14). **Sibling Tasks/40 (Lisa, same Tanya topic) dropped 30.6 → 17.8** composite — reassignment reduced repetition.
- Regression anchors **62/62 PASS**. Data grounding (arrears AP-bill derivation, owner Linda Castillo EVF-2026-014, current SoR recc83c05d889b354) is persona-independent and unchanged.

## Carries to S2
Unchanged from S1: (1) pin canonical eviction-ticket note surface (Linear OPS-32 vs Airtable EVF-2026-014); (2) validator relative-date NOTE prints stale 2026-06-12 default (true today 2026-07-01, prompt date-coherent). No `Linter_Justifications.md` produced — this was an accept/fix, not a push-back.
