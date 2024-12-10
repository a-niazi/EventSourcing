class DepositMade:
    def __init__(self, amount: float):
        self.amount = amount
        self.type = "DepositMade"


class WithdrawalMade:
    def __init__(self, amount: float):
        self.amount = amount
        self.type = "WithdrawalMade"


class AccountBlocked:
    def __init__(self):
        self.type = "AccountBlocked"
