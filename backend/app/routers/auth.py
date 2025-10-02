from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, Token, UserResponse
from app.core.auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_token,
)

router = APIRouter(prefix="/auth", tags=["Authentication"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


# 회원가입
@router.post("/register", response_model=Token)
def register(user_create: UserCreate, db: Session = Depends(get_db)):
    # 이메일 중복 확인
    if db.query(User).filter(User.email == user_create.email).first():
        raise HTTPException(status_code=400, detail="이미 가입된 이메일입니다.")

    # 사용자명 중복 확인
    if db.query(User).filter(User.username == user_create.username).first():
        raise HTTPException(status_code=400, detail="이미 존재하는 아이디입니다.")

    # 새 사용자 생성
    hashed_pw = hash_password(user_create.password)
    db_user = User(
        email=user_create.email,
        username=user_create.username,
        hashed_password=hashed_pw,
    )

    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="계정등록이 실패했습니다.")

    # 토큰 생성
    access_token = create_access_token(db_user.id)
    return Token(access_token=access_token, user=UserResponse.model_validate(db_user))


# 로그인
@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # 사용자 찾기
    user = db.query(User).filter(User.email == form_data.username).first()
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="메일 또는 비번이 틀립니다.")

    if not user.is_active:
        raise HTTPException(status_code=400, detail="비활성화 계정입니다.")

    # 토큰 생성
    access_token = create_access_token(user.id)
    return Token(access_token=access_token, user=UserResponse.model_validate(user))


# 현재 사용자 정보
@router.get("/me", response_model=UserResponse)
def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    user_id = verify_token(token)
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="없는 사용자입니다.")
    return UserResponse.model_validate(user)


# 로그아웃 (실제로는 클라이언트에서 토큰 삭제)
@router.post("/logout")
def logout():
    return {"message": "로그아웃 완료"}
