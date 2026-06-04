import pandas as pd

# Load NAV History
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort values
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Check invalid NAV values
invalid_nav = (nav["nav"] <= 0).sum()
print("Invalid NAV values:", invalid_nav)

# Save cleaned data
nav.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("NAV History cleaned successfully!")          

print("Transactions cleaning started")

txn = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date column
txn["transaction_date"] = pd.to_datetime(txn["transaction_date"], errors="coerce")

# Standardize transaction type
txn["transaction_type"] = txn["transaction_type"].str.upper()

# Keep valid types
txn = txn[txn["transaction_type"].isin(["SIP", "LUMPSUM", "REDEMPTION"])]

# Fix amount column (IMPORTANT CHANGE)
txn = txn[txn["amount_inr"] > 0]

txn.to_csv("data/processed/transactions_cleaned.csv", index=False)

print("Transactions done")

print("Performance cleaning started")

perf = pd.read_csv("data/raw/07_scheme_performance.csv")

cols = ["return_1yr_pct", "return_3yr_pct", "expense_ratio_pct"]

perf[cols] = perf[cols].apply(pd.to_numeric, errors="coerce")

perf = perf[(perf["expense_ratio_pct"] >= 0.1) & (perf["expense_ratio_pct"] <= 2.5)]

perf.to_csv("data/processed/performance_cleaned.csv", index=False)

print("Performance done")