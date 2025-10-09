from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.like import Like

router = APIRouter(prefix="/likes", tags=["Likes"])

# 좋아요 추가
@router.post("/")
def create_like(user_id : int, quote_id : int, db : Session = Depends(get_db)):
    like = Like(user_id = user_id, quote_id = quote_id)
    db.add(like)
    db.commit()
    return {"message" : "좋아요 추가"}

# 조회
@router.get("/")
def list_likes(db : Session = Depends(get_db)):
    return db.query(Like).all()

# 좋아요 삭제
@router.delete("/")
def delete_like(user_id : int, quote_id : int, db : Session = Depends(get_db)):
    like = db.query(Like).filter(Like.user_id == user_id, Like.quote_id == quote_id).first()
    if not like : 
        raise HTTPException(status_code=400, detail = "좋아요를 찾을 수 없음")
    db.delete(like)
    db.commit()
    return {"message" : "좋아요 삭제 됨"}