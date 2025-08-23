# src/infrastructure/services/event_service.py
from infrastructure.repositories.event_reponsitories import EventRepository

class EventService:
    def __init__(self):
        self.repo = EventRepository()

    def create_event(self, data):
        return self.repo.create(data)

    def get_event(self, event_id):
        return self.repo.get_by_id(event_id)

    def list_events(self):
        return self.repo.list_all()
