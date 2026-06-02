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