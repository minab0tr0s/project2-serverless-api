import json

def create_todo(event, context):
    """
    This function creates a new to-do item.
    For now, it just returns a success message.
    """
    body = {
        "message": "Go Serverless v3.0! Your create_todo function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response
