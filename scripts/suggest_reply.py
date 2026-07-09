from __future__ import annotations

import argparse
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_LIBRARY = ROOT / "ops" / "lead-reply-library.tsv"
REQUIRED_COLUMNS = {"scenario", "stage", "trigger", "next_action", "reply_text"}


def load_replies(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise SystemExit(f"[FAIL] Reply library does not exist: {path}")

    with path.open(newline="", encoding="utf-8-sig") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames or []))
        if missing:
            raise SystemExit("[FAIL] Missing reply library columns: " + ", ".join(missing))
        rows = list(reader)

    if not rows:
        raise SystemExit("[FAIL] Reply library has no rows.")
    return rows


def main() -> None:
    parser = argparse.ArgumentParser(description="Print a copy-ready WeChat reply for a lead scenario.")
    parser.add_argument("--scenario", help="Scenario id to print. Omit with --list to show all scenarios.")
    parser.add_argument("--library", type=Path, default=DEFAULT_LIBRARY)
    parser.add_argument("--list", action="store_true", help="List available scenarios.")
    args = parser.parse_args()

    rows = load_replies(args.library)

    if args.list:
        print("# Available Reply Scenarios")
        print()
        print("| Scenario | Stage | Trigger | Next action |")
        print("| --- | --- | --- | --- |")
        for row in rows:
            print(f"| {row['scenario']} | {row['stage']} | {row['trigger']} | {row['next_action']} |")
        return

    if not args.scenario:
        raise SystemExit("[FAIL] Provide --scenario or use --list.")

    matches = [row for row in rows if row["scenario"] == args.scenario]
    if not matches:
        available = ", ".join(row["scenario"] for row in rows)
        raise SystemExit(f"[FAIL] Unknown scenario: {args.scenario}. Available: {available}")

    row = matches[0]
    print(f"# Reply: {row['scenario']}")
    print()
    print(f"- Stage: {row['stage']}")
    print(f"- Trigger: {row['trigger']}")
    print(f"- Next action: {row['next_action']}")
    print()
    print("```text")
    print(row["reply_text"])
    print("```")


if __name__ == "__main__":
    main()
