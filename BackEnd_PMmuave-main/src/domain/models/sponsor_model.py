from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from . import Base

class Sponsor(Base):
    __tablename__ = "sponsors"

    sponsor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    industry = Column(String)

    booth_visits = relationship("BoothVisit", back_populates="sponsor")
