import pandas as pd
import re

input_file = "data/processed/indian_jobs_location_cleaned.csv"
output_file = "data/processed/indian_jobs_jobfamily_cleaned.csv"

print("================================")
print("CREATING JOB FAMILY")
print("================================")

df = pd.read_csv(input_file)


def contains_any(title, keywords):
    for keyword in keywords:
        pattern = r"\b" + re.escape(keyword.lower()) + r"\b"
        if re.search(pattern, title):
            return True
    return False


def classify_job(title):

    title = str(title).lower().strip()

    # -----------------------------
    # AI / ML
    # -----------------------------
    if contains_any(title, [
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "computer vision",
        "natural language processing",
        "nlp engineer",
        "ml engineer",
        "ai engineer",
        "ai/ml",
        "ai / ml",
        "data scientist"
    ]):
        return "AI / ML"

    # -----------------------------
    # Data & Analytics
    # -----------------------------
    if contains_any(title, [
        "data analyst",
        "data engineer",
        "data architect",
        "data analytics",
        "business analyst",
        "business intelligence",
        "bi analyst",
        "mis analyst",
        "mis executive",
        "reporting analyst",
        "analytics",
        "decision analyst"
    ]):
        return "Data & Analytics"

    # -----------------------------
    # Cybersecurity
    # -----------------------------
    if contains_any(title, [
        "cybersecurity",
        "cyber security",
        "information security",
        "security architect",
        "security engineer",
        "security analyst"
    ]):
        return "Cybersecurity"

    # -----------------------------
    # SAP / ERP
    # -----------------------------
    if contains_any(title, [
        "sap",
        "erp",
        "oracle erp",
        "erp consultant"
    ]):
        return "SAP / ERP"

    # -----------------------------
    # Banking / Insurance
    # -----------------------------
    if contains_any(title, [
        "banking",
        "bank",
        "gold loan",
        "home loan",
        "retail forex",
        "forex",
        "lending",
        "credit card",
        "credit",
        "branch teller",
        "teller",
        "relationship manager",
        "relationship officer",
        "insurance",
        "underwriting",
        "claims",
        "loan officer",
        "loan manager",
        "risk manager",
        "fraud"
    ]):
        return "Banking / Insurance"

    # -----------------------------
    # Design / Creative
    # -----------------------------
    if contains_any(title, [
        "graphic designer",
        "ui designer",
        "ux designer",
        "ui/ux",
        "user experience designer",
        "user interface designer",
        "interior designer",
        "visual designer",
        "video editor",
        "motion designer",
        "creative designer"
    ]):
        return "Design / Creative"

    # -----------------------------
    # HR / Recruitment
    # -----------------------------
    if contains_any(title, [
        "hr recruiter",
        "it recruiter",
        "recruiter",
        "recruitment",
        "talent acquisition",
        "human resource",
        "human resources",
        "hr executive",
        "hr manager",
        "staffing"
    ]):
        return "HR / Recruitment"

    # -----------------------------
    # Finance / Accounting
    # -----------------------------
    if contains_any(title, [
        "accountant",
        "accounting",
        "accounts executive",
        "accounts manager",
        "finance",
        "financial analyst",
        "chartered accountant",
        "company secretary",
        "tax",
        "audit",
        "payroll",
        "equity",
        "commercial finance"
    ]):
        return "Finance / Accounting"

    # -----------------------------
    # Sales / Business Development
    # -----------------------------
    if contains_any(title, [
        "sales",
        "business development",
        "business head",
        "business manager",
        "relationship manager",
        "relationship officer",
        "account manager",
        "territory sales",
        "area sales",
        "regional sales",
        "inside sales",
        "tele sales",
        "store promoter",
        "promoter"
    ]):
        return "Sales / Business Development"

    # -----------------------------
    # Marketing
    # -----------------------------
    if contains_any(title, [
        "marketing",
        "digital marketing",
        "product marketing",
        "brand marketing",
        "marketing manager",
        "marketing executive"
    ]):
        return "Marketing"

    # -----------------------------
    # Customer Service / BPO
    # -----------------------------
    if contains_any(title, [
        "customer service",
        "customer services",
        "customer support",
        "customer care",
        "customer success",
        "call center",
        "call centre",
        "telecaller",
        "tele caller",
        "bpo",
        "voice process",
        "chat support",
        "chat process",
        "non voice process",
        "email support",
        "contact centre",
        "contact center"
    ]):
        return "Customer Service / BPO"

    # -----------------------------
    # Healthcare
    # -----------------------------
    if contains_any(title, [
        "doctor",
        "physician",
        "cardiologist",
        "nurse",
        "staff nurse",
        "pharmacist",
        "medical",
        "healthcare",
        "clinical",
        "embryologist",
        "health claims"
    ]):
        return "Healthcare"

    # -----------------------------
    # Education
    # -----------------------------
    if contains_any(title, [
        "professor",
        "assistant professor",
        "associate professor",
        "teacher",
        "lecturer",
        "faculty",
        "academic",
        "education counsellor",
        "education counselor"
    ]):
        return "Education"

    # -----------------------------
    # Content / Media
    # -----------------------------
    if contains_any(title, [
        "content writer",
        "content editor",
        "journalist",
        "sports writer",
        "sports editor",
        "copywriter",
        "content creator"
    ]):
        return "Content / Media"

    # -----------------------------
    # Operations / Project Management
    # -----------------------------
    if contains_any(title, [
        "project manager",
        "project coordinator",
        "project engineer",
        "operations manager",
        "operations executive",
        "operations",
        "procurement",
        "purchase executive",
        "purchase manager",
        "supply chain",
        "logistics",
        "administration",
        "administrative",
        "commercial executive",
        "commercial manager"
    ]):
        return "Operations / Project Management"

    # -----------------------------
    # Engineering
    # -----------------------------
    if contains_any(title, [
        "mechanical engineer",
        "mechanical design",
        "civil engineer",
        "electrical engineer",
        "electronics engineer",
        "design engineer",
        "quality engineer",
        "site engineer",
        "production engineer",
        "safety engineer",
        "fire and safety",
        "structural engineer",
        "automation engineer",
        "automation assembly",
        "engineering manager",
        "maintenance engineer",
        "maintenance technician",
        "billing engineer",
        "mep engineer",
        "mep billing",
        "pole deployment engineer",
        "embedded software"
    ]):
        return "Engineering"

    # -----------------------------
    # Software / IT
    # -----------------------------
    if contains_any(title, [
        "software engineer",
        "software developer",
        "software development",
        "developer",
        "programmer",
        "full stack",
        "frontend developer",
        "front end developer",
        "backend developer",
        "back end developer",
        "web developer",
        "java developer",
        "python developer",
        ".net developer",
        "android developer",
        "flutter developer",
        "react developer",
        "devops",
        "site reliability engineer",
        "application developer",
        "application support",
        "technical support",
        "solution architect",
        "technology architect",
        "technical lead",
        "tech lead",
        "php developer",
        "embedded software"
    ]):
        return "Software / IT"

    return "Other / Unclassified"


df["job_family"] = df["title"].apply(classify_job)


print("\n========== JOB FAMILY COUNTS ==========")
print(df["job_family"].value_counts())


print("\n========== EXAMPLES ==========")
print(
    df[["title", "job_family"]]
    .drop_duplicates()
    .head(100)
    .to_string(index=False)
)


df.to_csv(output_file, index=False)

print("\nSaved to:")
print(output_file)

print("\nFinal columns:", len(df.columns))

print("\n================================")
print("JOB FAMILY CREATION COMPLETE")
print("================================")