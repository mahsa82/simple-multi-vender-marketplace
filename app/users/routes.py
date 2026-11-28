from app.core.database import get_db
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session

from app.users.models import UserModel
from app.users.schemas import UserLoginSchema, UserRegisterSchema, UserResponseSchema
from app.auth.service import register_user

router = APIRouter(tags=["users"], prefix="/users")

@router.get("")
async def list_users(db: Session = Depends(get_db)):
    return {"message": "users list"}



@router.post(
    "/register",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def register(payload: UserRegisterSchema, db: Session = Depends(get_db)):
    return register_user(payload=payload, db=db)


@router.post(
    "/login",
    response_model=UserResponseSchema,
    status_code=status.HTTP_201_CREATED,
)
def register(payload: UserRegisterSchema, db: Session = Depends(get_db)):
    return register_user(payload=payload, db=db)
