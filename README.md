# Codex for Researchers

Low-cost Codex research workflows for paper reading, citation checks, and reproducibility audits.

中文入口：加微信 `zhiyanaishe`，扫码付款后发送论文、段落或项目仓库信息。当前引流价：论文精读 `1.99 元`，引用审计 `3.99 元`，复现包审计 `5.99 元`。

Codex for Researchers is a GitHub-first Codex workflow pack for researchers, graduate students, labs, and technical founders who need help reading papers, improving manuscripts, mapping citations, and preparing reproducibility packages.

The project is intentionally lightweight: it depends on Codex workflows and local files first. Live web or literature search can be used when available, but the core value is repeatable research work instructions packaged as Codex skills.

## What is included

- `research-paper-reader`: turn a paper PDF, DOI, arXiv link, abstract, or pasted text into structured reading notes.
- `citation-support-finder`: split manuscript claims and build a claim-to-reference support map.
- `manuscript-polisher`: polish academic prose while preserving scientific meaning.
- `reproducibility-packager`: audit code, data, methods, and availability statements before submission.
- `templates/`: reusable outputs for reading briefs, citation maps, polishing requests, and reproducibility packages.
- `scripts/check_project.py`: basic repo health checks before publishing.
- `scripts/check_delivery.py`: pre-send Markdown delivery quality checks.
- `scripts/summarize_growth.py`: private funnel and revenue summary for weekly review.
- `scripts/suggest_offer.py`: post-delivery upsell suggestions from the offer ladder.
- `scripts/suggest_reply.py`: copy-ready WeChat replies for common lead scenarios.

## Buy a low-cost workflow

| Service | Price | You send | You receive | Typical delivery |
| --- | --- | --- | --- | --- |
| Paper reading brief | RMB 1.99 | One paper link, abstract, or PDF excerpt | A structured Markdown reading brief | 24-72 hours |
| Citation support audit | RMB 3.99 | One manuscript paragraph or claim list | A claim-to-citation risk table | 24-72 hours |
| Reproducibility package audit | RMB 5.99 | One repo/file inventory or project folder summary | A reproducibility checklist and risk report | 24-72 hours |

Order flow:

1. Add WeChat `zhiyanaishe`.
2. Say which service you want.
3. Pay with the QR code below.
4. Send payment screenshot and materials.
5. Receive the deliverable as Markdown text or a file.

Send this with the order to reduce back-and-forth:

```text
Service: paper reading brief / citation support audit / reproducibility package audit
Language: Chinese / English / bilingual
Materials: link, abstract, paragraph, or repo summary
Use case: journal club / writing / submission check / reproducibility cleanup
Permission to anonymize into a public sample: yes / no
```

Delivery expectations:

- Normal turnaround for the launch offers is 24-72 hours.
- Buyers can request Chinese, English, or bilingual output.
- Launch pricing includes one clarification reply, not unlimited rewrites.
- A material scope change after payment should be handled as a new order.

## Who this is for

- Researchers preparing manuscripts, rebuttals, grants, or journal club notes.
- Labs that want repeatable writing and review workflows.
- Solo builders creating paid research assistant templates or services.
- Consultants offering manuscript polishing, citation checking, or reproducibility audits.

## Monetization path

Start open source, monetize depth:

- Free: core skills, templates, and example prompts.
- Paid: private premium templates for specific fields, journal families, grant formats, and lab SOPs.
- Service: manuscript audit, citation support, reproducibility packaging, and paper-to-slide delivery.
- Enterprise: private lab plugin with custom writing style, checklist, terminology, and data policy references.

See:

