from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.producer import Producer

router = APIRouter(prefix="/producers", tags=["Producers"])

# 제작사 등록
@router.post("/")
def create_producer(name: str, pd_type: str, db: Session = Depends(get_db)):
    producer = Producer(name=name, pd_type=pd_type)
    db.add(producer)
    db.commit()
    db.refresh(producer)
    return producer

# 등록된 제작사 조회
@router.get("/")
def list_producers(db: Session = Depends(get_db)):
    return db.query(Producer).all()

# 등록된 제작사 삭제
@router.delete("/")
def delete_producer(producer_id: int, db: Session = Depends(get_db)):
    producer = db.query(Producer).filter(Producer.id == producer_id).first()
    if not producer:
        raise HTTPException(status_code=400, detail="제작사를 찾을 수 없습니다.")
    db.delete(producer)
    db.commit()
    return {"message" : "제작사 삭제 완료"}
