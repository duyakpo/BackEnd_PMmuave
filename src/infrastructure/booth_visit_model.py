from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base
 
class BoothVisit(Base):
   __tablename__ = "booth_visits"
 
   visit_id = Column(Integer, primary_key=True, index=True)
   sponsor_id = Column(Integer, ForeignKey("sponsors.sponsor_id"))
   user_id = Column(Integer, ForeignKey("users.user_id"))
   visit_time = Column(DateTime)
 
   sponsor = relationship("Sponsor")
   user = relationship("User")