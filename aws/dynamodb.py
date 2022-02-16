# Make sure you have aws cli installed
# 1. Have an IAM user with permissions to perform DynamoDB operations
#    Make sure you run: aws configure to input your credentials
# 2. Create an EC2 instance - not necessary
# 3. Create a DynamoDB table using the AWS CLI.
#
# Reference for boto3 commands https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html#DynamoDB.Client.batch_write_item

import boto3
import json


def create_table(client):
    response = client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'Id',
                'AttributeType': 'N'
            },
        ],
        TableName='ProductCatalog',
        KeySchema=[
            {
                'AttributeName': 'Id',
                'KeyType': 'HASH'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )
    print(json.dumps(response, indent=4))


def batch_write(client, payload):
    response = client.batch_write_item(
        RequestItems=payload,
        ReturnConsumedCapacity='TOTAL',
        ReturnItemCollectionMetrics='SIZE'
    )

    print("BatchWrite Response:")
    print(json.dumps(response, indent=4))


def query_dynamodb(client):
    response = client.get_item(
        TableName='ProductCatalog',
        Key={
            'Id': {
                'N': '403'
            }
        }
    )
    print("Query response:")
    print(json.dumps(response, indent=4))


def main():
    client = boto3.client('dynamodb')
    try:
        create_table(client)
    except client.exceptions.ResourceInUseException:
        print('Table already exists!')

    with open('items.json') as f:
        payload = json.load(f)
    batch_write(client, payload)

    query_dynamodb(client)


if __name__ == '__main__':
    main()