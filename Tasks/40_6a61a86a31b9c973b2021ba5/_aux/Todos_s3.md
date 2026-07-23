# Todos — S3 (Rubrics)

- [completed] 1. Read reference materials (Rubric_Format.md, Strict_Convention_Inventory.json, V4 QC ref rubrics, StarPM tool catalog, Rubric guidelines, Always-Failing Rubrics doc)
- [completed] 2. Read Fact_Ledger.json + Universe_Split slices for grounding values (Airtable MT-2026-1327 rec92f4a1c8e17bd3, Linear OPS-231, QB bill 195836274018, Gmail thread d1e2f3a4b5c6789a, Slack ts 1782789240.000301 + 1782824160.000302 + 1782863220.000303, contacts, calendar)
- [completed] 3. Draft 7_Rubrics.json (Outcome first: 1.1 per OE write action, 1.2 for content requirements, 2.1 for prompt tell-me cues); apply three-condition test before ANY process rubric
- [completed] 4. Run validator (validate.py --phase rubrics)
- [completed] 5. Fix validator issues, re-run until clean (fixed Slack channel-name form; amount WARNs are false-positive validator heuristics)
- [completed] 6. Spawn Council A grounding sub-agent (GO — all 16 grounded, no defects; report at _aux/Council_Reports/S3_A_grounding.md)
- [completed] 7. Spawn Council B adversarial ultrabrain sub-agent (GO — 5/5 on every sub-dim, 6/6 levers preserved; report at _aux/Council_Reports/S3_B_adversarial.md)
- [completed] 8. Apply council fixes, re-run validator + councils (no fixes needed; both councils GO first pass after Slack channel-name flex fix)
- [completed] 9. Auto-fire strict veteran AUDIT (ultrabrain) with --phase rubrics (PASS STRICT; report at _aux/Council_Reports/AUDIT_rubrics.md)
- [completed] 10. Iterate on AUDIT REVISE findings (cap 3 rounds — zero REVISE needed)
- [completed] 11. Write coverage matrix _aux/Reasoning/Rubric_Coverage_Matrix.md
- [completed] 12. Write cross-source verification _aux/Verification_s3.md
- [completed] 13. STOP gate — end response, wait for PIPELINE FINAL
