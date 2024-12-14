from bank_account.v3.aggregates.account import Account


class EventHandler:
	def __init__(self, account_aggregate: Account, projections):
		self.account_aggregate = account_aggregate
		self.projections = projections

	def handle_event(self, event):
		self.account_aggregate.apply(event)

		for projection in self.projections:
			projection.apply(event)
