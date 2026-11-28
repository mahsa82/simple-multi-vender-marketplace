from app.core.database import get_db
from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session

from app.users.models import UserModel
from app.users.schemas import UserLoginSchema, UserRegisterSchema

router = APIRouter(tags=["users"], prefix="/users")

@router.get("")
async def list_users(db: Session = Depends(get_db)):
    return {"message": "users list"}


@router.post("/login")
async def user_login(request:UserLoginSchema, db:Session=Depends(get_db)):
    return {}



@router.post("/register")
async def user_register(request:UserRegisterSchema, db:Session=Depends(get_db)):
    if db.query(UserModel).filter_by(user=request.email).first():
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="username already exists.")
    user_obj = UserModel(user=request.email)
    return {}
