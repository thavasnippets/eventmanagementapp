from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key
from dynamodb.dynamodbhelper import dynamodbhelper
from date_utils import get_current_datetime
import constants
tracer = Tracer()
logger = Logger()

event_table = dynamodbhelper(table_name='user_dtls')


def update_event(request_body, id):
    if not event_table.get(Key={constants.COL_ID: id}):
        request_body[constants.COL_UPDATED_ON] = get_current_datetime()
        event_table.update(Item=request_body)
        return {"data": "Success"}, 200

    else:
        return {"data": f"id({id}) number is not registered"}, 400
