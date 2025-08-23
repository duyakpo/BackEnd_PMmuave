from infrastructure.repositories.survey_repositories import SurveyRepository

class SurveyService:
    def __init__(self):
        self.repo = SurveyRepository()

    def create_survey(self, data):
        return self.repo.create(data)

    def get_survey(self, survey_id):
        return self.repo.get_by_id(survey_id)

    def list_surveys(self):
        return self.repo.list_all()
