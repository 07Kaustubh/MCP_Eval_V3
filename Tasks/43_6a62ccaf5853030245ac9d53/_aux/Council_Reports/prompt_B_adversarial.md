# Council B — Adversarial QC + Density + Hardness Preservation

**Phase:** prompt · **Universe:** starpm · **Task:** `Tasks/43_6a62ccaf5853030245ac9d53`
**Deliverable:** `5_Prompt.txt` · **Iteration:** 1 · **Date:** 2026-07-25
**Universe today:** 2026-07-01 (America/Chicago) — the "Jun 12" string in `7_QC_Spec_Doc1.json` is SUPERSEDED per task instructions + `today_horizon.json`.

Verdict computed as the **union of five role lenses** (Architect, Implementer, Red-team, Ground-truth, Integration), each a full re-read of the prompt.

---

## Grounding sweep (Ground-truth lens — per-task Universe_Split, re-queried)

| Claim / atom | Status | Evidence |
|---|---|---|
| Persona Carlos Mendez, Onsite PM, `carlos.mendez@starpm.com`, `p_009` | ✅ | `entities_personas.md`; PersonaBrief anchors Mesa Vista make-ready (flagship) |
| Business Function = Property Operations (BF1) | ✅ | `1_Business_Function.txt`; make-ready close-out is flagship Property Ops |
| Mesa Vista 4C exists; Linda Castillo = Property Owner | ✅ | Airtable `tblMakeReady` 4C rows; `entities_personas.md` Linda Castillo (npc, Property Owner) |
| AR invoice 2026-534 (`445653930748`), **CustomerRef = Linda Castillo**, Balance **$1,622** | ✅ | qb_entities: lines $387 / $1,140 / $95; DocNumber 2026-534; customer `proj-4ae920b7c9e8` |
| AP deep clean $387 — Sunshine, `195089456477`, Doc 2026-SC-4C | ✅ | qb_entities bill; matches AR line |
| AP repaint **$1,340** — Permian, `696089964235`, Doc PD-2026-09 | ✅ | qb_entities bill; AR shows $1,140 → **understated $200** |
| AP closet trim **$85** — Permian, `546359391323`, Doc 2026-519, acct "Owner Reserve (Trust)", "Pass-through to owner" | ✅ | qb_entities bill; AR shows $95 → **overstated $10** |
| Over-inclusion decoy $85 — Alamo HVAC, `991582431419`, "Internal labor charge for **Carlos Mendez's make-ready walk**" | ✅ | qb_entities bill; NOT on AR; excluded → adding = $1,897 |
| 10 distinct bills at exactly $1,340 across 6 vendors | ✅ | Confirmed 10 (`696089964235` = the only 4C repaint) |
| Belief email `5101c5a41dffa90a` from Carlos → Linda, "Mesa Vista 4C Make-Ready Complete. Cost Summary…" | ✅ | gmail: from `carlos.mendez@starpm.com`, to `linda.castillo@gmail.com` |
| Slack channel for "crew and front office" post | ✅ | `#make-ready` (C004), `#owner-relations` (C006), `#vendors` (C005) all exist |
| Correct total $1,812 = 387+1340+85; **never appears verbatim** in prompt | ✅ | Prompt contains **zero** dollar figures ($1,812/$1,727/$1,897/$1,622/$1,140/"$" all absent) |
| Pete Donovan owner decoy (Pete is Exterior Painter npc + a QB customer `proj-f6f9edfeae5c`) | ✅ decoy present | AR customer is Linda, not Pete → prompt keeping owner=Linda is correct |

**Ground-truth verdict: PASS** — every concrete atom resolves; the prompt itself carries no ungrounded tight identifier (it names only "Mesa Vista 4C", "Linda Castillo", "Carlos"; no IDs, amounts, channel/vendor names).

---

## [B1] QC sub-dimension scoring (scheme per Council_Protocol map)

