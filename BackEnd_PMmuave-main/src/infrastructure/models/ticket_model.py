from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Ticket(Base):
    __tablename__ = "tickets"

    ticket_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    event_id = Column(Integer, ForeignKey("events.event_id"))
    ticket_type_id = Column(Integer, ForeignKey("ticket_types.ticket_type_id"))

    user = relationship("User")
    event = relationship("Event", back_populates="tickets")
    ticket_type = relationship("TicketType")
