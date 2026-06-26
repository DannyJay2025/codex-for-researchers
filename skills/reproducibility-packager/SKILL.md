---
name: reproducibility-packager
description: Audit and prepare research code, data, methods, environment files, and availability statements for manuscript submission. Use when the user provides a project folder, code repository, analysis notebook, dataset inventory, methods text, or asks for reproducibility checks, data/code availability wording, repository packaging, submission readiness, or FAIR-style research artifact organization.
---

# Reproducibility Packager

## Workflow

1. Inspect the provided project folder or artifact list.
2. Identify research artifacts: code, notebooks, raw data, processed data, environment files, figures, tables, model weights, protocols, and documentation.
3. Run `scripts/audit_reproducibility.py` when a local folder is available.
4. Compare the project against `references/reproducibility-checklist.md`.
5. Produce a submission-readiness report with blockers, quick fixes, and optional polish.

## Output Contract

Include:

- Artifact inventory.
- Missing or weak items.
- Reproducibility risks.
- Suggested repository structure.
- Draft code availability statement.
- Draft data availability statement.
- Environment and execution notes.
- Final checklist with pass, partial, fail, or unknown status.

## Availability Statement Rules

- Do not promise public data/code release if the user has not confirmed it.
- For sensitive, proprietary, licensed, or human-subject data, suggest controlled-access wording.
- Separate code availability from data availability.
- Include accession numbers, repository URLs, commit hashes, and license details only when provided or verified.

## Script

Use:

```bash
python skills/reproducibility-packager/scripts/audit_reproducibility.py <project-folder>
```

The script performs a lightweight file inventory. It does not prove reproducibility; use its output as evidence for the final human-readable audit.
