# infrastructure/repositories/sponsor_repository.py
from infrastructure.databases.mssql import session
from infrastructure.models.sponsor_model import SponsorModel

class SponsorRepository:
    def create(self, data):
        sponsor = SponsorModel(**data)
        session.add(sponsor)
        session.commit()
        session.refresh(sponsor)
        return sponsor

    def get_by_id(self, sponsor_id):
        return session.query(SponsorModel).filter_by(id=sponsor_id).first()

    def list_all(self):
        return session.query(SponsorModel).all()

