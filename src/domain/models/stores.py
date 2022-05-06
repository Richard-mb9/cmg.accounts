from src.config import Base

from sqlalchemy import Column, Integer, String, ForeignKey


class Stores(Base):
    __tablename__ = 'sotores'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String)
    corporate_name = Column(String)
    cnpj = Column(String)

    def __repr__(self): # pragma: no cover
        return f'Store {self.corporate_name}'
