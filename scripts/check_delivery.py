from __future__ import annotations

import argparse
import re
from pathlib import Path


SERVICE_SECTIONS = {
    "paper-reading": [
        "thesis",
        "problem",
        "method",
        "evidence",
        "limitation",
        "question",
    ],
    "citation-audit": [
        "claim",
        "citation",
        "risk",
        "search",
        "safer",
        "verification",
    ],
    "repro-audit": [
        "artifact",
        "inventory",
        "risk",
        "code availability",
        "data availability",
        "next action",
    ],
}

COMMON_TERMS = [
    "scope",
    "verify",
]

DISCLAIMER_TERMS = [
    "ai-assisted",
    "workflow draft",
    "please verify",
    "verify final",
]

FORBIDDEN_PATTERNS = [
    re.compile(r"\bguarantee(?:d|s)?\s+(?:acceptance|publication|citation correctness)\b", re.I),
    re.compile(r"\bwill\s+be\s+accepted\b", re.I),
    re.compile(r"\bpublication\s+is\s+guaranteed\b", re.I),
]

PLACEHOLDER_PATTERNS = [
    re.compile(r"(?m)^\s*-\s*$"),
    re.compile(r"(?m)^\s*\d+\.\s*$"),
    re.compile(r"\|[ \t]*\|"),
    re.compile(r"\b" + "TODO" + r"\b|" + "TODO" + r":|\bTBD\b|\bFIXME\b", re.I),
    re.compile(r"(?m)^-\s+(Buyer|Delivery date|Source):\s*$", re.I),
]


def fail(message: str) -> None:
    raise SystemExit(f"[FAIL] {message}")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower())


def find_missing_terms(text: str, terms: list[str]) -> list[str]:
    normalized = normalize(text)
    return [term for term in terms if term not in normalized]


def find_placeholders(text: str) -> list[str]:
    hits: list[str] = []
    for pattern in PLACEHOLDER_PATTERNS:
        match = pattern.search(text)
        if match:
            hits.append(match.group(0).strip() or pattern.pattern)
    return hits


def main() -> None:
    parser = argparse.ArgumentParser(description="Check a customer-facing Markdown delivery before sending it.")
    parser.add_argument("file", type=Path, help="Path to the Markdown delivery file.")
    parser.add_argument("--service", choices=SERVICE_SECTIONS.keys(), required=True)
    args = parser.parse_args()

    if not args.file.exists():
        fail(f"Delivery file does not exist: {args.file}")

    text = args.file.read_text(encoding="utf-8")
    if len(text.strip()) < 500:
        fail("Delivery is too short to be customer-ready.")

    missing_common = find_missing_terms(text, COMMON_TERMS)
    if missing_common:
        fail("Delivery is missing common quality terms: " + ", ".join(missing_common))

    if not any(term in normalize(text) for term in DISCLAIMER_TERMS):
        fail("Delivery is missing a verification disclaimer or delivery note.")

    missing_sections = find_missing_terms(text, SERVICE_SECTIONS[args.service])
    if missing_sections:
        fail("Delivery is missing service-specific terms: " + ", ".join(missing_sections))

    placeholder_hits = find_placeholders(text)
    if placeholder_hits:
        fail("Delivery still contains placeholder content: " + "; ".join(placeholder_hits[:5]))

    forbidden_hits = [pattern.pattern for pattern in FORBIDDEN_PATTERNS if pattern.search(text)]
    if forbidden_hits:
        fail("Delivery contains unsafe guarantee wording: " + "; ".join(forbidden_hits))

    print(f"[OK] Delivery quality check passed for {args.service}: {args.file}")


if __name__ == "__main__":
    main()
