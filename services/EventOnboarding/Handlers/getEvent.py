import constants
from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key
from dynamodb.dynamodbhelper import dynamodbhelper

tracer = Tracer()
logger = Logger()

event_table = dynamodbhelper(table_name='user_dtls')


def get_eventById(id):
    logger.info(id)
    if id is not None:
        result = event_table.get(Key={constants.COL_ID: id})
    else:
        filter_expression = Attr(constants.COL_IS_DELETED).ne(True)
        result = event_table.scan(FilterExpression=filter_expression)

    return {"data": result}, 200


def get_eventByName(name):
    filter_expression = Attr(constants.COL_IS_DELETED).ne(True)
    if name is not None:
        result = event_table.query(KeyConditionExpression=Key(
            'name').eq(name) & filter_expression)
    else:
        result = event_table.scan(FilterExpression=filter_expression)

    return {"data": result}, 200
