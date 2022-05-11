from src.infra.repositories.base_repository import BaseRepository


class StoresRepository(BaseRepository):
    def __init__(self, entity):
        super().__init__(entity)