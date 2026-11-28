from sqlalchemy.orm import Session
from app.users.schemas import UserRegisterSchema
from app.users.models import RoleType, UserModel
from sqlalchemy import select
from fastapi import HTTPException, status
from app.auth.security import hash_password


def register_user(payload: UserRegisterSchema, db: Session) -> UserModel:
    normalized_email = payload.email.strip().lower()

    existing_user = db.scalar(
        select(UserModel).where(UserModel.email == normalized_email)
    )
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email is already registered.",
        )

    user = UserModel(
        email=normalized_email,
        hashed_password=hash_password(payload.password),
        role=RoleType.customer,
        is_active=True,
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
