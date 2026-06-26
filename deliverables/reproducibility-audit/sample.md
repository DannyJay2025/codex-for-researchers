# Sample Deliverable: Reproducibility Package Audit

## Scope

Input type: sample project inventory.

No customer files are included in this public sample.

## Artifact Inventory

| Artifact | Status | Notes |
| --- | --- | --- |
| README | Partial | Explains project purpose but lacks exact run command |
| Environment file | Missing | Add `requirements.txt`, `environment.yml`, or `Dockerfile` |
| Code entry point | Partial | Main notebook exists but execution order is unclear |
| Data | Unknown | Public/private status not specified |
| Figures | Partial | Generated figures present, but generation script not identified |
| License | Missing | Add license or usage restriction statement |

## Main Risks

- Results may not be reproducible without a locked environment.
- Data availability wording is currently too vague.
- Figure generation path is unclear.

## Draft Code Availability

```text
Code supporting this study will be made available in a public repository upon publication. The repository will include analysis scripts, environment information, and instructions for reproducing the main figures.
```

## Draft Data Availability

```text
Data availability will depend on the source and access restrictions of the datasets used. Public datasets should be cited with accession numbers or repository URLs; restricted datasets should include access instructions.
```

## Next Actions

1. Add exact run commands to README.
2. Add environment lock file.
3. Separate raw data, processed data, and generated outputs.
4. Add code and data availability statements to the manuscript.
