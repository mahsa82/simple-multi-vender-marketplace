from core.database import Base
from sqlalchemy import (Column, String, Text, Boolean, Enum,
                        Integer, DateTime, ForeignKey,)
import enum
from sqlalchemy.orm import relationship

class RoleType(str, enum.Enum):
    admin = "admin"
    vender = "vender"
    customer = "customer"


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=True)

    is_active = Column(Boolean, default=True)

    role = Column(Enum(RoleType), default="customer")


class TokenModel(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    token = Column(String, nullable=False, unique=True)

    user = relationship("UserModel", uselist=False)
