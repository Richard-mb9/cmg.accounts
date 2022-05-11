from src.infra.repositories.users_info_repository import UsersInfoRepository
from src.domain.models.users_info import UsersInfo
from src.security.security import get_user_id_in_token
from src.utils.handlers import object_as_dict

class UsersInfoService:
    def __init__(self):
        self.repository = UsersInfoRepository(UsersInfo)
        self.user_id_logged = None

    def __get_user_id_logged(self):
        if self.user_id_logged is None:
            self.user_id_logged = get_user_id_in_token()
        return self.user_id_logged

    def __update(self,data):
        user_info_updated =  self.repository.update(self.__get_user_id_logged(), data)
        return object_as_dict(user_info_updated)
    
    def __create(self, data):
        users_info = UsersInfo(
            user_id=self.__get_user_id_logged(), 
            name=data.get('name'), 
            cpf=data.get('cpf')
        )
        return object_as_dict(self.repository.create(users_info))

    def create_and_update(self, data):
        users_info = self.read_by_id()
        if users_info is not None:
            self.__update(data)
        return self.__create(data)

    def get_user_info_logged(self):
        user_info = self.repository.read_by_id(self.__get_user_id_logged())
        if user_info is None:
            return {}
        return object_as_dict(user_info)
    
    def read_by_id(self, id: int = None) -> UsersInfo:
        user_id = self.__get_user_id_logged() if id is None else id
        return self.repository.read_by_id(user_id)
