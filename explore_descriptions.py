import json
import re

with open("data/raw/adzuna_jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

print("================================")
print("ADZUNA DESCRIPTION INSPECTION")
print("================================")

for i, job in enumerate(jobs[:10], start=1):

    print("\n" + "=" * 80)

    print(f"JOB {i}")
    print("Title:", job.get("title"))
    print("Company:", job.get("company"))
    print("Location:", job.get("location"))
    print("Search term:", job.get("search_term"))

    description = job.get("description", "")

    # Remove excessive whitespace
    description = re.sub(r"\s+", " ", description)

    print("\nDESCRIPTION:")
    print(description[:1500])

print("\n" + "=" * 80)
print("INSPECTION COMPLETE")