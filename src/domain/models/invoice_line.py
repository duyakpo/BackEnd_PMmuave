from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from src.default import db

Base = db.Model

class InvoiceLine(Base):
    __tablename__ = "invoice_lines"

    line_id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.invoice_id"))
    ticket_id = Column(Integer, ForeignKey("tickets.ticket_id"))

    invoice = relationship("Invoice", back_populates="line")
    ticket = relationship("Ticket")