from jose import jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status
from app.config import JWT_SECRET_KEY

ALGORITHM = "HS256"
EXPIRY_HOURS = 24


def create_jwt(data: dict):
    payload = {
        **data,
        "iat": datetime.utcnow(),
        "exp": datetime.utcnow() + timedelta(hours=EXPIRY_HOURS)
    }
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)


def decode_jwt(token: str):
    try:
        return jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) 
   