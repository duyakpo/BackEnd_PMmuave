from infrastructure.databases.mssql import session
from infrastructure.models.survey_response_model import SurveyResponseModel

class SurveyResponseRepository:
    def create(self, data):
        sr = SurveyResponseModel(**data)
        session.add(sr)
        session.commit()
        session.refresh(sr)
        return sr

    def list_all(self):
        return session.query(SurveyResponseModel).all()
