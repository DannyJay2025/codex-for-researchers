# Fulfillment SOP

Use this SOP after payment is confirmed. Never commit customer files, manuscripts, payment screenshots, or private outputs to this public repository.

## Local Order Workspace

Create a private local workspace:

```powershell
python scripts\create_order_workspace.py --service paper-reading --buyer buyer-name
```

Supported services:

- `paper-reading`
- `citation-audit`
- `repro-audit`

The script creates an `orders/` folder, which is ignored by git.

It also copies a matching draft template to:

```text
orders/<order-id>/output/draft.md
```

Use `draft.md` while working and save the customer-ready version as `final.md`.

## RMB 1.99: Paper Reading Brief

Input:

- Paper title, DOI, URL, abstract, PDF excerpt, or pasted section.

Process:

1. Use `research-paper-reader`.
2. If only abstract or excerpt is provided, label the output as limited-scope.
3. Produce a concise reading brief.
4. Include caveats for unverified methods, figures, or statistics.

Output:

- One-sentence thesis.
- Problem and motivation.
- Method map.
- Key evidence.
- Limitations.
- 3 follow-up questions.

Use sample: `deliverables/paper-reading-brief/sample.md`.

Use template: `delivery-templates/paper-reading-brief.md`.

## RMB 3.99: Citation Support Audit

Input:

- One paragraph, introduction excerpt, discussion excerpt, or claim list.

Process:

1. Use `citation-support-finder`.
2. Split into atomic claims.
3. Flag overbroad wording.
4. Suggest search queries or candidate citation types.
5. Do not fabricate references.

Output:

- Claim-to-citation table.
- Support label.
- Safer wording.
- Verification notes.

Use sample: `deliverables/citation-audit/sample.md`.

Use template: `delivery-templates/citation-support-audit.md`.

## RMB 5.99: Reproducibility Package Audit

Input:

- GitHub URL, file list, repository zip summary, or project folder.

Process:

1. Use `reproducibility-packager`.
2. If a local folder is available, run the audit script.
3. Check README, environment, code entry point, data, outputs, and availability statements.
4. Mark unknowns clearly.

Output:

- Artifact inventory.
- Pass/partial/fail checklist.
- Main risks.
- Draft code and data availability statements.

Use sample: `deliverables/reproducibility-audit/sample.md`.

Use template: `delivery-templates/reproducibility-package-audit.md`.

## Revision Policy

For launch pricing:

- Include one clarification reply.
- Do not include unlimited rewrites.
- If the customer changes scope, ask them to place a new order.

## Quality Bar

Every paid delivery must:

- State the input scope.
- Mark unverified facts.
- Avoid publication guarantees.
- Avoid fabricated citations.
- Keep customer data private.
