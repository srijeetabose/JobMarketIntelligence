import pandas as pd
import re

input_file = "data/processed/indian_jobs_salary_cleaned.csv"
output_file = "data/processed/indian_jobs_location_cleaned.csv"

print("================================")
print("CREATING LOCATION FIELDS")
print("================================")

# --------------------------------------------------
# 1. Load dataset
# --------------------------------------------------

df = pd.read_csv(input_file)

print("\nTotal jobs:", len(df))


# --------------------------------------------------
# 2. Clean original location text
# --------------------------------------------------

df["location_clean"] = (
    df["location"]
    .astype(str)
    .str.strip()
)


# --------------------------------------------------
# 3. Identify work mode
# --------------------------------------------------

def get_work_mode(location):

    loc = location.lower().strip()

    if "remote" in loc:
        return "Remote"

    if "hybrid" in loc:
        return "Hybrid"

    # We cannot assume a normal city means on-site
    if "," in loc:
        return "Multi-city"

    return "Not specified"


df["work_mode"] = df["location_clean"].apply(get_work_mode)


# --------------------------------------------------
# 4. Extract primary location
# --------------------------------------------------

def get_primary_location(location):

    loc = location.strip()

    # Remote
    if loc.lower() == "remote":
        return "Remote"

    # Remove Hybrid prefix
    loc = re.sub(
        r"^hybrid\s*-\s*",
        "",
        loc,
        flags=re.IGNORECASE
    )

    # If multiple cities are listed
    if "," in loc:
        return "Multiple"

    # Remove details inside brackets
    loc = re.sub(r"\s*\(.*?\)", "", loc)

    # Remove extra spaces
    loc = re.sub(r"\s+", " ", loc).strip()

    return loc


df["primary_location"] = df["location_clean"].apply(
    get_primary_location
)


# --------------------------------------------------
# 5. Show examples
# --------------------------------------------------

print("\n========== LOCATION EXAMPLES ==========")

print(
    df[
        [
            "location",
            "work_mode",
            "primary_location"
        ]
    ]
    .drop_duplicates()
    .head(50)
    .to_string(index=False)
)


# --------------------------------------------------
# 6. Work mode distribution
# --------------------------------------------------

print("\n========== WORK MODE ==========")

print(
    df["work_mode"].value_counts()
)


# --------------------------------------------------
# 7. Top locations
# --------------------------------------------------

print("\n========== TOP LOCATIONS ==========")

print(
    df["primary_location"]
    .value_counts()
    .head(30)
)


# --------------------------------------------------
# 8. Save
# --------------------------------------------------

df.to_csv(output_file, index=False)

print("\nSaved to:")
print(output_file)

print("\nFinal columns:", len(df.columns))

print("\n================================")
print("LOCATION CLEANING COMPLETE")
print("================================")