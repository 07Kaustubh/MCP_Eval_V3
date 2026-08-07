# Prompt design — `2_6a6beba55996ad2ada369b15` (S1)

Universe **harmonygames** · framework `hg` · persona **Robert**, Co-Founder & Creative Director · business function **Executive** · universe today **2026-02-28** (Saturday, month-end, mid-Q1) · model under test **Claude Opus 4.7** · injection: **none** (`4_Changelog.json` = `[]`)

## The spine, and why it is one situation rather than two

The Hardness Plan escalated an unresolved fork to the operator: (a) wind-down spine, (b) Combo Fighter post-mortem, (c) combined. The operator chose **(c)**.

(c) is the highest-risk option, because Coherence is a **binary** QC sub-dim: a bolt-on is an outright FAIL with no partial band. So the combined spine only survives if the post-mortem and the wind-down are genuinely one problem rather than two asks stapled together.

My first candidate for that unifying link was **false**, and discarding it is the most important decision in this phase. I hypothesised that the data being licensed *was* the Combo Fighter performance data, which would have made the post-mortem and the deal the same asset. The universe refutes it: at ts `1770858442.063329` Leonard says the export is for "giving us quote on much much our company data is worth for ai labs", and the inventory being valued is Slack messages (~220K in 365 days), Figma files (1 project, 21 files), Google, GitHub and Analytics. Building the prompt on that link would have been a Truthfulness defect of exactly the kind `9_Common_Error.md` ranks at 4/12.

The link that **does** hold is in the data:

- Combo Fighter earned **$0.00** across all **72** rows of `ANALYTICS.MONETIZATION.REVENUE_DAILY`, over 2026-01-05 to 2026-02-09, while DAU grew from ~22 to ~420 per platform with D1 retention at 37-46%.
- `ANALYTICS.MARKETING.AD_SPEND_DAILY` carries Combo Fighter rows through **2026-02-28**, nineteen days past the shutdown decision. **$2,444.08** on Combo Fighter post-decision, **$8,452.64** across all three titles, **$160.88 dated today**.
- `FINANCE.EXPENSES.CASH_BALANCE` at month-end 2026-02-28: **$2,500** cash, **0.1** months runway.

The still-running acquisition spend is simultaneously (i) the closing fact of the Combo Fighter post-mortem and (ii) a live cash leak against a wind-down that is already at $2,500 with the founders personally liable as board members (ts `1770674426.735229`). One fact, both halves. That is the spine, and every paragraph of the prompt serves it.

The deliverable is a single honest account for the angel conversations Leonard still owes (ts `1770934638.035469`). An angel account is incomplete without both what happened to the product and where the money landed, which is what makes the two components necessary rather than adjacent.

## Levers engineered in

| Lever | How the prompt opens the door, without pre-solving |
|---|---|
| **L11 net-vs-gross** | "I know roughly what we are getting for the data and I know who we still owe, but I don't have a straight answer on whether that genuinely covers shutting down" plus "a number around in my head that I am no longer confident in". The $10,800 net has **zero** universe hits, verified; the only stated figure is the $22,500 gross. |
| **L2 structured-source skip** | Strengthened by the combined spine. The post-mortem gives the agent a legitimate reason to open Snowflake for `GAME_EVENTS`, which primes the Snowflake-as-analytics misread and makes failing to enumerate `FINANCE.EXPENSES` a sharper miss than if Snowflake were never opened at all. |
| **L8 multi-link chain** | "whether that genuinely covers shutting down in an orderly way" forces Slack gross to derived net to Snowflake cash on hand to named open obligations. |
| **L10 supersession** | "I know roughly what we are getting" is surfaced but, per Council B, **not forced**. Carried to S2/S3 as an explicit binding instruction. |
| **L7 multi-write** | Three writes across three services: a durable written account, a post to Leonard and Arthur in the wind-down channel, a tracking item. All internal, because Gmail here cannot send. |

**Two levers found during drafting that the Hardness Plan does not contain**, both confirmed load-bearing by Council B:

1. **The $0.00-against-growth latch.** A run that reads DAU sees a 17.4x growth story and may conclude the shutdown was premature. Only revenue reveals the game never monetised. This is `4_Prompt_Hard_Tips.md:35` first-framing latch, in the data rather than in prose.
2. **The `_V2` decoy.** `REVENUE_DAILY_V2` and `UA_SPEND_UNIFIED_V2` carry **zero** Combo Fighter rows while `REVENUE_DAILY` and `AD_SPEND_DAILY` carry 72 and 330. A run reaching for the newer-looking table concludes no Combo Fighter data exists at all.

## What the prompt deliberately withholds

The net figure; that $22,500 is gross or insufficient; that revenue was zero; that acquisition spend is still running; the words Snowflake, cash balance, runway, burn, ad spend and campaign; the sale-to-licence restructure; the final vendor keep/cancel list.

## Constraints honoured

