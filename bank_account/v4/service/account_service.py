from bank_account.v4.domain.events import CreateAccount, DepositMade, WithdrawalMade
from bank_account.v4.domain.aggregates import AccountAggregate


class AccountService:
	def __init__(self, repository, projection_manager):
		self.repository = repository
		self.projection_manager = projection_manager

	def create_account(self, account_id):
		event = CreateAccount(account_id)
		self.repository.save(event)
		self.projection_manager.project(event)

	def deposit(self, account_id, amount):
		event = DepositMade(account_id, amount)
		self.repository.save(event)
		self.projection_manager.project(event)

	def withdraw(self, account_id, amount):
		account = self.repository.load(account_id)
		if account.balance < amount:
			raise ValueError("Insufficient balance")
		event = WithdrawalMade(account_id, amount)
		self.repository.save(event)
		self.projection_manager.project(event)

	def get_account_summary(self, account_id):
		account = self.repository.load(account_id)
		return str(account)