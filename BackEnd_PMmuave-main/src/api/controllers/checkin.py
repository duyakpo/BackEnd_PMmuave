import uuid
from flask import Blueprint, request, jsonify
from database import SessionLocal
from models import Checkin
from schemas import CheckinSchema

bp_checkin = Blueprint("checkin", __name__)
checkin_schema = CheckinSchema()

@bp_checkin.route("/api/checkin", methods=["POST"])
def create_checkin():
    data = request.get_json()
    errors = checkin_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    db = SessionLocal()
    try:
        new_checkin = Checkin(id=str(uuid.uuid4()), **data)
        db.add(new_checkin)
        db.commit()
        return checkin_schema.dump(new_checkin), 201
    finally:
        db.close()