- `docs/customer-guide.zh-CN.md` for Chinese customer ordering instructions.
- `docs/faq.zh-CN.md` for buyer objections, refund boundaries, privacy expectations, and scope fit.
- `docs/samples.zh-CN.md` for a customer-facing sample gallery.
- `docs/index.html` for the public GitHub Pages landing page.
- `docs/getting-started.md` for the exact steps to run and launch the project.
- `docs/customer-delivery-flow.md` for lead-to-delivery operations.
- `docs/fulfillment-sop.md` for service execution steps.
- `docs/delivery-quality.md` for the pre-send delivery quality gate.
- `docs/growth-review-playbook.zh-CN.md` for weekly funnel, revenue, and channel review.
- `docs/upsell-playbook.zh-CN.md` for turning entry orders into repeat packages and custom work.
- `docs/lead-triage-playbook.zh-CN.md` for consultation triage and WeChat reply scripts.
- `docs/order-ops-playbook.zh-CN.md` for order status, scope control, refunds, and daily operations.
- `docs/monetization-roadmap.md` for the product ladder.
- `docs/service-offers.md` for service packages and starter pricing.
- `docs/premium-access.md` for WeChat payment and manual premium delivery.
- `docs/privacy-and-disclaimer.md` for customer-data handling and boundaries.
- `marketing/launch-posts.zh-CN.md` for copy-and-paste launch posts, private-chat closing scripts, and daily promotion rhythm.
- `ops/order-tracker-template.csv` for a private local order tracker template.
- `ops/growth-metrics-template.csv` for private funnel and revenue tracking.
- `ops/offer-ladder.csv` for entry, repeat, and custom service packaging.
- `ops/lead-reply-library.tsv` for public-safe WeChat reply templates.
- `premium-templates/` for the paid template catalog.
- `field-packs/` for research-domain expansion packs.

## Payment and delivery

This project is designed for a solo developer workflow:

- Take payment through WeChat QR code.
- Contact WeChat: `zhiyanaishe`.
- Confirm the buyer by payment screenshot plus GitHub username, email, or WeChat ID.
- Deliver premium materials through a private GitHub repository, private release archive, or direct file delivery.
- Use `premium-templates/order-form.md` to collect the buyer's order details.

Public GitHub repository:

```text
https://github.com/DannyJay2025/codex-for-researchers
```

Public landing page:

```text
https://dannyjay2025.github.io/codex-for-researchers/
```

WeChat payment QR code:

![WeChat payment QR code](assets/payments/wechat-qr.png)

Launch prices:

| Service | Price |
| --- | --- |
| Paper reading brief | RMB 1.99 |
| Citation support audit | RMB 3.99 |
| Reproducibility package audit | RMB 5.99 |

Sample deliverables:

- `deliverables/paper-reading-brief/sample.md`
- `deliverables/citation-audit/sample.md`
- `deliverables/reproducibility-audit/sample.md`

Chinese order guide:

- `docs/customer-guide.zh-CN.md`

## Quick start

This is a Codex workflow pack, not a web app. There is no dev server to start.

1. Open this folder in Codex.
2. Ask Codex to use one of the skills under `skills/`.
3. Provide the paper, manuscript section, claim list, or project folder you want processed.
4. Use the generated outputs as drafts, then verify scientific facts and citations before submission.

Example prompts:

```text
Use research-paper-reader on this PDF and create a journal club reading brief.
```

```text
Use citation-support-finder on these introduction paragraphs and produce a claim-to-citation table.
```

```text
Use reproducibility-packager to audit this project folder before submission.
```

## Product positioning

This is not a generic AI writing prompt collection. The repo packages repeatable scholarly workflows as Codex skills so the same quality bar can be reused across projects, teams, and services.

## Repository layout

```text
codex-for-researchers/
  .codex-plugin/plugin.json
  skills/
    research-paper-reader/
    citation-support-finder/
    manuscript-polisher/
    reproducibility-packager/
  templates/
  premium-templates/
  field-packs/
  marketing/
  ops/
  assets/
  docs/
    getting-started.md
  examples/
  scripts/
```

## Validation

Run:

```bash
python scripts/check_project.py
```

For plugin and skill validation, use the Codex skill/plugin creator validation scripts if they are available in your Codex environment.

## License

MIT. See `LICENSE`.
