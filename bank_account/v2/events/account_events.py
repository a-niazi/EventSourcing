from datetime import datetime


class DepositMade:
    def __init__(self, amount: float):
        self.amount = amount
        self.type = "DepositMade"
        self.timestamp = datetime.now()


class WithdrawalMade:
    def __init__(self, amount: float):
        self.amount = amount
        self.type = "WithdrawalMade"
        self.timestamp = datetime.now()


class AccountBlocked:
    def __init__(self):
        self.type = "AccountBlocked"
        self.timestamp = datetime.now()
