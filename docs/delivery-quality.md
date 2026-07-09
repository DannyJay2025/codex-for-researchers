# Delivery Quality Gate

Use this gate before sending a paid Markdown result to a customer.

## Command

```powershell
python scripts\check_delivery.py orders\<order-id>\output\final.md --service paper-reading
```

Supported services:

- `paper-reading`
- `citation-audit`
- `repro-audit`

The checker looks for:

- input scope or order scope
- verification wording
- a delivery note or disclaimer
- service-specific sections
- obvious blank placeholders
- unsafe guarantee wording

## Workflow

1. Create the order workspace with `scripts/create_order_workspace.py`.
2. Draft the result in `orders/<order-id>/output/draft.md`.
3. Save the customer-ready version as `orders/<order-id>/output/final.md`.
4. Run `scripts/check_delivery.py`.
5. Complete `orders/<order-id>/delivery-checklist.md`.
6. Send the final Markdown only after both checks pass.

## Limits

This script is a quality gate, not a scientific validator. It cannot verify that citations, statistics, DOI values, or methodological claims are correct. It only catches missing structure, missing disclaimers, obvious placeholders, and risky guarantee language.
