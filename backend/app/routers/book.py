from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.book import Book

router = APIRouter(prefix="/book", tags=["Book"])

# 책 등록
@router.post("/")
def create(title : str, author : str, db : Session = Depends(get_db)):
    book = Book(title=title, author=author)
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

# 등록된 책 조회
@router.get("/")
def list(db : Session = Depends(get_db)):
    return db.query(Book).all()

# 등록된 책 삭제 : isbn 대신 책 제목을 통해 삭제되도록 변경
@router.delete("/")
def delete_book(title : str, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.title == title).first()
    if not book:
        raise HTTPException(status_code=400, detail="책을 찾을 수 없습니다.")
    db.delete(book)
    db.commit()
    return {"message": "책 삭제 됨"}