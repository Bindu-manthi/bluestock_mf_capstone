"""
etl_pipeline.py

Master ETL pipeline for the
Bluestock Mutual Fund Analytics Project.
"""

import subprocess

def main():
    print("===== ETL PIPELINE STARTED =====")

    print("\nRunning Data Ingestion...")
    subprocess.run(["python", "scripts/data_ingestion.py"])

    print("\nRunning Data Cleaning...")
    subprocess.run(["python", "scripts/data_cleaning.py"])

    print("\n===== ETL PIPELINE COMPLETED =====")


if __name__ == "__main__":
    main()