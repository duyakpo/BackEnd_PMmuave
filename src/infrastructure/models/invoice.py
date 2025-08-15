from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from infrastructure.databases.base import Base
class InvoiceModel(Base):
    __tablename__ = 'invoices'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    total_amount = Column(Float, nullable=False)
    status = Column(String(50), nullable=False)  # paid, unpaid
    created_at = Column(DateTime)
