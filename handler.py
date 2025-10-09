import json
import boto3
import uuid
from datetime import datetime
import os

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
# Use an environment variable for the table name
table_name = os.environ.get('TODOS_TABLE')
table = dynamodb.Table(table_name)

def create_todo(event, context):
    """
    Creates a new to-do item.
    """
    try:
        data = json.loads(event.get("body"))
        if 'todo' not in data:
            return {'statusCode': 400, 'body': json.dumps({'error': 'Missing "todo" in request body'})}
    except:
        return {'statusCode': 400, 'body': json.dumps({'error': 'Invalid request body'})}

    timestamp = str(datetime.utcnow())
    item = {
        'id': str(uuid.uuid1()),
        'todo': data['todo'],
        'createdAt': timestamp,
        'updatedAt': timestamp,
        'completed': False
    }

    table.put_item(Item=item)

    return {"statusCode": 201, "body": json.dumps(item)}

def list_todos(event, context):
    """
    Retrieves all to-do items.
    """
    response = table.scan()
    items = response.get('Items', [])
    return {"statusCode": 200, "body": json.dumps(items)}

def get_todo(event, context):
    """
    Retrieves a single to-do item by its ID.
    """
    todo_id = event['pathParameters']['id']
    response = table.get_item(Key={'id': todo_id})
    item = response.get('Item')

    if not item:
        return {'statusCode': 404, 'body': json.dumps({'error': 'Item not found'})}
    
    return {"statusCode": 200, "body": json.dumps(item)}

def update_todo(event, context):
    """
    Updates an existing to-do item.
    """
    todo_id = event['pathParameters']['id']
    
    try:
        data = json.loads(event.get("body"))
        if 'todo' not in data or 'completed' not in data:
            return {'statusCode': 400, 'body': json.dumps({'error': 'Missing "todo" or "completed" in request body'})}
    except:
        return {'statusCode': 400, 'body': json.dumps({'error': 'Invalid request body'})}

    timestamp = str(datetime.utcnow())
    
    response = table.update_item(
        Key={'id': todo_id},
        UpdateExpression="SET todo = :todo, completed = :completed, updatedAt = :updatedAt",
        ExpressionAttributeValues={
            ':todo': data['todo'],
            ':completed': data['completed'],
            ':updatedAt': timestamp,
        },
        ReturnValues="ALL_NEW"
    )
    
    return {"statusCode": 200, "body": json.dumps(response['Attributes'])}

def delete_todo(event, context):
    """
    Deletes a to-do item.
    """
    todo_id = event['pathParameters']['id']
    table.delete_item(Key={'id': todo_id})
    
    return {"statusCode": 204, "body": ""} # 204 means No Content

