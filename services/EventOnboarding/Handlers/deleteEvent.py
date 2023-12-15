from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key
from dynamodb.dynamodbhelper import dynamodbhelper
from date_utils import get_current_datetime
import layers.Common_layer.python.constants as constants
tracer = Tracer()
logger = Logger()

event_table = dynamodbhelper(table_name='user_dtls')


def delete_event(id):
    payload = event_table.get(Key={constants.COL_ID: id})
    if payload:
        payload[constants.COL_UPDATED_ON] = get_current_datetime()
        payload[constants.COL_IS_DELETED] = True
        event_table.put(Item=payload)
        return {"data": "Success"}, 200

    else:
        return {"data": f"id({id}) number is not registered"}, 400
