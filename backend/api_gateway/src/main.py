import fastapi
import strawberry
from strawberry.fastapi import GraphQLRouter
from .app.services.shortener.resolvers import Mutation, Query
from .app.routes.redirect_routes import redirect_router
import uvicorn


scheme = strawberry.Schema(query=Query, mutation=Mutation)


graphql_app = GraphQLRouter(schema=scheme)


app = fastapi.FastAPI()
app.include_router(graphql_app, prefix="/graphql", tags=["GraphQL"])
app.include_router(redirect_router)


def run():
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=15015,
    )
