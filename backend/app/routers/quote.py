from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.quote import Quote

router = APIRouter(prefix="/quote", tags=["Quote"])

@router.post("/")
def create_quote(user_id: int, content : str, book_id: int = None, page: int = 0 , db: Session = Depends(get_db)):
    quote = Quote(user_id=user_id, content=content, book_id=book_id,  page=page)
    db.add(quote)
    db.commit()
    db.refresh(quote)
    return quote

@router.get("/")
def list_quotes(db: Session = Depends(get_db)):
    return db.query(Quote).all()

@router.delete("/")
def delete_quote(quote_id: int, db: Session = Depends(get_db)):
    quote = db.query(Quote).filter(Quote.id == quote_id).first()
    if not quote:
        raise HTTPException(status_code=400, detail="문장을 찾을 수 없습니다.")
    db.delete(quote)
    db.commit()
    return {"문장 삭제 됨"}
