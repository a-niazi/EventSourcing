from bank_account.v2.events.account_events import DepositMade, WithdrawalMade
from collections import Counter


class TopUsersProjection:

	def __init__(self):
		self.user_transactions = Counter()

	def apply(self, event: DepositMade | WithdrawalMade):
		self.user_transactions[event.entity_id] += 1

	def get_top_users(self, n=5):
		return self.user_transactions.most_common(n)
