import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    print("this is for lambda fn demo with  s3 events")
    dynamodb_client = boto3.client("dynamodb")
    table_name = "orders"
    response = dynamodb_client.put_item(
      TableName=table_name,
      Item={
        "order_id": {"S": "ord12345"},
        "order_date": {"S": "2023-09-03"},
        "user_email": {"S": "test@vytec.com"},
        "amount": {"N": "120"},
      },
    )

    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }