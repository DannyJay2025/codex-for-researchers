from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ORDERS = ROOT / "orders"
SERVICES = {
    "paper-reading": "RMB 1.99 paper reading brief",
    "citation-audit": "RMB 3.99 citation support audit",
    "repro-audit": "RMB 5.99 reproducibility package audit",
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
    args = parser.parse_args()

    today = dt.date.today().strftime("%Y%m%d")
    order_id = args.order_id or f"{today}-{slugify(args.buyer)}-{args.service}"
    target = ORDERS / order_id
    target.mkdir(parents=True, exist_ok=False)

    (target / "input").mkdir()
    (target / "output").mkdir()
    (target / "notes.md").write_text(
        "\n".join(
            [
                f"# Order {order_id}",
                "",
                f"- Buyer: {args.buyer}",
                f"- Service: {SERVICES[args.service]}",
                "- Payment screenshot received: no",
                "- Delivery status: not started",
                "- Customer consent for public redacted example: no",
                "",
                "## Materials",
                "",
                "Put customer materials in `input/`. Do not commit this folder.",
                "",
                "## Delivery",
                "",
                "Put final Markdown or files in `output/`.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    print(f"Created private order workspace: {target}")


if __name__ == "__main__":
    main()
