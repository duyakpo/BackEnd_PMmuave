from sqlalchemy import Column, Integer, String, DateTime
from infrastructure.databases.base import Base
class SponsorModel(Base):
    __tablename__ = 'sponsors'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    contact_person = Column(String(255))
    phone = Column(String(50))
    email = Column(String(255))
