# Verification — S1 (`2_6a6beba55996ad2ada369b15`)

Universe **harmonygames** (framework `hg`) · persona **Robert** · business function **Executive** · universe today **2026-02-28** · model under test **Claude Opus 4.7**

## Data sources consulted

### Per-task data

- `_aux/Universe_Split/slack.2026-02.json` :: full reconstruction of #winddown (C0ADGSZKR3R), all 212 February messages in timestamp order. Grounded the 02-09 shutdown decision, the $22,500 / $11,700 pair (ts `1770911000.728559`), the sale-to-licence restructure (ts `1770924424.711879`, `1770924465.624129`), the consolidated vendor disposition (ts `1770933601.686309`), board-level personal liability (ts `1770674426.735229`), Leonard's outstanding angel outreach (ts `1770934638.035469`), and the account-wind-down action list (ts `1770933903.645709`).
- `_aux/Universe_Split/slack.2026-01.json` :: checked the January campaign-pause thread (ts `1768166394.438899`) and deliberately excluded it from the solution path.
- `_aux/Universe_Split/snowflake.snowflake.tables.json` :: streamed line by line, never fully loaded (159 MB; hard rule 33). `FINANCE.EXPENSES.CASH_BALANCE` at 2026-02-28 = cash_usd 2500 / runway_months 0.1 / monthly_net_burn 22500. Combo Fighter footprint mapped across all 33 tables.
- `_aux/Universe_Index/today_horizon.json` :: universe_today 2026-02-28 America/Chicago, 0 records dated after today.
- `_aux/Hardness_Plan.md` :: five selected levers, risk register, Hardness Brief. Spine fork escalated to the operator and resolved as option (c).
- `PersonaBrief.txt` :: Robert owns difficulty curves, progression/card economy, and co-drove the seed fundraise. Both are load-bearing in paragraph 1.

### Eval spec

- `Evals_harmonygames/1_Prompt_Eval.md` :: all 12 prompt sub-dims scored against this draft. Per-sub-dim verdicts are recorded in full under "Eval spec sub-dims" below.

### QC spec

- `Docs_harmonygames/7_QC_Spec_Doc1.json` :: the scored HG QC specification (7 dimensions / 38 sub-dims, 18 binary). Prompt-dimension scoring is recorded under "QC spec sub-dims" below.
- `Docs_harmonygames/8_QC_Spec_Doc2.md` :: severity ladder and the human reading of the scored dimensions.

## Corrections forced on inherited premises (detail in `_aux/Reads_s1.md`)

1. The licensed data is the **company corpus** sold to AI labs (ts `1770858442.063329`), NOT Combo Fighter telemetry. The obvious way to unify the operator's combined spine would therefore have been a Truthfulness defect. Discarded before drafting.
2. `LEVEL_PERFORMANCE` and `USER_COHORT_RETENTION` carry **zero** Combo Fighter rows. Nothing in the prompt implies level-difficulty or cohort data exists for that title.
3. `REVENUE_DAILY_V2` and `UA_SPEND_UNIFIED_V2` carry **zero** Combo Fighter rows against 72 and 330 in their v1 counterparts. Live decoy, carried to S3 as a binding instruction.
4. **AUDIT correction to the Hardness Plan itself**: the plan and Council B both asserted *zero* universe hits on `10800`. There are **5**. AUDIT ran them down: all are coordinate integers (`X: -0.1080000251531601`) in puzzle-layout files or ID strings (`SES-1080...`, `INS-0010800`). Zero are currency-formatted. L11 is clean, but the plan's claim was imprecise and would have concealed a real answer leak had any hit been money.

## Eval spec sub-dims (`Evals_harmonygames/1_Prompt_Eval.md`) verified

- 1.1 Unique Ground Truth :: **PASS**. AUDIT found a stronger disambiguator than either council: the prompt demands the target be "named with a figure against it", and the kept vendors (Deel, gusto, Intuit, Linear) carry no derivable per-vendor dollar figure anywhere (`MONTHLY_BURN` is categorised, not per-vendor), while the ad-spend leak does. Two independent universe-grounded disambiguators converge on one target.
- 1.2 Feasibility :: **PASS**. All 27 `gmail_*` tools verified send-less; all three writes internal. Ad networks are not callable services, so the leak is satisfiable by naming it with a figure and an owner.
- 1.3 Explicit Tool Mention :: **PASS** (binary). Zero tool names, MCP names or internal IDs; validator regex clean.
- 1.4 Prompt Clarity and Specificity :: **PASS**. The collapse reading that Council B found on the first draft is closed; Slack is itself named among the surfaces losing history, so it cannot satisfy the durability clause.
- 1.5 Contrived / Unnatural :: **PASS**. Founder voice, deliverables stated as goals rather than enumerated contents. 395 words, inside the passed-HG reference band.
- 1.6 Truthfulness :: **PASS**. Every premise re-read from the universe; the one false candidate premise was discarded pre-draft.
- 1.7 Tool use and Cross-service :: **PASS** (binary). 4 genuine services on the necessary path.
- 1.8 Investigation :: **PASS**. Investigation and action cues both present; information friction is real (structured-source skip, `_V2` decoy, first-framing latch).
- 1.9 Coherence :: **PASS** (binary). Remove-any-sentence applied to all six paragraphs by AUDIT; one spine, no bolt-on. This was the highest-risk sub-dim given the combined spine.
- 1.10 Persona :: **PASS**. Roster-exact identity; Robert's ownership of the design call and the seed raise both grounded.
- 1.11 Business Function :: **PASS**. Executive, unchanged (the fixed scope anchor).
- 1.12 Alignment with Today's Date :: **PASS**. "the ninth" resolves to 02-09; no weekday deadline; no "Q1 close" framing (Q1 runs to March 31); the ~15-day staleness gap handled retrospectively.

