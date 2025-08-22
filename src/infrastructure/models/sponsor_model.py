<<<<<<< HEAD
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from infrastructure.databases.base import Base
class SponsorModel(Base):
    __tablename__ = "sponsors"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    company_name = Column(String(255), nullable=False)
=======
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float, Text
from infrastructure.databases.base import Base
class SponsorModel(Base):
    __tablename__ = "sponsors"
    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    event_id = Column(Integer, ForeignKey("events.id"), nullable=False)
    company_name = Column(String(255), nullable=False)
>>>>>>> 76b11cf79d76e4d4a56d8a8e010d0ba49af93f46
    booth_location = Column(String(255))