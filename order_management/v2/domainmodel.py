from eventsourcing.domain import Aggregate, event
from exception import InvalidOperationError


class Order(Aggregate):
	# @event('Registered')
	def __init__(self):
		super().__init__()
		self.items = []
		self.status = "Pending"
		self.total_price = 0.0

	class ItemAdded(Aggregate.Event):
		item_name: str
		price: float
		quantity: int

	def add_item(self, item_name: str, price: float, quantity: int):
		if quantity <= 0 or price <= 0:
			raise InvalidOperationError("Price and quantity must be positive.")
		self._add_item(item_name, price, quantity)

	#@event('TrickAdded')
	@event(ItemAdded)
	def _add_item(self, item_name: str, price: float, quantity: int):
		self.items.append({"item_name": item_name, "price": price, "quantity": quantity})
		self.total_price += price * quantity
