from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIVATE_DIRS = {"orders", "customer-files", "private-deliveries", ".git"}

REQUIRED_PATHS = [
    ".codex-plugin/plugin.json",
    "README.md",
    "LICENSE",
    "skills/research-paper-reader/SKILL.md",
    "skills/citation-support-finder/SKILL.md",
    "skills/manuscript-polisher/SKILL.md",
    "skills/reproducibility-packager/SKILL.md",
    "templates/reading-brief/template.md",
    "templates/citation-map/template.md",
    "templates/manuscript-polish/request-template.md",
    "templates/reproducibility-package/checklist.md",
    "premium-templates/README.md",
    "field-packs/README.md",
    "docs/customer-guide.zh-CN.md",
    "docs/faq.zh-CN.md",
    "docs/index.html",
    "docs/assets/wechat-qr.png",
    "docs/.nojekyll",
    "docs/getting-started.md",
    "docs/customer-delivery-flow.md",
    "docs/fulfillment-sop.md",
    "docs/delivery-quality.md",
    "docs/order-ops-playbook.zh-CN.md",
    "docs/monetization-roadmap.md",
    "docs/service-offers.md",
    "docs/premium-access.md",
    "docs/privacy-and-disclaimer.md",
    "marketing/launch-posts.zh-CN.md",
    "ops/README.md",
    "ops/order-tracker-template.csv",
    "assets/payments/README.md",
    "assets/payments/wechat-qr.png",
    "premium-templates/order-form.md",
    "scripts/create_order_workspace.py",
    "scripts/check_delivery.py",
    "delivery-templates/paper-reading-brief.md",
    "delivery-templates/citation-support-audit.md",
    "delivery-templates/reproducibility-package-audit.md",
    "deliverables/paper-reading-brief/sample.md",
    "deliverables/citation-audit/sample.md",
    "deliverables/reproducibility-audit/sample.md",
    ".github/workflows/ci.yml",
    ".github/workflows/pages.yml",
    ".github/ISSUE_TEMPLATE/order_request.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
]

MOJIBAKE_MARKERS = (
    "浣",
    "璇",
    "鏂",
    "鍏",
    "銆",
    "€",
    "�",
)


def fail(message: str) -> None:
    raise SystemExit(f"[FAIL] {message}")


def main() -> None:
    missing = [path for path in REQUIRED_PATHS if not (ROOT / path).exists()]
    if missing:
        fail("Missing required files:\n" + "\n".join(f"- {path}" for path in missing))

    plugin_path = ROOT / ".codex-plugin" / "plugin.json"
    try:
        manifest = json.loads(plugin_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"Invalid plugin JSON: {exc}")

    if manifest.get("name") != "codex-for-researchers":
        fail("Plugin manifest name must be codex-for-researchers")

    if manifest.get("skills") != "./skills/":
        fail("Plugin manifest must point skills to ./skills/")

    landing = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
    for required_text in [
        "1.99",
        "3.99",
        "5.99",
        "zhiyanaishe",
        "assets/wechat-qr.png",
        "faq.zh-CN.md",
        "24-72",
        "付款截图",
        "一次澄清回复",
    ]:
        if required_text not in landing:
            fail(f"Landing page is missing required text: {required_text}")

    chinese_paths = [
        ROOT / "README.md",
        ROOT / "docs" / "index.html",
        ROOT / "docs" / "customer-guide.zh-CN.md",
        ROOT / "docs" / "faq.zh-CN.md",
        ROOT / "docs" / "customer-delivery-flow.md",
    ]
    for path in chinese_paths:
        text = path.read_text(encoding="utf-8")
        if any(marker in text for marker in MOJIBAKE_MARKERS):
            fail(f"Potential mojibake detected in {path.relative_to(ROOT)}")

    todo_hits: list[str] = []
    for path in ROOT.rglob("*"):
        if any(part in PRIVATE_DIRS for part in path.relative_to(ROOT).parts):
            continue
        if path.is_file() and path.suffix.lower() in {".html", ".md", ".yaml", ".json", ".py"}:
            text = path.read_text(encoding="utf-8", errors="ignore")
            todo_marker = "[" + "TODO"
            todo_label = "TODO" + ":"
            if todo_marker in text or todo_label in text:
                todo_hits.append(str(path.relative_to(ROOT)))

    if todo_hits:
        fail("Remove TODO placeholders:\n" + "\n".join(f"- {path}" for path in todo_hits))

    print("[OK] Codex for Researchers project checks passed.")


if __name__ == "__main__":
    main()
