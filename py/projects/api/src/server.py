from starlette.applications import Starlette
from starlette.requests import Request
from starlette.routing import Route, WebSocketRoute
from starlette.templating import Jinja2Templates
from strawberry.asgi import GraphQL

from shared.settings import admin_settings, app_settings

from .admin.schema import schema as admin_schema
from .app.schema import schema as app_schema

PROJECT = "Safebear"

templates = Jinja2Templates(directory="src/templates")

print(app_settings)

app_strawberry_endpoint = GraphQL(
    schema=app_schema, debug=app_settings.debug, keep_alive=True, graphiql=False
)
admin_strawberry_endpoint = GraphQL(
    schema=admin_schema, debug=admin_settings.debug, keep_alive=True, graphiql=False
)

app = Starlette(
    routes=[
        Route(path="/graphql", methods=["POST"], endpoint=app_strawberry_endpoint),
        WebSocketRoute(path="/graphql", endpoint=app_strawberry_endpoint),
    ]
)
admin = Starlette(
    routes=[
        Route(path="/graphql", methods=["POST"], endpoint=admin_strawberry_endpoint),
        WebSocketRoute(path="/graphql", endpoint=admin_strawberry_endpoint),
    ]
)


async def graphiql(request: Request, service: str | None = None):
    context = {}
    # Context should always include a "request" key in Starlette
    context["request"] = request
    host = request.base_url.hostname or ""
    title = "GraphiQL"
    if service:
        title = f"{service} {title}"
    if env := "local" if "localhost" in host else None:
        title += f" ({env})"
    context["title"] = f"{title} | {PROJECT}"
    return templates.TemplateResponse(name="graphiql.html", context=context)


@app.route("/graphql", methods=["GET"])
async def app_graphiql(request: Request):
    return await graphiql(request=request, service="App")


@admin.route("/graphql", methods=["GET"])
async def admin_graphiql(request: Request):
    return await graphiql(request=request, service="Admin")


@app.route("/data-model", methods=["GET"])
@admin.route("/data-model", methods=["GET"])
async def voyager(request: Request):
    raise Exception("Not implemented")
    return templates.TemplateResponse(name="voyager.html", context={"request": request})
