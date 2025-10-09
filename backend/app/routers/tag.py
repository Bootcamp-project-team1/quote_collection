from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.tag import Tag

router = APIRouter(prefix="/tag", tags=["Tag"])

# 새 태그 생성
@router.post("/")
def create(name : str, db : Session = Depends(get_db)):
    tag = Tag(name=name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag

# 태그 조회
@router.get("/")
def list(db : Session = Depends(get_db)):
    return db.query(Tag).all()

# 태그 삭제
@router.delete("/")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.query(Tag).get(tag_id)
    if not tag:
        raise HTTPException(status_code=400, detail="태그를 찾을 수 없습니다.")
    db.delete(tag)
    db.commit()
    return {"message" : "태그 삭제 됨"}