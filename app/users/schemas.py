from pydantic import BaseModel, field_validator


class SignupRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str


class UserResponse(BaseModel):
    id: int
    username: str

