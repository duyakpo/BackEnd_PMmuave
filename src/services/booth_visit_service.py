from src.domain.repositories.booth_visit_repository import BoothVisitRepository

class BoothVisitService:
    def __init__(self):
        self.repo = BoothVisitRepository()

    def create(self, sponsor_id, user_id, event_id):
        return self.repo.create(sponsor_id, user_id, event_id)