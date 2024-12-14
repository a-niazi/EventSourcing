class Event:
	def __init__(self, account_id):
		self.account_id = account_id


class CreateAccount(Event):
	def __init__(self, account_id):
		super().__init__(account_id)


class DepositMade(Event):
	def __init__(self, account_id, amount):
		super().__init__(account_id)
		self.amount = amount


class WithdrawalMade(Event):
	def __init__(self, account_id, amount):
		super().__init__(account_id)
		self.amount = amount
