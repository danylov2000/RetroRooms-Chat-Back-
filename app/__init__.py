from fastapi import FastAPI
from app.endpoints import users


app = FastAPI()

app.include_router(
    users.router,
    prefix="/api/users",
    tags=["users"]
)

