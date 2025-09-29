from pydantic import BaseModel
from datetime import datetime


# 회원가입 요청
class UserCreate(BaseModel):
    email: str  # EmailStr 대신 일반 str 사용
    username: str
    password: str


# 로그인 요청
class UserLogin(BaseModel):
    email: str  # EmailStr 대신 일반 str 사용
    password: str


# 사용자 응답 (비밀번호 제외)
class UserResponse(BaseModel):
    id: int
    email: str
    username: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


# JWT 토큰 응답
class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse
