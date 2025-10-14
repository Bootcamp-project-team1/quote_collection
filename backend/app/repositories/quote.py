from app.models import Quote
from app.repositories.base import BaseRepository


class QuoteRepository(BaseRepository[Quote]):
    pass


quote_repository = QuoteRepository(Quote)
