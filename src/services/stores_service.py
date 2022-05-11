from ast import Store
from src.infra.repositories.stores_repository import StoresRepository
from src.domain.models.stores import Stores
from src.security.security import get_user_id_in_token
from src.utils.handlers import object_as_dict

class StoresService:
    def __init__(self):
        self.repository = StoresRepository(Stores)
        self.user_id_logged = None

    def __get_user_id_logged(self):
        if self.user_id_logged is None:
            self.user_id_logged = get_user_id_in_token()
        return self.user_id_logged

    def __update(self,data):
        store_updated =  self.repository.update(self.__get_user_id_logged(), data)
        return object_as_dict(store_updated)
    
    def __create(self, data):
        store = Stores(
            user_id=self.__get_user_id_logged(), 
            name=data.get('name'), 
            cnpj=data.get('cnpj'),
            corporate_name=data.get('corporate_name')
        )
        return object_as_dict(self.repository.create(store))

    def create_and_update(self, data):
        store = self.read_by_user_id()
        if store is not None:
            self.__update(data)
        return self.__create(data)

    def get_store_logged(self):
        store = self.repository.read_by_id(self.__get_user_id_logged())
        if store is None:
            return {}
        return object_as_dict(store)
    
    def read_by_user_id(self, id: int = None) -> Store:
        user_id = self.__get_user_id_logged() if id is None else id
        return self.repository.read_by_id(user_id)
