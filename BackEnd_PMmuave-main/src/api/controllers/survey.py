import uuid
from flask import Blueprint, request, jsonify
from database import SessionLocal
from model import Survey
from schemas import SurveySchema

bp_survey = Blueprint("survey", __name__)
survey_schema = SurveySchema()

@bp_survey.route("/api/survey", methods=["POST"])
def create_survey():
    data = request.get_json()
    errors = survey_schema.validate(data)
    if errors:
        return jsonify({
            "success": False,
            "message": "Validation failed",
            "errors": errors
        }), 400

    db = SessionLocal()
    try:
        survey = Survey(id=str(uuid.uuid4()), **data)
        db.add(survey)
        db.commit()
        db.refresh(survey)  # load lại object từ DB
        return jsonify({
            "success": True,
            "message": "Survey created successfully",
            "data": survey_schema.dump(survey)
        }), 201
    except Exception as e:
        db.rollback()
        return jsonify({
            "success": False,
            "message": f"Database error: {str(e)}"
        }), 500
    finally:
        db.close()
