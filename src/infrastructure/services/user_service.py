# src/infrastructure/services/user_service.py
from infrastructure.repositories.user_repositories import UserRepository

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, data):
        return self.repo.create(data)

    def get_user(self, user_id):
        return self.repo.get_by_id(user_id)

    def list_users(self):
        return self.repo.list_all()
