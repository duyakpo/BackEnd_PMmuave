from ticketing_app import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Quan hệ 1-n: 1 User có thể mua nhiều Ticket
    tickets = db.relationship("Ticket", back_populates="user", cascade="all, delete-orphan")


class Event(db.Model):
    __tablename__ = "events"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    # Quan hệ 1-n: 1 Event có nhiều Ticket
    tickets = db.relationship("Ticket", back_populates="event", cascade="all, delete-orphan")


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    seat_number = db.Column(db.String(20), nullable=False)
    purchased_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Khóa ngoại
    user_id = db.Column(db.Integer, db.ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey("events.id", ondelete="CASCADE"), nullable=False)

    # Quan hệ ngược
    user = db.relationship("User", back_populates="tickets")
    event = db.relationship("Event", back_populates="tickets")
