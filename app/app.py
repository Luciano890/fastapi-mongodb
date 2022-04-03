from fastapi import FastAPI
from routes.user import user

app = FastAPI(
    title="REST API with FastAPI and Mongodb",
    description="this is an example REST API using FastAPI and MongoDB Docker Image.",
    version="0.0.1",
    openapi_tags=[{
        "name":"users",
        "description":"users routes"
    }]
)

app.include_router(user)