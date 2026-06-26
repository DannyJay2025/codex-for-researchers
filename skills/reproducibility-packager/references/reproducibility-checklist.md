# Reproducibility Checklist

## Required

- README explains purpose, inputs, outputs, and how to run the analysis.
- License is present or release restrictions are stated.
- Environment is captured with one of: `requirements.txt`, `environment.yml`, `pyproject.toml`, `renv.lock`, `Dockerfile`, or similar.
- Code entry point is clear.
- Random seeds and stochastic steps are documented when relevant.
- Raw and processed data are separated or clearly labeled.
- Figure/table generation steps are documented.
- Data availability statement is truthful and specific.
- Code availability statement is truthful and specific.

## Strongly Recommended

- Example command or notebook reproduces a minimal result.
- Versioned release, commit hash, DOI, or archive target is identified.
- Large files and private data are excluded from the public repository.
- External datasets include access instructions and citations.
- Generated outputs are stored separately from source data and code.

## Status Labels

- Pass: adequate for submission.
- Partial: present but unclear or incomplete.
- Fail: missing or misleading.
- Unknown: cannot be assessed from available files.
