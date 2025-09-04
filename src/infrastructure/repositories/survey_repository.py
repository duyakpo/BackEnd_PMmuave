from src.domain.models.survey import Survey
from src.default import db
 
class SurveyRepository:
    def create(self, event_id, title):
        survey = Survey(event_id=event_id, title=title)
        db.session.add(survey)
        db.session.commit()
        return survey