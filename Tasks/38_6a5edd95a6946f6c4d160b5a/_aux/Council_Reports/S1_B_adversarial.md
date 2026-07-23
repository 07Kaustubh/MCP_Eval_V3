# Council B — Adversarial (S1 prompt, iter-2 after F1 BLOCKER retarget)

**Deliverable:** `Tasks/38_6a5edd95a6946f6c4d160b5a/5_Prompt.txt` (iter-2)
**Phase:** S1.5 iter-2 (post Council-A F1 BLOCKER fix: Item 2 write retargeted Linear → Airtable maintenance record)
**Universe:** starpm (confirmed via `_aux/Universe.txt`)
**Overwrites:** iter-1 report (which passed 5/5 all sub-dims but was invalidated by A's F1 finding).

---

## 1. Delta-focused re-scoring

### 1a. Feasibility (Item 2 write retarget)

- Iter-1: Item 2 asked for Linear issue update on Ridgeview roof — Council A found no such Linear issue exists in the universe. F1 BLOCKER.
- Iter-2: Item 2 asks for maintenance record update on Ridgeview roof.
- Target verification: Hardness Plan L8 chain confirms `Airtable tblMakeReady` row `Ridgeview - Roof Section` exists as the entry point to the 5-hop reconciliation. Row is queryable via the Airtable read tools and updateable via `airtable_update_records(baseId, tableId, records[])` per StarPM tool catalog (parameters per StarPM parameter-trap doc: camelCase `baseId`/`tableId`/`records[]`).
- Every hop in the chain (Airtable MR row → MT-2026-047 → QB bills 2026-481 + PD-2026-084 → QB invoice 2026-494 → payment 972286822645) is universe-grounded per Hardness Plan L8, so the "current status" the agent will write is derivable from real data.
- **Verdict: 5/5.** The target write record exists, is retrievable, and is updateable. No feasibility gap.

### 1b. Coherence (both Items now say "update the maintenance record")

Concern: Item 1 line 3 ends "update the maintenance record with it, and drop a note in #maintenance"; Item 2 line 5 now ends "update the maintenance record on it with the current status once you have it." Is there referential ambiguity between "the maintenance record" in the two items?

- Item 1 anaphoric anchor: paragraph 2 opens "The Sunset Ridge 208B AC is where I'm most uncomfortable" — establishes the Sunset Ridge 208B AC as the subject. Every "the maintenance record" / "it" in that paragraph unambiguously refers to Sunset Ridge 208B AC.
- Item 2 anaphoric anchor: paragraph 3 opens "The Ridgeview roof billing is the other one nagging at me" — establishes Ridgeview roof as the subject. "the maintenance record on it" resolves cleanly: "it" = the Ridgeview roof job, "the maintenance record on it" = the maintenance record associated with that job.
- Paragraphs are separated by a blank line and by a fresh topic sentence. No cross-paragraph pronoun leakage.
- Remove-sentence test: cutting either "update the maintenance record" clause leaves the paragraph without its write action and destroys the item's ask — confirms the clauses are load-bearing, not bolt-ons or duplicates.
- **Verdict: 5/5.** The two "update the maintenance record" phrases refer to two distinct records anchored by two distinct paragraph subjects. No ambiguity confusion.

### 1c. Persona (Brooke updating an Airtable maintenance record)

- Brooke's canonical scope per PersonaBrief line 14: "QuickBooks (invoice approval, budget), Gmail (owner and vendor threads), Slack `#vendors`, `#owner-relations`, `#budget-review`, `#general`, Google Calendar (owner meetings, ops sync), **Airtable (portfolio rollups)**."
- Airtable is explicitly named as a system Brooke touches. Updating a maintenance record on Airtable to log current status before rolling into an owner brief is a natural supervisor coordination action — it is the "portfolio rollups" activity in operation.
- Her signature scenario `owner_capex_approval_roof` (8 actions, leads) puts the Ridgeview roof capex flow squarely inside her scope. Updating the associated maintenance record on that same job is the operational side of her signature flow.
- The iter-1 residual wart on `#maintenance` channel canonicality is unchanged — still noted, still not a fail (per iter-1 §3 analysis: PersonaBrief "systems she touches most" is a frequency list, not a whitelist).
- **Verdict: 5/5.** Retarget from Linear to Airtable actually improves persona canonicality (Airtable is on her list, Linear is not).

---

## 2. Multi-write diversification check (Hardness Plan L7 baseline)

Hardness Plan L7 baseline: 3 writes across 3 services (originally Slack + Linear + Gmail).

Iter-2 write shape from the prompt body:
| # | Write action | Service | Prompt anchor |
|---|---|---|---|
| 1 | Update Sunset Ridge 208B AC maintenance record | Airtable | line 3 "update the maintenance record with it" |
| 2 | Drop a note in `#maintenance` | Slack | line 3 "drop a note in #maintenance" |
| 3 | Update Ridgeview roof maintenance record | Airtable | line 5 "update the maintenance record on it" |
| 4 | Draft Gmail to Aurora | Gmail | line 9 "draft a Gmail to Aurora" |

- Distinct write services: **3** (Airtable, Slack, Gmail) → meets L7 baseline of 3.
- Total writes: **4** (baseline was 3) → exceeds baseline. Extra Airtable write is the retargeted Item 2 write, no downside.
- Airtable appears twice but writes are on two distinct records (Sunset Ridge 208B vs Ridgeview roof) — this is not single-record thrash, it is two independent record updates in the same service.
- Linear write is gone but Linear read remains available for density buffer (contact resolution, cross-service triangulation).
- **Verdict: MEETS baseline.** Density projection remains defensible at 50.0 midpoint (Airtable writes cost ~3 supporting reads each just like Linear writes did in the baseline projection; the density math is invariant to Linear-vs-Airtable substitution).

---

## 3. Full 14-sub-dim scorecard (moves from iter-1)

| # | Sub-Dim | Scheme | Iter-1 | Iter-2 | Delta reason |
|---|---|---|---|---|---|
| 1 | Unique Ground Truth | 1/5 binary | 5 | **5** | End-states unchanged — Item 2 write target changed but the "current status" data (5-hop QB reconciliation result: $8,400 net, $640 partial, balance outstanding) is unchanged; the write lands somewhere else but carries the same payload. |
| 2 | Feasibility | 1/3/5 | 5 | **5** | See §1a. Airtable MR row exists and is updateable. Previously the Linear issue did NOT exist — iter-2 fix closes the gap. |
| 3 | Explicit Tool Mention | 1/5 binary | 5 | **5** | No MCP tool names. "Airtable" is not mentioned in the prompt body (Item 2 says "the maintenance record on it" — service-neutral). Prompt now names fewer platforms than iter-1 (Linear reference removed). |
| 4 | Prompt Clarity & Specificity | 1/3/5 | 5 | **5** | See §1b anaphoric resolution. No new interpretation ambiguity introduced. Write-action divergence hard gate: agent's writes are Airtable (twice) + Slack + Gmail regardless of reading. |
| 5 | Contrived / Unnatural | 1/3/5 | 5 | **5** | Reads as a supervisor's before-EOD ask. No artifact of the retarget shows in prose. |
| 6 | Truthfulness | 1/3/5 | 5 | **5** | Named atoms unchanged (Aurora, Tony, Robert, Tanya Mitchell, Sunset Ridge 208B, Ridgeview, `#maintenance`, `$8,400`). All still Fact_Ledger-grounded per Hardness Plan. Removal of the phantom Linear reference actually improves truthfulness — one fewer tight identifier at risk. |
| 7 | Tool Use & Cross-service | 1/5 binary | 5 | **5** | Airtable + QuickBooks + Slack + Gmail + Contacts across 5 services (was 6 with Linear read); still far above 2+ floor. |
| 8 | Investigation | 1/5 binary | 5 | **5** | Root causes still hidden. L9 authority-dismissal, L11+L2 pass-through, L6 record-freshness all unchanged. |
| 9 | Coherence (Bolt-on) | 1/5 binary | 5 | **5** | Three items still woven under "Aurora wants an operations update before I leave." Validator's 2 remaining WARNs are same-family false positives (see §5). |
| 10 | Persona | 1/3/5 | 5 | **5** | See §1c. Airtable retarget improves persona canonicality vs Linear (Airtable is on Brooke's canonical systems list, Linear is not). |
| 11 | Business Function | 3/5 no fail band | 5 | **5** | BF-2 Portfolio Coord & Owner Relations unchanged. |
| 12 | Alignment with Today's Date | 1/3/5 | 5 | **5** | Universe today = 2026-07-01 unchanged. All resolved windows still carry data. |
| 13 | Universe Data Exists | 1/5 binary | 5 | **5** | Every downstream lookup materialized. Retargeted Airtable MR row confirmed present per L8 chain. |
| 14 | Cross-service Coherence | 1/5 binary | 5 | **5** | L9 Slack/Gmail contradiction intentional. Universe internally coherent. |

**No moves. All 14 sub-dims remain at 5/5.** The iter-2 retarget affects Feasibility positively (was a latent phantom risk on the Linear side) and everything else invariantly.

---

## 4. Anti-pattern sweep

| Pattern | Iter-2 status | Evidence |
|---|---|---|
| Em-dashes (`—`) | **CLEAN** | Zero em-dashes in 5_Prompt.txt. Only ASCII hyphens ("back-and-forth"). |
| En-dashes (`–`) | **CLEAN** | Zero. |
| "at least N" | **CLEAN** | Not present. |
| MCP tool names | **CLEAN** | Zero tool-call identifiers. Product-name mentions (Slack, Gmail) natural. Linear no longer mentioned at all — even the platform-name reference is gone. |
| Internal IDs | **CLEAN** | No `MT-...`, no `rec...`, no QB bill numbers, no invoice IDs, no Airtable base/table IDs in prompt body. |
| Command list | **CLEAN** | No "First X, then Y, finally Z" prescription. Paragraph-per-item structure. |
| Bolt-on | **CLEAN** | Two validator WARNs remaining are heuristic false positives — see §5. |
| Pre-solving | **CLEAN** | No root causes disclosed. Tony's clogged-filter claim explicitly framed as "what I heard, but I want to know what actually came back." |
| Channel lock-in | **NOTED, NOT FAIL** | `#maintenance` still named as the update-note channel. Standard prompt hygiene. |

**Anti-pattern verdict: zero real hits.**

---

## 5. Validator's 2 remaining WARNs (down from 3) — false-positive review

Iter-1 had 3 bolt-on WARNs; iter-2 has 2. The dropped WARN was the "update the Linear issue" sentence (iter-1 WARN 3) — that sentence was rewritten and no longer triggers the heuristic. The 2 remaining WARNs are unchanged from iter-1:

### WARN 1 (still): "Tony told me on Slack it's probably a clogged filter and he'd get someone in Thursday..."

- Paragraph subject established in prior sentence ("The Sunset Ridge 208B AC is where I'm most uncomfortable").
- Remove-sentence test: cutting it destroys the L9 authority-dismissal misdirect (the entire hardness lever for Item 1). Sentence is causally central.
- **False positive.** Named-entity-overlap heuristic doesn't resolve paragraph-topic anchoring.

### WARN 2 (still): "I've been working off the "$8,400 approved scope" from the back-and-forth with Robert..."

- Paragraph subject established in prior sentence ("The Ridgeview roof billing is the other one nagging at me").
- Remove-sentence test: cutting it destroys the L11+L13 first-framing anchor the agent is supposed to defend against by discovering the pass-through structure.
- **False positive.** Same heuristic gap.

Both WARNs share the same root cause: the validator's `named-entity-overlap` heuristic doesn't cross-reference the paragraph topic sentence. In a paragraph-structured multi-item prompt, this heuristic reliably over-fires on the second sentence of each paragraph. Applying the remove-sentence test (the definitive Coherence check per Prompt_Format.md and QC spec) — neither sentence is bolted on.

**Coherence sub-dim = 5/5 (as scored in §3 row 9).**

---

## 6. Verdict

**PASS.**

- Iter-2 retarget (Linear → Airtable maintenance record for Item 2) closes Council A's F1 BLOCKER cleanly.
- All 14 applicable QC sub-dims remain at 5/5. No sub-dim moved from iter-1.
- The delta actually improves two sub-dims materially (Feasibility no longer at latent-phantom risk; Persona better-aligned since Airtable is on Brooke's canonical systems list). Both were 5/5 before; iter-2 makes the 5/5 more robust.
- Multi-write diversification (Hardness Plan L7 baseline) is preserved: 3 distinct write services (Airtable, Slack, Gmail), 4 total writes vs baseline 3.
- Density projection (50.0 midpoint) invariant to the Linear-vs-Airtable substitution: Airtable writes cost the same supporting-read count as Linear writes did.
- Anti-pattern sweep clean. Two remaining validator WARNs are same-family heuristic false positives as iter-1.

**No fix list. No further revise round from Council B side.** Ready for AUDIT (STRICT) as the S1.5 exit gate. If AUDIT concurs, S1.5 exits PASS.

---

**One advisory for downstream phases (carried forward from iter-1, unchanged by retarget):**
- If S2 OE or S3 rubric author lands on `#maintenance` as the ONLY acceptable channel for the Slack write, be aware Brooke's canonical channel set does not include it (her canonical channels: `#vendors`, `#owner-relations`, `#budget-review`, `#general`). If rubric wants maximally-strict persona, `#general` would be a more canonical fallback. Do NOT rewrite the prompt for this — the prompt as written names `#maintenance` and that is a valid supervisor cross-team coordination action.

**One additional advisory introduced by iter-2 retarget:**
- S2 OE authoring should now anchor Item 2's write on the Airtable `tblMakeReady` `Ridgeview - Roof Section` row (per Hardness Plan L8 first-link) rather than a Linear issue. OE writers who copy from Item 1's Airtable-write shape should get this right by default, but flag if S2 draft accidentally reintroduces the Linear write from stale memory.
