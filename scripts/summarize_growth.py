from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path


NUMERIC_FIELDS = [
    "impressions_est",
    "profile_clicks",
    "wechat_adds",
    "paid_orders",
    "revenue_rmb",
    "fulfilled_orders",
    "refunds",
]


def as_float(value: str) -> float:
    value = (value or "").strip()
    if not value:
        return 0.0
    return float(value)


def pct(numerator: float, denominator: float) -> str:
    if denominator <= 0:
        return "n/a"
    return f"{numerator / denominator * 100:.1f}%"


def money(value: float) -> str:
    return f"RMB {value:.2f}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize private growth metrics for weekly review.")
    parser.add_argument("csv_path", type=Path, help="Path to a growth metrics CSV file.")
    args = parser.parse_args()

    if not args.csv_path.exists():
        raise SystemExit(f"[FAIL] Metrics CSV does not exist: {args.csv_path}")

    rows: list[dict[str, str]] = []
    with args.csv_path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle)
        missing = [field for field in ["date", "channel", *NUMERIC_FIELDS] if field not in (reader.fieldnames or [])]
        if missing:
            raise SystemExit("[FAIL] Missing CSV columns: " + ", ".join(missing))
        rows = list(reader)

    if not rows:
        raise SystemExit("[FAIL] Metrics CSV has no rows.")

    totals = {field: 0.0 for field in NUMERIC_FIELDS}
    by_channel: dict[str, dict[str, float]] = defaultdict(lambda: {field: 0.0 for field in NUMERIC_FIELDS})

    for row in rows:
        channel = (row.get("channel") or "unknown").strip() or "unknown"
        for field in NUMERIC_FIELDS:
            value = as_float(row.get(field, ""))
            totals[field] += value
            by_channel[channel][field] += value

    print("# Growth Metrics Summary")
    print()
    print(f"- Rows: {len(rows)}")
    print(f"- Estimated impressions: {totals['impressions_est']:.0f}")
    print(f"- Profile clicks: {totals['profile_clicks']:.0f}")
    print(f"- WeChat adds: {totals['wechat_adds']:.0f}")
    print(f"- Paid orders: {totals['paid_orders']:.0f}")
    print(f"- Fulfilled orders: {totals['fulfilled_orders']:.0f}")
    print(f"- Refunds: {totals['refunds']:.0f}")
    print(f"- Revenue: {money(totals['revenue_rmb'])}")
    print(f"- Click rate: {pct(totals['profile_clicks'], totals['impressions_est'])}")
    print(f"- WeChat add rate from clicks: {pct(totals['wechat_adds'], totals['profile_clicks'])}")
    print(f"- Paid conversion from WeChat adds: {pct(totals['paid_orders'], totals['wechat_adds'])}")
    print()
    print("## By Channel")
    print()
    print("| Channel | Impressions | WeChat adds | Paid orders | Revenue |")
    print("| --- | ---: | ---: | ---: | ---: |")
    for channel, data in sorted(by_channel.items()):
        print(
            "| "
            + " | ".join(
                [
                    channel,
                    f"{data['impressions_est']:.0f}",
                    f"{data['wechat_adds']:.0f}",
                    f"{data['paid_orders']:.0f}",
                    money(data["revenue_rmb"]),
                ]
            )
            + " |"
        )


if __name__ == "__main__":
    main()
