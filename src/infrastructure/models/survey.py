from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Survey(Base):
    __tablename__= "surveys"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    responses = relationship("SurveyResponse", back_populates="survey")
    