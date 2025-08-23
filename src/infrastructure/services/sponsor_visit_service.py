from infrastructure.repositories.sponsor_visit_repositories import SponsorVisitRepository

class SponsorVisitService:
    def __init__(self):
        self.repo = SponsorVisitRepository()

    def create_visit(self, data):
        return self.repo.create(data)

    def list_visits(self):
        return self.repo.list_all()
