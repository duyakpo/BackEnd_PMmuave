from infrastructure.repositories.account_repositories import AccountRepository

class AccountService:
    def __init__(self):
        self.repo = AccountRepository()

    def create_account(self, data):
        return self.repo.create(data)

    def login(self, data):
        account = self.repo.get_by_email(data.get("email"))
        if account and account.password == data.get("password"):
            return account
        return None

    def get_me(self, ma_user: str):
        return self.repo.get_by_ma_user(ma_user)

    def update_me(self, ma_user: str, data):
        return self.repo.update_by_ma_user(ma_user, data)

    # Admin/Operator
    def list_users(self):
        return self.repo.list_all()

    def update_role(self, ma_user, vai_tro):
        account = self.repo.get_by_ma_user(ma_user)
        if not account:
            return None
        account.vai_tro = vai_tro
        return account
