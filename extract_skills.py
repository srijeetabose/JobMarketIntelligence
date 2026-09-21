import pandas as pd
import re

input_file = "data/processed/indian_jobs_jobfamily_cleaned.csv"
output_file = "data/processed/indian_jobs_skills_cleaned.csv"

print("================================")
print("EXTRACTING JOB SKILLS")
print("================================")

df = pd.read_csv(input_file)


# --------------------------------------------------
# Common skill dictionary
# --------------------------------------------------

skill_dictionary = {

    # Programming
    "Python": ["python"],
    "Java": ["java"],
    "C++": ["c++"],
    "C": ["c"],
    "C#": ["c#"],
    ".NET": [".net", "dot net"],
    "PHP": ["php"],
    "JavaScript": ["javascript"],
    "TypeScript": ["typescript"],
    "Dart": ["dart"],

    # Data
    "SQL": ["sql", "mysql", "mariadb", "postgresql", "postgres"],
    "Excel": ["excel", "microsoft excel", "ms excel"],
    "Power BI": ["power bi", "powerbi"],
    "Tableau": ["tableau"],
    "Data Analysis": ["data analysis", "data analytics"],
    "Data Visualization": ["data visualization"],
    "Machine Learning": ["machine learning"],
    "Deep Learning": ["deep learning"],
    "NLP": ["natural language processing", "nlp"],
    "Computer Vision": ["computer vision"],

    # Cloud / DevOps
    "AWS": ["aws", "amazon web services"],
    "Azure": ["azure", "microsoft azure"],
    "Azure DevOps": ["azure devops"],
    "GCP": ["gcp", "google cloud"],
    "Docker": ["docker"],
    "Kubernetes": ["kubernetes"],
    "DevOps": ["devops"],
    "Linux": ["linux"],

    # Software
    "React": ["react", "react js", "reactjs"],
    "Angular": ["angular"],
    "Node.js": ["node.js", "nodejs"],
    "Flutter": ["flutter"],
    "Android": ["android"],
    "Git": ["git", "github"],
    "REST API": ["rest api", "restful api"],

    # Databases
    "MongoDB": ["mongodb", "mongo db"],
    "Oracle": ["oracle"],
    "SAP": ["sap"],
    "ERP": ["erp"],

    # Engineering / Design
    "AutoCAD": ["autocad"],
    "SolidWorks": ["solid works", "solidworks"],
    "CAD": ["cad"],
    "CATIA": ["catia"],
    "Tekla": ["tekla"],
    "CFD": ["cfd"],
    "Simulation": ["simulation"],
    "Mechanical Design": ["mechanical design"],
    "Product Design": ["product design"],

    # Finance
    "GST": ["gst", "gst filing"],
    "Tally": ["tally"],
    "Taxation": ["tax", "tax audit", "taxation"],
    "Accounting": ["accounting", "accounts"],
    "Financial Reporting": ["financial reporting"],
    "Auditing": ["audit", "auditing"],

    # HR
    "Recruitment": ["recruitment", "recruiting"],
    "Talent Acquisition": ["talent acquisition"],
    "HR": ["human resource", "human resources", "hr"],

    # Sales / Marketing
    "Sales": ["sales"],
    "Business Development": ["business development"],
    "Digital Marketing": ["digital marketing"],
    "Performance Marketing": ["performance marketing"],
    "Product Marketing": ["product marketing"],
    "Lead Generation": ["lead generation"],

    # Customer Service
    "Customer Service": ["customer service"],
    "Customer Support": ["customer support"],
    "Chat Support": ["chat support"],
    "Call Center": ["call center", "call centre"],
    "BPO": ["bpo"],

    # Healthcare
    "Healthcare": ["healthcare"],
    "Medical Billing": ["medical billing"],
    "Clinical": ["clinical"],

    # Other useful professional skills
    "Project Management": ["project management"],
    "Supply Chain": ["supply chain"],
    "Procurement": ["procurement"],
    "Logistics": ["logistics"],
    "Risk Management": ["risk management"],
    "Fraud Prevention": ["fraud prevention"],
    "KYC": ["kyc"],
    "Compliance": ["compliance"],
    "Communication": ["communication", "communication skills"],
}


# --------------------------------------------------
# Extract skills from tags
# --------------------------------------------------

def extract_skills(tags):

    if pd.isna(tags):
        return []

    text = str(tags).lower()

    found = []

    for skill, keywords in skill_dictionary.items():

        for keyword in keywords:

            keyword = keyword.lower()

            # Special handling for short skills
            if keyword in ["c", "c++", "c#", "hr"]:
                pattern = r"(?<![a-z])" + re.escape(keyword) + r"(?![a-z])"
            else:
                pattern = r"(?<![a-z])" + re.escape(keyword) + r"(?![a-z])"

            if re.search(pattern, text):
                found.append(skill)
                break

    return found


df["extracted_skills"] = df["tagsAndSkills"].apply(extract_skills)

df["skill_count"] = df["extracted_skills"].apply(len)


# Convert list to readable text
df["extracted_skills"] = df["extracted_skills"].apply(
    lambda x: ", ".join(x)
)


print("\n========== SKILL EXTRACTION ==========")

print(
    df[
        [
            "title",
            "job_family",
            "tagsAndSkills",
            "extracted_skills"
        ]
    ]
    .drop_duplicates()
    .head(30)
    .to_string(index=False)
)


print("\n========== SKILL COUNT ==========")

print(
    df["skill_count"]
    .value_counts()
    .sort_index()
)


df.to_csv(output_file, index=False)

print("\nSaved to:")
print(output_file)

print("\nFinal columns:", len(df.columns))

print("\n================================")
print("SKILL EXTRACTION COMPLETE")
print("================================")