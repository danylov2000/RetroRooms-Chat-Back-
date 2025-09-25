from fastapi import FastAPI
from app.endpoints import users
from fastapi.middleware.cors import CORSMiddleware

cors_allowed_origins = [
    "http://localhost",
    "http://localhost:8000",
    "https://retrorooms-chat-back.onrender.com/"
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    users.router,
    prefix="/api/users",
    tags=["users"]
)

