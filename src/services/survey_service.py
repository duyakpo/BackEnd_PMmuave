from src.domain.repositories.survey_repository import SurveyRepository

class SurveyService:
    def __init__(self):
        self.repo = SurveyRepository()

    def create(self, event_id, title):
        return self.repo.create(event_id, title)