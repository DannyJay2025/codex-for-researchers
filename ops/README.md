# Operations Templates

This folder contains public-safe operating templates for the solo service workflow.

Do not store real customer names, WeChat IDs, manuscripts, payment screenshots, private order notes, or delivery outputs in this folder. Real order data belongs under the ignored local `orders/` directory.

Files:

- `order-tracker-template.csv`: copy this to `orders/order-tracker.csv` for private order tracking.
- `growth-metrics-template.csv`: copy this to `orders/growth-metrics.csv` for private funnel and revenue tracking.
- `offer-ladder.csv`: public-safe entry, repeat, and custom offer ladder used by `scripts/suggest_offer.py`.
- `lead-reply-library.tsv`: public-safe WeChat reply templates used by `scripts/suggest_reply.py`.

Related docs:

- `docs/growth-review-playbook.zh-CN.md`
- `docs/upsell-playbook.zh-CN.md`
- `docs/lead-triage-playbook.zh-CN.md`
- `docs/order-ops-playbook.zh-CN.md`
- `docs/fulfillment-sop.md`
- `marketing/launch-posts.zh-CN.md`
