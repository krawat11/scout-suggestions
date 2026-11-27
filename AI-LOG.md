# AI-LOG

## 1. "This 1BR is 18% below market, so it's bait"

Listing 149564147, a 923 sqft 1BR at AED 69,899 a year. Claude compared it with the tower's median asking price and called it bait.

What was true: the five registered 2026 rents for that exact size were 80k, 73k, 72k, 78k and 70k. The median is 73,000, so the listing is only 4% below what people actually pay. Asking prices in this building run well above registered rents.

How I caught it: the listing page shows registered transactions for the same size, and I checked the price against those instead of other adverts. This is why the rules use registered prices as a second yardstick and treat "cheap" as a weak signal (5 points).


## 2. "The four 6,147 sqft penthouses are one unit listed by four agencies"

Same size, same building, so Claude assumed one unit.

What was true: two listings at AED 14.95M describe 3 beds plus a cinema and office in a renovated half floor. Two at 9.5M describe a 5-bed corner unit. More likely two units, each listed twice. Without unit numbers it can't be settled.

How I caught it: I read the descriptions side by side instead of trusting the size match.

## 3. "14 listings are on the 97th floor"

Claude's floor extraction pulled "97" from the listing text.

What was true: the number came from boilerplate about the building's 97th-floor residents' lounge. No listing states a unit on floor 97. Almost no listing states a floor at all, which is a finding in itself.

How I caught it: 14 units on one floor of a 101-floor tower was too many. The text around each match was the same sentence.

