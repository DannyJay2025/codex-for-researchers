from __future__ import annotations

import argparse
from pathlib import Path


ENV_FILES = {
    "requirements.txt",
    "environment.yml",
    "environment.yaml",
    "pyproject.toml",
    "poetry.lock",
    "Pipfile",
    "Pipfile.lock",
    "renv.lock",
    "Dockerfile",
}

README_FILES = {"README.md", "README.rst", "README.txt"}
LICENSE_FILES = {"LICENSE", "LICENSE.md", "COPYING"}
CODE_SUFFIXES = {".py", ".R", ".r", ".jl", ".m", ".ipynb", ".sh"}
DATA_SUFFIXES = {".csv", ".tsv", ".xlsx", ".xls", ".json", ".parquet", ".h5", ".hdf5", ".rds"}
FIGURE_SUFFIXES = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".svg", ".pdf"}


def collect_files(root: Path) -> list[Path]:
    ignored = {".git", ".venv", "venv", "__pycache__", ".pytest_cache"}
    files: list[Path] = []
    for path in root.rglob("*"):
        if any(part in ignored for part in path.parts):
            continue
        if path.is_file():
            files.append(path)
    return files


def has_named(files: list[Path], names: set[str]) -> bool:
    return any(path.name in names for path in files)


def by_suffix(files: list[Path], suffixes: set[str]) -> list[Path]:
    return [path for path in files if path.suffix.lower() in suffixes]


def rel_list(root: Path, files: list[Path], limit: int = 12) -> list[str]:
    shown = [str(path.relative_to(root)) for path in files[:limit]]
    if len(files) > limit:
        shown.append(f"... and {len(files) - limit} more")
    return shown


def status(label: str, ok: bool) -> str:
    return f"- {label}: {'pass' if ok else 'missing'}"


def main() -> None:
    parser = argparse.ArgumentParser(description="Lightweight reproducibility artifact audit.")
    parser.add_argument("project", help="Project folder to audit")
    args = parser.parse_args()

    root = Path(args.project).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"Project folder not found: {root}")

    files = collect_files(root)
    code = by_suffix(files, CODE_SUFFIXES)
    data = by_suffix(files, DATA_SUFFIXES)
    figures = by_suffix(files, FIGURE_SUFFIXES)
    large = [path for path in files if path.stat().st_size > 50 * 1024 * 1024]

    print("# Reproducibility Artifact Audit")
    print()
    print(f"Project: `{root}`")
    print(f"Files scanned: {len(files)}")
    print()
    print("## Core Checks")
    print(status("README", has_named(files, README_FILES)))
    print(status("License", has_named(files, LICENSE_FILES)))
    print(status("Environment file", has_named(files, ENV_FILES)))
    print(status("Code files", bool(code)))
    print(status("Data-like files", bool(data)))
    print(status("Figure/report files", bool(figures)))
    print()
    print("## Inventory")
    print(f"- Code files: {len(code)}")
    for item in rel_list(root, code):
        print(f"  - `{item}`")
    print(f"- Data-like files: {len(data)}")
    for item in rel_list(root, data):
        print(f"  - `{item}`")
    print(f"- Figure/report files: {len(figures)}")
    for item in rel_list(root, figures):
        print(f"  - `{item}`")
    print()
    print("## Large Files")
    if large:
        for item in rel_list(root, large):
            print(f"- `{item}`")
    else:
        print("- None over 50 MB detected.")
    print()
    print("## Next Steps")
    print("- Confirm which data can be public, controlled-access, or unavailable.")
    print("- Add exact run commands for the main analysis.")
    print("- Record software versions and random seeds where relevant.")


if __name__ == "__main__":
    main()
