from sqlalchemy import Column, Integer, String, Float, DateTime, Text, ForeignKey
from infrastructure.databases.base import Base

class AccountModel(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    ma_user = Column(String(50), nullable=False)
    name = Column(String(100), nullable=False)
    email = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    vai_tro = Column(String(50), nullable=False)