SUB-DIM Unique Ground Truth -> SCORE 5/5 (1/3/5) -> REASON single derived end-state (correct existing AR 2026-534 to $1,812 = 387+1340+85; Airtable 4C closed w/ that cost; draft email Linda; Slack post); every alt end-state ($1,622 / $1,727 / $1,897 / new invoice / Pete) is foreclosed by prompt language, not a valid reading.
SUB-DIM Feasibility -> SCORE 5/5 (1/3/5) -> REASON all 4 writes tool-supported (QB invoice update, Airtable update, Gmail draft [StarPM gmail is draft-only — "email Linda" resolves to a draft], Slack post); every needed datum exists & is retrievable.
SUB-DIM Explicit Tool Mention -> SCORE 5/5 (1/5 binary) -> REASON "get our 4C make-ready record in Airtable updated" is a natural system-of-record reference (like "check my emails"), not a tool function name nor "use the Airtable tool/MCP server"; QuickBooks/Slack/Gmail are never named.
SUB-DIM Prompt Clarity & Specificity -> SCORE 5/5 (1/3/5) -> REASON asks are explicit and ordered by intent (reconcile → correct the EXISTING invoice, "I do not want a second bill created" → update Airtable 4C → email Linda → post channel); only channel-of-delivery ("our channel") and which-4C-row vary, both converging non-action/discovery details (non-fail band at worst).
SUB-DIM Contrived / Unnatural -> SCORE 5/5 (1/3/5) -> REASON natural first-person Carlos voice; no command list ("first…then…"), no arbitrary format/timestamp constraints; difficulty is organic reconciliation.
SUB-DIM Alignment with Today's Date -> SCORE 5/5 (1/3/5) -> REASON today 2026-07-01; spring billing (May), move-out 2026-06-01, target-ready 2026-06-14 all past; closing out the completed turn now is coherent, no future-facing ask.
SUB-DIM Truthfulness -> SCORE 5/5 (1/3/5) -> REASON every claim grounded (4C, Linda=owner, billed-in-spring via AR 2026-534, summary email exists, the three named line items match the AR); prompt states no figure → no numeric error possible.
SUB-DIM Tool Use & Cross-service -> SCORE 5/5 (1/5 binary) -> REASON requires QuickBooks (AP bills + AR) + Airtable (4C record) + Gmail (belief email + draft) + Slack + Contacts; the answer is scattered and must be reconciled across 5 services.
SUB-DIM Investigation + Action -> SCORE 5/5 (1/5 binary) -> REASON deep investigation (derive $1,812 from AP bills the AR never states) feeds 4 write actions; not pre-solved — no figure/root cause disclosed.
SUB-DIM Coherence / Bolt-on -> SCORE 5/5 (1/5 binary) -> REASON all asks flow from one situation (close out 4C owner pass-through); the validator-flagged "Correct the invoice she is holding…" sentence is a heuristic FALSE POSITIVE (see B-bolt-on analysis).
SUB-DIM Persona -> SCORE 5/5 (1/3/5) -> REASON Carlos Mendez, Onsite PM, leads the Mesa Vista 4C make-ready (his signature scenario); steady/structured voice matches.
SUB-DIM Business Function -> SCORE 5/5 (3/5) -> REASON Property Operations — make-ready turn close-out + updating the make-ready record is squarely the flagship Property Ops category.
SUB-DIM Universe Data Exists -> SCORE 5/5 (1/5 binary) -> REASON all bills/invoice/records/email/channels verified present and tool-retrievable.
SUB-DIM Universe Cross-service Coherence -> SCORE 5/5 (1/5 binary) -> REASON coherent; the closet-bill "internal labor (Tony Reyes)" phrase vs external Permian VendorRef is well-corroborated as owner-billable (external vendor + acct "Owner Reserve (Trust)" + "Pass-through to owner" + already on AR) → the supported reading, not a [Fail-Misaligned Data]. Watch-item for OE/rubric grounding (below).

**B1 verdict: all applicable sub-dims = 5. PASS.**

