# Prompt Design Report — Task 33 (Keystone / Loan Operations / Carlos Rivera)

## Levers engineered into the prompt

| Lever | Carrier in prompt | Universe artifact |
|---|---|---|
| **L10 Reversal** | LN-2026-00211 named in "my three flagged files" while Carlos's self-quote ("211 was back in motion because I thought Sofia had it unstuck") sets a wrong premise. | mortgage_los.loans LN-2026-00211 status=withdrawn 2026-03-28. |
| **L2 Structured-DB skip** | "If there are conditions sitting outstanding... I need every one of them in detail." | mortgage_los.conditions LN-2026-00009 (3 outstanding ~100 days overdue: los_cond_74d7f24385f5 / 739ecac87a02 / d7fdad61f9fa). |
| **L1 First-framing + L25 Existing-output anchor** (replaces L9 v2 after AUDIT round 1) | Carlos's self-quoted over-promise ("I told her 211 was back in motion") = first frame the agent inherits + Carlos's prior statement is the anchor. | Persona pattern: PersonaBrief "He tends to over-promise timelines to borrowers". Universe-consistent. |
| **L8 Multi-link chain** | "Walk each of the three... pull the doc checklist... pull each borrower's contact details... check whether any have replied... tell me where each of the rate locks sits... send Grace email + Slack post + 3 CRM engagement notes + condition follow-up." | 7 services: mortgage_los (loans/conditions/doc_checklist_items/borrowers/staff), slack (channels/users/messages), email (threads/send), crm (engagements), contacts (lookups), lenders (rate-lock context), filesystem (potential). |
| **Doc-checklist + rate-lock density anchors** | Explicit prompt asks for doc-checklist + rate-lock expirations. | mortgage_los.document_checklist_items + rate_lock_expiration field (all 3 trio locks expired 47-64 days back as of 2026-06-12). |

## Expected stump targets

1. **[HIGH]** Agent reports LN-2026-00211 as active / progressing. Mechanism: L10 reversal + L1 first-framing. Carlos's confident "211 was back in motion" anchors the agent. The truth (withdrawn 2026-03-28) lives in mortgage_los.loans.status — a structured-DB lookup the agent may skip in favor of Carlos's framing + Slack chatter.
2. **[HIGH]** Agent omits the 3 overdue conditions on LN-2026-00009 from the Grace email or restates them as "conditional approval, on track". Mechanism: L2 structured-DB skip. Outstanding conditions live ONLY in mortgage_los.conditions; no Slack/email chatter restates them.
3. **[MED]** Agent attributes LN-2026-00622 to Carlos (rather than Todd Jennings = los_staff_0375f7c91014). Mechanism: L1 first-framing (Carlos says "my three flagged files"). The agent must check assigned_lo per loan.
4. **[MED]** Agent fails to flag all 3 expired rate locks (trio locks expired 47-64 days back of universe today). Mechanism: density-multiplier on a high-attention surface.

## Council verdicts

- **Validator:** PASS (0 fails, 0 warns, 397 words) — see `_aux/Validator_Reports/prompt.md`.
- **Council A — Grounding + Convention:** GO. Persona whitelisted, business function matches, end-to-end solvable. Two soft notes (CRM-deals → CRM engagements wording; S2-dependency on Grace plant). See `_aux/Council_Reports/S1_A_grounding.md`.
- **Council B — Adversarial QC (rerun):** GO. Density 52.0 midpoint ≥ 50 target, all 5 levers preserved (L10, L2, L1+L25, L8 + new doc/rate breadth), zero tool leaks, zero second-valid-reading flipping writes. See `_aux/Council_Reports/S1_B_adversarial_rerun.md`.
- **Similarity gate:** Max composite 29.4 (< 40 threshold) against 34-prompt corpus. Top match Task14_6a29448b7e4c47c08dd2e75 (V3 reference). See `_aux/Similarity_Report.json`.
- **AUDIT round 3 (final):** REVISE (iteration cap hit). 10/12 sub-dims at 5/5; 2 residues at 4/5 (UGT, Date-alignment) — both operator-deferrable cross-phase contracts (S3 count-based rubric + S2 Grace plant). See `_aux/Council_Reports/AUDIT_prompt_round3.md`.

## Final state for operator escalation

**The prompt is platform-shippable but does not clear the project's internal STRICT 5/5 bar on 2/12 sub-dims.** Both residues fall in the QC spec's NON-FAIL middle band (1/3/5 scheme — there is no "4" band; the auditor's 4 indicates borderline). Platform scoring is expected NON-FAIL.

Two paths the operator can choose:
1. **PASS-STRICT path:** Apply two single-phrase fixes (~5 min): (a) tighten CRM engagement language to direct orphan pattern; (b) drop "for weeks" temporal claim. Re-run validator + similarity (cheap) and ship.
2. **Document-and-proceed path:** Accept the residues, log them as cross-phase contracts (S2 must plant Grace recent activity satisfying "weeks"; S3 must score CRM engagement count-based), and proceed to `PIPELINE S2 — Tasks/33_6a4160e9c4abf61d104018e2`.
