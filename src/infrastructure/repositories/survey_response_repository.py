from src.domain.models.survey_response import SurveyResponse
from src.default import db

class SurveyResponseRepository:
    def create (self, survey_id, user_id, answer):
        response = SurveyResponse(survey_id=survey_id, user_id=user_id, answer=answer)
        db.session.add(response)
        db.session.commit()
        return response
    
    def get_by_survey(self, survey_id):
        return db.session.query(SurveyResponse).filter_by(survey_id=survey_id).all()