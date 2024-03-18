import json


def lambda_handler(event, context):
    number = event["number"]
    squared = number * number
    return {
        "statusCode": 200,
        "body": json.dumps(f"The square of {number} is {squared}."),
    }
