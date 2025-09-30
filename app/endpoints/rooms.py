from fastapi import APIRouter

from app.schemas import UserCreateResponse

router = APIRouter()


# @router.post("api/rooms", response_model=RoomCreateResponse)
# def create_room(room):
#
