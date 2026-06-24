# Hardness Playbook — Stumping Opus 4.8

The single biggest lever for QC pass rates is **hardness without contrivance**. Opus 4.8 is the model under test. The patterns below are the ones that empirically defeat it on Brookfield tasks. Each lever maps to a hard-tip observation in `Docs/4_Prompt_Hard_Tips.md`. **No universe edits** in this pipeline — every lever must be found in the per-task `_aux/Universe_Split/` before being engineered into the prompt.

## Opus 4.8 failure modes (the levers)

| # | Lever | Failure mode it triggers | Hard-tip source | Tool-call cost |
|---|---|---|---|---:|
| 1 | **Latching** | Same incident in 2+ services with different counts/scope; the more-findable source is incomplete. Agent reports the first framing. | "Agents latch onto the first framing they encounter" | 5-8 |
| 2 | **Structured-DB skip** | Load-bearing fact lives only in Oracle GL / SAP / BlackLine / Records Vault / Airtable / Linear, not mirrored in email or Slack. Agent reads secondhand chatter and stops. | "Agents skip structured databases" | 4-7 |
| 3 | **Missing reply** | A dispute / question has a buried reply that flips the conclusion. Agent finds the dispute, reports it, never searches for the response. | "Agents don't search for responses to things they find" | 3-5 |
| 4 | **Search-result-cap eviction** | The load-bearing message is buried under high-traffic keywords or in an older thread. It gets pushed out of the top results. | "Data past search result limits is invisible" | 3-5 |
| 5 | **Thread-reply blindness** | The resolution sits in a Slack thread reply, not the top-level message. Agent reads the question, never the answer. | "Slack thread replies are also hard for agents to find" | 2-4 |
| 6 | **Near-miss entity confusion** | Two similar IDs / names / account numbers plausibly confused (`105000` differs per entity; two Noahs; two vendors with the same prefix). | Hard tips + universe account-trap rule | 3-5 |
| 7 | **Multi-write diversification** | Most agents default to one email. 3+ writes across 3+ services (Records Vault upload, Linear comment, Airtable update, Slack post, reminder) forces breadth. | "Diversify your write actions" | 9-12 |
| 8 | **Multi-link chain** | A→B→C where A is easy (Slack mention), B requires a follow-up search (vendor reply, SAP credit memo), C is the actual disposition. | "Three-link chains are harder" | 6-9 |
| 9 | **Universe-grounded gotcha** | Force a check that punishes assumed knowledge (account-role per entity, retention code that doesn't exist, unused `public` classification, open period past lock target, exception in `awaiting_approval` past SLA). | Universe summary anti-patterns | 3-5 |
| 10 | **Reversal / supersession** | A JE has `status="reversed"` and a `reverses_entry_id` partner; an SOW / W-9 / engagement letter has been superseded. Agent uses the gross figure or the old reference. | Task 11 / 12 worked examples | 4-6 |
| 11 | **Net-vs-gross framing** | An aggregate of "wire activity" or "AP spend" depends on which adjustments to apply. Agent uses the gross. | Task 11 worked example | 4-7 |

## Tool-call density projection (HARD GATE)

`PIPELINE HARDNESS` MUST project tool-call density before greenlighting S1. The projection sums:

| Component | Tool-call cost |
|---|---:|
| Base discovery (contact lookups, channel resolution, period lookup) | 5-8 |
| Sum of selected levers (from the table above) | ~ sum of ranges |
| Write actions (target 3+ writes × ~3 supporting reads each) | 9-12 |
| Cross-service triangulation buffer | 5-8 |

**Design target: average projected tool-call count must be ≥ 50 to greenlight S1 cleanly.** Three bands: midpoint ≥ 50 = PASS; midpoint 40-49 = `THIN_DENSITY` (operator can continue with per-task justification but task is at risk of underflow on real platform runs); midpoint < 40 = `INSUFFICIENT_DENSITY` (STOP — must add levers, expand write-action mix, or both). The 50+ midpoint design target produces ~40+ tool calls in real platform runs, which is the empirical floor below which tasks come back failing density.

## Composition rules

- **4-to-5 levers per task is the design default.** 3 is acceptable only if the chosen 3 include high-cost levers (L7 multi-write 9-12, L8 multi-link 6-9, L11 net-vs-gross 4-7 — sum 19-28) AND the operator documents in `Hardness_Plan.md` why expanding wasn't possible (universe constraint). To hit the 50+ midpoint design target consistently, default to 4-5 levers — 3 levers will frequently land in the THIN band (40-49) or below.
- **Levers must be discoverable, not buried.** Difficulty comes from connecting evidence, not hiding it. The first link of every chain must be findable through a normal broad search.
- **Each lever must be grounded in this task's `_aux/Universe_Split/`.** If a lever doesn't have backing data, drop it.
- **Stack with discipline.** Pair structured-DB-skip with multi-write so the agent has to query the source AND act on it. Pair missing-reply with latching so the agent has to override its first read.
- **3+ writes across 3+ services minimum.** Mix of: email, Slack channel post, Linear comment / update, Records Vault upload, Airtable update, reminder, calendar event, JE lifecycle, AP invoice approval / void, reconciliation lifecycle.

## Stump Hypothesis output (what HARDNESS phase emits)

Per task, HARDNESS produces `_aux/Hardness_Plan.md` containing:

1. **Levers Available** — which of the 11 the per-task data supports, with a one-line evidence pointer per lever (`<file>:<row_id>` or `<file>:<index>`).
2. **Selected Levers** — the 3 to 5 chosen, with rationale + projected tool-call cost per lever.
3. **Tool-Call Density Projection** — sum of base discovery + selected lever costs + write-action cost + buffer. PASS at ≥ 50 (design target), THIN_DENSITY at 40-49 (continue with per-task justification), INSUFFICIENT_DENSITY at < 40 (STOP).
4. **Stump Hypothesis** — the 2 to 4 specific rubric outcomes most likely to fail across the 6 Opus runs, with confidence (high / med / low) and reasoning citing the levers.
5. **Hardness Score** — `selected / 5`. If fewer than 3 levers are available, output `INSUFFICIENT_LEVERS`.
6. **Hardness Brief for the Prompt Writer** — a tight paragraph the S1 runbook hands directly to the prompt-drafting sub-agent.

## What hardness is NOT

- Not arbitrary precision ("the email at 3:47 PM"). That is contrived difficulty, fails the QC `Contrived / Unnatural Prompts` dimension.
- Not over-stacking unrelated asks. That fails Coherence.
- Not pre-solving the puzzle in the prompt. That fails Investigation.
- Not naming tools or IDs the agent is supposed to discover. That fails Explicit Tool Mention.
