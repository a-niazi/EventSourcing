from ..aggregates.account import BankAccount


class BalanceProjection:
	"""
		Projection to calculate total balance across all accounts.
	"""

	def __init__(self):
		self.total_balance = 0
		self.account_balances = {}

	def process_event(self, domain_event):
		if str(type(domain_event)) == str(BankAccount.Created):
			self.account_balances[domain_event.originator_id] = 0
		elif str(type(domain_event)) == str(BankAccount.MoneyDeposited):
			self.total_balance += domain_event.amount
			self.account_balances[domain_event.originator_id] += domain_event.amount
		elif str(type(domain_event)) == str(BankAccount.MoneyWithdrawn):
			self.total_balance -= domain_event.amount
			self.account_balances[domain_event.originator_id] -= domain_event.amount

