from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

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
    "docs/getting-started.md",
    "docs/monetization-roadmap.md",
    "docs/service-offers.md",
    "docs/premium-access.md",
    "assets/payments/README.md",
    "assets/payments/wechat-qr.png",
    "premium-templates/order-form.md",
]


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

    todo_hits: list[str] = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".yaml", ".json", ".py"}:
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
