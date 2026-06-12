
"""
data_cleaning.py

This script cleans and preprocesses
NAV history, investor transaction,
and scheme performance datasets
for further analysis.
"""

import pandas as pd

# =====================================================
# NAV HISTORY CLEANING
# =====================================================

print("NAV History cleaning started")

# Load NAV History
nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
nav["date"] = pd.to_datetime(nav["date"])

# Sort records
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicate records
nav = nav.drop_duplicates()

# Check invalid NAV values
invalid_nav = (nav["nav"] <= 0).sum()
print(f"Invalid NAV values found: {invalid_nav}")

# Save cleaned dataset
nav.to_csv("data/processed/nav_history_cleaned.csv", index=False)

print("NAV History cleaned successfully!")


# =====================================================
# INVESTOR TRANSACTION CLEANING
# =====================================================

print("Transactions cleaning started")

# Load transactions data
txn = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert transaction date
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"],
    errors="coerce"
)

# Standardize transaction types
txn["transaction_type"] = txn["transaction_type"].str.upper()

# Keep only valid transaction types
txn = txn[
    txn["transaction_type"].isin(
        ["SIP", "LUMPSUM", "REDEMPTION"]
    )
]

# Remove invalid transaction amounts
txn = txn[txn["amount_inr"] > 0]

# Save cleaned dataset
txn.to_csv(
    "data/processed/transactions_cleaned.csv",
    index=False
)

print("Transactions cleaned successfully!")


# =====================================================
# SCHEME PERFORMANCE CLEANING
# =====================================================

print("Performance cleaning started")

# Load performance data
perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

# Convert selected columns to numeric
cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "expense_ratio_pct"
]

perf[cols] = perf[cols].apply(
    pd.to_numeric,
    errors="coerce"
)

# Filter valid expense ratios
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

# Save cleaned dataset
perf.to_csv(
    "data/processed/performance_cleaned.csv",
    index=False
)

print("Performance cleaned successfully!")

print("===== DATA CLEANING COMPLETED =====")