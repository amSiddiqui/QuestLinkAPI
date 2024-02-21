import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schemas.query_schema import Query


schema = strawberry.Schema(query=Query, mutation=None)
graphql_app = GraphQLRouter(schema=schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
