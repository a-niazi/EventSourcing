from bank_account.v2.events.account_events import DepositMade, WithdrawalMade

class TransactionTypePercentageProjection:
	def __init__(self):
		self.total_count = 0
		self.type_counts = {"DepositMade": 0, "WithdrawalMade": 0}

	def apply(self, event: DepositMade | WithdrawalMade):
		if event.type in self.type_counts:
			self.type_counts[event.type] += 1
			self.total_count += 1

	def get_type_percentage(self):
		if self.total_count <= 0:
			return 0
		return {event_type: (count / self.total_count * 100) for event_type, count in self.type_counts.items()}
