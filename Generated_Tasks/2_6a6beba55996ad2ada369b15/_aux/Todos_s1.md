# Todos — S1 (`2_6a6beba55996ad2ada369b15`, universe harmonygames)

- [x] Run `phase_ready.py --phase s1` (exit 0, Hardness_Plan present)
- [x] Read `Reference/Sessions/S1.md`, `Reference/Prompt_Format.md`, `_aux/Hardness_Plan.md`
- [x] Read `Docs_harmonygames/9_Common_Error.md` (Part 1 prompt errors) BEFORE drafting
- [x] Read `Docs_harmonygames/4_Prompt_Hard_Tips.md`
- [x] Read `Docs_harmonygames/6_Prompt_Relative_Time_Updates.md` (date SSOT, today = 2026-02-28 Sat)
- [x] Resolve the spine fork the Hardness Plan escalated -> operator chose **(c) combined**: Combo Fighter post-mortem as the ask, wind-down as the context
- [x] Read `_aux/Universe_Index/*` (today_horizon, key_facts)
- [x] Read HG reference prompts (`QC_Tasks/V5_HG_Buckets/QC_Passed/Task2,Task4`) for voice
- [x] Read `Reference/Council_Protocol.md` (confirmed B3's 50/40 bands are V3-family, NOT hg)
- [x] Re-verify the load-bearing atoms against `_aux/Universe_Split/` before writing them into the prompt
      -> forced 3 corrections to inherited premises, logged in `_aux/Reads_s1.md`
- [x] Draft `5_Prompt.txt` (<= 500 words, no em-dash, no tool names, no internal IDs, no pre-solving)
- [x] Run `validate.py --phase prompt` -> PASS, 0 fails / 0 warns, 395 words
- [x] Run `check_persona_acl.py` -> 0 findings
- [x] Council A — grounding -> `_aux/Council_Reports/S1_A_grounding.md` -> **GO** (1 MINOR, A7b)
- [x] Council B — adversarial QC -> `_aux/Council_Reports/S1_B_adversarial.md` -> **conditional GO**, 3 propagations
- [x] Similarity gate -> max composite 29.8 (< 40); HG sibling confirmed present in corpus at 8.2
- [x] Apply Council B finding #2: para 5 rewritten so the written account is unambiguously a THIRD
      artifact distinct from the Slack post (was buying 2 writes, not 3; density sat at ~40 with no margin)
- [x] Re-run validator + ACL + similarity on the revised draft -> all still clean
- [x] Re-run BOTH councils on the revised deliverable -> Council A **GO**, Council B **GO**, density finding RESOLVED
- [x] AUDIT (mandatory per AGENTS.md rule 12) -> `_aux/Council_Reports/AUDIT_prompt.md` = **PASS (STRICT)**
- [x] Write `_aux/Verification_s1.md` (cross-source + eval sub-dim declarations)
- [x] Write `_aux/Reads_s1.md` (running log)
- [x] Final report written to `_aux/Reasoning/prompt_design.md`
- [x] STOP gate: S1 complete. Next trigger `PIPELINE S2 — Generated_Tasks/2_6a6beba55996ad2ada369b15` in a FRESH chat.

## Carried forward to later phases (from Council B B6, do not lose)

1. **-> S3** Bind the tracking-item criterion to the ad-spend target (114 rows / $2,444.08 post-02-09),
   not to a kept-vendor list. Bind revenue to v1 `REVENUE_DAILY` so a `_V2` "no CF data" read fails.
   Role-bind `$22,500`: it collides exactly with `CASH_BALANCE.monthly_net_burn = 22500`, so grading it
   as a bare token mis-grades. If S4 shows runs naming different targets, this converts to a UGT fail.
2. **-> S2/S3** L10 supersession (sale to licence; final vendor disposition) is surfaced but not forced.
   Either cover it in the OE and rubric set or explicitly accept it as carried by the obligations
   reconciliation. Do not leave it implicit.
3. **Known gap, mine not a council's**: Council A could not isolate the `AD_SPEND_DAILY` max date after
   repeated parse attempts and dropped it as non-material. It is NOT non-material, it is the spine's
   central fact. It IS verified, by my own direct query in this session: max date 2026-02-28, post-02-09
   CF spend $2,444.08 across 114 rows, $8,452.64 across all three titles, $160.88 dated today. Council B
   independently re-confirmed the post-stop continuation. Recorded so no later phase treats it as unverified.
4. **-> S3 (from Council A A7b, MINOR)** "whatever is still costing us" leaves the cost SET open by run.
   The write-action set is fixed at one tracking item, so write actions do not diverge, but the tracker
   criterion must be bound to the final state rather than to any single vendor.
