# 📊 Bluestock Mutual Fund Analytics Capstone

## 📌 Project Overview
This project analyzes Indian mutual fund data using Python, SQL, and data visualization techniques. It covers NAV trends, SIP inflows, AUM growth, and fund performance evaluation using financial metrics and benchmark comparison.

---

## 🎯 Objectives
- Clean and process mutual fund datasets  
- Build SQLite database using star schema  
- Perform exploratory data analysis (EDA)  
- Calculate financial performance metrics  
- Build fund ranking scorecard system  
- Compare funds with benchmark indices  

---

## 📁 Project Structure

bluestock_mf_capstone/

├── data/
│   ├── raw/
│   │   ├── 01_fund_master.csv
│   │   ├── 02_nav_history.csv
│   │   ├── 03_aum_by_fund_house.csv
│   │   ├── 04_monthly_sip_inflows.csv
│   │   ├── 05_category_inflows.csv
│   │   ├── 06_industry_folio_count.csv
│   │   ├── 07_scheme_performance.csv
│   │   ├── 08_investor_transactions.csv
│   │   ├── 09_portfolio_holdings.csv
│   │   ├── 10_benchmark_indices.csv
│   │   └── HDFC_Top100_live_nav.csv
│
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   ├── Performance_Analytics.ipynb
│
├── scripts/
│   ├── data_ingestion.py
│   ├── live_nav_fetch.py
│   ├── data_cleaning.py
│
├── sql/
│   ├── schema.sql
│   ├── queries.sql
│
├── reports/
│   ├── data_dictionary.md
│
├── dashboard/
├── requirements.txt
├── README.md
└── .gitignore

---

## 🛠️ Technologies Used
- Python 🐍  
- Pandas, NumPy  
- SQLite, SQLAlchemy  
- Matplotlib, Seaborn, Plotly  
- Jupyter Notebook  
- Git & GitHub  

---

## 📅 Project Workflow

### 🟢 Day 1: Data Ingestion
- Loaded multiple CSV datasets  
- Fetched live NAV data using API  
- Validated AMFI scheme codes  
- Organized project structure  

---

### 🟡 Day 2: Data Cleaning & SQL
- Cleaned NAV and transaction datasets  
- Standardized formats and removed errors  
- Designed SQLite star schema  
- Loaded data into database  
- Created SQL queries  

---

### 🔵 Day 3: Exploratory Data Analysis (EDA)
- NAV trend analysis (2022–2026)  
- SIP inflows and AUM growth  
- Investor demographics analysis  
- Geographic distribution  
- Correlation heatmaps  
- 15+ visualizations created  

---

### 🟣 Day 4: Performance Analytics
- Daily returns calculation  
- CAGR (1Y, 3Y, 5Y)  
- Sharpe & Sortino ratios  
- Alpha & Beta vs Nifty 100  
- Maximum Drawdown analysis  
- Fund Scorecard (0–100 ranking model)  
- Benchmark comparison (Nifty 50 vs Nifty 100)  

---

## 📊 Key Insights
- SIP inflows show consistent growth over time  
- Large-cap funds are more stable and less volatile  
- Fund performance varies significantly across categories  
- Top funds consistently outperform benchmarks  
- Risk-adjusted metrics are critical for fund selection  

---

## 📦 Final Outputs
- fund_scorecard.csv  
- alpha_beta.csv  
- benchmark_comparison.png  
- Cleaned datasets  
- EDA charts and insights  

---

## 🚀 Future Improvements
- Streamlit dashboard for interactive analysis  
- Real-time NAV tracking system  
- Predictive modeling for fund performance  
- Automated reporting system  

---

## 👨‍💻 Author
**Bindu Madhavi Manthi**  
Data Analyst Intern – Bluestock Fintech  

---

## 🏁 Conclusion
This project builds a complete mutual fund analytics pipeline covering data engineering, SQL modeling, exploratory analysis, and financial performance evaluation.

---
