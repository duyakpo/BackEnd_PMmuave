# src/infrastructure/repositories/account_repositories.py
from sqlalchemy.orm import Session
from typing import List, Optional
from infrastructure.models.accounts_model import Account 

class AccountRepository:
    def __init__(self, session: Session):
        """
        Hàm khởi tạo sẽ nhận một đối tượng session.
        Tất cả các thao tác trong class này sẽ dùng self.session.
        """
        self.session = session

    def create(self, data: dict) -> Account:
        account = Account(**data)
        self.session.add(account)
        self.session.commit()
        self.session.refresh(account)
        return account

    def get_by_email(self, email: str) -> Optional[Account]:
        return self.session.query(Account).filter_by(email=email).first()

    def get_by_ma_user(self, ma_user: int) -> Optional[Account]:
        return self.session.query(Account).filter_by(ma_user=ma_user).first()

    def update_by_ma_user(self, ma_user: int, data: dict) -> Optional[Account]:
        account = self.get_by_ma_user(ma_user)
        if account:
            for key, value in data.items():
                setattr(account, key, value)
            self.session.commit()
            self.session.refresh(account)
        return account

    def list_all(self) -> List[Account]:
        return self.session.query(Account).all()