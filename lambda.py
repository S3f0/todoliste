import json
import boto3

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    table_name = 'my-to-do-app'
    table = dynamodb.Table(table_name)

    todo_id = event['TodoID']
    user_id = event['UserID']

    try:
        response = table.get_item(Key={'TodoID': todo_id, 'UserID': user_id})
        item = response.get('Item', None)

        if item:
            return {
                'statusCode': 200,
                'body': json.dumps({'Mein Task': item}),
                'headers': {'Content-Type': 'application/json'}
            }
        else:
            return {
                'statusCode': 404,
                'body': json.dumps({'message': 'Task nicht gefunden'}),
                'headers': {'Content-Type': 'application/json'}
            }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'message': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }

