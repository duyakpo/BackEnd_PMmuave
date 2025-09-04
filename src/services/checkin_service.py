from src.domain.repositories.checkin_repository import CheckinRepository

class CheckinService:
    def __init__(self):
        self.repo = CheckinRepository()

    def create(self, user_id, event_id):
        return self.repo.create(user_id, event_id)