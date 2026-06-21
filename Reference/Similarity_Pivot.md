# Similarity Pivot Card

When the platform linter reports **40% or higher similarity** with a previously submitted task, the prompt must be pivoted while preserving the Hardness levers from S0. Drop into one of the 6 lever menus below. Combine if needed.

## The 6 levers

| # | Lever | What changes |
|---|---|---|
| 1 | **Acting persona** | Same situation, different acting voice. A partner asking instead of a senior. A compliance officer instead of an audit senior. Forces full persona-brief re-draft of the prompt. |
| 2 | **Ask-shape (reactive ↔ proactive)** | If the original is reactive ("X just landed, handle it"), pivot to proactive ("I'm prepping for next week's review, find anything off"). And vice versa. |
| 3 | **Underlying conflict type** | Swap the kind of friction: vendor dispute → SOW supersession → AML soft flag → reconciliation variance → BD3 lock blocker → out-of-scope absorb-or-change-order. |
| 4 | **Entity / scenario focus** | Move the anchor from Brookfield-internal to a client (Acme or Northstar), or from one period to another, or from one vendor family to another. The hardness levers travel; the concrete records change. |
| 5 | **Write-action mix** | If the original ends in email + Slack post + Linear comment, pivot to Records Vault upload + reminder + Airtable update. Different write surface, same investigation depth. |
| 6 | **Workflow shape** | Single-thread investigation → branching ("if A then X, if B then Y"). Or step-by-step dependency → stacked-asks unified by one situation. Or escalation → close-out / cleanup. |

## Process

1. Read the linter output. Identify which previously submitted task it matched and what dimensions of overlap drove the similarity score.
2. Pick the smallest pivot that breaks the match. Usually 2 of the 6 levers is enough.
3. Re-confirm the Hardness levers from S0 still apply after the pivot. If a pivot drops below 3 hardness levers, the pivot is wrong; pick a different combination.
4. Redraft `5_Prompt.txt` from scratch using the new persona / shape / focus. Do NOT incrementally edit the old prompt — surface-level edits leave too much fingerprint.
5. Log the pivot to `Submitted-Tasks/_meta/Similarity_Log.md` with the linter excerpt, the previous-task reference, the levers used, and a one-line outcome.

## Pivot patterns that empirically work

- **Persona swap** ("George the senior" → "Daniel the manager") forces a different vocabulary register and changes which open threads are natural to mention.
- **Time-frame swap** (mid-close → post-close cleanup; quarterly cycle → annual roll-forward) changes which records are load-bearing.
- **Counterparty swap** (vendor escalation → client escalation, internal blocker → external regulator query) changes the receiving inbox and the write-action mix.
- **Compliance angle swap** (AML wire flag → independence violation → retention sweep → improper-request refusal) changes which Records Vault and Airtable workflows surface.

## What NOT to do

- Do not just reorder sentences in the existing prompt.
- Do not just rename people. The work shape stays the same.
- Do not weaken the hardness. A pivoted prompt that loses 2 levers is a regression.
- Do not add new universe facts to "make room" for the pivot. No universe edits in this pipeline.
