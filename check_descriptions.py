import json

with open("data/raw/adzuna_jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

lengths = []

for job in jobs:
    description = job.get("description", "")
    lengths.append(len(description))

print("================================")
print("DESCRIPTION LENGTH CHECK")
print("================================")

print("Total jobs:", len(jobs))
print("Shortest description:", min(lengths), "characters")
print("Longest description:", max(lengths), "characters")
print("Average description:", round(sum(lengths) / len(lengths), 2), "characters")

print("\n========== SHORTEST 10 ==========")

shortest = sorted(jobs, key=lambda x: len(x.get("description", "")))

for job in shortest[:10]:
    print(
        len(job.get("description", "")),
        "|",
        job.get("title"),
        "|",
        job.get("company")
    )

print("\n========== LONGEST 10 ==========")

longest = sorted(
    jobs,
    key=lambda x: len(x.get("description", "")),
    reverse=True
)

for job in longest[:10]:
    print(
        len(job.get("description", "")),
        "|",
        job.get("title"),
        "|",
        job.get("company")
    )

print("\n================================")
print("CHECK COMPLETE")
print("================================")