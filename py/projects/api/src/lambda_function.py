# from aws_lambda_powertools.logging import correlation_paths
from mangum import Mangum
from mangum.types import LambdaContext

from shared.monitoring import tracer
from src.server import admin, app


# @logger.inject_lambda_context(correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL)
@tracer.capture_lambda_handler
def app_handler(event: dict, context: LambdaContext):
    # Handle keep warm event
    if not event or event.get("keep-warm"):
        print("Keep warm event received")
        return {}
    # Create a Mangum instance and pass the Starlette app
    asgi_handler = Mangum(app=app)
    response = asgi_handler(event, context)
    return response


# @logger.inject_lambda_context(correlation_id_path=correlation_paths.LAMBDA_FUNCTION_URL)
@tracer.capture_lambda_handler
def admin_handler(event: dict, context: LambdaContext):
    # Handle keep warm event
    if not event or event.get("keep-warm"):
        print("Keep warm event received")
        return {}
    # Create a Mangum instance and pass the Starlette app
    asgi_handler = Mangum(app=admin)
    response = asgi_handler(event, context)
    return response
