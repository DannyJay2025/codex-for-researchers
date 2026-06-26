# Citation Map Schema

Use this table for citation support tasks.

| ID | Manuscript claim | Claim type | Evidence needed | Candidate citation | Support | Safer wording | Verification notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 |  | Background / Method / Result / Novelty / Limitation |  |  | Direct / Partial / Background / Contradictory / Unsupported / Needs verification |  |  |

## Search Query Format

When live search is unavailable, give 2-4 queries per unsupported claim:

```text
("core concept" OR synonym) AND ("method" OR "population" OR "endpoint") AND review
```

```text
"exact mechanism phrase" AND "primary study"
```

## Risk Flags

- Overgeneralized: the claim says "all", "always", "first", "only", "significantly", or "widely" without evidence.
- Citation mismatch: the citation is related but does not support the exact sentence.
- Review-only: an empirical claim is supported only by a review.
- Old source: the field is fast-moving and the support may be outdated.
- Missing comparator: the claim implies superiority without a direct comparison.
