# Decoding the Indian Job Market

An end-to-end data analytics project that analyzes job postings in India to understand **hiring demand, salary patterns, skill requirements, experience levels, locations, and employer hiring behavior**.

The project combines **Python, SQL, and Power BI** to transform a raw job-market dataset into an interactive business intelligence dashboard.

---

## Project Objective

The Indian job market contains thousands of job postings across different locations, companies, experience levels, salaries, and skill requirements.

The goal of this project is to answer questions such as:

* Which job roles and skills are most in demand?
* How does salary vary by experience and job category?
* Which locations offer higher salary levels?
* Which skills are associated with higher compensation?
* Which companies have the highest hiring volumes?
* How concentrated is hiring among major employers?
* How does hiring demand differ between direct employers and staffing/recruitment firms?

---

## Dataset

**Source:** Kaggle — Indian Job Market Dataset 2025

The dataset contains approximately **97,679 job postings**.

The original dataset was cleaned and transformed before analysis. The project does not redistribute the original dataset in this repository.

---

## Project Workflow

```text
Kaggle Dataset
      ↓
Python Data Inspection
      ↓
Data Cleaning
      ↓
Salary & Location Engineering
      ↓
Job Family Classification
      ↓
Skill Extraction
      ↓
SQL Analysis
      ↓
Power BI Dashboard
      ↓
Business Insights
```

---

## Tools & Technologies

| Tool        | Purpose                                            |
| ----------- | -------------------------------------------------- |
| Python      | Data cleaning, transformation and skill extraction |
| Pandas      | Data manipulation and analysis                     |
| SQL         | Analytical queries and business analysis           |
| Power BI    | Interactive dashboard and visualization            |
| Power Query | Data transformation and preparation                |
| DAX         | Measures and calculated metrics                    |
| Excel       | Original dataset format                            |

---

## Key Analysis Areas

### 1. Job Market Overview

Analysis of:

* Total job postings
* Hiring locations
* Job categories
* Experience requirements
* Overall hiring distribution

### 2. Salary & Compensation

Analysis of:

* Median salary
* Salary distribution
* Salary by experience level
* Salary by job category
* Salary by location
* Salary disclosure rate

### 3. Skills & Market Demand

Analysis of:

* Most frequently requested skills
* Skill demand across job postings
* Number of skills required per posting
* Relationship between skill demand and salary
* Salary differences associated with specific skills

### 4. Companies & Hiring

Analysis of:

* Hiring volume by company
* Major hiring companies
* Hiring concentration
* Salary levels among companies with sufficient salary data
* Direct employers vs staffing/recruitment firms

---

## Dashboard

The final analysis is presented through an interactive Power BI dashboard containing dedicated sections for:

* Job Market Overview
* Salary & Compensation
* Skills & Market Demand
* Companies & Hiring

The Power BI dashboard is available in:

`dashboard/Decoding_India_Job_Market.pbix`

---

## Project Structure

```text
JobMarketIntelligence/
│
├── dashboard/
│   └── Decoding_India_Job_Market.pbix
│
├── src/
│   ├── inspect_data.py
│   ├── inspect_main_dataset.py
│   ├── profile_main_dataset.py
│   ├── inspect_duplicates.py
│   ├── check_descriptions.py
│   ├── explore_descriptions.py
│   ├── clean_main_dataset.py
│   ├── check_cleaned_data.py
│   ├── create_salary_fields.py
│   ├── create_location_fields.py
│   ├── add_job_family.py
│   └── extract_skills.py
│
├── app/
├── notebooks/
├── sql/
│
├── .gitignore
└── README.md
```

---

## Key Findings

Some of the analysis highlights include:

* Salary levels vary substantially across job categories and experience bands.
* Certain specialized skill groups show substantially different salary distributions from the overall market.
* Hiring demand is concentrated among a relatively small group of high-volume companies.
* Staffing and recruitment firms represent an important share of job-posting volume, which needs to be considered when interpreting company-level hiring rankings.
* Salary analysis is subject to a major limitation because salary information is not disclosed in every job posting.

> Exact findings and values are presented in the Power BI dashboard and are based on the cleaned dataset used for analysis.

---

## Limitations

* The analysis is based on a Kaggle dataset rather than a continuously updated live job feed.
* Salary information is missing from a substantial proportion of postings.
* Company-type classification is a **heuristic classification** based on company names and known exceptions, rather than an official employer classification.
* Job-skill extraction depends on the information available in job descriptions.
* The dataset represents a specific collection of job postings and should not be interpreted as a complete census of the Indian job market.

---

## Future Improvements

Possible extensions include:

* Automated periodic data updates
* Additional job-market data sources
* More robust company classification
* Job-demand forecasting
* An AI-based natural-language interface for querying the dashboard data
* Automated skill and salary trend monitoring

---

## Author

**Srijeeta Bose**
This project was developed as a portfolio project to demonstrate practical skills in **data cleaning, SQL analysis, Python, business intelligence, and Power BI dashboard development**.
