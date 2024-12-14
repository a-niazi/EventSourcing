# application/service.py
from bank_account.v3.aggregates.account import Account
from bank_account.v3.application.event_handler import EventHandler
from bank_account.v3.projections import TopUsersProjection, \
	TransactionSummaryProjection, \
	MonthlyTransactionSummaryProjection, \
	TransactionTypePercentageProjection, \
	TotalInventoryProjection


class AccountService:
	def __init__(self, event_store):
		self.event_store = event_store
		self.account_aggregate = Account()
		self.projections = [
			TopUsersProjection(),
			TotalInventoryProjection(),
			TransactionSummaryProjection(),
			MonthlyTransactionSummaryProjection(),
			TransactionTypePercentageProjection()
		]
		self.event_handler = EventHandler(self.account_aggregate, self.projections)

	def deposit(self, account_id, amount):
		event = self.account_aggregate.deposit(account_id, amount)
		self.event_store.append(event)
		self.event_handler.handle_event(event)

	def withdraw(self, account_id, amount):
		event = self.account_aggregate.withdraw(account_id, amount)
		self.event_store.append(event)
		self.event_handler.handle_event(event)

	def get_monthly_summary(self):
		for projection in self.projections:
			if isinstance(projection, MonthlyTransactionSummaryProjection):
				return projection.get_monthly_summary()

	def get_top_users(self, n=5):
		for projection in self.projections:
			if isinstance(projection, TopUsersProjection):
				return projection.get_top_users(n)

	def get_total_inventory(self):
		for projection in self.projections:
			if isinstance(projection, TotalInventoryProjection):
				return projection.get_total_inventory()
