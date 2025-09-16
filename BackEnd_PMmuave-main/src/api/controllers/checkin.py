import uuid
from flask import Blueprint, request, jsonify
from database import SessionLocal
from model import Checkin
from schemas import CheckinSchema

bp_checkin = Blueprint("checkin", __name__)
checkin_schema = CheckinSchema()

@bp_checkin.route("/api/checkin", methods=["POST"])
def create_checkin():
    data = request.get_json()
    errors = checkin_schema.validate(data)
    if errors:
        return jsonify({
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }), 400

    db = SessionLocal()
    try:
        new_checkin = Checkin(id=str(uuid.uuid4()), **data)
        db.add(new_checkin)
        db.commit()
        db.refresh(new_checkin)  # đảm bảo lấy dữ liệu mới nhất từ DB

        return jsonify({
            "success": True,
            "message": "Checkin created successfully",
            "data": checkin_schema.dump(new_checkin)
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({
            "success": False,
            "message": f"Database error: {str(e)}"
        }), 500
    finally:
        db.close()
