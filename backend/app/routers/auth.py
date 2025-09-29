from app.database import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..database import get_db
from ..models.user import User
from ..schemas.user import UserCreate, UserLogin, Token, UserResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == payload.email).first():
        raise HTTPException(400, "이미 가입된 이메일입니다.")
    if db.query(User).filter(User.username == payload.username).first():
        raise HTTPException(400, "이미 존재하는 아이디입니다.")
    
    db_user = User(
        email=payload.email,
        username=payload.username,
        password=payload.password,
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(400, "계정등록이 실패했습니다.")

    return UserResponse.model_validate(db_user)
