from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from .invoice import Base

class InvoiceLine(Base):
    __tablename__ = 'invoice_lines'
    
    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'))
    product_name = Column(String(100))
    quantity = Column(Integer)
    price = Column(Float)
    
    invoice = relationship("Invoice", back_populates="lines")
