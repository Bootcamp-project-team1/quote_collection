from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_db
from app.schemas import QuoteCreate, QuoteRead, QuoteUpdate, QuoteCreateWithSource
from app.services import quote_service, user_service, source_service

router = APIRouter(prefix="/quote", tags=["Quote"])

@router.post("/with_source", response_model=QuoteRead)
async def create_quote_with_source(quote_data: QuoteCreateWithSource, db: AsyncSession = Depends(get_async_db)):
    user = await user_service.repository.get(db, id=quote_data.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    source = await source_service.repository.get_by_title_and_creator(
        db, title=quote_data.source.title, creator=quote_data.source.creator
    )
    if not source:
        source = await source_service.repository.create(db, obj_in=quote_data.source)

    quote_create = QuoteCreate(
        content=quote_data.content,
        page=quote_data.page,
        user_id=quote_data.user_id,
        source_id=source.id,
    )
    return await quote_service.repository.create(db, obj_in=quote_create)

@router.post("/", response_model=QuoteRead)
async def create_quote(quote: QuoteCreate, db: AsyncSession = Depends(get_async_db)):
    user = await user_service.repository.get(db, id=quote.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    source = await source_service.repository.get(db, id=quote.source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
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
