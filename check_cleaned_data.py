import pandas as pd

file_path = "data/processed/indian_jobs_cleaned.csv"

df = pd.read_csv(file_path)

print("================================")
print("CLEANED DATASET CHECK")
print("================================")

print("\nRows:", len(df))
print("Columns:", len(df.columns))

print("\n========== SALARY ==========")

print("\nCurrency:")
print(df["currency"].value_counts())

print("\nSalary examples:")
print(df["salary"].drop_duplicates().head(30).to_string(index=False))

print("\nMinimum Salary:")
print(df["minimumSalary"].describe())

print("\nMaximum Salary:")
print(df["maximumSalary"].describe())

print("\nMissing minimum salary:", df["minimumSalary"].isna().sum())
print("Missing maximum salary:", df["maximumSalary"].isna().sum())

print("\n========== EXPERIENCE ==========")

print("\nMissing experience:", df["experience"].isna().sum())

print("\nExperience examples:")
print(df["experience"].value_counts().head(20))

print("\n========== LOCATION ==========")

print("\nUnique locations:", df["location"].nunique())

print("\nTop locations:")
print(df["location"].value_counts().head(30))

print("\n========== SKILLS ==========")

print("\nMissing skills:", df["tagsAndSkills"].isna().sum())

print("\nSkill examples:")
print(
    df["tagsAndSkills"]
    .dropna()
    .head(20)
    .to_string(index=False)
)

print("\n================================")
print("CHECK COMPLETE")
print("================================")