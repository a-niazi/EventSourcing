from bank_account_v1.events.account_events import DepositMade, WithdrawalMade, AccountBlocked
from bank_account_v1.infrastructure import event_store


class Account:
	def __init__(self, account_id):
		self.account_id = account_id
		self.balance = 0.0
		self.blocked = False
		self.version = 0

	def apply(self, event):
		if isinstance(event, DepositMade):
			self.balance += event.amount
		elif isinstance(event, WithdrawalMade):
			if self.balance < event.amount:
				raise ValueError("Insufficient funds")
			self.balance -= event.amount
		elif isinstance(event, AccountBlocked):
			self.blocked = True

	def deposit(self, amount: float):
		if self.blocked:
			raise ValueError("Account is blocked")
		event = DepositMade(amount)
		self.apply(event)
		return event

	def withdraw(self, amount: float):
		if self.blocked:
			raise ValueError("Account is blocked")
		event = WithdrawalMade(amount)
		self.apply(event)
		return event

	def block_account(self):
		event = AccountBlocked()
		self.apply(event)
		return event

	@classmethod
	def reconstruct(cls, account_id, event_store):
		account = cls(account_id)
		events = event_store.get_events(account_id)
		for event in events:
			account.apply(event)
		return account
