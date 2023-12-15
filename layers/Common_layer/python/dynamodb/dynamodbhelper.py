from logging import error
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools import Logger, Tracer
import boto3

tracer = Tracer()
logger = Logger()


class dynamodbhelper:

    def __init__(self, *, table_name, session=None, region=None):
        if session is not None:
            if region is not None:
                db = session.resource('dynamodb', region)
            else:
                db = session.resource('dynamodb')
        else:
            if region is not None:
                db = boto3.resource('dynamodb', region)
            else:
                db = boto3.resource('dynamodb')
        self.table_name = table_name
        self.table = db.Table(table_name)

    @tracer.capture_method
    def scan(self, **params):
        try:
            response = self.table.scan(**params)
            response_items = response["Items"]
            if not params.get("Limit"):
                while "LastEvaluatedKey" in response:
                    response = self.table.scan(
                        ExclusiveStartKey=response['LastEvaluatedKey'], **params)
                    response_items.extend(response['Items'])
            return response_items
        except Exception as err:
            logger.exception(err)
            raise Exception(f"Scan failed:{self.table_name}") from err

    @tracer.capture_method
    def query(self, **params):
        try:
            response = self.table.query(**params)
            response_items = response["Items"]
            if not params.get("Limit"):
                while "LastEvaluatedKey" in response:
                    response = self.table.scan(
                        ExclusiveStartKey=response['LastEvaluatedKey'], **params)
                    response_items.extend(response['Items'])
            return response_items
        except Exception as err:
            logger.exception(err)
            raise Exception(f"Query failed:{self.table_name}") from err

    @tracer.capture_method
    def get(self, **params):
        try:
            response_table = self.table.get_item(**params)
            return response_table['Item'] if 'Item' in response_table else None
        except Exception as err:
            logger.exception(err)
            raise Exception(
                f"Get data failed:{self.table_name} for key:{params}") from err

    @tracer.capture_method
    def put(self, **params):
        try:
            response_table = self.table.put_item(**params)
            return response_table
        except Exception as err:
            logger.exception(err)
            raise Exception(
                f"Put data failed:{self.table_name} for key:{params}") from err

    @tracer.capture_method
    def update(self, **params):
        try:
            response_table = self.table.update_item(**params)
            return response_table
        except Exception as err:
            logger.exception(err)
            raise Exception(
                f"update data failed:{self.table_name} for key:{params}") from err

    @tracer.capture_method
    def updateCustom(self, **params):
        try:
            inputData = response_table = self.table.get_item(Key=params["Key"])
            updateData = params["Item"]
            if inputData is not None and inputData.item_count == 1:
                for key, val in updateData.items():
                    if key in inputData:
                        inputData[key] = val
            response_table = self.table.put_item(inputData)
            return response_table
        except Exception as err:
            logger.exception(err)
            raise Exception(
                f"update data failed:{self.table_name} for key:{params}") from err

    @tracer.capture_method
    def delete(self, **params):
        try:
            self.table.delete_item(**params)
            return True
        except Exception as err:
            logger.exception(err)
            raise Exception(
                f"delete data failed:{self.table_name} for key:{params}") from err
