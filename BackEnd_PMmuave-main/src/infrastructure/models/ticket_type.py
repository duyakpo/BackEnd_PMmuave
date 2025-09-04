from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from infrastructure.databases.base import Base
class TicketTypeModel(Base):
    __tablename__ = "ticket_types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)

    tickets = relationship("Ticket", back_populates="ticket_type")
