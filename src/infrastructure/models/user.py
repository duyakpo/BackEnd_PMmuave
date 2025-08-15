from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base
class UserModel(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    phone = Column(String(50))
    role = Column(String(50), nullable=False) 
    created_at = Column(DateTime)
    updated_at = Column(DateTime)