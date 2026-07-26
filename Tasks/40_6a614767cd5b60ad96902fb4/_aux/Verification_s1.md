# Verification — S1 — Tasks/40_6a614767cd5b60ad96902fb4

**Universe:** starpm (V4) · **Phase:** s1 · **Today:** 2026-07-01 America/Chicago · **Timestamp:** 2026-07-23

## Sources consulted

| Source category | File / Query | What was verified |
|---|---|---|
| Per-task data | `_aux/Universe_Split/airtable.airtable_records.json` | grounded every prompt claim: Tanya Mitchell tenant; possession-HOLD recc83c05d889b354 (NEWEST, mod 2026-07-01 11:18:57, "cannot begin until possession is formally returned"); owner-approved rec922b9a2d1b9451 (EVF-2026-014); stale plan rec769c9f03f0b85f; breach rec8005502043b755; 3-day rec91517a5acab558; near-miss Rio Bend rec94e86a3007dd5e vs Tanya's Sunset Ridge reca8230a8fd9ff51. |
| Per-task data | `_aux/Universe_Split/{hubspot.hubspot_objects,slack.slack_channels,quickbooks.quickbooks_entities,contacts.contacts}.json` | ESA tickets NEW/OPEN/CLOSED (Tanya) + Gmail "APPROVED" thread; Brooke Phillips supervisor; make-ready channel C004; Tanya QB account surface. |
| Per-task data | `_aux/Fact_Ledger.json` + `_aux/Universe_Index/today_horizon.json` | atom surface; lifecycle.today = null (validator null-fallback prints Brookfield 2026-06-12); authoritative today = 2026-07-01 America/Chicago. |
| Eval spec | `Evals_starpm/1_Prompt_Eval.md` | sub-dims 1.1-1.12 (scored via Council B + strict AUDIT; all PASS/5). |
| QC spec | `Docs_starpm/7_QC_Spec_Doc1.json` + `Docs_starpm/8_QC_Spec_Doc2.md` | all 12 Prompt sub-dims = 5/5 (Council B + AUDIT strict; middle bands not invoked). |
| Reference cards | `Reference/Prompt_Format.md`, `Prompt_Guidelines.md`, `Docs_starpm/4_Prompt_Hard_Tips.md`, `Docs_starpm/6_Prompt_Relative_Time_Updates.md` | voice, anti-patterns, 500-word cap, StarPM relative-date logic re-checked. |
| Prior phase verification | `_aux/Verification_hardness.md` | 5 levers + density projection independently re-verified against Universe_Split (not trusted blind). |

## Eval spec sub-dims (Evals_starpm/1_Prompt_Eval.md) verified
- 1.1 Unique Ground Truth :: PASS (5) — HOLD is the unique end-state; line-3 forecloses the advance reading (AUDIT crux, two hard exclusions).
- 1.2 Feasibility :: PASS (5) — 5 writes map to StarPM tools; Gmail draft-only matches "do not send".
- 1.3 Explicit Tool Mention :: PASS (5) — no tool/MCP/param names; product/business surfaces only.
- 1.4 Prompt Clarity and Specificity :: PASS (5) — lone soft referent ("the ticket") converges on identical write-content.
- 1.5 Contrived / Unnatural :: PASS (5) — natural onsite-PM delegation, not a command list.
- 1.6 Truthfulness :: PASS (5) — hedged belief grounded in rec922b9a2d1b9451 (AUDIT per-atom table).
- 1.7 Tool use and Cross-service :: PASS (5) — 8 services, facts scattered.
- 1.8 Investigation :: PASS (5) — asserts the wrong belief; forces self-discovery + 5 writes.
- 1.9 Coherence :: PASS (5) — one matter (Tanya's Unit 14 turn+account), no bolt-on.
- 1.10 Persona :: PASS (5) — Lisa Smith onsite-PM voice + remit.
- 1.11 Business Function :: PASS (5) — Property Operations, exact match.
- 1.12 Alignment with Today's Date :: PASS (5) — "this week"/"today"/"next week" resolve into 2026-07-01 data windows.

## QC spec sub-dims (Docs_starpm/7_QC_Spec_Doc1.json — Prompt dimension) verified
- All 12 Prompt sub-dims scored 5/5 by Council B and re-scored 5/5 under the strict AUDIT interpretation (1/3/5 middle bands NOT invoked; binary dims all PASS).

## Verification statements
- [x] Validator (validate.py --phase prompt) exit 0 (0 fails / 0 warns / 7 notes).
- [x] verify_universe_atoms.py exit 0 (0 atoms — prompt carries no exact IDs/amounts).
- [x] Regression-anchor suite 62/62 PASS.
- [x] Council A grounding clean (zero ungrounded claims, zero convention drift, A4 accepted).
- [x] Council B QC scoring 12/12 = 5; density Opus ~44 / Gemini ~46 (StarPM >= 40 per model); all 5 levers triggered.
- [x] Similarity gate composite 26.6 < 40 (no pivot).
- [x] AUDIT verdict = PASS (STRICT); density independently re-projected Opus ~40-42 / Gemini ~42-46 (both >= 40).

## Discrepancies surfaced
- Validator date NOTE prints 2026-06-12 (validate.py:464 null-fallback; Fact_Ledger.lifecycle.today is null for StarPM). True today = 2026-07-01; the prompt's relative dates are coherent with it. Cosmetic cross-StarPM validator artifact; not patched during S1 (a validator change needs its own regression pass).
- HOLD record recc83c05d889b354: status field selSched + fldMoveOut 2026-05-02 CONTRADICT its notes (hold until possession returned). Universe quirk, not a prompt defect; strengthens the S1 lever. BINDING carry to S2: OE must derive the hold from the NOTES, never the status/date fields, and must not treat fldMoveOut as possession-returned.
- "the ticket we have open on it" (line 9) is a CROSS-service referent (Airtable EVF-2026-014 + Linear OPS-32/38/54 + HubSpot ESA). BINDING carry to S2/S3: pin to the eviction/turn tracker; rubric goal-phrased, no object lock-in.
- ESA has 3 HubSpot tickets (NEW/OPEN/CLOSED "interactive process completed in full") + Gmail "APPROVED, effective immediately". BINDING carry to S3: phrase as "an approved reasonable-accommodation on record ... before turnover/adverse action", not "an open ESA ticket".

## Verdict

PASS

- The prompt clears validator + atom-verifier + regression anchors + Council A + Council B + similarity + strict AUDIT (PASS STRICT). Zero prompt-phase defects. Four binding carries recorded for S2/S3 (ticket cross-service referent; ESA approved-on-record phrasing; decoy preservation incl. fldMoveOut/selSched notes-not-fields; universe date artifacts).
