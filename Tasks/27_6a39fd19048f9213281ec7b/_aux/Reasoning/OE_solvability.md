# OE Solvability — Tasks/27_6a39fd19048f9213281ec7b

Written: 2026-06-23 (S2 phase close)
Deliverable: `6_Oracle_Events.txt` — 24 OEs

## Verdict chain

| Gate | Result | Report |
|---|---|---|
| `validate.py --phase oe` | PASS (0 fails, 0 warns, 1 note: OE count 24) | `_aux/Validator_Reports/oe.md` |
| Council A (Grounding + Convention) | GO | `_aux/Council_Reports/S2_A_grounding.md` |
| Council B (Adversarial + Density + Hardness) | GO | `_aux/Council_Reports/S2_B_adversarial.md` |
| AUDIT (oracle, --phase oe, strict 5/5 / 50+ density) | PASS (STRICT) | `_aux/Council_Reports/AUDIT_oe.md` |

## OE-to-prompt coverage map

Prompt is 7 paragraphs. Mapping load-bearing sentences to OEs:

| Prompt clause | OE step(s) |
|---|---|
| "recon for the May close" / "exception on it is now lined up for accept-timing" | OE 3 (recon read), OE 5 (exception read) |
| "re-check both pieces against what is actually there" | OE 6-9 (re-check disposition story across Slack + email + messaging); OE 15-17 (re-check supporting evidence) |
| "Take the precedent claim from where it was raised" | OE 6, OE 7 (locate + read on C005 thread ts 1780147500.000000) |
| "Tell me what period it points to, the figure, the cause, and how it was closed out" | OE 7 (extract George's four pillars: FP-2025-11, $42, feed-drop residual, accept-timing/retry-clean) |
| "take it apart on all four: same account, same period, same cause label, same close-out path" | OE 10 (FP-2025-11 recon BL-8DCA6908E272), OE 11 (FP-2025-11 feed run run_9e4afe5f93d549) |
| "If that period is not the closest fit... which recent prior-period record on this account is the closer fit, and what that one shows on the same four" | OE 12 (list_exceptions filtered to brookfield/102000), OE 13 (exc_d8fc13aa2cc742 read), OE 14 (BL-782A2EC69343 read) |
| "Do the same on the supporting evidence... Read what each piece is labelled as. Then open the underlying documents" | OE 15 (blackline_show_data + client-side filter on evidence rows), OE 16 (doc_01b7c6e1cbe94529), OE 17 (doc_b3633a2899a04e9e) |
| "If the contents do not back the cause the recon is asserting, say so plainly" | OE 16, OE 17 conclusions + propagation into OE 20(b) / 22(3) / 24(b); USD-cash grounding from OE 4 propagates to OE 20(c) / 22(4) / 24(b) |
| "drop a write-up... into the vault under the close-cycle file" | OE 20 (records_vault_upload_document on BL-333FF9956BC6) |
| "Drop a short note into the channel the precedent was raised in" | OE 21 (slack_conversations_add_message on C005 thread 1780147500.000000) |
| "send George a direct line" | OE 22 (email_send_email to george.mcadam@brookfieldcpas.com) |
| "Set me a reminder to chase this with George before the period certifies" | OE 23 (reminder_add_reminder, framed distinct from existing reminder_scen_009_orphan_exception_0000 / _0008 per OE 18 pre-check) |
| "Tell me what you found and where you left it" | OE 24 (final user-facing response) |

FORWARD coverage: every actionable prompt sentence has at least one OE step. REVERSE coverage: every OE step maps to a real prompt ask (OE 18 anti-L25 reminder pre-check feeds OE 23's distinctness; OE 19 contact lookup feeds OE 22's recipient resolution; OE 1 is base persona self-lookup).

## OE-to-rubric mapping preview (for S3)

Anticipated Outcome rubrics (rubric drafting happens in S3):

| Likely rubric | OE source |
|---|---|
| 1.1 — Agent identifies `exc_d8fc13aa2cc742` (FP-2025-12, unrecorded_invoice, -617.63, "Corrective JE posted", BL-782A2EC69343) as the actual recent 102000 precedent | OE 12, OE 13, OE 14, propagated through OE 20(a) + 22(2) + 24(a) |
| 1.2 — Agent disproves all four pillars of George's FP-2025-11 / $42 / feed-drop / accept-timing-retry-clean claim against records | OE 10 (figure / cause / close-out), OE 11 (close-out via feed-run status) |
| 1.3 — Agent identifies both recon-evidence attachments as kind-mislabelled JE-support for unrelated Marketing / AICPA entries | OE 15, OE 16, OE 17, propagated through OE 20(b) + 22(3) + 24(b) |
| 1.4 — Agent grounds the USD-cash → no-FX-revaluation finding on 102000 brookfield | OE 4, propagated through OE 20(c) + 22(4) + 24(b) |
| 2.1 — Vault write-up uploaded with correct kind/retention/classification, related to BL-333FF9956BC6, containing all four findings | OE 20 |
| 2.2 — Slack thread post added to C005 thread 1780147500.000000 with the findings, not a disposition decision | OE 21 |
| 2.3 — Direct email to george.mcadam@brookfieldcpas.com with all four findings | OE 22 |
| 2.4 — Pre-certify reminder set with distinct framing from existing reminders | OE 23 |

Pure-discovery steps (no rubric expected): OE 1, OE 2, OE 5, OE 6, OE 7, OE 8, OE 9, OE 18, OE 19. OE 24 is the user-facing summary and is typically not a separate rubric (Outcomes 1.1-1.4 absorb its substance).

## Hardness levers traced

| Lever | Exercising OE(s) |
|---|---|
| P1 Latching (3-service consistency) | OE 6-7 (Slack), OE 8 (email pair), OE 9 (messaging) |
| P2 Structured-DB skip (blackline_evidence via blackline_show_data → RV docs) | OE 15, OE 16, OE 17 |
| P7 Multi-write diversification (4 writes across 3 services) | OE 20 (vault), OE 21 (Slack), OE 22 (email), OE 23 (reminder) |
| P8 Multi-link chain (precedent dig) | OE 10, OE 11, OE 12, OE 13, OE 14 |
| P9 Universe-grounded gotcha (USD Cash-Payroll → no FX) | OE 4, propagated into OE 20(c) / 22(4) / 24(b) |
| L9 authority-dismissal overlay (5-way alignment on wrong call) | OE 6-9 establish; OE 13-14 ground the disagreement on real data |

All six selected levers traced end-to-end. P8 (the load-bearing rebuild discriminator) is reachable from the prompt because of the explicit "If that period is not the closest fit... which recent prior-period record on this account is the closer fit" sentence.

## Density projection

Strict-minimum reading: 31-34 calls. Realistic reading: 45-55 calls. Candidate trajectory_stats on a similar shape: avg 53 / min 30 / max 69. AUDIT density bar 50+: PASS (avg 53 ≥ 50; OE 11 + OE 12 explicitly mandate pagination on subledger_feed_runs and list_exceptions).

## Notes from the verdict chain

- Council B blocked twice on (a) OE 15 tool-name shape and (b) OE 22 messaging-fallback param shape. Both fixed in-place; re-pass GO.
- Council B's initial PROPAGATE-TO-S1 was against a prompt quote that does not exist in `5_Prompt.txt`. The actual prompt already invites the cross-period precedent search via the "closer fit" sentence. Re-pass confirmed no propagate.
- AUDIT raised three MINOR non-blocking notes (OE 23 example due_datetime sits one day pre-today but is framed as illustrative; OE 10/13 use "about $X" narrative after exact figures are cited; OE 22 single-channel email lock-in is acceptable for "direct line"). None block.

## Next phase

`PIPELINE S3 — Tasks/27_6a39fd19048f9213281ec7b` in a fresh chat to draft `7_Rubrics.json`.
