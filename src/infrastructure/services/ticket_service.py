from infrastructure.repositories.ticket_reponistories import TicketRepository
from infrastructure.repositories.user_repositories import UserRepository
from infrastructure.repositories.event_reponsitories import EventRepository

class TicketService:
    def __init__(self):
        self.repo = TicketRepository()
        self.user_repo = UserRepository()
        self.event_repo = EventRepository()

    def create_ticket(self, data):
        # Check user tồn tại
        if not self.user_repo.get_by_id(data["user_id"]):
            raise ValueError("User not found")
        # Check event tồn tại
        if not self.event_repo.get_by_id(data["event_id"]):
            raise ValueError("Event not found")
        return self.repo.create(data)

    def get_ticket(self, ticket_id):
        return self.repo.get_by_id(ticket_id)

    def list_tickets(self):
        return self.repo.list_all()

