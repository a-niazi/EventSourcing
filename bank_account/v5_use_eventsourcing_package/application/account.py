from uuid import UUID
from decimal import Decimal
from ..aggregates.account import BankAccount
from eventsourcing.application import Application, AggregateNotFound
from ..projections.total_balance_projection import BalanceProjection
from ..exceptions import *


class AccountApplication(Application):
	def __init__(self, env=None):
		super().__init__(env)
		self.balance_projection = BalanceProjection()

	def create_account(self, full_name: str):
		account = BankAccount(full_name)
		event = self.save(account)
		self._project_events([event[0].domain_event])
		return account

	def get_account(self, account_id: UUID) -> BankAccount:
		try:
			aggregate = self.repository.get(account_id)
		except AggregateNotFound:
			raise AccountNotFoundException(account_id)
		return aggregate

	def deposit(self, account_id: UUID, amount: float):
		account = self.repository.get(account_id)
		account.deposit(amount)
		event = self.save(account)
		self._project_events([event[0].domain_event])

	def withdraw(self, account_id: UUID, amount: float):
		account = self.repository.get(account_id)
		account.withdraw(amount)
		event = self.save(account)
		self._project_events([event[0].domain_event])

	def block_account(self, account_id: UUID):
		account = self.repository.get(account_id)
		account.block()
		event = self.save(account)
		self._project_events([event[0].domain_event])

	def get_balance(self, account_id: UUID) -> object:
		for event in self.repository.event_store.get(account_id):
			self.balance_projection.process_event(event)
		return {"balance": self.balance_projection.total_balance}

	def _project_events(self, events):
		for event in events:
			self.balance_projection.process_event(event)
