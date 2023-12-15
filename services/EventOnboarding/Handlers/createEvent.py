from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key
from dynamodb.dynamodbhelper import dynamodbhelper
from common_utils import create_unique_id
from date_utils import get_current_datetime
import constants
tracer = Tracer()
logger = Logger()

event_table = dynamodbhelper(table_name='user_dtls')


def create_event(request_body):
    request_body[constants.COL_ID] = create_unique_id("event")
    request_body[constants.COL_STATUS] = constants.EventStatus.ACTIVE
    request_body[constants.COL_IS_DELETED] = False
    request_body[constants.COL_CREATED_ON] = get_current_datetime()
    request_body[constants.COL_UPDATED_ON] = get_current_datetime()
    event_table.put(Item=request_body)
    return {"data": {"event_id": request_body[constants.COL_ID]}}, 200
