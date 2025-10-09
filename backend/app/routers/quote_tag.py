from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.quote_tag import QuoteTag

router = APIRouter(prefix="/quote-tags", tags=["QuoteTags"])

# 문장 - 태그 추가
@router.post("/")
def add_quote_tag(quote_id: int, tag_id: int, db: Session = Depends(get_db)):
    quote_tag = QuoteTag(quote_id=quote_id, tag_id=tag_id)
    db.add(quote_tag)
    db.commit()
    db.refresh(quote_tag)
    return quote_tag

# 태그 조회
@router.get("/")
def list_quote_tags(db: Session = Depends(get_db)):
    return db.query(QuoteTag).all()

# 태그 삭제
@router.delete("/")
def remove_quote_tag(quote_id: int, tag_id: int, db: Session = Depends(get_db)):
    quote_tag = db.query(QuoteTag).filter(QuoteTag.quote_id == quote_id, QuoteTag.tag_id == tag_id).first()
    if not quote_tag:
        raise HTTPException(status_code=400, detail="태그를 찾을 수 없습니다.")
    db.delete(quote_tag)
    db.commit()
    return{"태그 삭제 완료"}