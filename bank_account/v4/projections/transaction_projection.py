from bank_account.v4.projections.base_projection import BaseProjection


class TransactionProjection(BaseProjection):
    def __init__(self):
        self.transactions = []

    def project(self, event):
        self.transactions.append(event)

    def get_transactions(self):
        return self.transactions
