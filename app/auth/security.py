from datetime import datetime, timedelta, timezone

import hashlib
from uuid import uuid4
import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidTokenError
from pwdlib import PasswordHash

from app.core.config import settings 

password_hasher = PasswordHash.recommended()


class TokenValidationError(Exception):
    """
    Raised when a JWT is expired, malformed, or has an unexpected type.
    """

def hash_password(plain_password: str) -> str:
    return password_hasher.hash(plain_password)

def verify_password(plain_password: str, hash_password: str) -> bool:
    return password_hasher.verify(plain_password, hash_password)

def hash_refresh_token(raw_token: str) -> str:
    return hashlib.sha256(raw_token.encode("utf-8")).hexdigest()

def create_access_token(user_id: int, role: str) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "role": role,
        "type": "access",
        "iat": now,
        "exp": now,
    }

