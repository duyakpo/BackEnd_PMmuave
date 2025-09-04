from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from . import Base

class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    date = Column(DateTime)

    lines = relationship("InvoiceLine", back_populates="invoice")
    user = relationship("User", back_populates="invoices")
