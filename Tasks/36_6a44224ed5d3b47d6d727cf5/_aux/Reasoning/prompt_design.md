# S1 Prompt Design — Task 36

## Persona + Business Function
- **Persona:** Julian Brooks — Lead Customer Support Specialist
- **Business function:** Customer Engagement (MoveOps 30% weight)
- **Universe:** MoveOps (V2.1 framework · universe today 2026-04-26 Sunday US/Pacific)

## Levers engineered into the prompt

| Lever | Prompt anchor | Failure mode preserved |
|---|---|---|
| **L25** — Existing-Output Anchor Trap (HIGHEST yield) | *"both went out the door as apologies with promises attached, not actual answers"* — signals Julian's own 4/23 outbounds were template-shaped, tempting the agent to re-use them. | Agent paraphrases Julian's 4/23 apology-then-promise (`email_email_6d0501ac647f` + `email_email_bedc44dbea30`) back to Simone/Marcus as the "status update," missing UrbanNest booked-vs-delivered facts, credit posture, hard-transfer availability, next factual checkpoint. |
| **L9** — Authority Self-Anchor (soft verbs per L24) | Prompt does NOT explicitly override Julian's 4/22 C007 self-anchor (*"If Airtable is showing completed/confirmed, just send him a quick acknowledgment and leave it in the queue"* — `slack ts 1776298200`). Agent will encounter it as persona-belief authority. | Agent reads `airtable.recSimoneRichterBrightloop.Status = "In Progress"` (correct observation), concludes "still active, just needs a check-in" (wrong conclusion) — never opens Special Requirements, never quantifies credit against QB invoice INV-2026-0308 = $11,350. |
| **L26** — Decoy Parent Thread | *"put the Slack status update on the audit thread Mina raised Thursday, not in a fresh post"* — 4 competing Slack parents remain valid distractors (Julian's C007 orphan `ts 1777011000`; Julian's C002 "Drafted and sent" `ts 1777012200`; Mina's C002 audit `ts 1776997200` — CANONICAL; Julian's C007 StormCloud context `ts 1777116900`). | Agent posts to Julian's own dead C007 orphan (self-answering) OR to a fresh no-parent post, when canonical target is Mina's C002 audit `ts 1776997200`. Lever partially thinned by "Mina raised" wording — yield reduced from 80%+ to est. 40-60% but "not in a fresh post" clause preserves the mechanism. |
| **L2 (MoveOps-adapted)** — Airtable-silence + QuickBooks-invoice skip | *"pull the booking-versus-delivered picture from email"* + *"what the swing on our account is"* + *"what the money impact looks like on the batch"* — never explicitly directs Airtable Special Requirements or QB invoice queries. | Agent trusts email/Slack chatter as SSOT for the unit-type claim (1BR promise), never queries `airtable.recSimoneRichterBrightloop.Special Requirements` (silent on unit type) or `quickbooks.invoices.1008 = INV-2026-0308 = $11,350` for credit-math base. |
| **Emergent L8** — Three-service reduction | Byproduct of L25 + L2 stacked: the truthful recovery answer requires Airtable relocation record read → email UrbanNest/Carmen no-reply verify → QuickBooks invoice for credit math. | ~40% pass — the target failure mode. Cross-service triangulation intrinsic to the persona role (Lead Customer Support Specialist closing recovery). |

## Expected stump targets

1. **[HIGH]** Opus 4.8 re-uses Julian's 4/23 apology template. Mechanism: L25.
2. **[HIGH]** Opus 4.8 trusts Julian's 4/22 self-anchor + reads only Airtable Status = "In Progress". Never quantifies credit against QB. Mechanism: L9 + L14.
3. **[MED]** Slack recovery-status post attaches to Julian's own dead C007 orphan OR to a fresh no-parent post. Mechanism: L26 (partially thinned).
4. **[MED]** Opus 4.8 conflates 3-way Marcus Webb identity (BrightLoop / Ironclad / gmail.lab) or 2-way Simone Richter (BrightLoop / StormCloud) and mis-addresses outbound. Mechanism: L4-adjacent (secondary attribution risk).

