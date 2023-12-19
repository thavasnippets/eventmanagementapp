from aws_lambda_powertools import Logger, Tracer
from boto3.dynamodb.conditions import Attr, Key


tracer = Tracer()
logger = Logger()


def validate_user(qr_data):

    return {"data": {"qr_data": qr_data, "image": encoded_image}}, 200
