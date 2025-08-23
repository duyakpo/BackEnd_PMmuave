from infrastructure.databases.mssql import session
from infrastructure.models.ticket_model import TicketModel

class TicketRepository:
    def create(self, data):
        ticket = TicketModel(**data)
        session.add(ticket)
        session.commit()
        session.refresh(ticket)
        return ticket

    def get_by_id(self, ticket_id):
        return session.query(TicketModel).filter_by(id=ticket_id).first()

    def list_all(self):
        return session.query(TicketModel).all()


