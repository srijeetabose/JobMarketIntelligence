import pandas as pd

input_file = "data/processed/indian_jobs_cleaned.csv"
output_file = "data/processed/indian_jobs_salary_cleaned.csv"

df = pd.read_csv(input_file)

print("================================")
print("CREATING SALARY FIELDS")
print("================================")

# --------------------------------------------------
# 1. Salary availability
# --------------------------------------------------

df["salary_available"] = (
    (df["currency"] == "INR") &
    df["minimumSalary"].notna() &
    df["maximumSalary"].notna()
)

# --------------------------------------------------
# 2. Flag suspiciously low INR salaries
# --------------------------------------------------

df["salary_suspicious"] = (
    (df["currency"] == "INR") &
    (
        (df["minimumSalary"] < 10000) |
        (df["maximumSalary"] < 10000)
    )
)

# --------------------------------------------------
# 3. Create midpoint salary
# --------------------------------------------------

df["salary_midpoint_inr"] = (
    df["minimumSalary"] + df["maximumSalary"]
) / 2

# --------------------------------------------------
# 4. Make invalid/suspicious salary values unavailable
# --------------------------------------------------

df.loc[df["salary_suspicious"], "salary_midpoint_inr"] = pd.NA

# --------------------------------------------------
# 5. Save
# --------------------------------------------------

df.to_csv(output_file, index=False)

print("\nTotal jobs:", len(df))

print(
    "Jobs with usable INR salary:",
    df["salary_available"].sum()
)

print(
    "Suspicious salary records:",
    df["salary_suspicious"].sum()
)

print(
    "Usable salary midpoint values:",
    df["salary_midpoint_inr"].notna().sum()
)

print("\nSaved to:")
print(output_file)

print("\n================================")
print("SALARY CLEANING COMPLETE")
print("================================")