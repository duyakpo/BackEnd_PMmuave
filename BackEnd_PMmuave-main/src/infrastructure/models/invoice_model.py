from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from infrastructure.databases.base import Base
class InvoiceModel(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    created_at = Column(DateTime, nullable=False)
    total_amount = Column(Float, nullable=False)