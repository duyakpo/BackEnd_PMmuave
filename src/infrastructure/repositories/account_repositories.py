from infrastructure.models.accounts_model import AccountModel
from infrastructure.databases.mssql import session

class AccountRepository:
    def create(self, data):
        account = AccountModel(**data)
        session.add(account)
        session.commit()
        session.refresh(account)
        return account

    def get_by_email(self, email):
        return session.query(AccountModel).filter_by(email=email).first()

    def get_by_ma_user(self, ma_user):
        return session.query(AccountModel).filter_by(ma_user=ma_user).first()

    def update_by_ma_user(self, ma_user, data):
        account = session.query(AccountModel).filter_by(ma_user=ma_user).first()
        if not account:
            return None
        for k, v in data.items():
            setattr(account, k, v)
        session.commit()
        return account

    def list_all(self):
        return session.query(AccountModel).all()

