from __future__ import annotations

import argparse
import datetime as dt
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ORDERS = ROOT / "orders"
SERVICES = {
    "paper-reading": "RMB 1.99 paper reading brief",
    "citation-audit": "RMB 3.99 citation support audit",
    "repro-audit": "RMB 5.99 reproducibility package audit",
}
TEMPLATES = {
    "paper-reading": ROOT / "delivery-templates" / "paper-reading-brief.md",
    "citation-audit": ROOT / "delivery-templates" / "citation-support-audit.md",
    "repro-audit": ROOT / "delivery-templates" / "reproducibility-package-audit.md",
}


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "buyer"


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a private local order workspace.")
    parser.add_argument("--service", choices=SERVICES.keys(), required=True)
    parser.add_argument("--buyer", required=True)
    parser.add_argument("--id", dest="order_id", default=None)
    parser.add_argument("--due-days", type=int, default=3)
    args = parser.parse_args()

    today_date = dt.date.today()
    today = today_date.strftime("%Y%m%d")
    due_date = today_date + dt.timedelta(days=args.due_days)
    order_id = args.order_id or f"{today}-{slugify(args.buyer)}-{args.service}"
    target = ORDERS / order_id
    target.mkdir(parents=True, exist_ok=False)

    (target / "input").mkdir()
    (target / "output").mkdir()
    template = TEMPLATES[args.service]
    draft = target / "output" / "draft.md"
    draft.write_text(template.read_text(encoding="utf-8"), encoding="utf-8")
    status = {
        "order_id": order_id,
        "buyer": args.buyer,
        "service": args.service,
        "service_label": SERVICES[args.service],
        "created_date": today_date.isoformat(),
        "due_date": due_date.isoformat(),
        "payment_screenshot_received": False,
        "materials_received": False,
        "scope_confirmed": False,
        "delivery_status": "not_started",
        "delivery_format": "markdown",
        "customer_consent_for_public_redacted_example": False,
        "private_materials_rule": "Do not commit this order folder or customer files.",
    }
    (target / "status.json").write_text(
        json.dumps(status, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (target / "delivery-checklist.md").write_text(
        "\n".join(
            [
                f"# Delivery Checklist: {order_id}",
                "",
                "## Before Work",
                "",
                "- [ ] Payment screenshot received.",
                "- [ ] Buyer identity recorded.",
                "- [ ] Service and scope confirmed.",
                "- [ ] Customer materials saved under `input/`.",
                "- [ ] Sensitive or private data flagged.",
                "",
                "## Before Delivery",
                "",
                "- [ ] Output starts from the correct delivery template.",
                "- [ ] Input scope is stated clearly.",
                "- [ ] Unverified facts, citations, and metadata are marked.",
                "- [ ] No fabricated references or publication guarantees.",
                "- [ ] Customer private material is not copied into public examples.",
                "- [ ] One next-step recommendation is included.",
                "",
                "## After Delivery",
                "",
                "- [ ] Final output saved as `output/final.md`.",
                "- [ ] Delivery message sent to customer.",
                "- [ ] Clarification/revision status recorded.",
                "- [ ] If allowed, redacted sample idea recorded separately.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    (target / "notes.md").write_text(
        "\n".join(
            [
                f"# Order {order_id}",
                "",
                f"- Buyer: {args.buyer}",
                f"- Service: {SERVICES[args.service]}",
                f"- Due date: {due_date.isoformat()}",
                "- Payment screenshot received: no",
                "- Delivery status: not started",
                "- Customer consent for public redacted example: no",
                "- Status file: `status.json`",
                "- Checklist: `delivery-checklist.md`",
                "",
                "## Materials",
                "",
                "Put customer materials in `input/`. Do not commit this folder.",
                "",
                "## Delivery",
                "",
                "Start from `output/draft.md`, then save the final customer version in `output/final.md`.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"Created private order workspace: {target}")
    print(f"Draft template: {draft}")
    print(f"Status file: {target / 'status.json'}")
    print(f"Delivery checklist: {target / 'delivery-checklist.md'}")


if __name__ == "__main__":
    main()
