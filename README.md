📈 AWS Real-Time Stock Analytics (Serverless Architecture)
🚀 Project Overview

This project implements a fully serverless real-time stock analytics pipeline using AWS cloud services. The system ingests live stock market data, stores it in scalable storage layers, performs SQL-based analytics, and triggers real-time alerts based on threshold conditions.

The architecture is event-driven, cost-efficient, and production-ready.

🏗️ Architecture

Services Used:

AWS Lambda – Data ingestion & processing

Amazon S3 – Raw data storage

Amazon DynamoDB – Latest price storage

Amazon Athena – SQL analytics on S3

Amazon SNS – Email alerts

Amazon EventBridge – Scheduled trigger

Amazon CloudWatch – Logging & monitoring

🔄 Workflow

EventBridge triggers Lambda every 5 minutes

Lambda fetches real-time stock data from Finnhub API

Raw JSON data is stored in S3

Latest stock price is updated in DynamoDB

Athena queries data directly from S3

SNS sends alert if stock crosses threshold

📂 Project Structure
real-time-stock-analytics-aws/
│
├── lambda/
│   └── lambda_function.py
│
├── athena/
│   └── create_table.sql
│
├── README.md
└── .gitignore
📊 Sample Athena Queries
SELECT AVG(c) AS avg_price FROM stock_data;

SELECT MAX(h) AS highest_price FROM stock_data;

SELECT MIN(l) AS lowest_price FROM stock_data;
⚙️ Setup Instructions

Create S3 bucket

Create DynamoDB table

Create SNS topic & confirm email

Deploy Lambda function

Add EventBridge schedule (rate 5 minutes)

Configure Athena external table

🔐 Security Best Practices

API key stored as Lambda Environment Variable

No credentials hardcoded

IAM role-based access control

Serverless architecture (no EC2 dependency)

💰 Cost Optimization

Fully serverless (pay-per-use model)

Free tier compatible

Minimal data scanned in Athena

Estimated cost: < $2/month for demo usage

🎯 Key Skills Demonstrated

Serverless Architecture Design

Event-Driven Systems

Cloud Data Engineering

AWS IAM & Security

Real-Time Data Processing

SQL-based Analytics on Data Lake
