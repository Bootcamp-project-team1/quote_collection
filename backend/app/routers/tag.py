from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.tag import Tag

router = APIRouter(prefix="/tag", tags=["Tag"])

# 새 태그 생성
@router.get("/")
def create(name : str, db : Session = Depends(get_db)):
    tag = Tag(name=name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

# 태그 조회
@router.post("/")
def list(db : Session = Depends(get_db)):
    return db.query(Tag).all()

# 태그 삭제