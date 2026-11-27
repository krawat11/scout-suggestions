# Rules

How the assistant scores a listing and what it tells the viewer.

## 1. Principle

The assistant advises. It does not act. It labels listings, explains its reasoning, and answers questions with prices, photos and documents. It never hides, removes or likes a listing, and it only contacts an agent when the viewer asks it to.

## 2. Trust Score

Each listing starts at 100. Points are deducted for each red flag found. The weights come from the Princess Tower audit: flags that appeared most often on misleading listings carry the largest deductions.

| Score | Label | What the viewer sees |
|---|---|---|
| 85 to 100 | Short list | Why the listing passed, with a suggestion to confirm availability. |
| 51 to 84 | Not sure | The open questions, and a drafted message to the agent. It is sent only if the viewer taps Send. |
| 0 to 50 | Likely misleading | A warning on the listing giving the reason. The listing stays in the results. |

Three conditions apply on top of the score:

- A listing is only labelled Likely misleading if at least one strong flag (flags a to e below) applies.
- If the price can't be checked (fewer than 5 comparable listings and no registered prices), the listing can't be short-listed.
- Verified and SuperAgent badges earn no points. 92% of listings in the building carry one, and so did 7 of the 12 misleading listings.

## 3. Flags

| | Flag | Deduction | Can be wrong when | Who it hurts |
|---|---|---|---|---|
| a | Photos match a different unit | 40 | One agent owns two identical units and photographed only one of them | Honest agent |
| b | Price more than 25% above the building median | 30 | The unit is genuinely premium (high floor, Palm view, upgraded) | Honest agent; a searcher who wanted that unit |
| c | Holiday let listed as a yearly rental (rent only) | 30 | The searcher wants a short, flexible stay | Searcher. The label says "holiday let", not "fake" |
| d | Price more than 25% above registered prices for that size | 20 | The registered sample is small, or cheap renewals pull it down | Honest agent |
| e | No DLD permit or Verified badge | 20 | The permit exists but isn't displayed yet | Honest agent, often at a small agency |
| f | Listing contradicts itself | 20 | It's a typo from an unedited template | Honest agent |
| g | Description copied from another unit | 15 | The agency uses one template for every listing | Honest agent |
| h | Price ends in 899, 999, 888 or 499 | 5 | Nearly always. It's a pricing habit | No one; 5 points alone never changes the label |
| i | On the market more than 90 days (rent) or 180 days (sale) | 5 | The market is slow, or the landlord is picky | Honest landlord |
| j | Availability date more than 60 days in the past | 5 | The agent never updated the date | Honest agent |
| k | Price more than 15% below the median | 5 | It's a real motivated seller | Searcher, who may miss a real deal |
| l | Flag k combined with a or g | 10 extra | It's a real bargain, written up lazily | Searcher |

Flag f was marked by hand in the audit. In the product, the AI reads the listing text to find it.

## 4. When the assistant isn't sure

The assistant drafts one question for each flag. Nothing is sent until the viewer approves it.

| Flag | Drafted question |
|---|---|
| b, d | Rent: "Is AED X the full yearly price, and how many cheques?" Sale: "What is the title-deed size and the last sale price?" |
| c | "Is this a 12-month Ejari tenancy?" |
| a | "Can you send photos of this exact unit, and which floor is it on?" |
| f, g | It asks about the specific mismatch, or "Which floor and view?" |
| i, j | "Is it available now, and from what date?" |

The agent's reply changes the score:

- If the agent clears a flag, its points are restored.
- If the agent confirms the problem, the warning quotes the agent's reply.
- If there's no reply within 48 hours, 10 points are deducted.

## 5. Rent vs sale

| | Rent | Sale |
|---|---|---|
| Flag c | Applies | Doesn't apply |
| Flag i threshold | 90 days | 180 days |
| Same unit listed more than once | The viewer is told it's the same unit, and whether it's also for sale | The viewer is told it's the same unit, and a question asking who holds the mandate (Form A) is drafted |

## 6. Test against the audit

I ran the rules over the 47 listings opened in the audit.

| Audit verdict | Likely misleading | Not sure | Short list |
|---|---|---|---|
| Likely misleading (12) | 11 | 1 | 0 |
| Suspicious (19) | 2 | 17 | 0 |
| Looked fine (16) | 1 | 1 | 14 |

42 of 47 match the audit, and no misleading or suspicious listing reached the short list.

Four of the five mismatches were stricter than the audit. The worst is listing 176035779, an honest 2BR priced 34% above the median, which was labelled Likely misleading. The fifth, listing 114610923, was more lenient: a misleading 3BR with an unusual size came out as Not sure.

Some of these flags shaped the audit verdicts in the first place, so the real test is a building that wasn't audited by hand.

The scripts that reproduce this test are `rules/flags.py` and `rules/score.py`.
