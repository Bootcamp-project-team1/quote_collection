from app.models import Source
from app.repositories.base import BaseRepository


class SourceRepository(BaseRepository[Source]):
    pass


source_repository = SourceRepository(Source)
