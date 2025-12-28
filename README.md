📊 MeetingBank ETL Pipeline with Apache Airflow & Docker

An end-to-end automated ETL (Extract, Transform, Load) pipeline built using Apache Airflow, Docker, PostgreSQL, and MongoDB to process the MeetingBank dataset and generate analytical HTML reports.

This project demonstrates data engineering best practices, workflow orchestration, containerization, and automated reporting.

🚀 Project Overview

The MeetingBank ETL Pipeline automates the complete lifecycle of meeting data processing:

Extract raw meeting transcripts

Clean & validate data

Transform data into structured & unstructured formats

Load data into relational (PostgreSQL) and NoSQL (MongoDB) databases

Run analytics

Generate detailed HTML reports automatically

All steps are orchestrated using Apache Airflow DAGs and executed inside Docker containers.

🧱 Architecture
                ┌────────────┐
                │ MeetingBank│
                │   Dataset  │
                └─────┬──────┘
                      │
                ┌─────▼──────┐
                │  Extract   │
                └─────┬──────┘
                      │
                ┌─────▼──────┐
                │   Clean    │
                └─────┬──────┘
                      │
                ┌─────▼──────┐
                │ Transform  │
                └─────┬──────┘
          ┌───────────┴───────────┐
          │                       │
┌─────────▼─────────┐   ┌─────────▼─────────┐
│   PostgreSQL DB    │   │   MongoDB DB       │
│ (Structured Data) │   │ (Unstructured Data)│
└─────────┬─────────┘   └─────────┬─────────┘
          │                       │
          └───────────┬───────────┘
                      ▼
               ┌────────────┐
               │ Analytics  │
               └─────┬──────┘
                     ▼
            ┌──────────────────┐
            │ HTML Report Auto │
            │   Generation     │
            └──────────────────┘

🛠️ Tech Stack
Component	Technology
Workflow Orchestration	Apache Airflow
Containerization	Docker & Docker Compose
Programming Language	Python 3
Relational Database	PostgreSQL
NoSQL Database	MongoDB
Analytics	Pandas, Python
Reporting	HTML (auto-generated)
📁 Project Structure
meetingbank_pipeline/
│
├── dags/
│   └── meetingbank_etl_pipeline.py   # Airflow DAG
│
├── scripts/
│   ├── extract.py
│   ├── clean.py
│   ├── transform.py
│   ├── load.py
│   ├── analytics.py
│   └── config.py
│
├── sql/
│   ├── create_tables.sql
│   ├── create_indexes.sql
│   └── sample_queries.sql
│
├── Reports/
│   ├── meetingbank_report_YYYY-MM-DD.html
│   └── meetingbank_detailed_report_YYYY-MM-DD.html
│
├── tests/
│   └── unit tests for ETL stages
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .gitignore
└── README.md

⚙️ How to Run the Project
1️⃣ Prerequisites

Docker Desktop installed

Git installed

Minimum 8 GB RAM recommended

2️⃣ Clone the Repository
git clone https://github.com/Dineshkumar250699/meetingbank-etl-pipeline.git
cd meetingbank-etl-pipeline

3️⃣ Start Services with Docker
docker compose up -d


This will start:

Airflow Webserver

Airflow Scheduler

PostgreSQL

MongoDB

4️⃣ Access Airflow UI

Open browser:

http://localhost:8080


Default credentials:

Username: airflow

Password: airflow

5️⃣ Run the DAG

Enable meetingbank_etl_pipeline

Trigger the DAG manually or wait for scheduled run

Monitor tasks in Graph View

🔄 Airflow DAG Tasks
Task	Description
fetch_data	Extracts MeetingBank data
clean_data	Cleans and validates data
transform_data	Structures data
load_to_postgres	Loads structured data
load_to_mongodb	Loads unstructured data
run_analytics	Computes analytics
generate_html_report	Creates HTML report
end_task	Pipeline completion
📊 HTML Report Output

After a successful DAG run, reports are generated automatically in:

Reports/


Example:

meetingbank_report_2025-12-27.html

meetingbank_detailed_report_2025-12-27.html

These reports include:

Pipeline execution summary

Analytics results

Data statistics

Execution timestamps

🧪 Testing

Unit tests are available under:

tests/


Run locally (optional):

pytest tests/

🧠 Key Learning Outcomes

Apache Airflow DAG design

Task dependencies & retries

Dockerized data pipelines

Multi-database loading (SQL + NoSQL)

Automated analytics & reporting

Git & GitHub workflow

📌 Future Improvements

Add CI/CD with GitHub Actions

Add data quality checks

Store reports in cloud storage (S3/GCS)

Add interactive dashboards (Streamlit / Power BI)

👤 Author

Dineshkumar Swaminathan
Master’s in Applied Data Science & AI
GitHub: Dineshkumar250699