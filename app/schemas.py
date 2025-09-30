from pydantic import BaseModel

class UserCreate(BaseModel):
    firebase_id: str


class UserCreateResponse(BaseModel):
    firebase_id: str
    user_id: int

class RoomCreate(BaseModel):
    room_name: str
    author: str
