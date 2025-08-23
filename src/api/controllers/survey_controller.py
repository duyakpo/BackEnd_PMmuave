from flask import Blueprint, request, jsonify
from api.schemas.survey_schema import SurveyRequestSchema, SurveyResponseSchema
from infrastructure.services.survey_service import SurveyService

bp = Blueprint("survey", __name__, url_prefix="/api/surveys")

service = SurveyService()
req_schema = SurveyRequestSchema()
res_schema = SurveyResponseSchema()

@bp.route("", methods=["POST"])
def create_survey():
    """
    Create a new survey
    ---
    post:
      summary: Create a survey
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/SurveyRequest'
      responses:
        201:
          description: Survey created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SurveyResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = req_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    survey = service.create_survey(data)
    return jsonify(res_schema.dump(survey)), 201

@bp.route("/<int:survey_id>", methods=["GET"])
def get_survey(survey_id):
    """
    Get survey by ID
    ---
    get:
      summary: Get survey info
      parameters:
        - name: survey_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: Survey details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SurveyResponse'
        404:
          description: Survey not found
    """
    survey = service.get_survey(survey_id)
    if not survey:
        return jsonify({"message": "Survey not found"}), 404
    return jsonify(res_schema.dump(survey)), 200

@bp.route("", methods=["GET"])
def list_surveys():
    """
    List all surveys
    ---
    get:
      summary: List all surveys
      responses:
        200:
          description: List of surveys
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/SurveyResponse'
    """
    surveys = service.list_surveys()
    return jsonify(res_schema.dump(surveys, many=True)), 200
