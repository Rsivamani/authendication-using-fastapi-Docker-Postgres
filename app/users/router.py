from fastapi import APIRouter, Depends, Form, HTTPException,status, Form
from typing import Annotated
from app.database import get_db
from app.auth.dependencies import validate_user
from app.auth.jwt_handler import create_jwt
from . import services
from .schemas import SignupRequest, LoginRequest, TokenResponse, UserResponse

router = APIRouter(prefix="/users", tags=["users"])



@router.post("/signup")
async def signup(
    data: Annotated[SignupRequest, Form()],
    db=Depends(get_db)
):
    existing = await services.get_user_by_username(db, data.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    await services.create_user(db, data.username, data.password)
    return {"message": "User created successfully"}


@router.post("/login", response_model=TokenResponse)
async def login(
    data: Annotated[LoginRequest, Form()],
    db=Depends(get_db)
):
    user = await services.get_user_by_username(db, data.username)
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    if not services.verify_password(data.password, user["password"]):
        raise HTTPException(status_code=400, detail="Wrong password")
    
    token = create_jwt({"id": user["id"], "username": user["username"]})
    return TokenResponse(access_token=token)


@router.get("/me", response_model=UserResponse)
async def get_me(
    db=Depends(get_db),
    user=Depends(validate_user)):
    row = await services.get_user_by_username(db, user["username"])
    return UserResponse(id=row["id"], username=row["username"])




