from bank_account.v2.events.account_events import DepositMade, WithdrawalMade


class TotalInventoryProjection:
	def __init__(self):
		self.inventory = 0

	def apply(self, event: DepositMade | WithdrawalMade):
		if event.type == "DepositMade":
			self.inventory += event.amount
		elif event.type == "WithdrawalMade":
			self.inventory -= event.amount

	def get_total_inventory(self):
		return self.inventory
