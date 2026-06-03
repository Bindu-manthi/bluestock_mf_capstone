print("===== DATA INGESTION STARTED =====")

import pandas as pd
import os

# Check current working directory
print("\nCurrent Working Directory:")
print(os.getcwd())

# Path to raw data folder
folder_path = "data/raw"

# Check if folder exists
if not os.path.exists(folder_path):
    print(f"\nERROR: Folder not found -> {folder_path}")
else:
    files = os.listdir(folder_path)

    print("\nFiles Found in data/raw:")
    print(files)

    csv_files = [file for file in files if file.endswith(".csv")]

    print(f"\nTotal CSV Files Found: {len(csv_files)}")

    for file in csv_files:

        print("\n" + "=" * 60)
        print(f"FILE NAME: {file}")

        file_path = os.path.join(folder_path, file)

        try:
            df = pd.read_csv(file_path)

            print("\nShape:")
            print(df.shape)

            print("\nColumns:")
            print(df.columns.tolist())

            print("\nData Types:")
            print(df.dtypes)

            print("\nFirst 5 Rows:")
            print(df.head())

            print("\nMissing Values:")
            print(df.isnull().sum())

        except Exception as e:
            print(f"\nError reading {file}")
            print(e)

print("\n===== DATA INGESTION COMPLETED =====")