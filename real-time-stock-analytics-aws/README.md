# AWS Real-Time Stock Analytics (Serverless)

## Architecture
- AWS Lambda (Data ingestion)
- Amazon S3 (Storage)
- DynamoDB (Latest price)
- Amazon Athena (SQL analytics)
- Amazon SNS (Alerts)
- Amazon EventBridge (Scheduler)

## How It Works
1. EventBridge triggers Lambda every 5 minutes.
2. Lambda fetches stock data from Finnhub API.
3. Data is stored in S3 and DynamoDB.
4. Athena queries data directly from S3.
5. SNS sends alerts when threshold is crossed.

## Setup
- Replace bucket name
- Replace SNS Topic ARN
- Add API_KEY as Lambda environment variable

