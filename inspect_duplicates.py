import pandas as pd

file_path = "data/raw/indian-job-market-dataset-2025.xlsx"

df = pd.read_excel(file_path)

print("================================")
print("DUPLICATE JOB ID ANALYSIS")
print("================================")

# Find duplicated job IDs
duplicate_ids = df[df["jobId"].duplicated(keep=False)].sort_values("jobId")

print("\nTotal duplicate rows:", len(duplicate_ids))
print("Unique duplicated job IDs:", duplicate_ids["jobId"].nunique())

print("\n========== DUPLICATE ID COUNTS ==========")
print(
    duplicate_ids["jobId"]
    .value_counts()
    .head(20)
)

print("\n========== EXAMPLE DUPLICATE RECORDS ==========")

for job_id in duplicate_ids["jobId"].drop_duplicates().head(5):

    print("\n--------------------------------")
    print("JOB ID:", job_id)
    print("--------------------------------")

    records = duplicate_ids[duplicate_ids["jobId"] == job_id]

    print(
        records[
            [
                "jobId",
                "title",
                "companyName",
                "location",
                "experience",
                "salary"
            ]
        ].to_string(index=False)
    )

print("\n================================")
print("DUPLICATE ANALYSIS COMPLETE")
print("================================")