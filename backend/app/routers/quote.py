from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_db
from app.schemas import QuoteCreate, QuoteRead, QuoteUpdate
from app.services import quote_service, user_service, book_service

router = APIRouter(prefix="/quote", tags=["Quote"])

@router.post("/", response_model=QuoteRead)
async def create_quote(quote: QuoteCreate, db: AsyncSession = Depends(get_async_db)):
    user = await user_service.repository.get(db, id=quote.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    if quote.book_id:
        book = await book_service.repository.get(db, id=quote.book_id)
        if not book:
            raise HTTPException(status_code=404, detail="Book not found")
    return await quote_service.repository.create(db, obj_in=quote)

@router.get("/", response_model=list[QuoteRead])
async def list_quotes(db: AsyncSession = Depends(get_async_db)):
    return await quote_service.repository.get_all(db)

@router.get("/{quote_id}", response_model=QuoteRead)
async def get_quote(quote_id: int, db: AsyncSession = Depends(get_async_db)):
    quote = await quote_service.repository.get(db, id=quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    return quote

@router.put("/{quote_id}", response_model=QuoteRead)
async def update_quote(quote_id: int, quote_in: QuoteUpdate, db: AsyncSession = Depends(get_async_db)):
    quote = await quote_service.repository.get(db, id=quote_id)
    if not quote:
        raise HTTPException(status_code=404, detail="Quote not found")
    quote = await quote_service.repository.update(db, db_obj=quote, obj_in=quote_in)
    return quote

@router.delete("/{quote_id}")
async def delete_quote(quote_id: int, db: AsyncSession = Depends(get_async_db)):
    quote = await quote_service.repository.get(db, id=quote_id)
    if not quote:
        raise HTTPException(status_code=400, detail="문장을 찾을 수 없습니다.")
    await quote_service.repository.remove(db, id=quote_id)
    return {"message": "문장 삭제 됨"}
