# Data Quality Summary

## Dataset Overview

Total datasets loaded: 10

### Dataset Details

| Dataset | Rows | Columns |
|----------|------|---------|
| Fund Master | 40 | 15 |
| NAV History | 46000 | 3 |
| AUM by Fund House | 90 | 5 |
| Monthly SIP Inflows | 48 | 6 |
| Category Inflows | 144 | 3 |
| Industry Folio Count | 21 | 6 |
| Scheme Performance | 40 | 19 |
| Investor Transactions | 32778 | 13 |
| Portfolio Holdings | 322 | 8 |
| Benchmark Indices | 8050 | 3 |

## Missing Values

Only Monthly SIP Inflows contains missing values:

- yoy_growth_pct : 12 missing values

Reason:
First-year records do not have previous-year data for YoY calculation.

## Data Quality Assessment

- No missing values in critical datasets.
- No schema issues detected.
- All AMFI codes appear properly formatted.
- Date columns require conversion to datetime format during cleaning stage.

## Status

Data ingestion completed successfully.