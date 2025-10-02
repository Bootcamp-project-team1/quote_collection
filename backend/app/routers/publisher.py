from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.publisher import Publisher

router = APIRouter(prefix="/publisher", tags=["Publisher"])

# 출판사 등록
@router.post("/")
def create(name : str, db : Session = Depends(get_db)):
    publisher = Publisher(name=name)
    db.add(publisher)
    db.commit()
    db.refresh(publisher)
    return publisher

# 등록된 출판사 조회
@router.get("/")
def list(db : Session = Depends(get_db)):
    return db.query(Publisher).all()

# 등록된 출판사 삭제
@router.delete("/")
def delete_publisher(name : str, db: Session = Depends(get_db)):
    publisher = db.query(Publisher).filter(Publisher.name == name).first()
    if not publisher:
        raise HTTPException(status_code=400, detail="출판사를 찾을 수 없습니다.")
    db.delete(publisher)
    db.commit()
    return {"message": "출판사 삭제 됨"}