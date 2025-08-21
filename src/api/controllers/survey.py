import uuid
from flask import Blueprint, request, jsonify
from database import SessionLocal
from models import Survey
from schemas import SurveySchema

bp_survey = Blueprint("survey", __name__)
survey_schema = SurveySchema()

@bp_survey.route("/api/survey", methods=["POST"])
def create_survey():
    data = request.get_json()
    errors = survey_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    db = SessionLocal()
    try:
        survey = Survey(id=str(uuid.uuid4()), **data)
        db.add(survey)
        db.commit()
        return survey_schema.dump(survey), 201
    finally:
        db.close()
