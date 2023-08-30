import boto3

boto3.setup_default_session(profile_name="default")

dynamodb_client = boto3.client("dynamodb")

table_name = "orders"

response = dynamodb_client.put_item(
    TableName=table_name,
    Item={
        "order_id": {"S": "ord1234"},
        "order_date": {"S": "2022-08-03"},
        "user_email": {"S": "test@example.com"},
        "amount": {"N": "120"},
    },
)

print(response)

# Output
"""
{'ResponseMetadata': 
  {'RequestId': '81QL1EK656G8G4U063IG2G0Q0RVV4KQNSO5AEMVJF66Q9ASUAAJG', 
  'HTTPStatusCode': 200, 
  'HTTPHeaders': {
    'server': 'Server', 
    'date': 'Wed, 03 Aug 2022 13:45:44 GMT', 
    'content-type': 'application/x-amz-json-1.0', 
    'content-length': '2', 
    'connection': 'keep-alive', 
    'x-amzn-requestid': '81QL1EK656G8G4U063IG2G0Q0RVV4KQNSO5AEMVJF66Q9ASUAAJG', 
    'x-amz-crc32': '2745614147'
    }, 
  'RetryAttempts': 0
  }
}
"""