from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_db
from app.schemas import QuoteTagCreate, QuoteTagRead
from app.services import quote_tag_service

router = APIRouter(prefix="/quote-tags", tags=["QuoteTags"])

# 문장 - 태그 추가
@router.post("/", response_model=QuoteTagRead)
async def add_quote_tag(quote_tag: QuoteTagCreate, db: AsyncSession = Depends(get_async_db)):
    return await quote_tag_service.repository.create(db, obj_in=quote_tag)

# 태그 조회
@router.get("/", response_model=list[QuoteTagRead])
async def list_quote_tags(db: AsyncSession = Depends(get_async_db)):
    return await quote_tag_service.repository.get_all(db)

# 태그 삭제
@router.delete("/")
async def remove_quote_tag(quote_id: int, tag_id: int, db: AsyncSession = Depends(get_async_db)):
    quote_tag = await quote_tag_service.repository.get(db, id=(quote_id, tag_id))
    if not quote_tag:
        raise HTTPException(status_code=400, detail="태그를 찾을 수 없습니다.")
    await quote_tag_service.repository.remove(db, id=(quote_id, tag_id))
    return {"message": "태그 삭제 완료"}