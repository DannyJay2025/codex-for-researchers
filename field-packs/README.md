# Field Packs

Field packs adapt the core skills to a specific research domain. Each pack should contain terminology, evidence standards, common review risks, and field-specific output templates.

## Initial Packs

| Pack | Buyer | Main paid use case |
| --- | --- | --- |
| `biomedicine` | Life science and clinical researchers | citation support, cautious mechanism wording, data availability |
| `ai-ml` | Machine learning researchers and startups | benchmark claims, reproducibility, model cards, ablation review |
| `social-science` | Social science researchers | study design, causal language, survey methods, ethics notes |

## Pack Structure

```text
field-name/
  README.md
  terminology.md
  evidence-standards.md
  review-risks.md
  templates/
```

The public repo can keep only `README.md` files at first. Detailed references belong in the private premium repo once they become a paid asset.
