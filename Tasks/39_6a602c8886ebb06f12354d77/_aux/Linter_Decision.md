# Linter Decision — Tasks/39_6a602c8886ebb06f12354d77 — Round 1

**Universe:** starpm (V4) · **Mode:** CB (6_/7_ are empty scaffold placeholders; fixes would land in `5_Prompt.txt` in place) · **Date:** 2026-07-22

## What the platform blocked

Two Class A findings, both returned FALSE by the platform AI-helper, both targeting the same claim that the prompt over-scopes James Bennett:

1. **StarPM Persona check** — James (junior Assistant Maintenance Technician) supposedly lacks the authority to close out a turn, coordinate workstreams, reconcile logged records, post crew-facing channel updates, or draft a status email to John. Reads like an Onsite PM / Lead Tech. Suggested reauthoring from Carlos Mendez.
2. **StarPM Business alignment check** — authoring seat, write actions, and accountability supposedly belong to Property Operations (Cat 1.1 Unit Turnover Coordination), not Maintenance & Repairs (Cat 4). Cites "John Smith is a Lead Tech; he doesn't draft status emails to himself."

No Class B (similarity) block was raised.

## Decision: INVALIDATE both. Prompt left UNCHANGED.

Skeptical-first flow: the two findings rest on a single factual premise (James is too junior for this ask). The per-task universe gives strong, grounded counters, so this is a linter false-positive, not a defect that warrants the expensive revise path.

**Counter-evidence (all re-grounded in `_aux/Universe_Split/`, confirmed by prior S1 Council A/B + an independent oracle re-adjudication):**

- **Persona is a fixed input.** `2_Persona.txt` assigns James Bennett; `1_Business_Function.txt` assigns Maintenance & Repairs. "Reauthor from Carlos Mendez" swaps a given, not a correctable prompt defect. The StarPM persona-anchor rule authors tasks from a persona's HOME function (James = Cat 4), not from participant appearances in a turn.
- **The load-bearing open item is James's OWN maintenance ticket.** OPS-227 / MT-2026-1271 (seized 8D disposal) was flagged by James himself: "This needs a full unit replacement... Routing back to you for parts approval before I swap it. — James" (`linear.linear_comments comment_16a0a0c53f543a1221f08de6a786cb66`; `airtable recac236210094352`, blank completion = OPEN). Investigating, unblocking, and reporting his own disposal ticket is canonical Cat 4.1 work.
- **Every decision routes to his direct lead.** John Smith is the Lead Maintenance Technician and James's lead (`contacts john.smith@starpm.com`; `airtable recf7aecc318b2252` = "John Smith and James Bennett are three days into the in-house make-ready work"). The prompt has James gather the true state and draft John the rundown so John makes the call. James never declares the unit ready, approves spend/parts, or directs anyone.
- **The business-alignment finding is factually wrong.** James authors the email; John receives it. They are different people, so nobody emails themselves. This breaks the finding's central argument.
- **Three prior internal gates already passed persona + BF 5/5** (Council A A4 authority + A10 business function; Council B Persona 5/5, Business Function 5/5; S1 AUDIT). An independent oracle re-adjudication (read the universe itself, applied an anti-rationalization lens, explicitly challenged the invalidate lean) returned **INVALIDATE on both**.

## Residual risk (documented, not acted on)

The one genuine yellow (pushback-risk, not a defect): the `#make-ready` crew-post clause. The universe shows **John** posting the daily progress updates on this turn (`airtable recf7aecc318b2252`), so crew-broadcast is Lead-active here. It is defensible for a named in-house crew member to post a factual stale-info correction, so the prompt stays unchanged. **If the platform rejects the pushback**, the cheapest surgical concession is folding the crew status into the email to John (that edit triggers the full validator + Council A + B + AUDIT re-gate, so do NOT apply preemptively). Do NOT concede the two flagged phrases ("closed out today", "square up what we've got logged") — they are the strongest ground and have plausible junior readings.

## Resolution state

- `5_Prompt.txt`: UNCHANGED (still the S1 draft that cleared validator + both councils + AUDIT).
- `_aux/Linter_Justifications.md`: two justifications, one per platform finding (Persona check + Business alignment check); `check_justification.py` = 0 hits, exit 0.
- `Tasks/_meta/Linter_Justifications.md`: entry appended (with the wrong-universe-pattern distinction vs Tasks 35/36).
- No revision → no AUDIT re-run (S1.5 step 8: AUDIT skipped for justification-only resolutions).

## Carry-forward to S2 (upstream hygiene, flagged by S1 Council B — NOT an S1.5 concern)

1. `_aux/Fact_Ledger.json` `lifecycle.today` is null (should be 2026-07-01). Council B says fix before S2/S3 (A3 narrative-state checks consume it). Rebuild via `build_fact_ledger.py` seeding today from the registry, or patch the value.
2. `_aux/S0_Setup_Report.md` claims `9_Universe_inject.sql` is "present with executable statements (73 lines)" and injection PASSed, but the file is a comment-only stub and `4_Changelog.json` is `[]`. Correct the report to "no separately-documented injection".
