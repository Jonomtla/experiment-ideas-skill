---
name: experiment-ideas
description: Turn a store's research (analytics funnel, surveys, heatmaps/Clarity, reviews, support tickets, past tests) into a prioritised list of CRO experiments drawn from the IC Experiment Library. Two modes: IC client mode (`/experiment-ideas {client}`) pulls the client's own files; guided mode (`/experiment-ideas`) interviews the user about what data they have. Portable: works from the bundled library snapshot when the IC repo is not present.
trigger: /experiment-ideas
---

# Experiment Ideas

Give a store the ten experiments most worth running next, each backed by the library's evidence, ranked, and written as a brief that can go straight to a developer. The library proposes solutions; the store's own research decides which problem deserves one. Never recommend an idea whose preconditions the data does not show.

Run as `/experiment-ideas {client}` (IC) or `/experiment-ideas` (guided).

## Library

- Live: `~/Claude/resources/experiment-library/ideas.json` + `evidence.json` (IC machine). Read `README.md` there first.
- Portable: `library/library.json` inside this skill folder (shareable snapshot; no client notes, no GoodUI rows). Rebuild with `python3 scripts/export_shareable.py` before handing the skill to someone else.
- Query helper: `python3 scripts/query.py --page pdp,cart --lever friction --industry consumables --min-grade B --effort low,medium --top 25`. It picks the live library when present, otherwise the snapshot.

Grades: A+ replicated, A one clean win with numbers, B thin or single-source, C directional, none = untested. D (net losing) is never recommended; it is what the library says NOT to do.

## Mode 1: IC client (`/experiment-ideas steadyrack`)

1. Read `~/Claude/clients/{client}/STATE-OF-PLAY.md`, the client research summary (`~/Documents/Obsidian Vault/Impact Conversion/Clients/{Client}/Key Findings.md` and `Overview.md`), and the client's run history: every run in `~/Claude/resources/learnings-library/test-record.json` with that client, plus live tests via Intelligems (search_experiments, status started) so nothing running or already tested is proposed again.
2. Build the exclusion list: idea_ids already run for this client (any verdict), ideas currently running, and every grade-D idea. Add ideas the client has explicitly parked (STATE-OF-PLAY says so).
3. Go to Diagnose.

## Mode 2: Guided (no client folder)

Ask these, one block at a time, and wait. Accept pasted text, CSV, screenshots, or "don't have it".

1. **The store.** URL, platform, what it sells, AOV, rough monthly sessions and orders, the one metric they want to move (CVR, RPV, AOV), anything they are not allowed to change (price, nav, checkout).
2. **Analytics funnel.** Sessions to PDP, PDP to add-to-cart, ATC to checkout, checkout to purchase, split by device if they have it. Where is the biggest drop vs typical D2C benchmarks (PDP→ATC 8-12%, ATC→checkout about 40-50%, checkout completion 45-60%)?
3. **Voice of customer.** Post-purchase survey ("what nearly stopped you"), non-buyer or exit survey, reviews, support tickets, returns reasons. Ask for the top three stated objections and the top three stated reasons to buy, in the customers' words.
4. **Behaviour.** Heatmaps, scrollmaps, session recordings (Clarity, Hotjar): rage clicks, dead clicks, scroll depth on PDP, what people click first, where they stall.
5. **Past tests.** Anything tested before, with results. Anything hard-coded recently.
6. **Ops facts** that gate ideas: real shipping threshold vs AOV, real dispatch time, returns window, warranty, installment provider, subscription offer, stock accuracy.

Map answers onto: `industry_fit` (consumables, high_consideration, apparel_fit, multi_sku_catalogue, single_hero_product, subscription, high_return_risk, or all_d2c), the weakest funnel step (→ page_type), and the dominant lever (objections about price → motivation; "which one is right for me" → clarity; effort or trust complaints → friction or trust).

## Research gaps (both modes, after intake)

Compare what they have against `research-playbook.md` (the research IC runs per client). For every gap, recommend the specific study: what to run, the exact questions or script from the playbook, what it would unlock for this store, and the effort. Rank the gaps by what would change the experiment list most: a store with no funnel read and no post-purchase survey gets those two first, this week, with Clarity switched on in the background. Say plainly which recommendations below are weaker because a gap exists ("this ranking assumes price is the objection; the post-purchase survey would confirm or kill that"). Do not block the experiment list on the research: a funnel read plus 100 post-purchase answers is enough to pick the first three tests.

## Diagnose (both modes)

Write a short diagnosis before touching the library: three to five problems, each tied to a data point ("78% abandon between ATC and checkout"; "34% say price nearly stopped them"; "0 of 4 user testers picked the right size"). Rank problems by revenue at stake (traffic at that step × drop × AOV). This is the part the library cannot do.

## Map

For each problem, query the library: page_type = the step, lever = the mechanism the data points at, industry_fit = the store, min grade B unless the data is strong enough to justify an untested idea, exclusions applied. Read `run_when` and `do_not_run_when` on every candidate and drop any whose precondition the store does not meet (no installment provider → no installment ideas; threshold far above AOV → no threshold nudges; Sport Chek lost 15% that way).

Check the evidence, not just the grade: how many wins, how many losses, median win lift, and whether the wins were on a comparable store type. Prefer ideas with a loss on record you can explain over ideas with no record at all.

## Output

A markdown report (and, in IC mode, Trello-ready briefs):

1. **Diagnosis** (the ranked problems with their data points).
2. **Top 10 experiments**, ranked. For each: title, page, plain-English change, hypothesis (If / then / because), primary metric and guardrails, effort, risk, evidence line ("A+ · 20 wins / 3 losses · median +6.2% · Blend, GoodUI, IC"), the data point that triggered it, what would make it a no-go, and a one-line sequencing note (do not run two tests on the same surface at once).
3. **Do not run** list: grade-D ideas relevant to the diagnosis, and ideas whose preconditions fail here, with the reason.
4. **Research to run next**: from the gap analysis, the two or three studies that would most change this list, with the playbook questions and a timeline.

Rules: numbers verbatim from the library, never rounded up; third-party results are benchmarks, never presented as your own; no em dashes; no fabricated urgency ideas; click-through is never a primary metric. In IC mode, hand the chosen brief to `/test-brief`.
