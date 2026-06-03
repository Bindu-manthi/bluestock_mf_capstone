import pandas as pd
import sqlite3

# Load cleaned data
nav = pd.read_csv("data/processed/nav_history_cleaned.csv")
txn = pd.read_csv("data/processed/transactions_cleaned.csv")
perf = pd.read_csv("data/processed/performance_cleaned.csv")

# Create database
conn = sqlite3.connect("bluestock_mf.db")

# Save tables
nav.to_sql("fact_nav", conn, if_exists="replace", index=False)
txn.to_sql("fact_transactions", conn, if_exists="replace", index=False)
perf.to_sql("fact_performance", conn, if_exists="replace", index=False)

print("Database created successfully!")
conn.close()