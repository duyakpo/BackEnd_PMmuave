from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

from ticketing_app import db
from ticketing_app.models import User, Event, Ticket

ticketing_bp = Blueprint("ticketing_bp", __name__)

# ----------------- AUTH -----------------
@ticketing_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already exists"}), 400

    user = User(
        username=data["username"],
        password=generate_password_hash(data["password"])
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201


@ticketing_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"error": "Invalid username or password"}), 401

    token = create_access_token(identity=user.id)
    return jsonify({"access_token": token}), 200


# ----------------- EVENT -----------------
@ticketing_bp.route("/events", methods=["POST"])
def create_event():
    data = request.json
    try:
        event = Event(
            name=data["name"],
            location=data["location"],
            date=datetime.fromisoformat(data["date"])
        )
        db.session.add(event)
        db.session.commit()
        return jsonify({"message": "Event created successfully", "id": event.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@ticketing_bp.route("/events", methods=["GET"])
def list_events():
    events = Event.query.all()
    return jsonify([
        {
            "id": e.id,
            "name": e.name,
            "location": e.location,
            "date": e.date.isoformat()
        }
        for e in events
    ]), 200


# ----------------- TICKET -----------------
@ticketing_bp.route("/tickets", methods=["POST"])
@jwt_required()
def buy_ticket():
    user_id = get_jwt_identity()
    data = request.json
    try:
        ticket = Ticket(
            seat_number=data["seat_number"],
            user_id=user_id,
            event_id=data["event_id"]
        )
        db.session.add(ticket)
        db.session.commit()
        return jsonify({"message": "Ticket purchased successfully", "id": ticket.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@ticketing_bp.route("/tickets", methods=["GET"])
@jwt_required()
def list_tickets():
    user_id = get_jwt_identity()
    tickets = Ticket.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": t.id,
            "seat_number": t.seat_number,
            "purchased_at": t.purchased_at.isoformat(),
            "event": t.event.name if t.event else None
        }
        for t in tickets
    ]), 200
