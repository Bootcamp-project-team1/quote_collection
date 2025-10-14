from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_async_db
from app.schemas import SourceCreate, SourceRead, SourceUpdate
from app.services import source_service

router = APIRouter(prefix="/source", tags=["Source"])

@router.post("/", response_model=SourceRead)
async def create_source(source: SourceCreate, db: AsyncSession = Depends(get_async_db)):
    return await source_service.repository.create(db, obj_in=source)

@router.get("/", response_model=list[SourceRead])
async def list_sources(db: AsyncSession = Depends(get_async_db)):
    return await source_service.repository.get_all(db)

@router.get("/{source_id}", response_model=SourceRead)
async def get_source(source_id: int, db: AsyncSession = Depends(get_async_db)):
    source = await source_service.repository.get(db, id=source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    return source

@router.put("/{source_id}", response_model=SourceRead)
async def update_source(source_id: int, source_in: SourceUpdate, db: AsyncSession = Depends(get_async_db)):
    source = await source_service.repository.get(db, id=source_id)
    if not source:
        raise HTTPException(status_code=404, detail="Source not found")
    source = await source_service.repository.update(db, db_obj=source, obj_in=source_in)
    return source

@router.delete("/{source_id}")
async def delete_source(source_id: int, db: AsyncSession = Depends(get_async_db)):
    source = await source_service.repository.get(db, id=source_id)
    if not source:
        raise HTTPException(status_code=400, detail="소스를 찾을 수 없습니다.")
    await source_service.repository.remove(db, id=source_id)
    return {"message": "소스 삭제 완료"}
