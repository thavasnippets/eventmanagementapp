from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.event_handler import content_types
from aws_lambda_powertools.event_handler.api_gateway import ApiGatewayResolver, ProxyEventType, Response, Router
from aws_lambda_powertools.logging import correlation_paths, logger
from aws_lambda_powertools.logging.formatter import JsonFormatter
from aws_lambda_powertools.tracing import tracer
from aws_lambda_powertools.utilities.validation import validate
from aws_lambda_powertools.utilities.validation.exceptions import SchemaValidationError
from Schemas import createSchema, updateSchema
import json
from Handlers import createEvent, deleteEvent, updateEvent, getEvent
tracer = Tracer()
logger = Logger()
router = Router()


@router.post('/eventonboarding')
def create_event():
    try:
        try:
            validate(event=router.current_event.json_body,
                     schema=createSchema.schema)
        except SchemaValidationError as err:
            response = {"error": "SchemaValidationError", "message": str(err)}
            return Response(status_code=400, content_type=content_types.APPLICATION_JSON, body=json.dumps(response))
        response, status_code = createEvent.create_event(
            router.current_event.json_body)

        return Response(
            status_code=status_code, content_type=content_types.APPLICATION_JSON, body=json.dumps(
                response)
        )
    except Exception as err:
        logger.exception(err)
        response = {"error": "Failed in Create event", "message": str(err)}
        return Response(
            status_code=400, content_type=content_types.APPLICATION_JSON, body=json.dumps(response)
        )


@router.delete('/eventonboarding/{id}')
def delete_event(id):
    try:
        response, status_code = deleteEvent.delete_event(
            id)
        return Response(
            status_code=status_code, content_type=content_types.APPLICATION_JSON, body=json.dumps(
                response)
        )
    except Exception as err:
        logger.exception(err)
        response = {"error": "Failed in delete event", "message": str(err)}
        return Response(
            status_code=400, content_type=content_types.APPLICATION_JSON, body=json.dumps(response)
        )


@router.get('/leventonboarding')
def get_event():
    try:
        id = router.current_event.get_query_string_value(
            name="id", default_value=None)
        name = router.current_event.get_query_string_value(
            name="name", default_value=None)
        if id is not None:
            response, status_code = getEvent.get_eventById(id)
        else:
            response, status_code = getEvent.get_eventByName(name)

        return Response(
            status_code=status_code, content_type=content_types.APPLICATION_JSON, body=json.dumps(
                response)
        )
    except Exception as err:
        logger.exception(err)
        response = {"error": "Failed in get event", "message": str(err)}
        return Response(
            status_code=400, content_type=content_types.APPLICATION_JSON, body=json.dumps(response)
        )


@router.put('/eventonboarding/{id}')
def update_event(id):
    try:
        try:
            validate(event=router.current_event.json_body,
                     schema=updateSchema.schema)
        except SchemaValidationError as err:
            response = {"error": "SchemaValidationError", "message": str(err)}
            return Response(status_code=400, content_type=content_types.APPLICATION_JSON, body=json.dumps(response))
        response, status_code = updateEvent.update_event(
            router.current_event.json_body, id)

        return Response(
            status_code=status_code, content_type=content_types.APPLICATION_JSON, body=json.dumps(
                response)
        )
    except Exception as err:
        logger.exception(err)
        response = {"error": "Failed in update event", "message": str(err)}
        return Response(
            status_code=400, content_type=content_types.APPLICATION_JSON, body=json.dumps(response)
        )
