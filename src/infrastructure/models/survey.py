from sqlalchemy import Column, Integer, String, DateTime
from src.infrastructure.databases.base import Base
from sqlalchemy.orm import relationship
import datetime

class Survey(Base):
    __tablename__= "surveys"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    responses = relationship("SurveyResponse", back_populates="survey")
    