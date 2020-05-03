import datetime
import json


def create_content_handler(event, context):
    query = event['queryStringParameters']['query']
    response_body = {"message": 'Hello {}!'.format(query), "time": datetime.datetime.now().isoformat()}

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
        },
        "body": json.dumps(response_body)
    }
