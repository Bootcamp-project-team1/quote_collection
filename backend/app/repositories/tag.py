from app.models import Tag
from app.repositories.base import BaseRepository


class TagRepository(BaseRepository[Tag]):
    pass


tag_repository = TagRepository(Tag)
