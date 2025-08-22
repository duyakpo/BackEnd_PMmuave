from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from infrastructure.databases.base import Base
class BoothVisitModel(Base):
    __tablename__ = "booth_visits"
    id = Column(Integer, primary_key=True)
    sponsor_id = Column(Integer, ForeignKey("sponsors.id"), nullable=False)
    visitor_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    visit_time = Column(DateTime, nullable=False)
