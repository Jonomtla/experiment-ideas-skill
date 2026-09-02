# Research playbook (what Impact Conversion runs before testing)

Use this when the intake shows a data gap. Recommend the specific research, not "do some research". Each item: what it is, how IC runs it, what it unlocks, effort.

## 1. Analytics funnel read (GA4) — first, always
Pull 6-12 months: sessions → product page → add to cart → checkout start → purchase, split by device, market, channel, landing page and product. Score each step against D2C benchmarks (PDP→ATC 8-12%, ATC→checkout roughly 40-50%, checkout completion 45-60%) and put a dollar figure on each gap (traffic at the step × shortfall × AOV). Check tracking first: duplicate tags, missing purchase events and bot traffic all fake a funnel. Unlocks: which page to test first and how big the prize is. Effort: half a day if GA4 is clean.

## 2. Post-purchase survey (on the order confirmation page) — cheapest, highest signal
Two questions, one at a time, open text:
- "What was the one thing that almost stopped you from purchasing today?"
- "What persuaded you to purchase today?"
Run until 100+ responses. Categorise every answer into 1-3 themes with an intensity score (1 mild, 2 moderate, 3 deal-breaker); "nothing" is a real answer; "other" under 10%. Unlocks: the real objections and the real reasons to buy, in customer words, for copy and for picking the lever (price → motivation, fit → clarity, trust → proof). Effort: an hour to set up (Hotjar, Fairing, Zigpoll, KnoCommerce), two to four weeks to fill.

## 3. Customer email survey (existing customers)
Email invite: "I'd like your help", 5 minutes, draw for three $50 vouchers, "be brutally honest, we can take it". Questions (open text unless stated): how did you first hear about us; what were you trying to solve; what else did you consider; what nearly stopped you buying; what convinced you; what would have made the decision easier; what frustrated you most on the site; what do you like most about the product; what would you tell a friend. Aim for 200+ responses. Unlocks: triggers, fears, competitors, language for headlines and best-for labels. Effort: a day to build and send, two weeks to collect, a day to analyse.

## 4. Non-purchaser survey (people who visited or added to cart but did not buy)
Same invite, sent to abandoned-cart and newsletter-only lists. Questions: what were you looking for; what stopped you; did you buy elsewhere and why; what would bring you back; what was confusing. Clean out existing customers who got the wrong survey. Unlocks: the objections converters never mention (sizing, shipping cost, delivery time, doubt about fit). Effort: same as above; responses are fewer, 80-100 is fine.

## 5. On-site surveys (Hotjar / Clarity / Zigpoll)
- Homepage intent, exit intent or after 30 seconds on mobile: "What was the purpose of your visit today?"; "Were you able to complete it?" yes/no; if no, "Why not?"; if yes, "What do you value most about our site?". Unlocks: commercial vs browse mindset split, and what the homepage fails to route.
- Product page, exit intent on desktop and at average engagement time on mobile: "What appeals to you most about this product?"; "What, if anything, holds you back from buying?"; "What could we do to make the decision easier?". Unlocks: the PDP objection list.
Effort: an hour each; run two to three weeks.

## 6. Heatmaps, scrollmaps and session recordings (Microsoft Clarity is free)
Look for: scroll depth on the PDP (is the price, the CTA, the proof seen?), rage clicks and dead clicks (things that look clickable), where mobile users stall, what people click first on the homepage, filters used vs ignored. Watch 20-30 recordings of sessions that reached checkout but did not buy. Rule: low clicks on a nav link does not mean low value (the link advertises the page to people who never click). Unlocks: layout and friction problems no survey will name. Effort: a day to review once it has run two weeks.

## 7. Review and support-ticket mining
Export reviews (own site, Amazon, Trustpilot) and the last 3-6 months of support tickets. Tag by theme: what people praise in their own words, what they complain about, the questions asked before buying, the reasons for returns. Count them. Unlocks: proof that argues (quotes that answer the top objection), the FAQ that belongs on the PDP, sizing and fit problems. Effort: half a day with an LLM tagging pass.

## 8. Moderated or unmoderated user testing (PlaybookUX, UserTesting; 5-6 participants from the target audience)
Script: search Google for the type of product and say what you learn; open the site, do not scroll, say what it is and who it is for and what questions spring to mind; think aloud about what you would need to know to choose the right product, then explore and say which questions were not answered; is there any reason you would hesitate to buy; what is missing from the experience. Unlocks: the "confident but wrong" problem (people who think they chose correctly and did not), the comprehension gaps that passive labels fix. Effort: a day to script and recruit, a day to watch and note.

## 9. Heuristic walk (the seven levels: relevance, trust, orientation, stimulance, security, convenience, confirmation)
Walk the funnel on mobile as a first-time visitor against each level. Cheap, subjective, useful only to generate hypotheses to check with the data above.

## 10. Competitor and category teardown
The three stores a customer would compare against: their offer, shipping promise, guarantee, proof, pricing presentation. Unlocks: table stakes you are missing and claims you can make that they cannot.

## Priority when they have nothing
1 (funnel) and 2 (post-purchase survey) first, together, this week. Then 6 (Clarity, free, start it running now). Then 3 or 4 depending on whether the problem is winning new buyers or converting interested ones. 7 any time. 8 when the data says comprehension is the issue. Do not wait for all of it before the first test: a funnel read plus 100 post-purchase answers is enough to pick the first three experiments.
