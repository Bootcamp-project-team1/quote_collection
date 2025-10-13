from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.bookmark import Bookmark

router = APIRouter(prefix="/bookmark", tags=["Bookmark"])

# 북마크 추가
@router.post("/")
def create_bookmark(user_id : int, quote_id : int, db : Session = Depends(get_db)):
    bookmark = Bookmark(user_id = user_id, quote_id = quote_id)
    db.add(bookmark)
    db.commit()
    return {"message" : "북마크 추가"}

# 조회
@router.get("/")
def list_bookmark(db : Session = Depends(get_db)):
    return db.query(Bookmark).all()

# 삭제
@router.delete("/")
def delete_bookmark(user_id : int, quote_id : int, db : Session = Depends(get_db)):
    bookmark = db.query(Bookmark).filter(Bookmark.user_id == user_id, Bookmark.quote_id == quote_id).first()
    if not bookmark : 
        raise HTTPException(status_code=400, detail = "북마크를 찾을 수 없음")
    db.delete(bookmark)
    db.commit()
    return {"message" : "북마크 삭제 됨"}