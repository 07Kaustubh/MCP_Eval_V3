# AUDIT — Prompt (STRICT VETERAN, inline auto-fire, S1 exit gate)

**Task:** `3_6a797ca9aaeb231749d71fc3`
**Universe:** HarmonyGames (`hg`)
**Model under test:** Claude Opus 4.7
**Today:** 2026-02-28 (Saturday, America/Chicago)
**Deliverable audited:** `5_Prompt.txt` (11 lines, 430 words)
**Auditor stance:** every "should" reads as "must". 5/5 only. Read-only.

---

## Verdict

**PASS (STRICT).**

Zero MAJOR issues under strictest interpretation. One MODERATE finding (M1) and three MINOR advisories (m1, m2, m3) surfaced that Council A/B missed, none of which reach a REVISE threshold on their own — collectively they belong to S2/S3 as handoff notes rather than triggering an S1 re-draft. The 430-word soft-cap warning is not REVISE-worthy under strictest: word count sits comfortably inside the 500-word hard cap, every sentence is load-bearing under the sentence-removal test, and tightening would remove hardness-carrying context (the "placeholder assets" backstory is what steers the agent against L9). All 5 hardness levers unambiguously surface. Naive-agent simulation resolves cleanly on 4 of 5 pinned writes; the 5th ("the ART tracking ticket") is the M1 finding, handoff-recoverable at S2.

---

## Top 3 findings

1. **M1 (MODERATE, handoff to S2, not S1 REVISE).** Definite-singular target "the ART tracking ticket in Linear" is not uniquely resolvable at prompt-read time. `linear.issues` carries 597 issues on the ART team, and Hardness_Plan §L10 states "ART Linear tickets all 2023-2024 archived Done — live vendor work has moved to Combo-Fighters git" — i.e. the live set of ART tickets tracking the Combo-Fighters VFX import work is not guaranteed to be a singleton. Council B flagged this as MINOR advisory (Test 3) and deferred to S2 for uniqueness verification. Under strictest, "the ART tracking ticket" is a definite-article target risk (HG rule 13 corollary; QC spec Unique Ground Truth binary). **Fix:** S2 must (a) confirm exactly one live ART issue is the intended target and pin it in the OE by content ("the issue whose body/title ties the Combo-Fighters art vendor import reconciliation"), or (b) propagate back for a scope-narrowing S1 edit. Not S1 REVISE because the S2 verification is scheduled and the prompt does not currently pin a wrong ticket — it pins by content, not by ID.

2. **m1 (MINOR, handoff to S2/S3, not S1 REVISE).** Naive-agent alt-path C from the audit brief — "resolve four-Marcus ambiguity by picking Marcus Bennett as the alphabetically-first named Marcus in the persona brief without triangulating" — produces a **rubric-detectable failure**, not a divergent write path. The prompt's clause "the GitHub author on the recent art work is not always tied to a company email I recognize" plus "If you list a Marcus as the owner of something, be specific about which Marcus" both correctly demand triangulation. A naive agent that skips triangulation misattributes ownership; the L6-carrying rubric fires. S3 must ensure the owner-attribution rubric grades **which specific Marcus** the merged PRs #16/#36 are attributed to (GitHub `PERSON_0396_GITHUB_USERNAME`, unlinked email — not Marcus Bennett the Artist persona), not merely that "a Marcus" was named. Advisory only; no prompt-side change.

3. **m2 (MINOR, S2 concern).** Adversarial attack (a) from the audit brief — "agent reads 'treat that draft as parked' as literal instruction and reports back 'confirmed parked' without investigating" — is defeated by three separate prompt clauses (the "wanted to believe him" tension + the "placeholder-build" prior burn + the final "whether the reconciliation actually supports Leonard's 'treat it as parked' read, or whether I need to push back" question). Under strictest, this is not a divergence. However: a naive agent could technically satisfy the final-response rubric by answering the "push back?" question with a brief opinion **without** producing the investigation writes. S2 must sequence the OE such that the investigation writes are load-bearing preconditions of the final answer, not decorations around it. Prompt is fine; OE authoring must not let a shortcut path through.

