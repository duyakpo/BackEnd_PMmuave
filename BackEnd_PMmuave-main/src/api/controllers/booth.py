import uuid
from flask import Blueprint, request, jsonify
from database import SessionLocal
from model import BoothVisit
from schemas import BoothVisitSchema

bp_booth = Blueprint("booth", __name__)
booth_schema = BoothVisitSchema()

@bp_booth.route("/api/booth", methods=["POST"])
def create_booth_visit():
    data = request.get_json()
    errors = booth_schema.validate(data)
    if errors:
        return jsonify({
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }), 400

    db = SessionLocal()
    try:
        visit = BoothVisit(id=str(uuid.uuid4()), **data)
        db.add(visit)
        db.commit()
        db.refresh(visit)

        return jsonify({
            "success": True,
            "message": "Booth visit created successfully",
            "data": booth_schema.dump(visit)
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({
            "success": False,
            "message": f"Database error: {str(e)}"
        }), 500
    finally:
        db.close()
