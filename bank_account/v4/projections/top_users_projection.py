from bank_account.v4.projections.base_projection import BaseProjection
from bank_account.v4.domain.events import DepositMade, WithdrawalMade


class TopUsersProjection(BaseProjection):
    def __init__(self):
        self.user_balances = {}

    def project(self, event):
        account_id = event.account_id
        if isinstance(event, DepositMade):
            self.user_balances[account_id] = self.user_balances.get(account_id, 0) + event.amount
        elif isinstance(event, WithdrawalMade):
            self.user_balances[account_id] = self.user_balances.get(account_id, 0) - event.amount

    def get_top_users(self, top_n=5):
        return sorted(self.user_balances.items(), key=lambda x: x[1], reverse=True)[:top_n]

