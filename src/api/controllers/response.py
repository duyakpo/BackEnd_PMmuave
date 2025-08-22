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
        return jsonify(errors), 400

    db = SessionLocal()
    try:
        response = SurveyResponse(id=str(uuid.uuid4()), **data)
        db.add(response)
        db.commit()
        return response_schema.dump(response), 201
    finally:
        db.close()
