import os

from starlette.applications import Starlette
from starlette.routing import Route, WebSocketRoute
from starlette.templating import Jinja2Templates
from strawberry.asgi import GraphQL

from .admin.schema import schema as admin_schema
from .app.schema import schema as app_schema

DEBUG = bool(os.getenv("DEBUG"))

templates = Jinja2Templates(directory="src/templates")


async def voyager(request):
    return templates.TemplateResponse("voyager.html", {"request": request})


def get_graphql_app(schema, debug: bool):
    graphql_endpoint = GraphQL(
        schema=schema,
        graphiql=True,
        debug=debug,
        keep_alive=True,
    )
    routes = [
        Route("/graphql", endpoint=graphql_endpoint, name="graphql"),
        Route("/data-model", endpoint=voyager),
        WebSocketRoute("/graphql", endpoint=graphql_endpoint),
    ]
    app = Starlette(debug=DEBUG, routes=routes)
    return app


app = get_graphql_app(schema=app_schema, debug=DEBUG)
admin = get_graphql_app(schema=admin_schema, debug=DEBUG)
