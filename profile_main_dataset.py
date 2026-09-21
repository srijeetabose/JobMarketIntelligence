import pandas as pd

file_path = "data/raw/indian-job-market-dataset-2025.xlsx"

df = pd.read_excel(file_path)

print("================================")
print("DETAILED DATASET PROFILING")
print("================================")

print("\nRows:", len(df))
print("Columns:", len(df.columns))

# --------------------------------------------------
# JOB ID
# --------------------------------------------------

print("\n========== JOB ID ==========")
print("Total job IDs:", df["jobId"].nunique())
print("Duplicate job IDs:", df["jobId"].duplicated().sum())

# --------------------------------------------------
# TITLES
# --------------------------------------------------

print("\n========== TOP JOB TITLES ==========")
print(df["title"].value_counts().head(30))

print("\nUnique job titles:", df["title"].nunique())

# --------------------------------------------------
# COMPANIES
# --------------------------------------------------

print("\n========== TOP COMPANIES ==========")
print(df["companyName"].value_counts().head(20))

print("\nUnique companies:", df["companyName"].nunique())

# --------------------------------------------------
# LOCATIONS
# --------------------------------------------------

print("\n========== TOP LOCATIONS ==========")
print(df["location"].value_counts().head(30))

print("\nUnique locations:", df["location"].nunique())

# --------------------------------------------------
# EXPERIENCE
# --------------------------------------------------

print("\n========== EXPERIENCE ==========")
print(df["experience"].value_counts().head(30))

print("\nUnique experience values:", df["experience"].nunique())

print("\nMinimum experience statistics:")
print(df["minimumExperience"].describe())

print("\nMaximum experience statistics:")
print(df["maximumExperience"].describe())

# --------------------------------------------------
# SALARY
# --------------------------------------------------

print("\n========== SALARY ==========")
print("Unique currencies:")
print(df["currency"].value_counts())

print("\nSalary examples:")
print(df["salary"].head(20).to_string(index=False))

print("\nMinimum salary statistics:")
print(df["minimumSalary"].describe())

print("\nMaximum salary statistics:")
print(df["maximumSalary"].describe())

# --------------------------------------------------
# SKILLS
# --------------------------------------------------

print("\n========== SKILLS / TAGS ==========")
print("Missing skills:", df["tagsAndSkills"].isna().sum())

print("\nSkill examples:")
print(df["tagsAndSkills"].dropna().head(20).to_string(index=False))

# --------------------------------------------------
# JOB UPLOAD DATE
# --------------------------------------------------

print("\n========== JOB UPLOAD DATE ==========")
print(df["jobUploaded"].head(20).to_string(index=False))

# --------------------------------------------------
# RATINGS
# --------------------------------------------------

print("\n========== COMPANY RATINGS ==========")
print("Missing ratings:", df["AggregateRating"].isna().sum())

print(df["AggregateRating"].describe())

print("\n========== REVIEW COUNTS ==========")
print("Missing review counts:", df["ReviewsCount"].isna().sum())

print(df["ReviewsCount"].describe())

# --------------------------------------------------
# DESCRIPTIONS
# --------------------------------------------------

print("\n========== JOB DESCRIPTIONS ==========")

description_lengths = df["jobDescription"].astype(str).str.len()

print("Minimum description length:", description_lengths.min())
print("Maximum description length:", description_lengths.max())
print("Average description length:", description_lengths.mean())

# --------------------------------------------------
# DUPLICATES
# --------------------------------------------------

print("\n========== DUPLICATES ==========")

print("Duplicate complete rows:", df.duplicated().sum())

print("Duplicate job IDs:", df["jobId"].duplicated().sum())

# --------------------------------------------------
# FINAL
# --------------------------------------------------

print("\n================================")
print("PROFILING COMPLETE")
print("================================")