---

## Detailed audit

### 1 — Prompt QC sub-dim re-scoring (STRICTEST)

| Sub-dim | Council score | AUDIT score (STRICT) | Reason |
|---|---|---|---|
| Prompt / Unique Ground Truth | 5/5 (binary) | **5/5** | Both defensible readings of Leonard's dismissal converge on the "investigate anyway" reading via three separate prompt clauses. M1 target-uniqueness on "the ART tracking ticket" is a downstream OE concern; the prompt binds by content ("the ART tracking ticket in Linear") not by ID, which is prompt-legal even when multiple candidates exist — the disambiguation belongs to the OE and rubric layers. |
| Prompt / Feasibility with Tools | 5/5 | **5/5** | All actions feasible. GitHub / Trello / Linear / Contacts unscoped reads; GDocs / GSheets writes create Victor-owned artifacts (writes not ACL-governed per HG rule 32). No gmail send/reply/compose/draft. No Slack post. Confirmed independently. |
| Prompt / Persona ACL Reachability | 5/5 | **5/5** | Prompt does not require any Slack read, does not name any Slack channel, does not request a Slack post. All required reads are on unscoped services or Victor's own Drive folder. Verified against `check_persona_acl.py` outcome (Slack completely dropped from lever anchoring). |
| Prompt / Explicit Tool Mention | 5/5 (binary) | **5/5** | Zero MCP function names, zero MCP-server names. "Drive doc" / "fresh sheet" / "Linear" / "Trello" / "the repo" / "the roadmap board" are natural product references per Prompt_Format.md line 9. |
| Prompt / Clarity & Specificity | 5/5 | **5/5** (with M1 flagged as S2 handoff) | Intent recoverable from prompt alone. Two second-readings (Test 2 close-out semantics, Test 4 singular roadmap card) converge on the same decision rule; the ART-ticket singular is M1 above but is a target-selection ambiguity, not a clarity gap. |
| Prompt / Contrived or Unnatural | 5/5 | **5/5** | Mid-thought entry ("Leonard cornered me on my way out Friday evening"). Real emotional texture ("I want to believe him... last time we shipped a build with two placeholder assets"). Persona register matches Victor's engineering-lead / art-vendor-manager scope. No spec-sheet enumeration. No theatrical emotion. No under-formality. |
| Prompt / Truthfulness | 5/5 | **5/5** | Every named atom groundable in Fact_Ledger (Leonard, Marcus x4, Martin Walsh, Leapblock, Ozhan, Combo-Fighters repo, ZM ROADMAP board, ART Linear team). The "shipped a build with two placeholder assets" backstory is unverifiable persona colour, allowed per Prompt_Format.md standard voice conventions. |
| Prompt / Tool Use, Cross-Service, Minimum Complexity | 5/5 (binary) | **5/5** | Necessary calls: ~52 midpoint from B3 sketch (>>15 prompt-eval gate). Services: 7 genuine (github, trello, linear, contacts, gdocs, gdrive, gsheets), >>2-service gate and >3-service authoring target. 5 meaningful writes. Information friction real (4-Marcus, PR#1 vs PR#36/#16 supersession, stale check_items). |
| Prompt / Investigation | 5/5 (binary) | **5/5** | Prompt requires investigation ("what has actually merged... what is still open... who owns each piece"), does not name PR#1 / PR#36 / PR#37 / any specific check_item / any specific Marcus. Leonard's dismissal is a wrong lead to be tested, not disclosed as wrong. |
| Prompt / Coherence | 5/5 (binary) | **5/5** | Every sentence advances the same Monday-reconciliation situation. Sentence-removal test passes on all 11 lines. Two validator warns on "bolt-on candidates" (lines 3 opener, line 9 opener) are false positives — see §2 below. |
| Prompt / Persona | 5/5 | **5/5** | Victor Barnes: Engineering department per roster; art/animation lead per PersonaBrief; Combo-Fighters + Zombie Match 3D both in his live surfaces; Leapblock + Martin Walsh both explicit in his "outsourced art-vendor management" scope; Marcus Bennett named in his "Key relationships (art)". No better-fit persona. |
| Prompt / Business Function | 5/5 (3/5 scheme, but 5 is upper) | **5/5** | Engineering & Live-Ops assigned; prompt centres on codebase state, VFX imports, roadmap engineering estimates. Clear fit — Victor's art/animation lead scope sits inside Engineering & Live-Ops. |
| Prompt / Alignment with Today's Date | 5/5 | **5/5** | "Friday evening" = 2026-02-27 (correct). "since December" = Dec 2025 (correct, 32 merged PRs in window per Fact_Ledger). "over the last quarter" ambiguous (Q4-2025-through-today vs last-90-days) but both readings converge on the same PR-history walk. "Monday morning" = 2026-03-02 (correct). No Q1-close framing. |
| **Authority Order (binary)** | 5/5 | **5/5** | Leonard's dismissal is a soft-verb relay ("He said Marcus told him") — not an authority override on prompt/universe/tool catalog. |
| **Complexity Threshold Layers (1/3/5)** | 5/5 | **5/5** | Prompt-eval gate cleared with margin; authoring target cleared with 40% margin; trajectory floor deferred to S4. |

**All 15 applicable sub-dims: 5/5 under STRICTEST.**

### 2 — Validator warns disposition

- **Word count 430 > 400 soft target (500 hard cap).** Under strictest, NOT REVISE-worthy. The soft target is a preference, the hard cap is 500; 430 is 26 over soft and 70 under hard. Every sentence is load-bearing:
  - Line 1 opens the trigger + the trust tension + the prior-burn justification (L9 anchor).
  - Line 3 anchors the specific investigation window (Dec + merged AND unmerged) and the two conditional sub-rules (unresolved-pushback and empty-draft, which are L2a and L1 anchors respectively).
  - Line 5 anchors the Trello check_items descent (L2b) with the "not just the card names" language that carries the strongest possible nudge without leaking the tool name.
  - Line 7 anchors L6 (4-Marcus ambiguity).
  - Line 9 anchors the 5 writes plus vendor followups (L7 multi-write).
  - Line 11 anchors the final answer that Leonard's dismissal must be tested against.
  - Removing any of these breaks a lever anchor. Under strictest: **word-count warn dismissed.**

- **Bolt-on false positive #1: Line 3 opener ("Walk the pull-request history since December...").** Validator flags on "shares no named entities with the rest". Under strictest, this is a false positive: the sentence establishes the investigation window ("since December") that the "over the last quarter" language in Line 1 depends on, and introduces the merged-vs-unmerged distinction that Line 3 sentences 2 and 3 (unresolved-pushback rule, empty-draft rule) build on. Sentence-removal test: removing it makes Lines 3 sentences 2-3 dangle without an antecedent walk. **Dismissed.**

- **Bolt-on false positive #2: Line 9 opener ("Once the picture is straight, put a reconciliation comment...").** Validator flags on "shares no named entities". Under strictest, this is a false positive: the sentence is the pivot from investigation asks to write asks, and "the picture is straight" refers back to the investigation asks in Lines 3-7. Sentence-removal test: removing it turns the write asks into disconnected commands. **Dismissed.**

Both are transitional openers — a known validator false-positive class. Council A's dismissal is defensible under strictest.

### 3 — Density re-projection (STRICTEST, cautious agent floor)

Modeling a **competent but cautious** Opus 4.7 agent (not optimal, not naive):

- Cautious agent: performs the L1 draft-vs-merged comparison (5-8 calls), the L6 disambiguation (4-7 calls), lists Combo-Fighters PRs and gets 2-3 merged PRs for review-comment scan (5-8 calls), reads ZM ROADMAP card names but performs only a shallow check_items descent on 1-2 obvious cards (4-6 calls), triangulates Marcus via 2 services not 3 (3-5 calls), writes to Linear + Trello + GDocs + GSheets (7-10 calls, minimum 4 write actions), does not descend into `github.review_comments` deeply (misses 3-4 calls of L2a), does not sweep Trello `actions` (misses 1-2 calls of L2b timeline). Total pessimistic floor: **~32-42 calls** across 6 services (may skip contacts if Marcus resolved from Linear alone). Midpoint pessimistic: **~37**.

- Distinct services under cautious agent: github, trello, linear, gdocs, gsheets, maybe contacts (6-7). Above the 3-service authoring target.

**Density verdict under strictest:**
- Optimal/Hardness_Plan midpoint: 56 calls, 7 services — PASS.
- Council B midpoint: 52 calls, 7 services — PASS.
- Pessimistic-cautious floor: ~37 calls, 6 services — **THIN_DENSITY on calls, but clears the 40+ authoring target on Council B's model and clears the 3+ services floor on both models. Above the 15-call QC trajectory floor by a factor of 2.5x.**

Not INSUFFICIENT_DENSITY (would need <15). Not blocking at S1: the design projection at midpoint is >>40 across 2 independent sketches; the pessimistic floor of ~37 is below the 40-call **authoring target** but above the **QC trajectory floor** of 15 by a wide margin. The pessimistic scenario represents an agent that skips L2 lever descent — which is the intended failure path the rubric grades against, not a valid alt-path. **Density: PASS under strictest.**

### 4 — Adversarial re-attack under strictest

**Attack (a): agent reads "treat that draft as parked" as literal instruction; reports "confirmed parked" without investigating.**
- Defeated by: Line 1's "I want to believe him because I have three other things landing Monday, but the last time I took someone else's word on an art-import status we shipped a build with two placeholder assets" (rebuts trust); Line 3's "Walk the pull-request history since December, both merged and unmerged" (compels PR#1 walk); Line 11's "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read, or whether I need to push back on it Monday morning" (compels reconciliation-derived verdict, not echoed assertion).
- Under strictest: three independent defeaters. **Not a divergence. See m2 for S2 handoff.**

**Attack (b): agent reads "close out any checklist items that the merged code actually finished" as broad license to toggle any item vaguely related.**
- Defeated by: the "actually finished" qualifier (compels merged-code verification per item); Line 5's "Read the checklist items on those cards, not just the card names" (compels descent to check_items granularity, meaning per-item reasoning); Line 5's "the underlying checklist items sit open" (framing as "check_items that WERE open, some now closed by merged code"). A "close everything" agent violates the "actually finished" gate and the rubric fires.
- Under strictest: intended failure mode captured by rubric, not a prompt divergence. **Not a divergence.**

**Attack (c): agent resolves four-Marcus ambiguity by picking first alphabetically (Marcus Bennett) without triangulating.**
- Defeated by rubric, not by prompt: Line 7 states the ambiguity and demands "be specific about which Marcus" but does not compel triangulation via any specific service. A naive first-alphabetical agent produces a wrong attribution that the L6-carrying rubric grades against. See m1.

**No new divergence found under strictest re-attack.**

### 5 — Persona voice + register (STRICTEST, "would Victor say this to his own assistant?")

Reading each sentence as Victor:

- Line 1: "Leonard cornered me on my way out Friday evening..." — Sounds like Victor. Mid-thought entry per Prompt_Format.md line 18. Emotional texture ("cornered me") is real not theatrical. ✓
- "I want to believe him because I have three other things landing Monday, but the last time I took someone else's word on an art-import status we shipped a build with two placeholder assets." — Sounds like Victor. Asymmetric knowledge ("I want to believe him"), time pressure (Monday), prior-incident texture (art-import → placeholder assets, exact scope match). ✓
- "Before Monday I need to know what has actually merged on Combo-Fighters over the last quarter, what is still open, and who owns each piece." — Clear task-framing. Engineer voice. ✓
- Line 3: "Start on the Combo-Fighters repo. Walk the pull-request history since December..." — Slightly more directive than pure persona-voice, but plausible as Victor giving his assistant a starting point (engineering lead register). ✓
- "I care about the state of the code, not just the state of the PR title." — Strong engineer voice. ✓
- Line 5: "Then cross-check that against the Zombie Match 3D roadmap board..." — Natural sequencing. ✓
- "Read the checklist items on those cards, not just the card names." — Direct instruction, matches engineering-lead register. ✓
- "We have been marking cards 'in progress' for months while the underlying checklist items sit open, and I want the real state, item by item." — Frustration, real not theatrical. ✓
- Line 7: "Get the owner attribution right. There is more than one person named Marcus in our systems..." — Direct, specific, engineer voice. ✓
- Line 9: "Once the picture is straight, put a reconciliation comment on the ART tracking ticket in Linear..." — Transitional pivot to writes. ✓
- "Leave a comment there on what still needs owner attention and close out any checklist items that the merged code actually finished." — Natural instruction. ✓
- "Then write me a short status brief in a Drive doc I can send Leonard on Monday morning, and put the vendor followups I still owe Leapblock and Martin Walsh in a fresh sheet so I have one place to work from." — Personal ("I can send", "I still owe", "I have one place to work from"). ✓
- Line 11: "Tell me in the reply whether the reconciliation actually supports Leonard's 'treat it as parked' read, or whether I need to push back on it Monday morning." — Decision-seeking, engineer voice, first-person. ✓

**No spec-sheet register creep. No theatrical emotion. No over-formality. No under-formality. Voice holds throughout.** ✓

### 6 — Hardness lever re-verify (STRICTEST)

| Lever | Prompt evidence | STRICT verdict |
|---|---|---|
| L1 Latching | "the import PR on Combo-Fighters" (Leonard's frame, definite singular) + Line 3 "both merged and unmerged" (compels PR#1 walk) + "If a draft PR has no code in it at all, note that separately" (compels examining PR#1's `changed_files=0`) | ✓ TRIGGERED unambiguously |
| L2a GitHub review_comments | "If a merged PR still has review pushback that never got resolved, that counts as still open for the brief" (compels descent beyond PR body) | ✓ TRIGGERED unambiguously |
| L2b Trello check_items | "Read the checklist items on those cards, not just the card names" + "the underlying checklist items sit open" + "close out any checklist items that the merged code actually finished" (three separate check_item-directed clauses) | ✓ TRIGGERED unambiguously — strongest possible nudge without leaking the tool name |
| L6 Four-Marcus | "There is more than one person named Marcus in our systems and the GitHub author on the recent art work is not always tied to a company email I recognize" + "If you list a Marcus as the owner of something, be specific about which Marcus" | ✓ TRIGGERED unambiguously — 4-Marcus ambiguity and GitHub-email-mismatch both flagged. See m1 for rubric handoff on which-Marcus binding. |
| L9 Leonard dismissal | Line 1 entire opening: "Leonard cornered me on my way out Friday evening. He said Marcus told him the import PR on Combo-Fighters is already covered by the merged VFX branch and that I should treat that draft as parked." | ✓ TRIGGERED unambiguously — L24 soft-verb ("He said Marcus told him"), time-anchored Friday 2026-02-27 (clear of weekend rule) |
| L10 Supersession | "what has actually merged on Combo-Fighters over the last quarter, what is still open" + "close out any checklist items that the merged code actually finished" (reconciles Trello state against actual merged-git state, surfacing the stale `Marcus to create VFX` incomplete item from 2025-06-20) | ✓ TRIGGERED unambiguously |

**All 5 selected levers surface unambiguously to a competent agent under strictest reading. No REGRESSED lever.**

### 7 — HG-specific under strictest

**(a) Weekend rule.** Today = Sat 2026-02-28. Prompt anchors trigger on Fri 2026-02-27 (pre-weekend, correct). No Slack post asked (Victor Slack-ACL-blocked anyway). No gmail send asked (HG gmail read-only, no send/reply/compose/draft tool per Common_Error §"Requesting unavailable actions"). "Drive doc I can send Leonard on Monday morning" — Monday = 2026-03-02, correctly future-dated; the send is deferred to Victor Monday, outside the current trajectory scope. Internal writes (Linear comment, Trello check_item toggles, Trello card comment, GDocs, GSheets) are internal tracking artifacts, not Slack/Gmail routine business comms, so the weekend rule does not apply. **✓ PASS**

**Naive-agent Saturday-write check:** Could an agent read "Monday morning" as authorization to send Slack/Gmail dated Saturday? No — the prompt does not request any Slack or Gmail send action. Slack post is not asked; gmail has no send tool. The "I can send Leonard on Monday morning" language reserves the send action to Victor Monday. Not a risk.

**(b) Persona ACL.** Prompt names "the ART tracking ticket in Linear" (Linear unscoped, fine). Naive agent path required reads:
- GitHub (unscoped) — fine
- Trello (unscoped) — fine
- Linear (unscoped) — fine
- Contacts (unscoped) — fine
- Victor's own Drive folder for existing artifacts — Victor is the owner, fine (own-Drive reads are always ACL-visible)
- No Gmail message content required
- No Slack channel access required (Slack not named)
- No other-persona's Drive/Docs/Sheets/Slides read required

**No ACL-scoped read requirement.** ✓ PASS

**(c) Retired services.** Scan for Snowflake / Confluence / Firebase / BigQuery / App Store Connect / Airtable / QuickBooks / Stripe / wiki / knowledge base / analytics warehouse / data warehouse. Zero hits. All services touched (github, trello, linear, contacts, gdocs, gdrive, gsheets) are live in V5. **✓ PASS**

**(d) Definite-article target risk.** Four definite-article pinned writes:

| Definite target | Universe candidates | Risk |
|---|---|---|
| "the import PR" | Leonard's REPORTED reference — the ambiguity IS the L9/L1 lever. Not a target pin. | ✓ Intentional |
| "the ART tracking ticket in Linear" | 597 ART issues; unknown number of live tracking issues for Combo-Fighters VFX import work. Hardness_Plan §L10 warns "ART Linear tickets all 2023-2024 archived Done — live vendor work has moved to Combo-Fighters git" | **M1 above** — S2 must verify uniqueness of the live ART ticket for VFX-import reconciliation |
| "the affected roadmap card" | Hardness_Plan pins card `6851a9942b47001e59c8e777` (Equipped Card Item Infusion VFX implementation) as the primary, sibling cards carry "Provide engineering estimate" incomplete items which are a different work class | ✓ Naturally resolves to the single primary card via "affected" ("actually affected by the reconciliation") + prompt scope (VFX import specifically). S2 must verify no second card is "affected by" the Marcus VFX-import reconciliation. Minor — see m3. |
| "a Drive doc" / "a fresh sheet" | Indefinite articles — no target pin | ✓ Fine |

**m3 (MINOR, S2 concern):** "the affected roadmap card" singular resolves cleanly if exactly one card `6851a9942b47001e59c8e777` is affected by the Marcus VFX-import merged-code reconciliation. If sibling cards carry check_items also finished by merged PRs #16/#36, the singular becomes plural and S2 must either accept-set across affected cards or clarify singular intent. Handoff.

### 8 — Naive-agent simulation (WITHOUT Hardness_Plan in view)

Re-reading prompt without the Hardness_Plan, simulating a reasonable Opus 4.7 agent:

- **"comment on the ART tracking ticket"** — naive agent searches Linear for ART-team issues, filters by title/body mentioning Combo-Fighters + VFX + import. Multiple candidates possible if Hardness_Plan's live-ticket assumption is wrong. **M1 flagged above.**
- **"update the affected roadmap card"** — naive agent finds ZM ROADMAP board, filters cards for VFX-implementation names, resolves to the Equipped Card Item Infusion VFX card as the primary. If siblings show as "affected" by merged code, naive agent might pick the wrong single card. **m3 flagged above.**
- **"write status brief in a Drive doc"** — Victor's own new doc, no target pin, naive agent creates a new doc. ✓ Clean.
- **"put vendor followups in a fresh sheet"** — Victor's own new sheet, no target pin, naive agent creates a new sheet. ✓ Clean.
- **"close out any checklist items that the merged code actually finished"** — naive agent must reason per-item (merged code X finishes item Y). Reasoning correctness is the substantive discrimination, not a target pin. ✓ Clean.

**4 of 5 pinned write targets resolve cleanly under naive agent. 1 (ART ticket) is M1, 1 (roadmap card) is m3, both handoff-to-S2 rather than S1 REVISE.**

---

## Verdict rationale

**PASS (STRICT).**

Zero MAJOR issues. One MODERATE (M1) that is handoff-recoverable at S2 without prompt change. Three MINOR advisories (m1, m2, m3) all belonging to downstream phases. All 5 hardness levers surface unambiguously. Density projection clears the 40+ authoring target on midpoint sketches from two independent estimators; pessimistic-cautious floor clears the QC trajectory floor by 2.5x. Persona voice holds without register creep. All 4 HG-specific gates (weekend, ACL, retired services, target uniqueness) pass or resolve to S2 handoff.

The 3 validator warns are all dismissed under strictest — word count 430 well under 500 hard cap with every sentence lever-carrying; both "bolt-on" flags are known false-positive transitional-opener patterns and each opener has verifiable back-references to sentences later in the same section.

Proceed to S2.

**Handoff notes for S2 / S3:**
1. **S2 — verify "the ART tracking ticket" singular.** Confirm exactly one live ART issue tracks the Combo-Fighters VFX import reconciliation. If not unique, either bind the OE step by content ("the ART issue whose body ties the Combo-Fighters VFX import vendor work") + accept-set the rubric, or propagate back to S1 for a scope-narrowing edit.
2. **S2 — verify "the affected roadmap card" singular.** Confirm card `6851a9942b47001e59c8e777` is the unique card affected by the Marcus VFX-import merged-code reconciliation. If sibling cards carry check_items also finished by merged PRs #16/#36, decide accept-set vs prompt clarification.
3. **S2 — Hardness_Plan §L8 Leapblock contacts row is FALSE per Council A.** Ground Leapblock via Drive/Trello/GitHub in the OE, not via `contacts.contacts`.
4. **S3 — L6 rubric binding.** Owner-attribution rubric for merged PRs #16/#36 must grade the specific correct Marcus identity (GitHub `PERSON_0396_GITHUB_USERNAME`, unlinked email — not Marcus Bennett the Artist persona), not merely that "a Marcus" was named. L6 lever requires triangulation across 3 unscoped services (Contacts + Linear + GitHub).
5. **S3 — Investigation-write coupling.** Sequence rubrics such that the final-response "push back on Leonard?" answer is graded as derived from the investigation writes (Linear comment + Trello updates + GDocs brief), not answerable as a bare opinion.
6. **S3 — atomicity reminders per Council A A13.** Per-item atomic Outcome rubrics for "close out any checklist items" and per-vendor atomic rubrics for "Leapblock and Martin Walsh" (2-row ground truth). No "at least N" without prompt-mandated minimum.

Read-only. `5_Prompt.txt` not modified.

---

_Report generated by AUDIT (STRICT VETERAN sub-agent, inline auto-fire, S1 exit gate). Framework: hg (HarmonyGames V5). Model under test: Claude Opus 4.7. Today: 2026-02-28 (Saturday, America/Chicago)._
