from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(100), unique=True, index=True, nullable=False)

    role = Column(
        Enum("guest", "visitor", "sponsor", "operator", "staff", name="account_roles"),
        nullable=False,
        default="guest"
    )

    full_name = Column(String(100), nullable=True)

    # Quan hệ ngược lại với EventModel
    events = relationship("EventModel", back_populates="organizer")

    def __repr__(self):
        return f"<Account id={self.id} username={self.username} role={self.role}>"
