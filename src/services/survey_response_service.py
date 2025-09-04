from src.domain.repositories.survey_reponse_repository import SurveyResponseRepository

class SurveyResponseService:
    def __init__(self):
        self.repo = SurveyResponseRepository()

    def create(self, survey_id, user_id, answer):
        return self.repo.create(survey_id, user_id, answer)

    def get_by_survey(self, survey_id):
        return self.repo.get_by_survey(survey_id)    