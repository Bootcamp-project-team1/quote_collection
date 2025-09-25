# app/routers/auth_mock.py
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
from app.schemas.user_simple import UserCreate, UserLogin, Token, UserResponse
from app.core.auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

# 메모리에 사용자 데이터 저장 (임시)
fake_users_db = {}
user_counter = 1


# 회원가입
@router.post("/register", response_model=Token)
def register(user_create: UserCreate):
    global user_counter

    # 이메일 중복 확인
    for user in fake_users_db.values():
        if user["email"] == user_create.email:
            raise HTTPException(status_code=400, detail="Email already registered")
        if user["username"] == user_create.username:
            raise HTTPException(status_code=400, detail="Username already taken")

    # 새 사용자 생성
    hashed_pw = hash_password(user_create.password)
    new_user = {
        "id": user_counter,
        "email": user_create.email,
        "username": user_create.username,
        "hashed_password": hashed_pw,
        "is_active": True,
        "created_at": datetime.utcnow(),
    }

    fake_users_db[user_counter] = new_user
    user_counter += 1

    # 토큰 생성
    access_token = create_access_token(new_user["id"])
    return Token(
        access_token=access_token,
        user=UserResponse(
            id=new_user["id"],
            email=new_user["email"],
            username=new_user["username"],
            is_active=new_user["is_active"],
            created_at=new_user["created_at"],
        ),
    )


# 로그인
@router.post("/login", response_model=Token)
def login(user_login: UserLogin):
    # 사용자 찾기
    user = None
    for u in fake_users_db.values():
        if u["email"] == user_login.email:
            user = u
            break

    if not user or not verify_password(user_login.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    if not user["is_active"]:
        raise HTTPException(status_code=400, detail="Account is inactive")

    # 토큰 생성
    access_token = create_access_token(user["id"])
    return Token(
        access_token=access_token,
        user=UserResponse(
            id=user["id"],
            email=user["email"],
            username=user["username"],
            is_active=user["is_active"],
            created_at=user["created_at"],
        ),
    )


# 현재 사용자 정보
@router.get("/me", response_model=UserResponse)
def get_current_user(token: str = Depends(oauth2_scheme)):
    user_id = verify_token(token)
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        id=user["id"],
        email=user["email"],
        username=user["username"],
        is_active=user["is_active"],
        created_at=user["created_at"],
    )


# 로그아웃
@router.post("/logout")
def logout():
    return {"message": "Successfully logged out"}


# 현재 등록된 사용자 목록 보기 (테스트용)
@router.get("/users", response_model=list[UserResponse])
def get_all_users():
    """테스트용: 현재 등록된 모든 사용자 조회"""
    users = []
    for user in fake_users_db.values():
        users.append(
            UserResponse(
                id=user["id"],
                email=user["email"],
                username=user["username"],
                is_active=user["is_active"],
                created_at=user["created_at"],
            )
        )
    return users


# 토큰 검증 (테스트용)
@router.get("/verify-token")
def verify_token_endpoint(token: str = Depends(oauth2_scheme)):
    """토큰 유효성 검증"""
    user_id = verify_token(token)
    user = fake_users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {
        "valid": True,
        "user_id": user["id"],
        "username": user["username"],
        "message": "Token is valid",
    }
