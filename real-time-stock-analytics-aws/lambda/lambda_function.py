import json
import boto3
import requests
import os
from datetime import datetime

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
sns = boto3.client('sns')

BUCKET_NAME = "your-bucket-name"
TABLE_NAME = "stock_prices"
SNS_TOPIC_ARN = "your-sns-topic-arn"
API_KEY = os.environ.get("API_KEY")

def lambda_handler(event, context):

    symbol = "AAPL"
    api_url = f"https://finnhub.io/api/v1/quote?symbol={symbol}&token={API_KEY}"

    response = requests.get(api_url)
    data = response.json()

    price = data.get("c", 0)
    timestamp = datetime.utcnow().isoformat()

    # Store raw data in S3
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=f"raw-data/{symbol}_{timestamp}.json",
        Body=json.dumps(data)
    )

    # Store latest price in DynamoDB
    table = dynamodb.Table(TABLE_NAME)
    table.put_item(
        Item={
            "symbol": symbol,
            "price": str(price),
            "timestamp": timestamp
        }
    )

    # Send alert if price > 200
    if price > 200:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="Stock Price Alert",
            Message=f"{symbol} crossed $200. Current price: {price}"
        )

    return {
        'statusCode': 200,
        'body': json.dumps("Stock data processed successfully")
    }
