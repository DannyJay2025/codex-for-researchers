---
name: citation-support-finder
description: Find, verify, and organize literature support for manuscript claims. Use when the user provides manuscript paragraphs, introduction text, discussion claims, grant text, reviewer requests for citations, a claim list, or asks to add references, find supporting papers, build a claim-to-citation table, verify citation relevance, or identify unsupported academic statements.
---

# Citation Support Finder

## Workflow

1. Split the input into atomic claims. Keep claims small enough that one citation can clearly support or fail to support each claim.
2. Classify each claim: background, method, benchmark, mechanism, clinical relevance, dataset, limitation, comparison, or novelty.
3. Decide what evidence standard is needed: primary research, review, guideline, dataset paper, methods paper, or benchmark paper.
4. Search or plan searches. When live literature tools or web search are available, use them for current bibliographic facts. When they are unavailable, produce precise search queries and mark the result as search-plan-only.
5. Verify each candidate reference against the claim. Do not accept title-only matches.
6. Return a claim-to-citation map with support strength and caveats.

## Evidence Labels

- Direct: the source directly supports the full claim.
- Partial: the source supports part of the claim, but the wording should be narrowed.
- Background: the source gives context but does not prove the claim.
- Contradictory: the source conflicts with the claim.
- Unsupported: no adequate source was found or provided.
- Needs verification: bibliographic data or full text could not be checked.

## Output Contract

Use `references/citation-map-schema.md` for structured outputs. Always include:

- Atomic claim.
- Recommended citation or search query.
- Support label.
- Reason for inclusion.
- Safer revised wording when the original claim is too broad.
- Missing evidence or verification notes.

## Citation Integrity

- Do not fabricate authors, titles, years, journals, DOIs, PMIDs, or URLs.
- Prefer primary papers for empirical claims and reviews for broad background claims.
- If the user requests a specific journal family, year range, impact tier, or database, follow that filter and report when it limits coverage.
- If the manuscript already has citations, verify whether each citation supports the sentence it is attached to.
- If the claim is speculative, suggest cautious wording rather than forcing citations.

## Commercial Use Angle

For paid services, deliver a polished citation audit table plus a "high-risk claims" section. This is the part labs and authors are most likely to pay for because it reduces reviewer friction.