## Council + AUDIT verdicts

| Gate | Verdict | Notes |
|---|---|---|
| Validator (`validate.py --phase prompt`) | PASS | 0 FAIL, 3 WARN (bolt-on false-positives on paragraph-continuity sentences), 6 NOTE. Word count 380 / 400 sweet spot. 0 em/en-dash, 0 tool names, 0 MCP names, 0 internal IDs. 4 distinct services referenced (regex count). |
| `verify_universe_atoms.py` | PASS | 0 atoms checked (prompt has no numeric / ID atoms). |
| Council A — Grounding + Convention (explore) | GO | 13/13 claims grounded (A1); 0 convention drift (A2); 0 narrative-state contradictions (A3); 0 action-divergences / authority-gaps (A4); Customer Engagement business function match (A10); full solvability chain (A11). 4 non-blocking advisories forwarded. |
| Council B — Adversarial QC (oracle, 5 role lenses) | GO | 12/12 QC sub-dims 5/5. Density midpoint 50 (PASS at design target). All 5 levers preserved. Service breadth 7 distinct services ≥ 5%. 2 low-severity notes on L26 partial thinning + persona-attribution landmine. |
| Similarity gate | PASS | Max composite 27.6 vs 37-prompt corpus (top match V3 Task14 at 27.6 raw, ×1.0 same-universe multiplier). Well below 40 pivot band + 35 near-pivot band. |
| Regression-anchor suite | PASS | 48/48 anchors fire. |
| AUDIT — STRICTEST veteran (oracle, 9 lenses) | PASS (STRICT) | Per-atom evidence table complete (13 rows). Zero BLOCKER. Zero LENS-1 sub-dims < 5. Every lever traces end-to-end with cited evidence. Density 50 midpoint holds under strictest reading. 9 advisories forwarded to S2/S3, none rising to REVISE after Lens 7 hard-exclusion checks. |

## Final similarity result
- Max composite: **27.6** (top match: `QC_Tasks/V3_Tasks/Task14_6a29448b7e4c641c30eb3875/Prompt.txt` — cross-universe reference, same-universe multiplier 1.0 for V3 corpus alignment; low raw lexical overlap because Task14 is a Brookfield JE / partner-sign-off scenario while Task 36 is a MoveOps customer-recovery scenario).

## Density projection carry-through
- Hardness_Plan projected midpoint: 50 (range 41-59) at design target.
- Council B B3 re-projected midpoint: 50 (Architect + Implementer + Red-team + Ground-truth + Integration lenses all agree).
- AUDIT Lens 4 strictest-reading projected midpoint: ~45-50 (borderline THIN if agent aggressively semantically-filters L26 parent enumeration; PASS at Council B baseline of 50 with 4 non-optional writes preserving floor).
- **Verdict:** PASS at design target. If real-run density comes in < 45, the fix is at S3 rubric-tightening (require enumeration + author cross-checks even when hints are present), NOT S1 prompt-revision — the prompt's write-action mandate is already exhaustive.

## Forwarded advisories (S2 / S3 attention)
- Fact_Ledger `today` stale (2026-06-12); Universe_Index timezone drift (NY vs Pacific); Hardness_Plan drift on Julian self-anchor date (says 4/22, actual 4/16 PDT).
- Additional Mina C002 candidate at `ts 1776999900` not in Hardness_Plan L26 decoy list — S3 must specify exact `thread_ts_legacy = 1776997200.000000` as canonical Slack parent.
- `email_email_ab2391d62ab1` sender field mis-tagged as Carmen (data anomaly) — S3 grounding must select by content / recipients / subject.
- Persona-attribution landmine on Marcus Webb (3-way) + Simone Richter (2-way) + Carmen Reyes (2-way) — S3 rubric grounding must grep candidate email addresses per auto-memory `persona_attribution_landmine.md` + `review_audit_must_deep_query_universe.md`.

## Exit
All S1 exit criteria met. Prompt shipped. Awaiting user next-trigger (`PIPELINE S1.5` on platform linter response OR `PIPELINE S2` on linter clean).