### Bolt-on WARN adjudication (validator heuristic flag on "Correct the invoice she is holding…")
- **Remove-sentence test:** deleting "Correct the invoice she is holding so it carries the right figure, and get our 4C make-ready record in Airtable updated…" **destroys** the prompt's core corrective action and orphans the two downstream asks that reference "the corrected number" ("email Linda so she is not sitting on a summary that no longer matches"; "post… so whoever else… is working off the corrected number"). The rest does NOT still make sense → **FAILS the remove test → NOT a bolt-on.**
- **Shared-situation/entities test:** the sentence shares every core entity (the invoice, Linda, 4C, the corrected figure) with the surrounding prompt.
- **Conclusion:** heuristic false positive. Coherence = 5.

---

## [B2] Adversarial alt-path + second-reading attack

### (a) Divergent-end-state paths — each classified
| Alt path | Different end-state? | Prompt AMBIGUITY (fault) or MODEL ERROR (trapped)? | Why |
|---|---|---|---|
| Log 4C closed at **$1,622** without opening AP bills | yes | **MODEL ERROR (trapped, flagship L2)** | Prompt: "every dollar on her bill has to line up with what we actually paid out… Go back to what each vendor charged us." Trusting the AR/email is explicitly disallowed. |
| **Create a NEW** owner invoice | yes | **MODEL ERROR (trapped, L9)** | Prompt: "I do not want a second bill created next to the one she already has. Correct the invoice she is holding." |
| Include the internal **$85 Alamo** inspection → **$1,897** | yes | **MODEL ERROR (trapped, L11)** | Prompt: "an internal walk or a condition check we handled in house, stays off her bill entirely" — maps precisely to Alamo ("Unit condition inspection…make-ready walk"). |
| Drop the closet **$85** as "internal" → **$1,727** | yes | **MODEL ERROR (trapped, L11)** | Closet is external-vendor repair (Permian), already an AR line, acct "Owner Reserve (Trust)", "pass-through to owner"; prompt says "line up… no more no less" against her existing bill. The lone "internal labor (Tony)" PrivateNote phrase is out-corroborated. |
| Bill/email **Pete Donovan** instead of Linda | yes | **MODEL ERROR (trapped, L6)** | Prompt names Linda as owner; AR CustomerRef IS Linda; "Correct the invoice she is holding" + "email Linda." Pete is a painter/decoy. |
| Grab the wrong **$1,340** bill from the 10-bill cluster | yes | **MODEL ERROR (trapped, L4/L6)** | Only `696089964235` (PD-2026-09, Permian) is the 4C repaint; the prompt's per-line reconciliation forces disambiguation. |

**The $1,622 reading is foreclosed as "valid"** because the prompt frames the 4C costs as a pass-through that "has to line up with what we actually paid out on that unit, to the dollar" and orders the agent to "go back to what each vendor charged us." A reading that stops at the AR/email is a comprehension failure the prompt is engineered to catch — not a defensible second interpretation. **Confirmed.**

### (b) Second-reading — does any rereading flip a WRITE action (recipient / create-vs-correct / act-vs-defer)?
- **Recipient:** unambiguous — Linda (named + AR customer). No flip.
- **Create-vs-correct:** unambiguous — "Correct the invoice she is holding… I do not want a second bill created." No flip.
- **Act-vs-defer:** unambiguous — "I would sooner square this myself now." Act. No flip.
- **Two soft/converging discovery choices** (NOT write-action flips): (i) *which Slack channel* — "our channel for the crew and front office" → `#make-ready`/`#owner-relations`; channel-of-delivery to the same audience is explicitly non-fail band. (ii) *which 4C Airtable row* — a stale `selProg` row (`recbd087a4abd605b`) vs the live `selReady` row (`recc8534b3fd13954`); this is the intended L1 latching near-miss, and the end-state (4C make-ready reflects $1,812 + closed) converges regardless. Neither changes the recipient, the create-vs-correct decision, or act-vs-defer.

