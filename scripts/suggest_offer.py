from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LADDER = ROOT / "ops" / "offer-ladder.csv"


def format_price(value: str) -> str:
    amount = float(value)
    if amount.is_integer():
        return f"RMB {int(amount)}"
    return f"RMB {amount:.2f}"


def load_offers(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        required = {
            "offer_id",
            "tier",
            "trigger_service",
            "name",
            "price_rmb",
            "best_for",
            "deliverable",
            "scope",
            "turnaround",
            "delivery_note",
        }
        missing = sorted(required - set(reader.fieldnames or []))
        if missing:
            raise SystemExit("[FAIL] Missing offer ladder columns: " + ", ".join(missing))
        return list(reader)


def matches_trigger(offer: dict[str, str], trigger: str) -> bool:
    value = (offer.get("trigger_service") or "").strip()
    return value in {trigger, "any"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Suggest post-delivery upsell offers from the offer ladder.")
    parser.add_argument("--after-service", choices=["paper-reading", "citation-audit", "repro-audit"], required=True)
    parser.add_argument("--ladder", type=Path, default=DEFAULT_LADDER)
    parser.add_argument("--max", type=int, default=3)
    args = parser.parse_args()

    offers = load_offers(args.ladder)
    candidates = [
        offer
        for offer in offers
        if offer.get("tier") in {"repeat", "custom"} and matches_trigger(offer, args.after_service)
    ]

    if not candidates:
        raise SystemExit(f"[FAIL] No upsell candidates for {args.after_service}")

    print("# Suggested Follow-Up Offers")
    print()
    print(f"After service: `{args.after_service}`")
    print()
    for offer in candidates[: args.max]:
        print(f"## {offer['name']}")
        print()
        print(f"- Price: {format_price(offer['price_rmb'])}")
        print(f"- Best for: {offer['best_for']}")
        print(f"- Deliverable: {offer['deliverable']}")
        print(f"- Scope: {offer['scope']}")
        print(f"- Turnaround: {offer['turnaround']}")
        print(f"- Note: {offer['delivery_note']}")
        print()
        print("Suggested message:")
        print()
        print("```text")
        print(
            "如果这次结果对你有帮助，下一步可以考虑："
            f"{offer['name']}（{format_price(offer['price_rmb'])}）。"
            f"适合{offer['best_for']}，交付内容是{offer['deliverable']}。"
            "不用现在决定，确认这次交付有用后再说。"
        )
        print("```")
        print()


if __name__ == "__main__":
    main()
