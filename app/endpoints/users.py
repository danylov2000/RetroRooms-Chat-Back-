from fastapi import APIRouter
from app.schemas import UserCreate, UserCreateResponse
from app.models import User
from app.database import session
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse



router = APIRouter()

@router.post("/", response_model=UserCreateResponse)
def create_user(user: UserCreate):
    user_object = User(firebase_id=user.firebase_id)
    try:
        session.add(user_object)
        session.commit()
        return {"firebase_id": user_object.firebase_id, "user_id": user_object.id}
    except IntegrityError:
        return JSONResponse(status_code=409, content={"message": "User already exists"})

@router.get("/{firebase_id}", response_model=UserCreateResponse)
def get_user_id(firebase_id: str):
    user_object = session.query(User).filter(User.firebase_id == firebase_id).first()
    if not user_object:
        return JSONResponse(status_code=404, content={"message": "User doesn't exist"})
    return {"firebase_id": user_object.firebase_id, "user_id": user_object.id}