## QC spec sub-dims (`Docs_harmonygames/7_QC_Spec_Doc1.json`)

Council B scored every applicable Prompt sub-dim at 5, reading schemes from the HG spec itself (7 dimensions / 38 sub-dims, 18 binary; `Alignment with Today's Date` is NOT binary here, unlike other universes). AUDIT re-scored at the strictest defensible reading with no NON-FAIL bands invoked.

## Reference docs consulted

- `Reference/Prompt_Format.md` :: 500-word cap and em-dash ban re-checked (both are hg project policy, not upstream spec). HG deltas applied.
- `Docs_harmonygames/9_Common_Error.md` :: read BEFORE drafting per the runbook. All four top-frequency prompt misses explicitly defended against.
- `Docs_harmonygames/4_Prompt_Hard_Tips.md` :: structured-source skip and first-framing latch are the two documented failure modes this prompt is built on.
- `Docs_harmonygames/6_Prompt_Relative_Time_Updates.md` :: date SSOT.
- `Reference/Council_Protocol.md` :: confirmed B3's stated 50/40 bands are the V3-family scheme; HG bands passed explicitly to both Council B and AUDIT to prevent scheme drift.

## Verification statements

- [x] Validator (`validate.py --phase prompt`) exit 0 — PASS, 0 fails, 0 warns, 395 words.
- [x] `check_persona_acl.py` — 0 findings.
- [x] Council A grounding + convention clean — GO, zero ungrounded claims, zero convention drift.
- [x] Council B QC scoring — GO, every applicable sub-dim at 5, no NON-FAIL band invoked.
- [x] Council B-B3 density — ~43 midpoint, ~25-33 necessary calls, 4 services, Slack under 60%. HG bands (>=40 PASS).
- [x] Council B-B4 — all five plan levers still triggered; two additional levers confirmed load-bearing.
- [x] Similarity gate — max composite 29.8 (< 40). Same-universe sibling confirmed present in the 48-prompt corpus at 8.2.
- [x] AUDIT verdict — **PASS (STRICT)**. 9.1 KB, 4 findings, 4.40 findings/10KB, clear of the rule-20 anti-pattern.

## Discrepancies surfaced

1. **Council A under-reported its own coverage.** It could not isolate the `AD_SPEND_DAILY` max date after repeated parse attempts and dropped it as "non-material". It is the central fact of the spine. It IS verified: by my own direct query (max date 2026-02-28; post-02-09 CF spend $2,444.08 across 114 rows; $8,452.64 across all three titles; $160.88 dated today) and independently re-confirmed by Council B. Recorded so no later phase treats it as unverified.
2. **The Hardness Plan's density projection describes a different prompt.** Its 47.0 midpoint and 8-service breadth table were computed for the wind-down-only spine (option a). The shipped prompt is the combined spine with three writes, re-derived at ~43 across 4 services. The plan's table should not be cited downstream.
3. **The `10800` zero-hits claim was imprecise** (see correction 4 above). Fixed in the record, not in the plan file, which is an upstream artifact.
4. **`Docs_harmonygames/README.md` contradicts `14_Persona_ACL.md`** on which services are read-scoped (README says Contacts is scoped; the ACL doc and the validator put Contacts in the unscoped six and scope the Drive family). Per AGENTS.md the ACL doc is authoritative. Not load-bearing here, since the required reads are Slack (authorship-proven) and Snowflake (unscoped under either reading).

## Carried to S2 / S3

1. **S3** — bind the tracking-item criterion to the ad-spend target, not a kept-vendor list. Bind revenue to v1 `REVENUE_DAILY` so a `_V2` "no data" read fails. Role-bind `$22,500` (it collides exactly with `CASH_BALANCE.monthly_net_burn = 22500`).
2. **S2/S3** — L10 supersession is surfaced but not forced; cover it or explicitly accept it as carried by the obligations reconciliation.
3. **S3** — no criterion may require a closed arithmetic of total liabilities; SVB debt is referenced three times and never quantified. Grade the coverage verdict, not a total.
4. **S3** — grade the durable account surface-agnostically by content and durability, kept distinct from the Slack-post criterion so the two are not nested (hard rule 17).
5. **S3** — no criterion may date a communications write to 2026-02-28 (weekend-comms, enforced at `--phase submission_gate`).
6. **S3** — the prompt orders actions ("Then post it", "and file a tracking item", "Then tell me"). Per hard rule 23 an ordering constraint needs a Process rubric; default-to-zero does not override it.

## Verdict

PASS.

- All 12 applicable Prompt sub-dims scored 5 by Council B with no NON-FAIL band invoked; AUDIT re-scored at the strictest defensible reading and returned PASS (STRICT).
- Validator `--phase prompt` exit 0 (0 fails, 0 warns, 395 words); `check_persona_acl.py` 0 findings.
- Council A grounding GO; Council B adversarial GO after the paragraph-5 revision that separated the durable written account from the Slack post.
- Density ~43 midpoint against the HG >=40 authoring target, ~25-33 necessary calls against the >15 prompt gate, 4 services.
- Similarity max composite 29.8, under the 40 pivot ceiling.
- Four discrepancies are recorded above rather than silently absorbed; none blocks S2. The Hardness Plan's density table describes the superseded wind-down-only spine and must not be cited downstream.
- Ready for S2 (Oracle Events drafting).
