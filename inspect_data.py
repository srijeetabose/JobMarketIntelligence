import json

# Load raw dataset
with open("data/raw/adzuna_jobs.json", "r", encoding="utf-8") as f:
    jobs = json.load(f)

print("================================")
print("JOB MARKET DATA INSPECTION")
print("================================")

print("Total jobs:", len(jobs))

# 1. Descriptions
with_description = sum(
    1 for job in jobs
    if job.get("description")
)

print("\n========== DESCRIPTIONS ==========")
print("With description:", with_description)
print("Without description:", len(jobs) - with_description)


# 2. Salary
with_salary = sum(
    1 for job in jobs
    if job.get("salary_min") is not None
)

print("\n========== SALARY ==========")
print("With salary:", with_salary)
print("Without salary:", len(jobs) - with_salary)


# 3. Duplicate IDs
job_ids = [job.get("job_id") for job in jobs]

print("\n========== DUPLICATES ==========")
print("Total job IDs:", len(job_ids))
print("Unique job IDs:", len(set(job_ids)))
print("Duplicate jobs:", len(job_ids) - len(set(job_ids)))


# 4. Categories
categories = {}

for job in jobs:
    category = job.get("category")

    if category:
        categories[category] = categories.get(category, 0) + 1

print("\n========== CATEGORIES ==========")

for category, count in sorted(
    categories.items(),
    key=lambda x: x[1],
    reverse=True
):
    print(category, ":", count)


# 5. Locations
locations = {}

for job in jobs:
    location = job.get("location")

    if location:
        locations[location] = locations.get(location, 0) + 1

print("\n========== TOP LOCATIONS ==========")

for location, count in sorted(
    locations.items(),
    key=lambda x: x[1],
    reverse=True
)[:20]:
    print(location, ":", count)


# 6. Search terms
search_terms = {}

for job in jobs:
    term = job.get("search_term")

    if term:
        search_terms[term] = search_terms.get(term, 0) + 1

print("\n========== SEARCH TERMS ==========")

for term, count in search_terms.items():
    print(term, ":", count)


print("\n================================")
print("INSPECTION COMPLETE")
print("================================")