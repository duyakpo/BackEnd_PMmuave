from infrastructure.repositories.survey_reponse_repositories import SurveyResponseRepository

class SurveyResponseService:
    def __init__(self):
        self.repo = SurveyResponseRepository()

    def create_response(self, data):
        return self.repo.create(data)

    def list_responses(self):
        return self.repo.list_all()
