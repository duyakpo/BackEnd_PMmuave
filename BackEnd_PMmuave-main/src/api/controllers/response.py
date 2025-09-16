import uuid
from flask import Blueprint, request, jsonify
from database import SessionLocal
from models import SurveyResponse
from schemas import SurveyResponseSchema

bp_response = Blueprint("response", __name__)
response_schema = SurveyResponseSchema()

@bp_response.route("/api/response", methods=["POST"])
def create_response():
    data = request.get_json()
    errors = response_schema.validate(data)
    if errors:
        return jsonify({
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }), 400

    db = SessionLocal()
    try:
        response = SurveyResponse(id=str(uuid.uuid4()), **data)
        db.add(response)
        db.commit()
        db.refresh(response)
        return jsonify({
            "success": True,
            "message": "Survey response created successfully",
            "data": response_schema.dump(response)  #  Sửa ở đây
        }), 201
    finally:
        db.close()
