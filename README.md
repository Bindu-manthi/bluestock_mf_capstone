# Bluestock Mutual Fund Analytics Capstone

## Project Overview

The Bluestock Mutual Fund Analytics Capstone Project is an end-to-end financial analytics solution designed to analyze mutual fund performance, investor behavior, market trends, and portfolio risk.

The project integrates data engineering, exploratory data analysis, performance evaluation, advanced risk analytics, and dashboard visualization to generate actionable insights for investors and financial analysts.

The solution was developed using Python, SQLite, Power BI, and various data analytics libraries to create a scalable workflow for mutual fund analysis.

---

## Project Objectives

* Build an automated ETL pipeline for mutual fund datasets.
* Clean and transform raw financial data.
* Store processed datasets in a SQLite database.
* Perform exploratory data analysis (EDA).
* Evaluate mutual fund performance using financial metrics.
* Calculate Alpha, Beta, Sharpe Ratio, VaR, and CVaR.
* Analyze investor behavior and SIP trends.
* Develop an interactive Power BI dashboard.
* Generate investment insights and recommendations.

---

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── db/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│   ├── Advanced_Analytics.ipynb
│
├── screenshots/
│   ├── Industry_Overview.png
│   ├── Fund_Performance.png
│   ├── Investor_Analytics.png
│   └── SIP_Market_Trends.png
│
├── scripts/
│   ├── data_ingestion.py
│   ├── data_cleaning.py
│   ├── database.py
│   ├── etl_pipeline.py
│   └── recommender.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── run_pipeline.py
├── bluestock_mf.db
├── Bluestock_mf_capstone.pbix
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Data Sources

The project uses multiple mutual fund datasets including:

* Fund Master Data
* NAV History Data
* AUM by Fund House Data
* Monthly SIP Inflow Data
* Category Inflow Data
* Industry Folio Count Data
* Scheme Performance Data
* Investor Transaction Data
* Portfolio Holdings Data
* Benchmark Index Data

---

## ETL Pipeline

The ETL pipeline automates data extraction, cleaning, transformation, and storage.

### Pipeline Flow

Raw Datasets → Data Ingestion → Data Cleaning → SQLite Database → Analytics → Dashboard

### Run the Pipeline

```bash
python run_pipeline.py
```

---

## Exploratory Data Analysis

Key analyses include:

* Data validation and quality assessment
* Fund category analysis
* Industry growth trends
* Investor participation analysis
* SIP trend analysis

---

## Performance Analytics

Implemented metrics include:

* CAGR Analysis
* Benchmark Comparison
* Alpha Analysis
* Beta Analysis
* Risk-adjusted Performance Evaluation

---

## Advanced Analytics

Implemented advanced analytics include:

* Historical VaR (95%)
* Conditional VaR (CVaR)
* Rolling Sharpe Ratio
* Investor Cohort Analysis
* SIP Continuity Analysis
* Risk-Based Fund Recommendation System

---

## Dashboard

The Power BI dashboard consists of four major sections:

### Industry Overview

Provides a high-level view of mutual fund industry growth and category distribution.

### Fund Performance

Analyzes fund returns, rankings, and benchmark comparisons.

### Investor Analytics

Evaluates investor participation and transaction behavior.

### SIP & Market Trends

Tracks SIP inflows and long-term investment patterns.

---

## Key Outputs

### Reports

* alpha_beta.csv
* fund_scorecard.csv
* final_fund_scorecard.csv
* var_cvar_report.csv

### Visualizations

* benchmark_comparison.png
* rolling_sharpe_chart.png
* Dashboard screenshots

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* SQLite
* Jupyter Notebook
* Power BI
* Git
* GitHub

---

## Author

**Bindu Madhavi Manthi**

Bluestock Mutual Fund Analytics Capstone Project
