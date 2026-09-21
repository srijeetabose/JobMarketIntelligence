import pandas as pd
import os


file_path = "data/raw/indian-job-market-dataset-2025.xlsx"

df = pd.read_excel(file_path)


print("================================")
print("DATASET INSPECTION")
print("================================")

print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\n========== COLUMNS ==========")

for column in df.columns:
    print("-", column)


print("\n========== FIRST 5 ROWS ==========")

print(df.head())


print("\n========== DATA TYPES ==========")

print(df.dtypes)


print("\n========== MISSING VALUES ==========")

print(df.isnull().sum())


print("\n========== DUPLICATES ==========")

print("Duplicate rows:", df.duplicated().sum())


print("\n========== UNIQUE VALUES ==========")

for column in df.columns:

    if df[column].dtype == "object":

        print(
            f"{column}: {df[column].nunique()}"
        )


print("\n================================")
print("INSPECTION COMPLETE")
print("================================")