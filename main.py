import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL

@strawberry.type
class User:
    name: str
    age: int

@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Sample", age=20)

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()

app.add_route("/graphql", graphql_app)
