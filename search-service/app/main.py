import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from app.schema.schema import Query, Mutation

# Create the GraphQL schema
schema = strawberry.Schema(query=Query, mutation=Mutation)

# Create a GraphQL router
graphql_app = GraphQLRouter(schema)

# Create the FastAPI application
app = FastAPI(title="Search Service")

# Add the GraphQL route
app.include_router(graphql_app, prefix="/graphql")

# Add a health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)