from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from infrastructure.databases.base import Base
class InvoiceLineModel(Base):
    __tablename__ = 'invoice_lines'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    invoice_id = Column(Integer, ForeignKey('invoices.id'), nullable=False)
    ticket_id = Column(Integer, ForeignKey('tickets.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)