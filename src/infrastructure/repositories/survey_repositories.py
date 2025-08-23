from infrastructure.databases.mssql import session
from infrastructure.models.survey_model import SurveyModel

class SurveyRepository:
    def create(self, data):
        survey = SurveyModel(**data)
        session.add(survey)
        session.commit()
        session.refresh(survey)
        return survey

    def get_by_id(self, survey_id):
        return session.query(SurveyModel).filter(SurveyModel.id == survey_id).first()

    def list_all(self):
        return session.query(SurveyModel).all()