**B2 verdict: no adversarial divergence that is a genuine prompt fault. PASS.** (Watch-item: OE/rubric should pin the exact 4C row and channel so grading is deterministic; a prompt-phase non-issue.)

---

## [B3] Tool-call density projection — PER MODEL (StarPM per-model gate)

Independent Opus 4.8 trajectory sketch:

| Segment | Calls |
|---|---|
| Contacts: resolve Linda Castillo email | 1 |
| Airtable: list/search 4C make-ready + get row(s) (latching disambiguation) | 3–4 |
| QuickBooks: find/read AR invoice 2026-534 | 2–3 |
| QuickBooks: search AP bills + read deep-clean/repaint/closet/Alamo + **disambiguate the 10-bill $1,340 cluster** | 8–12 |
| Gmail: read belief email `5101c5a41dffa90a` | 1–2 |
| Slack: context read (#make-ready) | 1–2 |
| **Writes (4):** correct AR invoice (+read-back) · update Airtable 4C · draft email Linda · Slack post | 4–6 |
| Post-write verification reads | 2–4 |
| **Total (Opus)** | **~34–50, midpoint ~43** |

| Model | Range | Midpoint | Band |
|---|---|---:|---|
| **Opus 4.8** | ~34–50 | **~43** | **PASS (≥ 40)** |
| **Gemini** (empirical −9.5) | ~26–41 | **~34** | **THIN (15–39)** |

- Cross-check vs Hardness_Plan: Opus 43.5 PASS / Gemini ~34 THIN — **matches my independent sketch.**
- **Scope reality check:** the prompt genuinely asks for **4 writes** (QB AR correction, Airtable 4C, Gmail draft, Slack post) across **5 services** exercised (QuickBooks, Airtable, Gmail, Slack, Contacts; Linear optional 6th). Density is **real, not inflated** — the 10-bill $1,340 cluster forces genuine disambiguation reads on both models.
- **Gemini THIN is pre-accepted:** Hardness_Plan documents a `## THIN density acceptance` section (Gemini ~34, above the 15 floor). Neither model is INSUFFICIENT (<15).

**B3 verdict: Opus PASS, Gemini THIN (documented-acceptance). Not INSUFFICIENT on either model → does NOT block.**

---

## [B4] Hardness preservation (4 selected levers)

| Lever | Surfaced by the prompt? | Evidence in prompt |
|---|---|---|
| **L2 — Structured-DB skip (flagship)** | ✅ preserved | "every dollar on her bill has to line up with what we actually paid out… Go back to what each vendor charged us for the 4C work and set it against the line items I sent her." Forces the AP bills (where $1,340/$85 live), not the visible AR/email. (Per empirical note: the trap survives even though the prompt points at "what each vendor charged us"; it doesn't even name QuickBooks.) |
| **L10 — Reversal / supersession** | ✅ preserved | "that summary is the record she keeps… be sure what she was actually charged holds up… so she is not sitting on a summary that no longer matches." Establishes the stale AR summary as the thing to supersede. |
| **L6 — Near-miss entity** | ✅ preserved | Per-line reconciliation drives the agent into the 10-bill $1,340 cluster ($1,140 vs $1,340), the $95-vs-$85 closet, the twin-$85 (Permian closet vs Alamo inspection), and the Linda/Pete owner decoy. |
| **L11 — Net-vs-gross** | ✅ preserved | "Only outside vendor work belongs on her side. Anything that was our own time on the unit, an internal walk or a condition check we handled in house, stays off her bill entirely." Keeps the $1,897 (include Alamo) and $1,727 (drop closet) decoys live as traps. |

**Levers preserved: 4 / 4. No HARDNESS_REGRESSION.**

---

## [B6] Upstream propagation

**No BLOCKING propagate flags.** The Hardness_Plan is internally coherent, the levers are data-supported, the THIN Gemini density is documented-accepted, and $1,812 never appears verbatim (verified). 

One **NOTE (non-blocking, downstream guidance — not a B6 root-cause-upstream defect):** the closet bill `546359391323` PrivateNote reads "Internal labor charge for Tony Reyes touch-up" while the same record is an **external Permian VendorRef**, acct **"Owner Reserve (Trust)"**, **"Pass-through to owner"**, and is already a line on AR 2026-534. This tension is intentional L6/L11 trap bait (Hardness_Plan explicitly calls it "twin $85 charges… one billable one internal"). The owner-billable reading is well-corroborated, so it is NOT a [Fail-Misaligned Data]. **Recommendation for S2/S3:** ground the closet=include / Alamo=exclude rationale explicitly (external-vendor pass-through + on-AR + Owner-Reserve acct vs "internal make-ready walk") so the $1,727 path grades as a genuine model failure and not a rubric artifact. This is prompt-phase clean; carry it forward as a watch-item only.

---

## Five-lens union

- **Architect:** structure fits V4 (implicit Carlos-voice close-out; 4-write/5-service scope). PASS.
- **Implementer:** all targets resolvable (invoice 2026-534, 4C rows, Linda's email, real channels); gmail draft-only constraint respected. PASS.
- **Red-team:** every adversarial path is a trapped model error, not a valid reading; no write-action flip. PASS.
- **Ground-truth:** every atom resolves in Universe_Split; prompt states no ungrounded identifier. PASS.
- **Integration:** all 4 levers preserved end-to-end; density real; one downstream watch-item (closet grounding) flagged, non-blocking. PASS.

**Union verdict: GO.**

```json
{"phase":"prompt","council":"B","task_dir":"Tasks/43_6a62ccaf5853030245ac9d53","verdict":"GO","scores":{"unique_ground_truth":{"score":5,"scheme":"1/3/5","reason":"single derived end-state; $1,622/$1,727/$1,897/new-invoice/Pete all foreclosed by prompt language"},"feasibility":{"score":5,"scheme":"1/3/5","reason":"4 writes tool-supported (gmail draft-only ok); all data retrievable"},"explicit_tool_mention":{"score":5,"scheme":"1/5","reason":"'in Airtable' is natural system-of-record reference, not a tool name or 'use the X tool'"},"clarity_specificity":{"score":5,"scheme":"1/3/5","reason":"correct existing invoice (not new); only converging channel/row discovery details vary"},"contrived_unnatural":{"score":5,"scheme":"1/3/5","reason":"natural Carlos voice; no command list or arbitrary constraints"},"alignment_today":{"score":5,"scheme":"1/3/5","reason":"today 2026-07-01; spring/June events past; close-out coherent"},"truthfulness":{"score":5,"scheme":"1/3/5","reason":"all claims grounded; no figures stated so no numeric error"},"tool_use_cross_service":{"score":5,"scheme":"1/5","reason":"QB+Airtable+Gmail+Slack+Contacts reconciliation"},"investigation_action":{"score":5,"scheme":"1/5","reason":"derive $1,812 from AP bills feeds 4 writes; not pre-solved"},"coherence_bolton":{"score":5,"scheme":"1/5","reason":"flagged sentence fails remove-test and shares entities -> heuristic false positive"},"persona":{"score":5,"scheme":"1/3/5","reason":"Carlos Mendez leads Mesa Vista 4C make-ready; voice matches"},"business_function":{"score":5,"scheme":"3/5","reason":"Property Operations make-ready close-out (flagship)"},"universe_data_exists":{"score":5,"scheme":"1/5","reason":"all bills/invoice/records/email/channels verified retrievable"},"universe_cross_service_coherence":{"score":5,"scheme":"1/5","reason":"closet 'internal' note out-corroborated by external vendor+trust acct+on-AR+pass-through; not misaligned-data"}},"density_projection":{"midpoint":43,"band":"PASS","gemini_midpoint":34,"gemini_band":"THIN","breadth_services":5,"breadth_band":"PASS"},"lever_preservation":{"expected":4,"preserved":4,"missing":[]},"bucket_1_risk_pct":null,"iteration":1,"timestamp":"2026-07-25"}
```
