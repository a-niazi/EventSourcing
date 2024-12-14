from bank_account.v4.domain.events import DepositMade, WithdrawalMade


class AccountAggregate:
    def __init__(self, account_id):
        self.account_id = account_id
        self.balance = 0

    def apply(self, event):
        if isinstance(event, DepositMade):
            self.balance += event.amount
        elif isinstance(event, WithdrawalMade):
            if self.balance < event.amount:
                raise ValueError("Insufficient balance")
            self.balance -= event.amount

    def __str__(self):
        return f"Account({self.account_id}, Balance: {self.balance})"
