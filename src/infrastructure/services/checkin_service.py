from infrastructure.repositories.checkin_repositories import CheckInRepository

class CheckInService:
    def __init__(self):
        self.repo = CheckInRepository()

    def create_checkin(self, data):
        return self.repo.create(data)

    def get_checkin(self, checkin_id):
        return self.repo.get_by_id(checkin_id)

    def list_checkins(self):
        return self.repo.list_all()
