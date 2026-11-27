# Scout's Suggestions: one-pager

## The problem behind the problem

Fake listings are a symptom. On Property Finder a listing is an agent's advert, paid per listing and judged by the leads it brings in, so an advert that gets calls has done its job even when the unit in it is gone, priced differently or belongs to someone else. Nothing in the system knows what a unit is, so the same flat shows up several times at several prices.

In Princess Tower (210 live listings, 27 Nov 2026) at least 16 (8%) are likely misleading. The most common way to mislead was a price far above the building's norm, not a fake bargain: 10 of 118 rentals are holiday-home operators showing monthly, bills-included pricing as a yearly rent, 30 to 50% above registered rents. The platform's own trust signals can't separate them. 92% of listings carry Verified, and so did 7 of the 12 misleading ones. PF's price box told 38 of 47 listings they were cheaper than "similar properties" because it benchmarks against the Dubai Marina average.

So the searcher doesn't really want fewer listings. They want to know which units are real, available and at what real price, and they want someone accountable for that answer. Renters care most about availability and the real yearly price. Buyers care about what that size actually sold for and whether two listings are the same unit.

## Where it lives

On the listing page, in place of the "Property details" block, on web and in the app. Scout gives the facts in two or three chat bubbles, a 0 to 100 Trust Score with plain reasons, and drafted questions for the agent that only go out when the viewer taps Send. The next step is a one-word label on each search-result card (Short list, Not sure, Check this) so people see it before they click.

Reading needs no login. Sending a question does, because the agent's reply has to come back to someone. That login is the handoff: the questions and replies live in the person's Scout thread, so a question asked on the laptop arrives as a push notification on the phone when the agent answers, and the thread opens where it left off. On the web, a "continue on your phone" QR code carries the thread into the app.

## Why use it, and when not to

Searching and calling agents means ringing about units that turn out to be gone, a different flat or a different price. Scout checks the listing against the building and the registered prices before you call, tells you what's wrong in one line, and asks the agent the specific question for you. A renter who'd have taken the Colife 1BR at AED 111,499 a year instead of a normal long let at about 75 to 86k saves AED 25 to 36k.

Call the agent directly when the listing already scores 85+ and you just want to book a viewing, when you know the agent, when you need to see it today, or when you actually want a short, flexible stay (the holiday lets are the right product for you).

## Agents and PF revenue

Honest agents win. Their accurate listing stops losing the first call to a cheaper bait photo, and the enquiry they get arrives with a specific question instead of "Hi, is this available?". Agents who post bait, stale or relabelled listings lose calls, and a flag they don't answer within 48 hours costs them 10 points. Agents can clear a flag by answering it, so the score gives them a reason to fix the listing rather than a penalty they can't do anything about.

PF sells exposure, but agencies buy leads. If Scout makes a lead more likely to turn into a viewing, a credit is worth more, which supports pricing and renewals of Premium and Featured. The cost is a short-term dip in raw enquiry counts on flagged listings, and pushback from holiday-home operators who rely on the yearly feed. Scout never takes a listing down, so PF's inventory count doesn't move.

## Metrics

A portal like PF lives on five numbers: traffic (sessions, app users), visit-to-lead conversion, lead quality (does the agent reply, does it become a viewing), supply (live listings, paying agents) and revenue per agency (credits and upgrades).

| Metric | Expected move | Why | Rough size (my guess) |
|---|---|---|---|
| Leads per visitor | Flat or slightly down | Fewer calls on flagged listings, more on short-listed ones | -3% to +2% |
| Leads that get an agent reply | Up | Specific questions get answers, the 48h rule nudges replies | about 70% to 75% |
| Return visits in 7 days | Up | People come back for agent replies | +5 to 10% |
| Live listings | Flat | Nothing is hidden | 0% |
| Upgrade renewals | Up later | Credits buy better leads | not measurable in a 2-week test |

## Proof metric and the 1% test

The proof number is **answered leads per 100 listing-page visitors**, where answered means the agent replied within 2 hours. It only goes up if people still contact agents and those contacts are better, so it can't be gamed by cutting leads or inflating them.

Test: 1% of Dubai rent and buy listing-page visitors, randomised by user, see Scout's Suggestions instead of Property details for 2 weeks. The other 99% are control. Guard metric: leads per visitor on listings scoring 85+ must not fall.

It's wrong if the treatment group's answered leads per 100 visitors isn't higher than control after 2 weeks, or if total leads fall more than 10% without a rise in the reply rate. In that case Scout is only putting people off, and the thing to try next is the label on search cards without the listing-page block.

## What I couldn't build

| Priority | What | Why it's needed | Why it isn't here |
|---|---|---|---|
| 1 | Registered prices for the whole building and every size | The fairest price check. Asking prices run above what people pay | Data. I only had the 5 transactions PF shows on each listing page |
| 2 | Unit identity (unit number, title deed, Form A) | To merge duplicate adverts into one unit and confirm who holds the mandate | Data. Not on listings; needs DLD or PF's internal records |
| 3 | Real agent messages | The core promise: asking the agent and reporting back | Internal PF connection to WhatsApp and PF Expert. Replies are scripted and labelled |
| 4 | Agent reply history in the score | Agents who never reply should score lower | Internal PF data |
| 5 | Labels on search-result cards | People should see the warning before they click | Engineering time. Only the listing page is built |
| 6 | Looking at the photos themselves | Catch photos from other buildings or lightly edited copies | Engineering and compute cost. Prototype matches identical image files only |
| 7 | Live AI for "Ask Scout anything" | Free-form questions | Engineering time. Answers come from keyword matching |
| 8 | App build and real web-to-app handoff | Most searches happen on phones | Engineering time. Built as a mobile-first web page |
| 9 | Arabic | A large share of searchers | Time |