- **Gmail cannot send.** All three writes are internal. The ad networks are not callable services, so "whatever is still taking money from us" is satisfiable by naming it with a figure and an owner, never by the agent switching off external spend.
- **No Combo Fighter level or cohort data exists.** `LEVEL_PERFORMANCE` and `USER_COHORT_RETENTION` carry zero rows for that title, which is a trap precisely because difficulty curves are Robert's domain. Nothing in the prompt implies they exist.
- **Date coherence.** "the ninth" resolves to the 02-09 decision. No weekday deadline, no "Q1 close" framing (Q1 runs to March 31). The ~15-day gap between the last Slack message and today is handled as "where did this land", never as fresh news.
- **The January campaign pause is not load-bearing.** ts `1768166394.438899` records "ok, campaigns are paused" but spend does not dip; it is confined to January and superseded by restart discussion on 01-22, 01-24 and 02-06. Nothing depends on it.

## Gate results

| Gate | Result |
|---|---|
| `validate.py --phase prompt` | PASS, 0 fails / 0 warns, 395 words, no em-dash or en-dash |
| `check_persona_acl.py` | 0 findings |
| `calc_similarity.py` | max composite **29.8** (< 40). Top match `QC_Tasks/V3_Tasks/Task14` at 30.0 raw. Same-universe sibling `Generated_Tasks/1_...aea` confirmed present in the 48-prompt corpus at composite **8.2** (raw lexical 32.7, the highest raw in the corpus, weighted down 0.252 by differing business function, persona and universe hash) |
| Council A — grounding | **GO** (1 MINOR, A7b) |
| Council B — adversarial QC | **GO** after revision |
| Council B-B3 density | **~43 midpoint**, ~25-33 necessary calls, **4** genuine services, Slack under the 60% ceiling. HG bands: >=40 PASS |
| Council B-B4 lever preservation | all five plan levers still triggered; two new levers confirmed load-bearing |
| **AUDIT (strict veteran)** | **PASS (STRICT)**. 9.1 KB, 4 findings, 4.40 findings/10KB. All six attacked thin points held under the strictest defensible HG reading |

### AUDIT's correction to the Hardness Plan

AUDIT's answer-leakage sweep returned **5 hits on `10800`**, contradicting the plan's and Council B's claim of zero. It ran them down rather than trusting the plan: every hit is a coordinate integer (`X: -0.1080000251531601`) in a puzzle-layout file, or an ID string (`SES-1080...`, `INS-0010800`) in the Snowflake blob. **Zero are currency-formatted.** L11 is clean, but the plan's "zero hits" claim was imprecise and would have concealed a real answer leak had any hit been money. Recorded rather than silently accepted.

AUDIT also found a **stronger disambiguator for Unique Ground Truth** than either council: the prompt requires the target be "named with a figure against it", and the kept vendors (Deel, gusto, Intuit, Linear) carry no derivable per-vendor dollar figure anywhere in the universe (`MONTHLY_BURN` is categorised, not per-vendor), while the ad-spend leak does. Two independent universe-grounded disambiguators converge on one target, which is what closes the crux both councils had left at MINOR.

## The one revision made during this pass

Council B's first pass counted only **two** writes and projected ~40 midpoint with zero margin, flagging `PROPAGATE TO S2`. The cause was a real defect in my draft: "Pull it together as one honest account I can hand to Leonard for those calls. Post it to him and Arthur..." let the account collapse into the Slack post.

I tightened the prompt rather than lowering the projection, since lowering it would have shipped a task designed to sit exactly on its own floor. Paragraph 5 now reads "Write it up as one honest account I can hand to Leonard for those calls, somewhere it will outlast our accounts going dark. Then post it to him and Arthur in the wind down channel, and file a tracking item...".

The new clause is grounded, not decorative: Leonard's 02-12 action list (ts `1770933903.645709`) says "archieve account on google after Feb 15" and keeps data-bearing accounts "until the data is extracted", Slack is being dropped to the free tier with no history, and Figma lapses at renewal. Because Slack is itself named among the surfaces losing history, it cannot satisfy the durability clause, which is what closes the collapse reading. Both councils re-verified this independently and re-returned GO; density moved to ~43 across 4 services.

## Carried to S2 / S3

1. **S3** — bind the tracking-item criterion to the ad-spend target, not to a kept-vendor list. Bind revenue to v1 `REVENUE_DAILY` so a `_V2` "no data" read fails. **Role-bind `$22,500`**: it collides exactly with `CASH_BALANCE.monthly_net_burn = 22500`, so grading it as a bare token mis-grades.
2. **S2/S3** — L10 supersession is surfaced but not forced; cover it or explicitly accept it as carried by the obligations reconciliation.
3. **S3** — grade the durable account surface-agnostically by content and durability, kept distinct from the Slack-post criterion so the two criteria are not nested (this is the hard-rule-17 dependent/antecedent trap).
4. **S3** — no criterion may date a communications write to 2026-02-28 (weekend-comms, enforced at `--phase submission_gate`).
5. **S3** — the prompt orders actions ("Then post it", "and file a tracking item", "Then tell me"). Per hard rule 23, an ordering constraint needs a Process rubric; default-to-zero does not override it.
