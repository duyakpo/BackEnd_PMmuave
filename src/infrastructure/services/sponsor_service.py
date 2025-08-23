# infrastructure/services/sponsor_service.py
from infrastructure.repositories.sponsor_repositories import SponsorRepository

class SponsorService:
    def __init__(self):
        self.repo = SponsorRepository()

    def create_sponsor(self, data):
        return self.repo.create(data)

    def get_sponsor(self, sponsor_id):
        return self.repo.get_by_id(sponsor_id)

    def list_sponsors(self):
        return self.repo.list_all()

