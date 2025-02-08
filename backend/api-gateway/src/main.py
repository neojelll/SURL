import fastapi
import strawberry
from strawberry.fastapi import GraphQLRouter
from api.services.shortener.resolvers import Mutation
from api.services.shortener.queries import Query
from api.routes.redirect_routes import redirect_router
import uvicorn

scheme = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(schema=scheme)

app = fastapi.FastAPI()

app.include_router(graphql_app, prefix="/graphql", tags=["GraphQL"])
app.include_router(redirect_router)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=15015,
    )
