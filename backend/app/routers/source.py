from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.source import Source

router = APIRouter(prefix="/source", tags=["Source"])

@router.post("/")
def create_source(source_type: str, pd_id: int, data: dict, db: Session = Depends(get_db)):
    source = Source(source_type=source_type, pd_id=pd_id, data=data)
    db.add(source)
    db.commit()
    db.refresh(source)
    return source

@router.get("/")
def list_sources(db: Session = Depends(get_db)):
    return db.query(Source).all()

@router.delete("/")
def delete_source(source_id: int, db: Session = Depends(get_db)):
    source = db.query(Source).filter(Source.id == source_id).first()
    if not source:
        raise HTTPException(status_code=400, detail="소스를 찾을 수 없습니다.")
    db.delete(source)
    db.commit()
    return {"소스 삭제 완료"}
