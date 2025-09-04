import uuid
from flask import Blueprint, request, jsonify
from database import SessionLocal
from models import BoothVisit
from schemas import BoothVisitSchema

bp_booth = Blueprint("booth", __name__)
booth_schema = BoothVisitSchema()

@bp_booth.route("/api/booth", methods=["POST"])
def create_booth_visit():
    data = request.get_json()
    errors = booth_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    db = SessionLocal()
    try:
        visit = BoothVisit(id=str(uuid.uuid4()), **data)
        db.add(visit)
        db.commit()
        return booth_schema.dump(visit), 201
    finally:
        db.close()
