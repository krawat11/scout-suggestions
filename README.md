# Scout's Suggestions

A mobile-first clickable prototype of a search assistant inside Property Finder. It checks a listing against the rest of the building and registered prices, says in plain words how far to trust it, and drafts questions for the agent that the viewer chooses to send. It advises and never acts: nothing is hidden, and nothing goes to an agent until the viewer taps Send.

Built on a hand audit of Princess Tower, Dubai Marina (210 live listings, 27 Nov 2026).

## How to run

No build step. Open `site/index.html` in a browser, or run `python3 -m http.server` inside `site/` and open http://localhost:8000 at phone width.

To re-run the scoring test: `python3 rules/flags.py && python3 rules/score.py` (42 of 47 listings match the audit verdicts).

## Demo path

1. "I'm renting", open the 3BR (114610923). Tap "Ask: is it available now…", then Send. The simulated reply clears two flags and the score goes from 60 to 85, Short list.
2. Open the 1BR (163244904). Ask "Is this a 12-month Ejari tenancy?" The reply confirms it's a holiday let, and the warning now quotes the agent.
3. "I'm buying", open the 2BR (165059354). Compare its photos with listing 175131725 (identical files), then ask the agent about the floor.

## Real vs mocked

| Real | Mocked |
|---|---|
| Listing photos, prices, sizes, text, agent and agency names from propertyfinder.ae | Agent replies, scripted and labelled "simulated reply" |
| Registered rents and sales shown on each PF listing page | Score changes after a reply (they follow RULES.md, but the reply is scripted) |
| Flags and scores, computed by `rules/flags.py` and `rules/score.py` | "Ask Scout anything" answers use keyword matching |
| The shared-photo match (identical image hashes in PF photo URLs) | Sending: no message leaves the page; viewing slots are made up |
