from src.infra.repositories.base_repository import BaseRepository
from src.config import get_session


class TelephonesRepository(BaseRepository):
    def __init__(self, entity):
        super().__init__(entity)

    def list_by_user_id(self, user_id):
        session = get_session()
        return session.query(self.entity).filter_by(user_id=user_id).all()