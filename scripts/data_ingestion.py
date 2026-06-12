print("===== DATA INGESTION STARTED =====")

import pandas as pd
import os

folder_path = "data/raw"

if not os.path.exists(folder_path):
    print(f"ERROR: Folder not found -> {folder_path}")

else:
    files = os.listdir(folder_path)
    csv_files = [file for file in files if file.endswith(".csv")]

    print(f"Total CSV Files Found: {len(csv_files)}")

    for file in csv_files:

        file_path = os.path.join(folder_path, file)

        try:
            df = pd.read_csv(file_path)

            print(f"Loaded: {file} | Rows: {df.shape[0]} | Columns: {df.shape[1]}")

        except Exception as e:
            print(f"Error reading {file}: {e}")

print("===== DATA INGESTION COMPLETED =====")