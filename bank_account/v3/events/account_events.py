from datetime import datetime


class Base:
	def __init__(self, entity_id: int):
		self.entity_id = entity_id
		self.type = None
		self.version = 0
		self.timestamp = datetime.now()
		self.version = self.version + 1


class AccountCreated(Base):
	def __init__(self, entity_id: int):
		super().__init__(entity_id)
		self.type = "AccountCreated"


class DepositMade(Base):
	def __init__(self, entity_id: int, amount: float):
		super().__init__(entity_id)
		self.amount = amount
		self.type = "DepositMade"


class WithdrawalMade(Base):
	def __init__(self, entity_id: int, amount: float):
		super().__init__(entity_id)
		self.amount = amount
		self.type = "WithdrawalMade"


class AccountBlocked(Base):
	def __init__(self, entity_id: int):
		super().__init__(entity_id)
		self.type = "AccountBlocked"
