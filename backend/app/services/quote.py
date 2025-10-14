from app.repositories import quote_repository
from app.services.base import BaseService
from app.repositories.quote import QuoteRepository


class QuoteService(BaseService[QuoteRepository]):
    pass


quote_service = QuoteService(quote_repository)
