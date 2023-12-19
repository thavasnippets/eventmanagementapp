from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.tracing import tracer
from Handlers import validateUser

tracer = Tracer()
logger = Logger()


@tracer.capture_lambda_handler
def lambda_handler(event, context):
    try:
        sf_id = event["Execution"]["Name"]
        payload = event["Execution"]["Input"]
        response = validateUser.validate_user(
            sf_id=sf_id,
            payload=payload
        )
        return response
    except Exception as err:
        logger.exception(err)
        return {"STATUS": "Exception", "error": str(err)}
