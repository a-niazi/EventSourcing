from bank_account.v3.events.account_events import DepositMade, WithdrawalMade, AccountBlocked, AccountCreated


class Account:
	def __init__(self):
		self.account_id = None
		self.balance = 0.0
		self.blocked = False
		self.version = 0

	def apply(self, event):
		if isinstance(event, AccountCreated):
			self.account_id = event.account_id
			self.balance = 0.0
		elif isinstance(event, DepositMade):
			self.balance += event.amount
		elif isinstance(event, WithdrawalMade):
			if self.balance < event.amount:
				raise ValueError("Insufficient funds")
			self.balance -= event.amount
		elif isinstance(event, AccountBlocked):
			self.blocked = True

	def create_account(self, account_id):
		"""Creates a new account and returns the corresponding event."""
		if self.account_id is not None:
			raise ValueError("Account already exists.")
		event = AccountCreated()
		self.apply(event)
		return event

	def deposit(self, account_id, amount):
		"""Processes a deposit and returns the corresponding event."""
		if self.blocked:
			raise ValueError("Account is blocked")
		# if self.account_id != account_id:
		# 	raise ValueError("Account ID does not match.")
		if amount <= 0:
			raise ValueError("Deposit amount must be greater than zero.")
		event = DepositMade(entity_id=account_id, amount=amount)
		self.apply(event)
		return event

	def withdraw(self, account_id, amount):
		"""Processes a withdrawal and returns the corresponding event."""
		# if self.account_id != account_id:
		# 	raise ValueError("Account ID does not match.")
		if amount <= 0:
			raise ValueError("Withdrawal amount must be greater than zero.")
		if self.balance < amount:
			raise ValueError("Insufficient balance.")
		event = WithdrawalMade(entity_id=account_id, amount=amount)
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

	def create_snapshot(self):
		return {
			"account_id": self.account_id,
			"balance": self.balance,
			"blocked": self.blocked,
			"version": self.version,
		}

	@classmethod
	def reconstruct_from_snapshot(cls, snapshot, event_store):
		account = cls(snapshot["account_id"])
		account.balance = snapshot["balance"]
		account.blocked = snapshot["blocked"]
		account.version = snapshot["version"]

		# replay events after snapshot
		events = event_store.get_events(account.account_id)
		for event in events[account.version:]:
			account.apply(event)
		return account