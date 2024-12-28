from eventsourcing.domain import Aggregate, event
from ..exceptions import *


class BankAccount(Aggregate):
	def __init__(self, owner_name):
		self.owner_name = owner_name
		self.balance = 0
		self.blocked = False

# class BankAccount(Aggregate):
# 	owner_name = None
# 	balance = 0
# 	blocked = False

	# def __init__(self):
	# 	super().__init__()

	# class AccountCreated(Aggregate.Event):
	# 	full_name: str
	#
	# @event(AccountCreated)
	# def create_account(self, full_name: str):
	# 	self.owner_name = full_name
	# 	self.balance = 0
	# 	self.blocked = False

	class MoneyDeposited(Aggregate.Event):
		amount: float

	@event(MoneyDeposited)
	def deposit(self, amount: float):
		self.check_account_is_not_closed()
		self.balance += amount

	class MoneyWithdrawn(Aggregate.Event):
		amount: float

	@event(MoneyWithdrawn)
	def withdraw(self, amount: float):
		self.check_account_is_not_closed()
		self.check_has_sufficient_funds(amount)
		self.balance -= amount

	@event("AccountBlocked")
	def block(self):
		self.blocked = True

	def check_account_is_not_closed(self) -> None:
		if self.blocked:
			raise AccountBlockedException({"account_id": self.id})

	def check_has_sufficient_funds(self, amount: float) -> None:
		if self.balance < amount:
			raise InsufficientFundsException({"account_id": self.id})

	def get_events(self):
		return self.collect_events()


