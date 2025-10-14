from app.models import QuoteTag
from app.repositories.base import BaseRepository


class QuoteTagRepository(BaseRepository[QuoteTag]):
    pass


quote_tag_repository = QuoteTagRepository(QuoteTag)
