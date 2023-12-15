from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, ProxyEventType, Response
from aws_lambda_powertools.logging import correlation_paths, logger
from aws_lambda_powertools.tracing import tracer
from aws_lambda_powertools.utilities.validation import validate
from aws_lambda_powertools.utilities.validation.exceptions import SchemaValidationError
import eventOnboarding
tracer = Tracer()
logger = Logger()
app = ApiGatewayResolver(proxy_type=ProxyEventType.APIGatewayProxyEvent)
app.include_router(eventOnboarding.router)


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event, context):
    return app.resolve(event, context)
