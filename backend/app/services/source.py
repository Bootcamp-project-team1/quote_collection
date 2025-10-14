from app.repositories import source_repository
from app.services.base import BaseService
from app.repositories.source import SourceRepository


class SourceService(BaseService[SourceRepository]):
    pass


source_service = SourceService(source_repository)
