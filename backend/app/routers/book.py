from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.book import Book

router = APIRouter(prefix="/book", tags=["Book"])

# 책 등록
@router.post("/")
def create(title : str, author : str, isbn : str = None, db : Session = Depends(get_db)):
    book = Book(title=title, author=author, isbn=isbn)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

# 등록된 책 조회
@router.get("/")
def list(db : Session = Depends(get_db)):
    return db.query(Book).all()

# 등록된 책 삭제
@router.delete("/")
def delete_book(isbn : str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.isbn == isbn).first()
    if not book:
        raise HTTPException(status_code=400, detail="책을 찾을 수 없습니다.")
    db.delete(book)
    db.commit()
    return {"message": "책 삭제 됨"}