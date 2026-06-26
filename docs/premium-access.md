# Premium Access

Use this page as the public route from the free repository to paid templates, field packs, and services. This version assumes a solo developer setup: WeChat payment first, manual delivery after confirmation.

## Access Options

| Option | Best for | How it works |
| --- | --- | --- |
| One-time template purchase | Individuals who want a specific pack | Buyer scans the WeChat QR code, sends payment proof, then receives the selected pack |
| Private repository access | Repeat buyers, labs, consultants | Buyer is manually invited to `codex-for-researchers-premium` after payment |
| Service package | Authors who need a concrete deliverable | Buyer sends a manuscript excerpt, claim list, or project folder for a fixed-scope audit |
| Custom lab workflow | Labs and research teams | You create a private Codex plugin with lab-specific SOPs and templates |

## Buyer Flow

1. Buyer chooses a pack or service from `docs/service-offers.md`.
2. Buyer sends the order details using `premium-templates/order-form.md`.
3. Buyer pays through your WeChat payment QR code.
4. Buyer sends payment screenshot plus one delivery identity: GitHub username, email, or WeChat ID.
5. You manually deliver the asset by private repo invite, release archive, or direct file transfer.

Current contact:

```text
WeChat: zhiyanaishe
GitHub: https://github.com/DannyJay2025
Public repo: https://github.com/DannyJay2025/codex-for-researchers
```

## Payment QR Code

Recommended public asset path:

```text
assets/payments/wechat-qr.png
```

The QR code is intended to be public for this project. Add the image file at the path above before publishing the first paid version.

![WeChat payment QR code](../assets/payments/wechat-qr.png)

Suggested buyer instructions:

```markdown
Need premium templates or a private lab workflow?

1. Choose a package from docs/service-offers.md.
2. Fill in premium-templates/order-form.md.
3. Add WeChat zhiyanaishe and pay by WeChat QR code.
4. Send your payment screenshot and GitHub username for delivery.
```

## Suggested Premium Prices

| Product | Price | Delivery |
| --- | --- | --- |
| Paper reading brief | RMB 1.99 | Markdown reading brief |
| Citation support audit | RMB 3.99 | Claim-to-citation table |
| Reproducibility audit | RMB 5.99 | Audit report and availability statements |
| Single premium template pack | RMB 99-199 | Archive or private repo folder |
| Full premium template bundle | RMB 299-699 | Private repo access |
| One manuscript section polish | RMB 399-1499 | Markdown or DOCX-style output |
| Lab custom workflow | RMB 6999+ | Private Codex plugin and templates |

## Manual Fulfillment Checklist

- Confirm payment amount and buyer identity.
- Record product, delivery method, and date.
- Invite the buyer to the private repo or send the archive.
- Keep paid assets out of the public repository.
- Use clear refund and revision rules before accepting service work.

## Private Repo Structure

Recommended private repository:

```text
codex-for-researchers-premium/
  premium-templates/
    journal-submission-kit/
    citation-audit-kit/
    reproducibility-release-kit/
  field-packs/
    biomedicine/
    ai-ml/
    social-science/
  lab-sops/
  examples/
```
