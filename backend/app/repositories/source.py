from app.models import Source
from app.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


class SourceRepository(BaseRepository[Source]):
    async def get_by_title_and_creator(self, db: AsyncSession, *, title: str, creator: str) -> Source | None:
        statement = select(Source).filter(Source.title == title, Source.creator == creator)
        result = await db.execute(statement)
        return result.scalar_one_or_none()


source_repository = SourceRepository(Source)
