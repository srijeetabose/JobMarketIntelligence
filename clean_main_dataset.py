import pandas as pd
import os

input_file = "data/raw/indian-job-market-dataset-2025.xlsx"
output_file = "data/processed/indian_jobs_cleaned.csv"

print("================================")
print("MAIN DATASET CLEANING")
print("================================")

# Load dataset
df = pd.read_excel(input_file)

print("\nOriginal rows:", len(df))

# --------------------------------------------------
# 1. Remove duplicate job IDs
# --------------------------------------------------

before = len(df)

df = df.drop_duplicates(subset="jobId", keep="first")

after = len(df)

print("\nDuplicate job IDs removed:", before - after)
print("Rows after duplicate removal:", after)

# --------------------------------------------------
# 2. Convert blank strings to missing values
# --------------------------------------------------

df = df.replace(r"^\s*$", pd.NA, regex=True)

# --------------------------------------------------
# 3. Treat zero salary values as missing
# --------------------------------------------------

df.loc[df["minimumSalary"] == 0, "minimumSalary"] = pd.NA
df.loc[df["maximumSalary"] == 0, "maximumSalary"] = pd.NA

# --------------------------------------------------
# 4. Save cleaned dataset
# --------------------------------------------------

os.makedirs("data/processed", exist_ok=True)

df.to_csv(output_file, index=False)

print("\nSaved cleaned dataset to:")
print(output_file)

print("\nFinal rows:", len(df))
print("Final columns:", len(df.columns))

print("\n========== REMAINING DUPLICATES ==========")
print("Duplicate job IDs:", df["jobId"].duplicated().sum())
print("Duplicate complete rows:", df.duplicated().sum())

print("\n================================")
print("CLEANING COMPLETE")
print("================================")