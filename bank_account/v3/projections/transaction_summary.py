
class TransactionSummaryProjection:
    def __init__(self):
        self.total_deposits = 0.0
        self.total_withdrawals = 0.0
        self.transaction_count = 0

    def apply(self, event):
        if event.type == "DepositMade":
            self.total_deposits += event.amount
        elif event.type == "WithdrawalMade":
            self.total_withdrawals += event.amount
        self.transaction_count += 1

    def get_summary(self):
        return {
            "total_deposits": self.total_deposits,
            "total_withdrawals": self.total_withdrawals,
            "transaction_count": self.transaction_count,
        }
