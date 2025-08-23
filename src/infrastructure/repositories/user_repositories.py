# src/infrastructure/repositories/user_repository.py
from infrastructure.models.user_model import UserModel
from infrastructure.databases.mssql import session

class UserRepository:
    def create(self, data):
        user = UserModel(**data)
        session.add(user)
        session.commit()
        session.refresh(user)
        return user

    def get_by_id(self, user_id):
        return session.query(UserModel).filter_by(id=user_id).first()

    def list_all(self):
        return session.query(UserModel).all()
